import pandas as pd
from pathlib import Path


# ------------------------------------------------------------
# Paths
# ------------------------------------------------------------

ROOT = Path(__file__).resolve().parents[1]

INPUT_FILE = ROOT / "data" / "clauses.json"
OUTPUT_FILE = ROOT / "docs" / "clause_annotations.csv"


# ------------------------------------------------------------
# Load clauses
# ------------------------------------------------------------

df = pd.read_json(INPUT_FILE)

annotations = df[
    ["swe_id", "section", "text", "source", "source_url", "type"]
].copy()

annotations["applies_to"] = ""
annotations["interpretation"] = ""


def apply_many(indices, label, interpretation):
    annotations.loc[indices, "applies_to"] = label
    annotations.loc[indices, "interpretation"] = interpretation


def apply_one(index, label, interpretation):
    annotations.loc[index, "applies_to"] = label
    annotations.loc[index, "interpretation"] = interpretation


# ============================================================
# REQUIREMENTS
# ============================================================

apply_many(
    [24, 25, 27, 28, 29, 30, 32, 33, 34, 35,
     36, 37, 43, 45, 46, 48, 49, 50, 51, 53],
    "PROCESS",
    "Organizational or software engineering governance activity that cannot be evaluated from the contents of an SRS alone."
)

apply_many(
    [54, 55, 57, 58, 59, 60, 70, 73, 83, 84,
     86, 88, 91, 92, 93, 95, 96, 97, 98, 100],
    "PROCESS",
    "Project, organizational, governance, planning, or software-management activity that cannot be evaluated from the contents of an SRS alone."
)

apply_many(
    [102, 105, 107, 108, 110, 111, 112, 113, 114,
     116, 118, 120, 122, 123, 125, 127, 128, 129],
    "PROCESS",
    "Project planning, management, assurance, classification, verification, or lifecycle activity that cannot be established from the contents of an SRS alone."
)

apply_one(
    130,
    "MULTIPLE",
    "Requires implementation of safety-critical software behaviors, but an SRS can also be checked for whether corresponding safety requirements are documented."
)

apply_many(
    [101, 132, 134, 136, 137, 140, 143, 148, 149,
     151, 152, 154, 155, 159, 171, 173, 175, 177],
    "PROCESS",
    "Project, implementation, verification, architecture, design, security, or lifecycle activity that cannot be established from the contents of an SRS alone."
)

apply_one(
    142,
    "SET/SRS",
    "Can be checked at the document level by determining whether the SRS specifies applicable reusability requirements."
)

apply_one(
    157,
    "SET/SRS",
    "Can be checked at the SRS level by determining whether requirements exist for collecting, reporting, and storing data related to adversarial actions."
)

apply_many(
    [178, 179, 181, 184, 185, 186, 189, 190, 192,
     194, 195, 197, 198, 200, 202, 204, 205, 206,
     208, 210],
    "PROCESS",
    "Implementation, coding, testing, verification, configuration management, operations, or maintenance activity that cannot be evaluated from the contents of an SRS alone."
)

apply_many(
    [211, 212, 213, 214, 216, 217, 218, 220, 222,
     223, 224, 225, 226, 229, 231, 232, 234, 236,
     237, 238],
    "PROCESS",
    "Delivery, maintenance, configuration management, risk management, review, measurement, or monitoring activity that cannot be evaluated from the contents of an SRS alone."
)

apply_many(
    [240, 241, 242, 244, 246],
    "PROCESS",
    "Requirements management, defect tracking, non-conformance assessment, or process-control activity that cannot be evaluated from the contents of an SRS alone."
)

# Section 4.1 requirements

apply_one(
    162,
    "PROCESS",
    "Governs whether the project has a requirements-management practice at all. An SRS alone cannot demonstrate approval or maintenance."
)

apply_one(
    164,
    "PROCESS",
    "Concerns the requirements-analysis activity, not just wording in the SRS."
)

apply_one(
    165,
    "MULTIPLE",
    "Partly process-level safety analysis, but inclusion of safety constraints in the SRS is document-checkable."
)

apply_one(
    166,
    "PROCESS",
    "Pure change-control activity; an SRS alone cannot show that requirements changes are tracked and managed."
)

apply_one(
    167,
    "MULTIPLE",
    "Requirement inconsistencies may be detectable in the SRS, but corrective-action tracking is process-level."
)

apply_one(
    168,
    "PROCESS",
    "Validation requires stakeholder and operational-environment activity, so it cannot be judged from SRS text alone."
)


# ============================================================
# SWEHB GUIDANCE
# ============================================================

