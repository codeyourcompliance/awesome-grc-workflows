# Bootstrap First-Principles and Adversarial Review

Date: 2026-07-28

Scope: merged bootstrap PR #1 and corrective PR #2.

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

Correction: use separate demand-research states and `challenge_status`. Public workflow frontmatter is fixed at `demand_status: candidate`.

### F2 — Source independence was under-specified

Severity: high.

The original model allowed recurrence across “employers or sources.” A practitioner post or framework document could therefore advance a hiring-demand claim despite not being employer demand evidence.

Correction: only independent employers advance demand maturity. Practitioner, official, regulatory, standards, incident, and product material are contextual sources.

### F3 — Required outputs could be silently invented

Severity: high.

A normalized workflow often needs an output, but a job description may not name one. Treating inferred deliverables as observed employer requirements would overstate the evidence.

Correction: classify each output as `explicit` or `inferred` and preserve the reasoning.

### F4 — The automation boundary was too categorical

Severity: medium.

The original wording placed remediation execution and production-state change under “not delegated.” This could be read as a universal technical prohibition. The actual boundary is authority and accountability: execution may be automated in an authorized system, but technical capability does not create permission, approval, or risk ownership.

Correction: describe actions requiring separate authority or control rather than declaring them universally non-automatable.

### F5 — Recurrence unit was inconsistent

Severity: high.

An intermediate correction used `independent_demand_sources`, while the methodology described recurrence across independent employers. Multiple postings from one employer could therefore inflate demand maturity.

Correction: use `independent_employers` as the admission metric. `qualifying_demand_sources` is an optional supporting count and does not drive admission. Multiple roles, reposts, locations, and business units from one employer count as one employer. Entities under the same ultimate corporate parent are conservatively grouped as one employer unless genuine independence is documented.

### F6 — Public admission boundary was unresolved

Severity: high.

The repository described `candidate` as an admission threshold but still allowed `observed` and `repeated` files in the public `workflows/` directory.

Correction: only `candidate` workflows may be published in `workflows/`. Earlier research states remain in the private tracker. The schema enforces `demand_status: candidate` and at least three independent employers.

### F7 — The repository is not yet an Awesome List in the conventional sense

Severity: medium, non-blocking for the research project.

The repository currently contains methodology and templates but no curated workflow entries. It should not yet claim inclusion in the central Awesome index or present maturity implied by established Awesome lists.

The central Awesome project currently expects, among other things, a mature curated list, an Awesome badge, a `Contents` section, appropriate topics, linting, and at least 30 days of maturity before submission. It also states that AI-generated lists are not accepted. These are external project rules, not requirements for this repository to exist.

Decision: retain the name, but do not pursue central Awesome-list submission until the repository contains independently reviewed entries and can satisfy the external rules without misrepresenting authorship.

### F8 — License file contains a notice rather than the complete legal code

Severity: medium.

The current `LICENSE` identifies CC BY 4.0 and links to the legal code, but it does not contain the complete standard license text. This may reduce automatic license recognition and makes the repository less self-contained.

Decision required: replace it with the unmodified complete CC BY 4.0 text, or deliberately retain a notice file and document why. Do not modify the legal text.

### F9 — No actual workflow claim was merged

Severity: positive containment finding.

PR #1 added structure, methodology, and templates only. It did not publish employer-specific claims, synthetic datasets, or workflow entries. The defects above therefore affect the future evidence model rather than requiring withdrawal of published findings.

## Adversarial scenarios

The corrected model should resist these failures:

1. Three copies of one job advertisement are counted as three employers.
2. Three different roles from one employer are counted as three independent employers.
3. Related subsidiaries are counted separately without examining the ultimate corporate parent.
4. One job posting plus two LinkedIn posts is promoted to repeated demand.
5. A challenge receives strong learner feedback and is presented as stronger market evidence.
6. A job asks for “control testing,” while the repository invents a specific closure package and labels it employer-required.
7. Python appears in one posting and is presented as universally required for the workflow.
8. An automation can technically change production state and is therefore assumed authorized to do so.
9. Every workflow links to a maintainer-owned challenge, turning the repository into a promotional directory.
10. An `observed` or `repeated` research note is published as if it were part of the curated workflow list.

## Merge recommendation

The bootstrap merge does not need to be reverted because it published no substantive workflow claims.

Corrective PR #2 may be merged only after all of the following agree:

- README states that only `candidate` workflows are public;
- methodology counts recurrence by independent employer;
- schema requires `demand_status: candidate` and at least three independent employers;
- workflow template uses the same fields and thresholds;
- contribution and PR rules prevent source-count inflation;
- demand evidence, contextual evidence, challenge maturity, and authorization remain separate.

The license should be completed before inviting external contributions or substantial reuse, but it does not block the evidence-model correction.
