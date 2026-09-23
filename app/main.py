from fastapi import FastAPI

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