guidance = {
    249: ("SET/SRS", "Defines minimum document-level content expected across the SRS."),
    250: ("SET/SRS", "Defines required introductory content for the SRS as a whole."),
    251: ("MULTIPLE", "Combines individual requirement quality checks with document-level coverage of required requirement categories."),
    252: ("SET/SRS", "Checks whether the SRS defines how requirements will be verified and validated using qualification methods."),
    253: ("MULTIPLE", "Rationale can be checked per requirement, while document-wide absence of rationale is an SRS-level issue."),
    254: ("SET/SRS", "Addresses completeness and allowable representation of the SRS as a document."),
    255: ("SET/SRS", "Describes the role and value of the SRS as a whole."),
    256: ("SET/SRS", "Describes document-level purposes and benefits of maintaining a complete SRS."),
    257: ("MULTIPLE", "Combines document-structure guidance with lifecycle and requirements-management process guidance."),
    258: ("SET/SRS", "Defines the expected purpose of the SRS introduction section."),
    259: ("SET/SRS", "Checks whether the SRS includes an adequate purpose and audience description."),
    260: ("SET/SRS", "Checks whether the SRS adequately defines system scope, goals, functions, and limitations."),
    261: ("SET/SRS", "Checks whether the SRS contains an adequate system overview and supporting context."),
    262: ("MULTIPLE", "Combines individual requirement quality criteria with document-level organization, coverage, and completeness."),
    263: ("MULTIPLE", "Contains both per-requirement quality criteria and set-level guidance such as completeness and prioritization."),
    264: ("MULTIPLE", "Combines requirements-analysis activities with document-level capture of functional, decomposed, and derived requirements."),
    265: ("MULTIPLE", "Applies to individual decomposed requirements and their relationships to parent requirements."),
    266: ("MULTIPLE", "Applies to individual derived requirements, traceability, rationale, and the process used to derive them."),
    267: ("MULTIPLE", "Describes relationships and traceability across multiple requirement types and levels."),
    268: ("MULTIPLE", "Combines traceability and stakeholder-validation process guidance with individual requirement quality criteria."),
    269: ("MULTIPLE", "Requires document-wide state/mode coverage and correlation while also constraining individual requirements."),
    270: ("MULTIPLE", "Combines document-level coverage of data requirements with detailed properties of individual data requirements."),
    271: ("MULTIPLE", "Requires safety requirements to exist in the SRS and also be individually designated as safety requirements."),
    272: ("PROCESS", "Requires implementation of safety-critical software behaviors and cannot be demonstrated from an SRS alone."),
    273: ("MULTIPLE", "Defines a safety-critical software behavior that may be specified in an SRS, but actual implementation cannot be proven from the SRS alone."),

    284: ("MULTIPLE", "Combines individual safety requirements, document-level safety coverage and traceability, and implementation-oriented safety guidance."),
    285: ("MULTIPLE", "Combines individual control-system requirement quality with document-level coverage, traceability, and implementation guidance."),
    286: ("MULTIPLE", "Combines individual algorithm requirement quality with traceability, completeness, and implementation guidance."),
    287: ("MULTIPLE", "Combines individual I/O requirement properties with document-level coverage and implementation-oriented validation guidance."),
    288: ("MULTIPLE", "Combines individual security and privacy requirements with document-level coverage and security engineering practices."),
    289: ("MULTIPLE", "Combines individual fault-management requirements with system-wide coverage, traceability, and engineering activities."),
    290: ("MULTIPLE", "Combines individual operating-system requirements with document-level platform coverage and implementation constraints."),
    291: ("MULTIPLE", "Combines individual BSP requirements with document-level coverage and implementation and testing activities."),
    292: ("MULTIPLE", "Combines individual partitioning requirements with document-level isolation coverage and implementation guidance."),
    293: ("MULTIPLE", "Combines individual fault-tolerance requirements with system-wide coverage and engineering activities such as FMEA and common-cause analysis."),

    294: ("MULTIPLE", "Combines document-level coverage of non-functional requirement categories with individual requirements that should be measurable, testable, and traceable."),
    295: ("MULTIPLE", "Combines document-level performance and timing coverage with measurable properties of individual requirements."),
    296: ("MULTIPLE", "Combines document-level quality attribute coverage with measurable individual quality requirements."),
    297: ("MULTIPLE", "Combines document-level coverage of design constraints with individual constraint requirements."),
    298: ("MULTIPLE", "Combines document-level hardware resource coverage with measurable individual resource-utilization requirements."),
    299: ("INDIVIDUAL", "Provides examples of measurable individual hardware and resource-utilization requirements."),
    300: ("MULTIPLE", "Combines document-level interface coverage with detailed properties of individual interface requirements and interface-management practices."),
    301: ("MULTIPLE", "Combines coverage of external interfaces with detailed properties that individual external-interface requirements should specify."),
    302: ("MULTIPLE", "Combines document-level internal-interface coverage with detailed properties of individual interface requirements."),
    303: ("MULTIPLE", "Combines overall user-interface coverage with detailed properties and quality expectations for individual UI requirements."),
    304: ("MULTIPLE", "Combines system-interface coverage with detailed requirements for individual system interactions."),
    305: ("MULTIPLE", "Combines hardware-interface coverage with detailed characteristics of individual hardware-interface requirements."),
    306: ("MULTIPLE", "Combines communication-interface coverage with detailed protocol, timing, security, and error-handling requirements."),
    307: ("MULTIPLE", "Combines service-interface coverage with detailed properties of individual service-interface requirements."),
    308: ("MULTIPLE", "Combines individual user-requirement quality criteria with document-level coverage and user-engagement activities."),
    309: ("INDIVIDUAL", "Provides examples of individual user requirements and user stories."),
    310: ("MULTIPLE", "Requires verification methods for individual requirements while also requiring document-level qualification and traceability information."),
    311: ("MULTIPLE", "Rationale can be checked for individual requirements while absence of rationale across the SRS is a document-level issue."),
    312: ("SET/SRS", "Checks whether the SRS as a whole captures other necessary requirements, references, use cases, terminology, and supporting information."),
    313: ("MULTIPLE", "Combines document-level recording of assumptions and limitations with stakeholder clarification and later validation activities."),

    314: ("MULTIPLE", "Combines individual requirement quality guidance, document-level consistency and traceability, and collaborative requirements-management practices."),
    315: ("MULTIPLE", "Traceability can be checked for individual requirements, but maintaining bidirectional traceability is also a requirements-management process."),
    316: ("MULTIPLE", "Combines SRS structure, individual requirement fields, traceability, tooling, automation, and requirements-management practices for small projects."),
    317: ("INDIVIDUAL", "Provides an example of a single measurable non-functional requirement with associated metadata."),
    318: ("MULTIPLE", "Combines document structure, individual requirement metadata, tooling, automation, visualization, and change-management guidance."),
    319: ("SET/SRS", "Provides reference material supporting the SRS and requirements guidance at the document level."),
    320: ("PROCESS", "Describes tools used to assess requirements quality rather than a property directly established from the SRS itself."),
    321: ("PROCESS", "Provides links to related requirements-engineering guidance and activities rather than a directly checkable SRS criterion."),
    322: ("PROCESS", "Provides process asset templates and checklists used during requirements development and review."),
    323: ("PROCESS", "References a requirements quality checklist used as part of the requirements review process."),
    324: ("PROCESS", "References a requirements contents checklist used during SRS review."),
    325: ("PROCESS", "Describes an editorial checklist used by analysts when reviewing software requirements."),
    326: ("PROCESS", "Provides Center process assets, templates, training, and guidance rather than a direct SRS-content criterion."),
    327: ("PROCESS", "Identifies the related software requirements lifecycle activity rather than a direct SRS-content criterion."),
    328: ("MULTIPLE", "Combines individual requirement clarity, document-level completeness and safety coverage, traceability, and verification and validation practices."),
    329: ("PROCESS", "Primarily concerns maintaining and updating requirements and traceability during an Agile development process."),
    330: ("MULTIPLE", "Combines individual requirement quality, whole-SRS completeness, traceability, assurance, verification, stakeholder review, and requirements-management processes.")
}

