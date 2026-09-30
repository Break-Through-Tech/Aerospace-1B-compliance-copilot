import pandas as pd
from pathlib import Path


# ------------------------------------------------------------
# Paths
# ------------------------------------------------------------

ROOT = Path(__file__).resolve().parents[1]

CLAUSES_FILE = ROOT / "data" / "clauses.json"
ANNOTATIONS_FILE = ROOT / "data" / "clause_annotations.csv"


# ------------------------------------------------------------
# Load data
# ------------------------------------------------------------

clauses = pd.read_json(CLAUSES_FILE)
annotations = pd.read_csv(ANNOTATIONS_FILE)


# ------------------------------------------------------------
# Validate required columns
# ------------------------------------------------------------

required_clause_columns = {
    "chunk_id",
    "swe_id",
    "section",
    "text",
    "source",
    "source_url",
    "type",
}

required_annotation_columns = required_clause_columns | {
    "applies_to",
    "interpretation",
}

missing_clause_columns = required_clause_columns - set(clauses.columns)
missing_annotation_columns = required_annotation_columns - set(annotations.columns)

if missing_clause_columns:
    raise ValueError(
        f"clauses.json is missing columns: {missing_clause_columns}"
    )

if missing_annotation_columns:
    raise ValueError(
        f"clause_annotations.csv is missing columns: "
        f"{missing_annotation_columns}"
    )


# ------------------------------------------------------------
# Validate chunk IDs
# ------------------------------------------------------------

if clauses["chunk_id"].duplicated().any():
    raise ValueError("Duplicate chunk_id values found in clauses.json")

if annotations["chunk_id"].duplicated().any():
    raise ValueError(
        "Duplicate chunk_id values found in clause_annotations.csv"
    )

clause_ids = set(clauses["chunk_id"])
annotation_ids = set(annotations["chunk_id"])

missing_annotations = clause_ids - annotation_ids
extra_annotations = annotation_ids - clause_ids

if missing_annotations:
    raise ValueError(
        f"{len(missing_annotations)} clauses do not have annotations:\n"
        f"{sorted(missing_annotations)}"
    )

if extra_annotations:
    raise ValueError(
        f"{len(extra_annotations)} annotations refer to clauses "
        f"that no longer exist:\n{sorted(extra_annotations)}"
    )


# ------------------------------------------------------------
# Validate annotation labels
# ------------------------------------------------------------

valid_labels = {
    "INDIVIDUAL",
    "SET/SRS",
    "PROCESS",
    "MULTIPLE",
}

unexpected_labels = (
    set(annotations["applies_to"].dropna()) - valid_labels
)

if unexpected_labels:
    raise ValueError(
        f"Unexpected applies_to labels: {unexpected_labels}"
    )

if annotations["applies_to"].isna().any():
    raise ValueError("Some clauses are missing applies_to labels.")

if annotations["interpretation"].isna().any():
    raise ValueError("Some clauses are missing interpretations.")


# ------------------------------------------------------------
# Rebuild metadata from clauses.json using chunk_id
# ------------------------------------------------------------

labels = annotations[
    ["chunk_id", "applies_to", "interpretation"]
].copy()

rebuilt = clauses.merge(
    labels,
    on="chunk_id",
    how="left",
    validate="one_to_one",
)

if rebuilt["applies_to"].isna().any():
    raise ValueError(
        "Some clauses lost annotations during the chunk_id merge."
    )


# ------------------------------------------------------------
# Save normalized annotation table
# ------------------------------------------------------------

rebuilt.to_csv(ANNOTATIONS_FILE, index=False)


# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------

print(f"Validated and saved {len(rebuilt)} annotated clauses.")
print(f"Output: {ANNOTATIONS_FILE}")

print("\nLabel counts:")
print(rebuilt["applies_to"].value_counts())

print("\nBreakdown by clause type:")
print(pd.crosstab(rebuilt["type"], rebuilt["applies_to"]))