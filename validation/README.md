# Validation

Run the public case-library foundation check from the repository root:

```bash
python3 validation/validate_case_foundation.py
```

The validator checks:

- required case package template paths;
- active `cases/` public-surface wording;
- protocol v2.1 case maturity values;
- the private qualification, sanitized-packet, and explicit transfer gate wording;
- output basis as `explicit`, `inferred`, or `case-designed`;
- optional Role Relevance treatment;
- canonical Role Relevance relationship and basis vocabulary;
- required-tools coverage in the overview, task brief, metadata, and schema;
- the `case-ready` non-recruitment public-resource schema condition;
- canonical `metadata.yaml` ownership;
- legacy treatment of `workflows/`, `challenges/`, and the legacy workflow schema;
- a direct legacy banner on the existing workflow page;
- authority, rubric, reviewer-guide, and reference-answer requirements;
- absence of private-layer IDs, private paths, and recruitment URLs from the public case template;
- the current number of non-template case directories.

The validator reports only what it checks. `PRIVATE_LAYER_REFERENCES_IN_TEMPLATE=0` means the scanned template files contain none of the defined private-layer or recruitment markers. It does not prove that a cross-repository transfer did or did not occur, or that transfer approval is valid.

This remains a structural guard. It does not replace YAML or JSON Schema execution, substantive case review, fictional-independence review, licensing review, first-principles review, adversarial review, transfer authorization review, or pilot testing.
