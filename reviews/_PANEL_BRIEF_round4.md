# PANEL BRIEF — Round 4 (editor: acting handling editor, Journal of Pain Research)

**Manuscript under review:** `manuscript/manuscript_v1.1.8.md` (+ `.docx`)
**Venue:** Journal of Pain Research (Dove Press), Original Research — bioinformatics reanalysis of public GEO data, single author (anesthesiologist, B.M. only — do NOT flag the missing MD/PhD; deliberate and correct).

**Provenance of this version:** v1.1.8 was accepted at Round 3 on content grounds and then underwent a **language-only "de-AI" revision** (removal of em-dashes and machine-writing vocabulary). No number, citation, or claim was intended to change, and programmatic checks confirmed the numeric sets are identical to the accepted v1.1.7. **Round 4 exists because a language-only revision is exactly where silent semantic damage hides.** The panel's job is to verify the polish and give the manuscript a fresh pair of eyes before final submission packaging.

**What the study is:** A prospectively specified secondary reanalysis of GSE342782 (bulk RNA-seq of the HD10.6 human sensory-neuron line; direct VZV infection vs mock; 36-h serum-exosome exposure from control/HZ/PHN donors), scoring frozen mechanotransduction modules (M1–M4), an electrochemical nociceptor module (E1) and neutral controls (N1–N3), with a single pre-specified primary endpoint (M3, HZ-exo vs control-exo) and exact label-permutation inference.

---

## Reviewer assignments

| Reviewer | Mandate | Must read |
|---|---|---|
| **C1 — semantic drift auditor** | Prove or disprove that the de-AI revision changed any meaning | `manuscript/manuscript_v1.1.8.md` **and** `manuscript/archive/manuscript_v1.1.7.md` (the only reviewer permitted to read the archive) |
| **C2 — domain expert (mechanotransduction/PHN)** | Fresh-eyes scientific review of the accepted text | v1.1.8 only |
| **C3 — statistics auditor** | Independent recomputation and deposit cross-check | v1.1.8 + raw counts + `analysis/results/layer1/` |
| **C4 — language & venue compliance** | Post-polish prose quality, AMA/Dove style, submission checklist | v1.1.8 only |

## Independence discipline

- C2, C3, C4 review the manuscript **as if a first submission**: do not read prior review reports (`REVIEW_*`, `A*`, `B*`), release notes, memory, or the archive. Judge the text on its own merits.
- C1's mandate **requires** the two-version comparison; C1 must not read other reviewers' outputs before filing.
- Each reviewer writes only their assigned file. No reviewer may soften a finding because a prior round "already accepted" the text.

## Environment notes

- Shell is Git Bash on Windows; workspace root `D:/2026.10/机械应力/`.
- Python with pandas/numpy/scipy: **`C:/Python314/python.exe`** (bare `python` lacks pandas).
- Raw inputs: `analysis/data/raw/GSE342782_Processed_DirectInf_neuronHD10s_BulkSeq_Counts.csv.gz` (comma-separated; 6 mockInf* + 6 vzvInf*), `analysis/data/raw/GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz` (7 C*, 7 S*, 5 P*).
- Deposits: `analysis/results/layer1/*.json|csv`; shipped editor verifier `analysis/verify_round2/verify_round2.py` (114 checks, exits non-zero on failure).
- Long paragraphs are single lines in the `.md`; use `sed -n 'Np' file | fold -s -w 200`.
