def qualify_lead(lead: dict) -> dict:
    company = lead["company"].strip().lower()
    source = lead["source"].strip().lower()

    if company and source == "linkedin":
        return {
            "qualification": "qualified",
            "score": 80
        }

    if company:
        return {
            "qualification": "manual_review",
            "score": 50
        }

    return {
        "qualification": "not_qualified",
        "score": 20
    }