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

## Public case identity

Assign each public case an independently created public ID. Do not reuse a private candidate, source, employer, employer-group, packet, preparation, or transfer identifier, and do not expose a reversible public-to-private mapping.

## Package rules

A case must:

- use a fictional organization and synthetic or safely constructed data;
- train one bounded work action;
- identify the trigger, inputs, action, decision target, deliverables, exclusions, and failure modes;
- state required tools and distinguish them from accepted equivalents and optional tools;
- define permitted assumptions, prohibited assumptions, and the response required when evidence is insufficient;
- contain enough imperfect evidence to require professional reasoning;
- separate facts, assumptions, inference, recommendations, and authorized decisions;
- state who may analyze, recommend, approve, accept risk, interpret legal requirements, sign off, close remediation, and change production state;
- include a reviewer guide covering blocking errors, common mistakes, minimum passing evidence, professional judgment, partial credit, and authority checks;
- include a separate reference answer representing one defensible response and acceptable alternatives;
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
| `case-ready` | Inputs, assumption rules, required tools, deliverables, output format, scoring, complete reviewer guidance, reference answer, authority boundary, external resource, validation, and independent review are complete. |
| `pilot-tested` | At least one independent participant completed the case and supplied feedback. |
| `validated-case` | Repeated use materially revised and stabilized the package. |

Public `main` should normally contain only `case-ready` or more mature cases.

## Current cases

- [Remediation Evidence Closure Review](remediation-evidence-closure-review/README.md) — review a synthetic remediation closure package against six documented requirements and prepare a closure-readiness recommendation. Status: `case-ready`.

Do not add placeholder case directories merely to increase the case count.
