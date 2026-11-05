"""
Shared pieces for reviewing one SRS requirement with an LLM.

Used by:
    08_generate_report.ipynb      fixed retrieval: top 5 clauses + 3 always-included
    11_tool_calling_agent.ipynb   the agent searches for clauses itself

The LLM fills in a DraftReview (decisions only). to_review() adds the requirement ID, raw text,
and exact NASA citations, then runs Lauren's checks in report_schema.py.
"""

import time
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Literal
from urllib.parse import urldefrag

import pandas as pd
from pydantic import BaseModel, Field

from report_schema import (DOCUMENT_TO_AUTHORITY, SOURCE_TO_DOCUMENT, EvidenceStrength, IssueCode,
                           QualityStatus, Report, RequirementReview, Severity, SoftwareRequirementStatus)

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

srs = pd.read_csv(DATA_DIR / "srs_requirements.csv")
retrievals = pd.read_csv(DATA_DIR / "rag_retrievals.csv")
clauses = pd.read_csv(DATA_DIR / "addressable_clauses.csv").set_index("chunk_id")
srs_text = (DATA_DIR / "Starhawk Mission Computer SRS.md").read_text(encoding="utf-8")

# Retrieval matches topic, so it never surfaces the general writing rules (see 08 for why these three).
ALWAYS_INCLUDE = ["swehb-1.b-guidance", "swehb-3.2.1-guidance", "npr-4.1.4-requirement"]


def clauses_for(req_id):
    """Notebook 07's top 5 for this requirement, plus the always-included clauses."""
    retrieved = retrievals.loc[retrievals.req_id == req_id].sort_values("rank").chunk_id.tolist()
    return list(dict.fromkeys(retrieved + ALWAYS_INCLUDE))


def clause_block(ids):
    return "\n\n".join(f"[{cid}] {clauses.at[cid, 'source']} §{clauses.at[cid, 'section']}\n{clauses.at[cid, 'text']}"
                       for cid in ids)


def locator(row):
    """'3.3 Targeting and Weapons' -> '§3.3, SFMC-REQ-015' (the format in Mark's sample)."""
    return f"§{row.section.split()[0].rstrip('.')}, {row.req_id}"


# What the LLM fills in: a smaller version of RequirementReview. SWE links are limited to SWE-184, the
# only §4.1 provision whose content (safety constraints and controls) can appear in a requirement.

class Quote(BaseModel):
    locator: str = Field(description="Where the quote is from. For the requirement under review, use exactly the "
                                     "locator given in the prompt. For other SRS text, use its section, e.g. '§11, Open Item 10'.")
    excerpt: str = Field(description="Words copied exactly from the SRS, as short as possible.")


class DraftIssue(BaseModel):
    issue_code: IssueCode
    severity: Severity
    explanation: str
    evidence: List[Quote] = Field(min_length=1)
    clause_ids: List[str] = Field(min_length=1, description="IDs of the provided clauses that support this issue.")
    recommendation: str
    requires_stakeholder_input: bool


class DraftSweLink(BaseModel):
    swe_id: Literal["SWE-184"]
    strength: EvidenceStrength
    explanation: str
    evidence: List[Quote] = Field(min_length=1)


class DraftReview(BaseModel):
    analysis: str = Field(description="Brief reasoning before deciding: check the requirement against each issue type.")
    software_requirement_status: SoftwareRequirementStatus
    quality_issues: List[DraftIssue]
    swe_links: List[DraftSweLink]
    quality_status: QualityStatus
    summary: str = Field(description="One or two evidence-grounded sentences.")


LINK_CLAUSE = {"SWE-184": "npr-4.1.4-requirement"}
STRENGTH_ORDER = ["DIRECT_CONTENT", "PARTIAL_CONTENT", "INDIRECT_CONTEXT"]


def nasa_ref(cid):
    c = clauses.loc[cid]
    document = SOURCE_TO_DOCUMENT[c.source]
    return {
        "document": document,
        "authority": DOCUMENT_TO_AUTHORITY[document],
        "section": f"§{c.section}",
        "swe_id": c.swe_id if isinstance(c.swe_id, str) else None,
        "url": urldefrag(c.source_url)[0],
    }


