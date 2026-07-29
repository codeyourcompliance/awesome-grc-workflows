# Contributing

Contributions should improve evidence quality, clarity, curation, or practical usefulness. Volume alone is not a goal.

## Before submitting

Confirm that the proposed public entry:

- describes one bounded work action;
- is supported by at least three independent employers;
- distinguishes employer evidence from contextual evidence and external resources;
- identifies whether each required output is explicit or inferred;
- separates employer-requested technologies, workflow-derived capabilities, and optional implementation choices;
- states the human judgment, authorization, or approval boundary, or marks it unresolved;
- distinguishes observed evidence from normalization, automation inference, and synthetic exercise design;
- uses public, independently accessible sources;
- records observation dates, last-checked dates, source status, and independence notes;
- contains no confidential, personal, production, commercial, or non-public research information;
- does not infer a control failure, skill shortage, inability to hire, market gap, workflow gap, unmet demand, software budget, procurement intent, or universal workflow from hiring evidence;
- labels invented organizations, policies, systems, errors, and datasets as synthetic;
- remains useful after removing maintainer-owned links.

## Submission types

### New workflow

Use `workflows/_template.md` and complete all required sections. New workflow files must already meet the publication threshold.

### Evidence update

Add an independent employer, add or replace a qualifying source, update source status, add contextual evidence, correct a date, or narrow a claim.

### Resource update

Add a high-quality external resource only when its relevance is explained. Do not add weak links to satisfy a quota or promotional links that do not provide independent value.

### Challenge proposal

A proposal should define the scenario, inputs, required deliverables, evaluation dimensions, likely false positives, uncertainties, and authorization boundary. A narrative prompt alone is not sufficient.

### Correction or withdrawal

Open an issue or pull request when an entry is stale, duplicated, unsupported, misleading, based on copied sources, or no longer meets the publication threshold.

## Source handling

Prefer official employer pages for employer evidence. Use attributable job-board copies only when the original is unavailable. Use official documentation, standards bodies, regulators, first-person practitioner material, incident reports, open-source documentation, and product documentation as contextual evidence or external resources.

Do not copy substantial portions of job descriptions or articles. Quote only the minimum necessary phrase and provide a link, observation date, last-checked date, source class, status, and concise interpretation.

Count independence at employer level:

- a job-board mirror and the original employer posting count as one source record;
- multiple postings, roles, locations, or business units from one employer count as one employer;
- entities under one ultimate corporate parent are conservatively counted as one employer unless independence is documented with public evidence.

When a source becomes unavailable, mark it accordingly and reassess the publication threshold. Do not silently continue treating a dead link as active evidence.

## Publication requirements

A new workflow requires:

- at least three independent employers;
- a sufficiently stable task, output, and human boundary;
- explicit and inferred outputs kept separate;
- documented alternative explanations;
- public evidence that allows independent inspection;
- at least one relevant non-recruitment external resource, unless its absence is justified;
- completed first-principles and adversarial review.

Contextual evidence and external resources may strengthen interpretation and usefulness but do not substitute for independent employers.

## Challenge maturity changes

Challenge maturity is independent of workflow evidence:

- `none` to `proposed`: a bounded exercise concept exists;
- `proposed` to `challenge-ready`: synthetic inputs, required deliverables, and evaluation dimensions are complete;
- `challenge-ready` to `pilot-tested`: external completion and feedback are documented;
- `pilot-tested` to `validated-pattern`: repeated feedback has caused material revision and stabilization.

Maintainers may downgrade challenge status or withdraw a workflow when evidence expires or assumptions prove unstable.

## Style

Use plain language. Prefer specific actions such as "reconcile HR and directory records" over broad labels such as "perform IAM governance."

Separate facts, source paraphrases, normalization choices, inference, and challenge-design decisions. Avoid marketing language, unsupported market-size claims, gap claims without separate evidence, claims of full automation, and claims that a named technology is universally required.

## Pull requests

A pull request should explain:

- what changed;
- which independent employers support the workflow;
- which qualifying sources support each employer;
- which contextual sources and external resources were used;
- what is explicit and what is inferred;
- how technologies and capabilities were classified;
- what remains uncertain;
- whether source lifecycle or challenge maturity changes;
- how first-principles and adversarial review were performed.

By contributing original material, you agree that it may be distributed under the repository license. Do not submit material you do not have the right to share.
