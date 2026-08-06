# Task Brief

## Your role

You are the Evidence Review Analyst assigned to perform a read-only documentary closure review. You may analyze and recommend. You may not approve closure, accept risk, make legal determinations, execute remediation, or change production.

## Assignment

Review the submitted remediation evidence and issue-closure artifacts against the documented closure requirements. Determine whether the package is ready for authorized closure consideration, conditionally ready, not ready, or unable to conclude.

## Materials provided

- `inputs/01-issue-record.md`
- `inputs/02-closure-requirements.csv`
- `inputs/03-remediation-action-plan.md`
- `inputs/04-closure-submission.md`
- `inputs/05-evidence-inventory.csv`
- `inputs/06-change-record.md`
- `inputs/07-post-change-sample-test.md`
- `inputs/08-monitoring-report.csv`
- `inputs/09-management-representation.md`
- `inputs/10-approval-history.csv`
- `inputs/11-account-removal-record.md`

The evidence inventory lists EV-01 and EV-08, but the referenced procedure files are not supplied. Treat the inventory metadata as a submitted claim only. Do not infer or reconstruct the contents of those unavailable artifacts.

## Required tools

- Spreadsheet editor for CSV review and workpaper preparation.
- Document editor for the closure-readiness memo.

Accepted equivalents are permitted. Optional scripts may be used for duplicate detection, date comparison, or traceability checks, but no automation result may be accepted without verification.

## Required deliverables

| Deliverable | Format | Required contents |
| --- | --- | --- |
| Evidence-to-requirement review workpaper | CSV or spreadsheet | Requirement ID, expected evidence, artifact, date, owner/source, relevance, completeness, reliability concern, coverage, observation, disposition, follow-up, traceability reference |
| Evidence deficiency register | CSV or spreadsheet | Deficiency ID, affected requirement, gap or contradiction, impact, blocking treatment, follow-up, fictional owner, unresolved authority question, status |
| Closure-readiness memo | Markdown or document | Scope, materials reviewed, facts, assumptions, findings, unresolved questions, evidence-sufficiency conclusion, recommendation, additional evidence request, reserved decisions |

Templates are provided in `templates/`. Equivalent formats are accepted when all required fields remain reviewable.

## Required distinctions

The submission must separate case facts, assumptions, unsupported or missing information, findings, recommendations, and decisions reserved for authorized roles.

## Assumption rules

### Permitted assumptions

- UTC and local timestamps that differ by exactly one hour refer to the same deployment event when all other identifiers match.
- CSV row order has no evidentiary significance.
- File names are labels; artifact identity must be established using identifiers, dates, versions, hashes, availability, and content actually supplied.

Each assumption used must be stated. None may replace material evidence.

### Prohibited assumptions

The learner must not:

- invent missing evidence, approvals, dates, owners, criteria, or system state;
- infer the contents of EV-01, EV-08, or any unavailable artifact from inventory metadata alone;
- assume implementation proves operating effectiveness;
- treat management representation as independent verification;
- assume a missing approval is harmless;
- treat an unavailable or unlisted artifact as reviewed;
- change the documented closure requirements;
- infer final closure, risk-acceptance, legal, sign-off, or production authority;
- conclude remediation effectiveness from this documentary package.

### When evidence is insufficient

1. Identify the specific gap, contradiction, or ambiguous criterion.
2. Explain its impact on the closure-readiness judgment.
3. Request the exact evidence or authorized clarification needed.
4. Use a conditional recommendation or escalation rather than unsupported certainty.

## Included scope

- Evidence inventory and traceability review.
- Relevance, completeness, freshness, consistency, availability, and reliability checks.
- Identification and prioritization of deficiencies.
- Closure-readiness recommendation.

## Excluded scope

- Final closure or exception approval.
- Residual-risk acceptance.
- Legal or regulatory determination.
- Remediation execution or production change.
- Root-cause resolution testing or sustained effectiveness validation.
- Changing issue status in the system of record.

## Submission requirements

- Use requirement and artifact identifiers exactly as supplied.
- Cite input file names and relevant row or section references.
- Distinguish inventory metadata from artifact content actually reviewed.
- Reconcile the workpaper, deficiency register, and memo; material conclusions must not conflict.
- State whether each deficiency is blocking, potentially blocking pending clarification, or non-blocking.
- End the memo with: `This recommendation is not final issue-closure approval.`

## Use of AI or automation

AI or automation may assist with read-only extraction, date checks, duplicate detection, traceability, and drafting. The learner remains responsible for verifying facts, calculations, citations, evidence availability, and authority boundaries.

## Completion condition

Submit all three deliverables. A forced final approval decision is not required when evidence is insufficient.