def to_review(row, draft, allowed):
    """Draft -> RequirementReview. Raises ValueError (incl. Pydantic's ValidationError) if any check fails."""
    for issue in draft.quality_issues:
        issue.clause_ids = [cid.strip("[] ") for cid in issue.clause_ids]  # the prompt shows IDs in brackets
    unknown = {cid for issue in draft.quality_issues for cid in issue.clause_ids} - set(allowed)
    if unknown:
        raise ValueError(f"clause_ids that were not provided: {sorted(unknown)}. Cite only the IDs in square brackets.")
    links = [{
        "swe_id": l.swe_id,
        "strength": l.strength,
        "explanation": l.explanation,
        "srs_evidence": [q.model_dump() for q in l.evidence],
        "nasa_reference": nasa_ref(LINK_CLAUSE[l.swe_id]),
    } for l in draft.swe_links]
    primary = min(links, key=lambda l: STRENGTH_ORDER.index(l["strength"]), default=None)
    return RequirementReview.model_validate({
        "requirement_id": row.req_id,
        "raw_text": row.text,
        "software_requirement_status": draft.software_requirement_status,
        "quality_status": draft.quality_status,
        "quality_issues": [{
            **issue.model_dump(exclude={"evidence", "clause_ids"}),
            "srs_evidence": [q.model_dump() for q in issue.evidence],
            "nasa_references": [nasa_ref(cid) for cid in dict.fromkeys(issue.clause_ids)],
        } for issue in draft.quality_issues],
        "primary_swe_id": primary and primary["swe_id"],
        "primary_swe_strength": primary and primary["strength"],
        "swe_links": links,
        "summary": draft.summary,
    })


def fallback(row, reason):
    """Used when a requirement can't be reviewed; callers don't cache it, so the next run tries again."""
    return RequirementReview.model_validate({
        "requirement_id": row.req_id, "raw_text": row.text,
        "software_requirement_status": "UNCERTAIN", "quality_status": "UNDETERMINED",
        "quality_issues": [], "primary_swe_id": None, "primary_swe_strength": None, "swe_links": [],
        "summary": f"Automated review failed ({reason}); needs human review.",
    })


def with_api_retries(call):
    """Run call(); wait and retry when Gemini is busy (503) or rate-limited (429).
    A bad answer (ValueError) and the free tier's daily quota are raised right away."""
    for wait in [30, 60, 120, None]:
        try:
            return call()
        except ValueError:
            raise
        except Exception as e:
            if wait is None or "PerDay" in str(e):
                raise
            print(f"API unavailable ({type(e).__name__}), waiting {wait}s")
            time.sleep(wait)


