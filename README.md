# Mechanical stress x postherpetic neuralgia — pre-registered reanalysis of GSE342782

Reproducibility package for: *Route-dependent transcriptional effects of varicella-zoster virus and patient serum exosomes on ion-channel programmes in human sensory neurons: a pre-registered reanalysis of GSE342782* (Yongxin Yang, ORCID 0009-0004-9698-6552).

## File map

```
PROTOCOL_机械应力与PHN.md          # pre-registered protocol (v0.4) incl. execution milestones
manuscript/
  manuscript_v1.0.0.md             # full manuscript (source of truth for text)
  manuscript_v1.0.0.docx           # submission file (Times New Roman 12 pt, figures embedded)
  build_docx.py                    # md -> docx builder
  gate_consistency.py              # consistency gate (74 assertions)
analysis/
  config/mtp_panel.json            # FROZEN panel, tag mtp-frozen-2026-10-19 — do not modify
  scripts/layer1_mechano.py        # W0 examination + module scores + CCI + permutation nulls
  scripts/layer1_diag.py           # gene-level diagnostics + global-shift audit
  scripts/fig_layer1.py            # Fig 2a/2b/2c
  scripts/fig_extra.py             # Fig 1 + Fig 2d
  data/raw/                        # GEO inputs (gzip-integrity verified)
  results/layer1/
    layer1_results.json            # all statistics (incl. BH q-values)
    layer1_module_scores.csv       # per-contrast per-module table
    layer1_cci.csv                 # CCI results
    layer1_diag.json               # global-shift audit
    gate_consistency_report.txt    # consistency gate output
    MANIFEST.json                  # SHA-256 of inputs and key outputs
    fig/                           # all figures (PNG, 150 dpi)
```

## Reproduce

```bash
python analysis/scripts/layer1_mechano.py   # regenerates all Layer-1 statistics
python analysis/scripts/layer1_diag.py      # regenerates gene-level + global-shift audit
python analysis/scripts/fig_layer1.py       # Fig 2a-c
python analysis/scripts/fig_extra.py        # Fig 1 + Fig 2d
python manuscript/build_docx.py             # rebuilds the docx
python manuscript/gate_consistency.py       # must report 74/74 PASS
```

Software: Python 3.13 (pandas 2.3.3, SciPy 1.18.1, Matplotlib 3.11.1, python-docx 1.2.0). Input counts are fetched from GEO (GSE342782); URLs are embedded in `analysis/data/raw/_download.sh`.

## Caveats

- The MTP panel in `analysis/config/mtp_panel.json` was frozen **before** data examination; any change requires a changelog entry and a version bump.
- CYR61 and CTGF are absent from the processed matrix; TRPV4/STOML3/LOX/MMP9 are below detection in HD10 neurons — see manuscript §3.1.
- The PHN-exosome contrast is exploratory (donor age/sex confounding, acknowledged by the original authors).
- The primary endpoint (M3, HZ-exo vs control-exo) is a **correctly-powered null** and is reported as such.
- Full bibliographic identifiers for references [1,5,7,8] are flagged in the manuscript's reference-verification note and must be inserted from verified sources at submission.
