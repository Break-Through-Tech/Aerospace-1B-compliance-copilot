# Requirement Rewrites

Six requirements from the Starhawk Mission Computer SRS, selected from the NEEDS REVIEW rows in
`manual_requirement_review.csv`.

**Governing principle.** Identifying a defect and correcting it are different acts. Where the
missing information is a value only a stakeholder can supply, the correct engineering response is
to say so — not to invent a plausible number. Two of the six below are deliberately left
unrewritten for that reason.

---

## 1. SFMC-REQ-006 — Autopilot Arrival

**Original.** "The autopilot shall deliver the spacecraft reasonably close to the selected destination."

**Problem.** Unquantified qualifier (A1). "Reasonably close" has no tolerance, so no acceptance criterion exists. SRS Open Items #2 admits this is unresolved.

**Proposed revision.** *None offered.*

This cannot be repaired from the document. Writing "within 100 metres" would invent an engineering value with no source. The arrival tolerance depends on docking approach envelopes, sensor accuracy, and mission profile — none of which appear in this SRS.

**Assumptions made.** None. We deliberately declined to supply a number.

**Questions for stakeholders.**
- What is the maximum acceptable miss distance at autopilot handover, and in what units?
- Does it vary by destination type (station, waypoint, another spacecraft)?
- Is arrival defined as position only, or position plus matched velocity?

---

## 2. SFMC-REQ-010 — Engine Failure

**Original.** "If the SFMC detects a failure of a main engine, it shall notify the pilot and take appropriate corrective action."

**Problem.** Missing response (A5). The trigger is precise; the required behavior is a placeholder. As written, the contingency design is delegated to the developer.

**Proposed revision.** *None offered for the second clause.*

The notification half could be tightened immediately — "shall display a main-engine failure alert to the pilot within 1 second of detection", mirroring REQ-027. The corrective-action half cannot be written without knowing the intended contingency, and guessing at it would embed an unreviewed flight-safety decision in the SRS.

**Assumptions made.** That the 1-second bound from REQ-027 is a reasonable precedent for fault annunciation. This is our inference and should be confirmed.

**Questions for stakeholders.**
- What sequence constitutes corrective action — thruster re-trim, fuel isolation, automatic transition to Emergency mode, or pilot handover?
- Does the response differ by which engine fails, or by flight phase?
- Should this requirement be split into annunciation and response?

---

## 3. SFMC-REQ-040 — Software Failure

**Original.** "The SFMC software shall never crash during a mission."

**Problem.** Unverifiable absolute (A3). A universal negative cannot be established by finite testing.

**Proposed revision.**

> The SFMC software shall experience no more than **[X]** unplanned terminations per **[Y]** operating hours, demonstrated against the operational profile defined in **[reference]**.

**Assumptions made.** That the stakeholder intent is quantified reliability rather than literal perfection. The structure is correct and reusable; the two values are placeholders and must not be filled in by the reviewing team.

**Questions for stakeholders.**
- What reliability target applies, and at which software safety classification?
- Is there a defined operational profile to measure against?
- Does an automatic recovery within the REQ-041 window count as a termination?

---

## 4. SFMC-REQ-043 — Degraded Operation

**Original.** "If a spacecraft subsystem becomes unavailable, the SFMC shall continue operating using the remaining available systems whenever possible."

**Problem.** Escape clause (A4). "Whenever possible" makes the requirement unfalsifiable — any failure to continue can be attributed to impossibility.

**Proposed revision.**

> For each subsystem loss identified in the degraded-mode matrix **[reference]**, the SFMC shall continue to provide the functions that matrix designates as required, and shall annunciate the resulting loss of capability to the pilot.

**Assumptions made.** That a per-subsystem degraded-mode analysis is the intended engineering artifact. This replaces an open-ended promise with a bounded obligation, but the matrix itself does not yet exist.

**Questions for stakeholders.**
- Does a degraded-mode matrix exist, or must one be produced?
- Which functions are mandatory after losing Navigation? Propulsion? Communications?
- Should degraded operation differ in Emergency mode?

---

## 5. SFMC-REQ-035 and SFMC-REQ-015 — Pilot Override vs. Friendly-Fire Inhibit

**Original.**
> REQ-035: "The pilot shall always be able to override automatic spacecraft controls."
> REQ-015: "The SFMC shall never permit the pilot to fire a weapon at a friendly spacecraft."

**Problem.** Requirements conflict (B1). Both are absolutes and they contradict each other: if override is truly unconditional, it extends to the friendly-fire inhibit. This is a weapons-release safety question that the document leaves undecided.

**Proposed revision (structure only).**

> REQ-035 (revised): The pilot shall be able to override automatic spacecraft controls, **except for the safety inhibits enumerated in [reference]**.
>
> REQ-015 (revised): The SFMC shall inhibit weapon release against any contact classified as friendly per the criteria in **[reference]**. This inhibit **[is / is not]** subject to pilot override.

**Assumptions made.** That an enumerated list of non-overridable inhibits is the right mechanism. We deliberately did **not** decide whether the friendly-fire inhibit is overridable — that is a safety and rules-of-engagement decision, not a documentation fix.

**Questions for stakeholders.**
- Which safety inhibits, if any, may the pilot override?
- If the inhibit is overridable, what action is required (two-step confirmation, logged authorization)?
- What criteria classify a contact as friendly? SRS Open Items #10 lists this as unresolved.

---

## 6. SFMC-REQ-025 — Secure Communications

**Original.** "All important communications shall be securely encrypted."

**Problem.** Three defects in one sentence. Undefined term (A2) — "important" is never defined and reappears undefined in REQ-042. Unquantified qualifier (A1) — "securely" names no standard. Scope/allocation error (A7) — passive voice with no subject leaves it unclear that the SFMC is responsible.

**Proposed revision (partial).**

> The SFMC shall encrypt all outgoing and incoming communications classified as **[category, per reference]** using **[named cryptographic standard]**.

**Assumptions made.** That the SFMC is the responsible component — reasonable given §2.6, but the original never says so. The two bracketed values are placeholders.

**Questions for stakeholders.**
- What classification scheme distinguishes communications requiring encryption?
- Which cryptographic standard applies (FIPS 140-3, a CCSDS profile, something else)?
- Should all communications simply be encrypted, removing the classification problem entirely?

---

## Summary

| ID | Rewritten? | Blocking information |
|---|---|---|
| REQ-006 | No | Arrival tolerance value |
| REQ-010 | Partially | Contingency sequence |
| REQ-040 | Structure only | Reliability target + operational profile |
| REQ-043 | Structure only | Degraded-mode matrix |
| REQ-035 / 015 | Structure only | Which inhibits are overridable |
| REQ-025 | Structure only | Data classification + crypto standard |

None of the six could be fully repaired from the document alone. That is the finding, not a
shortfall: most requirement defects in this SRS are **missing stakeholder decisions**, not poor
wording. A reviewer who "fixed" all six by supplying numbers would have quietly authored six
engineering decisions nobody reviewed.
