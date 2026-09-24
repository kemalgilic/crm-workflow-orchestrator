from app.services.normalization import normalize_lead
from app.services.qualification import qualify_lead
from app.services.routing import route_lead
from app.schemas import LeadCreate


def test_normalization():
    lead = LeadCreate(
        first_name="  ANNA  ",
        last_name="  MEYER  ",
        email="ANNA@EXAMPLE.COM",
        company="  Example GmbH  ",
        source="  LinkedIn  "
    )

    result = normalize_lead(lead)

    assert result["first_name"] == "Anna"
    assert result["last_name"] == "Meyer"
    assert result["email"] == "anna@example.com"
    assert result["company"] == "Example GmbH"
    assert result["source"] == "linkedin"


def test_qualification():
    lead = {
        "first_name": "John",
        "last_name": "Smith",
        "email": "john@example.com",
        "company": "Acme Inc",
        "source": "linkedin"
    }

    result = qualify_lead(lead)

    assert result["qualification"] == "qualified"
    assert result["score"] == 80


def test_routing():
    qualification = {
        "qualification": "manual_review",
        "score": 50
    }

    result = route_lead(qualification)

    assert result["route"] == "human_review"
    assert result["action"] == "wait_for_review"