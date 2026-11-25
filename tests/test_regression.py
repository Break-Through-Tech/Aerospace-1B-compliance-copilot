import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT_JSON = ROOT / "data" / "report.json"
REPORT_MD = ROOT / "data" / "report.md"


with open(REPORT_JSON, "r", encoding="utf-8") as f:
    report = json.load(f)


def get_requirement(requirement_id):
    return next(
        r for r in report["requirement_reviews"]
        if r["requirement_id"] == requirement_id
    )


def get_relationship(relationship_id):
    return next(
        r for r in report["relationships"]
        if r["relationship_id"] == relationship_id
    )


def get_document_finding(finding_id):
    return next(
        f for f in report["document_findings"]
        if f["finding_id"] == finding_id
    )


def get_swe(swe_id):
    return next(
        s for s in report["swe_coverage"]
        if s["swe_id"] == swe_id
    )


def test_good_requirement():
    req = get_requirement("SFMC-REQ-002")

    assert req["quality_status"] == "ACCEPTABLE"
    assert req["quality_issues"] == []


def test_unclear_requirement():
    req = get_requirement("SFMC-REQ-010")

    issue_codes = {
        issue["issue_code"]
        for issue in req["quality_issues"]
    }

    assert req["quality_status"] == "NEEDS_REVIEW"
    assert "UNSPECIFIED_RESPONSE" in issue_codes


def test_safety_interaction():
    rel = get_relationship("REL-001")

    assert rel["requirement_ids"] == [
        "SFMC-REQ-015",
        "SFMC-REQ-035",
    ]
    assert rel["status"] == "NEEDS_CLARIFICATION"
    assert rel["issue_code"] == "SAFETY_INTERACTION"
    assert rel["status"] != "CONFIRMED_CONFLICT"


def test_missing_document_element():
    finding = get_document_finding("DOC-002")

    assert finding["status"] == "MISSING"


def test_process_evidence_abstention():
    for swe_id in ["SWE-053", "SWE-054", "SWE-055"]:
        swe = get_swe(swe_id)
        assert swe["document_evidence"] == "NOT_ASSESSABLE"

    for swe in report["swe_coverage"]:
        assert swe["project_compliance"] == "NOT_DETERMINED"


def test_markdown_contains_all_requirement_ids():
    markdown = REPORT_MD.read_text(encoding="utf-8")

    for review in report["requirement_reviews"]:
        assert review["requirement_id"] in markdown