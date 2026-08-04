# Input Package

List and describe every synthetic input supplied to the learner.

| File | Evidence type | Purpose | Known limitation |
| --- | --- | --- | --- |
| `replace-with-input.ext` | Record, policy, export, log, register, or correspondence | What the learner should use it for | Missing field, stale date, ambiguity, or other designed limitation |

## Input design checks

The package should contain enough information to perform the bounded action while requiring professional reasoning.

Where relevant, include:

- one material issue;
- one plausible false positive or non-issue;
- one missing, stale, inconsistent, duplicated, ambiguous, or unsupported item;
- identifiers, timestamps, owners, versions, and provenance fields needed for traceability;
- authorized criteria where comparison is expected;
- explicit gaps where criteria or authority are unresolved.

Do not include confidential, personal, production, customer, or employer-internal data.

## File integrity

For binary or structured inputs, document the intended format, expected row or record count, and any integrity hash or validation instruction required by the case.

## Synthetic disclaimer

All inputs in this directory are synthetic or safely constructed for this case.
