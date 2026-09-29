# AI Review — Preliminary Problem Definition

Written after manually reviewing all 54 Starhawk requirements. Ideas only; no implementation.
The point of doing this last is that every claim below is grounded in a task we actually performed.

---

## 1. What should the LLM receive?

**Per requirement:**
- Requirement ID and full text
- The section it sits in (defines whether it is functional, performance, security, constraint)
- The five operating modes from §1.3 — many defects are "which mode does this apply in?"
- SRS Open Items (§11) — a list of terms the document *admits* are undefined

**Retrieved from the standards:**
- Relevant SWEHB 5.09 §3.2.1 characteristics
- **Not** NPR 7150.2D §4.1. All six clauses are process-level and cannot be judged from requirement text (see `nasa_guidance_analysis.csv`). Retrieving them would invite the model to cite a clause that cannot apply — which is precisely the groundedness failure we want to avoid.

**Only for set-level checks:**
- The full requirement list, for conflict and vocabulary detection

**An honest note on retrieval.** Our whole usable rubric is roughly a dozen statements from one
handbook page. That is small enough to fit in a prompt directly. RAG may be the wrong tool for the
*criteria*; it is the right tool for searching the 54 requirements for conflicts. Worth raising
with the team before building a vector database we do not need.

---

## 2. What should the critique contain?

Per finding, not per requirement:

| Field | Why |
|---|---|
| Requirement ID | Anchor |
| Verdict | See §3 |
| Defect category | From `requirement_quality_taxonomy.md` |
| Evidence span | The exact words at fault ("extremely accurate") — makes the claim checkable |
| NASA source | A real clause ID, or explicitly `INFERENCE` |
| Confidence | See §5 |
| Proposed revision **or** stakeholder question | See §4 |

**Multiple findings per requirement, not one.** REQ-021 ("shall respond quickly to dangerous
threats") has three distinct defects: an unquantified qualifier, an undefined term, and a missing
response. A single verdict would lose two of them.

---

## 3. Should it be PASS / FAIL?

No. Two values are not enough. We propose three:

- **ACCEPTABLE** — no defect found
- **NEEDS REVIEW** — a defect detectable from the text
- **CANNOT DETERMINE FROM TEXT** — the criterion is process-level or requires information the document does not contain

The third is the important one. Without it, a model asked whether requirements are traceable
(SWE-052) will guess, and a guess on a process requirement is a fabrication. The system should be
able to decline.

---

## 4. Should it propose rewrites?

Only conditionally — and this is the subtlest lesson from Activity 5.

Of six requirements we attempted to rewrite, **zero** could be fully repaired from the document.
Most defects are missing stakeholder decisions, not bad wording. A model that confidently rewrites
"shall respond quickly" as "shall respond within 100 ms" has invented an engineering value and
made it look authoritative.

**Proposed rule.** The system may restructure, but may not supply values. Output the corrected
form with explicit `[PLACEHOLDER]` markers plus the question that must be answered — mirroring the
rewrites file. If it cannot rewrite without inventing, it must return a stakeholder question instead.

---

## 5. Definite defect vs. needs human review

Map to the levels from `nasa_guidance_analysis.csv`:

- **High confidence (Level A, lexical).** Subjective qualifiers, universal absolutes, escape clauses. Detectable from one sentence, arguably without an LLM at all — a keyword list finds most of them. Good baseline for the team's TF-IDF model.
- **Medium (Level A, semantic).** Missing response, circular definition, allocation errors. Require understanding what the sentence asserts.
- **Low / flag for human (Level B).** Conflicts and vocabulary inconsistency. Need the whole set in context. Our two best findings — REQ-035 vs REQ-015, REQ-038 vs REQ-002 — are here, and neither is findable one requirement at a time.
- **Refuse (Level C).** Process requirements. Return CANNOT DETERMINE.

A useful heuristic: **if we needed a second requirement to see the problem, the model does too.**

---

## 6. How would we know the critique was correct?

`manual_requirement_review.csv` is a 54-row labelled benchmark — 32 ACCEPTABLE, 22 NEEDS REVIEW,
each with a category and a source. It is a ground truth we can score against today.

**Metrics:**
- **Precision** — of flagged requirements, how many we also flagged. False positives are the expensive failure: a reviewer who chases ten invented defects stops trusting the tool.
- **Recall** — of our 22, how many it found.
- **Category agreement** — right requirement, right defect type. Catching REQ-041 for the wrong reason is not a success.
- **Groundedness** — does the cited clause exist, and does it say what the model claims? We produced a real failure of this kind during Activity 2: a summarization step invented two SWEHB characteristics ("measurable", "constraint-driven") that are not on the page. That is the exact error mode, and it argues for validating every citation against a fixed clause list rather than trusting generated text.

**Caveats we should state plainly:**
- Our benchmark is one team's judgment on one fictional SRS, not NASA-endorsed truth.
- We labelled the same document the system will be tested on. Scores are optimistic and we should not present them as generalization.
- Several rows encode contested calls — whether compound requirements are defects, whether "continuously" is too vague. Disagreement with those is not necessarily model error.

---

## 7. What is impossible from the requirement alone?

- **Completeness.** Detecting an absence needs domain knowledge. Nothing in the text reveals that no requirement covers autopilot failure mid-route. The best available proxy is SWEHB 5.09 §1.b's requirement-type checklist — turning "what is missing?" into "which expected categories are absent?"
- **Whether a constraint is justified.** REQ-051 (specific flight computer) is a legitimate constraint; an unexplained one would be a defect. The text looks identical either way.
- **Everything process-level.** Approval, change control, validation, traceability.
- **Whether a value is right.** We can see that REQ-008's 15% threshold is well-formed. We cannot see whether 15% is the correct number.

---

## 8. Open questions for the team

1. Do we need a vector database if the whole rubric is a dozen statements?
2. Should set-level checks (conflicts) be a separate pass with different inputs?
3. How do we score a model that finds a real defect we missed — error, or benchmark gap?
4. Do we report the Level C refusals as a feature, or does the advisor expect coverage there?
