# Author Verification Statement

**Manuscript:** Route-dependent transcriptional effects of VZV and patient serum
exosomes on ion-channel programmes in human sensory neurons: a pre-registered
reanalysis of GSE342782

**Author:** Yongxin Yang (ORCID 0009-0004-9698-6552)

**Date:** 2026-10-19

I, the sole author, confirm the following:

1. **Data provenance.** All analyses derive from the publicly available dataset
   GSE342782 (Niemeyer et al., *Annals of Neurology*, 2026; DOI 10.1002/ana.78352).
   The raw processed count matrices were downloaded from the NCBI GEO FTP server
   and verified by gzip integrity check. No data were fabricated or simulated.

2. **Reproducibility.** Every quantitative claim in the manuscript is regenerated
   from the raw GEO files by the scripts in `analysis/scripts/` (Python 3.13,
   pandas / scipy / matplotlib). The frozen mechano-transduction panel is in
   `analysis/config/mtp_panel.json` (tag `mtp-frozen-2026-10-19`).

3. **Independent recomputation.** A consistency gate (`manuscript/gate_consistency.py`)
   verifies key statistics against the result JSON and independently recomputes
   gene-level values from the raw counts. All 74 assertions pass. The gate caught
   and the manuscript corrected three numeric inaccuracies before submission.

4. **Integrity.** I have not manipulated results to achieve significance. The
   pre-registered primary endpoint (M3 ECM–Hippo module score, HZ-exo vs
   control-exo) was a correctly powered **null** (permutation P = 0.416) and is
   reported as such. No causal or therapeutic claim is made; the study is
   explicitly hypothesis-generating.

5. **Data availability.** The full reproducibility package is deposited at
   https://github.com/yyx-4113/mechano-phn-gse342782-reanalysis (tag v1.0.0),
   with SHA-256 checksums in `MANIFEST.json`.
