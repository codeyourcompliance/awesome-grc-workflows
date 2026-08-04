# Methodology

## Objective

Awesome GRC Workflows publishes evidence-calibrated synthetic work-sample cases. The public repository teaches one bounded professional action at a time through realistic inputs, required deliverables, explicit authority boundaries, and review criteria.

The public case is not employer research, a job-posting archive, a market-demand claim, or a representation of any named organization’s internal process.

## Three-layer separation

The project keeps these layers separate:

```text
Private Evidence Engine
→ Normalized Bounded Workflow
→ Public Synthetic Case Package
```

The private layer may contain named sources, employer-group reconciliation, qualification reasoning, internal identifiers, and unpublished research notes. None of that material is automatically public.

The normalized workflow is employer-agnostic. It defines the trigger, inputs, action, decision target, outputs, exclusions, failure modes, authority boundaries, capabilities, automation opportunities, and possible role-family relationships.

The public layer independently designs a fictional organization, synthetic evidence package, professional deliverables, rubric, reviewer guide, and reference answer.

No stage automatically authorizes the next.

## Unit of design

The unit is one bounded work action.

Do not use a job title, framework, regulation, product, technology, department, broad responsibility, complete GRC function, presumed skill gap, market gap, or software opportunity as the case unit.

A bounded action should have:

- a recognisable trigger;
- defined inputs;
- an operational action;
- a decision target;
- reviewable outputs;
- clear exclusions;
- identifiable failure modes;
- an authority boundary.

## Public case requirements

A `case-ready` package includes:

1. **README** — purpose, bounded action, maturity, package map, and synthetic disclaimer.
2. **Scenario** — fictional organization, operating context, roles, systems, dates, and relevant constraints.
3. **Task brief** — learner role, work action, included and excluded scope, required deliverables, and submission format.
4. **Inputs** — sufficient but imperfect synthetic evidence.
5. **Templates** — optional structures for the expected professional output.
6. **Scoring rubric** — observable criteria, weights, critical errors, and maturity anchors.
7. **Reviewer guide** — review method, acceptable answer range, ambiguity treatment, and authority checks.
8. **Reference answer** — one defensible response, not the only possible response.
9. **Role relevance** — optional employer-agnostic role-family relationships.
10. **Metadata** — machine-readable status and package information.

A narrative prompt alone is not a runnable case.

## Synthetic independence

Public organizations, systems, records, authority structures, incidents, policies, dates, and datasets must be fictional or safely constructed.

Do not pseudonymize a real employer as a “leading bank,” “major consultancy,” or similar label. Do not preserve a real organization’s distinctive combination of facts while changing only its name.

Every case must state:

> This case uses a fictional organization and synthetic or safely constructed data. It does not represent any named employer’s internal process, systems, controls, authority structure, or records.

## Evidence package design

Inputs should be sufficient to perform the bounded action but imperfect enough to require professional reasoning.

Where relevant, include:

- at least one material issue;
- at least one plausible false positive or non-issue;
- at least one missing, stale, inconsistent, ambiguous, duplicated, or unsupported item;
- enough metadata to assess scope, provenance, date, owner, version, and traceability;
- explicit criteria where the learner is expected to compare evidence against them;
- clear limits where criteria or authority are unresolved.

Do not introduce noise merely to make the case difficult. Every ambiguity should test a stated capability or review criterion.

## Output classes

Keep these classes separate:

- `employer-observed` — used only in private qualification and not exposed as named-employer evidence in the public case;
- `workflow-inferred` — derived from the bounded action;
- `case-designed` — created to make the exercise usable and reviewable.

Public deliverables are normally `case-designed`. They must not be represented as outputs required by a real employer unless separately authorized and supported.

## Human authority boundary

Identify separately who may:

- prepare or supply evidence;
- perform analysis or testing;
- recommend;
- approve;
- accept exceptions or residual risk;
- interpret legal or regulatory requirements;
- sign off conclusions;
- close remediation;
- execute production changes.

