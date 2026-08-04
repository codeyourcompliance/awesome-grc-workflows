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
    "cases/_template/role-relevance.md",
    "cases/_template/metadata.yaml",
    "schemas/case-entry.schema.yaml",
    "workflows/README.md",
    "workflows/_template.md",
    "challenges/README.md",
]

TEMPLATE_FILES = [path for path in REQUIRED if path.startswith("cases/_template/")]
BANNED_TEMPLATE_PATTERNS = [
    r"\b(?:SRC|EMP|WFA|CG|MIR)-\d+\b",
    r"(?:sources/employer/|qualification-reviews/|case-design-packets/|transfer-records/)",
    r"(?:linkedin\.com/jobs|efinancialcareers\.com/jobs|myworkdayjobs\.com)",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    root = Path(parser.parse_args().root).resolve()
    errors: list[str] = []

    def read(relative: str) -> str:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing required path: {relative}")
            return ""
        return path.read_text(encoding="utf-8")

    docs = {relative: read(relative) for relative in REQUIRED}

    required_markers = {
        "README.md": [
            "Runnable synthetic GRC work-sample cases",
            "cases/ is the active public product surface",
            "No v2.1 case is published yet",
        ],
        "METHODOLOGY.md": [
            "Private Evidence Engine",
            "Normalized Bounded Workflow",
            "Public Synthetic Case Package",
            "Technical capability, access, or automation does not create authorization",
        ],
        "CONTRIBUTING.md": [
            "Use `cases/_template/`",
            "A `case-ready` submission normally includes",
            "No stage automatically authorizes the next",
        ],
        "workflows/README.md": ["Legacy Workflows", "Do not add new workflow entries here"],
        "workflows/_template.md": ["Do Not Use", "cases/_template/"],
        "challenges/README.md": ["Legacy Challenge Guidance", "Do not add new standalone challenge entries here"],
        "cases/_template/README.md": [
            "`metadata.yaml` is the canonical machine-readable source",
            "This case uses a fictional organization",
        ],
        "cases/_template/task-brief.md": ["## Required deliverables", "## Excluded scope"],
        "cases/_template/scoring-rubric.md": ["## Critical errors", "Authority-boundary discipline"],
        "cases/_template/reviewer-guide.md": ["## Acceptable answer range", "## Authority checks"],
        "cases/_template/reference-answer.md": ["one defensible response", "## Acceptable alternatives"],
        "cases/_template/role-relevance.md": ["evidence-observed", "workflow-inferred", "case-designed"],
    }

    for relative, markers in required_markers.items():
        for marker in markers:
            if marker not in docs[relative]:
                errors.append(f"{relative}: missing marker {marker!r}")

    metadata = docs["cases/_template/metadata.yaml"]
    for field in [
        "status: draft",
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
        "- case-ready",
        "synthetic_data:",
        "const: true",
        "private_dependency:",
        "maintainer_service_required:",
        "pilot_completions:",
    ]:
        if marker not in schema:
            errors.append(f"case schema: missing {marker!r}")

    if docs["cases/_template/README.md"].startswith("---"):
        errors.append("case README duplicates canonical metadata in frontmatter")

    for relative in TEMPLATE_FILES:
        for pattern in BANNED_TEMPLATE_PATTERNS:
            if re.search(pattern, docs[relative], re.IGNORECASE):
                errors.append(f"{relative}: private-layer or recruitment marker matched {pattern}")

    if errors:
        print("CASE_FOUNDATION_VALIDATION=FAIL")
        for error in errors:
            print(f"ERROR={error}")
        return 1

    print("CASE_FOUNDATION_VALIDATION=PASS")
    print(f"REQUIRED_PATHS_CHECKED={len(REQUIRED)}")
    print("ACTIVE_PUBLIC_SURFACE=cases")
    print("LEGACY_WORKFLOW_DIRECTORY=retained")
    print("LEGACY_CHALLENGE_DIRECTORY=retained")
    print("PUBLIC_CASE_COUNT=0")
    print("PRIVATE_TRANSFER_PERFORMED=false")
    return 0


if __name__ == "__main__":
    sys.exit(main())
