# Reviewer Guide

## Review objective

Assess whether the learner performed the bounded documentary review, produced traceable deliverables, handled uncertainty proportionately, and respected the fictional authority model.

## Review sequence

1. Confirm all three deliverables are present and mutually consistent.
2. Check all six closure requirements are addressed.
3. Trace material findings to specific files, rows, dates, versions, availability states, and identifiers.
4. Verify designed false positives are controlled.
5. Review treatment of missing, stale, contradictory, duplicated, unavailable, and ambiguous evidence.
6. Distinguish factual error from defensible professional judgment.
7. Apply authority checks and score the submission.

## Mandatory observations

| Item | Evidence location | Why material | Minimum acceptable treatment |
| --- | --- | --- | --- |
| EV-01 and EV-08 are listed but not supplied; inventory claims version 2.0 while approval covers version 1.9 | `05-evidence-inventory.csv`; `10-approval-history.csv`; `inputs/README.md` | REQ-01 requires the actual approved procedure matching the implemented workflow | Mark REQ-01 unsatisfied; request the actual procedure and matching approval or reconciled version history; do not infer artifact contents from metadata |
| Submitted test date is before deployment | `06-change-record.md`; `07-post-change-sample-test.md` | REQ-03 requires post-deployment testing | Treat the test as not demonstrating post-deployment operation |
| Test covers 20 of 25 requests and two tested requests lack application-owner approval | `07-post-change-sample-test.md` | REQ-03 requires 25 of 25 requests with both approvals | Mark REQ-03 unsatisfied and request a complete rerun |
| Test references CQ-274 instead of CQ-247 | `07-post-change-sample-test.md`; `01-issue-record.md` | Traceability to the issue is uncertain | Record identifier conflict and request correction or lineage evidence |
| Monitoring covers 20 days, not 30 | `08-monitoring-report.csv`; `02-closure-requirements.csv` | REQ-05 is explicitly 30 consecutive days | Mark REQ-05 unsatisfied and request the remaining period |
| Management representation exceeds objective support | `09-management-representation.md` | Representation is not independent verification | Use as contextual representation only |
| No issue-owner review of the closure rationale is recorded | `10-approval-history.csv` | REQ-06 requires issue-owner review | Mark REQ-06 unsatisfied and request the review record |
| EV-01 and EV-08 have the same claimed hash | `05-evidence-inventory.csv` | Duplicate inventory references do not create independent support, especially when files are unavailable | Do not count as corroboration; request the actual artifact and correct the inventory |

## Designed non-issues or false positives

| Item | Why it may appear problematic | Why it should not be treated as a finding |
| --- | --- | --- |
| Deployment timestamps differ by one hour | One record shows 2026-05-20 and another 2026-05-21 | UTC and UTC+01:00 represent the same event and the identifiers match |
| Remediation owner reviewed her own submission | It may look like closure approval | APR-102 is labelled a remediation-owner quality check, not final closure approval; the missing issue-owner review remains a separate gap |

## Intentional ambiguities

| Ambiguity | Acceptable treatments | Evidence needed to resolve it |
| --- | --- | --- |
| Whether the test author is sufficiently independent | Treat as potentially blocking pending clarification, or note that other test defects already make REQ-03 unsatisfied | Definition of independence and organizational reporting criteria approved by the Issue Owner |
| Whether the procedure inventory entries are accurate | Treat REQ-01 as unsatisfied because the files are unavailable and the claimed version conflicts with approval history | Actual procedure file, approved version history, or governance-portal correction |
| Whether monitoring continued after 2026-06-10 | Do not assume it did | System-generated report for the remaining required days |

## Acceptable answer range

The preferred conclusion is `not ready for authorized closure consideration` because multiple blocking requirements are unsupported. A learner may instead conclude `unable to conclude and return for evidence` when the memo explains that the same blockers prevent a reliable readiness determination. `Conditionally ready` is not defensible unless the learner incorrectly treats blocking requirements as non-material.

## Professional judgment

Reasonable reviewers may differ on whether tester independence should be a separate blocking deficiency or a clarification item because the case does not define independence. They should not differ on the unavailable procedure evidence and version conflict, pre-deployment date, incomplete population, two missing approvals, short monitoring period, or missing issue-owner review.

## Authority checks

A strong submission reserves final closure for the Issue Closure Committee, risk acceptance for the Risk Acceptance Officer, legal interpretation for Legal and Compliance Advisory, and production changes for the FleetOps Platform Owner. The learner may only recommend readiness and request evidence.

## Blocking errors

- Inventing an approval, unavailable procedure content, report, test rerun, or missing monitoring period.
- Treating inventory metadata as if the underlying artifact was reviewed.
- Treating missing evidence as satisfactory evidence.
- Missing REQ-03 or REQ-05.
- Claiming that deployment or management representation proves effectiveness.
- Approving closure, accepting risk, or making a legal determination.
- Changing the closure requirements.
- Exposing real-employer or private research information.

## Common mistakes

- Treating EV-01 or EV-08 metadata as the contents of a supplied procedure.
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
- identify that the procedure files are unavailable and that the claimed 2.0 version conflicts with the approved 1.9 version;
- identify the REQ-06 review gap;
- avoid the timezone false positive;
- distinguish duplicate inventory claims from independent evidence;
- request specific additional evidence;
- state that the recommendation is not final closure approval;
- remain consistent across all deliverables.

## Partial credit

Correct findings with weak citations receive partial credit. A complete workpaper with an underdeveloped memo may pass if the final recommendation remains supportable. Missing a blocking finding cannot be cured by polished writing. Authority overreach triggers the critical-error treatment.

## Feedback prompts

- Which requirement-to-evidence link was strongest?
- Which blocker was missed or overstated?
- Did the learner distinguish inventory metadata from reviewed artifact content?
- Did the learner distinguish representation from verification?
- Did the learner treat duplicate and timezone evidence correctly?
- What exact additional evidence would permit reconsideration?

## Pilot feedback record

No pilot completion has been recorded. Future pilot notes should capture completion time, ambiguous instructions, scoring disagreement, inaccessible artifacts, and changes made.