# The rules come from Mark's output contract and the team's quality taxonomy. They describe each issue
# type in general terms only: no benchmark requirement or answer appears here, so the calibration
# comparison stays a fair check.
SYSTEM = """You review one requirement from the Starhawk Mission Computer SRS (SH-SRS-001, the SFMC).
Judge how well the requirement is written using the NASA software engineering handbook topic 5.09
(NASA-HDBK-2203), and link it to NPR 7150.2D SWE-184 only where its text justifies that.

software_requirement_status
- YES: it states behavior the SFMC software must provide (even if phrased around the pilot).
- NO: it is clearly not an obligation on the software.
- UNCERTAIN: it is unclear which system the obligation is allocated to.

quality_status
- ACCEPTABLE: no demonstrated writing defect. This is not a certificate of perfection; quality_issues must be empty.
- NEEDS_REVIEW: at least one specific defect you can show with an exact quote.
- UNDETERMINED: the SRS does not give enough to judge; explain what is missing.

Issue codes (use the most specific one; a requirement may have more than one issue)
- VAGUE_CRITERION: a degree word with no measurable bound or threshold (quickly, accurate, close, sufficient, noticeable).
- UNDEFINED_TERM: depends on a category the SRS never defines (which items count as "critical", "safe", "important"),
  including circular definitions where the condition is defined by the behavior it requires.
- UNSPECIFIED_RESPONSE: a trigger is given, but the required behavior is a placeholder ("appropriate action").
- ALLOCATION_UNCLEAR: the subject is not the SFMC software, references a system outside its documented interfaces,
  or leaves responsibility unassigned.
- UNVERIFIABLE_ABSOLUTE: a universal claim over unbounded time or inputs that no finite test can establish
  ("shall never fail"). "Never" or "always" attached to a clear, testable inhibit or capability is not this defect by itself.
- ESCAPE_CLAUSE: a qualifier that excuses non-compliance ("whenever possible", "as appropriate").
- SCOPE_AMBIGUITY: unclear which modes, conditions, or data the requirement applies to.
- SAFETY_INTERACTION: may interact with a safety function or inhibit in a way the SRS leaves unresolved (precedence
  unclear). Use this for a possible interaction, not a proven contradiction.
- OVERLAP_CLARIFICATION: overlaps another requirement and it is unclear which one governs.
- INCOMPLETE_TRACEABILITY, MISSING_QUALIFICATION_PROVISIONS, MISSING_ACCEPTANCE_CRITERIA, UNNUMBERED_REQUIREMENTS,
  INCOMPLETE_SAFETY_DEFINITIONS: document-level problems; use only if this requirement itself shows the problem.
- OTHER: a real defect none of the above covers; explain it.
Several obligations in one sentence is not a defect by itself.

Severity: CRITICAL if the defect leaves a safety function unverifiable or unimplementable; MAJOR if it makes the
requirement unverifiable or forces a design decision; MINOR otherwise.

Evidence and citations
- Every quote must be copied exactly from the SRS text provided. Keep quotes short.
- Cite NASA clauses only by the IDs shown in square brackets, choosing ones that actually support the issue.
- Handbook text is guidance. Never describe not following the Handbook as violating an NPR requirement.
- Recommendations must not invent numbers, mission parameters, or approval status. If stakeholders must decide
  something, say so and set requires_stakeholder_input to true.

SWE-184 link (NPR 7150.2D §4.1.4: safety constraints, controls, mitigations, and assumptions between hardware,
operator, and software belong in the software requirements)
- Link only if the requirement itself states a safety constraint, control, or mitigation: something the software
  must do or prevent specifically to avoid a hazard to the crew or spacecraft (an inhibit, interlock, or transition
  to a safe state).
- Ordinary functions are not safety controls just because their failure could be dangerous: displaying, monitoring,
  navigating, communicating, or reporting a fault. Detecting a fault counts only when a protective response is stated.
- DIRECT_CONTENT: states a safety control with clear criteria.
- PARTIAL_CONTENT: states a safety control, but its criteria or scope are unresolved.
- INDIRECT_CONTEXT: use rarely. When in doubt, leave swe_links empty.
- Never link because words overlap ("safe", "danger", "failure"). Expect only a few requirements in an SRS to have a link.
"""


def prompt_for(row, allowed):
    return f"""REQUIREMENT UNDER REVIEW
{row.req_id} ({row.title}) — locator for quotes from it: "{locator(row)}"
{row.text}

NASA CLAUSES (cite by the ID in square brackets)
{clause_block(allowed)}

FULL SRS
{srs_text}"""


def build_report(reviews, method, limitations, path):
    """Assemble requirement reviews into a DEMO-scope report.json (Lauren's Task #8 adds the other sections)."""
    report = Report.model_validate({
        "schema_version": "1.0.0",
        "run": {
            "input_document_id": "SH-SRS-001",
            "input_document_version": "1.0",
            "input_source": "https://github.com/Break-Through-Tech/Aerospace-1B-compliance-copilot/blob/main/data/Starhawk%20Mission%20Computer%20SRS.md",
            "evaluation_scope": "DEMO",
            "npr_reference_version": "NPR-7150.2D",
            "handbook_reference": "NASA-HDBK-2203-5.09",
            "method": method,
            "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "limitations": limitations,
        },
        "requirement_reviews": [r.model_dump() for r in reviews],
        "relationships": [],
        "document_findings": [],
        "swe_coverage": [],
    })
    report.to_json(path)
    return report
