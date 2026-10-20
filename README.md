# Mechanical stress x postherpetic neuralgia — prospectively specified reanalysis of GSE342782

Reproducibility package for: *Route-dependent transcriptional effects of varicella-zoster virus and patient serum exosomes on ion-channel programs in an immortalized human sensory-neuron line (HD10.6): a prospectively specified reanalysis of GSE342782* (Yongxin Yang, ORCID 0009-0004-9698-6552).

Protocol v0.4 and the frozen panel (`mtp-frozen-2026-10-19`) were committed to this repository before any expression data were examined; no external registry entry exists.

## File map

```
PROTOCOL_机械应力与PHN.md          # prospectively specified protocol (v0.4) incl. execution milestones
manuscript/
  manuscript_v1.1.8.md             # full manuscript (source of truth for text; current version)
  manuscript_v1.1.8.docx           # submission file (Times New Roman 12 pt, figures embedded)
  archive/                         # superseded manuscript versions (excluded from release packaging)
  build_docx.py                    # md -> docx builder
  cover_letter_JPR.md              # cover letter
  gate_consistency.py              # consistency gate (manuscript numbers vs deposited artifacts)
  gate_jpr_compliance.py           # Journal of Pain Research compliance gate
reviews/                           # independent multi-expert review reports (editor's copies)
analysis/
  config/mtp_panel.json            # FROZEN panel, tag mtp-frozen-2026-10-19 — do not modify
  scripts/layer1_mechano.py        # W0 examination + module scores + CCI + permutation nulls
  scripts/layer1_diag.py           # gene-level diagnostics + global-shift audit
  scripts/layer1_extra_checks.py   # E1-N1 benchmark + neuronal integrity + TRPV1 by route
  scripts/layer1_norm_robustness.py# DESeq2-style median-of-ratios robustness
  scripts/layer1_round2_additions.py # route x module DiDiD, detected-gene CCI, E1-core, PTK2 sensitivities
  scripts/gen_manifest.py        # regenerates results/layer1/MANIFEST.json (SHA-256)
  verify_round2/                 # editor-run independent recomputation (114 checks)
    verify_round2.py             # re-derives every Round-2 number from raw counts
    verify_round2_output.txt     # latest run (must end "114/114 checks PASS")
  scripts/fig_layer1.py            # Fig 2a, 2b, 2d
  scripts/fig_extra.py             # Fig 1 + Fig 2c
  data/raw/                        # GEO inputs (gzip-integrity verified)
  results/layer1/
    layer1_results.json            # all statistics (incl. BH q-values)
    layer1_round2_additions.json   # post hoc robustness analyses deposited for the Round-2 (v1.1.7) revision
    layer1_module_scores.csv       # per-contrast per-module table
    layer1_cci.csv                 # CCI results
    layer1_gene_level.csv          # per-gene per-contrast table (incl. within-module BH q)
    layer1_global_de.csv           # global differential-expression counts
    layer1_diag.json               # global-shift audit
    layer1_extra_checks.json       # post hoc checks (E1-N1 benchmark, injury panel, TRPV1 by route)
    layer1_norm_robustness.json    # median-of-ratios robustness
    MANIFEST.json                  # SHA-256 of inputs and key outputs
    fig/                           # all figures (PNG, 150 dpi)
```

## Reproduce

```bash
python analysis/scripts/layer1_mechano.py        # regenerates all Layer-1 statistics
python analysis/scripts/layer1_diag.py           # regenerates gene-level + global-shift audit
python analysis/scripts/layer1_extra_checks.py   # E1-N1 benchmark + injury panel + TRPV1 by route
python analysis/scripts/layer1_norm_robustness.py# median-of-ratios robustness
python analysis/scripts/layer1_round2_additions.py # Round-2 post hoc robustness analyses
python analysis/scripts/gen_manifest.py           # refreshes MANIFEST.json (run last)
python analysis/verify_round2/verify_round2.py    # editor independent verification (must exit 0)
python analysis/scripts/fig_layer1.py            # Fig 2a, 2b, 2d
python analysis/scripts/fig_extra.py             # Fig 1 + Fig 2c
python manuscript/build_docx.py                  # rebuilds the docx
python manuscript/gate_consistency.py            # must report all assertions PASS
python manuscript/gate_jpr_compliance.py         # venue-compliance gate
```

Software: Python 3.14.5 (NumPy 2.5.1, pandas 3.0.5, SciPy 1.18.0, Matplotlib 3.11.1, python-docx 1.2.0). Input counts are fetched from GEO (GSE342782); URLs are embedded in `analysis/data/raw/_download.sh`.

## Caveats

- The MTP panel in `analysis/config/mtp_panel.json` was frozen **before** data examination; any change requires a changelog entry and a version bump.
- CYR61 and CTGF are absent from the processed matrix; TRPV4/STOML3/LOX/MMP9 are below detection in HD10 neurons — see manuscript §3.1.
- The PHN-exosome contrast is exploratory (donor age/sex confounding, acknowledged by the original authors).
- The primary endpoint (M3, HZ-exo vs control-exo) is a **correctly bounded null** (80% power for effects >= 0.18 log2CPM) and is reported as such.
- All manuscript numbers are traceable to the deposited artifacts; both gates must be green before submission.
