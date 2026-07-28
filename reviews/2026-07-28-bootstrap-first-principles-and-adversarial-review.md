# Bootstrap First-Principles and Adversarial Review

Date: 2026-07-28

Scope: merged bootstrap PR #1.

## First-principles question

The repository should answer one narrow question:

> What recurring, publicly observable work are employers asking GRC, technology-risk, audit, resilience, and compliance practitioners to perform, and how can that work be represented without inventing demand, authority, or internal process?

The minimum defensible object is therefore not an `awesome` link, job title, technology, framework, or challenge. It is:

```text
independent employer demand evidence
-> normalized work action
-> explicit or inferred output
-> bounded human authorization/accountability
-> optional automation hypothesis
-> optional synthetic exercise
```

Each transition must remain inspectable.

## Findings

### F1 — Demand maturity and challenge maturity were collapsed

Severity: high.

The original `status` field mixed evidence states (`observed`, `repeated`, `candidate`) with exercise-design states (`challenge-ready`, `pilot-tested`, `validated-pattern`). This allowed a polished challenge to appear as stronger demand evidence, or strong demand evidence to appear as a completed exercise.

Correction: use independent `demand_status` and `challenge_status` fields.

### F2 — Source independence was under-specified

Severity: high.

The original model allowed recurrence across “employers or sources.” A practitioner post or framework document could therefore advance a hiring-demand claim despite not being employer demand evidence.

Correction: only independent employer demand sources advance demand maturity. Practitioner, official, regulatory, standards, incident, and product material are contextual sources.

### F3 — Required outputs could be silently invented

Severity: high.

A normalized workflow often needs an output, but a job description may not name one. Treating inferred deliverables as observed employer requirements would overstate the evidence.

Correction: classify each output as `explicit` or `inferred` and preserve the reasoning.

### F4 — The automation boundary was too categorical

Severity: medium.

The original wording placed remediation execution and production-state change under “not delegated.” This could be read as a universal technical prohibition. The actual boundary is authority and accountability: execution may be automated in an authorized system, but technical capability does not create permission, approval, or risk ownership.

Correction: describe actions requiring separate authority or control rather than declaring them universally non-automatable.

### F5 — `independent_employers` did not match the stated evidence model

Severity: medium.

The schema counted employers while the prose referred to employers or sources. The mismatch would create inconsistent status assignments.

Correction: replace it with `independent_demand_sources` and add a separate `contextual_sources` count.

### F6 — The repository is not yet an Awesome List in the conventional sense

Severity: medium, non-blocking for the research project.

The repository currently contains methodology and templates but no curated workflow entries. It should not yet claim inclusion in the central Awesome index or present maturity implied by established Awesome lists.

The central Awesome project currently expects, among other things, a mature curated list, an Awesome badge, a `Contents` section, appropriate topics, linting, and at least 30 days of maturity before submission. It also states that AI-generated lists are not accepted. These are external project rules, not requirements for this repository to exist.

Decision: retain the name, but do not pursue central Awesome-list submission until the repository contains independently reviewed entries and can satisfy the external rules without misrepresenting authorship.

### F7 — License file contains a notice rather than the complete legal code

Severity: medium.

The current `LICENSE` identifies CC BY 4.0 and links to the legal code, but it does not contain the complete standard license text. This may reduce automatic license recognition and makes the repository less self-contained.

Decision required: replace it with the unmodified complete CC BY 4.0 text, or deliberately retain a notice file and document why. Do not modify the legal text.

### F8 — No actual workflow claim was merged

Severity: positive containment finding.

PR #1 added structure, methodology, and templates only. It did not publish employer-specific claims, synthetic datasets, or workflow entries. The defects above therefore affect the future evidence model rather than requiring withdrawal of published findings.

## Adversarial scenarios

The corrected model should resist these failures:

1. Three copies of one job advertisement are counted as three employers.
2. One job posting plus two LinkedIn posts is promoted to repeated demand.
3. A challenge receives strong learner feedback and is presented as stronger market evidence.
4. A job asks for “control testing,” while the repository invents a specific closure package and labels it employer-required.
5. Python appears in one posting and is presented as universally required for the workflow.
6. An automation can technically change production state and is therefore assumed authorized to do so.
7. Every workflow links to a maintainer-owned challenge, turning the repository into a promotional directory.

## Merge recommendation

The bootstrap merge does not need to be reverted because it published no substantive workflow claims. A corrective PR should be merged before adding the first workflow entry.

Blocking corrections before workflow publication:

- separate demand and challenge maturity;
- separate demand and contextual sources;
- classify outputs as explicit or inferred;
- correct the schema and template;
- clarify authority versus technical automation.

License completion should be resolved before inviting external contributions or substantial reuse.
