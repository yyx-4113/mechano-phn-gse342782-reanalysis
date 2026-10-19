# PANEL BRIEF — Round 2 (editor: acting handling editor, Journal of Pain Research)

**Manuscript under review:** `manuscript/manuscript_v1.1.5.md` (+ `manuscript/manuscript_v1.1.5.docx`)
**Venue:** Journal of Pain Research (Dove Press), Original Research — bioinformatics reanalysis of public GEO data, single author (anesthesiologist, B.M. only — do NOT flag the missing MD/PhD; that is deliberate and correct).
**What the study is:** A prospectively specified secondary reanalysis of GSE342782 (bulk RNA-seq of HD10.6 human sensory-neuron line; direct VZV infection vs mock; 36-h serum-exosome exposure from control/HZ/PHN donors). It scores frozen mechanotransduction modules (M1–M4), an electrochemical nociceptor module (E1) and neutral controls (N1–N3), with a single pre-specified primary endpoint (M3, HZ-exo vs control-exo) and exact permutation inference.

---

## Independence discipline (mandatory)

You are reviewing this manuscript **as if it were a first submission**. You have no knowledge of any prior review, revision, or response letter, and you must not acquire any.

**Forbidden to read (do not open these files at all):**
- `reviews/REVIEW_*.md`, `reviews/_PANEL_BRIEF*.md`, `reviews/A[1-4]_*.md`, and any new `reviews/B*.md` / `REVIEW_*` files
- `release_notes_*.md`, `README.md`, `PROTOCOL_*.md`, `GITHUB_DEPOSIT_SOP.md`, `author_verification_statement.md`, `CITATION.cff`, root `MANIFEST.json`, `requirements.txt`
- `manuscript/archive/` (older manuscript versions — reading them contaminates the "first submission" frame)
- Any file under `.workbuddy/` (memory, notes)
- Other reviewers' outputs in `reviews/` — you may write ONLY your own assigned file

**Forbidden to use:** prior-round artifacts as evidence. Every judgement must come from text or source data you read yourself. Treat the manuscript as mature or not on its own merits — do not assume it has passed anything.

## Environment notes (read before you start — do not rediscover these)

- Shell is Git Bash on Windows. Paths use forward slashes. Workspace root: `D:/2026.10/机械应力/`.
- Python with pandas/numpy/scipy available: **`C:/Python314/python.exe`**. (The default `python` on PATH lacks pandas — gate scripts fail with ModuleNotFoundError under bare `python`; use the full path.)
- Raw inputs (already downloaded, do not re-download): `analysis/data/raw/GSE342782_Processed_DirectInf_neuronHD10s_BulkSeq_Counts.csv.gz`, `analysis/data/raw/GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz`, `analysis/data/raw/GSE342782_series_matrix.txt.gz`.
- Frozen panel: `analysis/config/mtp_panel.json`. Scripts: `analysis/scripts/`. Results: `analysis/results/layer1/` (JSON/CSV + `fig/` PNGs).
- Long single-line paragraphs in the `.md` display truncated in some readers; use `sed -n 'Np' file | fold -s -w 200` if you need a full paragraph.
- The DOI `10.1002/ana.78352` (Niemeyer et al., Ann Neurol 2026) is cited as the source study; its claims about donor age/sex confounding come from the manuscript's citation of it, not from data you have.

## Mandatory checks for every reviewer

1. **Any claim in the manuscript that you CAN verify, you MUST verify.** Numbers you cite in your report must be ones you recomputed yourself (or explicitly say you trusted the deposited artefact and name the file+key).
2. Read the ENTIRE manuscript including Abstract, all figure/table callouts, Data availability, Ethics, and References. Every reference that you can check against PubMed/Crossref (via WebFetch/WebSearch), check: PMID/DOI resolves to the correct paper, author list, title, journal, year. Report any mismatch.
3. Do not trust the deposited results blindly — spot-recompute at least 3 headline numbers from the raw counts.
4. Where you propose a fix, give a paste-ready English replacement sentence, or an explicit spec for a new analysis (variables, strata, output columns). "Consider strengthening" style comments are banned.
5. Do NOT mention what tools you use; write review comments only.

## Output contract — every item must have four parts

- 【Problem】 one sentence
- 【Evidence】 pinned to file:line, or section + exact numbers you recomputed
- 【Why it matters】 concrete effect on conclusions / credibility / acceptance
- 【Specific fix】 paste-ready English replacement sentence, or explicit analysis spec

Also required in every report:
- **§ Stands up (≥3 items, with evidence)** — things you suspected but found correct. Explicitly mark them; this tells the author what NOT to change.
- **§ Questions for the authors** — what you need to know; do not guess answers.
- **§ What I actually checked** — files read, commands run, values recomputed vs the manuscript's, with discrepancy stated (or "identical").

Write your report to `reviews/<YOUR_CODE>_<role>.md` (you will be told your code). Expect 200–500 lines. End with a numbered **must-fix list** ordered by severity.
