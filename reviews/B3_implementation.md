# B3 — Implementation / Provenance / Reproducibility Review

**Manuscript:** `manuscript/manuscript_v1.1.5.md` (+ `.docx`) — "Route-dependent transcriptional effects of varicella-zoster virus and patient serum exosomes on ion-channel programs in human sensory neurons: a prospectively specified reanalysis of GSE342782"
**Venue:** Journal of Pain Research (Dove Press), Original Research
**Reviewer:** B3 (implementation / provenance / reproducibility), reviewing as a first submission
**Scope of this review:** literal re-execution of the deposited pipeline from the raw GEO files, artifact-vs-artifact diffing, MANIFEST integrity, docx fidelity, script-vs-Methods audit, gate honesty, and verification of every quoted byte size, group size, detection fraction and headline number. Statistical design, biological interpretation and journal fit are covered by other panel members and are not re-litigated here except where they bear on traceability.

**Bottom line up front:** the computational core of this submission is the strongest I have audited. Every deposited result file — including the SHA-256 MANIFEST, both gate reports and all five figure PNGs — regenerates **byte-identically** from the raw GEO counts with the deposited scripts, and every headline number I recomputed matched the manuscript exactly. The defects I found are all in the *provenance wrapper and citation layer*: a stale repository tag that makes the central "regenerates every number" claim practically false for a reader, a results-directory MANIFEST that does not cover two artifacts the manuscript leans on, and five reference errors (one protocol cited as efficacy evidence, one dead URL, two wrong bibliographic records). None requires reanalysis; all are local fixes. Verdict: **Minor revision**.

---

## 1. Problems (four-part contract)

### P1. The Data availability statement cites repository tag v1.1.4, a package that cannot reproduce this manuscript's numbers

【Problem】The manuscript's reproducibility claim is anchored to tag `v1.1.4`, but the v1.1.4 package predates the v1.1.5 manuscript and does not contain the normalization-robustness script or its output that §2.3 explicitly relies on.

【Evidence】`manuscript_v1.1.5.md:146`: "Reproducibility package … (tag v1.1.4). The package regenerates every number in this manuscript from the raw GEO files." Listing the deposited release archives: `release_v1.1.4.zip` contains `manuscript/manuscript_v1.1.4.md/.docx` and **no** `layer1_norm_robustness.json` / `layer1_norm_robustness.py`; `release_v1.1.5.zip` contains `manuscript_v1.1.5.md` (43,530 bytes, identical to the reviewed file), `layer1_norm_robustness.json` (4,244 bytes) and `layer1_norm_robustness.py`. The manuscript under review is v1.1.5 and §2.3 (`manuscript_v1.1.5.md:55`) quotes three numbers that exist only in `layer1_norm_robustness.json` (E1 −0.194, P = 0.015; M3 −0.024, P = 0.64; interaction P = 0.0017). A reader who downloads the cited tag therefore cannot regenerate those numbers — or obtain the reviewed manuscript text.

【Why it matters】The single most load-bearing sentence of the submission ("The package regenerates every number in this manuscript from the raw GEO files") is literally true of the current working tree — I verified it byte-for-byte — but false of the artifact the Data availability statement points to. For a journal whose readership includes methods-scrutinous referees, a tag mismatch between manuscript version and package version is exactly the kind of provenance defect that undermines an otherwise exemplary reproducibility record, and it is trivially discoverable by any reader.

【Specific fix】Replace the Data availability sentence with (tag to be set to the release that contains exactly these files):

> Reproducibility package (analysis scripts, frozen panel `mtp-frozen-2026-10-19`, result JSON/CSV with SHA-256 MANIFEST, all figures): https://github.com/yyx-4113/mechano-phn-gse342782-reanalysis (tag v1.1.5). The package regenerates every number in this manuscript from the raw GEO files. SHA-256 checksums for all deposited artifacts are provided in `MANIFEST.json`.

### P2. The results-directory MANIFEST does not cover two result JSONs that the manuscript cites, contradicting §2.5

【Problem】`analysis/results/layer1/MANIFEST.json` covers only 6 of the 9 result files; the two JSONs the manuscript cites by name for post hoc checks (`layer1_norm_robustness.json`, §2.3; `layer1_extra_checks.json`, source of the E1−N1 benchmark, neuronal markers and TRPV1-by-route numbers quoted in §3.3/§3.7/§4.4) are absent, as are all five figures.

【Evidence】Deposited `MANIFEST.json` lists exactly: `layer1_results.json`, `layer1_module_scores.csv`, `layer1_cci.csv`, `layer1_gene_level.csv`, `layer1_global_de.csv`, `layer1_diag.json`, plus `inputs` (DirectInf, SeraExo, panel). I verified every listed hash against disk — all 9 MATCH, no self-reference, no stale entries. But `layer1_norm_robustness.json` (4,244 B), `layer1_extra_checks.json` (7,386 B), the five `fig/*.png` and both gate reports are on disk and uncovered. `manuscript_v1.1.5.md:63` (§2.5) states: "Every result file carries a SHA-256 manifest linking it to the exact input files and the frozen panel."

