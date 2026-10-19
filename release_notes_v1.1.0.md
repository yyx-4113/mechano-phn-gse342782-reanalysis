Layer 1 reproducibility package — v1.1.0

Prospectively specified reanalysis of GSE342782 (Niemeyer et al., Ann Neurol 2026): route-dependent, channel-class-selective transcriptional effects of varicella-zoster virus (VZV) and patient serum exosomes on ion-channel programmes in human sensory neurons (HD10.6 line).

Key changes from v1.0.0
- Exact label-permutation null: enumerates every C(n1+n2,n1) partition (no Monte-Carlo approximation, no 1/B floor), reporting two-sided empirical P and the observed difference's percentile in the null.
- Primary endpoint reframed as a bounded null: minimum detectable effect at 80% power = 0.18 log2CPM; 95% CI -0.18 to +0.08; permutation-inversion CI -0.16 to +0.06.
- "Double dissociation" replaced by a contrast-of-contrasts interaction test: HZ-serum-exosome E1-selective suppression is robust (interaction P = 0.0017); the reciprocal VZV M1-selective pattern is not supported at the interaction level (P = 0.19). Read as hypothesis-generating, not an established symmetric dissociation.
- HD10.6 identity correction: a tetracycline-regulatable v-myc immortalised embryonic dorsal root ganglion clonal line, not an iPSC-derived model and not DRG tissue.
- Honest allodynia framing: allodynia in the literature is predominantly a gain of mechanosensory function (Piezo2 gain-of-function; SCN9A loss-of-function causing congenital insensitivity to pain), so reduced electrochemical-channel expression is presented as a signalling-mode shift requiring in vivo validation, not as a transcriptomic allodynia substrate.
- Added Table 1 (detection baseline); completed references [1]–[17]; Ethics/Consent/Author-contributions/Acknowledgments statements added.

Quality gates
- Consistency gate (manuscript/gate_consistency.py): 82/82 assertions PASS, all expectations derived dynamically from artifacts (no hard-coded numbers).
- MANIFEST.json (tag v1.1.0): 30 file-level SHA-256 checksums.

Archive integrity
- SHA-256 (release_v1.1.0.zip): 2dd51a008ad7f37066c1f29dcf92ca571d41743ea252ecdc2b2d9c611ea2d0cb
- File-level SHA-256: see MANIFEST.json inside the archive.

Reproduce
1. python analysis/scripts/layer1_mechano.py   # regenerates layer1_results.json / layer1_gene_level.csv / layer1_global_de.csv
2. python manuscript/build_docx.py             # builds manuscript_v1.1.0.docx
3. python manuscript/gate_consistency.py       # 82-assertion consistency check -> gate_consistency_report.txt
4. python analysis/scripts/make_manifest.py    # regenerates MANIFEST.json

Note: .github/workflows/release.yml is included in the archive but is intentionally not committed to the repository, because the current gh token lacks the 'workflow' OAuth scope required to push workflow files. Releases are created manually with `gh release create`; enabling Actions later requires a token with workflow scope or a web-UI addition.
