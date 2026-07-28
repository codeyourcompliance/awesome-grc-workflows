# Contributing

Contributions should improve the evidence quality, clarity, or practical usefulness of a workflow. Volume alone is not a goal.

## Before submitting

Confirm that the proposed entry:

- describes a concrete work action;
- identifies a required output;
- states the human judgment or approval boundary;
- distinguishes observed evidence from inference;
- uses public, independently accessible sources;
- contains no confidential, personal, or production data;
- does not infer a control failure or software budget from a job description;
- labels invented organizations, policies, and datasets as synthetic.

## Submission types

### New workflow

Use `workflows/_template.md` and complete all required sections.

### Evidence update

Add a new independent source, correct a source date, narrow a claim, or update maturity status.

### Challenge proposal

A proposal should define the scenario, inputs, required deliverables, evaluation dimensions, likely false positives, and human boundary. A narrative prompt alone is not sufficient.

### Correction or withdrawal

Open an issue or pull request when an entry is stale, duplicated, unsupported, misleading, or based on copied sources.

## Source handling

Prefer official employer pages, official documentation, standards bodies, regulators, and first-person practitioner material.

Do not copy substantial portions of job descriptions or articles. Quote only the minimum necessary phrase and provide a link, observation date, and concise interpretation.

A job-board mirror and the original employer posting count as one underlying source. Several copied postings do not establish recurrence.

## Workflow status changes

Status advancement requires evidence:

- `observed` to `repeated`: an additional independent observation;
- `repeated` to `candidate`: stable task, output, and human boundary;
- `candidate` to `challenge-ready`: bounded synthetic materials and evaluation dimensions;
- `challenge-ready` to `pilot-tested`: documented external completion and feedback;
- `pilot-tested` to `validated-pattern`: repeated feedback and material revision.

Maintainers may downgrade a status when evidence expires or assumptions prove unstable.

## Style

Use plain language. Prefer specific actions such as "reconcile HR and directory records" over broad labels such as "perform IAM governance."

Separate facts, interpretation, and design decisions. Avoid marketing language, unsupported market-size claims, and claims of full automation.

## Pull requests

A pull request should explain:

- what changed;
- which evidence supports the change;
- what remains uncertain;
- whether the change affects challenge design or maturity status.

By contributing original material, you agree that it may be distributed under the repository license. Do not submit material you do not have the right to share.