【Why it matters】The q-values are properly covered (they live inside `layer1_results.json` and `layer1_gene_level.csv`, both manifested and produced by the deposited `layer1_mechano.py`), so the primary-endpoint chain is intact. But the sentence "every result file carries a SHA-256 manifest" is inaccurate as written, and the two uncovered JSONs are precisely the ones carrying the manuscript's most decision-relevant post hoc numbers (E1−N1 = −0.064, P = 0.178; ATF3; MoR robustness). A provenance auditor cannot verify those files' integrity from the results directory alone.

【Specific fix】Regenerate the inner manifest so it covers every deposited result file (explicit spec: after running `layer1_diag.py`, `layer1_mechano.py`, `layer1_extra_checks.py`, `layer1_norm_robustness.py`, `fig_extra.py`, `fig_layer1.py`, compute SHA-256 over `layer1_results.json`, `layer1_module_scores.csv`, `layer1_cci.csv`, `layer1_gene_level.csv`, `layer1_global_de.csv`, `layer1_diag.json`, `layer1_extra_checks.json`, `layer1_norm_robustness.json`, `fig/fig1_design.png`, `fig/fig2a_module_scores.png`, `fig/fig2b_cci.png`, `fig/fig2c_E1_genes.png`, `fig/fig2d_dissociation.png`, and the three input/panel files; write to `MANIFEST.json` in the same directory). If instead the repository-root `MANIFEST.json` is intended to be the single integrity record, amend §2.5 to say so, e.g.: "Every deposited artifact carries a SHA-256 checksum in the repository-root `MANIFEST.json`; the results-directory `MANIFEST.json` additionally binds the Layer-1 result files to the exact input files and the frozen panel."

### P3. Reference [9] is a trial protocol with no results, yet is cited as evidence that ESWT "has shown benefit"

【Problem】A study protocol is cited alongside outcome-reporting trials as evidence of clinical benefit.

【Evidence】`manuscript_v1.1.5.md:35` (Introduction): "extracorporeal shockwave therapy (ESWT) … has shown benefit in small herpetic-neuralgia trials^4,7–9^"; `manuscript_v1.1.5.md:126` (§4.3): "ESWT has shown benefit in herpetic neuralgia in small trials,^4,7–9^". Reference [9] (`manuscript_v1.1.5.md:190`) is Chen L, Zhou R, Sun F, et al. *Trials*. 2020;21:573 — verified via PubMed (PMID 32641142, DOI 10.1186/s13063-020-04564-z): publication type "Clinical Trial Protocol", abstract describes a trial that "will evaluate" efficacy; it reports no outcomes. (Its results paper is reference [7], Chen et al. *Front Neurol* 2022, which the manuscript already cites and accurately characterizes, including the absent time-by-group interaction.)

【Why it matters】Citing a protocol as demonstrated benefit overstates the clinical evidence base in both the Introduction and the Discussion. Referees and readers checking reference [9] will find a SPIRIT protocol, which reads as citation padding in a manuscript that is otherwise scrupulous about disclosure.

【Specific fix】In both locations, drop [9] from the benefit claim, e.g. for line 35: "…has shown benefit in small herpetic-neuralgia trials^4,7,8^ (although the largest randomized trial reported pain reduction without a significant time-by-group interaction)^7^…" and for line 126: "…and ESWT has shown benefit in herpetic neuralgia in small trials,^4,7,8^ although the largest randomized trial reported pain reduction without a significant time-by-group interaction.^7^" Reference [9] may be retained in the list if it is cited elsewhere as a registered protocol (e.g., ChiCTR1900025828), or removed if not.

### P4. Reference [12] contains a dead GEO URL (wrong series directory)

【Problem】The FTP URL for GSE314229 in reference [12] returns HTTP 404.

【Evidence】`manuscript_v1.1.5.md:196`: "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE31nnn/GSE314229/ (accessed October 19, 2026)". Fetching that URL returns "Object not found" (Apache 404). The correct GEO series directory for accession GSE314229 is `GSE314nnn`; `https://ftp.ncbi.nlm.nih.gov/geo/series/GSE314nnn/GSE314229/` resolves and serves the series (matrix/, miniml/, soft/, suppl/). The manuscript's own Data availability URL for GSE342782 uses the correct `GSE342nnn` pattern, so the error is isolated to [12].

【Why it matters】A dead data link in a reproducibility-focused submission is a direct traceability defect: the rESWT single-cell dataset is the only evidentiary basis for §4.3's compartmental argument about shockwave mechanisms.

【Specific fix】Replace the URL in reference [12] with `https://ftp.ncbi.nlm.nih.gov/geo/series/GSE314nnn/GSE314229/` (accessed date may stay October 19, 2026).

### P5. Reference [15] has the wrong year, volume and issue

【Problem】The Murthy et al. Piezo2 mechanical-pain paper is cited with an incorrect year/volume/issue.

【Evidence】`manuscript_v1.1.5.md:202`: "Murthy SE, Loud MC, Daou I, et al. The mechanosensitive ion channel Piezo2 mediates sensitivity to mechanical pain in mice. Sci Transl Med. 2019;11(486):eaat9897." Verified against Crossref (DOI 10.1126/scitranslmed.aat9897) and PubMed (PMID 30305457): *Sci Transl Med*. **2018** Oct 10;**10**(462):eaat9897. Title, authors and article number are correct; year, volume and issue are wrong.

