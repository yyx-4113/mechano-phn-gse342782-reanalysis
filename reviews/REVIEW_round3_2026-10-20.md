# Round-3 targeted review — v1.1.7 acceptance audit (editor's copy)

**Date:** 2026-10-20 · **Editor:** Yongxin Yang (acting editor, single-author project)
**Scope:** not a new scientific review — a targeted audit that (a) every Round-2 revision item actually landed in the v1.1.7 submission package, (b) no new internal contradiction was introduced by the revisions, and (c) the package is internally consistent (manuscript ↔ docx ↔ artifacts ↔ cover letter ↔ repository state). This is the final gate before the "accept for submission" decision.

## Method (three independent lines)

1. **Gates (self-consistency + venue compliance):** `gate_consistency.py` 228/228 PASS; `gate_jpr_compliance.py` 45/45 PASS (abstract 294/300 words, AMA citation order, captions present, brand-free README, tag v1.1.7 everywhere).
2. **Editor independent recomputation** (`analysis/verify_round2/verify_round2.py`): re-derives every Round-2 statistic from the raw GEO count matrices + frozen panel only, comparing against deposits and printed values — **114/114 PASS**, exit 0.
3. **Packaging audit:** citation completeness/orphaning, section and figure cross-references, docx↔md number-layer equality, cover-letter alignment, MANIFEST coverage and hash verification, git tag ↔ manuscript version ↔ Data-availability string.

## A. Round-2 revision items — landing verification

| # | Round-2 item (panel) | Where it landed | Status |
|---|---|---|---|
| 1 | B1 PTK2 duplication disclosure | §2.2 + §3.2 sensitivity (−0.047, P = 0.44; −0.024, P = 0.52) | ✅ verified vs artifact |
| 2 | B1 CCN1/CCN2 alias sensitivity | §3.2 (58 genes: −0.048; P = 0.42) | ✅ |
| 3 | B2 route dependence as contrast-of-contrasts | §3.2 M4 route (+0.027; P = 0.58), §3.4 DiDiD (−0.193; P = 0.0011), §4.2, §5 | ✅ recomputed 114/114 |
| 4 | B2 M1 resolution limit (detected-gene flip) | §3.3 (P = 0.046), §3.6 (−0.171, P = 0.046), §5 | ✅ |
| 5 | B2 E1-vs-N1 benchmark | §3.3 (−0.064; P = 0.178; Welch 0.187), §4.4(xi), cover letter | ✅ recomputed |
| 6 | B3 content/code audit — docx↔md | docx rebuilt; number layer 400/400 tokens equal; 5 figures, 30 superscript runs, 5 captions, 1 table, continuous line numbers, PAGE field | ✅ |
| 7 | B3 MANIFEST coverage | root MANIFEST v2 (71 files, no self-entry, forward-slash keys) + layer1 MANIFEST (21 entries) | ✅ 0 hash mismatches |
| 8 | B3 packaging hygiene | v1.1.5 archived; v1.1.4 archive move **blocked by OS file lock** (see D) | ⚠️ deferred |
| 9 | B4 venue compliance (AMA, captions, word limits) | 45/45 gate; 27 references renumbered in first-appearance order; every PMID/DOI verified programmatically | ✅ |
| 10 | B5 wording repairs | Chesler claim corrected; triple-negative sentence repaired; (vi)(vii) contradictions fixed; new limitations (xiv)(xv)(xvi) | ✅ |

## B. New-contradiction scan (revisions themselves)

- **BH families kept separate across contrasts:** §3.2's "q = 0.20" for M4 refers to the VZV-vs-mock family (deposit: 0.1991); §3.6's table refers to the HZ-exo family (M4 q = 0.462). Both verified against `layer1_results.json` — no conflation.
- **Route statements consistent:** §3.2 (no route specificity for M4), §3.4 (DiDiD supports route dependence for E1−M1), §4.2 (asymmetric: exosome E1 signal vs no selective M1 signal), §5 (same framing) — consistent, and the detected-gene dilution caveat is carried in all locations.
- **Detection-floor narrative consistent:** SCN10A floor-limited (§3.3), M1 dilution (§3.4/§3.6), TRPA1 CPM 0.033→0.007 (§3.6), OR5A1 0.89 CPM (§3.6) — all recomputed.
- **Citation integrity:** 39 citation tokens → 27 unique refs, strictly sequential by first appearance, no orphans either direction, no bracketed citations, all §x.y cross-references resolve, all five figures + Table 1 cited in body text.
- **Cover letter ↔ manuscript:** title string identical; PHN definition, DiDiD, E1−N1, MoR robustness (E1 P = 0.015; M3 P = 0.64) all match; signature "Yongxin Yang, B.M." (no graduate-degree title).
- **Version string consistency:** manuscript Data availability (tag v1.1.7) = git tag v1.1.7 = CITATION.cff 1.1.7 = root MANIFEST tag = release notes.

## C. Errors found by this audit and fixed (before acceptance)

1. **M3−PTK2 printed −0.048** → corrected to **−0.047** (full precision −0.0474965; the 4-decimal deposit −0.0475 had been rounded upward as if exact).
2. **E1-core Welch CI used pooled df = 12** (interval −0.383 to −0.105, anti-conservatively narrow) → replaced with the Welch–Satterthwaite df = 9.38 used everywhere else in the paper: artifact CI [−0.388, −0.101], manuscript prints **−0.39 to −0.10**. Artifact regenerated; byte-diff confirmed only `welch_ci95` changed (+ new `welch_ci95_df`).
3. **The verification tool itself had a bug** (v1 built the M4-route null from the E1−M1 composite distribution, giving P = 0.6731); fixed in v2, which now reproduces the deposited P = 0.5783 exactly. Disclosed in release notes for audit transparency.
4. **Root MANIFEST hygiene:** removed the impossible self-referential hash entry, switched keys to forward slashes, excluded reviewer scratch directories (which had leaked in, including a duplicated raw-data copy), extended coverage to reviews/ and all release notes; tag/date parameterized in `make_manifest.py`.

## D. Known deviation (non-blocking)

`manuscript/manuscript_v1.1.4.docx` could not be moved to `manuscript/archive/` — the file is locked by another process on this machine (OS "Device or resource busy"; retried 4×). It remains tracked in `manuscript/` and is therefore included in the v1.1.7 release zip and root MANIFEST. This affects packaging tidiness only; no script, gate, or manuscript text references it. Once the file is closed, move it to `archive/`, regenerate the root MANIFEST, and the next tag will exclude it automatically.

## Decision

**ACCEPTED for submission to the *Journal of Pain Research* as v1.1.7.** All Round-2 revision items are landed and independently verified; the two printed-value errors introduced/undetected earlier were caught and fixed by this audit line; both gates and the editor recomputation are green; the release artifact (tag v1.1.7) matches the manuscript, the cover letter, the deposits, and the MANIFEST. The only open item is the cosmetic D above.

Submission checklist status: manuscript (md+docx) ✅ · cover letter ✅ · figures (5 PNG, embedded) ✅ · tables ✅ · references (27, AMA) ✅ · reproducibility package (public repo, tag v1.1.7, release zip + SHA-256) ✅ · data availability statement ✅ · ethics/consent statements ✅.
