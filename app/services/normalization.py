from app.schemas import LeadCreate


def normalize_lead(lead: LeadCreate) -> dict:
    return {
        "first_name": lead.first_name.strip().title(),
        "last_name": lead.last_name.strip().title(),
        "email": str(lead.email).strip().lower(),
        "company": lead.company.strip(),
        "source": lead.source.strip().lower(),
    }