【Why it matters】Reference [15] supports a central interpretive claim in §4.1 (Piezo2 requirement for mechanical pain). A bibliographic error in a load-bearing citation is minor in isolation but, in a package that advertises checksum-level rigor, erodes confidence in the citation layer as a whole.

【Specific fix】Replace reference [15] with: "[15] Murthy SE, Loud MC, Daou I, et al. The mechanosensitive ion channel Piezo2 mediates sensitivity to mechanical pain in mice. Sci Transl Med. 2018;10(462):eaat9897. doi:10.1126/scitranslmed.aat9897. PMID: 30305457."

### P6. Reference [21] has the wrong final two authors

【Problem】The author list of the human DRG single-nucleus reference does not match the published record.

【Evidence】`manuscript_v1.1.5.md:214`: "Nguyen MQ, von Buchholtz LJ, Reker AN, **Rycroft KM, Ma J**. Single-nucleus transcriptomic analysis of human dorsal root ganglion neurons. Elife. 2021;10:e71752." Verified against Crossref (DOI 10.7554/eLife.71752) and PubMed (PMID 34825887): the author list is Nguyen MQ, von Buchholtz LJ, Reker AN, **Ryba NJP, Davidson S**. Title, journal, year, volume and article number are correct.

【Why it matters】Reference [21] anchors the §4.4 limitation that PIEZO2 is widely expressed across adult human DRG neuronal classes — a correction the authors already made once. Getting the author list wrong on the very reference used to support a corrected claim invites avoidable referee comment.

【Specific fix】Replace reference [21] with: "[21] Nguyen MQ, von Buchholtz LJ, Reker AN, Ryba NJP, Davidson S. Single-nucleus transcriptomic analysis of human dorsal root ganglion neurons. Elife. 2021;10:e71752. doi:10.7554/eLife.71752. PMID: 34825887."

### P7. The gates are honest but cover only part of the manuscript's numeric claims; ~20 quoted numbers are asserted by no automated check

【Problem】Both gates pass and their expected values are derived from artifacts (not hardcoded), but a substantial set of manuscript numbers — including every Table 1 detection fraction and several §3.x P values — is asserted nowhere, so the "every number traceable" discipline is only partially enforced.

【Evidence】I ran both gates from `manuscript/`: `gate_consistency.py` → 137 assertions, 137 PASS, 0 FAIL; `gate_jpr_compliance.py` → 30 checks, 30 PASS, 0 FAIL; both reports regenerate byte-identically. Reading `gate_consistency.py`, all expected values are pulled from `layer1_results.json`, `layer1_diag.json`, `layer1_gene_level.csv`, `layer1_global_de.csv`, `layer1_extra_checks.json`, `layer1_norm_robustness.json`, plus one genuinely independent recompute of the primary M3 permutation P from the raw counts — no hardcoded results. However, the following quoted numbers appear in no gate assertion: byte sizes 622,501 / 884,411 (§2.1); module coverage 9/9, 20/20, 25/25, 18/18 (§2.2); "138 RPL/RPS genes" (§2.3); "43,236 matrix genes" (§2.4); all Table 1 rows for PIEZO1, ITGB1(SeraExo), SCN10A(DirectInf), SCN9A, TRPV1, TAC1 and all ten detected fractions (§3.1); M4 under HZ exosomes P = 0.46 (§3.2); the six M3 gene-level values COL4A1/COL4A2/ADAMTS1/TEAD1/LOX/YAP1 (§3.2); E1 Welch P = 0.011, PIEZO1 P = 0.10, P2RX3 P = 0.076, SCN10A P = 0.008 (§3.3); the "4/9 vs 5/18 below detection" counts and the Bonferroni P = 0.0034 (§3.4); OR5A1 32% detection and the KCNQ3/KCNQ2 within-N1 q values 0.500/0.564 (§3.6); NTRK1/PRPH/NEFL values and "no marker survived BH" (§3.7); the five software versions (§2.5). I recomputed every one of these myself from the raw files and artifacts — all correct (values in §"What I actually checked").

【Why it matters】Nothing in the manuscript is currently wrong, but the gate gives false assurance about the unchecked remainder: any future typo in, e.g., a Table 1 fraction or a §3.2 gene-level P would pass both gates silently. Since the authors have already built the machinery, extending it is cheap and converts a partial check into the comprehensive one the Data availability language implies.

【Specific fix】Extend `gate_consistency.py` with assertions for the enumerated items, e.g.: Table 1 — `numchk("PIEZO1 DI CPM", "2.64", w0["PIEZO1"]["DirectInf"]["mean_cpm"])` and analogous rows for ITGB1/SeraExo, SCN10A/DirectInf, SCN9A (both experiments), TRPV1 (both), TAC1/SeraExo, plus detected fractions via `w0[gene][experiment]["detect_frac_cpm1"]`; coverage — derive from `panel_missing` (assert `len(panel_missing[m]) == expected_missing` for each module); "138" — `NR["ribosomal_gene_share_pct"]["n_ribosomal_genes"]`; "43,236" — `GD["n_genes"]`; M4-HZ P — `mod("HZexo_vs_CtrlExo","M4_mechano_effectors")["p_perm_exact"]`; the six M3 genes — `gv(gene,"HZexo_vs_CtrlExo","log2FC")` / `"welch_p"` from the gene CSV; E1 Welch P — `e1["p_ttest"]`; PIEZO1/P2RX3/SCN10A — `gv(...)`; detection-floor counts — `interaction_detected_only` n_E1/n_M1 vs module totals; KCNQ3/KCNQ2 within-N1 q — `gv(..., module="N1_voltage_gated_control")`; NTRK1/PRPH/NEFL — `X["neuronal_integrity_markers"]["genes"][g]`; "no marker survived" — `claim_ge` on the minimum marker q.

