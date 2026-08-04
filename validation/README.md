# Validation

Run the public case-library foundation check from the repository root:

```bash
python3 validation/validate_case_foundation.py
```

The validator checks:

- required case package template paths;
- active `cases/` public-surface wording;
- legacy treatment of `workflows/` and `challenges/`;
- canonical `metadata.yaml` ownership;
- case metadata schema markers;
- authority, rubric, reviewer-guide, and reference-answer requirements;
- absence of private-layer IDs, private paths, and recruitment URLs from the public case template.

It is a structural guard. It does not replace substantive case review, fictional-independence review, licensing review, first-principles review, adversarial review, or pilot testing.
