"""
Pydantic models for the Compliance Copilot output.

Based on Mark's output contract:
    contract/output_contract_schema_v1.json
    contract/output_contract_v1.md

Checks that:
- Requirement IDs are in the SRS data.
- NASA references match our clause data.
- Evidence quotes are from the SRS.
- ACCEPTABLE requirements have no listed issues.

Pydantic raises a ValidationError if a check fails.
"""

from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path
from typing import Annotated, List, Literal, Optional
from urllib.parse import urldefrag

import pandas as pd
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

#Files and reference data used to check the report

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
SRS_REQUIREMENTS_CSV = DATA_DIR / "srs_requirements.csv"
ADDRESSABLE_CLAUSES_CSV = DATA_DIR / "addressable_clauses.csv"
SRS_DOCUMENT_MD = DATA_DIR / "Starhawk Mission Computer SRS.md"

SOURCE_TO_DOCUMENT = {
    "NPR 7150.2D": "NPR-7150.2D",
    "SWEHB 5.09": "NASA-HDBK-2203-5.09",
}
DOCUMENT_TO_AUTHORITY = {
    "NPR-7150.2D": "NPR_REQUIREMENT",
    "NASA-HDBK-2203-5.09": "HANDBOOK_GUIDANCE",
}

NPR_CHAPTER4_URL = (
    "https://nodis3.gsfc.nasa.gov/displayDir.cfm?"
    "Internal_ID=N_PR_7150_002D_&page_name=Chapter4"
)
CORE_SWE_SECTIONS = {
    "SWE-050": "4.1.2",
    "SWE-051": "4.1.3",
    "SWE-184": "4.1.4",
    "SWE-053": "4.1.5",
    "SWE-054": "4.1.6",
    "SWE-055": "4.1.7",
}


def _norm_text(s: str) -> str:
    """Collapse whitespace and straighten quotes so harmless formatting
    differences don't fail an exact-match check."""
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    return " ".join(s.split())


def _norm_section(s: str) -> str:
    """'§4.1.4' / 'Section 4.1.4' / ' 4.1.4 ' -> '4.1.4'"""
    s = s.strip().replace("\u00a7", "")
    s = re.sub(r"^section\s*", "", s, flags=re.IGNORECASE)
    return s.strip()


def _norm_url(u: str) -> str:
    """Drop the '#tabs-3' style fragment. The clause CSV keeps it, Mark's
    sample doesn't, and both point at the same page."""
    return urldefrag(u.strip())[0]


@lru_cache(maxsize=1)
def srs_requirements() -> dict:
    """req_id -> requirement text, for the 54 Starhawk requirements."""
    df = pd.read_csv(SRS_REQUIREMENTS_CSV)
    return dict(zip(df["req_id"], df["text"]))


