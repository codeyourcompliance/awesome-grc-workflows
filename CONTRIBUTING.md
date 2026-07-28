# Contributing

Contributions should improve evidence quality, clarity, or practical usefulness. Volume alone is not a goal.

## Before submitting

Confirm that the proposed public entry:

- describes a concrete work action;
- is supported by at least three independent employers;
- distinguishes employer evidence from contextual evidence;
- identifies whether each required output is explicit or inferred;
- states the human judgment, authorization, or approval boundary, or marks it unresolved;
- distinguishes observed evidence from normalization and automation inference;
- uses public, independently accessible sources;
- contains no confidential, personal, or production data;
- does not infer a control failure, software budget, market gap, or universal workflow from a job description;
- labels invented organizations, policies, systems, errors, and datasets as synthetic.

## Submission types

### New workflow

Use `workflows/_template.md` and complete all required sections. New workflow files must already meet the publication threshold.

### Evidence update

Add an independent employer, add a qualifying source for an existing employer, add contextual evidence, correct a source date, or narrow a claim.

### Challenge proposal

A proposal should define the scenario, inputs, required deliverables, evaluation dimensions, likely false positives, uncertainties, and authorization boundary. A narrative prompt alone is not sufficient.

### Correction or withdrawal

Open an issue or pull request when an entry is stale, duplicated, unsupported, misleading, based on copied sources, or no longer meets the publication threshold.

## Source handling

Prefer official employer pages for employer evidence. Use official documentation, standards bodies, regulators, first-person practitioner material, incident reports, and product documentation as contextual evidence.

Do not copy substantial portions of job descriptions or articles. Quote only the minimum necessary phrase and provide a link, observation date, source class, and concise interpretation.

Count independence at employer level:

- a job-board mirror and the original employer posting count as one source record;
- multiple postings, locations, or business units from one employer count as one employer;
- entities under one ultimate corporate parent are conservatively counted as one employer unless independence is documented with public evidence.

## Publication requirements

A new workflow requires:

- at least three independent employers;
- a sufficiently stable task, output, and human boundary;
- documented alternative explanations;
- public evidence that allows independent inspection;
- completed first-principles and adversarial review.

Contextual evidence may strengthen interpretation but does not substitute for independent employers.

## Challenge maturity changes

Challenge maturity is independent of workflow evidence:

- `none` to `proposed`: a bounded exercise concept exists;
- `proposed` to `challenge-ready`: synthetic inputs, required deliverables, and evaluation dimensions are complete;
- `challenge-ready` to `pilot-tested`: external completion and feedback are documented;
- `pilot-tested` to `validated-pattern`: repeated feedback has caused material revision and stabilization.

Maintainers may downgrade challenge status or withdraw a workflow when evidence expires or assumptions prove unstable.

## Style

Use plain language. Prefer specific actions such as "reconcile HR and directory records" over broad labels such as "perform IAM governance."

Separate facts, normalization choices, interpretation, and challenge-design decisions. Avoid marketing language, unsupported market-size claims, claims of full automation, and claims that a named technology is universally required.

## Pull requests

A pull request should explain:

- what changed;
- which independent employers support the workflow;
- which qualifying sources support each employer;
- which contextual sources were used;
- what is explicit and what is inferred;
- what remains uncertain;
- whether challenge maturity changes, and why.

By contributing original material, you agree that it may be distributed under the repository license. Do not submit material you do not have the right to share.
