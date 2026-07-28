# Methodology

## Objective

The repository identifies recurring professional work in GRC, technology risk, audit, resilience, and compliance, then converts sufficiently stable patterns into reusable workflow descriptions and optional synthetic practice challenges.

The unit of analysis is a **work action**, not a job posting, employer, title, product, or regulation.

## Source classes

Entries may draw on:

1. public job descriptions;
2. official employer career pages;
3. public practitioner discussions and implementation retrospectives;
4. official standards, regulatory publications, and framework documentation;
5. official product documentation describing supported capabilities and limitations;
6. public incident, audit, enforcement, or post-incident material where appropriate.

Search-result snippets alone are not sufficient evidence. Sources should be independently accessible and interpreted narrowly.

## Core analytical fields

### Observed work task

A bounded action that a role is expected to perform, such as validating remediation evidence or reviewing privileged access.

### Required output

The observable deliverable expected from the task, such as an exception register, control-test record, closure package, review report, or evidence bundle.

### Human boundary

The point where accountable judgment remains with an authorized person or role. Examples include approving an exception, accepting residual risk, determining regulatory adequacy, or signing off closure.

### Technical capabilities

Capabilities reasonably required to perform the work. These may include data reconciliation, Python, SQL, API use, configuration parsing, evidence metadata handling, reporting, or domain-specific platform knowledge.

A technical capability should be derived from the workflow, not added merely because it is generally popular.

### Automation boundary

The entry separates:

- read-only collection, normalization, comparison, validation, and reporting;
- judgment, approval, remediation, risk acceptance, and production-state change.

An automation opportunity is an analytical inference. It is not evidence that an employer intends to buy software or delegate accountability.

## Pattern formation

A single observation may enter the repository as `observed`.

A workflow normally advances only when:

- similar work appears in independent sources;
- the required output remains substantially stable;
- the human boundary can be stated without inventing organizational authority;
- alternative interpretations have been considered;
- the workflow is concrete enough to support a bounded exercise.

Repeated wording copied across job aggregators does not count as independent recurrence.

## Evidence maturity

- `observed`: at least one qualifying public observation;
- `repeated`: recurrence across at least two independent employers or sources;
- `candidate`: stable task, output, and human boundary;
- `challenge-ready`: synthetic scenario and evaluation dimensions exist;
- `pilot-tested`: external completion and feedback exist;
- `validated-pattern`: repeated use has materially revised and stabilized the model.

## Challenge construction

A synthetic challenge must distinguish between:

- **observed demand**: the public evidence that the work is requested;
- **synthetic exercise**: the invented organization, records, systems, policies, errors, and expected deliverables.

A useful challenge should contain:

- a bounded role and task;
- sufficient but imperfect inputs;
- at least one genuine issue;
- at least one plausible false positive;
- at least one uncertainty, contradiction, or missing item;
- explicit required deliverables;
- evaluation dimensions rather than a single simplistic answer;
- a stated human decision boundary.

## Evaluation model

Evaluation should consider:

- detection of material issues;
- evidence reasoning and traceability;
- control of false positives;
- handling of missing or contradictory evidence;
- completeness of required deliverables;
- respect for human approval and accountability boundaries;
- verification of AI-assisted output where AI is used.

A response may be acceptable without reaching a final decision when the available evidence is insufficient. Unsupported certainty should score worse than a justified request for additional evidence.

## Claims that are not permitted

An entry must not claim, solely from hiring evidence, that:

- an employer has a control failure;
- a market has a software gap;
- budget or procurement intent exists;
- a task is fully automatable;
- a particular workflow is universal;
- a synthetic challenge reflects a named employer's internal process.

## Review and correction

Entries should retain source dates, status history, and material revisions. Corrections should narrow or withdraw claims when the supporting evidence is stale, copied, contradicted, or insufficient.