### P8. Four of the eight pipeline scripts are bound to the author's absolute Windows paths (one also hardcodes sample names and carries dead code), so the package does not regenerate from raw on any other machine

【Problem】The "regenerates from raw" claim holds only on the author's machine for part of the pipeline; three scripts plus both figure scripts resolve paths absolutely, and the diagnostic script hardcodes the 19 SeraExo column names.

【Evidence】`layer1_mechano.py:32-36`, `layer1_extra_checks.py:26-29` and `layer1_norm_robustness.py:26-30` correctly derive paths from `__file__`. In contrast: `layer1_diag.py:9-11` hardcodes `RAW/CFG/OUT = "D:/2026.10/机械应力/..."`; `layer1_diag.py:44` hardcodes the column order `["C11","C15","C18","C2","C20","C21","C5","P1","P10","P4","P7","P9","S17","S24","S27","S34","S44","S45","S62"]`; `fig_layer1.py:11`, `fig_extra.py:11` and `verify_interaction.py:13` hardcode the same absolute results path. Additionally `layer1_diag.py:15-25` defines a `load_counts` helper that would raise FileNotFoundError if ever called (it reads `path.replace('.gz','')`), and is dead code. I confirmed the hardcoded column order happens to match the current file header exactly, so the deposited outputs are correct — the issue is fragility, not error.

【Why it matters】On any other machine (or after any GEO file refresh that renames/reorders columns), `layer1_diag.py` writes to a non-existent directory and the figure scripts fail; a user cannot reproduce `layer1_diag.json` or the figures without hand-editing paths. Since the inner MANIFEST includes `layer1_diag.json`, the chain is only reproducible in situ.

【Specific fix】Make all scripts location-independent with the same pattern already used in `layer1_mechano.py`, e.g. at the top of `layer1_diag.py`, `fig_layer1.py`, `fig_extra.py`, `verify_interaction.py`: `from pathlib import Path; _ROOT = Path(__file__).resolve().parents[2]; RAW = _ROOT / "analysis" / "data" / "raw"; OUT = _ROOT / "analysis" / "results" / "layer1"` (for figure scripts, `_ROOT = Path(__file__).resolve().parents[1]`). In `layer1_diag.py`, replace the hardcoded column assignment with `se.columns = list(pd.read_csv(gzip.open(path), nrows=0).columns[1:])` read from the file header, and delete the dead `load_counts` function at lines 15-25.

### P9. Methods does not describe how the minimum detectable effect, the two confidence intervals, or the permutation percentile were computed

【Problem】Three reported quantities (MDE at 80% power, Welch and permutation-inversion 95% CIs, null percentile) appear in §3 and in the artifacts but nowhere in the Methods, so a reader cannot reproduce 0.18 log2CPM without reading code.

【Evidence】`manuscript_v1.1.5.md:59` (§2.4) describes Welch t, Mann-Whitney U, exact permutation enumeration and BH only. The MDE is computed in `layer1_mechano.py:109-119` as a non-central-t (equal-variance, pooled-SD) 80%-power minimum detectable difference — note this is an equal-variance approximation sitting inside an otherwise Welch-based analysis — and the CIs at `layer1_mechano.py:121-145` (permutation inversion: [D − q97.5, D − q2.5] of the exact null; Welch Satterthwaite). The percentile statistic (`perm_percentile`, reported as `perm_pct` in `layer1_module_scores.csv`) is computed at `layer1_mechano.py:106` but never defined or used in the text.

【Why it matters】The bounded-null argument (MDE 0.18 log2CPM vs observed −0.049) is the paper's headline interpretive device for the primary endpoint; its computation deserves a Methods sentence, and the equal-variance approximation behind it should be stated rather than left implicit.

【Specific fix】Add to §2.4: "The minimum detectable effect at 80% power (two-sided α = 0.05) was computed from the pooled within-group standard deviation of the per-sample module scores under an equal-variance normal approximation with a non-central t distribution. Confidence intervals for module-score differences are reported both as Welch (Satterthwaite) intervals and as permutation-inversion intervals, [D − q0.975, D − q0.025] of the exact permutation null, and the observed difference's percentile within the null distribution is reported alongside the two-sided empirical P value."

### P10. §2.2 says the M-modules were "fully represented" and then immediately lists 56/58 for M3 in the same parenthetical

【Problem】An internal contradiction in one sentence: "fully represented" is asserted for a set whose own parenthetical includes 56/58.

