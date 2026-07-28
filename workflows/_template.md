---
id: replace-with-workflow-id
title: Replace with workflow title
domains:
  - technology-risk
demand_status: observed
first_observed: YYYY-MM-DD
last_reviewed: YYYY-MM-DD
independent_demand_sources: 1
contextual_sources: 0
challenge_status: none
---

# Workflow title

## Summary

One or two sentences describing the bounded work action and why it exists.

## Observed work task

State the action in operational terms. Separate source wording from the normalized task.

## Required outputs

Label each output as `explicit` or `inferred`.

| Output | Basis | Reasoning |
| --- | --- | --- |
| Output one | explicit / inferred | Why this classification is justified |

## Human and authorization boundary

State the judgment, authorization, approval, risk acceptance, regulatory interpretation, or sign-off that remains with an authorized person or role.

When authority is not established by public evidence, state that uncertainty instead of inventing an owner.

## Typical inputs

- Input or evidence source
- Input or evidence source

## Decision points

- Decision that must be made
- Condition that changes the next step

## Technical capabilities

- Data reconciliation
- Evidence metadata handling
- Relevant platform, scripting, query, or reporting capability

Only include capabilities derived from the workflow. Distinguish technologies explicitly requested by employers from capabilities inferred as implementation options.

## Automation boundary

### Suitable for bounded automation

- Read-only collection
- Normalization
- Comparison
- Completeness or freshness checks
- Exception reporting

### Requires separate authority or control

- Approval or risk acceptance
- Remediation execution
- Regulatory or legal determination
- Production-state change
- Any action whose accountable owner is unresolved

These actions are not declared universally non-automatable. The workflow records that technical execution does not itself create authority or accountability.

## Employer demand evidence

Only qualifying employer demand sources count toward `demand_status`.

| Source | Observed date | Minimal supporting signal | Independence note |
| --- | --- | --- | --- |
| Public employer source URL | YYYY-MM-DD | Short paraphrase or minimal quotation | Original employer, mirror relationship, or related-entity note |

## Contextual evidence

Use this section for practitioner material, standards, regulators, official product documentation, incidents, or implementation retrospectives.

| Source | Observed date | Context supplied | Limitation |
| --- | --- | --- | --- |
| Public contextual source URL | YYYY-MM-DD | Constraint, failure mode, terminology, or capability | Why it does not independently prove hiring demand |

## Evidence limitations and alternatives

Explain what the sources do not establish. Include plausible alternatives such as copied job language, a temporary programme, bundled responsibilities, regulatory timing, or vendor-specific staffing.

## Practice challenge

- **Status:** none / proposed / challenge-ready / pilot-tested / validated-pattern
- **Scenario:** synthetic
- **Link:** add when available

### Candidate exercise inputs

- Synthetic file or record type

### Required learner deliverables

- Deliverable

### Evaluation dimensions

- Material issue detection
- Evidence reasoning and traceability
- False-positive control
- Handling of uncertainty
- Respect for authorization and accountability boundaries
- Verification of AI-assisted output, where applicable

## Revision history

| Date | Change | Reason |
| --- | --- | --- |
| YYYY-MM-DD | Initial entry | Initial qualifying observation |