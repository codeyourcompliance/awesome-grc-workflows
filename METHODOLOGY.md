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

## Private-to-public transfer gate

Public case design based on private research may begin only when:

1. the bounded workflow has passed private qualification;
2. an employer-agnostic normalized workflow exists;
3. a sanitized case-design packet has been prepared;
4. explicit transfer approval has been granted as a separate action; and
5. only the approved sanitized content is used in public design.

The public repository must not contain named employers, recruitment URLs, private identifiers, employer-group records, private qualification reasoning, internal scoring, commercial priorities, buyer hypotheses, contact research, private paths, or transfer records.

An external case concept does not bypass this sequence. Maintainers must route the bounded workflow through the same private qualification and sanitized-transfer controls before a public case package is designed or submitted.

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

1. **README** — purpose, bounded action, maturity, required tools, package map, and synthetic disclaimer.
2. **Scenario** — fictional organization, operating context, roles, systems, dates, and relevant constraints.
3. **Task brief** — learner role, work action, included and excluded scope, required tools, required deliverables, and submission format.
4. **Inputs** — sufficient but imperfect synthetic evidence.
5. **Templates** — at least one deliverable template or a clearly defined output format.
6. **Scoring rubric** — observable criteria, weights, critical errors, and maturity anchors.
7. **Reviewer guide or reference answer** — review method, acceptable answer range, and one defensible response.
8. **Human authority boundary** — clear separation of analysis, recommendation, approval, risk acceptance, legal interpretation, sign-off, closure, and production change.
9. **Metadata** — machine-readable status and package information, including required tools.
10. **External resource** — at least one relevant non-recruitment public resource with its relevance and limitation explained.

A narrative prompt alone is not a runnable case.

A Role Relevance Map is a recommended enhancement, not an absolute `case-ready` requirement. Removing role relevance must not make the core task unusable or unreviewable.

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

## Output basis

Keep these output-basis classes separate:

- `explicit` — an output directly named or requested in qualifying private evidence;
- `inferred` — an output derived from the bounded workflow logic but not directly named in qualifying evidence;
- `case-designed` — an output created to make the synthetic exercise usable and reviewable.

The public case may use the normalized output class without exposing named-employer evidence. It must not present an `inferred` or `case-designed` output as an observed employer requirement.

These output-basis values are distinct from Role Relevance basis values. Role relationships use `evidence-observed`, `workflow-inferred`, or `case-designed`.

Public learner deliverables are normally `case-designed`, even where their structure is informed by an explicit or inferred normalized output class.

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

- `performs`;
- `contributes`;
- `reviews`;
- `consumes`;
- `authorizes/owns`.

Where used, classify the relationship as:

- `evidence-observed`;
- `workflow-inferred`;
- `case-designed`.

Role relevance supports navigation and learning. It does not establish universal job ownership, current hiring demand, professional authorization, or approval authority. Role relevance completeness is separate from case maturity.

## Required tools

Every case overview must state the tools required to complete the work.

- If no specialized tool is required, state `none` or describe the ordinary editor or spreadsheet capability needed.
- Distinguish required tools from accepted equivalents and optional implementation choices.
- Do not convert a technology observed in one source or preferred by a maintainer into a universal requirement.
- A product or version may be mandatory only when the synthetic task genuinely depends on it and the requirement is disclosed before the learner starts.

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

## External resources and public value

A `case-ready`, `pilot-tested`, or `validated-case` package must contain at least one relevant non-recruitment public resource. A `proposed` or `design-ready` package may omit it while design is incomplete.

For each included resource, explain:

- what it helps the learner understand or perform;
- what it does not establish;
- why it is not merely decorative.

After removing all maintainer-owned links, can a user still understand the scenario, inspect the inputs, complete the task, produce a deliverable, and apply the review criteria?

If not, the case is not ready.

## Case maturity and release gates

| Status | Meaning |
| --- | --- |
| `proposed` | Only the case concept exists. |
| `design-ready` | Scenario, task, and input design are complete. |
| `case-ready` | Inputs, deliverables, output format, scoring, reviewer guidance, authority boundaries, required tools, external resources, and independent review are complete. |
| `pilot-tested` | At least one independent participant completed the case and supplied feedback. |
| `validated-case` | Repeated use and material revision have stabilized the package. |

Public `main` should normally contain only `case-ready` or more mature cases.

A case must not be marked `case-ready`, published, or merged merely because a private candidate is qualified or a design packet exists. Explicit transfer approval and complete public case review remain separate gates. Case maturity does not strengthen employer evidence.

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

Files under `workflows/` and `challenges/`, together with `schemas/workflow-entry.schema.yaml`, were created under the pre-v2.1 employer-evidence-centred model. They are retained for history and may be migrated only through a separate reviewed change.

Do not use a legacy workflow page as the template for a new case.

## Review and correction

Before release, inspect the complete package for:

- fictional independence;
- internal consistency across scenario, inputs, task, rubric, and answer;
- private-information leakage;
- unsupported authority;
- output-basis confusion;
- adjacent-workflow confusion;
- hidden dependencies;
- misleading claims;
- licensing and source-attribution issues.

Prefer fewer defensible cases over a large collection of shallow exercises. Narrow, hold, revise, or retire a case rather than inventing plausible content.
