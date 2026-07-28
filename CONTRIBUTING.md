# Contributing

Contributions should improve evidence quality, clarity, or practical usefulness. Volume alone is not a goal.

## Before submitting

Confirm that the proposed entry:

- describes a concrete work action;
- distinguishes employer demand sources from contextual sources;
- identifies whether each required output is explicit or inferred;
- states the human judgment, authorization, or approval boundary;
- distinguishes observed evidence from normalization and automation inference;
- uses public, independently accessible sources;
- contains no confidential, personal, or production data;
- does not infer a control failure, software budget, market gap, or universal workflow from a job description;
- labels invented organizations, policies, systems, errors, and datasets as synthetic.

## Submission types

### New workflow

Use `workflows/_template.md` and complete all required sections.

### Evidence update

Add an independent employer demand source, add contextual evidence, correct a source date, narrow a claim, or update demand maturity.

### Challenge proposal

A proposal should define the scenario, inputs, required deliverables, evaluation dimensions, likely false positives, uncertainties, and authorization boundary. A narrative prompt alone is not sufficient.

### Correction or withdrawal

Open an issue or pull request when an entry is stale, duplicated, unsupported, misleading, based on copied sources, or no longer meets its stated maturity threshold.

## Source handling

Prefer official employer pages for demand evidence. Use official documentation, standards bodies, regulators, and first-person practitioner material as contextual evidence.

Do not copy substantial portions of job descriptions or articles. Quote only the minimum necessary phrase and provide a link, observation date, source class, and concise interpretation.

A job-board mirror and the original employer posting count as one underlying source. Several copied postings do not establish recurrence.

## Demand maturity changes

Demand maturity requires independent employer evidence:

- `observed` to `repeated`: a second independent employer demand source;
- `repeated` to `candidate`: at least three independent employer demand sources plus a sufficiently stable task, output, and human boundary.

Contextual sources may strengthen interpretation but do not substitute for employer demand sources.

## Challenge maturity changes

Challenge maturity is independent of demand maturity:

- `none` to `proposed`: a bounded exercise concept exists;
- `proposed` to `challenge-ready`: synthetic inputs, required deliverables, and evaluation dimensions are complete;
- `challenge-ready` to `pilot-tested`: external completion and feedback are documented;
- `pilot-tested` to `validated-pattern`: repeated feedback has caused material revision and stabilization.

Maintainers may downgrade either status when evidence expires or assumptions prove unstable.

## Style

Use plain language. Prefer specific actions such as "reconcile HR and directory records" over broad labels such as "perform IAM governance."

Separate facts, normalization choices, interpretation, and challenge-design decisions. Avoid marketing language, unsupported market-size claims, claims of full automation, and claims that a named technology is universally required.

## Pull requests

A pull request should explain:

- what changed;
- which employer demand evidence supports the change;
- which contextual sources were used;
- what is explicit and what is inferred;
- what remains uncertain;
- whether demand maturity or challenge maturity changes, and why.

By contributing original material, you agree that it may be distributed under the repository license. Do not submit material you do not have the right to share.