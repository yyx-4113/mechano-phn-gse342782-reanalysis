# C4 — Language quality and venue compliance (post-polish review)

**Reviewer:** C4 (language editor / venue-compliance reviewer; first-exposure review of v1.1.8)

## Mandate

Assess the prose quality after the de-AI revision, verify AMA/Dove mechanical style, and re-run the Journal of Pain Research submission checklist.

## Prose quality (post-polish)

- **Machine-writing tells:** none detectable on scan. Em-dash count 0 (was 54); no "robust" outside file names and one gated phrase; no "highlight/underscore/showcase/pivotal/landscape/delve" register; no formulaic sentence openers ("Notably," / "Moreover," / "Furthermore,"); no "It is worth noting".
- **Evidence-calibrated hedges** are preserved and should stay: "resolution-limited", "bounded null", "floor-limited descriptive value", "hypothesis-generating", "descriptive rank-based observation rather than as a negative control". These are hedges doing scientific work, not padding.
- **Readability:** long sentences remain, but the punctuation substitutions are on balance an improvement — appositions that were em-dash pairs now sit in parentheses, and several list-introducing colons genuinely read better than dashes.
- **En-dashes:** 8 remain, all legitimate numeric ranges or fixed compounds (Piezo1–FAK, Benjamini–Hochberg, 18-20, q ≈ 0.07–0.13, −0.39 to −0.10-type ranges). Correct per style.

## Mechanical style spot checks (AMA, as gated)

- Superscript citation numbers follow punctuation, numbered in first-appearance order 1→27; cited set = listed set; no parenthetical "[n]" forms in body. ✓
- Author lists: ≤6 listed before "et al." throughout the 27 references. ✓
- Every reference carries year, journal, volume(issue):pages, DOI and PMID (ref 15, Benjamini–Hochberg, is a statistical monograph citation — DOI/PMID not applicable; consistent with prior accepted form). ✓
- Units and formats: "log2CPM" defined once (§2.3) and used consistently; P values to two–three decimals consistently; CI format consistent. ✓

## Ruling on "ie" (§3.3)

The manuscript prints "ie E1 is not separable from N1 at the module level" without periods. An earlier round recorded this as a deliberate Dove-style choice and enforces it in the consistency gate. AMA convention would be "i.e.,". I could not verify Dove's rule from public sources during this review. Ruling: **retained** — there is no positive evidence against it, and reversing a previously recorded, gate-enforced decision without evidence is churn. If the production office normalizes it at proof stage, that is costless.

## Advisory wording fix (rides with C1's required fix)

§3.4: "SCN10A contributes to E1 only in the infection experiment" — the gene is an E1 member in both routes; what differs is its measurable contribution (mean CPM 7.23 vs 0.55). Recommend: "SCN10A contributes appreciably to the E1 score only in the infection experiment". One clause, zero risk to any number or citation.

## JPR submission checklist (re-run on v1.1.8)

| Requirement | Status |
|---|---|
| Structured abstract ≤300 words | 294 ✓ (Keywords line excluded from count per gate logic) |
| Keywords 3–6 | 6 ✓ |
| All sections present (Abstract → Data availability → Declarations) | ✓ |
| Figures cited in body, numbered in order | Figures 1, 2a–2d cited in order ✓ |
| Tables cited | Table 1 cited ✓ |
| Corresponding author address / telephone / fax | Address, phone, fax-note present ✓ |
| Data availability with persistent identifiers | GEO URL + GitHub tag v1.1.8 ✓ |
| Ethics statement (secondary analysis of public data) | ✓ |
| Author contributions / conflicts / funding | ✓ |
| Running title | ✓ |
| Title qualification of model (HD10.6) | ✓ |
| Single author, no MD/PhD title | ✓ (correct) |

## Verdict

Language and compliance pass. One required fix exists in this round (C1's comma, §3.1) plus the one-clause advisory above; both are text-only and can ship together in the next patch version.