【Evidence】`manuscript_v1.1.5.md:49`: "Module coverage after matching against the count matrix: M1-M4 and E1-N1 were fully represented (9/9, 20/20, 56/58, 25/25, 18/18, 17/17 genes); M3 lacked CYR61 and CTGF (56/58); N2 lacked OR6A1, OR10A1, OR13C1 (13/16); N3 lacked RPS4 (17/18; an RPS4X ortholog was present)." The underlying numbers are all correct (I verified panel membership against the count matrices: exactly CYR61/CTGF, OR6A1/OR10A1/OR13C1 and RPS4 absent; RPS4X, CCN1, CCN2 present). Only the word "fully" is wrong for M3.

【Why it matters】Cosmetic, but in a sentence whose whole purpose is precise coverage accounting; a careful referee will stop on it.

【Specific fix】Replace the clause with: "Module coverage after matching against the count matrix: M1, M2, M4, E1 and N1 were fully represented (9/9, 20/20, 25/25, 18/18 and 17/17 genes respectively); M3 was represented by 56 of 58 genes (CYR61 and CTGF absent; the CCN1/CCN2 orthologs were present and used in an alias sensitivity analysis); N2 by 13 of 16 (OR6A1, OR10A1, OR13C1 absent); N3 by 17 of 18 (RPS4 absent; an RPS4X ortholog was present)."

### P11. The structured abstract is exactly at the 300-word limit

【Problem】The abstract contains exactly 300 words — the Journal's maximum — leaving zero margin for any editorial expansion.

【Evidence】`manuscript_v1.1.5.md:17-27`; word count of the abstract block excluding the Keywords line = 300 (limit 300). The compliance gate reports "abstract <= 300 words (actual 300)".

【Why it matters】Any copyedit insertion, or any future revision sentence, breaks a hard journal requirement and forces another compliance cycle.

【Specific fix】Trim ~15 words for margin, e.g. in the Background: "GSE342782 — RNA-sequencing of human sensory neurons exposed to varicella-zoster virus (VZV) or to serum exosomes from controls, acute herpes zoster (HZ) and PHN patients — permits a test." → "RNA-sequencing of human sensory neurons exposed to varicella-zoster virus (VZV) or to serum exosomes from controls, acute herpes zoster (HZ) and PHN patients (GSE342782) permits a test." (and similarly tighten one Results clause), targeting ≤ 285 words.

### P12. The v1.1.5 release package ships the superseded manuscript version alongside the current one

【Problem】The reproducibility archive for this submission contains `manuscript_v1.1.4.docx` (396,128 bytes) next to `manuscript_v1.1.5.docx/.md`.

【Evidence】Listing of `release_v1.1.5.zip`: `manuscript/manuscript_v1.1.4.docx` (2026-10-19 23:53) and `manuscript/manuscript_v1.1.5.docx` (2026-10-20 00:26) both present; `manuscript/archive/` is excluded from packaging, so the v1.1.4 files in `manuscript/` are what leak in.

【Why it matters】Minor hygiene: a first-submission package containing two manuscript versions invites confusion about which is under review, and slightly bloats the archive.

【Specific fix】Before tagging the release for this submission, move `manuscript_v1.1.4.docx` (and any other superseded version) into `manuscript/archive/` (already excluded by the packaging step) and regenerate the tag.

---

## 2. Stands up (verified correct — do not change)

**S1. The pipeline regenerates every deposited artifact byte-for-byte from the raw GEO files.** I copied `analysis/` to an isolated scratch tree, deleted the scratch results, and re-ran all scripts from the raw `.csv.gz` inputs. SHA-256 comparison, regenerated vs deposited: `layer1_results.json` e579dc0c…, `layer1_module_scores.csv` db877136…, `layer1_cci.csv` b3a64875…, `layer1_gene_level.csv` 3310b276…, `layer1_global_de.csv` 8f9d58b9…, `layer1_diag.json` 27d4d99e…, `layer1_extra_checks.json` 28a888c0…, `layer1_norm_robustness.json` fb9bee54…, `MANIFEST.json` 2faedf58…, both gate reports, and all five figure PNGs — **all identical**. No tracked file in the repository was modified by the re-run.

**S2. The exact-permutation implementation matches the Methods text exactly.** `layer1_mechano.py:88-107` enumerates all C(n₁+n₂, n₁) label partitions via `itertools.combinations` — no Monte-Carlo, no 1/B floor — with n = 3432 (7v7), 792 (5v7), 924 (6v6) confirmed in the outputs. The minimum achievable two-sided P is respected: the PHN N3 value is 0.0012626… = exactly 1/792, the smallest attainable for that design, so no floor violation exists anywhere in the results.

**S3. Group assignment by column prefix is correct against the series metadata.** The SeraExo header is `C11,C15,C18,C2,C20,C21,C5,P1,P10,P4,P7,P9,S17,S24,S27,S34,S44,S45,S62`; the series matrix library names and sample titles (control sera EV replicates 1-7, PHN sera EV 1-5, acute zoster sera EV 1-7) map one-to-one onto the C/P/S prefixes, matching the manuscript's "7/5/7" (§2.1) and the code's `startswith` mapping (`layer1_mechano.py:175-181`). DirectInf is 6 mock / 6 VZV, matching "mockInf*"/"vzvInf*" columns and the series titles.

