# Software Requirements Compliance Review

- **Document ID:** SH-SRS-001
- **Document version:** 1.0
- **Evaluation scope:** FULL_SRS
- **Generated at (UTC):** 2026-11-11T23:26:50Z
- **Method:** RAG: top-5 clauses retrieved from Chroma (all-MiniLM-L6-v2) plus 3 always-included clauses; verdicts by gemini-3.5-flash (served by the API as gemini-3.6-flash) with structured output; citations filled from addressable_clauses.csv; validated with report_schema.py; relationships, document findings, and SWE coverage by gemini-3.5-flash in notebook 09 (one call per section, whole SRS in context), citations filled from addressable_clauses.csv

## Limitations

- No NASA project compliance is determined from the SRS alone.
- Verdicts are LLM-generated and have not been checked by a human reviewer.
- Relationships cover only the three benchmark requirement pairs; other pairs were not compared.

## Summary

### Requirements by quality status

| Quality status | Count |
|---|---:|
| ACCEPTABLE | 24 |
| NEEDS_REVIEW | 30 |

### Issue code frequency

| Issue code | Count |
|---|---:|
| ALLOCATION_UNCLEAR | 3 |
| ESCAPE_CLAUSE | 1 |
| OTHER | 1 |
| SAFETY_INTERACTION | 1 |
| SCOPE_AMBIGUITY | 4 |
| UNDEFINED_TERM | 16 |
| UNSPECIFIED_RESPONSE | 2 |
| UNVERIFIABLE_ABSOLUTE | 1 |
| VAGUE_CRITERION | 14 |

## Requirement Review Summary

| Requirement ID | Quality status | Issue codes | Primary SWE |
|---|---|---|---|
| SFMC-REQ-001 | ACCEPTABLE | None | None |
| SFMC-REQ-002 | ACCEPTABLE | None | None |
| SFMC-REQ-003 | ACCEPTABLE | None | None |
| SFMC-REQ-004 | NEEDS_REVIEW | VAGUE_CRITERION, UNDEFINED_TERM | None |
| SFMC-REQ-005 | NEEDS_REVIEW | SCOPE_AMBIGUITY | None |
| SFMC-REQ-006 | NEEDS_REVIEW | VAGUE_CRITERION | None |
| SFMC-REQ-007 | NEEDS_REVIEW | VAGUE_CRITERION | None |
| SFMC-REQ-008 | ACCEPTABLE | None | None |
| SFMC-REQ-009 | ACCEPTABLE | None | None |
| SFMC-REQ-010 | NEEDS_REVIEW | UNSPECIFIED_RESPONSE | SWE-184 |
| SFMC-REQ-011 | ACCEPTABLE | None | None |
| SFMC-REQ-012 | ACCEPTABLE | None | None |
| SFMC-REQ-013 | ACCEPTABLE | None | None |
| SFMC-REQ-014 | ACCEPTABLE | None | SWE-184 |
| SFMC-REQ-015 | NEEDS_REVIEW | UNDEFINED_TERM | SWE-184 |
| SFMC-REQ-016 | NEEDS_REVIEW | VAGUE_CRITERION, ALLOCATION_UNCLEAR | None |
| SFMC-REQ-017 | ACCEPTABLE | None | None |
| SFMC-REQ-018 | NEEDS_REVIEW | VAGUE_CRITERION, UNDEFINED_TERM | None |
| SFMC-REQ-019 | ACCEPTABLE | None | None |
| SFMC-REQ-020 | ACCEPTABLE | None | None |
| SFMC-REQ-021 | NEEDS_REVIEW | VAGUE_CRITERION, UNSPECIFIED_RESPONSE, UNDEFINED_TERM | None |
| SFMC-REQ-022 | ACCEPTABLE | None | None |
| SFMC-REQ-023 | ACCEPTABLE | None | None |
| SFMC-REQ-024 | ACCEPTABLE | None | None |
| SFMC-REQ-025 | NEEDS_REVIEW | UNDEFINED_TERM, VAGUE_CRITERION | None |
| SFMC-REQ-026 | NEEDS_REVIEW | UNDEFINED_TERM, VAGUE_CRITERION | None |
| SFMC-REQ-027 | ACCEPTABLE | None | None |
| SFMC-REQ-028 | ACCEPTABLE | None | None |
| SFMC-REQ-029 | ACCEPTABLE | None | None |
| SFMC-REQ-030 | NEEDS_REVIEW | UNDEFINED_TERM, VAGUE_CRITERION | None |
| SFMC-REQ-031 | NEEDS_REVIEW | ALLOCATION_UNCLEAR | SWE-184 |
| SFMC-REQ-032 | NEEDS_REVIEW | UNDEFINED_TERM, VAGUE_CRITERION | SWE-184 |
| SFMC-REQ-033 | NEEDS_REVIEW | UNDEFINED_TERM, VAGUE_CRITERION | SWE-184 |
| SFMC-REQ-034 | NEEDS_REVIEW | UNDEFINED_TERM | SWE-184 |
| SFMC-REQ-035 | NEEDS_REVIEW | SCOPE_AMBIGUITY, SAFETY_INTERACTION | SWE-184 |
| SFMC-REQ-036 | ACCEPTABLE | None | None |
| SFMC-REQ-037 | NEEDS_REVIEW | VAGUE_CRITERION | None |
| SFMC-REQ-038 | NEEDS_REVIEW | SCOPE_AMBIGUITY | None |
| SFMC-REQ-039 | ACCEPTABLE | None | None |
| SFMC-REQ-040 | NEEDS_REVIEW | UNVERIFIABLE_ABSOLUTE | None |
| SFMC-REQ-041 | NEEDS_REVIEW | UNDEFINED_TERM | None |
| SFMC-REQ-042 | NEEDS_REVIEW | UNDEFINED_TERM | None |
| SFMC-REQ-043 | NEEDS_REVIEW | ESCAPE_CLAUSE | None |
| SFMC-REQ-044 | ACCEPTABLE | None | None |
| SFMC-REQ-045 | ACCEPTABLE | None | None |
| SFMC-REQ-046 | ACCEPTABLE | None | None |
| SFMC-REQ-047 | NEEDS_REVIEW | VAGUE_CRITERION | None |
| SFMC-REQ-048 | NEEDS_REVIEW | UNDEFINED_TERM, SCOPE_AMBIGUITY | None |
| SFMC-REQ-049 | NEEDS_REVIEW | UNDEFINED_TERM | None |
| SFMC-REQ-050 | NEEDS_REVIEW | VAGUE_CRITERION | None |
| SFMC-REQ-051 | ACCEPTABLE | None | None |
| SFMC-REQ-052 | NEEDS_REVIEW | UNDEFINED_TERM | None |
| SFMC-REQ-053 | NEEDS_REVIEW | ALLOCATION_UNCLEAR, UNDEFINED_TERM | None |
| SFMC-REQ-054 | NEEDS_REVIEW | OTHER | SWE-184 |

