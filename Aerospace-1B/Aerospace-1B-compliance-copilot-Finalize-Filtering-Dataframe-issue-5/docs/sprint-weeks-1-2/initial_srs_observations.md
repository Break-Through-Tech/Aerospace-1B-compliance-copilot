# initial_srs_observations.md
**Project:** Aerospace Compliance Copilot — Week 1–2 Sprint  
**Target Document:** Starhawk Space Fighter Mission Computer SRS (`SH-SRS-001`, v1.0 Draft)  
**Evaluation Standards:** NASA NPR 7150.2D (§4.1) & NASA Software Engineering Handbook (SWEHB §5.09)  

---

## 1. What Information Does the Document Contain?
The document is a preliminary System/Software Requirements Specification containing:
- **System Scope & Boundaries:** High-level narrative of the Starhawk Space Fighter Mission Computer (SFMC), core subsystems, and five distinct operational modes (*Standby, Manual Flight, Autopilot, Combat, Emergency*).
- **Subsystem Interfaces:** Qualitative interface summaries (pilot controls/displays, navigation, propulsion, weapons, defense, communications).
- **Software Requirements Set:** 54 numbered requirements distributed across 7 operational and quality domains (functional navigation, vehicle health, reliability, security, constraints, etc.).
- **Preliminary Traceability Source:** A top-level list of 10 Mission Needs (`MN-01` to `MN-10`).
- **Open Items Register:** A 10-point list of unresolved engineering definitions.

---

## 2. How Are Requirements Identified?
- **Formal Identifiers:** Requirements in Sections 3 through 9 follow a structured convention: `SFMC-REQ-[001–054]`, followed by a short title (e.g., `SFMC-REQ-008 — Fuel Warning`).
- **Normative Verb ("Shall"):** Formal items utilize the imperative keyword **"shall"** (or negative constraint **"shall never"**), which aligns with the standard convention described in NASA SWEHB 5.09 for denoting binding system obligations.
- **Traceability Linkages:** The requirements do not yet include inline parent tags (e.g., `[Traces to: MN-01]`).

---

## 3. What Distinguishes Explanatory Text from Actual Requirements?
- **Structural Location:** Narrative overviews (Sections 1.1–1.3) and interface summaries (Sections 2.2–2.6) use descriptive present tense (*"The SFMC exchanges commands...", "The Navigation System provides..."*) to establish operational context.
- **Syntactic Bleed (The Section 2.1 Anomaly):** In Section 2.1 (*Pilot Interface*), the author writes:
  > *"The SFMC shall receive pilot commands from the cockpit controls."*  
  > *"The SFMC shall display spacecraft status information on the pilot's primary display."*  
  These contain the binding keyword `"shall"` but **lack requirement tags (`SFMC-REQ-xxx`)** and reside in an introductory section. Per SWEHB 5.09 guidelines, untagged "shall" statements create ambiguity about whether they are binding contractual obligations or descriptive context.

---

## 4. What Information Would a Developer Obtain from This Document?
- **What a Developer Can Use:** A clear high-level understanding of the architecture, operating state machine, and required input/output subsystems.
- **What a Developer Is Missing (Implementation Roadblocks):**
  - *No Algorithmic Logic:* `SFMC-REQ-004` demands calculating a "safe and efficient route," and `SFMC-REQ-010` orders "appropriate corrective action" without defining the path-planning algorithms, clearance buffers, or engine failure contingency logic.
  - *Missing Data Formats & Protocols:* No packet structures, bus frequencies, or data dictionaries are provided for the spacecraft data network (`SFMC-REQ-052`).

---

## 5. What Information Would a Tester Obtain from This Document?
- **What a Tester Can Verify:** Deterministic, quantitative requirements that have clear pass/fail thresholds:
  - `SFMC-REQ-002`: Position display update rate $\le 500\text{ ms}$.
  - `SFMC-REQ-008` & `009`: Fuel warning triggers at exactly $< 15\%$ and $< 5\%$.
  - `SFMC-REQ-027`: Fault annunciated on pilot display within $\le 1\text{ s}$.
  - `SFMC-REQ-036`: Boot/operational readiness within $\le 30\text{ s}$.
