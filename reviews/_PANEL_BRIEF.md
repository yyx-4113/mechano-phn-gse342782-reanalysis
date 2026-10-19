# Panel brief — Round 1 review (editor-set, 2026-10-19)

You are reviewing a manuscript submitted to **Journal of Pain Research** (SCIE,
JIF 3.1 / 2025, JCR Q2) as a **research article / bioinformatics reanalysis**.

## The manuscript

`D:/2026.10/机械应力/manuscript/manuscript_v1.0.0.md`

Title: *Route-dependent transcriptional effects of varicella-zoster virus and
patient serum exosomes on ion-channel programmes in human sensory neurons: a
pre-registered reanalysis of GSE342782*

What it claims, in one paragraph: A frozen four-module mechanotransduction
panel (M1 mechanogated channels; M2 membrane–cytoskeleton coupling; M3
ECM–integrin–Hippo; M4 mechano-effectors), plus an electrochemical nociceptor
module (E1) and three neutral controls (N1–N3), was pre-registered before data
examination. Primary endpoint = M3 module-score difference between acute-HZ
serum exosomes and control exosomes in differentiated HD10 human sensory
neurons. Reported result: primary endpoint is a correctly-powered null
(−0.049 log2CPM, permutation P = 0.416, q = 0.46); secondary endpoint E1 is
suppressed (−0.220, P = 0.011, q = 0.030) with PIEZO2 spared; direct VZV
infection shows the mirror pattern (M1 −0.050, P = 0.051; E1 +0.0005,
P = 0.996); exploratory PHN-exosome contrast is non-specific (a neutral module
N1 also shifts, P = 0.035) and confounded (donors older, almost all female).

## Where everything lives (verify from these, not from the manuscript)

- Raw data (gzip-verified GEO processed counts):
  - `analysis/data/raw/GSE342782_Processed_DirectInf_neuronHD10s_BulkSeq_Counts.csv.gz`
  - `analysis/data/raw/GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz`
- Frozen panel: `analysis/config/mtp_panel.json`
- Analysis scripts: `analysis/scripts/layer1_mechano.py`, `layer1_diag.py`,
  `fig_layer1.py`, `fig_extra.py`, `make_manifest.py`
- Results: `analysis/results/layer1/layer1_results.json`, `layer1_diag.json`,
  `layer1_module_scores.csv`, `layer1_cci.csv`, `MANIFEST.json`
- Manuscript consistency gate: `manuscript/gate_consistency.py` (74 assertions)
- Protocol: `PROTOCOL_机械应力与PHN.md` (Chinese; v0.4)
- Cover letter: `manuscript/cover_letter_JPR.md`
- Reproducibility repo (public): https://github.com/yyx-4113/mechano-phn-gse342782-reanalysis

## Independence discipline (mandatory)

Forbidden to read: `REVIEW_*.md`, `RESPONSE_*.md`, `REVISION_*.md`,
`.workbuddy/memory/*`, `README.md`, `CITATION.cff`, `GITHUB_DEPOSIT_SOP.md`,
`author_verification_statement.md`, `PROTOCOL_机械应力与PHN.md`, and any other
reviewer's output in `reviews/`. Do not assume the manuscript is mature or has
passed previous review: treat it as a first submission. Every judgement must
come from text or data you read yourself. Any claim in the manuscript that you
CAN verify, you MUST verify.

## Output contract (every item, four parts)

- 【Problem】 one sentence
- 【Evidence】 pinned to file:line, or section + exact numbers; numbers you cite
  must be ones you recomputed yourself
- 【Why it matters】 concrete effect on conclusions / credibility / acceptance
- 【Specific fix】 paste-ready English replacement sentence, or an explicit spec
  for a new analysis (variables, strata, output columns)

"Consider strengthening the discussion" is banned.

## Also required in your report

- § Stands up (≥3 items, with evidence) — things you suspected but found
  correct. This is a deliverable, not filler.
- § Questions for the authors.
- § What I actually checked — files read, commands run, values recomputed vs
  the manuscript's, with any discrepancy stated.

Do not mention what tools you use; write review comments only.

## Environment notes

- Managed Python 3.13: `C:/Users/Administrator/.workbuddy/binaries/python/envs/default/Scripts/python.exe`
  (pandas/scipy/numpy/matplotlib available). Use forward slashes in paths.
- If you recompute module scores, reproduce the pipeline in
  `analysis/scripts/layer1_mechano.py` rather than inventing a new one — your
  job is to audit that pipeline, not replace it (unless you believe the pipeline
  itself is wrong, in which case say so explicitly and show the corrected
  numbers).