Technical capability, access, or automation does not create authorization, approval rights, legal authority, risk-acceptance authority, production authority, or accountability.

When accountability is not established, mark it unresolved or design a clearly fictional authorized role. Do not silently grant the learner final authority.

## Automation boundary

Suitable bounded automation may include:

- read-only collection;
- normalization;
- metadata, completeness, and freshness checks;
- comparison against authorized machine-readable criteria;
- duplicate or contradiction detection;
- traceability generation;
- exception identification;
- draft workpapers and reporting.

Approval, closure, risk acceptance, legal determination, remediation execution, production changes, overrides, and final sign-off require separately defined authority or controls.

Do not claim either universal full automation or universal non-automability.

## Role relevance

A case may identify employer-agnostic role families that may:

- `perform`;
- `contribute`;
- `review`;
- `consume`;
- `authorize/own`.

Where used, classify the relationship as:

- `evidence-observed`;
- `workflow-inferred`;
- `case-designed`.

Role relevance supports navigation and learning. It does not establish universal job ownership, current hiring demand, professional authorization, or approval authority.

## Evaluation model

A rubric should assess observable work quality rather than keyword matching.

Common dimensions include:

- scope discipline;
- material issue detection;
- evidence-to-requirement traceability;
- handling of missing or contradictory information;
- false-positive control;
- fact, inference, and recommendation separation;
- completeness and usability of the deliverable;
- authority-boundary discipline;
- communication quality;
- verification of AI-assisted output where AI is used.

A justified request for additional evidence may be stronger than an unsupported final conclusion.

Critical errors may include:

- inventing facts or evidence;
- treating a recommendation as approval;
- accepting risk without authority;
- making an unsupported legal conclusion;
- changing production state;
- claiming closure despite a material unresolved deficiency;
- exposing confidential or personal data.

## Reviewer guide and reference answer

The reviewer guide should explain:

- what must be found;
- what may reasonably vary;
- which ambiguities are intentional;
- what evidence would support alternative conclusions;
- which authority overreaches are critical;
- how partial credit is assigned.

The reference answer is one defensible response. It must distinguish facts, assumptions, unresolved questions, findings, recommendations, and authorized decisions.

## Public value test

After removing all maintainer-owned links, can a user still understand the scenario, inspect the inputs, complete the task, produce a deliverable, and apply the review criteria?

If not, the case is not ready.

Each case should normally include at least one relevant non-recruitment public resource. A weak link should not be added merely to satisfy a quota.

## Case maturity and release gates

- `draft` — incomplete or under internal review;
- `case-ready` — complete package and independent review passed;
- `pilot-tested` — at least one independent participant completed the case and supplied feedback;
- `validated-pattern` — repeated use materially revised and stabilized the case;
- `retired` — retained for history but not current practice.

A case must not be marked `case-ready`, published, or merged merely because a private candidate is qualified or a design packet exists.

## Prohibited claims

Do not claim from a case, private qualification, or role map alone that:

- a named employer has a weakness or uses the synthetic process;
- current hiring demand exists;
- a market, skill, workflow, or software gap exists;
- employers cannot find qualified people;
- budget or procurement intent exists;
- one technology or workflow is universal;
- the task is fully automatable;
- completing the case creates professional authority or full role competence.

Commercial and market claims require separate evidence.

## Legacy public content

Files under `workflows/` and `challenges/` were created under the pre-v2.1 employer-evidence-centred model. They are retained for history and may be migrated only through a separate reviewed change.

Do not use a legacy workflow page as the template for a new case.

## Review and correction

Before release, inspect the complete package for:

- fictional independence;
- internal consistency across scenario, inputs, task, rubric, and answer;
- private-information leakage;
- unsupported authority;
- output-class confusion;
- adjacent-workflow confusion;
- hidden dependencies;
- misleading claims;
- licensing and source-attribution issues.

Prefer fewer defensible cases over a large collection of shallow exercises. Narrow, hold, revise, or retire a case rather than inventing plausible content.
