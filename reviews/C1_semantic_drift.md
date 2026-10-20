# C1 — Semantic drift audit of the de-AI revision (v1.1.7 → v1.1.8)

**Reviewer:** C1 (independent semantic-drift auditor)
**Files compared:** `manuscript/archive/manuscript_v1.1.7.md` (accepted text) vs `manuscript/manuscript_v1.1.8.md` (polished text)
**Method:** sentence-level diff (`difflib.SequenceMatcher` on punctuation-split sentences); every non-equal opcode classified and adjudicated for meaning preservation. Complementary checks: decimal-token set-diff (both directions), citation-token diff, figure/table caption diff.

## Headline verdict

**40 change blocks; 0 semantic drifts; 1 grammatical defect introduced by the revision (must fix); 1 terminology rename noted (acceptable).** The revision is meaning-preserving throughout, and four changes actually *improve* precision (§3.4 below).

## Change classification (40 blocks)

| Category | n | Meaning preserved? |
|---|---|---|
| Em-dash apposition → parentheses | 8 | Yes |
| Em-dash apposition → paired commas | 14 | Yes (13) / **No — see F-1** (1) |
| Em-dash → colon or semicolon (list/clause split) | 3 | Yes |
| De-AI vocabulary substitution | 6 | Yes |
| Vague count made precise | 1 | Yes (verified against listed items) |
| Hyperbole/boilerplate removal | 4 | Yes (claim unchanged, emphasis marker removed) |
| Tag/version update | 1 | Required |
| Heading punctuation | 1 | Yes |
| Correspondence-line separator | 1 | Front matter |
| Terminology rename (prose only) | 1 | Yes — see O-1 |

## F-1 (REQUIRED FIX) — missing closing comma, §3.1

- **v1.1.7 (correct):** "The HD10.6 line — a tetracycline-regulatable v-myc immortalized embryonic dorsal root ganglion clonal line, not an iPSC-derived model^16,17^ — expressed PIEZO2 at high levels …"
- **v1.1.8 (defective):** "The HD10.6 line, a tetracycline-regulatable v-myc immortalized embryonic dorsal root ganglion clonal line, not an iPSC-derived model^16,17^ expressed PIEZO2 at high levels …"

The paired em-dashes delimited the apposition. The revision replaced the *first* dash with a comma but deleted the *second* dash without substituting its comma, so the apposition is never closed. A first-read parse can attach "expressed PIEZO2" to the citation superscripts. Required repair: `…not an iPSC-derived model^16,17^, expressed PIEZO2 at high levels…`.

**Severity:** minor in print, but it is a genuine defect introduced by the reviewed revision, in the first Results sentence of the manuscript, and must not ship.

## O-1 (noted, no action) — prose/file-name terminology, §3.6

"normalization-robustness analysis" was renamed "normalization sensitivity analysis". The deposited artifact is still cited verbatim as `layer1_norm_robustness.json` in §2.5, so traceability is intact and the descriptor arguably describes the artifact better than its file name. Cosmetic mismatch between prose and file name; acceptable. No change required.

## Changes that improve precision (no action; recorded for the decision letter)

1. **§4.2:** "produce a robust E1 suppression" → "produce a clear E1 suppression **at the gene level**". The manuscript's own §3.4 discloses that the module-level interaction does not survive the detected-gene subset analysis; "robust" at that position overstated what the paper itself qualifies. The new wording is *more* consistent with the accepted evidence.
2. **§4.4 (vi):** "rests on the robust module-level E1 suppression" → "rests on the module-level E1 suppression" (same rationale).
3. **§5:** "an important negative result directing …" → "a negative result that redirects …" (removes self-appraisal; claim unchanged).
4. **§3.7:** "several pan-neuronal markers" → "**five** pan-neuronal markers"; the sentence lists exactly five genes (NEFH, TUBB3, NTRK1, PRPH, NEFL) — count verified against the list and against the deposited 10-gene panel.

## Definition-preservation checks

- **Numbers:** decimal-token set-diff v1.1.7↔v1.1.8 empty in both directions (0 lost, 0 added).
- **Citations:** 27 references, first-appearance order 1→27, cited set = listed set, no orphan on either side; citation superscripts unchanged at every site (spot-verified at ^1,2^, ^14^, ^16,17^, ^18-20^, ^25,26^).
- **Figures/tables:** 5 captions present, identical text, all called out in body order; Table 1 values identical.
- **Protected phrases:** all ~130 gate-asserted fragments survive verbatim in v1.1.8 (gate_consistency 228/228, gate_jpr_compliance 45/45 on the polished text).

## Rulings on carried-over wording (re-examined, retained)

- "ie" without periods (§3.3): gate-enforced as a Dove-style decision from an earlier round. I could not verify Dove's rule from public sources in this review, and there is no positive evidence against the retained form; overturning a prior recorded decision without evidence would be churn. **Retained; noted for the editor's final record.**
- §3.4 "SCN10A contributes to E1 only in the infection experiment": imprecise (the gene is an E1 member in both routes; what differs is its measurable contribution — 7.23 vs 0.55 mean CPM). Recommend C4-style tightening to "contributes appreciably to the E1 score only in the infection experiment". Non-blocking, cheap, improves accuracy.

## Decision-relevant summary for the editor

The de-AI revision is safe to ship **after** F-1 is repaired. F-1 is a one-comma fix with zero risk to any gated value. The C-4/C-2 advisories (SCN10A wording) can ride in the same version bump. No re-review of content is warranted; this remains a Round-3-accepted manuscript.
