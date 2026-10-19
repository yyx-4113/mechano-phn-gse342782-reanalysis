# Reviewer B2 — Statistics / study design / causal inference

**Manuscript:** `manuscript/manuscript_v1.1.5.md` — "Route-dependent transcriptional effects of varicella-zoster virus and patient serum exosomes on ion-channel programs in human sensory neurons: a prospectively specified reanalysis of GSE342782"
**Venue:** Journal of Pain Research (Original Research)
**Reviewed as:** first submission. All judgements below come from the manuscript text, the raw GEO count matrices, the frozen panel, the pipeline scripts, and the deposited result artifacts, plus my own independent recomputation from the raw counts. No prior-round material was consulted.

---

## Summary

I independently recomputed the entire statistical core of this manuscript from the two raw count matrices (43,236 genes; 19 SeraExo samples and 12 DirectInf samples) — every module score, every exact permutation P, both confidence intervals, the MDE, all BH q values, all gene-level headline values, the MoR robustness re-analysis, the CCI, the global-shift and ribosomal diagnostics, and the DE counts. **Every number quoted in the manuscript reproduces** (agreement to 3–4 significant figures throughout; full table in § What I actually checked). The SHA-256 hashes of the raw inputs and the frozen panel match the deposited MANIFEST, so the reproducibility chain is intact. This is an unusually clean numerical submission.

The problems are therefore interpretive and design-level, and they concentrate in the neutral-control logic:

1. The CCI "null-by-construction" interpretation (§3.6) is not supported by the data. The CCI null is produced by cancellation between a real E1 rank displacement and a detection-floor-driven M1 displacement (dominated by TRPA1 at 0.033 vs 0.007 CPM). Restricting the CCI to detected genes — the same subset logic the manuscript itself applies to module scores — gives +215.6, permutation P = 0.046. The CCI as implemented is not a valid negative control, and the sentence drawn from it should be withdrawn.
2. Under the frozen eight-module BH family, the two neutral controls outrank the paper's main positive finding (N3 q = 0.014, N2 q = 0.023 vs E1 q = 0.034), yet only N2's q is stated in the text; the PHN contrast (§3.5) discloses neutral-control q values, so the practice is internally inconsistent.
3. The route-dependence claim is never subjected to its own formal test. With a consistently oriented composite, the route-by-program difference-in-differences is −0.193 log2CPM, exact permutation P = 0.0011 — i.e., the formal test *supports* the claim but is absent. Conversely, the M4 sentence in §3.2 commits the significant-versus-not-significant juxtaposition the manuscript elsewhere avoids (formal route difference for M4: P = 0.58).

Everything else — the permutation implementation, the BH implementation, the MDE formula, the bounded-null honesty, the MoR re-analysis, the detected-gene symmetry, the N1∩E1 disclosure, the gene-level family definitions, the injury panel, the detection baseline, and all 21 references — checks out. Verdict: **Major revision** (text-level fixes plus one added sensitivity analysis; no new data required).

---

## 1. Primary endpoint inference (M3, HZ-exo vs control-exo, n = 7 vs 7)

### 1.1 Verified values (all recomputed from raw counts)

| Quantity | Manuscript | My recomputation | Agreement |
|---|---|---|---|
| Difference (HZ − control) | −0.049 log2CPM | −0.04888 | identical |
| Exact permutation P (two-sided) | 0.42 | 0.4219 (1,448/3,432) | identical |
| Welch t / P | t = −0.835 / P = 0.42 | t = −0.8353 / P = 0.4199 | identical |
| BH q (8 modules, HZ contrast) | 0.46 | 0.4615 | identical |
| Welch 95% CI | −0.18 to +0.08 | [−0.176, +0.079] | identical |
| Permutation-inversion 95% CI | −0.16 to +0.06 | [−0.159, +0.062] | identical |
| MDE at 80% power | 0.18 log2CPM | 0.1786 | identical |
| Group SDs (control / HZ) | — | 0.1058 / 0.1130 (pooled 0.1095) | matches deposited |

The permutation null enumerates all C(14,7) = 3,432 label partitions of the observed per-sample module scores, two-sided, with no Monte-Carlo sampling and no 1/B floor — the disclosed implementation is the implemented one (an unfloor-ed P of 1,448/3,432 = 0.42191 is exactly what I obtain). The MDE uses the non-central-t two-sample formula (α = 0.05 two-sided, power 0.80, df = 12) applied to the *observed* pooled module-score SD (0.1095) — formula, SD source, non-centrality parameter and degrees of freedom are all correct.

### 1.2 "Bounded null" — honestly stated, with one presentational caveat

The manuscript says "no detectable response" is the claim, not "inert by mechanism" (§4.3), reports the MDE alongside both CIs, and the CI half-width (0.128) is consistent with the MDE (0.179) at the expected ratio (~0.71). This is the right way to report a null with n = 7 vs 7. Two caveats, neither requiring reanalysis:

- The MDE is derived from the observed SD, i.e., it is a post-hoc sensitivity statement rather than a design-stage power calculation; one clause saying so would pre-empt the obvious criticism.
- The bound applies to the 56-gene module *mean*. Coherent shifts confined to M3 subsets (e.g., the four nominally down collagen/Hippo genes at the gene level) are not bounded by the module MDE. The manuscript's gene-level incoherence argument (§3.2) covers this qualitatively.

---

## 2. Secondary / exploratory hierarchy

### 2.1 Verified values

