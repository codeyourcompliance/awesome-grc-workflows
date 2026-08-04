#!/usr/bin/env python3
"""Validate the v2.1 public case-library foundation."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED = [
    "README.md",
    "METHODOLOGY.md",
    "CONTRIBUTING.md",
    "cases/README.md",
    "cases/_template/README.md",
    "cases/_template/scenario.md",
    "cases/_template/task-brief.md",
    "cases/_template/inputs/README.md",
    "cases/_template/templates/deliverable-template.md",
    "cases/_template/scoring-rubric.md",
    "cases/_template/reviewer-guide.md",
    "cases/_template/reference-answer.md",
    "cases/_template/metadata.yaml",
    "schemas/case-entry.schema.yaml",
    "schemas/workflow-entry.schema.yaml",
    "workflows/README.md",
    "workflows/_template.md",
    "workflows/remediation-effectiveness-validation.md",
    "challenges/README.md",
]

OPTIONAL = ["cases/_template/role-relevance.md"]

BANNED_TEMPLATE_PATTERNS = [
    r"\b(?:SRC|EMP|WFA|CG|MIR)-\d+\b",
    r"(?:sources/employer/|qualification-reviews/|case-design-packets/|transfer-records/)",
    r"(?:linkedin\.com/jobs|efinancialcareers\.com/jobs|myworkdayjobs\.com)",
]

ACTIVE_CASE_DOCS = [
    "README.md",
    "METHODOLOGY.md",
    "CONTRIBUTING.md",
    "cases/README.md",
    "cases/_template/README.md",
    "cases/_template/metadata.yaml",
    "schemas/case-entry.schema.yaml",
]

LEGACY_MATURITY_TERMS = ["validated-pattern", "status: draft", "- retired"]

ROLE_RELATIONSHIPS = [
    "`performs`",
    "`contributes`",
    "`reviews`",
    "`consumes`",
    "`authorizes/owns`",
]

OBSOLETE_ROLE_RELATIONSHIPS = [
    "`perform`",
    "`contribute`",
    "`review`",
    "`consume`",
    "`authorize/own`",
]


def extract_section(text: str, heading: str) -> str:
    marker = f"## {heading}"
    if marker not in text:
        return ""
    remainder = text.split(marker, 1)[1]
    return remainder.split("\n## ", 1)[0]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    root = Path(parser.parse_args().root).resolve()
    errors: list[str] = []

    def read(relative: str, required: bool = True) -> str:
        path = root / relative
        if not path.is_file():
            if required:
                errors.append(f"missing required path: {relative}")
            return ""
        return path.read_text(encoding="utf-8")

    docs = {relative: read(relative) for relative in REQUIRED}
    optional_docs = {
        relative: read(relative, required=False)
        for relative in OPTIONAL
        if (root / relative).is_file()
    }

    required_markers = {
        "README.md": [
            "Runnable synthetic GRC work-sample cases",
            "`cases/` is the active public product surface",
            "No v2.1 case is published yet",
            "## Private-to-public gate",
            "explicit transfer approval",
            "required tools",
            "`design-ready`",
            "`validated-case`",
        ],
        "METHODOLOGY.md": [
            "Private Evidence Engine",
            "Normalized Bounded Workflow",
            "Public Synthetic Case Package",
            "## Private-to-public transfer gate",
            "sanitized case-design packet",
            "explicit transfer approval",
            "## Public case identity",
            "A public case ID must be independently assigned",
            "## Output basis",
            "## Assumption rules",
            "## Required tools",
            "explicitly labelled `Synthetic Scenario`",
            "The reviewer guide and reference answer are separate artifacts",
            "the preferred answer or preferred conditional answer",
            "unsupported answers and why they fail",
            "assumptions that materially change the result",
            "evidence needed to resolve material uncertainty",
            "Technical capability, access, or automation does not create authorization",
            "A Role Relevance Map is a recommended enhancement",
            "must contain at least one relevant non-recruitment public resource",
        ],
        "CONTRIBUTING.md": [
            "Use `cases/_template/`",
            "## Qualification and transfer prerequisite",
            "sanitized case-design packet",
            "explicit transfer approval",
            "## Public case identity",
            "Private candidate review",
            "A Role Relevance Map is recommended but optional",
            "No stage automatically authorizes the next",
            "permitted assumptions",
            "minimum passing evidence",
            "required tools",
            "`validated-case`",
        ],
        "cases/README.md": [
            "This directory is the active public product surface",
            "## Entry gate",
            "explicit transfer approval",
            "required tools",
            "Role relevance is optional",
            "`design-ready`",
            "`validated-case`",
        ],
        "workflows/README.md": ["Legacy Workflows", "Do not add new workflow entries here"],
        "workflows/_template.md": ["Do Not Use", "cases/_template/"],
        "workflows/remediation-effectiveness-validation.md": [
            "Legacy pre-v2.1 workflow entry",
            "not a current runnable synthetic case",
        ],
        "schemas/workflow-entry.schema.yaml": [
            "Legacy Awesome GRC Workflow Entry Frontmatter (pre-v2.1)",
            "Retained for validation of historical workflow entries only",
        ],
        "challenges/README.md": [
            "Legacy Challenge Guidance",
            "Do not add new standalone challenge entries here",
        ],
        "cases/_template/README.md": [
            "`metadata.yaml` is the canonical machine-readable source",
            "This case uses a fictional organization",
            "## Public case ID",
            "## Required tools",
            "## Authority boundary",
            "optional employer-agnostic role-family map",
        ],
        "cases/_template/scenario.md": [
            "# Synthetic Scenario",
            "## Fictional organization",
            "## Synthetic disclaimer",
        ],
        "cases/_template/task-brief.md": [
            "## Required tools",
            "## Required deliverables",
            "## Assumption rules",
            "### Permitted assumptions",
            "### Prohibited assumptions",
            "### When evidence is insufficient",
            "## Excluded scope",
        ],
        "cases/_template/scoring-rubric.md": [
            "## Critical errors",
            "Authority-boundary discipline",
        ],
        "cases/_template/reviewer-guide.md": [
            "## Acceptable answer range",
            "## Professional judgment",
            "## Authority checks",
            "## Blocking errors",
            "## Common mistakes",
            "## Minimum passing evidence",
        ],
        "cases/_template/reference-answer.md": [
            "one defensible response",
            "## Preferred answer",
            "## Acceptable alternatives",
            "## Unsupported answers",
            "## Assumptions that change the result",
            "## Evidence needed to resolve uncertainty",
        ],
    }

    for relative, markers in required_markers.items():
        for marker in markers:
            if marker not in docs[relative]:
                errors.append(f"{relative}: missing marker {marker!r}")

    metadata = docs["cases/_template/metadata.yaml"]
    for field in [
        "status: proposed",
        "required_tools:",
        "synthetic_data: true",
        "private_dependency: false",
        "maintainer_service_required: false",
        "pilot_completions: 0",
    ]:
        if field not in metadata:
            errors.append(f"metadata template: missing {field!r}")

    schema = docs["schemas/case-entry.schema.yaml"]
    for marker in [
        "Awesome GRC Workflows Public Case Metadata",
        "- proposed",
        "- design-ready",
        "- case-ready",
        "- pilot-tested",
        "- validated-case",
        "required_tools:",
        "synthetic_data:",
        "const: true",
        "private_dependency:",
        "maintainer_service_required:",
        "public_resources:",
        "minItems: 1",
        "pilot_completions:",
        "not:",
        "^(?:wfa|src|emp|cg|mir|aprprep)-",
    ]:
        if marker not in schema:
            errors.append(f"case schema: missing {marker!r}")

    required_block = (
        schema.split("required:", 1)[1].split("properties:", 1)[0]
        if "required:" in schema and "properties:" in schema
        else ""
    )
    if "- role_families" in required_block:
        errors.append("case schema: role_families must remain optional")
    if "- required_tools" not in required_block:
        errors.append("case schema: required_tools must be required")

    if "enum:\n            - case-ready\n            - pilot-tested\n            - validated-case" not in schema:
        errors.append("case schema: case-ready public-resource condition is missing")

    if docs["cases/_template/README.md"].startswith("---"):
        errors.append("case README duplicates canonical metadata in frontmatter")

    for relative in ACTIVE_CASE_DOCS:
        for term in LEGACY_MATURITY_TERMS:
            if term in docs[relative]:
                errors.append(f"{relative}: obsolete active case maturity term {term!r}")

    output_section = extract_section(docs["METHODOLOGY.md"], "Output basis")
    for marker in ["`explicit`", "`inferred`", "`case-designed`"]:
        if marker not in output_section:
            errors.append(f"methodology output basis: missing {marker!r}")
    for obsolete in ["`employer-observed`", "`workflow-inferred`"]:
        if obsolete in output_section:
            errors.append(
                f"methodology output basis: role-basis term used as output basis {obsolete!r}"
            )

    methodology_role_section = extract_section(docs["METHODOLOGY.md"], "Role relevance")
    for marker in ROLE_RELATIONSHIPS:
        if marker not in methodology_role_section:
            errors.append(f"methodology role relevance: missing relationship {marker!r}")
    for obsolete in OBSOLETE_ROLE_RELATIONSHIPS:
        if obsolete in methodology_role_section:
            errors.append(f"methodology role relevance: obsolete relationship {obsolete!r}")

    role_doc = optional_docs.get("cases/_template/role-relevance.md")
    if role_doc:
        for marker in [
            "optional enhancement",
            "evidence-observed",
            "workflow-inferred",
            "case-designed",
            *ROLE_RELATIONSHIPS,
        ]:
            if marker not in role_doc:
                errors.append(f"role relevance template: missing {marker!r}")
        for obsolete in OBSOLETE_ROLE_RELATIONSHIPS:
            if obsolete in role_doc:
                errors.append(f"role relevance template: obsolete relationship {obsolete!r}")

    template_docs = {
        relative: text
        for relative, text in {**docs, **optional_docs}.items()
        if relative.startswith("cases/_template/")
    }
    private_marker_matches = 0
    for relative, text in template_docs.items():
        for pattern in BANNED_TEMPLATE_PATTERNS:
            if re.search(pattern, text, re.IGNORECASE):
                private_marker_matches += 1
                errors.append(
                    f"{relative}: private-layer or recruitment marker matched {pattern}"
                )

    cases_root = root / "cases"
    public_case_count = 0
    if cases_root.is_dir():
        public_case_count = sum(
            1
            for path in cases_root.iterdir()
            if path.is_dir() and not path.name.startswith("_")
        )

    if errors:
        print("CASE_FOUNDATION_VALIDATION=FAIL")
        for error in errors:
            print(f"ERROR={error}")
        return 1

    print("CASE_FOUNDATION_VALIDATION=PASS")
    print(f"REQUIRED_PATHS_CHECKED={len(REQUIRED)}")
    print("CASE_MATURITY_MODEL=protocol-v2.1")
    print("OUTPUT_BASIS=explicit,inferred,case-designed")
    print("PRIVATE_TO_PUBLIC_GATE=required")
    print("PUBLIC_CASE_ID_INDEPENDENT=true")
    print("SYNTHETIC_SCENARIO_LABEL=required")
    print("ASSUMPTION_RULES=required")
    print("AUTHORITY_OVERVIEW_REQUIRED=true")
    print("REVIEWER_GUIDE_MINIMUMS=required")
    print("REFERENCE_ANSWER_DECISION_RANGE=required")
    print("ROLE_RELEVANCE_REQUIRED=false")
    print("ROLE_RELATIONSHIP_VOCABULARY=protocol-v2.1")
    print("REQUIRED_TOOLS_FIELD=required")
    print("CASE_READY_PUBLIC_RESOURCE_MINIMUM=1")
    print("ACTIVE_PUBLIC_SURFACE=cases")
    print("LEGACY_WORKFLOW_DIRECTORY=retained")
    print("LEGACY_CHALLENGE_DIRECTORY=retained")
    print("LEGACY_PAGE_BANNER=PASS")
    print(f"PUBLIC_CASE_COUNT={public_case_count}")
    print(f"PRIVATE_LAYER_REFERENCES_IN_TEMPLATE={private_marker_matches}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
