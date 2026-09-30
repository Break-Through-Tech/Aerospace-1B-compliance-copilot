# Requirement Quality Taxonomy

Derived from the manual review of all 54 requirements in the Starhawk Mission Computer SRS
(`manual_requirement_review.csv`). Each category generalizes a defect we actually found, so that
a reviewer — human or automated — can look for it in other documents.

**Sourcing convention.** Every category states its NASA basis. Where NASA material does not
directly support the category, it is marked **INFERENCE** rather than dressed up as a citation.

---

## Level A — Detectable from a single requirement

### A1. Unquantified Qualifier
**Definition.** The requirement uses an adjective or adverb of degree with no numeric bound, unit, or threshold.

**Why it matters.** A tester cannot write a pass/fail criterion. Two implementations differing by orders of magnitude both satisfy the wording.

**Examples.** REQ-016 "extremely accurate"; REQ-021 "respond quickly"; REQ-037 "without noticeable delay"; REQ-006 "reasonably close"; REQ-047 "sufficient storage"; REQ-050 "state-of-the-art".

**NASA basis.** SWEHB 5.09 §3.2.1 — "Specific: Clear and unambiguous (e.g., avoid subjective terms like 'efficient' or 'user-friendly')." The handbook names this defect directly.

**Detection questions.**
- Does the sentence contain a degree word (quickly, accurately, sufficiently, reasonably, clearly)?
- If so, is a number, unit, or threshold attached to it anywhere in the document?

*Most common defect in this SRS: 9 of 22 findings.*

---

### A2. Undefined Term
**Definition.** The requirement depends on a classification or category that the document never defines.

**Why it matters.** Different from A1: the word is not vague in degree, it is a category with no membership rule. A developer must invent the rule, which silently becomes a design decision.

**Examples.** "important" (REQ-025, REQ-042); "critical" (REQ-030); "safe" (REQ-004, REQ-033, REQ-034); "friendly" (REQ-015); "nonessential" (REQ-032).

**NASA basis.** SWEHB 5.09 §3.2.1 — "Specific: Clear and unambiguous."

**Detection questions.**
- Does the requirement sort things into a category (important vs. not, critical vs. not, friendly vs. hostile)?
- Is the membership rule stated anywhere in the document?

**Severity note.** When the undefined term gates a safety function, this is more serious than ordinary vagueness. REQ-015 makes a weapons inhibit depend on "friendly", which SRS Open Items #10 admits is unresolved — the safety behavior is therefore unimplementable. Cross-reference NPR 7150.2D §4.1.4 (SWE-184), which requires safety constraints to be captured in the requirements documentation.

---

### A3. Unverifiable Absolute
**Definition.** The requirement asserts that something will *never* happen or will *always* hold, across unbounded time or input space.

**Why it matters.** Finite testing cannot demonstrate a universal negative. The requirement is unfalsifiable and therefore cannot be signed off.

**Example.** REQ-040 "The SFMC software shall never crash during a mission."

**NASA basis.** SWEHB 5.09 §3.2.1 — "Specific and verifiable/testable: each requirement should be clear enough to be tested with defined success criteria." That a universal negative fails this test is our engineering reasoning — **INFERENCE**, not a NASA statement.

**Detection questions.**
- Does the requirement contain never / always / all / under any circumstances?
- Could a finite test campaign establish it, or only fail to refute it?

---

### A4. Escape Clause
**Definition.** A conditional qualifier that lets any non-compliance be explained away.

**Why it matters.** Structurally the opposite of A3 but with the same effect: the requirement cannot be failed, so it cannot be verified.

**Example.** REQ-043 "shall continue operating using the remaining available systems **whenever possible**."

**NASA basis.** SWEHB 5.09 §3.2.1 (verifiable/testable). The specific pattern is **INFERENCE**.

**Detection questions.**
- Does it contain whenever possible / where practical / as appropriate / to the extent feasible?
- Who decides whether the condition was met — and could they ever be shown wrong?

---

### A5. Missing Response
**Definition.** A trigger condition is specified but the required system behavior is not.

**Why it matters.** Delegates a design decision to whoever implements it. In safety contexts that decision may never be reviewed by the people qualified to make it.

**Example.** REQ-010 — "If the SFMC detects a failure of a main engine, it shall notify the pilot and take **appropriate corrective action**." The trigger is precise; the action is not stated at all.

**NASA basis.** SWEHB 5.09 §3.2.1 — "Behavioral: They define system behavior or operations under specific conditions."

**Detection questions.**
- Is there an if/when clause?
- Is the consequent a concrete, observable action, or a placeholder for one?

---

### A6. Circular Definition
**Definition.** The requirement's scope is defined by the very property it is meant to establish.

**Why it matters.** Gives the appearance of a bounded requirement while bounding nothing.

**Example.** REQ-041 — "If a **recoverable** software fault occurs, the SFMC shall recover automatically." A fault is recoverable if it can be recovered from; the requirement therefore applies exactly where it already succeeds.

**NASA basis.** **INFERENCE.** NASA material does not name this pattern. Included because it recurs and is genuinely distinct from A2.

**Detection questions.**
- Does the qualifier restricting scope share a root with the required behavior?
- Could an implementer declare any failure out of scope after the fact?

---

