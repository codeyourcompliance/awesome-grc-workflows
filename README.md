# Awesome GRC Workflows

Runnable synthetic GRC work-sample cases for practising bounded professional actions, producing reviewable deliverables, and learning where evidence, judgment, and authority must remain separate.

> Status: case-library foundation. No v2.1 public case has been released yet.

## What this repository is

Awesome GRC Workflows is an evidence-calibrated synthetic case library covering GRC, technology risk, IT audit, operational resilience, cybersecurity governance, third-party risk, AI governance, privacy, and compliance operations.

The public product is a runnable case. Each case should let a learner:

- review realistic but synthetic records and evidence;
- handle missing, stale, inconsistent, or ambiguous information;
- perform one bounded work action;
- produce a professional deliverable;
- separate fact, inference, recommendation, and authorization;
- compare the result with a rubric and reviewer guide.

Public cases do not expose the private evidence engine used to qualify and normalize candidate workflows.

## Public case model

A complete case package normally contains:

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
├── role-relevance.md        # optional enhancement
└── metadata.yaml
```

A case must remain understandable, completable, and reviewable without access to a private repository, hidden evidence, or maintainer-owned service.

## Required boundaries

Every case must:

- use a fictional organization and synthetic or safely constructed data;
- train one bounded work action rather than an entire role or GRC function;
- state included and excluded scope;
- identify required learner deliverables;
- distinguish evidence review, analysis, recommendation, approval, risk acceptance, legal interpretation, remediation closure, sign-off, and production change;
- avoid granting authority merely because the learner can perform analysis or use technical tools;
- label case-designed outputs and any role relationships as such;
- include review criteria that reward justified uncertainty over unsupported certainty.

Technical capability does not create approval rights, closure authority, risk-acceptance authority, legal authority, production authority, or accountability.

## Case maturity

| Status | Meaning |
| --- | --- |
| `proposed` | Only the case concept exists. |
| `design-ready` | Scenario, task, and input design are complete. |
| `case-ready` | Inputs, deliverables, templates, scoring, reviewer guidance, authority boundaries, and required public resources are complete. |
| `pilot-tested` | At least one independent participant completed the case and supplied feedback. |
| `validated-case` | Repeated use and material revision have stabilized the case package. |

Public `main` should normally contain only `case-ready` or more mature cases. A private workflow qualification or prepared design packet does not automatically make a public case `case-ready`.

## Claims this repository does not make

A case does not prove:

- that a named employer uses the synthetic process;
- that an employer has a control weakness;
- current hiring demand, market size, skill shortage, unmet demand, budget, or procurement intent;
- that one role universally owns the work;
- that a named technology is universally required;
- that the task is fully automatable;
- that completing the case creates professional authorization or complete role competence.

## Repository structure

```text
.
├── README.md
├── METHODOLOGY.md
├── CONTRIBUTING.md
├── LICENSE
├── cases/
│   ├── README.md
│   └── _template/
├── schemas/
│   ├── case-entry.schema.yaml
│   └── workflow-entry.schema.yaml
├── resources/
│   └── README.md
├── workflows/
│   └── legacy employer-evidence-centred entries
└── challenges/
    └── legacy challenge guidance
```

- `cases/` is the active public product surface.
- `schemas/case-entry.schema.yaml` defines public case metadata.
- `resources/` contains useful public non-recruitment resources.
- `workflows/`, `challenges/`, and `schemas/workflow-entry.schema.yaml` are retained as pre-v2.1 legacy material until separately migrated or retired.

## Current public cases

No v2.1 case is published yet. New cases must use the package structure and review gates described in [cases/README.md](cases/README.md).

## Legacy content

The existing remediation-effectiveness workflow remains available as a historical pre-v2.1 entry. It is not a v2.1 runnable case and should not be used as the template for new contributions. See [workflows/README.md](workflows/README.md).

## Contributing

Read [METHODOLOGY.md](METHODOLOGY.md) and [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a case, template change, correction, or legacy migration.

## License

Unless a file states otherwise, original repository content is licensed under the [Creative Commons Attribution 4.0 International Public License](LICENSE). Third-party material remains subject to its original rights and is not relicensed by this repository.
