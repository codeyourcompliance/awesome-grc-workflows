# Synthetic Scenario

## Fictional organization

Cedar Quay Transit Cooperative is a fictional regional public-transport operator with 1,800 employees. It operates scheduling, ticketing, fleet-maintenance, and workforce systems. The cooperative uses an internal issue-management process to track control deficiencies and remediation actions.

## Operating context

An internal access-governance review identified that privileged access requests for the FleetOps maintenance platform did not consistently retain manager and application-owner approvals. The remediation owner states that a revised workflow was deployed and the issue is ready for closure.

The issue-management standard requires documentary closure review before the Issue Closure Committee may decide whether to close an issue. Closure review is performed against the requirements recorded in `inputs/02-closure-requirements.csv`.

All dates and records are synthetic. System timestamps are stored in UTC. Cedar Quay operates in UTC+01:00 during the case period.

## Roles and authority

| Fictional role | Responsibility in this case | Explicit authority | Excluded authority |
| --- | --- | --- | --- |
| Maya Chen, Remediation Owner | Supplies the closure package and answers evidence questions | Maintain remediation records and submit evidence | Approve her own closure package or accept residual risk |
| Learner, Evidence Review Analyst | Reviews the package against documented requirements | Analyze, document deficiencies, request evidence, recommend readiness | Final closure, exception approval, risk acceptance, legal determination, production change |
| Omar Reyes, Issue Owner | Owns the issue record and confirms requirement ownership | Clarify issue scope and present the package to the committee | Unilateral risk acceptance outside delegated limits |
| Issue Closure Committee | Makes the separately authorized closure decision | Approve closure, return the package, or escalate within its charter | Modify production or waive legal requirements without authority |
| Priya Nair, Risk Acceptance Officer | Evaluates any proposed residual-risk acceptance | Accept residual risk within delegated authority | Rewrite evidence or approve production changes |
| Legal and Compliance Advisory | Provides interpretation when formally requested | Interpret applicable legal or regulatory obligations | Perform the learner’s evidence review |
| FleetOps Platform Owner | Authorizes production changes | Approve and execute controlled platform changes | Approve issue closure solely because a change was deployed |

## Timeline

| Date | Event |
| --- | --- |
| 2026-04-08 | Issue CQ-247 opened. |
| 2026-04-15 | Remediation action plan approved. |
| 2026-05-20 23:48 UTC | Workflow change recorded as deployed. |
| 2026-05-21 00:48 local | Same deployment displayed in the local service console. |
| 2026-05-24 | Orphan privileged account removal recorded. |
| 2026-06-18 | Closure package submitted. |
| 2026-06-20 | Documentary closure review assigned to the learner. |

## Case facts

- The learner must use the requirements register as the authorized comparison basis.
- A deployment record does not by itself prove sustained operation or remediation effectiveness.
- A management statement is evidence of representation, not independent verification.
- Duplicate files do not provide independent corroboration.
- The one-hour deployment timestamp difference is explained by UTC versus local time.
- Final closure belongs to the Issue Closure Committee.

## Intentional uncertainty

The package contains missing coverage, a test performed before the recorded deployment, inconsistent identifiers, a duplicated artifact, a short monitoring period, and an approval that may apply to the wrong version. The independence requirement for the tester is not fully defined in the supplied standard and may require owner clarification.

## Synthetic disclaimer

> This case uses a fictional organization and synthetic or safely constructed data. It does not represent any named employer’s internal process, systems, controls, authority structure, or records.
