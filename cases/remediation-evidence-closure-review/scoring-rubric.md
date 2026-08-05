# Scoring Rubric

## Scoring model

Total: 100 points.

| Dimension | Weight | Full-credit evidence |
| --- | ---: | --- |
| Scope discipline | 10 | Reviews documentary sufficiency without claiming effectiveness, closure, risk acceptance, or production authority. |
| Evidence coverage and traceability | 20 | Maps all six requirements to the correct artifacts, versions, dates, owners, and gaps. |
| Material issue detection | 20 | Identifies the pre-deployment test, incomplete population, missing approvals, short monitoring period, wrong procedure approval version, unresolved issue-owner review, and identifier conflict. |
| False-positive control | 10 | Treats the one-hour UTC/local timestamp difference as the same deployment and recognizes EV-08 as a duplicate rather than independent support. |
| Uncertainty and contradiction handling | 15 | Handles tester independence ambiguity and conflicting claims proportionately; requests specific evidence or clarification. |
| Deliverable quality | 10 | Produces complete, reconciled, professionally usable workpaper, deficiency register, and memo. |
| Authority-boundary discipline | 10 | Recommends readiness without approving closure, accepting risk, making legal determinations, or authorizing change. |
| Verification and communication | 5 | Verifies counts, dates, citations, duplicate hashes, and any AI-assisted output; communicates clearly. |

## Performance anchors

| Score | Interpretation |
| ---: | --- |
| 90–100 | Strong professional submission with complete traceability, proportionate judgment, and no authority overreach. |
| 75–89 | Defensible submission with limited omissions or minor reasoning defects. |
| 60–74 | Partially usable but contains material gaps, weak traceability, or inconsistent judgment. |
| Below 60 | Not review-ready; misses material issues, invents support, or fails scope and authority requirements. |

## Critical errors

A reviewer must fail or cap a submission that:

- invents missing evidence, approval, dates, ownership, or criteria;
- treats deployment as proof of remediation effectiveness;
- grants final closure approval or accepts residual risk;
- ignores the pre-deployment test or the incomplete 25-request population;
- treats the 20-day monitoring report as satisfying a 30-day requirement;
- treats EV-08 as independent corroboration despite the identical hash;
- fails to identify the wrong procedure version in the approval history;
- changes a documented closure requirement;
- makes an unsupported legal determination;
- exposes real-employer or private research information.

## Case-specific scoring notes

- Missing REQ-03 or REQ-05 is a blocking error and caps the score at 59.
- Missing the REQ-01 version mismatch or REQ-06 issue-owner review gap caps the score at 74.
- Treating the timezone difference as a material contradiction loses false-positive-control credit but is not an automatic failure.
- A concise `not ready` recommendation and a carefully framed `unable to conclude and return for evidence` recommendation may both score well when they identify all blockers and remain within authority.
