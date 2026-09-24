from datetime import datetime, timezone


def create_audit_event(
    event: str,
    lead: dict,
    details: dict | None = None
) -> dict:
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event": event,
        "lead_email": lead["email"],
        "details": details or {}
    }