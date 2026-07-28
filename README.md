# Awesome GRC Workflows

Evidence-backed work tasks, required outputs, human boundaries, technical capabilities, and practice challenges across GRC, technology risk, audit, resilience, and compliance roles.

> Status: early public index. Entries describe observed work demand and synthetic practice opportunities. They do not prove a control failure, compliance gap, software buying intent, market size, or full automability.

## What this repository is

This repository organizes recurring work observed in GRC, technology risk, IT audit, operational resilience, third-party risk, cybersecurity governance, and compliance roles.

Each workflow is described through a common structure:

- **Observed work task** — the action an employer expects someone to perform.
- **Required output** — an explicitly requested or cautiously inferred deliverable, record, analysis, or evidence package.
- **Human boundary** — the judgment, authorization, risk acceptance, or sign-off that remains accountable to a person or authorized role.
- **Technical capabilities** — practical capabilities derived from the work rather than added because they are generally popular.
- **Automation boundary** — what may be collected, compared, validated, or reported automatically, and where authorization and accountability remain external to the automation.
- **Practice challenge** — an optional synthetic exercise for learning or assessment.

## What this repository is not

This is not:

- a general directory of GRC products, certifications, books, or regulations;
- a claim that every listed workflow should be automated;
- evidence that an employer has a control deficiency;
- evidence of software budget or purchasing intent;
- a substitute for legal, regulatory, audit, or risk advice;
- a collection of confidential employer procedures or production data.

## Evidence maturity

Evidence maturity describes the strength of the public demand pattern. It does not describe challenge quality.

| Status | Meaning |
| --- | --- |
| `observed` | The work task has been observed in at least one qualifying public demand source. |
| `repeated` | Substantially similar work has been observed in at least two independent employer demand sources. |
| `candidate` | The task recurs across at least three independent employer demand sources and the task, output, and human boundary are sufficiently stable to justify a reusable workflow entry. |

Practitioner discussions, standards, regulatory material, and product documentation may clarify context, failure modes, or constraints. They do not substitute for independent employer demand sources when advancing demand maturity.

## Challenge maturity

Challenge maturity describes the state of the synthetic exercise, not the strength of market evidence.

| Status | Meaning |
| --- | --- |
| `none` | No exercise has been proposed. |
| `proposed` | A bounded exercise concept exists, but inputs or evaluation criteria remain incomplete. |
| `challenge-ready` | A synthetic scenario, input set, required deliverables, and evaluation dimensions have been designed. |
| `pilot-tested` | At least one external participant has completed the exercise and supplied feedback. |
| `validated-pattern` | Repeated use and feedback have materially revised and stabilized the exercise and evaluation model. |

Neither status is a quality score for an employer, product, profession, or control environment.

## Workflow domains

The initial scope includes:

- access review, IAM, and privileged access;
- technology control testing;
- evidence collection, validation, lineage, and freshness;
- continuous control monitoring and configuration drift;
- operational resilience, BCP, and disaster recovery exercises;
- incident evidence and post-incident review;
- remediation validation and control retesting;
- third-party technology risk;
- cloud and change-control assurance;
- AI governance and model-risk operations.

## Repository structure

```text
.
├── README.md
├── CONTRIBUTING.md
├── METHODOLOGY.md
├── LICENSE
├── schemas/
│   └── workflow-entry.schema.yaml
└── workflows/
    ├── README.md
    └── _template.md
```

## Entry requirements

A workflow entry should:

1. describe a concrete work action rather than a broad job title;
2. distinguish explicitly observed outputs from outputs inferred during normalization;
3. state where accountable human judgment or authorization remains necessary;
4. distinguish observed demand from inferred automation opportunity;
5. identify independent employer demand sources separately from contextual sources;
6. link to public evidence where licensing and source stability permit;
7. label all invented organizations, records, policies, and datasets as synthetic;
8. avoid reproducing confidential, personal, or production information.

See [METHODOLOGY.md](METHODOLOGY.md) for the evidence model and [CONTRIBUTING.md](CONTRIBUTING.md) for submission rules.

## Planned first workflows

The first candidate set is expected to cover:

- privileged access recertification;
- leaver and orphan-account reconciliation;
- evidence freshness assessment;
- remediation evidence validation;
- technology-risk finding closure;
- control testing and evidence packaging;
- firewall-rule recertification;
- DR exercise evidence review;
- post-incident evidence sufficiency review;
- third-party technology-risk assessment.

These are backlog candidates, not yet validated entries.

## License

Unless a file states otherwise, original repository content is licensed under the Creative Commons Attribution 4.0 International Public License. Third-party source material remains subject to its original rights and is not relicensed by this repository.