# 274-283 all use the same interpretation.
for i in range(274, 284):
    guidance[i] = (
        "MULTIPLE",
        "Defines a specific software behavior that can be represented in an individual SRS requirement, while actual implementation cannot be demonstrated from the SRS alone."
    )

for i, (label, interpretation) in guidance.items():
    apply_one(i, label, interpretation)


# ============================================================
# NOTES
# ============================================================

apply_many(
    [8, 26, 44, 47, 56, 63, 72, 74, 75, 81,
     87, 89, 94, 99, 103, 104, 106, 109, 115, 117],
    "PROCESS",
    "Provides additional context for project, governance, tailoring, planning, classification, acquisition, or lifecycle activities that cannot be evaluated from the contents of an SRS alone."
)

note_details = {
    121: ("PROCESS", "Describes software assurance activities performed throughout the project lifecycle."),
    124: ("PROCESS", "Describes IV&V planning and review activity."),
    126: ("PROCESS", "Provides guidance on delivering artifacts and project data for IV&V."),
    131: ("PROCESS", "Clarifies applicability of safety-critical implementation requirements."),
    133: ("PROCESS", "Explains MC/DC testing and waiver practices rather than an SRS-content criterion."),
    135: ("PROCESS", "Explains code-complexity measurement and assessment practices."),
    138: ("PROCESS", "Clarifies the meaning of electronic access to project data."),
    141: ("PROCESS", "Describes organizational appraisal, rating, evaluation, and risk-mitigation activities."),
    144: ("PROCESS", "Describes software reuse repository, approval, licensing, and release practices."),
    147: ("MULTIPLE", "Combines software quality characteristics such as well-defined interfaces with development and operational security practices."),
    150: ("PROCESS", "Describes security planning and threat-protection activities."),
    153: ("MULTIPLE", "Includes review and analysis activities, but also concerns security vulnerabilities in software requirements and design."),
    156: ("PROCESS", "Describes acceptable verification methods for secure coding compliance."),
    158: ("MULTIPLE", "Identifies observable security-related behaviors that may become requirements, while also describing monitoring and incident-analysis activities."),
    160: ("PROCESS", "Describes maintaining bidirectional traceability as a requirements-management process."),
    163: ("MULTIPLE", "Defines individual requirement quality characteristics such as clarity, measurability, completeness, verifiability, and traceability, while also describing the requirements-definition process."),
    172: ("PROCESS", "Describes the expected contents of a software architecture artifact rather than an SRS."),
    180: ("PROCESS", "Describes collecting and using software complexity metrics to manage development risk."),
    182: ("PROCESS", "Provides unit-testing guidance for safety-critical software."),
    183: ("PROCESS", "Provides unit-testing guidance for safety-critical software.")
}

