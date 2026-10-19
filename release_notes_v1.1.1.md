# Release v1.1.1 — Layer 1 reanalysis of GSE342782

## Scope
This release supersedes v1.1.0. It incorporates the corrections demanded by the
independent Round-2 review (statistical, pain-neuroscience, and reproducibility
panels) and hardens the reproducibility audit.

## Key scientific changes vs v1.1.0
- **Channel-class selectivity reframed to gene level.** The full-module
  contrast-of-contrasts interaction (E1 vs M1 selectivity, P = 0.0017) was shown
  to be an artefact of detection-floor asymmetry between modules (M1 carries 4/9
  genes below detection, each contributing ~0 and diluting its module mean; E1
  only 5/18). Restricting both modules to detected genes (mean CPM > 1) yields a
  much smaller interaction (−0.072) that is **not significant (P = 0.16)**.
  The selectivity is therefore reported as **gene-level and hypothesis-generating**
  only: E1 component genes (TRPV1, SCN9A, ASIC1/2, KCNS1) are individually
  significant, whereas **no M1 gene reaches significance** (PIEZO2 P = 0.18,
  PIEZO1 P = 0.10, P2RX3 P = 0.076).
- **Interaction test disclosed as post hoc.** It was not in the original frozen
  analysis plan; reported as exploratory with explicit multiplicity disclosure
  (two routes tested; Bonferroni-adjusted exosome interaction P = 0.0034 remains
  significant, but the detected-gene correction above renders the selectivity
  non-significant).
- **Piezo2 literature corrected.** Citations now read: Woo et al., 2014
  (mechanotransduction channel); Sánchez-Carranza et al., 2024 (gain-of-function
  sensitizes nociceptors — Brain); Murthy et al., 2019 (required for mechanical
  pain in mice); Chesler et al., 2016 (human loss-of-function mechanosensation
  / tactile-allodynia defects — NEJM); Cox et al., 2006 (SCN9A loss-of-function).
- **PHN confounder caveat** added (donors older and almost exclusively female;
  exploratory contrast behaved non-specifically).
- **SCN10A (Nav1.8) floor caveat** retained: mean CPM 0.55, detected in 2/19
  samples (≈11%); its descriptive log2FC (−0.384) is reported but not treated as
  a confirmed signal.

## Reproducibility hardening
- Pipeline (`layer1_mechano.py`) now also reports the **detected-gene interaction**
  and an **independent raw-count M3 permutation recompute** is added to the gate,
  breaking the circular-dependency concern raised by the reproducibility panel.
- Consistency gate (`gate_consistency.py`): **87/87 assertions PASS**, including
  the independent M3 recompute matching the canonical result (permutation P = 0.42).
- MANIFEST re-frozen for tag **v1.1.1** (40 deposited artifacts, SHA-256 below).

## Data availability
Raw and processed inputs, all scripts, frozen panel (`mtp-frozen-2026-10-19`),
result JSON/CSV, figures, and this MANIFEST are regenerated from the raw GEO
files by the deposited pipeline. No data are "available on request."

Repository: https://github.com/yyx-4113/mechano-phn-gse342782-reanalysis (tag v1.1.1)

## Archive integrity
`release_v1.1.1.zip` SHA-256:
`409270c8d188c754bf2c2e6a74384be44ed84e7253833af9cb603c0d23bc50d4`
