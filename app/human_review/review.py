def create_review_item(lead: dict, routing: dict) -> dict | None:
    if routing["route"] != "human_review":
        return None

    return {
        "review_required": True,
        "status": "pending",
        "reason": "Lead requires manual review before further processing"
    }