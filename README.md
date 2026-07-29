# Awesome GRC Workflows

Evidence-backed work tasks, required outputs, human boundaries, technical capabilities, external resources, and practice challenges across GRC, technology risk, audit, resilience, and compliance roles.

> Status: early public curated index. Published entries describe recurring, publicly observable work. They do not prove a control failure, compliance gap, skill shortage, software buying intent, market size, or full automability.

## What this repository is

This repository organizes recurring work observed across GRC, technology risk, IT audit, operational resilience, third-party risk, cybersecurity governance, and compliance roles.

It combines two public layers:

1. **Awesome curation** — employer evidence, official guidance, open-source tools, external articles, implementation cases, courses, labs, datasets, and external challenges.
2. **Normalized workflow analysis** — bounded work tasks, required outputs, human boundaries, technical capabilities, automation boundaries, evidence limitations, and optional original synthetic challenges.

Each published workflow uses a common structure:

- **Observed and normalized work task** — the source wording and the bounded action derived from it.
- **Required output** — an explicitly requested or cautiously inferred deliverable, record, analysis, or evidence package.
- **Human boundary** — the judgment, authorization, risk acceptance, or sign-off that remains accountable to a person or authorized role.
- **Technical capabilities** — employer-requested technologies, workflow-derived capabilities, and optional implementation choices kept separate.
- **Automation boundary** — what may be collected, compared, validated, or reported automatically, and where authorization and accountability remain external to the automation.
- **External resources** — non-recruitment material selected for learning, implementation context, inspection, or practice.
- **Practice resources** — external exercises and optional original synthetic challenges kept separate.

## What this repository is not

This is not:

- a general directory of GRC products, certifications, books, or regulations;
- a job-posting archive or market-wide census;
- evidence of a skill shortage, inability to hire, market gap, workflow gap, or unmet demand;
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
6. all supporting evidence is public and independently inspectable;
7. source lifecycle information is recorded;
8. first-principles and adversarial review are complete.

Independence is counted at employer level, not by number of links or postings. Multiple roles, reposts, job-board mirrors, locations, or business units from one employer count as one employer. Entities under the same ultimate corporate parent are conservatively counted as one employer unless independence is documented.

Practitioner discussions, standards, regulatory material, incident reports, open-source projects, and product documentation may clarify context, failure modes, terminology, or implementation options. They do not substitute for independent employer evidence when deciding whether a workflow qualifies for publication.

Each workflow should normally include at least one relevant non-recruitment external resource. Weak links are not added merely to satisfy a quota.

## Independent value test

Every page must pass this test:

> After removing all maintainer-owned links, is the page still worth reading, saving, and citing?

A page should still let readers understand the work, inspect the evidence, find external learning resources, and see the technical and accountability boundaries without using a maintainer-owned product or challenge.

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
├── workflows/
│   ├── README.md
│   └── _template.md
├── resources/
│   └── README.md
└── challenges/
    └── README.md
```

- `workflows/` contains evidence-backed normalized work actions.
- `resources/` defines and curates external resources that provide independent public value.
- `challenges/` distinguishes external practice resources from original synthetic challenges.

A browsable workflow and resource index will be added as qualifying entries are published. Empty categories and unsupported entries are not added merely to make the repository appear complete.

## Entry requirements

A published workflow entry must:

1. describe a concrete work action rather than a broad job title;
2. be supported by at least three independent employers;
3. distinguish source wording from the normalized task;
4. distinguish explicitly observed outputs from outputs inferred during normalization;
5. state where accountable human judgment or authorization remains necessary, or mark the authority as unresolved;
6. distinguish employer-requested technologies, workflow-derived capabilities, and optional implementation choices;
7. distinguish employer evidence, contextual evidence, external resources, and inferred automation opportunity;
8. retain source dates, status, minimal supporting signals, and independence notes;
9. label all invented organizations, records, policies, systems, errors, and datasets as synthetic;
10. avoid reproducing confidential, personal, production, commercial, or non-public research information.

See [METHODOLOGY.md](METHODOLOGY.md) for the evidence model and [CONTRIBUTING.md](CONTRIBUTING.md) for submission rules.

## License

Unless a file states otherwise, original repository content is licensed under the [Creative Commons Attribution 4.0 International Public License](LICENSE). Third-party source material remains subject to its original rights and is not relicensed by this repository.
