# Change Record CR-7751

- Change title: Enforce dual approval before FleetOps privileged-access fulfillment
- Production environment: FleetOps
- Implementation status: Completed
- Deployment timestamp: 2026-05-20 23:48 UTC
- Local console timestamp: 2026-05-21 00:48 UTC+01:00
- Implementer: FleetOps Platform Team
- Change approver: Lena Ortiz, FleetOps Platform Owner
- Rollback plan: Restore workflow configuration package 4.8.2
- Configuration package: 4.9.0

## Implemented rule

A request cannot enter `Ready for Fulfillment` until both `Manager Approval` and `Application Owner Approval` fields contain approved records.

## Validation attached to the change

A deployment smoke test confirmed the workflow loaded and a test ticket could not progress with both approval fields blank. No population-level operating test is attached to this change record.
