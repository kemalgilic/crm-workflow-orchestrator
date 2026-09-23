\# CRM Workflow Orchestrator



A portfolio implementation demonstrating auditable CRM workflow orchestration with FastAPI.



The project shows how incoming leads can move through a structured workflow including normalization, deduplication, qualification, routing, human review, CRM updates, follow up logic and audit tracking.



\## Planned Workflow



Lead Intake  

→ Normalize  

→ Dedupe  

→ Source of Truth  

→ CRM Upsert  

→ Qualification  

→ Routing  

→ Human Review  

→ CRM Update  

→ Follow Up  

→ Audit Log



\## Failure Handling



Retry  

→ Exception Queue  

→ Human Review



\## Tech Stack



\- Python

\- FastAPI

\- REST APIs

\- Human in the Loop

\- Workflow Orchestration

\- Audit Logging

\- Structured Error Handling



\## Current Status



Initial FastAPI service is running with basic health endpoints.



More workflow components will be added incrementally.



\## Production Scope



This repository is a portfolio implementation.



Certain production components, integrations, credentials, proprietary business logic and internal orchestration mechanisms are intentionally excluded.



Production repositories are maintained privately.

