# Methodology

## Objective

The repository identifies recurring professional work in GRC, technology risk, audit, resilience, and compliance, then converts sufficiently stable patterns into reusable workflow descriptions and optional synthetic practice challenges.

The unit of analysis is a **work action**, not a job posting, employer, title, product, regulation, or presumed software opportunity.

## First-principles model

A workflow entry exists only when the following objects can be kept separate:

1. **Demand observation** — a public employer source declares that someone is expected to perform work.
2. **Normalized work action** — the narrow action extracted from that source.
3. **Output claim** — the deliverable explicitly requested by the source, or an output cautiously inferred during normalization.
4. **Human boundary** — the accountable judgment or authorization that the public evidence supports or leaves unresolved.
5. **Automation hypothesis** — a bounded engineering inference about collection, comparison, validation, or reporting.
6. **Synthetic exercise** — invented data and context used to practise the work.

None of these objects should silently stand in for another.

## Source classes

### Employer demand sources

These establish declared hiring demand:

1. official employer career pages;
2. employer-authored public job descriptions;
3. a job-board copy only when the original is unavailable and the employer attribution is clear.

A mirror and its original count as one source record. Multiple postings from the same employer may provide corroboration and detail, but they do not increase the independent-employer count.

For the public admission threshold, independence is counted at employer level:

- reposts, role variants, locations, and business units under one employer count as one employer;
- entities under the same ultimate corporate parent are conservatively counted as one employer;
- an exception requires documented evidence that hiring authority and operating context are genuinely independent.

### Contextual sources

These may explain constraints, failure modes, terminology, or implementation options:

1. public practitioner discussions and implementation retrospectives;
2. official standards, regulatory publications, and framework documentation;
3. official product documentation describing supported capabilities and limitations;
4. public incident, audit, enforcement, or post-incident material where appropriate.

Contextual sources do not substitute for independent employers when advancing demand maturity or deciding public admission.

Search-result snippets alone are not sufficient evidence. Sources should be independently accessible, dated, and interpreted narrowly.

## Core analytical fields

### Observed work task

A bounded action that a role is expected to perform, such as validating remediation evidence or reviewing privileged access.

### Required output

The observable deliverable expected from the task, such as an exception register, control-test record, closure package, review report, or evidence bundle.

Each output should be labelled as one of:

- `explicit` — directly requested or named in a qualifying employer demand source;
- `inferred` — derived during normalization and therefore subject to revision.

### Human boundary

The point where accountable judgment or authorization remains with an identified or reasonably bounded role. Examples include approving an exception, accepting residual risk, determining regulatory adequacy, or signing off closure.

Absence of evidence is not evidence that a decision can be delegated. When authority is unclear, the entry should record the uncertainty rather than invent a role.

### Technical capabilities

Capabilities reasonably required to perform the work. These may include data reconciliation, Python, SQL, API use, configuration parsing, evidence metadata handling, reporting, or domain-specific platform knowledge.

A capability should be derived from the workflow. A job description naming a technology is evidence that the employer requested it, but not proof that it is necessary in every implementation of the workflow.

### Automation boundary

The entry may identify bounded automation for read-only collection, normalization, comparison, validation, and reporting.

It must separately identify:

- actions that change production state;
- decisions requiring authorization;
- risk acceptance or regulatory interpretation;
- remediation execution;
- unresolved accountability.

These actions are not universally prohibited from automation. Automation capability does not itself create authority, approval, or accountability.

## Research maturity and public admission

The private research process may use these demand-maturity states:

- `observed`: substantially relevant work at one qualifying employer;
- `repeated`: substantially similar work across two independent employers;
- `candidate`: substantially similar work across at least three independent employers, with sufficiently stable task, output, and human boundary.

Only `candidate` patterns are admitted to the public `workflows/` directory. `Observed` and `repeated` records remain in the private research tracker. The public repository is therefore a curated projection, not the research workspace.

The three-employer threshold is an admission rule, not a statistical market conclusion. It does not prove prevalence, market size, budget, urgency, or software demand.

Alternative interpretations must be recorded. Examples include generic copied job language, a one-off transformation programme, regulatory timing, vendor-specific staffing, or a role combining several unrelated responsibilities.

## Challenge maturity

Challenge maturity is tracked separately from demand maturity:

- `none`: no exercise proposed;
- `proposed`: scenario concept exists, but inputs or evaluation remain incomplete;
- `challenge-ready`: bounded synthetic inputs, deliverables, and evaluation dimensions exist;
- `pilot-tested`: at least one external participant has completed the exercise and supplied feedback;
- `validated-pattern`: repeated use has materially revised and stabilized the exercise and evaluation model.

A public workflow can have no challenge. A polished challenge can still rest on weak demand evidence and therefore cannot bypass the public admission threshold.

## Challenge construction

A synthetic challenge must distinguish between:

- **observed demand** — public evidence that independent employers request the work;
- **contextual constraints** — public material used to make the exercise plausible;
- **synthetic exercise** — the invented organization, records, systems, policies, errors, and expected deliverables.

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

A response may be acceptable without reaching a final decision when the available evidence is insufficient. Unsupported certainty should score worse than a justified request for additional evidence.

## Claims that are not permitted

An entry must not claim, solely from hiring evidence, that:

- an employer has a control failure;
- a market has a software gap;
- budget or procurement intent exists;
- a task is fully automatable;
- a particular workflow is universal;
- a technology named in a posting is necessary for every implementation;
- a synthetic challenge reflects a named employer's internal process.

## Review and correction

Entries should retain source dates, source class, employer identity or grouping rationale in the private tracker, status history, and material revisions. Corrections should narrow or withdraw claims when supporting evidence is stale, copied, contradicted, inaccessible, or insufficient.

The repository should prefer a smaller set of defensible workflows over a large set of weakly supported entries.
