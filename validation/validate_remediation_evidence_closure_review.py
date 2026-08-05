#!/usr/bin/env python3
"""Validate the public remediation-evidence-closure-review case package."""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

CASE_ID = "remediation-evidence-closure-review"
CASE = Path("cases") / CASE_ID
REQUIRED = [
    "README.md",
    "scenario.md",
    "task-brief.md",
    "scoring-rubric.md",
    "reviewer-guide.md",
    "reference-answer.md",
    "role-relevance.md",
    "metadata.yaml",
    "inputs/README.md",
    "inputs/01-issue-record.md",
    "inputs/02-closure-requirements.csv",
    "inputs/03-remediation-action-plan.md",
    "inputs/04-closure-submission.md",
    "inputs/05-evidence-inventory.csv",
    "inputs/06-change-record.md",
    "inputs/07-post-change-sample-test.md",
    "inputs/08-monitoring-report.csv",
    "inputs/09-management-representation.md",
    "inputs/10-approval-history.csv",
    "inputs/11-account-removal-record.md",
    "templates/evidence-review-workpaper.csv",
    "templates/deficiency-register.csv",
    "templates/closure-readiness-memo.md",
]
BANNED = [
    r"\b(?:WFA|SRC|EMP|CG|MIR|APRPREP)-\d+\b",
    r"(?:case-design-packets/|qualification-reviews/|transfer-records/|sources/employer/)",
    r"(?:linkedin\.com/jobs|myworkdayjobs\.com|efinancialcareers\.com/jobs)",
    r"\b(?:Northern Trust|KPMG|Truist|SMBC|Royal Bank of Canada)\b",
]
DISCLAIMER = "This case uses a fictional organization and synthetic or safely constructed data."
EXPECTED_SUPPLIED = {
    "EV-02": "inputs/06-change-record.md",
    "EV-03": "inputs/07-post-change-sample-test.md",
    "EV-04": "inputs/08-monitoring-report.csv",
    "EV-05": "inputs/09-management-representation.md",
    "EV-06": "inputs/10-approval-history.csv",
    "EV-07": "inputs/11-account-removal-record.md",
}
EXPECTED_UNAVAILABLE = {"EV-01", "EV-08"}


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors: list[str] = []
    docs: dict[str, str] = {}

    for rel in REQUIRED:
        path = root / CASE / rel
        if not path.is_file():
            errors.append(f"missing required file: {CASE / rel}")
            continue
        text = path.read_text(encoding="utf-8")
        docs[rel] = text
        if not text.strip():
            errors.append(f"empty file: {CASE / rel}")
        if "replace with" in text.lower() or "|  |" in text:
            errors.append(f"placeholder content: {CASE / rel}")
        for pattern in BANNED:
            if re.search(pattern, text, re.I):
                errors.append(f"private or employer marker in {CASE / rel}: {pattern}")

    markers = {
        "README.md": [
            DISCLAIMER,
            "## Bounded work action",
            "## Authority boundary",
            "## Relevant public resources",
        ],
        "scenario.md": [
            "# Synthetic Scenario",
            "Cedar Quay Transit Cooperative",
            "## Roles and authority",
            DISCLAIMER,
        ],
        "task-brief.md": [
            "## Required tools",
            "## Required deliverables",
            "### Permitted assumptions",
            "### Prohibited assumptions",
            "### When evidence is insufficient",
            "## Excluded scope",
            "referenced procedure files are not supplied",
            "inventory metadata as a submitted claim only",
        ],
        "inputs/README.md": [
            "complete evidence package",
            "EV-01 and EV-08",
            "not supplied",
            "must not be treated as reviewed evidence",
        ],
        "scoring-rubric.md": [
            "Total: 100 points",
            "## Critical errors",
            "Authority-boundary discipline",
            "contents of an unavailable artifact",
        ],
        "reviewer-guide.md": [
            "## Mandatory observations",
            "## Designed non-issues or false positives",
            "## Intentional ambiguities",
            "## Acceptable answer range",
            "## Professional judgment",
            "## Authority checks",
            "## Blocking errors",
            "## Minimum passing evidence",
            "## Partial credit",
            "Treating inventory metadata",
        ],
        "reference-answer.md": [
            "one defensible response",
            "## Preferred answer",
            "## Acceptable alternatives",
            "## Unsupported answers",
            "## Assumptions that change the result",
            "## Evidence needed to resolve uncertainty",
            "## Decisions reserved for authorized roles",
            "neither procedure file is supplied",
        ],
        "metadata.yaml": [
            f"id: {CASE_ID}",
            "status: case-ready",
            "version: 1.0.0",
            "synthetic_data: true",
            "private_dependency: false",
            "maintainer_service_required: false",
            "pilot_completions: 0",
        ],
    }
    for rel, values in markers.items():
        for value in values:
            if value not in docs.get(rel, ""):
                errors.append(f"{rel}: missing marker {value!r}")

    metadata = docs.get("metadata.yaml", "")
    if not re.search(r"^id: [a-z0-9]+(?:-[a-z0-9]+)*$", metadata, re.M):
        errors.append("metadata: invalid public case ID")
    if re.search(r"^id: (?:wfa|src|emp|cg|mir|aprprep)-", metadata, re.M):
        errors.append("metadata: private-prefix case ID")
    if "https://www.theiia.org/en/content/standards/complete-global-internal-audit-standards/" not in metadata:
        errors.append("metadata: missing public non-recruitment resource")

    def rows(rel: str) -> list[dict[str, str]]:
        path = root / CASE / rel
        if not path.is_file():
            return []
        with path.open(newline="", encoding="utf-8") as handle:
            return list(csv.DictReader(handle))

    requirements = rows("inputs/02-closure-requirements.csv")
    if [r.get("requirement_id") for r in requirements] != [f"REQ-0{i}" for i in range(1, 7)]:
        errors.append("requirements: expected REQ-01 through REQ-06")
    if any(r.get("materiality") != "blocking" for r in requirements):
        errors.append("requirements: all supplied requirements should be blocking")

    inventory = rows("inputs/05-evidence-inventory.csv")
    if len(inventory) != 8:
        errors.append(f"evidence inventory: expected 8 rows, got {len(inventory)}")
    inventory_by_id = {row.get("artifact_id", ""): row for row in inventory}
    if set(inventory_by_id) != {f"EV-0{i}" for i in range(1, 9)}:
        errors.append("evidence inventory: expected EV-01 through EV-08")

    hashes = [r.get("hash") for r in inventory]
    if hashes.count("sha256-a91f") != 2:
        errors.append("evidence inventory: designed duplicate claimed hash missing")

    for artifact_id in EXPECTED_UNAVAILABLE:
        row = inventory_by_id.get(artifact_id, {})
        if row.get("availability") != "listed-not-supplied":
            errors.append(f"evidence inventory: {artifact_id} must be listed-not-supplied")
        if row.get("case_input_reference") != "(none)":
            errors.append(f"evidence inventory: {artifact_id} must not have a case input reference")
        file_name = row.get("file_name")
        if file_name and (root / CASE / "inputs" / file_name).exists():
            errors.append(f"evidence inventory: {artifact_id} is marked unavailable but its file exists")

    for artifact_id, relative in EXPECTED_SUPPLIED.items():
        row = inventory_by_id.get(artifact_id, {})
        if row.get("availability") != "supplied":
            errors.append(f"evidence inventory: {artifact_id} must be supplied")
        if row.get("case_input_reference") != relative:
            errors.append(f"evidence inventory: {artifact_id} case input reference mismatch")
        if not (root / CASE / relative).is_file():
            errors.append(f"evidence inventory: supplied reference missing for {artifact_id}: {relative}")

    monitoring = rows("inputs/08-monitoring-report.csv")
    if len(monitoring) != 20:
        errors.append(f"monitoring: expected 20 rows, got {len(monitoring)}")
    if any(r.get("bypass_exceptions") != "0" for r in monitoring):
        errors.append("monitoring: designed report should show zero recorded exceptions")

    approvals = rows("inputs/10-approval-history.csv")
    if not any(
        r.get("object") == "Privileged Access Procedure" and r.get("version") == "1.9"
        for r in approvals
    ):
        errors.append("approval history: designed procedure-version mismatch missing")

    reference = docs.get("reference-answer.md", "")
    for req in [f"REQ-0{i}" for i in range(1, 7)]:
        if req not in reference:
            errors.append(f"reference answer: missing {req}")
    if "Not ready for authorized closure consideration" not in reference:
        errors.append("reference answer: preferred conditional conclusion missing")
    if "This recommendation is not final issue-closure approval." not in docs.get(
        "templates/closure-readiness-memo.md", ""
    ):
        errors.append("memo template: authority statement missing")

    role_doc = docs.get("role-relevance.md", "")
    allowed_relationships = {
        "performs",
        "contributes",
        "reviews",
        "consumes",
        "authorizes/owns",
    }
    allowed_bases = {"evidence-observed", "workflow-inferred", "case-designed"}
    for line in role_doc.splitlines():
        if line.startswith("|") and "---" not in line and "Role family" not in line:
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 4:
                if cells[1] not in allowed_relationships:
                    errors.append(f"role relevance: invalid relationship {cells[1]!r}")
                if cells[2] not in allowed_bases:
                    errors.append(f"role relevance: invalid basis {cells[2]!r}")

    if errors:
        print("CASE_VALIDATION=FAIL")
        for error in errors:
            print(f"ERROR={error}")
        return 1

    print("CASE_VALIDATION=PASS")
    print(f"CASE_ID={CASE_ID}")
    print("CASE_STATUS=case-ready")
    print(f"REQUIRED_FILES={len(REQUIRED)}")
    print(f"CLOSURE_REQUIREMENTS={len(requirements)}")
    print(f"EVIDENCE_INVENTORY_ROWS={len(inventory)}")
    print(f"UNAVAILABLE_INVENTORY_ARTIFACTS={len(EXPECTED_UNAVAILABLE)}")
    print(f"MONITORING_DAYS={len(monitoring)}")
    print("PRIVATE_MARKERS=0")
    print("PUBLIC_RESOURCE_MINIMUM=PASS")
    print("AUTHORITY_BOUNDARY=PASS")
    print("EVIDENCE_AVAILABILITY_BOUNDARY=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