| Claim (manuscript) | Recomputed | Agreement |
|---|---|---|
| E1 −0.220; perm P = 0.013; Welch P = 0.011; q = 0.034; CI −0.38 to −0.06 | −0.2196; 0.01282 (44/3,432); 0.01108; 0.03419; [−0.377, −0.062] | identical |
| M1 −0.078, P = 0.11 | −0.0780, 0.1131 | identical |
| M2 −0.148, P = 0.068 | −0.1483, 0.0682 | identical |
| M4 null under HZ exosomes (P = 0.46) | −0.0278, 0.4615 | identical |
| M3 null under VZV (P = 0.85) / PHN (P = 0.83) | 0.8528 / 0.8295 | identical |
| M4 under VZV −0.054, P = 0.03 | −0.0544, 0.0303 | identical |
| E1−N1 benchmark −0.064, P = 0.178; Welch P = 0.187 | −0.0638, 0.1783; 0.18667 | identical |
| Detected-gene subset: M1 −0.171, P = 0.046 | −0.1709, 0.0460 | identical |
| Detected-gene interaction −0.072, P = 0.16 | −0.0718, 0.1573 | identical |
| Post-hoc interaction −0.142, P = 0.0017 | −0.1417, 0.00175 (6/3,432) | identical |
| 2-route Bonferroni interaction P = 0.0034 | 2 × 0.00175 = 0.0035 (6/3,432 × 2) | identical |
| VZV interaction −0.051, P = 0.19 | −0.0508, 0.1926 (924 = C(12,6)) | identical |
| PHN: M1 −0.119 (P = 0.009, q = 0.024); E1 −0.197 (P = 0.005, q = 0.020); M2 −0.178 (P = 0.030); N1 −0.198 (P = 0.039); N3 +0.577 (P = 0.001, q = 0.010) | −0.1190/0.0088/0.0236; −0.1974/0.0051/0.0202; −0.1783/0.0303; −0.1981/0.0391; +0.5774/0.0013/0.0101 | identical |
| PHN/HZ DE counts at |log2FC| > 0.5: 568 up/125 down vs 129/174 | 568/125 vs 129/174 | identical |

The BH implementation is a correct step-up procedure across exactly eight modules within each contrast (verified for all three contrasts, all 24 q values). The interaction's exact permutation enumerates the 3,432 within-route label swaps of the per-sample composite (E1 − M1) score — a valid exact test of the exosome difference-in-differences. Note for the text: the minimum attainable two-sided P with 3,432 partitions is 1/3,432, so the reported interaction P = 6/3,432 = 0.0017 is a genuine enumeration value, not a floored one.

### 2.2 Problem R1 — the route-dependence claim is never tested formally; the correctly oriented test (P = 0.0011) is missing, and the M4 sentence commits a significant-vs-not comparison across experiments

【Problem】The route-dependence conclusion rests on an informal comparison of two within-route interactions computed with *opposite* sign conventions (§3.4: exosome (E1 − M1) = −0.142, P = 0.0017; infection (M1 − E1) = −0.051, P = 0.19), and §3.2 states that M4 "was null under HZ exosomes (P = 0.46) but, notably, was suppressed under direct VZV infection (−0.054; P = 0.03)" — a cross-experiment significant-versus-not juxtaposition with no interaction test.

【Evidence】With a consistently oriented composite (E1 − M1 in both routes), the route-by-program difference-in-differences is DiD_exo = −0.1417 vs DiD_inf = +0.0508, difference = −0.1925 log2CPM, exact permutation P = 0.0011 (product of the two exact within-route nulls, 3,432 × 924 = 3,171,168 partitions; the two experiments are disjoint sample sets so the nulls are independent). The manuscript's sign-flipped orientation differences two same-signed quantities (−0.0908, P = 0.17), which is why the informal reading looks weaker than the data. For M4: DiD_exo = −0.0278 (P = 0.456), DiD_inf = −0.0544 (P = 0.030), route difference +0.0266, P = 0.578 — the two contrasts do not differ. (Caveat on my own test: the DiDiD assumes the E1−M1 composite is comparable across experiments; SCN10A is detected in DirectInf but at the floor in SeraExo, so the composite's composition differs between routes — worth one clause in the text.)

【Why it matters】The paper's title-level claim ("route-dependent") currently has no formal test behind it; the missing test happens to support it (P = 0.0011), so this is an easy strengthening. The M4 sentence, meanwhile, is precisely the "difference between significant and not significant is not itself significant" reasoning the manuscript avoids everywhere else, and a statistically literate reviewer will flag it.

【Specific fix】Add to §3.4 after the two within-route interaction P values: "Testing whether the route modifies the E1-versus-M1 pattern directly, the difference between the exosome and direct-infection difference-in-differences (E1−M1 composite, same orientation in both routes) was −0.193 log2CPM, exact permutation P = 0.0011 (3,171,168 combined label partitions); this formal route-by-program interaction supports route dependence, while noting that SCN10A contributes to E1 only in the infection experiment, so the composite is not identically composed across routes." Replace the M4 clause in §3.2 with: "M4 was unchanged under HZ exosomes (−0.028; P = 0.46) and modestly suppressed under direct VZV infection (−0.054; P = 0.03); the route difference for M4 was not itself significant (+0.027; permutation P = 0.58), so no route specificity is claimed for M4."

---

## 3. Gene-level claims

### 3.1 Verified values (HZ-exo vs control-exo, Welch t on log2(1+CPM))

