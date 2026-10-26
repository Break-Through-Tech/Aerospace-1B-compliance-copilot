"""Tests for report_schema.py 
Run from the repo root:
    python -m pytest notebooks/test_report_schema.py -v
Each test maps to a "Done when" item or one of the 4 extra checks.
"""
import copy
import json
import sys
from pathlib import Path

import pytest
from pydantic import ValidationError

sys.path.insert(0, str(Path(__file__).resolve().parent))
from report_schema import (  # noqa: E402
    DocumentFinding,
    Relationship,
    Report,
    RequirementReview,
    SweCoverage,
)

CONTRACT_DIR = Path(__file__).resolve().parent.parent / "contract"
SAMPLE = json.loads((CONTRACT_DIR / "output_contract_schema_v1.json").parent.joinpath(
    "sample_output_v1.json").read_text(encoding="utf-8"))


def review(req_id):
    """Fresh copy of one of Mark's sample reviews, to break on purpose."""
    r = next(r for r in SAMPLE["requirement_reviews"] if r["requirement_id"] == req_id)
    return copy.deepcopy(r)


def rejects(model, data, match):
    with pytest.raises(ValidationError, match=match):
        model.model_validate(data)


#Done when: sample requirement_reviews load 

def test_sample_requirement_reviews_load():
    for r in SAMPLE["requirement_reviews"]:
        RequirementReview.model_validate(r)

#Done when: bad examples rejected 
def test_rejects_made_up_issue_code():
    r = review("SFMC-REQ-015")
    r["quality_issues"][0]["issue_code"] = "SOUNDS_BAD"
    rejects(RequirementReview, r, "issue_code")


def test_rejects_citation_not_in_62_clauses():
    r = review("SFMC-REQ-015")
    # Real NPR section, but filtered out of the addressable clauses
    r["quality_issues"][0]["nasa_references"][1].update(section="§4.1.7", swe_id="SWE-055")
    rejects(RequirementReview, r, "not in the 62 addressable clauses")


def test_rejects_fully_invented_citation():
    r = review("SFMC-REQ-035")
    r["quality_issues"][0]["nasa_references"][0]["section"] = "§9.9.9"
    rejects(RequirementReview, r, "not in the 62 addressable clauses")


#The 4 extra checks

def test_check1_requirement_id_must_be_one_of_54():
    r = review("SFMC-REQ-002")
    r["requirement_id"] = "SFMC-REQ-099"
    rejects(RequirementReview, r, "not one of the 54")


def test_check2_citation_swe_id_must_match_clause():
    r = review("SFMC-REQ-015")
    # §4.1.4 is SWE-184, not SWE-050
    r["quality_issues"][0]["nasa_references"][1]["swe_id"] = "SWE-050"
    rejects(RequirementReview, r, "not in the 62 addressable clauses")


def test_check2_section_and_url_formats_are_normalized():
    #Clause CSV has '3.2.1' + '#tabs-3'; Mark's sample has '§3.2.1' and no fragment.
    r = review("SFMC-REQ-015")
    ref = r["quality_issues"][0]["nasa_references"][0]
    ref["section"] = "3.2.1"
    ref["url"] += "#tabs-3"
    RequirementReview.model_validate(r)


def test_check3_excerpt_must_appear_in_srs():
    r = review("SFMC-REQ-015")
    r["quality_issues"][0]["srs_evidence"][0]["excerpt"] = "at an enemy spacecraft"
    rejects(RequirementReview, r, "not found in the SRS")


def test_check3_excerpt_must_be_from_the_requirement_its_locator_names():
    r = review("SFMC-REQ-015")
    #Real SRS text, but it's REQ-035's, not REQ-015's
    r["quality_issues"][0]["srs_evidence"][0]["excerpt"] = (
        "always be able to override automatic spacecraft controls"
    )
    rejects(RequirementReview, r, "does not appear in SFMC-REQ-015")


def test_check3_evidence_from_elsewhere_in_srs_is_allowed():
    #Mark's own REQ-015 example quotes §11 Open Item 10. Already covered by
    #the sample loading, but spelled out so nobody "fixes" it later.
    r = review("SFMC-REQ-015")
    locs = [e["locator"] for e in r["quality_issues"][0]["srs_evidence"]]
    assert any("Open Item" in l for l in locs)
    RequirementReview.model_validate(r)