## Requirement Details

### SFMC-REQ-004

**Requirement text:** When the pilot selects a destination, the SFMC shall calculate a safe and efficient route to the destination.

**Quality status:** NEEDS_REVIEW

#### VAGUE_CRITERION

- **Severity:** MAJOR
- **Explanation:** The requirement specifies that the route must be 'efficient' without providing any measurable bounds, metrics, or thresholds (e.g., fuel usage, time of arrival) to evaluate compliance.
- **Requires stakeholder input:** True
- **Recommendation:** Define measurable performance and resource criteria for route efficiency, such as maximum time or fuel usage bounds, with stakeholder input.

**SRS evidence:**

- **§3.1, SFMC-REQ-004:** "efficient"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §7.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

#### UNDEFINED_TERM

- **Severity:** MAJOR
- **Explanation:** The term 'safe' is undefined in the requirement, leaving the criteria for hazard avoidance or path constraints unspecified. This defect is acknowledged in §11 Open Item 1.
- **Requires stakeholder input:** True
- **Recommendation:** Specify explicit rules and constraints for what constitutes a 'safe' route (e.g., minimum clearance distance from hazardous bodies or hostile zones).

**SRS evidence:**

- **§3.1, SFMC-REQ-004:** "safe"
- **§11, Open Item 1:** "Definition of a safe route."

**NASA references:**

