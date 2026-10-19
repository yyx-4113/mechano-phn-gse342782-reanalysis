# Release v1.1.2 — Journal of Pain Research submission finalization

Editorial finalization pass to bring the Layer 1 manuscript into *Journal of Pain Research*
(Dove Press) submission compliance. No scientific results changed; all figures and
statistics are identical to v1.1.1 (gate 87/87 PASS, independent M3 permutation recompute P = 0.42).

## Changes
- **New citation [2]** — Liang X, Fan Y. *Front Immunol* 2023 (FinnGen PHN GWAS, n = 195,191):
  supports the sentence on genetic/causal determinants of PHN risk, displacing the prior
  Johnson & Rice 2014 NEJM review (now renumbered) which remains cited for the PHN/allodynia definition.
- **New citation [20]** — Dworkin RH et al. *Pain* 2007 (evidence-based neuropathic-pain guideline):
  anchors the clinical statement that mechanical allodynia is a cardinal, defining symptom of PHN.
  (Prior ref [6] Haberberger 2020 remains for the HD10.6 cell-line identity.)
- **Abstract trimmed to 292 words** (JPR limit: 300) by tightening the Background/Methods/Results phrasing.
- **British → American spelling** throughout the manuscript body and the cover letter
  (programme→program, signalling→signaling, immortalised→immortalized, emphasise→emphasize, centred→centered,
  hypothesised→hypothesized), per JPR's American-English requirement. The verbatim reference list is untouched.
- **Filename honesty**: manuscript renamed `manuscript_v1.1.2.md`; the superseded `manuscript_v1.0.0.md`
  source is moved to `manuscript/archive/` and excluded from the deposited MANIFEST.

## Consistency & reproducibility
- `gate_consistency.py`: **87/87 assertions PASS**, including the independent raw-count M3 permutation
  recompute (P = 0.42, matches the pipeline-derived value).
- `MANIFEST.json`: 38 deposited files, tag `v1.1.2`, SHA-256 over every artifact.
- Repository: https://github.com/yyx-4113/mechano-phn-gse342782-reanalysis (tag v1.1.2)

## Pre-submission checklist (JPR)
- [x] Structured abstract ≤ 300 words (292)
- [x] 3–6 keywords (6)
- [x] Numbered Vancouver references
- [x] American English
- [x] Pre-registered single primary endpoint + frozen panel (`mtp-frozen-2026-10-19`)
- [ ] Author-instructions final format pass (page/line limits, figure legends) — do at submission
- [ ] Re-confirm [2] Liang & Fan and [20] Dworkin DOIs at submission
