# Awesome GRC Workflows

Evidence-backed work tasks, required outputs, human boundaries, technical capabilities, and practice challenges across GRC, technology risk, audit, resilience, and compliance roles.

> Status: early public curated index. Published entries describe recurring, publicly observable work. They do not prove a control failure, compliance gap, software buying intent, market size, or full automability.

## What this repository is

This repository organizes recurring work observed across GRC, technology risk, IT audit, operational resilience, third-party risk, cybersecurity governance, and compliance roles.

Each published workflow uses a common structure:

- **Observed work task** — the action employers expect someone to perform.
- **Required output** — an explicitly requested or cautiously inferred deliverable, record, analysis, or evidence package.
- **Human boundary** — the judgment, authorization, risk acceptance, or sign-off that remains accountable to a person or authorized role.
- **Technical capabilities** — practical capabilities derived from the work rather than added because they are generally popular.
- **Automation boundary** — what may be collected, compared, validated, or reported automatically, and where authorization and accountability remain external to the automation.
- **Practice challenge** — an optional synthetic exercise for learning or assessment.

## What this repository is not

This is not:

- a general directory of GRC products, certifications, books, or regulations;
- a job-posting archive or market-wide census;
- a claim that every listed workflow should be automated;
- evidence that an employer has a control deficiency;
- evidence of software budget or purchasing intent;
- a substitute for legal, regulatory, audit, or risk advice;
- a collection of confidential employer procedures or production data.

## Publication criteria

A workflow is published only when:

1. substantially similar work is supported by at least three independent employers;
2. the normalized task is narrow enough to describe operationally;
3. required outputs are either explicitly supported or clearly marked as inferred;
4. human authorization and accountability boundaries are stated or marked unresolved;
5. alternative explanations have been considered;
6. all supporting evidence is public and independently inspectable.

Independence is counted at employer level, not by number of links or postings. Multiple roles, reposts, job-board mirrors, locations, or business units from one employer count as one employer. Entities under the same ultimate corporate parent are conservatively counted as one employer unless independence is documented.

Practitioner discussions, standards, regulatory material, incident reports, and product documentation may clarify context, failure modes, terminology, or implementation options. They do not substitute for independent employer evidence when deciding whether a workflow qualifies for publication.

## Challenge maturity

Challenge maturity describes the state of the synthetic exercise, not the strength of the workflow evidence.

| Status | Meaning |
| --- | --- |
| `none` | No exercise has been proposed. |
| `proposed` | A bounded exercise concept exists, but inputs or evaluation criteria remain incomplete. |
| `challenge-ready` | A synthetic scenario, input set, required deliverables, and evaluation dimensions have been designed. |
| `pilot-tested` | At least one external participant has completed the exercise and supplied feedback. |
| `validated-pattern` | Repeated use and feedback have materially revised and stabilized the exercise and evaluation model. |

A published workflow may have no challenge. A polished challenge does not strengthen the underlying workflow evidence.

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

A published workflow entry must:

1. describe a concrete work action rather than a broad job title;
2. be supported by at least three independent employers;
3. distinguish explicitly observed outputs from outputs inferred during normalization;
4. state where accountable human judgment or authorization remains necessary, or mark the authority as unresolved;
5. distinguish employer evidence from inferred automation opportunity;
6. identify employer evidence separately from contextual evidence;
7. link to public evidence where licensing and source stability permit;
8. label all invented organizations, records, policies, systems, errors, and datasets as synthetic;
9. avoid reproducing confidential, personal, or production information.

See [METHODOLOGY.md](METHODOLOGY.md) for the evidence model and [CONTRIBUTING.md](CONTRIBUTING.md) for submission rules.

## License

Unless a file states otherwise, original repository content is licensed under the [Creative Commons Attribution 4.0 International Public License](LICENSE). Third-party source material remains subject to its original rights and is not relicensed by this repository.
