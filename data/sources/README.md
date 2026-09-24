# Reference sources

The two documents `data/clauses.json` is built from. Treat these as read-only;
regenerate the corpus by running `notebooks/01_extract_clauses.ipynb`.

| File | Document | Authority | Origin | Retrieved |
|---|---|---|---|---|
| `N_PR_7150_002D_.pdf` | NPR 7150.2D, *NASA Software Engineering Requirements* (effective 2022-03-08) | **Mandatory** for NASA projects | [NODIS](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_) printable PDF | 2026-09-23 |
| `swehb_5.09_srs.html` | NASA Software Engineering Handbook (NASA-HDBK-2203, Ver D), topic 5.09 *SRS - Software Requirements Specification* | Recommended practice | [swehb.nasa.gov](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification) page HTML | 2026-09-24 |

## Why the Handbook is HTML, not PDF

Topic 5.09 is split across seven tabs (Minimum Recommended Content, Rationale,
Guidance, Small Projects, Resources, Lessons Learned, Software Assurance).
Printing the page to PDF captures only the tab that is open, so a printed copy
silently drops most of the page. The saved HTML contains all seven tab bodies.

To refresh the snapshot, call `fetch_swehb_snapshot()` in the notebook and
update the retrieval date above.