| Gene | Manuscript | Recomputed log2FC / P / within-E1 q |
|---|---|---|
| TRPV1 | −0.567, P = 0.0009, q = 0.017 | −0.5673 / 0.000915 / 0.01648 |
| KCNS1 | −0.393, P = 0.017, q ≈ 0.07 | −0.3930 / 0.01741 / 0.06933 |
| SCN9A | −0.323, P = 0.018, q ≈ 0.07 | −0.3231 / 0.01815 / 0.06933 |
| ASIC1 | −0.181, P = 0.019, q ≈ 0.07 | −0.1812 / 0.01926 / 0.06933 |
| ASIC2 | −0.296, P = 0.042, q ≈ 0.13 | −0.2960 / 0.04215 / 0.12645 |
| SCN10A | log2FC −0.384, P = 0.008; 0.55 CPM, 11% detected | −0.3844 / 0.00760; 0.55 CPM, 2/19 = 10.5% detected; within-E1 q = 0.0684 |
| PIEZO2 | −0.282, P = 0.18; CI ≈ −0.72 to +0.15 | −0.2822 / 0.18155; [−0.718, +0.154] |
| PIEZO1 / P2RX3 | P = 0.10 / P = 0.076 | 0.1034 / 0.07551 |
| M3: COL4A1 / COL4A2 / ADAMTS1 / TEAD1 | −0.381 (0.005) / −0.627 (0.007) / −0.479 (0.013) / −0.339 (0.047) | −0.3808 (0.00522) / −0.6268 (0.00734) / −0.4794 (0.01295) / −0.3392 (0.04685) |
| M3 up: LOX / YAP1 | +0.291 (0.024) / +0.425 (0.18) | +0.2910 (0.02403) / +0.4254 (0.18343) |
| VZV route: TRPV1 / PIEZO2 | −0.149 (Welch P = 0.008, q = 0.144) / −0.144 (P = 0.021) | −0.1487 (0.00797, q = 0.14353) / −0.1438 (0.02127) |

The within-module BH family for E1 is correctly the 18 panel genes present in the matrix (TRPV1 q = 0.0165 ≈ 0.017, reproducing exactly); no M1 gene reaches P < 0.05 under the primary contrast (smallest: P2RX3, P = 0.0755); no M3 gene survives within-module BH (smallest q = 0.137), consistent with the manuscript's decision to report M3 gene-level values only as uncorrected nominal illustration of directional incoherence. The descriptive-versus-corrected separation is explicitly stated in §2.4 and honored in the text — this is exactly the right discipline.

### 3.2 Problem R2 — SCN10A described as "the second-strongest in E1"; true by P value, false by effect size

【Problem】§3.3 calls SCN10A's nominal down-regulation "the second-strongest in E1"; by effect size it is the third-largest (KCNS1 −0.393 exceeds |−0.384|); it is second only by P value.

【Evidence】Recomputed within-E1 effect sizes: TRPV1 −0.5673, KCNS1 −0.3930, SCN10A −0.3844; P values: 0.000915, 0.01741, 0.00760.

【Why it matters】Minor, but "strongest" reads as effect size to most readers, and the sentence is load-bearing for the floor-limitation discussion.

【Specific fix】Replace "the second-strongest in E1" with "the second-smallest P value in E1 (after TRPV1)". Optionally add, since it strengthens the floor argument: "its within-E1 q was 0.068, so it would not have survived within-module correction in any case."

### 3.3 Problem R3 — detection-floor caveat applied to SCN10A but not to LOX/YAP1 in the M3 incoherence argument

【Problem】§3.2 uses LOX (+0.291, P = 0.024) and YAP1 (+0.425, P = 0.18) as upward-moving M3 genes without the floor-limitation caveat that §3.3 applies to SCN10A, although both are at or below the study's own CPM > 1 detection threshold.

【Evidence】Recomputed: LOX mean CPM 0.40 (detected in 5% of samples), YAP1 1.04 (32%); SCN10A, excluded as floor-limited, has 0.55 CPM and 10.5% detection — i.e., LOX is no better detected than SCN10A.

【Why it matters】Asymmetric floor discipline invites the charge of selective exclusion. The incoherence argument does not depend on these two genes: among detected M3 genes the pattern is still mixed (COL4A1/COL4A2/ADAMTS1/TEAD1/LOXL2 down versus MOB1A +0.264 [44.5 CPM, 100% detected, P = 0.003], TEAD2 +0.392, PLOD2 +0.285 up), so the fix is a caveat, not a reanalysis.

【Specific fix】Append to §3.2: "(LOX, mean CPM 0.40, and YAP1, 1.04, are themselves at or near the detection floor and are listed for completeness only; the directional incoherence among detected M3 genes — COL4A1, COL4A2, ADAMTS1, TEAD1 and LOXL2 down versus MOB1A, TEAD2 and PLOD2 up — is unchanged when they are excluded.)"

---

## 4. Neutral-control logic

### 4.1 Verified values

