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
├── metadata.yaml
└── role-relevance.md        # optional enhancement
```

Use [`_template/`](./_template/README.md) when creating a new case.

## Entry gate

A public case must not bypass private workflow qualification. Before public design begins, maintainers must confirm that the bounded workflow passed qualification, an employer-agnostic normalized workflow and sanitized case-design packet exist, and explicit transfer approval was granted separately.

Only approved sanitized content may inform the public case. Private evidence, named employers, recruitment URLs, private identifiers, qualification records, internal scoring, private paths, and transfer records must not be added here.

## Package rules

A case must:

- use a fictional organization and synthetic or safely constructed data;
- train one bounded work action;
- identify the trigger, inputs, action, decision target, deliverables, exclusions, and failure modes;
- state required tools and distinguish them from accepted equivalents and optional tools;
- contain enough imperfect evidence to require professional reasoning;
- separate facts, assumptions, inference, recommendations, and authorized decisions;
- state who may analyze, recommend, approve, accept risk, interpret legal requirements, sign off, close remediation, and change production state;
- include review criteria that permit defensible alternative conclusions;
- remain usable without private evidence or maintainer-owned services.

A `case-ready` or more mature case must include at least one relevant non-recruitment public resource, with its relevance and limitation explained.

Role relevance is optional. Where included, it must remain employer-agnostic and must not create unsupported ownership or authority.

## Standard disclaimer

Every case must include:

> This case uses a fictional organization and synthetic or safely constructed data. It does not represent any named employer’s internal process, systems, controls, authority structure, or records.

## Maturity

| Status | Required treatment |
| --- | --- |
| `proposed` | Only the case concept exists. |
| `design-ready` | Scenario, task, and input design are complete. |
| `case-ready` | Inputs, required tools, deliverables, output format, scoring, reviewer guidance, authority boundary, external resource, validation, and independent review are complete. |
| `pilot-tested` | At least one independent participant completed the case and supplied feedback. |
| `validated-case` | Repeated use materially revised and stabilized the package. |

Public `main` should normally contain only `case-ready` or more mature cases.

## Current cases

No v2.1 public case has been released yet.

Do not add placeholder case directories merely to increase the case count.
