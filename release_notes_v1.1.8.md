# Layer 1 reanalysis v1.1.8 — de-AI language polish (prose-only revision; no number, citation, or claim changed)

## 1. Scope

A pass over `manuscript/manuscript_v1.1.8.md` to remove machine-writing tells while preserving scientific content exactly. This is a **language-only revision** of the v1.1.7 text: every number, unit, citation, figure caption value, table entry, and claim is unchanged. The verification below is the evidence for that claim.

## 2. What was changed (by pattern type)

- **Em-dashes: 54 occurrences, all removed.** Prose asides ("X — the M3 difference ... — was -0.049") were recast with commas, parentheses, or colons. The one em-dash in the author correspondence block was replaced with a vertical bar. Post-pass count: 0 (was 54).
- **AI-vocabulary trimming (10 "robust" instances audited):** "robustly expressed" -> "highly expressed" (§3.1 heading); "a robust E1 suppression" -> "a clear E1 suppression at the gene level" (§4.2); "is not robust to detection-floor correction" -> "does not survive detection-floor correction" (§4.2); "the robust module-level E1 suppression" -> "the module-level E1 suppression" (§4.4 vi); "the normalization-robustness analysis" -> "the normalization sensitivity analysis" (§3.6, aligning with §2.3's own wording). **Kept verbatim:** the five remaining instances that are file names (`layer1_norm_robustness.json`) or protected assertions (the "post hoc robustness analysis" phrase required by the consistency gate).
- **Boilerplate emphasis removed:** "We emphasize that this null is a substantive result" -> "This null is a substantive result" (§3.2); "Critically, E1 must also be judged..." -> "E1 must also be judged..." (§3.3).
- **Hype adjective removed:** "aligning with the growing literature" -> "aligning with the literature" (§4.2); "an important negative result" -> "a negative result that redirects the mechanical-axis search toward non-neuronal compartments" (§5).
- **Vague count made precise:** "several pan-neuronal markers" -> "five pan-neuronal markers" (§3.7; five genes are listed).
- **Sentence tightening:** a small number of clause-stacked sentences split; no sentence that carried a gated assertion fragment was restructured beyond punctuation.

## 3. What was NOT changed

- All ~130 gated text fragments (consistency-gate `numchk`/`present` assertions) survive verbatim; both gates re-run green.
- All numbers: numeric-token set difference between v1.1.7 and v1.1.8 is **empty in both directions** (nothing lost, nothing invented).
- All 27 references, all citation superscripts, the title, the five figure captions' quantitative content, Table 1, the abstract's six labelled paragraphs (still 294 words, limit 300), and all hedges calibrated to evidence ("suggests", "resolution-limited", "bounded null", "hypothesis-generating").
- Deliberately preserved as correct scholarly constructs (per humanizer rules): evidence-tied hedging, passive voice, "we", semicolons, en-dashes in numeric ranges and standing compounds (e.g., `Piezo1–FAK`, `Benjamini–Hochberg`, `18-20`, `0.07–0.13`), journal-format bold run-in labels (Background/Methods/..., **Frozen panel.**, Table 1), and file names.

## 4. Verification

- **Machine scan (encoding-safe, Python):** em-dash 54 -> **0**; curly quotes 0; prose boldface limited to journal-format labels; AI-vocabulary watchlist re-scanned clean (remaining "robust" = file names + one gated phrase, listed above).
- **Numeric set-diff v1.1.7 -> v1.1.8:** `lost = []`, `added = []`.
- **`gate_consistency.py`: 228/228 PASS** (every expectation still derived from deposited artifacts; none hard-coded).
- **`gate_jpr_compliance.py`: 45/45 PASS** (abstract 294/300 words, 6 keywords, AMA citation order, caption presence +限定词, tag v1.1.8, cover-letter/README consistency).
- **Editor independent recomputation (`analysis/verify_round2/`): 114/114 checks PASS** unchanged; it reads raw counts and does not depend on manuscript prose.
- **`manuscript_v1.1.8.docx` rebuilt and verified:** 5 embedded figures, 30 superscript citation runs, 5 captions, 1 table, continuous line numbers, footer PAGE field; em-dash count in docx text = 0; md<->docx numeric layer 400/400 tokens with zero difference (same test as v1.1.7).
- Superseded `manuscript_v1.1.7.md/.docx` moved to `manuscript/archive/`; root MANIFEST regenerated (tag v1.1.8); release zip cross-verified against the MANIFEST (0 mismatch).

## 5. Version ladder

- **v1.1.7** — Round-2 expert-review response + Tier-0/Tier-1 analyses + editor final verification (reviews/REVIEW_round3_2026-10-20.md accepted it for submission).
- **v1.1.8** — this release: de-AI language polish on top of v1.1.7, content-identical. **Cite v1.1.8 when submitting.**