**S4. BH is applied exactly as described — across the eight modules within each contrast, on the exact permutation P values** (`layer1_mechano.py:277-284`; e.g., HZ contrast: E1 q = 0.0342, N3 q = 0.0140, M3 q = 0.4615 — all reproduced). Gene-level within-module BH is computed per (contrast, module) family and written one row per gene-module membership, so the shared KCNQ2/KCNQ3 genes carry family-specific q values (E1: 0.3655/0.4970; N1: 0.5004/0.5636) and are not overwritten — matching §3.6's quoted 0.366/0.500/0.497/0.564 exactly.

**S5. The MANIFEST that exists is honest.** All nine listed hashes (six results + DirectInf input + SeraExo input + frozen panel) match disk; there is no self-reference and no stale entry. The panel hash binds the results to `mtp-frozen-2026-10-19`, whose content I read and confirmed matches the §2.2 gene lists (M1 9, M2 20, M3 58, M4 25, E1 18, N1 17, N2 16, N3 18 genes).

**S6. docx fidelity is complete.** The docx embeds exactly five images whose bytes are identical to the five deposited PNGs; Table 1 renders as one 11×5 table whose 50 cells match the md verbatim; all five figure captions are present; every figure is called out in text twice (caption + in-text); continuous line numbering (`w:lnNumType countBy=1 start=1`) and a footer `PAGE` field are present; extracted docx text matches the md for every body paragraph I diffed (abstract, all §2-§5 paragraphs, Data availability, limitations, references), including the sentences with numbers.

**S7. The gates' expected values are derived, not hardcoded.** Every asserted value in `gate_consistency.py` is read from the deposited artifacts, and the primary endpoint is additionally recomputed independently from the raw counts inside the gate. Pass counts reproduce exactly (137/137; 30/30). The only hardcoded quantities are inequality thresholds (0.82, 0.05, 0.20, 0.40, 1.61), which are claim bounds, not results.

**S8. The median-of-ratios robustness check is methodologically sound.** `layer1_norm_robustness.py` avoids the two classic traps (it documents both in comments): CPM scale-invariance is handled by comparing library-size-CPM vs MoR-normalized-CPM at matched scale, and the size factors are rescaled to CPM magnitude before the log2(1+·) offset so the pseudocount does not distort low-expressed genes. The quoted MoR results (E1 −0.194, P = 0.015; M3 −0.024, P = 0.64; interaction P = 0.0017) regenerate exactly.

**S9. Reference integrity is high.** Of 21 references, I verified 16 against PubMed/Crossref with exact agreement on authors, title, journal, year, volume/issue/pages, DOI and PMID: [1], [2], [3] (the source study, including its "canonical nociceptive ion channels downregulated, substance P upregulated" finding that the manuscript accurately paraphrases), [4], [5], [6], [7], [8], [10], [11], [13], [14], [16], [18], [19], [20]. The five defects are itemized in P3-P6 and are localized.

**S10. The raw-data hygiene claims check out.** gzip integrity passes for all three files; byte sizes are exactly 622,501 and 884,411 as quoted (§2.1); both matrices contain 43,236 gene rows with zero unparseable rows, zero duplicate symbols and no negative counts; the deposited series matrix contains no donor age/sex fields (only "cell line: HD10"), corroborating §3.5's statement that the confounding cannot be quantified from public data.

---

## 3. Questions for the authors

1. Protocol v0.4: where is it publicly deposited, and what is its deposit timestamp relative to the first data download? Under this review's independence rules I did not open the protocol file, so the "deposited before data examination" claim (Abstract, Registration) is not independently verifiable from the materials I was permitted to examine. A citable registry entry or repository commit hash would settle it.
2. Was the median-of-ratios robustness analysis (§2.3) part of protocol v0.4, or is it post hoc like the E1-vs-N1 benchmark and neuronal-integrity panel (both labeled post hoc in their artifacts)? §2.3 currently reads as if pre-specified; if it was added later, say so in one clause.
3. Which repository tag should readers cite for this submission — v1.1.5, or a new tag to be cut after the fixes in this report?
4. The MDE uses an equal-variance pooled-SD approximation while all inference is Welch. Was this deliberate (and should the text say so, per P9), or would you prefer a Welch-based power calculation?
5. §3.4 states sub-threshold genes contribute "≈0" to module means; precisely, they contribute log2(1+CPM) ∈ (0,1) — e.g., TRPV4 averages ≈0.25 in SeraExo versus 5-9 for detected genes. Confirm the wording is intended as an approximation (the dilution argument is unaffected).
6. Is the N2 calibration claim ("the signal rests on a single low-baseline gene, OR5A1") supported by any quantitative driver analysis (e.g., leave-one-gene-out of the 13-gene module), or is it qualitative? If quantitative, please deposit it; if qualitative, the sentence is fine as interpretation.
7. Do you intend the results-directory `MANIFEST.json` or the repository-root `MANIFEST.json` to be the canonical integrity record (see P2)? The manuscript currently implies both.

---

## 4. What I actually checked

**Manuscript.** Read in full (214 lines, including all figure/table callouts, Data availability, Ethics, Declarations, all 21 references), using line-folded reads for the long single-line paragraphs.

