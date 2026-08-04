# Contributing

Contributions should improve the completeness, realism, reviewability, or safety of runnable synthetic GRC work-sample cases. Volume alone is not a goal.

## Active submission types

### New case

Use `cases/_template/`. A new case must train one bounded work action and include the complete package required for its proposed maturity state.

### Case correction

Correct an inconsistency, ambiguity, unsafe authority assumption, unsupported claim, broken resource, scoring defect, or reference-answer error.

### Case improvement

Improve synthetic inputs, deliverable templates, reviewer guidance, accessibility, metadata, or pilot-feedback treatment without changing the bounded action.

### Template or schema change

Propose a reusable structural improvement. Explain how existing and future cases are affected.

### Legacy migration

Migrate a pre-v2.1 workflow or challenge only through a separate reviewed change. Do not copy private employer research into the public repository.

## Qualification and transfer prerequisite

A public case package must not be used to bypass private workflow qualification.

Before public case design begins, maintainers must confirm that:

- the bounded workflow passed private qualification;
- an employer-agnostic normalized workflow exists;
- a sanitized case-design packet was prepared;
- explicit transfer approval was granted as a separate action; and
- public design uses only the approved sanitized content.

Do not place private evidence, named employers, recruitment URLs, private identifiers, employer-group records, qualification reasoning, internal scoring, commercial priorities, buyer hypotheses, contact research, private paths, or transfer records in the public repository.

An external contributor may propose a bounded concept for consideration, but a public case PR must not proceed until maintainers have routed the workflow through the same qualification and transfer controls. The public PR should state that the prerequisite was confirmed without exposing private details.

## Before submitting a case

Confirm that the proposal:

- trains one bounded work action;
- uses a fictional organization and synthetic or safely constructed data;
- is not a lightly renamed version of a real employer or event;
- states included and excluded scope;
- contains sufficient but imperfect inputs;
- requires at least one professional deliverable;
- states required tools, accepted equivalents, and optional tools separately;
- includes a scoring rubric, reviewer guide, and reference answer;
- separates fact, inference, recommendation, approval, risk acceptance, legal interpretation, sign-off, closure, and production change;
- does not grant authority merely because the learner can perform analysis or use technical tools;
- keeps output basis as `explicit`, `inferred`, or `case-designed`;
- labels role relationships as `evidence-observed`, `workflow-inferred`, or `case-designed` when a role map is included;
- remains completable without private evidence or maintainer-owned services;
- contains no confidential, personal, production, employer-internal, or commercially sensitive information;
- avoids unsupported market, hiring, budget, procurement, shortage, gap, universal-technology, or full-automation claims.

## Required package

A `case-ready` submission normally includes:

```text
cases/<case-id>/
├── README.md
├── scenario.md
├── task-brief.md
├── inputs/
├── templates/
├── scoring-rubric.md
├── reviewer-guide.md
├── reference-answer.md
├── metadata.yaml
└── role-relevance.md        # optional enhancement
```

Additional files may be added when they materially help the learner or reviewer. Do not add empty sections merely to look complete.

The README, task brief, and metadata must state required tools. If no specialized tool is needed, say so explicitly. Do not convert an optional implementation choice or a technology observed in one source into a universal requirement.

A Role Relevance Map is recommended but optional. Its absence does not block `case-ready` when the core case is otherwise complete. Removing it must not make the task unusable or unreviewable.

## Synthetic data rules

Synthetic material must be independently fictional.

Do not:

- replace a real employer name with a generic label while preserving its distinctive facts;
- copy real customer, employee, incident, audit, risk, policy, ticket, system, or control data;
- include personal information;
- reproduce substantial copyrighted source material;
- imply that a named organization uses the scenario, process, controls, or authority model.

Every case must include the standard synthetic disclaimer from `METHODOLOGY.md`.

## Deliverables and evaluation

Required deliverables should resemble professional work products, not quiz answers.

A rubric must:

- use observable criteria;
- define weights or scoring ranges;
- identify critical errors;
- allow defensible alternative conclusions;
- reward traceability and justified uncertainty;
- penalize invented facts and authority overreach.

A reviewer guide must explain intentional ambiguities, acceptable answer ranges, partial credit, and escalation conditions.

A reference answer must distinguish facts, assumptions, unresolved questions, findings, recommendations, and authorized decisions. It is one defensible answer, not the only answer.

## Authority and automation

State separately who prepares evidence, analyzes or tests, recommends, approves, accepts exceptions or residual risk, interprets legal or regulatory requirements, signs off, closes remediation, and performs production changes.

Technical capability, system access, or automation does not create authority or accountability.

Bounded automation may support read-only collection, normalization, checks, comparison against authorized criteria, traceability, exception identification, and draft reporting. Approval, closure, risk acceptance, legal determination, remediation execution, production changes, overrides, and final sign-off require separate authority or controls.

## External resources

A `case-ready`, `pilot-tested`, or `validated-case` submission must include at least one relevant non-recruitment public resource. A `proposed` or `design-ready` submission may omit it while design is incomplete.

For each resource, explain its relevance and limitation. Maintainer-owned links are optional and must not be required to complete or review the case.

## Case maturity

Use only these values:

- `proposed` — only the case concept exists;
- `design-ready` — scenario, task, and input design are complete;
- `case-ready` — inputs, deliverables, output format, scoring, reviewer guidance, authority boundary, required tools, required external resource, and independent review are complete;
- `pilot-tested` — at least one independent participant completed the case and supplied feedback;
- `validated-case` — repeated use and material revision have stabilized the case.

Public `main` should normally contain only `case-ready` or more mature cases.

## Pull requests

Use a focused branch and open a Draft PR by default.

The PR body should explain:

- the bounded work action;
- that the private qualification and explicit transfer prerequisite was confirmed, without exposing private details;
- what is synthetic and how fictional independence was checked;
- package contents, required tools, and required deliverables;
- authority and adjacent-workflow boundaries;
- output-basis treatment;
- rubric and reviewer-guide design;
- relevant public resources;
- validation performed;
- first-principles and adversarial findings;
- known limitations;
- case maturity requested;
- explicit non-actions, including whether no Ready transition, merge, or branch deletion occurred.

Inspect the complete diff and cross-file consistency before requesting review. Do not mix unrelated cases or repository cleanup into the same PR.

## Review gates

No stage automatically authorizes the next.

```text
Private candidate review
→ private workflow qualification
→ employer-agnostic normalized workflow
→ sanitized case-design packet
→ explicit transfer approval
→ proposed public case
→ design-ready package
→ case-ready validation
→ independent review
→ explicit Ready approval
→ explicit merge approval
→ pilot testing
```

A case must remain below `case-ready` until scenario, inputs, task brief, required tools, deliverables, output format, rubric, reviewer guidance, reference answer, metadata, authority boundaries, external resource, and cross-file consistency are complete.

## Style

Use plain, precise language. Separate observed case facts, assumptions, inference, recommendations, case-design decisions, and unresolved questions.

Prefer a smaller number of defensible, usable cases over shallow bulk generation.

By contributing original material, you agree that it may be distributed under the repository license. Do not submit material you do not have the right to share.