@lru_cache(maxsize=1)
def srs_document_text() -> str:
    """Whole SRS, normalized. Evidence can come from outside a requirement
    (e.g. '§11, Open Item 10' in Mark's REQ-015 example)."""
    return _norm_text(SRS_DOCUMENT_MD.read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def allowed_citations() -> frozenset:
    """(document, section, url, swe_id) for each of the 62 addressable clauses."""
    df = pd.read_csv(ADDRESSABLE_CLAUSES_CSV)
    out = set()
    for _, row in df.iterrows():
        swe = row["swe_id"] if isinstance(row["swe_id"], str) else None
        out.add((
            SOURCE_TO_DOCUMENT[row["source"]],
            _norm_section(str(row["section"])),
            _norm_url(row["source_url"]),
            swe,
        ))
    return frozenset(out)


#Allowed values for the fields in the report

RequirementId = Annotated[str, Field(pattern=r"^[A-Za-z][A-Za-z0-9_.-]{2,63}$")]
SweId = Annotated[str, Field(pattern=r"^SWE-\d{3}$")]
NonEmptyStr = Annotated[str, Field(min_length=1)]

SoftwareRequirementStatus = Literal["YES", "NO", "UNCERTAIN"]
QualityStatus = Literal["ACCEPTABLE", "NEEDS_REVIEW", "UNDETERMINED"]
IssueCode = Literal[
    "VAGUE_CRITERION",
    "UNDEFINED_TERM",
    "UNSPECIFIED_RESPONSE",
    "ALLOCATION_UNCLEAR",
    "UNVERIFIABLE_ABSOLUTE",
    "ESCAPE_CLAUSE",
    "SCOPE_AMBIGUITY",
    "SAFETY_INTERACTION",
    "OVERLAP_CLARIFICATION",
    "INCOMPLETE_TRACEABILITY",
    "MISSING_QUALIFICATION_PROVISIONS",
    "MISSING_ACCEPTANCE_CRITERIA",
    "UNNUMBERED_REQUIREMENTS",
    "INCOMPLETE_SAFETY_DEFINITIONS",
    "OTHER",
]
Severity = Literal["MINOR", "MAJOR", "CRITICAL", "UNDETERMINED"]
EvidenceStrength = Literal["DIRECT_CONTENT", "PARTIAL_CONTENT", "INDIRECT_CONTEXT"]
NasaDocument = Literal["NPR-7150.2D", "NASA-HDBK-2203-5.09"]
Authority = Literal["NPR_REQUIREMENT", "HANDBOOK_GUIDANCE"]

RelationshipStatus = Literal["NO_CONFIRMED_CONFLICT", "NEEDS_CLARIFICATION", "CONFIRMED_CONFLICT"]
RelationshipIssueCode = Literal["NONE", "SAFETY_INTERACTION", "OVERLAP_CLARIFICATION", "OTHER"]
DocumentCriterion = Literal[
    "TRACEABILITY",
    "QUALIFICATION_PROVISIONS",
    "ACCEPTANCE_CRITERIA",
    "REQUIREMENT_IDENTIFIERS",
    "SAFETY_DEFINITIONS",
    "OTHER",
]
DocumentStatus = Literal["PRESENT", "PARTIAL", "MISSING", "UNDETERMINED"]
CoreSweId = Literal["SWE-050", "SWE-051", "SWE-184", "SWE-053", "SWE-054", "SWE-055"]
DocumentEvidence = Literal["DOCUMENTED", "PARTIAL_EVIDENCE", "NO_SRS_EVIDENCE", "NOT_ASSESSABLE"]


class _Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")


#Checks that SRS quotes and NASA references are valid

class SrsEvidence(_Strict):
    locator: NonEmptyStr
    excerpt: NonEmptyStr

    @model_validator(mode="after")
    def check_excerpt_in_srs(self):
        excerpt = _norm_text(self.excerpt)
        if excerpt not in srs_document_text():
            raise ValueError(f"srs_evidence excerpt not found in the SRS: {self.excerpt!r}")
        reqs = srs_requirements()
        for req_id in re.findall(r"[A-Za-z]+-REQ-\d{3}", self.locator):
            if req_id in reqs and excerpt not in _norm_text(reqs[req_id]):
                raise ValueError(
                    f"srs_evidence excerpt {self.excerpt!r} does not appear in "
                    f"{req_id}'s text (locator {self.locator!r})"
                )
        return self


class NasaReference(_Strict):
    """Reference to an actual NASA provision; swe_id is null for handbook guidance."""
    document: NasaDocument
    authority: Authority
    section: NonEmptyStr
    swe_id: Optional[SweId]
    url: NonEmptyStr

    @field_validator("url")
    @classmethod
    def looks_like_uri(cls, v: str) -> str:
        if not re.match(r"^https?://\S+$", v):
            raise ValueError(f"url is not a valid http(s) URI: {v!r}")
        return v

    @model_validator(mode="after")
    def authority_matches_document(self):
        if DOCUMENT_TO_AUTHORITY[self.document] != self.authority:
            raise ValueError(
                f"{self.document} must use authority {DOCUMENT_TO_AUTHORITY[self.document]}, "
                f"got {self.authority}"
            )
        return self

    def key(self) -> tuple:
        return (self.document, _norm_section(self.section), _norm_url(self.url), self.swe_id)

    def check_in_addressable_clauses(self) -> "NasaReference":
        if self.key() not in allowed_citations():
            raise ValueError(
                f"NASA reference not in the 62 addressable clauses: "
                f"{self.document} §{_norm_section(self.section)} "
                f"(swe_id={self.swe_id}, url={self.url})"
            )
        return self


def _check_refs(refs: List[NasaReference]) -> List[NasaReference]:
    for r in refs:
        r.check_in_addressable_clauses()
    return refs


#Models and checks for each requirement review

class QualityIssue(_Strict):
    issue_code: IssueCode
    severity: Severity
    explanation: NonEmptyStr
    srs_evidence: List[SrsEvidence] = Field(min_length=1)
    nasa_references: List[NasaReference] = Field(min_length=1)
    recommendation: NonEmptyStr
    requires_stakeholder_input: bool

    @field_validator("nasa_references")
    @classmethod
    def refs_in_clauses(cls, v: List[NasaReference]) -> List[NasaReference]:
        return _check_refs(v)


class SweLink(_Strict):
    swe_id: SweId
    strength: EvidenceStrength
    explanation: NonEmptyStr
    srs_evidence: List[SrsEvidence] = Field(min_length=1)
    nasa_reference: NasaReference

    @field_validator("nasa_reference")
    @classmethod
    def ref_in_clauses(cls, v: NasaReference) -> NasaReference:
        return v.check_in_addressable_clauses()

    @model_validator(mode="after")
    def ref_matches_swe(self):
        if self.nasa_reference.swe_id != self.swe_id:
            raise ValueError(
                f"swe_link {self.swe_id} cites a reference for {self.nasa_reference.swe_id}"
            )
        return self


class RequirementReview(_Strict):
    requirement_id: RequirementId
    raw_text: NonEmptyStr
    software_requirement_status: SoftwareRequirementStatus
    quality_status: QualityStatus
    quality_issues: List[QualityIssue]
    primary_swe_id: Optional[SweId]
    primary_swe_strength: Optional[EvidenceStrength]
    swe_links: List[SweLink]
    summary: NonEmptyStr

    @field_validator("requirement_id")
    @classmethod
    def id_in_srs(cls, v: str) -> str:
        if v not in srs_requirements():
            raise ValueError(f"requirement_id {v!r} is not one of the 54 in srs_requirements.csv")
        return v

    @model_validator(mode="after")
    def contract_rules(self):
        if self.quality_status == "ACCEPTABLE" and self.quality_issues:
            raise ValueError(
                f"{self.requirement_id}: ACCEPTABLE must have no quality_issues "
                f"(found {len(self.quality_issues)}); use NEEDS_REVIEW or UNDETERMINED"
            )
        expected = srs_requirements().get(self.requirement_id)
        if expected is not None and _norm_text(self.raw_text) != _norm_text(expected):
            raise ValueError(f"{self.requirement_id}: raw_text doesn't match the SRS text")
        if (self.primary_swe_id is None) != (self.primary_swe_strength is None):
            raise ValueError(
                f"{self.requirement_id}: primary_swe_id and primary_swe_strength "
                "must both be set or both be null"
            )
        if self.primary_swe_id is not None and not any(
            l.swe_id == self.primary_swe_id and l.strength == self.primary_swe_strength
            for l in self.swe_links
        ):
            raise ValueError(f"{self.requirement_id}: primary SWE must match one of swe_links")
        ids = [l.swe_id for l in self.swe_links]
        if len(ids) != len(set(ids)):
            raise ValueError(f"{self.requirement_id}: duplicated SWE links")
        return self


#Additional checks for relationships, document findings, and SWE coverage

class Relationship(_Strict):
    relationship_id: NonEmptyStr
    requirement_ids: List[RequirementId] = Field(min_length=2)
    status: RelationshipStatus
    issue_code: RelationshipIssueCode
    explanation: NonEmptyStr
    srs_evidence: List[SrsEvidence] = Field(min_length=2)
    nasa_references: List[NasaReference] = Field(min_length=1)
    recommendation: NonEmptyStr

    @field_validator("nasa_references")
    @classmethod
    def refs_in_clauses(cls, v: List[NasaReference]) -> List[NasaReference]:
        return _check_refs(v)

    @field_validator("requirement_ids")
    @classmethod
    def ids_valid(cls, v: List[str]) -> List[str]:
        if len(v) != len(set(v)):
            raise ValueError("requirement_ids must be unique")
        unknown = [x for x in v if x not in srs_requirements()]
        if unknown:
            raise ValueError(f"requirement_ids not in srs_requirements.csv: {unknown}")
        return v


class DocumentFinding(_Strict):
    finding_id: NonEmptyStr
    criterion: DocumentCriterion
    status: DocumentStatus
    issue_code: NonEmptyStr
    searched_scope: NonEmptyStr
    explanation: NonEmptyStr
    srs_evidence: List[SrsEvidence]  #may be empty for absence findings
    nasa_references: List[NasaReference] = Field(min_length=1)
    recommendation: NonEmptyStr

    @field_validator("nasa_references")
    @classmethod
    def refs_in_clauses(cls, v: List[NasaReference]) -> List[NasaReference]:
        return _check_refs(v)


class SweCoverage(_Strict):
    swe_id: CoreSweId
    document_evidence: DocumentEvidence
    project_compliance: Literal["NOT_DETERMINED"]
    rationale: NonEmptyStr
    supported_by_requirement_ids: List[RequirementId]
    srs_evidence: List[SrsEvidence]
    external_evidence_needed: List[NonEmptyStr]
    nasa_reference: NasaReference

    @field_validator("supported_by_requirement_ids", "external_evidence_needed")
    @classmethod
    def unique(cls, v: List[str]) -> List[str]:
        if len(v) != len(set(v)):
            raise ValueError("items must be unique")
        return v

    @field_validator("supported_by_requirement_ids")
    @classmethod
    def ids_in_srs(cls, v: List[str]) -> List[str]:
        unknown = [x for x in v if x not in srs_requirements()]
        if unknown:
            raise ValueError(f"supported_by_requirement_ids not in srs_requirements.csv: {unknown}")
        return v

    @model_validator(mode="after")
    def ref_is_the_core_provision(self):
        ref = self.nasa_reference
        expected = ("NPR-7150.2D", CORE_SWE_SECTIONS[self.swe_id], NPR_CHAPTER4_URL, self.swe_id)
        if ref.key() != expected:
            raise ValueError(
                f"{self.swe_id}: nasa_reference must be NPR-7150.2D §{CORE_SWE_SECTIONS[self.swe_id]} "
                f"(Chapter 4) with swe_id {self.swe_id}"
            )
        return self


#Run details and validation for the complete report
class Run(_Strict):
    input_document_id: NonEmptyStr
    input_document_version: NonEmptyStr
    input_source: NonEmptyStr
    evaluation_scope: Literal["DEMO", "FULL_SRS"]
    npr_reference_version: Literal["NPR-7150.2D"]
    handbook_reference: Literal["NASA-HDBK-2203-5.09"]
    method: NonEmptyStr
    generated_at_utc: NonEmptyStr
    limitations: List[NonEmptyStr]

    @field_validator("generated_at_utc")
    @classmethod
    def is_datetime(cls, v: str) -> str:
        from datetime import datetime
        try:
            datetime.fromisoformat(v.replace("Z", "+00:00"))
        except ValueError:
            raise ValueError(f"generated_at_utc is not an ISO date-time: {v!r}")
        return v

    @field_validator("limitations")
    @classmethod
    def unique(cls, v: List[str]) -> List[str]:
        if len(v) != len(set(v)):
            raise ValueError("limitations must be unique")
        return v


class Report(_Strict):
    """The whole report.json."""
    schema_version: Literal["1.0.0"]
    run: Run
    requirement_reviews: List[RequirementReview]
    relationships: List[Relationship]
    document_findings: List[DocumentFinding]
    swe_coverage: List[SweCoverage]

    @model_validator(mode="after")
    def cross_section_rules(self):
        ids = [r.requirement_id for r in self.requirement_reviews]
        if len(ids) != len(set(ids)):
            raise ValueError("duplicate requirement review IDs")
        for rel in self.relationships:
            missing = set(rel.requirement_ids) - set(ids)
            if missing:
                raise ValueError(f"{rel.relationship_id}: unreviewed requirement IDs {sorted(missing)}")
        swes = [s.swe_id for s in self.swe_coverage]
        if len(swes) != len(set(swes)):
            raise ValueError("duplicate swe_coverage entries")
        for s in self.swe_coverage:
            missing = set(s.supported_by_requirement_ids) - set(ids)
            if missing:
                raise ValueError(f"{s.swe_id}: cites unreviewed requirement IDs {sorted(missing)}")
        if self.run.evaluation_scope == "FULL_SRS":
            expected = set(srs_requirements())
            if set(ids) != expected:
                raise ValueError(
                    f"FULL_SRS run: missing {sorted(expected - set(ids))}, "
                    f"extras {sorted(set(ids) - expected)}"
                )
            if set(swes) != set(CORE_SWE_SECTIONS):
                raise ValueError(f"FULL_SRS run: missing SWE summaries {sorted(set(CORE_SWE_SECTIONS) - set(swes))}")
            if not any(f.criterion == "REQUIREMENT_IDENTIFIERS" for f in self.document_findings):
                raise ValueError("FULL_SRS run: needs a REQUIREMENT_IDENTIFIERS document finding")
        return self

    def to_json(self, path: str | Path) -> None:
        """Write report.json in the contract's shape."""
        Path(path).write_text(self.model_dump_json(indent=2), encoding="utf-8")