- [NASA-HDBK-2203-5.09 | §7.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §3.2.1.6](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-005

**Requirement text:** When Autopilot mode is enabled, the SFMC shall control the spacecraft propulsion system to follow the selected route.

**Quality status:** NEEDS_REVIEW

#### SCOPE_AMBIGUITY

- **Severity:** MAJOR
- **Explanation:** The requirement specifies behavior when 'Autopilot mode is enabled' to follow 'the selected route', but fails to define the software condition or behavior if Autopilot mode is engaged when no destination or route has been selected.
- **Requires stakeholder input:** True
- **Recommendation:** Specify the required system response or safety behavior if Autopilot mode is activated without an active, valid route selection.

**SRS evidence:**

- **§3.1, SFMC-REQ-005:** "When Autopilot mode is enabled, the SFMC shall control the spacecraft propulsion system to follow the selected route."

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §3.2.1.5](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-006

**Requirement text:** The autopilot shall deliver the spacecraft reasonably close to the selected destination.

**Quality status:** NEEDS_REVIEW

#### VAGUE_CRITERION

- **Severity:** MAJOR
- **Explanation:** The criterion 'reasonably close' is subjective and lacks a measurable bound or target threshold for distance, making the requirement unverifiable through finite testing.
- **Requires stakeholder input:** True
- **Recommendation:** Replace 'reasonably close' with a quantitative positional tolerance threshold (e.g., within X kilometers of the selected destination). Stakeholder input is required to resolve Open Item 2.

**SRS evidence:**

- **§3.1, SFMC-REQ-006:** "reasonably close"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §3.2.1.5](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §3.2.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-007

**Requirement text:** The SFMC shall continuously monitor the status of the spacecraft's main engines.

**Quality status:** NEEDS_REVIEW

#### VAGUE_CRITERION

- **Severity:** MAJOR
- **Explanation:** The term 'continuously monitor' lacks a measurable timing bound or frequency (such as a sampling interval or update rate). Because software executes in discrete cycles, an unquantified requirement for 'continuous' monitoring cannot be verified through testing without a specified rate.
- **Requires stakeholder input:** True
- **Recommendation:** Specify the exact sampling rate or maximum interval (e.g., at least once every 100 ms) at which the SFMC must poll or process main engine status data.

**SRS evidence:**

- **§3.2, SFMC-REQ-007:** "continuously monitor"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §3.2.1.5](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-010

**Requirement text:** If the SFMC detects a failure of a main engine, it shall notify the pilot and take appropriate corrective action.

**Quality status:** NEEDS_REVIEW

#### UNSPECIFIED_RESPONSE

- **Severity:** MAJOR
- **Explanation:** The requirement specifies a trigger (detection of a main engine failure) but uses the placeholder phrase 'take appropriate corrective action' instead of defining the specific software response or recovery logic.
- **Requires stakeholder input:** True
- **Recommendation:** Define the specific automated corrective actions the SFMC must execute upon detecting a main engine failure (e.g., thrust rebalancing, fuel cutoff, or transitioning to Emergency mode).

**SRS evidence:**

- **§3.2, SFMC-REQ-010:** "take appropriate corrective action"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §3.2.1.9](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-015

**Requirement text:** The SFMC shall never permit the pilot to fire a weapon at a friendly spacecraft.

**Quality status:** NEEDS_REVIEW

#### UNDEFINED_TERM

- **Severity:** MAJOR
- **Explanation:** The requirement prohibits permitting the pilot to fire at a 'friendly spacecraft', but the criteria used to classify a spacecraft as friendly are undefined and acknowledged as an unresolved open item in the SRS.
- **Requires stakeholder input:** True
- **Recommendation:** Specify the exact criteria, message types, or system inputs (such as IFF responses or fleet status flags) used by the SFMC software to classify a spacecraft as friendly.

**SRS evidence:**

- **§3.3, SFMC-REQ-015:** "friendly spacecraft"
- **§11, Open Item 10:** "Criteria for determining whether a detected spacecraft is friendly or hostile."

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §6.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-016

**Requirement text:** The targeting system shall be extremely accurate.

**Quality status:** NEEDS_REVIEW

#### VAGUE_CRITERION

- **Severity:** MAJOR
- **Explanation:** The requirement relies on the subjective phrase 'extremely accurate' without providing measurable bounds, error tolerances, or quantitative targeting metrics.
- **Requires stakeholder input:** True
- **Recommendation:** Define explicit, measurable targeting accuracy parameters (such as maximum allowable position or angular error) in coordination with project stakeholders, as noted in Section 11 Open Item 7.

**SRS evidence:**

- **§3.3, SFMC-REQ-016:** "extremely accurate"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §3.2.1.5](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

#### ALLOCATION_UNCLEAR

- **Severity:** MAJOR
- **Explanation:** The requirement assigns the obligation to 'the targeting system' rather than specifying the SFMC software, leaving it unclear whether this requirement applies to the mission computer software or external weapons hardware/subsystems.
- **Requires stakeholder input:** True
- **Recommendation:** Clarify the target of the requirement to explicitly name the SFMC software and delineate software responsibilities from external targeting hardware.

**SRS evidence:**

- **§3.3, SFMC-REQ-016:** "targeting system"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §1.b](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-018

**Requirement text:** The SFMC shall clearly indicate which incoming threat represents the greatest danger to the spacecraft.

**Quality status:** NEEDS_REVIEW

#### VAGUE_CRITERION

- **Severity:** MAJOR
- **Explanation:** The requirement specifies that the software shall 'clearly indicate' the threat, which is a subjective criterion that lacks measurable verification parameters or explicit visual interface requirements.
- **Requires stakeholder input:** True
- **Recommendation:** Specify the exact display mechanism (e.g., highlight in red, flash icon, or position at top of threat list) to make the requirement testable.

**SRS evidence:**

- **§3.4, SFMC-REQ-018:** "clearly indicate"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §7.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

#### UNDEFINED_TERM

- **Severity:** MAJOR
- **Explanation:** The term 'greatest danger' is not defined in the SRS, leaving the algorithm or operational logic for threat ranking unspecified.
- **Requires stakeholder input:** True
- **Recommendation:** Define the objective criteria (e.g., time to impact, target proximity, target classification) used by the SFMC to calculate threat priority.

**SRS evidence:**

- **§3.4, SFMC-REQ-018:** "greatest danger"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §7.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-021

**Requirement text:** The SFMC shall respond quickly to dangerous threats.

**Quality status:** NEEDS_REVIEW

#### VAGUE_CRITERION

- **Severity:** MAJOR
- **Explanation:** The term 'quickly' is a subjective degree word that provides no measurable bound or timing threshold, rendering the requirement unverifiable.
- **Requires stakeholder input:** True
- **Recommendation:** Specify an explicit maximum response latency (e.g., within 100 milliseconds) for threat handling.

**SRS evidence:**

- **§3.4, SFMC-REQ-021:** "quickly"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §7.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

#### UNSPECIFIED_RESPONSE

- **Severity:** MAJOR
- **Explanation:** The requirement states that the software shall 'respond', but fails to specify what concrete action or sequence of operations the SFMC must execute upon detecting a threat.
- **Requires stakeholder input:** True
- **Recommendation:** Define the specific software behaviors required when a threat is detected (e.g., deploying automated countermeasures, alerting the pilot, or initiating evasive maneuvering).

**SRS evidence:**

- **§3.4, SFMC-REQ-021:** "respond"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

#### UNDEFINED_TERM

- **Severity:** MAJOR
- **Explanation:** The requirement uses the phrase 'dangerous threats' without defining the classification parameters or criteria used to categorize a threat as dangerous.
- **Requires stakeholder input:** True
- **Recommendation:** Specify the threat classification criteria or reference a defined threat evaluation document that identifies which threat conditions trigger this requirement.

**SRS evidence:**

- **§3.4, SFMC-REQ-021:** "dangerous threats"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §7.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-025

**Requirement text:** All important communications shall be securely encrypted.

**Quality status:** NEEDS_REVIEW

#### UNDEFINED_TERM

- **Severity:** MAJOR
- **Explanation:** The requirement specifies encryption for 'important communications', but the SRS does not define which communications are classified as important, rendering the applicability scope undefined.
- **Requires stakeholder input:** True
- **Recommendation:** Specify the explicit communication types or channels (e.g., all outgoing telemetry, command messages) to which encryption applies.

**SRS evidence:**

- **§3.5, SFMC-REQ-025:** "important communications"
- **§11, Open Item 4:** "Definition of important communication."

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1.8](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §7.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

#### VAGUE_CRITERION

- **Severity:** MAJOR
- **Explanation:** The modifier 'securely encrypted' is non-verifiable because it lacks an objective encryption algorithm, standard, or protocol specification.
- **Requires stakeholder input:** True
- **Recommendation:** Define the mandatory cryptographic algorithm or protocol standard (such as AES-256 or TLS 1.3).

**SRS evidence:**

- **§3.5, SFMC-REQ-025:** "securely encrypted"
- **§11, Open Item 9:** "Required cybersecurity algorithms and standards."

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1.8](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §3.2.3.6](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-026

**Requirement text:** The SFMC shall monitor the health of the Navigation, Propulsion, Weapons, Defensive, and Communications systems.

**Quality status:** NEEDS_REVIEW

#### UNDEFINED_TERM

- **Severity:** MAJOR
- **Explanation:** The term 'health' is not defined within the SRS for the Navigation, Propulsion, Weapons, Defensive, or Communications subsystems, leaving developers and testers unable to determine which specific telemetry metrics, status flags, or diagnostics the software is required to evaluate.
- **Requires stakeholder input:** True
- **Recommendation:** Define the specific parameters, status messages, or heartbeat signals that constitute system 'health' for each of the five listed subsystems.

**SRS evidence:**

- **§3.6, SFMC-REQ-026:** "health"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §3.2.1.5](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

#### VAGUE_CRITERION

- **Severity:** MAJOR
- **Explanation:** The requirement specifies that the software shall 'monitor' subsystem health but omits any measurable execution frequency, polling interval, or sampling rate.
- **Requires stakeholder input:** True
- **Recommendation:** Specify the required monitoring rate or polling cycle (e.g., periodic sampling interval in milliseconds) for monitoring subsystem health.

**SRS evidence:**

- **§3.6, SFMC-REQ-026:** "monitor the health"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §3.2.1.5](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-030

**Requirement text:** The SFMC shall immediately notify the pilot of all critical faults.

**Quality status:** NEEDS_REVIEW

#### UNDEFINED_TERM

- **Severity:** MAJOR
- **Explanation:** The term 'critical faults' is not defined within the SRS, leaving it unclear which fault conditions require this behavior. Section 11 acknowledges this gap as Open Item 3 ('Definition of critical fault').
- **Requires stakeholder input:** True
- **Recommendation:** Define a explicit categorization or listing of fault types that constitute critical faults in collaboration with system stakeholders.

**SRS evidence:**

- **§3.6, SFMC-REQ-030:** "critical faults"
- **§11, Open Item 3:** "Definition of critical fault."

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1.9](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §6.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

#### VAGUE_CRITERION

- **Severity:** MAJOR
- **Explanation:** The timing term 'immediately' lacks a bounded, measurable threshold (such as a maximum response time in milliseconds), rendering the temporal requirement unverifiable by test.
- **Requires stakeholder input:** True
- **Recommendation:** Replace 'immediately' with an explicit maximum duration threshold (e.g., 'within 250 milliseconds').

**SRS evidence:**

- **§3.6, SFMC-REQ-030:** "immediately"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §3.2.1.9](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-031

**Requirement text:** The pilot shall be able to place the SFMC into Emergency mode using a dedicated cockpit control.

**Quality status:** NEEDS_REVIEW

#### ALLOCATION_UNCLEAR

- **Severity:** MINOR
- **Explanation:** The requirement uses 'The pilot shall' as the subject instead of specifying the obligation on the SFMC software to transition to Emergency mode when the cockpit control signal is received.
- **Requires stakeholder input:** False
- **Recommendation:** Rephrase the requirement to state software behavior directly, e.g., 'The SFMC shall transition to Emergency mode upon receiving an activation signal from the dedicated emergency cockpit control.'

**SRS evidence:**

- **§4, SFMC-REQ-031:** "The pilot shall be able to place the SFMC into Emergency mode"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §1.b](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-032

**Requirement text:** While operating in Emergency mode, the SFMC shall prioritize life-support, navigation, and propulsion functions over nonessential spacecraft functions.

**Quality status:** NEEDS_REVIEW

#### UNDEFINED_TERM

- **Severity:** MAJOR
- **Explanation:** The term 'nonessential spacecraft functions' relies on a functional category that is never defined in the SRS, leaving implementation and verification teams without objective boundaries for what software functions to shed or suppress.
- **Requires stakeholder input:** True
- **Recommendation:** Explicitly define which spacecraft subsystems and software tasks are categorized as nonessential during Emergency mode operations.

**SRS evidence:**

- **§4, SFMC-REQ-032:** "nonessential spacecraft functions"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §7.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

#### VAGUE_CRITERION

- **Severity:** MAJOR
- **Explanation:** The requirement specifies that the software shall 'prioritize' certain functions without defining the required software mechanism or performance threshold (e.g., task preemption, CPU resource allocation limits, network bandwidth throttling, or disabling nonessential interfaces).
- **Requires stakeholder input:** True
- **Recommendation:** Specify the exact software implementation logic for prioritization, such as suspending nonessential task execution or allocating deterministic CPU cycles and interface bandwidth to critical functions.

**SRS evidence:**

- **§4, SFMC-REQ-032:** "prioritize"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §7.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-033

**Requirement text:** If the spacecraft is seriously damaged, the SFMC shall automatically determine the safest destination.

**Quality status:** NEEDS_REVIEW

#### UNDEFINED_TERM

- **Severity:** MAJOR
- **Explanation:** The condition 'seriously damaged' is not defined in the SRS, leaving the trigger criteria for this emergency function ambiguous and unverifiable.
- **Requires stakeholder input:** True
- **Recommendation:** Specify explicit operational conditions or fault thresholds (such as loss of hull integrity percentage or failure of specific critical propulsion components) that constitute serious damage.

**SRS evidence:**

- **§4, SFMC-REQ-033:** "seriously damaged"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §7.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

#### VAGUE_CRITERION

- **Severity:** MAJOR
- **Explanation:** The requirement uses the superlative 'safest destination' without providing measurable criteria or priority logic to evaluate destination safety.
- **Requires stakeholder input:** True
- **Recommendation:** Define explicit criteria for destination safety ranking, such as proximity, available fuel vs. required delta-v, and presence of friendly forces or landing facilities.

**SRS evidence:**

- **§4, SFMC-REQ-033:** "safest destination"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §7.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-034

**Requirement text:** The SFMC shall be capable of automatically flying the spacecraft to a safe location during an emergency.

**Quality status:** NEEDS_REVIEW

#### UNDEFINED_TERM

- **Severity:** MAJOR
- **Explanation:** The requirement relies on 'safe location', which is not defined anywhere in the SRS, leaving the automated flight objective unverifiable and forcing design assumptions.
- **Requires stakeholder input:** True
- **Recommendation:** Specify the precise criteria, coordinates, or deterministic decision rules the SFMC software must use to select a safe location during emergency operations.

**SRS evidence:**

- **§4, SFMC-REQ-034:** "safe location"
- **§11, Open Item 5:** "Definition of a safe location during an emergency."

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §7.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-035

**Requirement text:** The pilot shall always be able to override automatic spacecraft controls.

**Quality status:** NEEDS_REVIEW

#### SCOPE_AMBIGUITY

- **Severity:** MAJOR
- **Explanation:** The term 'automatic spacecraft controls' is ambiguous because the SRS does not specify which automated functions or operational modes (e.g., Autopilot in SFMC-REQ-005, Emergency Autopilot in SFMC-REQ-034, Automatic Countermeasures in SFMC-REQ-020) are subject to pilot override.
- **Requires stakeholder input:** True
- **Recommendation:** Explicitly identify all automated functions, control loops, and operational modes that the pilot can override.

**SRS evidence:**

- **§4, SFMC-REQ-035:** "automatic spacecraft controls"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1.2](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

#### SAFETY_INTERACTION

- **Severity:** MAJOR
- **Explanation:** The requirement states the pilot must 'always be able to override' automated controls, but fails to define the safety precedence, input mechanism, or constraints (such as requiring two independent pilot actions to prevent inadvertent override during critical automated maneuvers).
- **Requires stakeholder input:** True
- **Recommendation:** Define the precise pilot actions required to perform an override, precedence logic between manual inputs and automatic controls, and any safety constraints on override execution.

**SRS evidence:**

- **§4, SFMC-REQ-035:** "always be able to override"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1.4](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-037

**Requirement text:** The SFMC shall respond to pilot commands without noticeable delay.

**Quality status:** NEEDS_REVIEW

#### VAGUE_CRITERION

- **Severity:** MAJOR
- **Explanation:** The phrase 'without noticeable delay' is subjective and not measurable. A test cannot conclusively establish compliance without a defined quantitative response time limit (such as a maximum allowable latency in milliseconds).
- **Requires stakeholder input:** True
- **Recommendation:** Replace 'without noticeable delay' with a specific maximum response time limit (e.g., 'within 100 milliseconds'), taking into account §11 Open Item 8.

**SRS evidence:**

- **§5, SFMC-REQ-037:** "without noticeable delay"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-038

**Requirement text:** During normal operation, the SFMC shall update flight information displayed to the pilot at least 10 times per second.

**Quality status:** NEEDS_REVIEW

#### SCOPE_AMBIGUITY

- **Severity:** MINOR
- **Explanation:** The phrase 'normal operation' is used to scope the requirement, but SRS §1.3 defines operational modes as Standby, Manual Flight, Autopilot, Combat, and Emergency. It is unclear whether 'normal operation' applies to all non-emergency modes or a specific subset of modes.
- **Requires stakeholder input:** True
- **Recommendation:** Replace 'normal operation' with explicit operational modes (such as Manual Flight, Autopilot, and Combat) defined in SRS §1.3.

**SRS evidence:**

- **§5, SFMC-REQ-038:** "normal operation"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1.2](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-040

**Requirement text:** The SFMC software shall never crash during a mission.

**Quality status:** NEEDS_REVIEW

#### UNVERIFIABLE_ABSOLUTE

- **Severity:** MAJOR
- **Explanation:** The phrase 'shall never crash' constitutes an absolute universal statement across unbounded operational inputs and execution scenarios. Finite testing cannot verify that a crash will never occur under any circumstance.
- **Requires stakeholder input:** True
- **Recommendation:** Stakeholders should replace this absolute statement with verifiable reliability, availability, or fault-handling metrics, such as a specified Mean Time Between Failures (MTBF) or explicit fault-recovery requirements.

**SRS evidence:**

- **§6, SFMC-REQ-040:** "shall never crash"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §7.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-041

**Requirement text:** If a recoverable software fault occurs, the SFMC shall recover automatically without requiring pilot intervention.

**Quality status:** NEEDS_REVIEW

#### UNDEFINED_TERM

- **Severity:** MAJOR
- **Explanation:** The requirement conditions behavior on a 'recoverable software fault', but the SRS provides no definition, categorization, or criteria to distinguish software faults that are recoverable from those that are not, rendering test verification ambiguous.
- **Requires stakeholder input:** True
- **Recommendation:** Specify the exact types of software faults (e.g., process crashes, execution timeouts, memory exceptions) that require automatic recovery, along with the required recovery mechanism (e.g., module restart, fallback state, or checkpoint restore).

**SRS evidence:**

- **§6, SFMC-REQ-041:** "recoverable software fault"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1.9](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §6.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-042

**Requirement text:** Recovery from a software fault shall not cause the loss of important mission data.

**Quality status:** NEEDS_REVIEW

#### UNDEFINED_TERM

- **Severity:** MAJOR
- **Explanation:** The requirement relies on the term 'important mission data', but the SRS does not define which data categories or specific state/log items are considered 'important'. Without defining what data must be retained, implementation cannot guarantee proper persistence, and verification cannot test for data loss.
- **Requires stakeholder input:** True
- **Recommendation:** Specify the explicit data types, parameters, or logs (e.g., mission log, current navigation state, vehicle fault history) that must be preserved during fault recovery.

**SRS evidence:**

- **§6, SFMC-REQ-042:** "important mission data"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §6.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-043

**Requirement text:** If a spacecraft subsystem becomes unavailable, the SFMC shall continue operating using the remaining available systems whenever possible.

**Quality status:** NEEDS_REVIEW

#### ESCAPE_CLAUSE

- **Severity:** MAJOR
- **Explanation:** The qualifier 'whenever possible' excuses non-compliance and makes the requirement unverifiable, as it does not define specific conditions, degraded modes, or boundaries under which the software is obligated to maintain operation.
- **Requires stakeholder input:** True
- **Recommendation:** Remove the escape clause and specify explicit degraded operating modes and capabilities for each subsystem failure scenario.

**SRS evidence:**

- **§6, SFMC-REQ-043:** "whenever possible"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §6.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-047

**Requirement text:** The mission log shall contain sufficient storage for an entire mission.

**Quality status:** NEEDS_REVIEW

#### VAGUE_CRITERION

- **Severity:** MAJOR
- **Explanation:** The requirement specifies 'sufficient storage' without defining a quantifiable capacity (e.g., megabytes, gigabytes, or maximum number of log entries), making it unverifiable during testing.
- **Requires stakeholder input:** True
- **Recommendation:** Specify the exact data storage size (or entry capacity) needed to accommodate event logging over the maximum defined mission duration.

**SRS evidence:**

- **§7, SFMC-REQ-047:** "sufficient storage"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1.3](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §6.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-048

**Requirement text:** The SFMC shall verify that the pilot is authorized before enabling spacecraft operation.

**Quality status:** NEEDS_REVIEW

#### UNDEFINED_TERM

- **Severity:** MAJOR
- **Explanation:** The requirement states that the SFMC must verify that the pilot is 'authorized', but the SRS does not define the criteria, credentials, or mechanism (e.g., biometrics, passcode, security token) used to verify pilot authorization.
- **Requires stakeholder input:** True
- **Recommendation:** Define the specific authentication mechanisms, credential formats, and authorization criteria required for pilot verification.

**SRS evidence:**

- **§8, SFMC-REQ-048:** "authorized"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §7.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

#### SCOPE_AMBIGUITY

- **Severity:** MAJOR
- **Explanation:** The phrase 'spacecraft operation' is ambiguous regarding which subsystems, modes, or flight controls are inhibited prior to pilot verification versus which basic functions (e.g., telemetry monitoring or standby diagnostics) remain accessible.
- **Requires stakeholder input:** True
- **Recommendation:** Explicitly identify the scope of spacecraft operations and functions that are disabled until pilot authorization is established.

**SRS evidence:**

- **§8, SFMC-REQ-048:** "spacecraft operation"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §7.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-049

**Requirement text:** The SFMC shall reject unauthorized commands received through the spacecraft communications system.

**Quality status:** NEEDS_REVIEW

#### UNDEFINED_TERM

- **Severity:** MAJOR
- **Explanation:** The requirement relies on the term 'unauthorized commands' without defining the security criteria, authentication protocols, or access control rules used to identify whether an incoming command is authorized or unauthorized.
- **Requires stakeholder input:** True
- **Recommendation:** Specify the exact authentication and validation mechanisms (e.g., cryptographic signature verification, authorization tokens, or origin validation) used to determine command authorization, as well as the required response when an unauthorized command is detected (e.g., logging, alerting, or dropping the packet).

**SRS evidence:**

- **§8, SFMC-REQ-049:** "unauthorized commands"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1.7](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §3.2.3.6](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-050

**Requirement text:** The SFMC shall use state-of-the-art security techniques to protect the spacecraft from cyberattack.

**Quality status:** NEEDS_REVIEW

#### VAGUE_CRITERION

- **Severity:** MAJOR
- **Explanation:** The phrase 'state-of-the-art security techniques' is subjective and provides no quantifiable bounds, specific security standards, or defined algorithms to enable verification.
- **Requires stakeholder input:** True
- **Recommendation:** Specify exact cybersecurity standards, authentication protocols, and cryptographic algorithms (e.g., AES-256 encryption, TLS 1.3) required for implementation and verification.

**SRS evidence:**

- **§8, SFMC-REQ-050:** "state-of-the-art security techniques"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §7.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §3.2.1.8](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-052

**Requirement text:** The SFMC shall communicate with spacecraft subsystems using the Starhawk spacecraft data network.

**Quality status:** NEEDS_REVIEW

#### UNDEFINED_TERM

- **Severity:** MAJOR
- **Explanation:** The requirement mandates communication over the 'Starhawk spacecraft data network', but this network interface, its protocols, message formats, and data rates are left undefined in the SRS, and no Interface Control Document (ICD) is referenced.
- **Requires stakeholder input:** True
- **Recommendation:** Specify the exact communication protocols, data formats, and standards to be used on the Starhawk spacecraft data network, or reference the applicable Interface Control Document (ICD) or Interface Design Description (IDD).

**SRS evidence:**

- **§9, SFMC-REQ-052:** "Starhawk spacecraft data network"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.3.6](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-053

**Requirement text:** Authorized maintenance personnel shall be able to install updated SFMC software while the spacecraft is in Standby mode.

**Quality status:** NEEDS_REVIEW

#### ALLOCATION_UNCLEAR

- **Severity:** MAJOR
- **Explanation:** The requirement is phrased around the capability of human personnel ('Authorized maintenance personnel shall be able to') rather than specifying the obligation of the SFMC software to provide an update interface or accept software installations under specified conditions.
- **Requires stakeholder input:** False
- **Recommendation:** Rephrase the requirement with the SFMC software as the subject, for example: 'The SFMC shall provide a software update function that allows authenticated maintenance personnel to install software updates while in Standby mode.'

**SRS evidence:**

- **§9, SFMC-REQ-053:** "Authorized maintenance personnel shall be able to install updated SFMC software"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

#### UNDEFINED_TERM

- **Severity:** MAJOR
- **Explanation:** The requirement references 'Authorized maintenance personnel', but the SRS does not define maintenance personnel user classes, authorization levels, or authentication mechanisms (unlike pilot authorization in SFMC-REQ-048).
- **Requires stakeholder input:** True
- **Recommendation:** Define the maintenance user class and specify the credentials or authorization protocol required to perform software updates.

**SRS evidence:**

- **§9, SFMC-REQ-053:** "Authorized maintenance personnel"

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.1.3](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### SFMC-REQ-054

**Requirement text:** The SFMC shall verify the integrity and authenticity of a software update before installing it.

**Quality status:** NEEDS_REVIEW

#### OTHER

- **Severity:** MAJOR
- **Explanation:** The requirement mandates verifying the integrity and authenticity of software updates prior to installation, but fails to specify the required verification mechanisms, cryptographic algorithms, or acceptance standards. Furthermore, it omits explicit error-handling and rejection behavior when verification fails. Section 11, Open Item 9 explicitly acknowledges that required cybersecurity algorithms and standards are currently unresolved.
- **Requires stakeholder input:** True
- **Recommendation:** Specify the cryptographic standard and algorithms (e.g., digital signatures, cryptographic hashes) required for authenticity and integrity verification, and explicitly define the software rejection and logging response if verification fails once stakeholders resolve Open Item 9.

**SRS evidence:**

- **§9, SFMC-REQ-054:** "verify the integrity and authenticity of a software update before installing it"
- **§11, Open Item 9:** "Required cybersecurity algorithms and standards."

**NASA references:**

- [NASA-HDBK-2203-5.09 | §7.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §3.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

## Relationships

### REL-001

- **Requirements:** SFMC-REQ-015, SFMC-REQ-035
- **Status:** NEEDS_CLARIFICATION
- **Issue code:** SAFETY_INTERACTION
- **Explanation:** There is a potential scope overlap and interaction regarding whether pilot override can bypass software safety inhibits. SFMC-REQ-015 restricts weapon firing unconditionally, while SFMC-REQ-035 grants universal pilot override authority over automatic controls without defining if safety inhibits are included.
- **Recommendation:** Clarify SFMC-REQ-035 to explicitly bound pilot override to flight navigation controls and specify that safety inhibits, such as friendly fire blocks, cannot be overridden.

**SRS evidence:**

- **§3.3, SFMC-REQ-015:** "The SFMC shall never permit the pilot to fire a weapon at a friendly spacecraft."
- **§4, SFMC-REQ-035:** "The pilot shall always be able to override automatic spacecraft controls."

**NASA references:**

- [NPR-7150.2D | SWE-184 | §4.1.4](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter4)
- [NPR-7150.2D | SWE-054 | §4.1.6](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter4)

### REL-002

- **Requirements:** SFMC-REQ-002, SFMC-REQ-038
- **Status:** NO_CONFIRMED_CONFLICT
- **Issue code:** NONE
- **Explanation:** Different numeric minimums are not a conflict because updating displayed flight information at 10 Hz (every 100 milliseconds) fulfills both the general display update constraint and the 500 millisecond position display requirement.
- **Recommendation:** No requirement change is needed to resolve a conflict. Optionally, harmonize display timing references across sections for clarity.

**SRS evidence:**

- **§3.1, SFMC-REQ-002:** "The SFMC shall update the displayed spacecraft position at least once every 500 milliseconds"
- **§5, SFMC-REQ-038:** "the SFMC shall update flight information displayed to the pilot at least 10 times per second."

**NASA references:**

- [NPR-7150.2D | SWE-054 | §4.1.6](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter4)
- [NASA-HDBK-2203-5.09 | §3.2.2.1](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### REL-003

- **Requirements:** SFMC-REQ-033, SFMC-REQ-034
- **Status:** NO_CONFIRMED_CONFLICT
- **Issue code:** NONE
- **Explanation:** The requirements work together without contradiction: SFMC-REQ-033 provides the destination selection logic, while SFMC-REQ-034 provides the automated piloting capability to execute transit to that location.
- **Recommendation:** Maintain both requirements as complementary elements of Emergency mode functionality.

**SRS evidence:**

- **§4, SFMC-REQ-033:** "the SFMC shall automatically determine the safest destination."
- **§4, SFMC-REQ-034:** "The SFMC shall be capable of automatically flying the spacecraft to a safe location during an emergency."

**NASA references:**

- [NPR-7150.2D | SWE-054 | §4.1.6](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter4)
- [NASA-HDBK-2203-5.09 | §3.2.1.5](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

## Document Findings

### DOC-001: TRACEABILITY

- **Status:** PARTIAL
- **Issue code:** INCOMPLETE_TRACEABILITY
- **Searched scope:** SRS §10
- **Explanation:** Section 10 identifies high-level mission needs but lacks mapping between the software requirements and these parent needs.
- **Recommendation:** Develop and include a complete bidirectional requirement-to-mission-need traceability matrix linking each software requirement to its parent mission need.

**SRS evidence:**

- **§10:** "A complete requirement-to-mission-need traceability matrix has not yet been developed."

**NASA references:**

- [NPR-7150.2D | SWE-052 | §3.12.1](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter3)
- [NASA-HDBK-2203-5.09 | §3.8](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### DOC-002: QUALIFICATION_PROVISIONS

- **Status:** MISSING
- **Issue code:** MISSING_QUALIFICATION_PROVISIONS
- **Searched scope:** FULL
- **Explanation:** The SRS contains no section specifying qualification provisions or verification methods for the defined software requirements.
- **Recommendation:** Add a Qualification Provisions section specifying the verification method (testing, analysis, inspection, or demonstration) for each software requirement.

**SRS evidence:**


**NASA references:**

- [NASA-HDBK-2203-5.09 | §1.c](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NASA-HDBK-2203-5.09 | §3.3](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### DOC-003: ACCEPTANCE_CRITERIA

- **Status:** PARTIAL
- **Issue code:** MISSING_ACCEPTANCE_CRITERIA
- **Searched scope:** SRS §§3–9
- **Explanation:** Several requirement statements rely on ambiguous, non-measurable language instead of quantitative acceptance criteria.
- **Recommendation:** Replace subjective terms with clear, quantitative, and testable acceptance criteria across requirements in sections 3 through 9.

**SRS evidence:**

- **§3.1, SFMC-REQ-006:** "reasonably close"
- **§3.3, SFMC-REQ-016:** "extremely accurate"
- **§5, SFMC-REQ-037:** "without noticeable delay"

**NASA references:**

- [NPR-7150.2D | SWE-050 | §4.1.2](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter4)
- [NASA-HDBK-2203-5.09 | §3.7](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

### DOC-004: REQUIREMENT_IDENTIFIERS

- **Status:** PARTIAL
- **Issue code:** UNNUMBERED_REQUIREMENTS
- **Searched scope:** SRS §2.1
- **Explanation:** Section 2.1 includes normative requirements containing 'shall' that lack requirement tags/identifiers.
- **Recommendation:** Assign unique requirement identifiers to all normative 'shall' statements in section 2.1 or rephrase them as non-normative context.

**SRS evidence:**

- **§2.1:** "The SFMC shall receive pilot commands from the cockpit controls."
- **§2.1:** "The SFMC shall display spacecraft status information on the pilot's primary display."

**NASA references:**

- [NASA-HDBK-2203-5.09 | §1.b](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NPR-7150.2D | SWE-050 | §4.1.2](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter4)

### DOC-005: SAFETY_DEFINITIONS

- **Status:** PARTIAL
- **Issue code:** INCOMPLETE_SAFETY_DEFINITIONS
- **Searched scope:** SRS §§3.3,4,11
- **Explanation:** Key terms governing safety-critical functions (e.g., friendly spacecraft target interlocks and emergency safe locations) are not defined in the requirements and are documented as open items.
- **Recommendation:** Resolve open items to explicitly define safety-critical terms and logic relied upon by safety requirements.

**SRS evidence:**

- **§3.3, SFMC-REQ-015:** "friendly spacecraft"
- **§11, Open Item 5:** "Definition of a safe location during an emergency."
- **§11, Open Item 10:** "Criteria for determining whether a detected spacecraft is friendly or hostile."

**NASA references:**

- [NASA-HDBK-2203-5.09 | §3.2.1.4](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
- [NPR-7150.2D | SWE-184 | §4.1.4](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter4)

## SWE Coverage

### SWE-050

- **Document evidence:** PARTIAL_EVIDENCE
- **Project compliance:** NOT_DETERMINED
- **Rationale:** Software requirements are established and recorded within the SRS document. However, requirements for COTS, GOTS, MOTS, OSS, or reused software components are completely absent, and formal approval/maintenance records reside outside the document.

- **Supported by requirements:** None

**SRS evidence:**

- **§1.1, Purpose:** "This Software Requirements Specification defines the software requirements for the Starhawk Space Fighter Mission Computer (SFMC)."

**External evidence needed:**

- Software Development Plan (SDP)
- Software Configuration Management Plan
- Change Control Board (CCB) approval records and signature sheets
- COTS/GOTS/MOTS/OSS trade studies and software reuse evaluation records

**NASA reference:**

- [NPR-7150.2D | SWE-050 | §4.1.2](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter4)

### SWE-051

- **Document evidence:** PARTIAL_EVIDENCE
- **Project compliance:** NOT_DETERMINED
- **Rationale:** High-level mission needs are mapped in Section 10, but the document explicitly states that a complete requirement-to-mission-need traceability matrix has not yet been developed and leaves key parameters unresolved in Section 11.

- **Supported by requirements:** None

**SRS evidence:**

- **§10, Requirement Traceability:** "A complete requirement-to-mission-need traceability matrix has not yet been developed."

**External evidence needed:**

- Top-level Systems Engineering Requirements Specification
- System and Software Safety Analysis Reports (e.g., Hazard Analysis)
- Hardware Interface Control Documents (ICDs) and Specifications
- Software Requirements Analysis and Trade Study reports

**NASA reference:**

- [NPR-7150.2D | SWE-051 | §4.1.3](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter4)

### SWE-184

- **Document evidence:** DOCUMENTED
- **Project compliance:** NOT_DETERMINED
- **Rationale:** Software-related safety constraints and controls are explicitly documented in the SRS, including restrictions on firing at friendly spacecraft, automated threat countermeasures, and pilot command override capabilities.

- **Supported by requirements:** SFMC-REQ-015, SFMC-REQ-035

**SRS evidence:**

- **§3.3, SFMC-REQ-015:** "The SFMC shall never permit the pilot to fire a weapon at a friendly spacecraft."
- **§4, SFMC-REQ-035:** "The pilot shall always be able to override automatic spacecraft controls."

**External evidence needed:**

- System Hazard Analysis (SHA) and System Safety Plan
- Software System Safety Technical Report
- Hazard Tracking System logs showing hazard mitigation mapping to SRS requirements

**NASA reference:**

- [NPR-7150.2D | SWE-184 | §4.1.4](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter4)

### SWE-053

- **Document evidence:** NOT_ASSESSABLE
- **Project compliance:** NOT_DETERMINED
- **Rationale:** The requirement mandates a management process for tracking and managing changes over time, which cannot be assessed from the contents of the SRS itself.

- **Supported by requirements:** None

**SRS evidence:**


**External evidence needed:**

- Software Configuration Management Plan
- Change Control Board (CCB) meeting minutes
- Software Change Requests (SCRs) and Change Request tracking repository
- Version control repository commit logs and baseline history

**NASA reference:**

- [NPR-7150.2D | SWE-053 | §4.1.5](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter4)

### SWE-054

- **Document evidence:** NOT_ASSESSABLE
- **Project compliance:** NOT_DETERMINED
- **Rationale:** Tracking inconsistencies among requirements, plans, and products to closure is a management process. The SRS lists unresolved items but cannot demonstrate process closure.

- **Supported by requirements:** None

**SRS evidence:**

- **§11, Open Items:** "The following items remain to be resolved during development:"

**External evidence needed:**

- Corrective Action Tracking System / Discrepancy Reports
- Software Quality Assurance (SQA) audit reports and inconsistency logs
- Requirements Verification Matrix
- CCB action item logs and closure records

**NASA reference:**

- [NPR-7150.2D | SWE-054 | §4.1.6](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter4)

### SWE-055

- **Document evidence:** NOT_ASSESSABLE
- **Project compliance:** NOT_DETERMINED
- **Rationale:** Requirements validation is a project process involving customer reviews, simulations, or operational evaluations that cannot be proven by the static text of an SRS.

- **Supported by requirements:** None

**SRS evidence:**


**External evidence needed:**

- Software Validation Plan
- Requirements Validation Review (RVR) reports and stakeholder sign-offs
- Operational Concept Document (OpsCon) validation feedback
- User-in-the-loop simulation and prototype test reports

**NASA reference:**

- [NPR-7150.2D | SWE-055 | §4.1.7](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter4)