def test_check4_acceptable_must_have_no_issues():
    r = review("SFMC-REQ-015")
    r["quality_status"] = "ACCEPTABLE"
    rejects(RequirementReview, r, "ACCEPTABLE must have no quality_issues")


#Other contract rules the models enforce

def test_rejects_made_up_status_value():
    r = review("SFMC-REQ-002")
    r["quality_status"] = "PASS"
    rejects(RequirementReview, r, "quality_status")


def test_rejects_extra_fields():
    r = review("SFMC-REQ-002")
    r["confidence"] = 0.93
    rejects(RequirementReview, r, "confidence")


def test_rejects_altered_raw_text():
    r = review("SFMC-REQ-002")
    r["raw_text"] = "The SFMC shall update the position sometimes."
    rejects(RequirementReview, r, "raw_text")


def test_rejects_primary_swe_without_matching_link():
    r = review("SFMC-REQ-015")
    r["primary_swe_strength"] = "DIRECT_CONTENT"  #link says PARTIAL_CONTENT
    rejects(RequirementReview, r, "primary SWE must match")


def test_rejects_handbook_cited_as_npr_requirement():
    r = review("SFMC-REQ-035")
    r["quality_issues"][0]["nasa_references"][0]["authority"] = "NPR_REQUIREMENT"
    rejects(RequirementReview, r, "must use authority HANDBOOK_GUIDANCE")


#Stretch: relationships, document_findings, swe_coverage

def test_stretch_sample_sections_load():
    for x in SAMPLE["relationships"]:
        Relationship.model_validate(x)
    for x in SAMPLE["document_findings"]:
        DocumentFinding.model_validate(x)
    for x in SAMPLE["swe_coverage"]:
        SweCoverage.model_validate(x)


def test_stretch_whole_sample_report_loads_and_round_trips(tmp_path):
    report = Report.model_validate(SAMPLE)
    out = tmp_path / "report.json"
    report.to_json(out)
    assert json.loads(out.read_text(encoding="utf-8")) == SAMPLE


def test_stretch_round_trip_passes_marks_validator(tmp_path):
    jsonschema = pytest.importorskip("jsonschema")
    sys.path.insert(0, str(CONTRACT_DIR))
    from validate_report import validate

    out = tmp_path / "report.json"
    Report.model_validate(SAMPLE).to_json(out)
    validate(out)  #raises if Mark's schema or his checks fail


def test_stretch_relationship_rejects_unknown_requirement():
    rel = copy.deepcopy(SAMPLE["relationships"][0])
    rel["requirement_ids"][1] = "SFMC-REQ-777"
    rejects(Relationship, rel, "not in srs_requirements.csv")


def test_stretch_swe_coverage_rejects_wrong_section():
    cov = copy.deepcopy(SAMPLE["swe_coverage"][0])
    cov["nasa_reference"]["section"] = "§4.1.6"
    rejects(SweCoverage, cov, "must be NPR-7150.2D §4.1.4")


def test_stretch_swe_coverage_allows_process_only_swes():
    #SWE-055 isn't in the 62 clauses, but a FULL_SRS run must cover it
    cov = copy.deepcopy(SAMPLE["swe_coverage"][0])
    cov.update(
        swe_id="SWE-055",
        document_evidence="NOT_ASSESSABLE",
        supported_by_requirement_ids=[],
        srs_evidence=[],
    )
    cov["nasa_reference"].update(section="§4.1.7", swe_id="SWE-055")
    SweCoverage.model_validate(cov)


def test_stretch_report_rejects_relationship_to_unreviewed_requirement():
    data = copy.deepcopy(SAMPLE)
    data["requirement_reviews"] = [r for r in data["requirement_reviews"]
                                   if r["requirement_id"] != "SFMC-REQ-035"]
    rejects(Report, data, "unreviewed requirement IDs")


def test_stretch_full_srs_run_requires_all_54():
    data = copy.deepcopy(SAMPLE)
    data["run"]["evaluation_scope"] = "FULL_SRS"
    rejects(Report, data, "FULL_SRS run: missing")
