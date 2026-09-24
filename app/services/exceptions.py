exception_queue = []


def run_with_retry(action, max_attempts: int = 3):
    last_error = None

    for attempt in range(1, max_attempts + 1):
        try:
            result = action()

            return {
                "success": True,
                "attempts": attempt,
                "result": result
            }

        except Exception as error:
            last_error = str(error)

    return {
        "success": False,
        "attempts": max_attempts,
        "error": last_error
    }


def add_to_exception_queue(lead: dict, error: str) -> dict:
    item = {
        "lead_email": lead["email"],
        "status": "pending",
        "error": error
    }

    exception_queue.append(item)

    return item