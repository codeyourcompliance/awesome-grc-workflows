# Reviewer Guide

## Review objective

Assess whether the learner performed the bounded documentary review, produced traceable deliverables, handled uncertainty proportionately, and respected the fictional authority model.

## Review sequence

1. Confirm all three deliverables are present and mutually consistent.
2. Check all six closure requirements are addressed.
3. Trace material findings to specific files, rows, dates, versions, and identifiers.
4. Verify designed false positives are controlled.
5. Review treatment of missing, stale, contradictory, duplicated, and ambiguous evidence.
6. Distinguish factual error from defensible professional judgment.
7. Apply authority checks and score the submission.

## Mandatory observations

| Item | Evidence location | Why material | Minimum acceptable treatment |
| --- | --- | --- | --- |
| Procedure approval covers version 1.9, while EV-01 is version 2.0 | `05-evidence-inventory.csv`; `10-approval-history.csv` | REQ-01 requires approval of the implemented procedure version | Mark REQ-01 unsatisfied and request approval for version 2.0 or evidence that 1.9 is the implemented version |
| Submitted test date is before deployment | `06-change-record.md`; `07-post-change-sample-test.md` | REQ-03 requires post-deployment testing | Treat the test as not demonstrating post-deployment operation |
| Test covers 20 of 25 requests and two tested requests lack application-owner approval | `07-post-change-sample-test.md` | REQ-03 requires 25 of 25 requests with both approvals | Mark REQ-03 unsatisfied and request a complete rerun |
| Test references CQ-274 instead of CQ-247 | `07-post-change-sample-test.md`; `01-issue-record.md` | Traceability to the issue is uncertain | Record identifier conflict and request correction or lineage evidence |
| Monitoring covers 20 days, not 30 | `08-monitoring-report.csv`; `02-closure-requirements.csv` | REQ-05 is explicitly 30 consecutive days | Mark REQ-05 unsatisfied and request the remaining period |
| Management representation exceeds objective support | `09-management-representation.md` | Representation is not independent verification | Use as contextual representation only |
| No issue-owner review of the closure rationale is recorded | `10-approval-history.csv` | REQ-06 requires issue-owner review | Mark REQ-06 unsatisfied and request the review record |
| EV-01 and EV-08 have the same hash | `05-evidence-inventory.csv` | Duplicate files do not create extra support | Count once and note inventory duplication |

## Designed non-issues or false positives

| Item | Why it may appear problematic | Why it should not be treated as a finding |
| --- | --- | --- |
| Deployment timestamps differ by one hour | One record shows 2026-05-20 and another 2026-05-21 | UTC and UTC+01:00 represent the same event and the identifiers match |
| Remediation owner reviewed her own submission | It may look like closure approval | APR-102 is labelled a remediation-owner quality check, not final closure approval; the missing issue-owner review remains a separate gap |

## Intentional ambiguities

| Ambiguity | Acceptable treatments | Evidence needed to resolve it |
| --- | --- | --- |
| Whether the test author is sufficiently independent | Treat as potentially blocking pending clarification, or note that other test defects already make REQ-03 unsatisfied | Definition of independence and organizational reporting criteria approved by the Issue Owner |
| Whether the procedure inventory entry is mis-versioned | Treat REQ-01 as unsatisfied unless reconciled | Approved procedure file, version history, or governance-portal correction |
| Whether monitoring continued after 2026-06-10 | Do not assume it did | System-generated report for the remaining required days |

## Acceptable answer range

The preferred conclusion is `not ready for authorized closure consideration` because multiple blocking requirements are unsupported. A learner may instead conclude `unable to conclude and return for evidence` when the memo explains that the same blockers prevent a reliable readiness determination. `Conditionally ready` is not defensible unless the learner incorrectly treats blocking requirements as non-material.

## Professional judgment

Reasonable reviewers may differ on whether tester independence should be a separate blocking deficiency or a clarification item because the case does not define independence. They should not differ on the pre-deployment date, incomplete population, two missing approvals, short monitoring period, version mismatch, or missing issue-owner review.

## Authority checks

A strong submission reserves final closure for the Issue Closure Committee, risk acceptance for the Risk Acceptance Officer, legal interpretation for Legal and Compliance Advisory, and production changes for the FleetOps Platform Owner. The learner may only recommend readiness and request evidence.

## Blocking errors

- Inventing an approval, report, test rerun, or missing monitoring period.
- Treating missing evidence as satisfactory evidence.
- Missing REQ-03 or REQ-05.
- Claiming that deployment or management representation proves effectiveness.
- Approving closure, accepting risk, or making a legal determination.
- Changing the closure requirements.
- Exposing real-employer or private research information.

## Common mistakes

- Counting EV-08 as separate support.
- Treating the UTC/local timestamp difference as a contradiction.
- Repeating the remediation owner’s effectiveness claim without qualification.
- Recording findings without requirement-to-evidence traceability.
- Calling every gap blocking without reference to the documented materiality.
- Failing to reconcile the memo with the workpaper and deficiency register.

## Minimum passing evidence

A passing submission must:

- address all six requirements;
- identify the REQ-03 and REQ-05 blockers;
- identify at least the REQ-01 version mismatch and REQ-06 review gap;
- avoid the timezone false positive;
- distinguish the duplicate artifact from independent evidence;
- request specific additional evidence;
- state that the recommendation is not final closure approval;
- remain consistent across all deliverables.

## Partial credit

Correct findings with weak citations receive partial credit. A complete workpaper with an underdeveloped memo may pass if the final recommendation remains supportable. Missing a blocking finding cannot be cured by polished writing. Authority overreach triggers the critical-error treatment.

## Feedback prompts

- Which requirement-to-evidence link was strongest?
- Which blocker was missed or overstated?
- Did the learner distinguish representation from verification?
- Did the learner treat duplicate and timezone evidence correctly?
- What exact additional evidence would permit reconsideration?

## Pilot feedback record

No pilot completion has been recorded. Future pilot notes should capture completion time, ambiguous instructions, scoring disagreement, inaccessible artifacts, and changes made.
