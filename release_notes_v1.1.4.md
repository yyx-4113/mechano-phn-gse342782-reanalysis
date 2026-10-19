# Release v1.1.4 — JPR Round-4 revisions: compliance, citation integrity, and an internal benchmark

Round 4 was organized by the handling editor as a three-reviewer panel (biostatistics/methodology,
pain neuroscience, clinical pain medicine + journal compliance). Every number introduced in this
release was **independently recomputed outside the pipeline before being written into the text**
(verification script results reproduced below), and every reviewer claim was checked rather than
accepted.

## 1. A new internal benchmark: E1 is not separable from its own neutral control

The single most consequential change. The manuscript previously claimed channel-class *selectivity*
on the basis that E1 fell while M1 did not. It never tested E1 against the neutral control that was
built for exactly that purpose (N1, voltage-gated channels).

- Per-sample (E1 − N1) difference under HZ exosomes: **−0.064 log2CPM, exact permutation P = 0.178**
  (Welch P = 0.187; Mann–Whitney P = 0.259).
- E1 therefore survives as a **gene-level, family-corrected signal led by TRPV1**, not as a
  demonstrated module-level dissociation from control channels. The abstract, §3.3, §4.4 and the
  figure captions were all amended accordingly.

Independent recomputation reproduced the pipeline exactly on every pre-existing statistic
(M1 P = 0.1131, E1 P = 0.0128, M3 P = 0.4219, BH q = 0.0341, …), so this is a genuine addition,
not a correction of earlier arithmetic.

## 2. Citation integrity: three references pointed at the wrong papers

Checked against PubMed E-utilities and Crossref (2026-10-19):

| Ref | Problem | Correction |
|---|---|---|
| [18] | Volume/pages/DOI/PMID all belonged to an unrelated *Brain* glioma-mapping paper | *Brain*. 2024;**147(10):3487–3500**; doi:**10.1093/brain/awae227**; PMID **38984717** |
| [19] | PMID 27726347 resolved to an *Inorg Chem* paper | PMID **27653382** |
| [11] | DOI missing a digit (`embj.202211799`) | doi:**10.15252/embj.2022111799**; PMID 35844093 added |
| [3], [16] | PMID missing | 42734212; 21816040 |

Author lists were also brought into line with Dove's rule (≤6 authors listed in full, otherwise
first three + *et al.*) using author counts retrieved from PubMed, not from memory.

## 3. Journal compliance (Dove Press instructions, verified online)

- **Abstract trimmed from 414 to 300 words** (limit 300).
- **In-text citations converted to superscript Arabic numerals without parentheses, placed after
  punctuation** (16 citations); the reference list is untouched.
- **Figures are now cited in the text** — previously five figures were embedded in the Word file
  with no in-text call-out (Figure 1 in §3.1; 2a/2c in §3.3; 2d in §3.4; 2b in §3.6).
- Corresponding-author block completed with department, postal address, telephone and fax line.
- Word file gained continuous line numbering, footer page numbers and double line spacing.
- Remaining British spellings removed (`remodeling`, `analyzed`).
- **New `gate_jpr_compliance.py`**: 30 checks covering abstract length, keyword count, reference
  numbering, American spelling, figure/table citation, contact block, mandatory sections. This gate
  is separate from `gate_consistency.py` — one tests *self-consistency of numbers*, the other tests
  *conformance to the journal*. Both must be green.

## 4. Pipeline bug fixed: cross-module q-value overwrite

`q_within_module` was written back into a single row per gene, so genes belonging to two modules
were overwritten by whichever module was processed last. KCNQ2 and KCNQ3 (in both E1 and N1) carried
N1's q values inside the E1 dictionary (0.5636 / 0.5004 instead of 0.4970 / 0.3655). Fixed by
computing q per (contrast, module, gene) and emitting one row per module membership; the CSV now
carries a `module` column. Three regression assertions were added to the gate.

## 5. Figures regenerated

The embedded figures still described the pre-Round-2 analysis (`B = 5000 Monte-Carlo`, a
"double dissociation", `P = 0.416`). They now state exact permutation, carry the E1-vs-N1 caveat,
and no longer assert a dissociation.

## 6. Other reviewer-driven additions

- §3.7 (new): neuronal integrity — ATF3 unchanged (+0.0002, P = 0.998) argues against cytotoxicity,
  while pan-neuronal markers move modestly, bounding the specificity claim in both directions.
- §3.4: route dependence is one of **magnitude, not direction** — TRPV1 also falls under direct VZV
  (−0.149, P = 0.008, within-E1 q = 0.144).
- §3.1: baseline means now state their denominator (SCN9A 8.31 all-12 vs 8.39 mock-only).
- §4.4: three new limitations — substrate stiffness unmeasured (xii), neurons-only preparation and
  unquantified exosome dose (xiii), and the E1-vs-N1 non-separation (xi).
- §3.5: donor age/sex are **absent from the deposited GEO metadata**, so the PHN confounding is
  documented as reported by the source publication and cannot be quantified here.
- §4.3: "inert" softened to "no detectable transcriptional response".

## Verification status

- `gate_consistency.py`: **119/119 PASS**
- `gate_jpr_compliance.py`: **30/30 PASS**
- Independent recomputation (fresh implementation, raw counts): reproduces M1/M2/M3/M4/E1/N1–N3
  permutation P values, all BH q values, TRPV1 under both routes, ATF3 and the neuronal panel.
- MANIFEST: 42 files, tag `v1.1.4`, SHA-256 per artifact.
- Release archive: `release_v1.1.4.zip`, SHA-256 `d53dbd790ef33c4a31ce312f0e15d6d0a407d75e04dfcd58aff0f88606eb4e26`
