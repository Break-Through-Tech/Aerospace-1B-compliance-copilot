3.6 Software Assurance and Software Independent Verification
& Validation

3.6.1 The project manager shall plan and implement software assurance, software safety, and IV&V
(if required) per NASA-STD-8739.8, Software Assurance and Software Safety Standard.
[SWE-022]

Note: Software assurance activities occur throughout the life of the project. Some of the
actual analyses and activities may be performed by engineering or the project. Software
Assurance directions, requirements, and guidance can be found in the NASA-STD-8739.8.


3.6.2 For projects reaching Key Decision Point A, the program manager shall ensure that software
IV&V is performed on the following categories of projects: [SWE-141]
a. Category 1 projects as defined in NPR 7120.5.
b. Category 2 projects as defined in NPR 7120.5, that have Class A or Class B payload risk
classification per NPR 8705.4, Risk Classification for NASA Payloads.
c. Projects selected explicitly by the Mission Directorate Associate Administrator (MDAA) to have
software IV&V.


3.6.3 If software IV&V is required for a project, the project manager, in consultation with NASA
IV&V, shall ensure an IPEP is developed, approved, maintained, and executed in accordance with
IV&V requirements in NASA-STD-8739.8. [SWE-131]
Note: The IV&V Advisory Board will review the scope of NASA IV&V activities on an
annual basis as part of the budget planning process.


3.6.4 If software IV&V is performed on a project, the project manager shall ensure that IV&V is
provided access to development artifacts, products, source code, and data required to perform the
IV&V analysis efficiently and effectively. [SWE-178]


3.6.5 If software IV&V is performed on a project, the project manager shall provide responses to IV&V submitted issues and risks and track these issues and risks to closure. [SWE-179] 



3.7 Safety-Critical Software

3.7.1 The project manager, in conjunction with the SMA organization, shall determine if each
software component is considered to be safety-critical per the criteria defined in
NASA-STD-8739.8. [SWE-205]


3.7.2 If a project has safety-critical software, the project manager shall implement the safety-critical
software requirements contained in NASA-STD-8739.8. [SWE-023]

3.7.3 If a project has safety-critical software or mission-critical software, the project manager shall
implement the following items in the software: [SWE-134]
a. The software is initialized, at first start and restarts, to a known safe state.
b. The software safely transitions between all predefined known states.
c. Termination performed by software functions is performed to a known safe state.
d. Operator overrides of software functions require at least two independent actions by an operator.
e. Software rejects commands received out of sequence when execution of those commands out of
sequence can cause a hazard.
f. The software detects inadvertent memory modification and recovers to a known safe state.
g. The software performs integrity checks on inputs and outputs to/from the software system.
h. The software performs prerequisite checks prior to the execution of safety-critical software
commands.
i. No single software event or action is allowed to initiate an identified hazard.
j. The software responds to an off-nominal condition within the time needed to prevent a hazardous
event.
k. The software provides error handling.
l. The software can place the system into a safe state.
Note: These requirements apply to components that reside in a mission-critical or
safety-critical system, and the components control, mitigate, or contribute to a hazard as
well as software used to command hazardous operations/activities.

3.7.4 If a project has safety-critical software, the project manager shall ensure that there is 100 percent code test coverage using the Modified Condition/Decision Coverage (MC/DC) criterion for rall identified safety-critical software components. [SWE-219]

3.7.5 If a project has safety-critical software, the project manager shall ensure all identified safety-critical software components have a cyclomatic complexity value of 15 or lower. Any exceedance shall be reviewed and waived with rationale by the project manager or technical approval authority. [SWE-220] 


3.10 Software Reuse
3.10.1 The project manager shall specify reusability requirements that apply to its software
development activities to enable future reuse of the software, including the models, simulations, and
associated data used as inputs for auto-generation of software, for U.S. Government purposes.
[SWE-147]


3.10.2 The project manager shall evaluate software for potential reuse by other projects across
NASA and contribute reuse candidates to the appropriate NASA internal sharing and reuse software
system. However, if the project manager is not a civil servant, then a civil servant will pre-approve
all such software contributions; all software contributions should include, at a minimum, the
following information: [SWE-148]
a. Software Title.
b. Software Description.
c. The Civil Servant Software Technical POC for the software product.
d. The language or languages used to develop the software.
e. Any third-party code contained therein, and the record of the requisite license or permission
received from the third party permitting the Government’s use and any required markings (e.g.,
required copyright, author, applicable license notices within the software code, and the source of
each third-party software component (e.g., software URL & license URL)), if applicable.
f. Release notes.