- N2 single-gene basis: OR5A1 mean CPM 0.89, detected in 32% of samples (2/19... precisely 6/19 = 31.6%); N2 module −0.022, P = 0.006, q = 0.023. The calibration-benchmark interpretation is correct and well argued.
- N3 as exposure/positive control: +0.391 (P = 0.002) under HZ, +0.577 (P = 0.001) under PHN — verified; the label is appropriate.
- N1∩E1 overlap: KCNQ2 and KCNQ3 are in both modules (confirmed in the frozen panel); under the primary contrast KCNQ3 q = 0.365 within E1 and 0.500 within N1, KCNQ2 q = 0.497 and 0.564 — reproducing the manuscript exactly; under PHN both move with E1 (KCNQ2 −0.313, KCNQ3 −0.295), as disclosed. The family-specific q reporting is exactly right.
- CCI computation: per-sample (mean rank of 9 M1 genes − mean rank of 18 E1 genes) over all 43,236 genes; HZ +82.7 (P = 0.833), PHN −74.3 (P = 0.851), VZV −19.8 (P = 0.965) — the "all P ≥ 0.82" claim reproduces exactly.

### 4.2 Problem R4 (most severe) — the CCI "null-by-construction" interpretation is unsupported; the null is a floor-gene cancellation, and the detected-gene CCI is nominally significant (P = 0.046)

【Problem】§3.6 interprets the null CCI as "consistent with the rank-based CCI being null-by-construction at the absolute scale that drives the module-level E1 signal" and reports the CCI as "a relative-displacement negative control". My decomposition shows the null is instead produced by cancellation between a genuine E1 rank displacement and a detection-floor-driven M1 displacement, and that it does not survive removal of below-detection genes.

