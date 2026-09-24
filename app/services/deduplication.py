seen_emails = set()


def is_duplicate(email: str) -> bool:
    normalized_email = email.strip().lower()

    if normalized_email in seen_emails:
        return True

    seen_emails.add(normalized_email)
    return False