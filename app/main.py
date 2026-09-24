from fastapi import FastAPI

from app.schemas import LeadCreate
from app.services.normalization import normalize_lead
from app.services.deduplication import is_duplicate
from app.services.qualification import qualify_lead
from app.services.routing import route_lead
from app.human_review.review import create_review_item
from app.services.audit import create_audit_event
from app.services.exceptions import run_with_retry, add_to_exception_queue

app = FastAPI(
    title="CRM Workflow Orchestrator",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "service": "crm-workflow-orchestrator",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/leads")
def create_lead(lead: LeadCreate):
    normalized_lead = normalize_lead(lead)

    duplicate = is_duplicate(normalized_lead["email"])

    if duplicate:
        audit = create_audit_event(
            event="duplicate_detected",
            lead=normalized_lead
        )

        return {
            "status": "duplicate",
            "lead": normalized_lead,
            "audit": audit
        }

    qualification = qualify_lead(normalized_lead)
    routing = route_lead(qualification)
    review = create_review_item(normalized_lead, routing)

    def simulated_crm_action():
        if normalized_lead["company"].lower() == "fail corp":
            raise RuntimeError("Simulated CRM connection failure")

        return {
            "crm_status": "updated"
        }

    crm_result = run_with_retry(simulated_crm_action)

    exception_item = None

    if not crm_result["success"]:
        exception_item = add_to_exception_queue(
            normalized_lead,
            crm_result["error"]
        )

    audit = create_audit_event(
        event="lead_processed",
        lead=normalized_lead,
        details={
            "qualification": qualification,
            "routing": routing,
            "human_review": review,
            "crm_result": crm_result,
            "exception": exception_item
        }
    )

    return {
        "status": "received",
        "lead": normalized_lead,
        "qualification": qualification,
        "routing": routing,
        "human_review": review,
        "crm_result": crm_result,
        "exception": exception_item,
        "audit": audit
    }