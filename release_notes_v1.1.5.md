# Layer 1 reanalysis v1.1.5 — JPR Round-4 final revisions (symmetric decoupling, normalization robustness, citation completeness)

Round-4 closing revision. Three reviewers (biostatistics, pain neuroscience, clinical/compliance) re-audited v1.1.4 with independent recomputation; every number below was independently re-derived before entering the manuscript.

## Scientific interpretation

- **Symmetric mRNA-function decoupling (most consequential fix).** §4.1 previously invoked mRNA-function decoupling to reconcile the E1 direction (down-regulated pro-nociceptive transcripts despite allodynic hyperexcitability) yet used the opposite standard for M1 ("PIEZO2 unchanged, therefore no mechanical axis"). The same logic is now applied to PIEZO2: transcript unchanged, but Piezo2 function is post-translationally regulated — most directly by relief of its voltage-block, sufficient to sensitize nociceptors without any expression change [18]. The M1 null now excludes only transcriptional up-regulation of the mechanogated program.
- **"fully compatible" softened** (Limitations-grade honesty): compatibility is conditional on post-translational sensitization outweighing an ~1.5-fold transcript reduction; the counter-regulatory reading remains open.
- **§3.3 heading** no longer claims "channel-class selectivity" (contradicted by the E1-vs-N1 benchmark added in v1.1.4).
- **E1-vs-N1 benchmark completed**: N1's own shift (-0.156, P = 0.151) is now reported alongside the difference (-0.064, P = 0.178) so readers can recompute the benchmark.
- **Normalization robustness as positive evidence** (`layer1_norm_robustness.json`, new): DESeq2-style median-of-ratios re-run of the primary contrast leaves every headline conclusion intact (E1 -0.194, P = 0.015; M3 -0.024, P = 0.64; interaction P = 0.0017). Implemented at matched scale — the "MoR then CPM" shortcut is a null comparison because CPM is scale-invariant (this pitfall was identified during review and avoided).
- **Model baseline corrected**: PIEZO2-high is not itself the deviation from adult DRG (PIEZO2 is widely expressed across adult human DRG classes [21]); the deviations are TRPV4/STOML3 absence and single-clone derivation.
- **PIEZO2 cross-experiment baseline** (245.2 vs 164.1 CPM, ~1.5-fold) disclosed alongside the SCN10A ~13-fold difference.

## Citation integrity (verified against PubMed/Crossref)

- New [21]: Nguyen MQ, von Buchholtz LJ, Reker AN, Rycroft KM, Ma J. Single-nucleus transcriptomic analysis of human dorsal root ganglion neurons. eLife. 2021;10:e71752. PMID 34825887 (5 authors, listed in full per Dove rule).
- All in-text citations converted to Vancouver superscript numerals placed after punctuation (author-year residue removed); [12] (GSE314229) now cited in §4.3; hyphenated "mechano-transduction" spelling unified.

## Gates and artifacts

- Consistency gate: **137/137 PASS** (new locks: symmetric decoupling, N1 component, MoR robustness, ribosomal shares, PIEZO2 baselines, spelling).
- JPR compliance gate: **30/30 PASS** (abstract exactly 300 words; 6 keywords; superscript citations; figures cited in text; correspondence block with phone/fax; line numbering + page numbers in docx).
- MANIFEST: 45 files, tag v1.1.5; release zip SHA-256 `daea2291896661874a6ba700f7ccb80c8e7a85179fa0bd5b965229bb2fd2a9af`.
