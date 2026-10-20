# Layer 1 reanalysis v1.1.9 — Round-4 post-polish verification + two prose fixes (content-identical to v1.1.8)

## 1. Scope

`manuscript/manuscript_v1.1.9.md` is the **Round-4 editorial revision** of v1.1.8. Round 4 was a post-de-AI-polish verification audit plus a fresh-eye final read (reviews/_PANEL_BRIEF_round4.md + C1–C4 + REVIEW_round4_2026-10-20.md). Two genuine prose defects introduced or surviving from the de-AI pass were repaired; everything else is unchanged.

## 2. Round-4 expert findings (C1 semantics, C2 domain, C3 statistics, C4 language/compliance)

- **C1 (semantics/drift):** sentence-level diff of v1.1.7 -> v1.1.8 confirmed **all 40 change blocks are punctuation/lexical only** — no claim, number, or citation drifted. 10/10 Table-1 gene-expression values re-checked from raw counts (PIEZO2, P2RX3, PIEZO1, TRPV4, STOML3, ITGB1, SCN10A, SCN9A, TRPV1, TAC1; means, detection fractions, log2CPM, DI/SE fold ratios) all match the manuscript. **One TRUE defect found (REQUIRED fix):** the de-AI pass deleted an em-dash in §3.1 and left the apposition unclosed — "not an iPSC-derived model^16,17^ expressed PIEZO2 at high levels" reads as if PIEZO2 were the model. Fixed by restoring the closing comma.
- **C2 (domain):** HD10.6 narrative, route-dependent axis, and limitations read cleanly on a fresh read. No domain errors.
- **C3 (statistics):** the two repaired sentences carry no statistic; all reported numbers remain those deposited and editor-recomputed (114/114). No statistical change.
- **C4 (language/compliance):** v1.1.9 em-dash count = 0; "robust" audit unchanged; AMA order, 6 keywords, abstract 294/300, captions, tag all still compliant.

## 3. What was changed in v1.1.9 text (two prose fixes, zero numeric/citation change)

1. **§3.1 — closing comma restored** (C1-1, REQUIRED): "not an iPSC-derived model^16,17^**,** expressed PIEZO2 at high levels (log2CPM 7.94, detected in 100% of samples)" — resolves the dangling modifier left by the v1.1.8 em-dash removal.
2. **§3.3 — precision on SCN10A contribution** (advisory): "SCN10A contributes **appreciably to the E1 score** only in the infection experiment" — makes explicit that the gene loads on E1 in the exosome route too, just not appreciably.

Plus the Data-availability version tag updated to v1.1.9.

## 4. What was NOT changed

- All ~130 gated text fragments survive verbatim; both gates re-run green.
- All numbers: numeric-token set difference between v1.1.8 and v1.1.9 is empty in both directions.
- All 27 references, citation superscripts, title, five figure captions, Table 1, abstract (294/300), and all evidence-calibrated hedges.
- Editor independent recomputation (`analysis/verify_round2/`): 114/114 checks PASS unchanged.

## 5. Verification

- **Numeric set-diff v1.1.8 -> v1.1.9:** `lost = []`, `added = []`.
- **`gate_consistency.py`: 228/228 PASS**; **`gate_jpr_compliance.py`: 45/45 PASS**.
- **`manuscript_v1.1.9.docx` rebuilt and verified:** 5 embedded figures, 30 superscript runs, 5 captions, 1 table, continuous line numbers, footer PAGE field; em-dash in docx text = 0; md<->docx numeric layer 400/400 tokens, zero difference.
- Superseded `manuscript_v1.1.8.md/.docx` moved to `manuscript/archive/`; root MANIFEST regenerated (tag v1.1.9); release zip cross-verified against the MANIFEST (0 mismatch).

## 6. Version ladder

- **v1.1.7** — Round-2 expert-review response + Tier-0/Tier-1 analyses; accepted at Round 3.
- **v1.1.8** — de-AI language polish on top of v1.1.7 (content-identical).
- **v1.1.9** — this release: Round-4 post-polish verification + two prose fixes (comma restoration in §3.1, SCN10A precision in §3.3). **Cite v1.1.9 when submitting.**