for i, (label, interpretation) in note_details.items():
    apply_one(i, label, interpretation)

apply_many(
    [187, 191, 193, 196, 199, 201, 203, 207,
     219, 221, 227, 230, 235, 239, 243, 245],
    "PROCESS",
    "Provides additional guidance on testing, verification, configuration management, risk, measurement, review, or defect-management activities that cannot be evaluated from the contents of an SRS alone."
)


# ============================================================
# EXPLANATORY
# ============================================================

apply_many(
    [0, 1, 2, 3, 4, 5, 6, 7, 9, 10,
     11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "PROCESS",
    "Provides background, structure, applicability, governance, or lifecycle context for the NASA directive rather than a criterion that can be evaluated directly from an SRS."
)

apply_many(
    [21, 22, 23, 31, 38, 39, 40, 41, 42, 52,
     61, 62, 64, 65, 66, 67, 68, 69, 71, 76],
    "PROCESS",
    "Describes organizational roles, authority, tailoring governance, assurance, training, oversight, or lifecycle processes rather than a criterion that can be evaluated directly from an SRS."
)

apply_many(
    [77, 78, 79, 80, 82, 85, 90, 119, 139, 145,
     146, 161, 169, 174, 176, 188, 209, 215, 228],
    "PROCESS",
    "Provides background or context about tailoring, management, architecture, design, implementation, testing, maintenance, configuration management, or review processes rather than a criterion directly evaluable from an SRS."
)

apply_one(
    170,
    "MULTIPLE",
    "Primarily describes software architecture, but also states that valid and invalid modes or states of operation should be documented within the software requirements."
)

apply_one(
    233,
    "PROCESS",
    "Describes software measurement programs and process/product improvement activities rather than a criterion directly evaluable from an SRS."
)

apply_one(
    247,
    "PROCESS",
    "Describes the broader set of software engineering products and records used across the lifecycle rather than an SRS-specific check."
)

apply_one(
    248,
    "PROCESS",
    "Provides guidance on software engineering record content, templates, baselining, and updates rather than a criterion directly evaluable from an SRS."
)


# ============================================================
# VALIDATION
# ============================================================

if len(annotations) != 331:
    raise ValueError(
        f"Expected 331 clauses, but found {len(annotations)}."
    )

missing_labels = annotations["applies_to"].eq("").sum()
missing_interpretations = annotations["interpretation"].eq("").sum()

if missing_labels:
    raise ValueError(
        f"{missing_labels} clauses are missing applies_to labels."
    )

if missing_interpretations:
    raise ValueError(
        f"{missing_interpretations} clauses are missing interpretations."
    )

valid_labels = {"INDIVIDUAL", "SET/SRS", "PROCESS", "MULTIPLE"}

unexpected_labels = set(annotations["applies_to"]) - valid_labels

if unexpected_labels:
    raise ValueError(
        f"Unexpected applies_to labels found: {unexpected_labels}"
    )


# ------------------------------------------------------------
# Save results
# ------------------------------------------------------------

annotations.to_csv(OUTPUT_FILE, index=False)

print(f"Saved {len(annotations)} annotated clauses to:")
print(OUTPUT_FILE)

print("\nLabel counts:")
print(annotations["applies_to"].value_counts())

print("\nBreakdown by clause type:")
print(pd.crosstab(annotations["type"], annotations["applies_to"]))