- **What a Tester Cannot Verify (Fails SWEHB §5.09 Verifiability):**
  - Words such as "reasonably close" (`REQ-006`), "extremely accurate" (`REQ-016`), "quickly" (`REQ-021`), and "without noticeable delay" (`REQ-037`) lack objective test criteria. A tester cannot write a pass/fail verification test procedure for subjective terms.
  - `SFMC-REQ-040` (*"The SFMC software shall never crash..."*) states an unprovable universal negative; software reliability must instead be proven against finite operational profiles or statistical failure rates.

---

## 6. Which Requirements Initially Seem Unusually Strong vs. Weak?

### Strong Requirements (Comply with SWEHB §5.09 Quality Attributes)
- **`SFMC-REQ-002` (Navigation Update):** Clearly specifies condition, action, operating modes, and an explicit quantitative update frequency ($\le 500\text{ ms}$).
- **`SFMC-REQ-009` (Critical Fuel Warning):** Unambiguous threshold ($< 5\%$) coupled to two distinct, testable outputs (display warning and audible alarm).
- **`SFMC-REQ-029` (Fault Log Contents):** Completely enumerates the required data payload items (ID, subsystem, timestamp, description).

### Weak Requirements (Violate NASA SWEHB §5.09 & NPR 7150.2D Principles)
- **`SFMC-REQ-006` (Autopilot Arrival):** Uses the subjective qualifier *"reasonably close"*, making acceptance criteria impossible to establish.
- **`SFMC-REQ-010` (Engine Failure):** Directs the system to take *"appropriate corrective action"*, which delegates critical flight safety design choices to software developers rather than specifying the behavior.
- **`SFMC-REQ-042` (Data Preservation):** Protects *"important mission data"* without defining a data classification taxonomy.
- **`SFMC-REQ-050` (Security):** Mandates *"state-of-the-art security techniques"*, a vague phrase that dates quickly and lacks compliance standards (e.g., FIPS, AES-256).

---

## 7. What Questions Would You Ask the Stakeholders?
*(These target the unresolved definitions listed in SRS Section 11, which must be closed before the requirements can be baselined.)*

1. **Flight Dynamics / GNC:** What are the exact spherical keep-out zones and obstacle clearance radii that define a "safe route" (`REQ-004`) and the maximum allowable arrival radius for "reasonably close" (`REQ-006`)?
2. **Propulsion / Safety Engineering:** What exact recovery sequence constitutes "appropriate corrective action" (`REQ-010`) upon main engine failure (e.g., fire RCS thrusters to stabilize, isolate fuel valves, automatically switch to Emergency mode)?
3. **Human Systems Integration (HSI):** What is the quantitative latency ceiling for pilot controls (`REQ-037`) to avoid lag (e.g., $\le 50\text{ ms}$ input-to-display)?
4. **Cybersecurity Operations:** Which specific cryptographic protocols and authentication standards (e.g., FIPS 140-3, CCSDS-compliant algorithms) must be used (`REQ-048`, `049`, `050`)?
5. **Program Management / Systems Engineering:** When will the complete bidirectional Traceability Matrix (mapping `SFMC-REQ-001` through `054` back to `MN-01` through `MN-10`) be provided as required by NPR 7150.2D **SWE-052**?

---

## 8. Additional Observations

### Undefined qualifiers recur across the whole set
The same vague adjectives appear in unrelated requirements, and none is defined anywhere in the document:

- **"important"** — `REQ-025` (communications), `REQ-042` (mission data)
- **"critical"** — `REQ-009` (fuel), `REQ-030` (faults)
- **"safe"** — `REQ-004` (route), `REQ-033` (destination), `REQ-034` (location)

Read one at a time, each looks like a local wording problem. Read together, it's one problem: the SRS has no shared vocabulary. That distinction matters because it can only be seen by reading the full document, not any single requirement.

### Some requirements bundle several obligations under one ID
- `REQ-045`: six distinct log event classes
- `REQ-013`: four separate display fields
- `REQ-009`: two behaviors — display a warning *and* sound an alarm

Each clause needs its own test, but they share one identifier. If five of six log event types are implemented, there is no clean way to record that as either pass or fail.