**Full pipeline re-run from raw.** Copied `analysis/` to an isolated scratch tree (scratch raw/config verified byte-identical to the deposited inputs), cleared the scratch results directory, and executed, in dependency order: `layer1_diag.py`, `layer1_mechano.py`, `layer1_extra_checks.py`, `layer1_norm_robustness.py`, `fig_extra.py`, `fig_layer1.py`, `verify_interaction.py`. Diffed every regenerated JSON/CSV/MANIFEST/gate-report/PNG against the deposited files: **all byte-identical (SHA-256 table in S1)**. The claim "the package regenerates every number in this manuscript from the raw GEO files" is therefore literally true of the working tree — the defect is the cited tag (P1).

**MANIFEST integrity.** Verified all SHA-256 entries in `analysis/results/layer1/MANIFEST.json` against disk: 6/6 result files MATCH, 3/3 inputs MATCH (including the frozen panel hash). No stale entries, no missing listed files, no self-reference. Uncovered on-disk files: `layer1_norm_robustness.json`, `layer1_extra_checks.json`, five `fig/*.png`, two gate reports (P2).

**Headline numbers recomputed from raw (manuscript value → my value, all identical):** M3 −0.049 / P = 0.42 / q = 0.46 / Welch CI −0.18…+0.08 / perm CI −0.16…+0.06 / MDE 0.18 (→ −0.0489, 0.4219, 0.4615, [−0.1764, 0.0787], [−0.1593, 0.0616], 0.1786); E1 −0.220 / P = 0.013 / Welch P = 0.011 / q = 0.034 / CI −0.38…−0.06 (→ −0.2196, 0.0128, 0.0111, 0.0342, [−0.3768, −0.0625]); M1 −0.078 / P = 0.11 (→ −0.0780, 0.1131); interaction −0.142 / P = 0.0017 (→ −0.1417, 0.001748); detected-gene interaction −0.072 / P = 0.16 (→ −0.0718, 0.1573, nE1 = 13, nM1 = 5); detected-gene M1 −0.171 / P = 0.046 (→ −0.1709, 0.0460); CCI all P ≥ 0.82 (→ min 0.8328; rank space 43,236 genes); N2 −0.022 / P = 0.006 / q = 0.023; N3 +0.391 / P = 0.002 (→ +0.3914, 0.001748); PHN contrast M1 −0.119/0.009/0.024, E1 −0.197/0.005/0.020, M2 −0.178/0.030, N1 −0.198/0.039, N3 +0.577/0.001/0.010; VZV contrast M1 −0.050/P = 0.05/Welch 0.047, M4 −0.054/P = 0.03, M3 P = 0.85, PHN M3 P = 0.83, M4-HZ P = 0.46; gene-level (HZ vs ctrl): TRPV1 −0.567/P = 0.0009/q = 0.017, KCNS1 −0.393/0.017/q = 0.069, SCN9A −0.323/0.018/q = 0.069, ASIC1 −0.181/0.019/q = 0.069, ASIC2 −0.296/0.042/q = 0.127, SCN10A −0.384/0.008/q = 0.068, PIEZO2 −0.282/P = 0.18/CI −0.72…+0.15, PIEZO1 P = 0.10, P2RX3 P = 0.076; M3 genes COL4A1 −0.381/0.005, COL4A2 −0.627/0.007, ADAMTS1 −0.479/0.013, TEAD1 −0.339/0.047, LOX +0.291/0.024, YAP1 +0.425/0.18; Table 1 (all 10 genes × 4 columns, e.g., PIEZO2 245.2/1.00/164.1/1.00, P2RX3 806.8/1.00/470.6/1.00, TRPV4 0.25/0.00/0.19/0.00, STOML3 0.01/0.00/0.00/0.00, SCN10A 7.23/1.00/0.55/0.11); baselines SCN9A 8.31 (all-12) / 8.39 (mock-only), TRPV1 6.94 / 7.02; OR5A1 0.89 CPM / 32% detected; neuronal markers ATF3 +0.0002/P = 0.998, NEFH −0.221/0.006, TUBB3 −0.183/0.012, NTRK1 −0.202/0.031, PRPH −0.128/0.048, NEFL −0.111/0.053, none surviving BH across the ten-gene panel (min q among nominally significant = 0.06); E1−N1 = −0.064/P = 0.178 and N1 −0.156/P = 0.151; ribosomal share 138 genes, 3.233% → 4.217%; MoR robustness E1 −0.1942/P = 0.0152, M3 −0.0236/P = 0.6428, interaction −0.136/P = 0.0017; global DE 129 up/174 down (HZ) and 568/125 (PHN) at |log2FC| > 0.5 over 43,236 genes; per-sample mean log2CPM range 1.553-1.605 (claimed 1.55-1.61); software versions Python 3.14.5, NumPy 2.5.1, pandas 3.0.5, SciPy 1.18.0, Matplotlib 3.11.1 — all exact.

**Raw inputs.** `gzip -t` passes on all three files; sizes 622,501 / 884,411 / 3,563 bytes; 43,236 gene rows per matrix, 0 skipped, 0 duplicates, all counts ≥ 0; series matrix: 31 samples (6 mock, 6 VZV, 7 control-EV, 5 PHN-EV, 7 HZ-EV), library names match count-matrix columns, characteristics = "cell line: HD10" only (no age/sex), MOI 0.003, harvest 4 dpi, exosome exposure 36 h, GPL24676, BioProject PRJNA1508885.

