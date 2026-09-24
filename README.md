# CRM Workflow Orchestrator

A portfolio implementation demonstrating auditable CRM workflow orchestration with FastAPI.

The project shows how incoming leads move through a structured workflow including validation, normalization, deduplication, qualification, routing, human review, CRM actions, retry logic, exception handling and audit logging.

## Workflow

Lead Intake  
→ Validation  
→ Normalization  
→ Deduplication  
→ Qualification  
→ Routing  
→ Human Review  
→ CRM Action  
→ Audit Log

## Failure Handling

CRM Action  
→ Retry  
→ Exception Queue  
→ Human Review  
→ Audit Log

## Features

- FastAPI REST API
- Pydantic validation
- Lead normalization
- Duplicate detection
- Qualification logic
- Routing logic
- Human in the Loop review
- Retry handling
- Exception queue
- Audit logging
- Automated tests

## Example Flow

A qualified LinkedIn lead can be routed to the sales pipeline.

A lead requiring manual review is routed to a human review step before further processing.

A simulated CRM failure is retried three times and then moved to an exception queue.

## Tech Stack

- Python 3.11
- FastAPI
- Pydantic
- Pytest
- REST APIs

## API

### POST /leads

Example request:

```json
{
  "first_name": "Anna",
  "last_name": "Meyer",
  "email": "anna@example.com",
  "company": "Example GmbH",
  "source": "linkedin"
}

Tests

Run:

python -m pytest

Current test coverage includes:

normalization
qualification
routing
Project Structure
app/
├── main.py
├── schemas.py
├── services/
│   ├── normalization.py
│   ├── deduplication.py
│   ├── qualification.py
│   ├── routing.py
│   ├── audit.py
│   └── exceptions.py
└── human_review/
    └── review.py

tests/
└── test_workflow.py
Production Scope

This repository is a portfolio implementation.

Certain production integrations, credentials, proprietary business logic and internal orchestration mechanisms are intentionally excluded.

Production repositories are maintained privately.