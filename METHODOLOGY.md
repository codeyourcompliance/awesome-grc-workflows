# Methodology

## Objective

The repository identifies recurring professional work in GRC, technology risk, audit, resilience, and compliance, then represents sufficiently stable patterns as reusable workflow descriptions and optional synthetic practice challenges.

The unit of analysis is a **work action**, not a job posting, employer, title, product, regulation, or presumed software opportunity.

## First-principles model

A published workflow keeps the following objects separate:

1. **Employer evidence** — public employer sources showing that someone is expected to perform work.
2. **Normalized work action** — the narrow action extracted from those sources.
3. **Output claim** — a deliverable explicitly requested by a source or cautiously inferred during normalization.
4. **Human boundary** — accountable judgment or authorization supported by the evidence or marked unresolved.
5. **Automation hypothesis** — a bounded engineering inference about collection, comparison, validation, or reporting.
6. **Synthetic exercise** — invented data and context used to practise the work.

None of these objects should silently stand in for another.

## Source classes

### Employer evidence

Qualifying employer evidence includes:

1. official employer career pages;
2. employer-authored public job descriptions;
3. a job-board copy when the original is unavailable and employer attribution is clear.

A mirror and its original count as one source record. Multiple postings from the same employer may provide corroboration and detail, but they do not increase the independent-employer count.

For publication, independence is counted at employer level:

- reposts, role variants, locations, and business units under one employer count as one employer;
- entities under the same ultimate corporate parent are conservatively counted as one employer;
- an exception requires public evidence that hiring authority and operating context are genuinely independent.

### Contextual evidence

Contextual evidence may explain constraints, failure modes, terminology, or implementation options. Examples include:

1. public practitioner discussions and implementation retrospectives;
2. official standards, regulatory publications, and framework documentation;
3. official product documentation describing supported capabilities and limitations;
4. public incident, audit, enforcement, or post-incident material.

Contextual evidence does not substitute for independent employer evidence when deciding publication eligibility.

Search-result snippets alone are not sufficient evidence. Sources should be independently accessible, dated, and interpreted narrowly.

## Publication threshold

A workflow may be published only when:

- substantially similar work appears across at least three independent employers;
- the normalized task is sufficiently stable and bounded;
- required outputs are explicit or transparently inferred;
- the human boundary can be stated without inventing organizational authority, or is marked unresolved;
- plausible alternative explanations have been considered;
- the published entry contains enough public evidence for independent inspection.

The three-employer threshold is a repository publication rule, not a statistical market conclusion.

Alternative explanations may include generic copied job language, a temporary transformation programme, regulatory timing, vendor-specific staffing, or a role that combines unrelated responsibilities.

## Core analytical fields

### Observed work task

A bounded action that roles are expected to perform, such as validating remediation evidence or reviewing privileged access.

### Required outputs

The observable deliverables expected from the task, such as an exception register, control-test record, closure package, review report, or evidence bundle.

Each output is labelled as:

- `explicit` — directly requested or named in qualifying employer evidence;
- `inferred` — derived during normalization and therefore subject to revision.

### Human boundary

The point where accountable judgment or authorization remains with an identified or reasonably bounded role. Examples include approving an exception, accepting residual risk, determining regulatory adequacy, or signing off closure.

Absence of evidence is not evidence that a decision can be delegated. When authority is unclear, the entry records the uncertainty rather than inventing an owner.

### Technical capabilities

Capabilities reasonably required to perform the work may include data reconciliation, Python, SQL, API use, configuration parsing, evidence metadata handling, reporting, or domain-specific platform knowledge.

A capability must be derived from the workflow. A job description naming a technology is evidence that an employer requested it, but not proof that it is necessary in every implementation.

### Automation boundary

The entry may identify bounded automation for read-only collection, normalization, comparison, validation, and reporting.

It separately identifies:

- actions that change production state;
- decisions requiring authorization;
- risk acceptance or regulatory interpretation;
- remediation execution;
- unresolved accountability.

These actions are not universally prohibited from automation. Automation capability does not itself create authority, approval, or accountability.

## Challenge maturity

Challenge maturity is tracked separately from workflow evidence:

- `none`: no exercise proposed;
- `proposed`: a scenario concept exists, but inputs or evaluation remain incomplete;
- `challenge-ready`: bounded synthetic inputs, deliverables, and evaluation dimensions exist;
- `pilot-tested`: at least one external participant has completed the exercise and supplied feedback;
- `validated-pattern`: repeated use has materially revised and stabilized the exercise and evaluation model.

A published workflow can have no challenge. A polished challenge does not strengthen the underlying workflow evidence.

## Challenge construction

A synthetic challenge distinguishes between:

- **employer evidence** — public evidence that employers request the work;
- **contextual constraints** — public material used to make the exercise plausible;
- **synthetic exercise** — invented organizations, records, systems, policies, errors, and expected deliverables.

A useful challenge should contain:

- a bounded role and task;
- sufficient but imperfect inputs;
- at least one genuine issue;
- at least one plausible false positive;
- at least one uncertainty, contradiction, or missing item;
- explicit required deliverables;
- evaluation dimensions rather than a single simplistic answer;
- a stated authorization and accountability boundary.

## Evaluation model

Evaluation should consider:

- detection of material issues;
- evidence reasoning and traceability;
- control of false positives;
- handling of missing or contradictory evidence;
- completeness of required deliverables;
- respect for authorization and accountability boundaries;
- verification of AI-assisted output where AI is used.

A response may be acceptable without reaching a final decision when available evidence is insufficient. Unsupported certainty should score worse than a justified request for additional evidence.

## Claims that are not permitted

An entry must not claim, solely from hiring evidence, that:

- an employer has a control failure;
- a market has a software gap;
- budget or procurement intent exists;
- a task is fully automatable;
- a workflow is universal;
- a technology named in a posting is necessary for every implementation;
- a synthetic challenge reflects a named employer's internal process.

## Review and correction

Published entries retain source dates, source classifications, material revisions, and known limitations. Claims should be narrowed or withdrawn when supporting evidence becomes stale, copied, contradicted, inaccessible, or insufficient.

The repository prefers a smaller set of defensible workflows over a large set of weakly supported entries.