**Script-vs-text audit (Methods §2.2-2.5 vs code).** CPM = column-sum scaling ×10⁶ ✓; log2(1+CPM) applied uniformly ✓; module score = mean of log2(1+CPM) over present panel genes ✓; detection = CPM > 1 ✓; group prefixes C/P/S and mock/vzv ✓ (cross-checked against series metadata); exact enumeration of all partitions, no MC, no floor ✓; BH across exactly 8 modules per contrast on exact permutation P ✓; CCI = per-sample mean rank of M1 minus E1 across all 43,236 genes, same permutation scheme ✓ (rank direction matches "mean expression rank" wording); gene-level Welch t on log2(1+CPM) with within-module BH (q_within_module) ✓; the only deviations are the dead `module_score` helper and dead `load_counts` (P8), and the equal-variance MDE sitting inside a Welch framework (P9).

**Gate honesty.** Ran both gates from `manuscript/`: 137/137 and 30/30; reports regenerate byte-identically. Confirmed expected values are artifact-derived (no hardcoded results) and enumerated the ~20 quoted numbers no gate asserts (P7), each of which I verified manually (values above).

**docx.** Unpacked and inspected: 5 media images (bytes identical to deposited PNGs), 1 table (11×5 = Table 1, values identical to md), 5 figure captions, each figure called out twice, `w:lnNumType` continuous line numbering, footer `fldSimple w:instr="PAGE"`; extracted full text and diffed against the md — every body paragraph present and matching (three apparent mismatches were bullet-prefix artifacts of the builder and confirmed present).

**Release packages.** Listed the contents of `release_v1.1.4.zip` and `release_v1.1.5.zip` (file names only): v1.1.4 lacks the norm-robustness artifacts and ships the v1.1.4 manuscript (P1, P12); v1.1.5 contains the reviewed manuscript and artifacts.

**References.** Verified 16/21 exactly against PubMed/Crossref (PMIDs/DOIs as listed); defects at [9] (protocol cited as benefit evidence — verified publication type "Clinical Trial Protocol"), [12] (404 URL; correct directory GSE314nnn verified live), [15] (2019;11(486) → 2018;10(462), verified via Crossref), [21] (author list tail "Rycroft KM, Ma J" → "Ryba NJP, Davidson S", verified via Crossref and PubMed).

**Independence.** I did not open anything under `reviews/` except the panel brief, nor release notes, README, protocol, deposit SOP, verification statement, CITATION.cff, the root MANIFEST, `manuscript/archive/`, or `.workbuddy/`. During the review window an untracked file `analysis/scripts/_b1_recompute.py` appeared in the working tree (not part of any MANIFEST I could see); I did not open it and used nothing from it. My re-run modified no tracked file.

---

## 5. Must-fix list (ordered by severity)

1. **P1** — Update the Data availability tag from v1.1.4 to the release that contains this manuscript and all cited artifacts (paste-ready sentence provided); the "regenerates every number" claim is otherwise broken for every reader who follows the link.
2. **P2** — Cover all deposited result files (including `layer1_norm_robustness.json` and `layer1_extra_checks.json`) in the results-directory MANIFEST, or correct §2.5 to point at the repository-root MANIFEST; the two uncovered JSONs carry the manuscript's most decision-relevant post hoc numbers.
3. **P3** — Remove reference [9] (a protocol with no results) from the two "ESWT has shown benefit" sentences; keep the accurate [7] characterization.
4. **P4** — Fix the dead GSE314229 URL in reference [12] (`GSE31nnn` → `GSE314nnn`).
5. **P5** — Correct reference [15] to *Sci Transl Med*. 2018;10(462):eaat9897.
6. **P6** — Correct reference [21] author list to Nguyen, von Buchholtz, Reker, Ryba, Davidson.
7. **P8** — Replace absolute paths in `layer1_diag.py`, `fig_layer1.py`, `fig_extra.py`, `verify_interaction.py` with `__file__`-relative roots; read SeraExo column names from the file header instead of hardcoding; delete the dead loader.
8. **P9** — Add the MDE/CI/percentile computation to §2.4 (paste-ready sentence provided), disclosing the equal-variance approximation.
9. **P7** — Extend `gate_consistency.py` to assert the ~20 currently unchecked numbers (spec provided), so the automated check matches the manuscript's traceability language.
10. **P10** — Fix the "fully represented (…56/58…)" contradiction in §2.2 (paste-ready replacement provided).
11. **P11** — Trim the abstract below the 300-word ceiling for margin.
12. **P12** — Exclude the superseded `manuscript_v1.1.4.docx` from the submission package.

---

## 6. Verdict

**Minor revision.** The analysis itself is reproducible to the byte and every number I could check — including all Table 1 values, all q-values, and the bounded-null apparatus — regenerated exactly from the raw GEO files; what stands between this package and acceptance is a stale repository tag, an incomplete results manifest, and five citation defects, all of which are local, textual fixes that require no reanalysis.