3.10.3 In accordance with NPD 2091.1, Inventions Made by Government Employees, NASA Civil
Servant employees who make an invention embodied by software will submit to NASA a disclosure
of such invention. Likewise, such inventions made by NASA contractors will be reported to NASA,

3.11 Software Cybersecurity


3.11.1 Software defects are a central and critical aspect of computer security vulnerabilities.
Software defects with cybersecurity ramifications include implementation bugs such as buffer
overflows and design flaws such as inconsistent error handling.


3.11.2 The project manager shall perform a software cybersecurity assessment on the software
components per the Agency security policies and the project requirements, including risks posed by
the use of COTS, GOTS, MOTS, OSS, or reused software components. [SWE-156]


3.11.3 The project manager shall identify cybersecurity risks, along with their mitigations, in flight
and ground software systems and plan the mitigations for these systems. [SWE-154]

3.11.4 The project manager shall implement protections for software systems with communications
capabilities against unauthorized access per the requirements contained in the NASA-STD-1006,
Space System Protection Standard. [SWE-157]


3.11.5 The project manager shall test the software and record test results for the required software
cybersecurity mitigation implementations identified from the security vulnerabilities and security
weaknesses analysis. [SWE-159]

3.11.6 The project manager shall identify, record, and implement secure coding practices.
[SWE-207]
3.11.7 The project manager shall verify that the software code meets the project’s secure coding
standard by using the results from static analysis tool(s). [SWE-185]

3.11.8 The project manager shall identify software requirements for the collection, reporting, and
storage of data relating to the detection of adversarial actions. [SWE-210]

3.11.8 The project manager shall identify software requirements for the collection, reporting, and
storage of data relating to the detection of adversarial actions. [SWE-210]

3.12 Software Bi-Directional Traceability

3.12.1 The project manager shall perform, record, and maintain bi-directional traceability between
the following software elements: [SWE-052]

Table 1. Bi-directional traceability by software classification
Bi-directional Traceability Class A, B,
and C Class D Class F
Higher-level requirements to the software requirements X X
Software requirements to the system hazards X X
Software requirements to the software design components X
Software design components to the software code X
Software requirements to the software verification(s) X X X
Software requirements to the software non-conformances X X X


Chapter 4: Software Engineering Life Cycle
Requirements

4.1 Software Requirements

4.1.2 The project manager shall establish, capture, record, approve, and maintain software
requirements, including requirements for COTS, GOTS, MOTS, OSS, or reused software
components, as part of the technical specification. [SWE-050]

4.1.3 The project manager shall perform software requirements analysis based on flowed-down and
derived requirements from the top-level systems engineering requirements, safety and reliability
analyses, and the hardware specifications and design. [SWE-051]

4.1.4 The project manager shall include software related safety constraints, controls, mitigations, and
assumptions between the hardware, operator, and software in the software requirements
documentation. [SWE-184]

4.1.5 The project manager shall track and manage changes to the software requirements. [SWE-053]

4.1.6 The project manager shall identify, initiate corrective actions, and track until closure
inconsistencies among requirements, project plans, and software products. [SWE-054]

4.1.7 The project manager shall perform requirements validation to ensure that the software will
perform as intended in the customer environment. [SWE-055]

4.2 Software Architecture

4.2.1 Experience confirms that the quality and longevity of a software-reliant system is primarily
determined by its architecture. The software architecture underpins a system’s software design and
code; it represents the earliest design decisions, ones that are difficult and costly to change later. The
transformation of the derived and allocated requirements into the software architecture results in the
basis for all software development work.


4.2.2 A software architecture:
a. Formalizes precise subsystem decompositions.
b. Defines and formalizes the dependencies among software work products within the integrated
system.
c. Serves as the basis for evaluating the impacts of proposed changes.
d. Maintains rules for use by subsequent software engineers that ensure a consistent software system
as the work products evolve.
e. Provides a stable structure for use by future groups through the documentation of the architecture,
its views and patterns, and its rules.
f. Follows guidelines created by the NASA Space Asset and the Enterprise Protection Program to
protect mission architectures.
g. Documents the valid and invalid modes or states of operation within the software requirements.


4.2.3 The project manager shall transform the requirements for the software into a recorded software
architecture. [SWE-057]
