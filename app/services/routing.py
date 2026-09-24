def route_lead(qualification: dict) -> dict:
    status = qualification["qualification"]

    if status == "qualified":
        return {
            "route": "sales_pipeline",
            "action": "send_to_crm"
        }

    if status == "manual_review":
        return {
            "route": "human_review",
            "action": "wait_for_review"
        }

    return {
        "route": "nurture",
        "action": "no_immediate_sales_action"
    }