### A7. Scope / Allocation Error
**Definition.** The requirement's subject is not the software under specification, or it references a system outside the documented interfaces.

**Why it matters.** Distinct from vagueness: the requirement may be perfectly clear and still not belong in this document. Unnoticed, it creates untraceable obligations.

**Examples.**
- REQ-016 — subject is "the targeting system", not the SFMC.
- REQ-032 — requires prioritizing life-support, which §1.2 does not list among SFMC-connected subsystems.
- REQ-025 — passive voice with no subject ("All important communications shall be securely encrypted"), leaving responsibility unassigned.

**NASA basis.** NPR 7150.2D §4.1.3 (SWE-051) requires requirements analysis based on flow-down from system requirements and hardware design; misallocation is what that analysis exists to catch. Application to a specific sentence is **INFERENCE**.

**Detection questions.**
- What is the grammatical subject? Is it the software being specified?
- Does it reference a subsystem listed in the interfaces section?

---

### A8. Compound Requirement
**Definition.** One identifier carries several independently verifiable obligations.

**Why it matters.** Each obligation needs its own test, but there is one ID to record the result against. Partial implementation cannot be recorded as either pass or fail.

**Examples.** REQ-045 (six log event classes); REQ-013 (four display fields); REQ-029 (four log fields); REQ-009 (visual warning plus audible alarm).

**NASA basis.** **INFERENCE.** SWEHB 5.09 §3.2.1 recommends numbering each requirement for easy reference and including acceptance criteria, which implies one testable obligation per ID — but it does not state this.

**Severity — team decision.** In the Starhawk SRS every instance is *complete and unambiguous*; the enumerated lists are arguably good practice. We therefore record these as **ACCEPTABLE with a traceability note** in `manual_requirement_review.csv` rather than as defects. This is a deliberate choice and a reviewer could reasonably disagree.

**Detection questions.**
- Does it contain a list, or "and" joining two distinct obligations?
- Could half of it pass while the other half fails?

---

## Level B — Detectable only across the requirements set

### B1. Requirements Conflict
**Definition.** Two requirements cannot both be satisfied as written.

**Why it matters.** The most severe class found. Each requirement reads correctly on its own, so per-requirement review never surfaces it.

**Examples.**
- **REQ-035 vs REQ-015.** The pilot "shall **always** be able to override automatic spacecraft controls", but the SFMC "shall **never** permit the pilot to fire a weapon at a friendly spacecraft." Whether the friendly-fire inhibit is overridable is undecidable from the document — and it is a weapons-release safety question.
- **REQ-038 vs REQ-002.** Flight information updates at least 10 times per second; displayed position updates at least once every 500 ms (2 Hz). If position is flight information, the rates disagree.

**NASA basis.** NPR 7150.2D §4.1.6 (SWE-054) — "identify, initiate corrective actions, and track until closure inconsistencies among requirements, project plans, and software products." Directly on point.

**Detection questions.**
- Do two requirements constrain the same behavior, quantity, or actor?
- Does one use an absolute (always / never) that another contradicts?

---

### B2. Inconsistent Vocabulary
**Definition.** The same undefined qualifier appears across unrelated requirements with different implied meanings.

**Why it matters.** Individually each is an A2 finding. Together they show the document has no shared vocabulary — a different, document-level problem whose fix is a definitions section, not seven separate edits.

**Example.** "important" in REQ-025 (communications) and REQ-042 (mission data); "critical" in REQ-009 and REQ-030; "safe" in REQ-004, REQ-033, REQ-034.

**NASA basis.** NPR 7150.2D §4.1.6 (SWE-054), inconsistencies among requirements.

**Detection questions.**
- Does a qualifier appear in more than one requirement?
- Is it defined once, in one place, for all uses?

---

### B3. Missing Structural Element
**Definition.** The SRS omits a section the handbook's recommended content calls for.

**Why it matters.** No individual requirement reveals it. The largest gap here is verification: nothing in the document states how any requirement will be confirmed.

**Examples.**
- No **Qualification Provisions** section (SWEHB 5.09 §1.c names four methods: Demonstration, Testing, Analysis, Inspection).
- No **rationale** and no **acceptance criteria** on any of the 54 requirements (SWEHB 5.09 §3.2.1, structured format).
- No requirements covering **resource utilization** (memory, CPU, storage) or **partitioning** (SWEHB 5.09 §1.b).

**NASA basis.** SWEHB 5.09 §1.b–1.d. Note SWEHB is guidance, not binding like the NPR — these are best recorded as "recommendation not followed" rather than "violation."

**Detection questions.**
- Compare the SRS table of contents against SWEHB 5.09 §1's recommended content. What is absent?
- Pick any requirement: does it carry a rationale and an acceptance criterion?

---

## Level C — Not detectable from the document at all

Recorded for completeness, because recognizing that these are *out of reach* is itself a finding.
NPR 7150.2D §4.1 consists almost entirely of this class: whether requirements were approved
(SWE-050), analyzed from flow-down (SWE-051), change-controlled (SWE-053), or validated with
stakeholders (SWE-055). Traceability (SWE-052, §3.12.1) also sits here.

No amount of reading the SRS text can establish compliance with these. An automated reviewer
should decline to judge them rather than guess. See `nasa_guidance_analysis.csv`.
