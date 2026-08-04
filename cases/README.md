# Cases

This directory is the active public product surface for Awesome GRC Workflows.

Each directory contains one runnable synthetic work-sample case built around one bounded GRC work action.

## Required structure

A `case-ready` package normally contains:

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
├── role-relevance.md
└── metadata.yaml
```

Use [`_template/`](./_template/README.md) when creating a new case.

## Package rules

A case must:

- use a fictional organization and synthetic or safely constructed data;
- train one bounded work action;
- identify the trigger, inputs, action, decision target, deliverables, exclusions, and failure modes;
- contain enough imperfect evidence to require professional reasoning;
- separate facts, assumptions, inference, recommendations, and authorized decisions;
- state who may analyze, recommend, approve, accept risk, interpret legal requirements, sign off, close remediation, and change production state;
- include review criteria that permit defensible alternative conclusions;
- remain usable without private evidence or maintainer-owned services.

## Standard disclaimer

Every case must include:

> This case uses a fictional organization and synthetic or safely constructed data. It does not represent any named employer’s internal process, systems, controls, authority structure, or records.

## Maturity

| Status | Required treatment |
| --- | --- |
| `draft` | Incomplete or under internal review; do not present as ready for independent use. |
| `case-ready` | Complete package, validation, first-principles review, adversarial review, and independent review passed. |
| `pilot-tested` | At least one independent participant completed the case and supplied feedback. |
| `validated-pattern` | Repeated use materially revised and stabilized the package. |
| `retired` | Retained for lineage but no longer current practice material. |

## Current cases

No v2.1 public case has been released yet.

Do not add placeholder case directories merely to increase the case count.
