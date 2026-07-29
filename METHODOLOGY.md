# Methodology

## Objective

The repository identifies recurring professional work in GRC, technology risk, audit, resilience, and compliance, then represents sufficiently stable patterns as reusable workflow descriptions and optional synthetic practice challenges.

The unit of analysis is a **work action**, not a job posting, employer, title, product, regulation, technology, presumed skill gap, market gap, or software opportunity.

The repository combines two public layers:

1. **Awesome curation** — employer evidence, official guidance, open-source tools, external articles, implementation cases, courses, labs, datasets, and external challenges.
2. **Normalized analysis** — bounded work tasks, required outputs, human boundaries, technical capabilities, automation boundaries, evidence limitations, and optional original synthetic challenges.

These layers must remain useful and understandable without maintainer-owned links.

## First-principles model

A published workflow keeps the following objects separate:

1. **Employer evidence** — public employer sources showing that someone is expected to perform work.
2. **Normalized work action** — the narrow action extracted from those sources.
3. **Output claim** — a deliverable explicitly requested by a source or cautiously inferred during normalization.
4. **Human boundary** — accountable judgment or authorization supported by the evidence or marked unresolved.
5. **Technical capability** — an employer-requested technology, workflow-derived capability, or optional implementation choice.
6. **Automation hypothesis** — a bounded engineering inference about collection, comparison, validation, or reporting.
7. **External resource** — public material selected for learning, implementation context, or practice.
8. **Synthetic exercise** — invented data and context used to practise the work.

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

Employer evidence may support claims about requested work, explicitly requested outputs, named technologies, responsibilities, and stated approval boundaries. It does not by itself establish a control weakness, skill shortage, inability to hire, market gap, workflow gap, unmet demand, software budget, or procurement intent.

### Contextual evidence

Contextual evidence may explain constraints, failure modes, terminology, implementation options, or capabilities. Examples include:

1. public practitioner discussions and implementation retrospectives;
2. official standards, regulatory publications, and framework documentation;
3. official product documentation describing supported capabilities and limitations;
4. public incident, audit, enforcement, or post-incident material;
5. open-source projects and technical documentation.

Contextual evidence does not substitute for independent employer evidence when deciding publication eligibility.

### External resources

External resources give the page independent practical value. They may include official guidance, open-source tools, articles, cases, courses, labs, datasets, and external challenges.

A resource should be included because it materially helps the reader understand, inspect, implement, or practise the work. Do not add weak links merely to meet a quota. Maintainer-owned resources are optional and must not be necessary for the page to remain useful.

Search-result snippets alone are not sufficient evidence. Sources should be independently accessible, dated, and interpreted narrowly.

## Publication threshold

A workflow may be published only when:

- substantially similar work appears across at least three independent employers;
- the normalized task is sufficiently stable and bounded;
- required outputs are explicit or transparently inferred;
- the human boundary can be stated without inventing organizational authority, or is marked unresolved;
- plausible alternative explanations have been considered;
- the published entry contains enough public evidence for independent inspection;
- first-principles and adversarial review are complete.

The three-employer threshold is a repository publication rule, not a statistical market conclusion.

Alternative explanations may include generic copied job language, a temporary transformation programme, regulatory timing, vendor-specific staffing, bundled responsibilities, or repeated publication within one corporate group.

## Core analytical fields

### Observed work task

A bounded action that roles are expected to perform, such as validating remediation evidence or reviewing privileged access.

Keep source wording separate from the normalized task. Document material normalization choices.

### Required outputs

The observable deliverables expected from the task, such as an exception register, control-test record, closure package, review report, or evidence bundle.

Each output is labelled as:

- `explicit` — directly requested or named in qualifying employer evidence;
- `inferred` — derived during normalization and therefore subject to revision.

An inferred output must never be presented as an observed employer requirement.

### Human boundary

The point where accountable judgment or authorization remains with an identified or reasonably bounded role. Examples include approving an exception, accepting residual risk, determining regulatory adequacy, approving remediation closure, signing a control conclusion, or authorizing a production change.

Absence of evidence is not evidence that a decision can be delegated. When authority is unclear, the entry records the uncertainty rather than inventing an owner.

### Technical capabilities

Separate three categories:

- **employer-requested technology** — explicitly named in qualifying employer evidence;
- **workflow-derived capability** — reasonably required by the normalized work;
- **optional implementation choice** — one possible technical approach.

A technology named in one posting is evidence that the employer requested it, not proof that every implementation requires it.

### Automation boundary

The entry may identify bounded automation for read-only collection, normalization, comparison, completeness or freshness checks, metadata validation, exception identification, and reporting.

It separately identifies:

- actions that change production state;
- decisions requiring authorization;
- risk acceptance or legal or regulatory interpretation;
- remediation execution;
- unresolved accountability.

These actions are not universally prohibited from automation. Automation capability does not itself create authority, approval rights, or accountability.

## Source lifecycle

Each employer source should retain:

- employer and role title;
- public URL;
- observation date;
- last-checked date;
- minimal supporting paraphrase or quotation;
- independence note;
- source status.

Suggested source statuses are `active`, `unavailable`, and `replaced`.

When a source becomes unavailable:

1. do not silently treat it as active;
2. retain only the limited observation that the published record can still support;
3. mark the source status and last-checked date;
4. reassess whether the remaining public evidence still meets the publication threshold;
5. narrow or withdraw claims that are no longer independently inspectable.

An unavailable source does not create a new employer or strengthen recurrence.

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
- **external practice resources** — third-party labs or exercises selected for relevance;
- **original synthetic exercise** — invented organizations, records, systems, policies, errors, and expected deliverables.

Every original challenge must state that it does not represent any named employer's internal process.

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
- a skill shortage exists;
- employers cannot find qualified people;
- a market, workflow, or software gap exists;
- unmet demand exists;
- budget or procurement intent exists;
- a task is fully automatable;
- a workflow is universal;
- a technology named in a posting is necessary for every implementation;
- a synthetic challenge reflects a named employer's internal process.

Prefer terms such as `recurring employer demand`, `workflow pattern`, `technical capability`, `automation opportunity`, and `implementation option`.

## Review and correction

Published entries retain source dates, source classifications, source status, material revisions, and known limitations. Claims should be narrowed or withdrawn when supporting evidence becomes stale, copied, contradicted, inaccessible, or insufficient.

Every page must pass this test:

> After removing all maintainer-owned links, is the page still worth reading, saving, and citing?

The repository prefers a smaller set of defensible workflows and resources over a large set of weakly supported entries.