【Evidence】(a) The 18 E1 genes moved a mean of 596 within-sample rank positions downward between control and HZ exosomes (GRIA1 −2,868; SCN10A −1,396; TRPV1 −1,042; GRIN2B −1,025), so the CCI is not blind to the E1 shift. (b) The 9 M1 genes moved a mean of 514 positions downward, dominated by TRPA1 (mean CPM 0.033 vs 0.007 — far below the CPM > 1 threshold; −5,451 rank positions); excluding TRPA1, M1 genes moved +104. The CCI null (+82.7) is the net of these opposing displacements. (c) Counterfactual sensitivity: imposing a uniform −0.2196 log2CPM shift on the E1 genes of the HZ group yields a between-group CCI difference of +2,470 (permutation P = 0.0006); imposing the observed per-gene E1 differences as a pure absolute shift (control group raised by each gene's observed log2FC) yields −829 (P = 0.058). The CCI is therefore highly sensitive to absolute shifts of the observed magnitude and is not "null-by-construction". (d) Restricting the CCI to detected genes (5 M1, 13 E1 — the identical subset logic the manuscript applies to module scores in §3.6) gives +215.6, permutation P = 0.046 (Welch P = 0.046), i.e., nominally significant, and in the direction expected if the E1 suppression has an absolute component.

【Why it matters】The CCI null is one of the three neutral-control arguments, and it is used to qualify the E1 module signal as a relative/compositional displacement. If the detected-gene CCI is nominally significant in the opposite interpretive direction, that qualification is unsupported and possibly backwards; and as implemented the CCI's M1 arm is floor-dominated, so it is not a valid negative control at all. This is the one place where the manuscript's interpretation, as opposed to its arithmetic, does not survive recomputation.

【Specific fix】Replace the CCI sentences in §3.6 with: "The CCI did not differ between groups under any contrast at the full gene set (HZ exosomes +82.7, permutation P = 0.83; PHN exosomes −74.3, P = 0.85; direct infection −19.8, P = 0.97). This null is not a construction artifact: the 18 E1 genes moved a mean of 596 within-sample rank positions downward between control and HZ exosomes (GRIA1 2,868; SCN10A 1,396; TRPV1 1,042), and the CCI is sensitive to displacements of this size — a uniform −0.22 log2CPM shift imposed on the E1 genes of the HZ group would produce a CCI difference of about +2,470 (P = 0.0006). The observed null instead reflects cancellation by the M1 arm, whose displacement is dominated by below-detection TRPA1 (mean CPM 0.033 versus 0.007; −5,451 rank positions); restricted to detected genes (5 M1, 13 E1), the CCI becomes +215.6 (permutation P = 0.046). The CCI is therefore reported as a descriptive rank-based observation rather than as a negative control, and its direction under the detected-gene restriction is consistent with an absolute component to the E1 suppression; no claim of channel-class specificity is drawn from it."

---

## 5. Confounding and design-level issues

### 5.1 Donor age/sex confounding in the PHN contrast

The non-specificity half of the PHN conclusion is established from the data themselves and reproduces: the neutral control N1 shifts by essentially the same amount as E1 (−0.198 vs −0.197), 568/125 genes move at |log2FC| > 0.5 (vs 129/174 under HZ), and N3 is induced (+0.577). That argument stands on its own. The confounding half rests on the claim, attributed to the source study, that PHN donors were older and almost exclusively female. Donor-level covariates are indeed absent from the deposited GEO metadata (the series matrix reports cell line and treatment only), so the confounding cannot be quantified from public data — the manuscript says so explicitly, which is correct. However, I could not verify the underlying empirical claim: the abstract of the cited source study (PMID 42734212) does not state donor age or sex distribution. See Questions.

### 5.2 Ribosomal-shift dilution argument — verified and quantitatively sound

Recomputed: 138 genes with RPL/RPS prefixes rise from 3.233% to 4.217% of the library between control and HZ exosomes (manuscript: 3.23% → 4.22%). The maximum compositional dilution of non-ribosomal transcripts implied by this shift is 95.77/96.77 = 0.9897, i.e., ≈0.015 log2 units — about 7% of the observed E1 effect (−0.220). The MoR robustness re-analysis is a genuine scale-matched median-of-ratios comparison, not a shortcut: size factors from the 17,922 genes positive in all samples (range 0.83–1.29), rescaled to the CPM dimension via the geometric mean of library sizes, then log2(1 + CPM). My independent implementation reproduces E1 −0.194 (P = 0.015), M3 −0.024 (P = 0.64), interaction −0.136 (P = 0.0017), and additionally shows N3 is *stronger* under MoR (+0.428, P = 0.0017) — the ribosomal response is real, and the E1 suppression survives composition-aware normalization. One presentational point: this re-analysis is described in §2.3 as part of the methods without the post-hoc label the manuscript applies to the injury panel and the interaction; label it for consistency.

### 5.3 Global-shift diagnostics

Recomputed per-sample mean log2CPM across all 19 exosome samples: 1.553 to 1.605 (manuscript: 1.55 to 1.61) — verified. Caveat: the mean of log2(1+CPM) over 43,236 genes is a blunt instrument for "no genome-wide drift" (it is dominated by the many low-count genes and can look stable while composition shifts, as the 3.23%→4.22% ribosomal shift itself demonstrates). The MoR re-analysis is the substantive answer to the drift question; the diagnostic is supportive color, and one clause acknowledging its bluntness would be honest.

### 5.4 ATF3 / pan-neuronal injury panel (post hoc) — verified

Recomputed for the actual ten-gene panel (ATF3, NEFH, TUBB3, NEFL, PRPH, NTRK1, SPP1, GAL, TAC1, CALCA): ATF3 +0.0002 (P = 0.998), NEFH −0.221 (P = 0.006), TUBB3 −0.183 (P = 0.012), NTRK1 −0.202 (P = 0.031), PRPH −0.128 (P = 0.048), NEFL −0.111 (P = 0.053) — all six manuscript values reproduce. BH across the ten-gene family: minimum q = 0.060 (NEFH, TUBB3), so "no marker survived Benjamini-Hochberg correction across the ten-gene panel" is exactly right, and the two-sided interpretation (argues against cytotoxicity; does not establish channel-specificity) is appropriately bounded. The post-hoc label is present.

---

## 6. Multiple-comparison honesty

The exploratory/post-hoc labeling is largely exemplary: the interaction is labeled post hoc with a 2-route Bonferroni adjustment (which I verify: 2 × 0.00175 = 0.0035), the detected-gene analysis is explicitly labeled a subset sensitivity rather than a correction, the PHN contrast is pre-designated exploratory with gene-level results explicitly disclaimed as not family-wise controlled, and §2.4 separates descriptive from corrected claims. Three residual issues:

### 6.1 Problem R5 — selective q reporting in the primary contrast: under the frozen BH family the neutral controls outrank E1, but N3's q is not stated

【Problem】In the HZ contrast the eight-module BH gives N3 q = 0.014 and N2 q = 0.023 — both smaller (more significant) than the E1 secondary endpoint's q = 0.034 — yet the text states only N2's q (§3.6) and gives N3 as "P = 0.002" without q; the abstract presents E1's q = 0.034 as the corrected headline.

【Evidence】Recomputed BH across the eight modules, HZ contrast: N3 0.01399, N2 0.02331, E1 0.03419, M2 0.13636, M1 0.18089, N1 0.20124, M3/M4 0.46154 — matching the deposited values exactly. §3.5's own practice for the PHN contrast (where N3 q = 0.010, E1 q = 0.020, M1 q = 0.024 are all stated) shows the inconsistency.

【Why it matters】A reader of the abstract cannot see that the pre-specified multiplicity control ranks the two neutral controls above the paper's main positive finding. Selective q reporting is the kind of asymmetry that undermines an otherwise disciplined correction; stating all eight q values converts a vulnerability into evidence of calibration (the neutral controls behaving as expected benchmarks).

【Specific fix】In §3.2 or §3.3 add: "Under the same eight-module Benjamini–Hochberg family, the neutral controls also crossed q < 0.05 (N3 q = 0.014; N2 q = 0.023); they are interpreted as an exposure response and a calibration benchmark, respectively, not as biological findings (§3.6)." In §3.6, change "N3 (ribosomal proteins) was induced by HZ exosomes (+0.391; P = 0.002)" to "N3 (ribosomal proteins) was induced by HZ exosomes (+0.391; P = 0.002; q = 0.014)".

### 6.2 Problem R6 — the abstract juxtaposes significant vs non-significant interaction P values without effect sizes

【Problem】Abstract: "A post hoc interaction (P = 0.0017) was non-significant among detected genes (P = 0.16)" — a significant-versus-not comparison with no effect sizes.

【Evidence】Recomputed: −0.142 (P = 0.00175) versus −0.072 (P = 0.157) — a halving of the effect, which is the substantive point.

【Why it matters】The full text is careful about this; the abstract is where the dichotomy does the most damage to a lay reader.

【Specific fix】Replace with: "A post hoc interaction (−0.142 log2CPM, P = 0.0017) was much smaller and non-significant in the detected-gene subset (−0.072, P = 0.16)."

### 6.3 Problem R7 — minor consistency items: stale deposit tag, unlabeled post-hoc MoR analysis, unreported Mann-Whitney results

【Problem】Three small inconsistencies: (i) Data availability cites repository tag v1.1.4 while the manuscript is v1.1.5 (tags v1.1.0–v1.1.6 exist; v1.1.5 matches this manuscript); (ii) the MoR robustness analysis is presented in §2.3 as part of the methods without the post-hoc label used elsewhere; (iii) Mann-Whitney U is announced in §2.4 and the abstract as one of three inferential methods but no MWU P value appears anywhere in the text.

【Evidence】Tag list retrieved from the repository's public API; MWU P values exist only in the deposited JSON (e.g., M3 HZ MWU P = 0.620).

【Why it matters】Individually trivial; collectively they are the kind of versioning/method-reporting slippage that a reproducibility-focused journal notices.

【Specific fix】(i) Change "tag v1.1.4" to "tag v1.1.5". (ii) Add "(post hoc robustness analysis)" to the median-of-ratios sentence in §2.3. (iii) Either add MWU P values parenthetically at first use (e.g., "M3: Welch P = 0.42, Mann-Whitney P = 0.62") or state in §2.4: "Mann-Whitney U P values are deposited in the reproducibility package and are not relied upon for any claim."

---

## § Stands up (verified correct — do not change)

1. **Every headline number reproduces from the raw counts.** All module-level differences, exact permutation P, Welch P, MWU P, BH q, both CIs, MDE, all gene-level values quoted in the text, the MoR values, the CCI values, the global-shift range, the ribosomal percentages, and the DE counts agree with my independent recomputation to 3–4 significant figures (full table in § What I actually checked). The SHA-256 hashes of both raw count files and the frozen panel match the deposited MANIFEST, so the deposited results demonstrably derive from the deposited inputs.
2. **The exact permutation implementation is genuinely exact and honestly disclosed.** C(14,7) = 3,432 (exosome contrasts), C(12,6) = 924 (VZV), C(12,5) = 792 (PHN); two-sided empirical P with no Monte-Carlo sampling and no 1/B floor, exactly as §2.4 states. The smallest reported P (interaction, 6/3,432 = 0.0017) is a true enumeration value.
3. **The BH implementation is correct**: step-up Benjamini-Hochberg across exactly the eight modules within each contrast; all 24 q values reproduce to four decimals; the within-module E1 family is correctly the 18 present genes (TRPV1 q = 0.0165).
4. **The MDE computation is correct in form and inputs**: non-central-t two-sample formula, α = 0.05 two-sided, 80% power, df = 12, pooled SD from the observed group SDs; 0.1786 ≈ the reported 0.18; and the bounded-null framing ("no detectable response", not "inert by mechanism") with both CIs is honest and internally consistent (CI half-width/MDE ≈ 0.71, as expected).
5. **The MoR robustness re-analysis is a real scale-matched median-of-ratios comparison, not a shortcut**, and the dilution argument is quantitatively sound (maximum implied dilution ≈ 0.015 log2 units, ~7% of the E1 effect); the E1 signal survives (−0.194, P = 0.015) while N3 strengthens (+0.428).
6. **The detected-gene sensitivity is symmetric and honestly reported**: E1 survives it (−0.243, P = 0.013) while M1 flips (−0.171, P = 0.046), and the text explicitly refuses to call M1 either "spared" or "confirmed down" — the correct response to exactly this situation.
7. **Neutral-control bookkeeping**: N2's single-gene basis (OR5A1, 0.89 CPM, 32% detection) is verified and used as a calibration argument; the N1∩E1 overlap (KCNQ2/KCNQ3) is disclosed with family-specific q values that reproduce exactly; the N3 "exposure control" relabeling is appropriate.
8. **Detection baseline (Table 1) is exact**: all ten genes, both experiments, mean CPM and detection fractions reproduce (e.g., PIEZO2 245.2/164.1 CPM; SCN10A 7.23 vs 0.55 CPM; P2RX3 806.8/470.6); the file byte sizes in §2.1 are exact; the claimed gene coverage after matching (9/9, 20/20, 56/58, 25/25, 18/18, 17/17, 13/16, 17/18) is exact.
9. **Injury panel**: all six reported marker values reproduce; "no marker survived BH across the ten-gene panel" is exactly right (min q = 0.060); the two-sided interpretation is appropriately bounded and labeled post hoc.
10. **References**: all 21 resolve to the correct papers (PMIDs/DOIs checked individually; author lists, titles, journals and years match). The one nuance is conventional, not an error: ref 15 (Murthy et al.) carries a 2018 epub date but the manuscript's "2019;11(486)" matches the formal journal citation.
11. **M3 alias sensitivity** (adding CCN1/CCN2 to reach the full 58 genes): −0.048, P = 0.416 — conclusion unchanged. This exists in the deposited package but is not mentioned in the text; see Questions.

---

## § Questions for the authors

1. The donor age/sex confounding of the PHN group is attributed to the source study (ref 3), but I could not locate the statement in its abstract. Please pin the exact source (table/figure/page of ref 3) or soften to "reported by the source study" without specifics.
2. What is the public URL and deposit timestamp of protocol v0.4 / frozen panel `mtp-frozen-2026-10-19`? The manuscript asserts deposition before data examination; the only machine-checkable artifact I could find is the repository tag.
3. Was the detected-gene subset rule (mean CPM > 1) fixed before the module-level results were seen? It is presented as a sensitivity analysis; if chosen after observing that M1 flips, please say so explicitly.
4. Was a detected-gene CCI ever computed in the deposited package? My recomputation gives +215.6, P = 0.046 — if not, please add it (§4.2 fix).
5. Please add one sentence on the M3 alias sensitivity (CCN1/CCN2: −0.048, P = 0.416) to §4.4(v), since the CYR61/CTGF absence is discussed there.
6. For the interaction tests, please state in the text that the exact permutation enumerates the 3,432 within-route label swaps of the per-sample composite score; as written, a reader could assume a 28-sample interaction null.
7. E1 contains 5/18 below-detection genes (SCN10A, TRPM8, KCNQ3, GRIN2B, GRIA1) and M1 contains 4/9; the manuscript reports this for M1 but not for E1. Was the E1 floor exposure considered when interpreting the E1−M1 interaction? (For transparency: the detected-gene E1 effect is *larger*, −0.243, so this does not threaten the E1 finding.)

---

## § What I actually checked

**Files read in full:** the manuscript (all 214 lines, including the long single-line paragraphs expanded in full); `analysis/config/mtp_panel.json`; both raw count matrices (`GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz`, 43,236 genes × 19 samples, 884,411 bytes; `GSE342782_Processed_DirectInf_neuronHD10s_BulkSeq_Counts.csv.gz`, 43,236 × 12, 622,501 bytes — byte sizes and SHA-256 match the manuscript and the deposited MANIFEST); the series matrix sample titles (group assignment C/P/S = 7/5/7 confirmed); the pipeline scripts `layer1_mechano.py`, `layer1_norm_robustness.py`, and the panel sections of `layer1_extra_checks.py`; the deposited artifacts `layer1_results.json`, `layer1_norm_robustness.json`, `layer1_extra_checks.json`, `layer1_cci.csv`, `layer1_gene_level.csv`, and the results-directory MANIFEST.

**Independent recomputation** (my own implementation from the raw counts; scratch outputs written only to `analysis/scratch_B2/`; deposited results never modified): CPM conversion and log2(1+CPM); all module scores over present genes; exact enumeration of all label partitions (3,432 / 924 / 792) for two-sided permutation P; Welch t and Mann-Whitney U; step-up BH across eight modules per contrast and within each module; the non-central-t MDE; the permutation-inversion and Welch CIs; the composite-score difference-in-differences and its convolution null across routes; the median-of-ratios re-analysis (size factors from 17,922 all-positive genes, rescaled to CPM dimension); the CCI and its rank-displacement decomposition; per-gene Welch tests for all 43,236 genes in all three contrasts; the ten-gene injury panel with BH; global-shift, ribosomal-share, and DE-count diagnostics.

**Recomputed vs manuscript (discrepancy stated):**

| Item | Manuscript | Recomputed | Status |
|---|---|---|---|
| M3 diff / perm P / Welch P / q / CI-Welch / CI-perm / MDE | −0.049 / 0.42 / 0.42 / 0.46 / −0.18..+0.08 / −0.16..+0.06 / 0.18 | −0.0489 / 0.4219 / 0.4199 / 0.4615 / [−0.176,+0.079] / [−0.159,+0.062] / 0.1786 | identical |
| E1 diff / perm P / Welch P / q / CI | −0.220 / 0.013 / 0.011 / 0.034 / −0.38..−0.06 | −0.2196 / 0.01282 / 0.01108 / 0.03419 / [−0.377,−0.062] | identical |
| M1 / M2 / M4 (HZ) | −0.078 (0.11) / −0.148 (0.068) / null (0.46) | −0.0780 (0.1131) / −0.1483 (0.0682) / −0.0278 (0.4615) | identical |
| N1 / N2 / N3 (HZ) | −0.156 (0.151) / −0.022 (0.006, q 0.023) / +0.391 (0.002) | −0.1558 (0.1509) / −0.0221 (0.0058, q 0.0233) / +0.3914 (0.0017) | identical |
| PHN: M1/E1/M2/N1/N3 | −0.119 (0.009, q 0.024) / −0.197 (0.005, q 0.020) / −0.178 (0.030) / −0.198 (0.039) / +0.577 (0.001, q 0.010) | −0.1190 (0.0088, 0.0236) / −0.1974 (0.0051, 0.0202) / −0.1783 (0.0303) / −0.1981 (0.0391) / +0.5774 (0.0013, 0.0101) | identical |
| VZV: M1 / M3 / M4 / E1 | −0.050 (0.047 Welch; 0.05 perm) / 0.85 / −0.054 (0.03) / +0.0005 (0.996) | −0.0504 (0.0466; 0.0498) / 0.8528 / −0.0544 (0.0303) / +0.0005 (0.9957) | identical |
| Interaction (exo / VZV / detected-only) | −0.142 (0.0017) / −0.051 (0.19) / −0.072 (0.16) | −0.1417 (0.00175) / −0.0508 (0.1926) / −0.0718 (0.1573) | identical |
| E1−N1 benchmark | −0.064 (0.178; Welch 0.187) | −0.0638 (0.1783; 0.1867) | identical |
| TRPV1 (HZ / VZV) | −0.567 (0.0009, q 0.017) / −0.149 (0.008, q 0.144) | −0.5673 (0.000915, 0.01648) / −0.1487 (0.00797, 0.14353) | identical |
| KCNS1/SCN9A/ASIC1/ASIC2 | −0.393 (0.017) / −0.323 (0.018) / −0.181 (0.019) / −0.296 (0.042) | −0.3930 (0.01741) / −0.3231 (0.01815) / −0.1812 (0.01926) / −0.2960 (0.04215) | identical |
| SCN10A | −0.384 (0.008); 0.55 CPM; 11% | −0.3844 (0.00760); 0.55 CPM; 10.5% (2/19) | identical |
| PIEZO2 (HZ / VZV) | −0.282 (0.18; CI −0.72..+0.15) / −0.144 (0.021) | −0.2822 (0.18155; [−0.718,+0.154]) / −0.1438 (0.02127) | identical |
| M3 genes COL4A1/COL4A2/ADAMTS1/TEAD1/LOX/YAP1 | −0.381 (0.005) / −0.627 (0.007) / −0.479 (0.013) / −0.339 (0.047) / +0.291 (0.024) / +0.425 (0.18) | −0.3808 (0.00522) / −0.6268 (0.00734) / −0.4794 (0.01295) / −0.3392 (0.04685) / +0.2910 (0.02403) / +0.4254 (0.18343) | identical |
| KCNQ2/KCNQ3 q within E1/N1 | 0.497/0.564 and 0.366/0.500 | 0.49702/0.56359 and 0.36549/0.50043 | identical |
| MoR: E1 / M3 / interaction | −0.194 (0.015) / −0.024 (0.64) / P = 0.0017 | −0.1942 (0.0152) / −0.0236 (0.6428) / −0.1360 (0.00175) | identical |
| CCI all-P claim | all P ≥ 0.82 | 0.8328 / 0.8510 / 0.9654 | identical |
| Global shift / ribosomal share | 1.55–1.61 / 3.23%→4.22% (138 genes) | 1.5528–1.6054 / 3.233%→4.217% (138 genes) | identical |
| DE counts | 129/174 (HZ); 568/125 (PHN) | 129/174; 568/125 | identical |
| Injury panel (6 markers) | ATF3 +0.0002 (0.998); NEFH −0.221 (0.006); TUBB3 −0.183 (0.012); NTRK1 −0.202 (0.031); PRPH −0.128 (0.048); NEFL −0.111 (0.053) | +0.0002 (0.9983); −0.2205 (0.00614); −0.1833 (0.01195); −0.2019 (0.03062); −0.1280 (0.04794); −0.1113 (0.05264); min BH q across 10-gene panel = 0.0598 | identical |
| Table 1 baseline (10 genes × 2 experiments) | as printed | as printed (PIEZO2 245.24/164.13; P2RX3 806.84/470.61; SCN10A 7.23/0.55 with 10.5% detection; etc.) | identical |
| M3 alias (CCN1/CCN2, 58 genes) | not in text | −0.0478 (0.4155) | reviewer-computed; conclusion unchanged |
| Detected-only CCI (5 M1, 13 E1) | not in text | +215.6 (0.0460) | reviewer-computed; see Problem R4 |
| Route×module DiDiD (consistent orientation) | not in text | −0.1925 (P = 0.0011) | reviewer-computed; see Problem R1 |
| M4 route difference | "notably suppressed under VZV" juxtaposition | +0.0266 (P = 0.578) | reviewer-computed; see Problem R1 |

**References checked** (PMID/DOI resolve to the correct paper, authors, title, journal, year): all 21, via PubMed/Crossref. No mismatches; the only nuance is the conventional 2018-epub/2019-issue date of ref 15, which matches the manuscript's citation format.

---

## Must-fix list (ordered by severity)

1. **Withdraw the CCI "null-by-construction" interpretation and add the detected-gene CCI** (§4.2 / Problem R4): replace the §3.6 sentences with the paste-ready text; the CCI null is a floor-gene cancellation (TRPA1 −5,451 rank positions), not a construction artifact, and the detected-only CCI is +215.6, P = 0.046. Without this fix, one of the three neutral-control arguments is unsupported and the E1 signal's "relative displacement" qualification is unearned.
2. **Add the formal route×module interaction test and remove the M4 significant-vs-not sentence** (§2.2 / Problem R1): report the consistently oriented difference-in-differences (−0.193, exact permutation P = 0.0011) and restate M4 with its non-significant route difference (P = 0.58).
3. **Disclose all eight BH q values for the primary contrast**, including N3 q = 0.014 and N2 q = 0.023 alongside E1 q = 0.034 (§6.1 / Problem R5).
4. **Add effect sizes to the abstract's interaction sentence** (§6.2 / Problem R6): −0.142 (P = 0.0017) vs −0.072 (P = 0.16).
5. **Apply the detection-floor caveat symmetrically to LOX and YAP1** in §3.2 (§3.3 / Problem R3), noting the incoherence argument survives without them.
6. **Correct "second-strongest in E1" to "second-smallest P value in E1"** for SCN10A, and optionally add its within-E1 q = 0.068 (§3.2 / Problem R2).
7. **Fix the three consistency items** (§6.3 / Problem R7): deposit tag v1.1.4 → v1.1.5; label the MoR analysis post hoc; report or explicitly defer the Mann-Whitney P values.
8. **Answer Questions 1, 3 and 4** (age/sex source in ref 3; pre-specification status of the detected-gene subset; detected-gene CCI), and consider the two optional additions (M3 alias sentence; interaction null description).

---

## Verdict

**Major revision.** Every reported statistic reproduces exactly from the raw data — the numerical core of this manuscript is trustworthy — but the CCI neutral-control interpretation is contradicted by the data once detection floors are handled symmetrically, the title-level route-dependence claim lacks its own formal test, and multiplicity disclosure is selective in the primary contrast; all are fixable in text plus one added sensitivity analysis, with no new experiments or data required.
