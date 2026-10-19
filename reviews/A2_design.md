# A2 review — statistical design and inference layer

**Reviewer role:** biostatistics / bioinformatics methods (permutation inference, multiple testing, small-sample RNA-seq design)
**Manuscript:** `manuscript/manuscript_v1.0.0.md` — *Route-dependent transcriptional effects of varicella-zoster virus and patient serum exosomes on ion-channel programmes in human sensory neurons: a pre-registered reanalysis of GSE342782*
**Scope:** design and inference only (power, permutation scheme, multiplicity, interaction logic, control calibration). Gene-level biology and venue fit are out of scope.
**Method of verification:** every number below was recomputed by me from the raw GEO count files (`analysis/data/raw/*.csv.gz`) by reproducing the pipeline of `analysis/scripts/layer1_mechano.py` verbatim (same CPM/log2 transform, same frozen panel `mtp-frozen-2026-10-19`, same group assignment, same seed 20261019), plus exact enumeration of all distinct label permutations and a difference-of-differences interaction analysis.

---

## Issue 1 — "Correctly-powered null" is not supported by any calculation; the primary-endpoint null is a bounded null, and its bound is wide

【Problem】 The manuscript calls the primary endpoint a "correctly-powered null … adequately powered at the gene-set level" (manuscript_v1.0.0.md:71) without showing any power calculation, and reports no confidence interval for the primary endpoint anywhere.

【Evidence】 Reproduced from the raw SeraExo counts via the manuscript's own pipeline (56 of 58 M3 genes; CYR61/CTGF absent, as stated). M3 module-score difference, HZ-exo (n = 7) vs control-exo (n = 7): **−0.0489 log2CPM**; within-group SDs 0.106 (control) and 0.113 (HZ), pooled 0.109. **95% Welch CI: −0.176 to +0.079** (df = 11.9; t = −0.835, P = 0.420). **Minimal detectable difference at 80% power, two-sided α = 0.05, n = 7 vs 7: 0.179 log2CPM** (noncentral-t, 12 df; normal approximation 0.164). Power for an effect of the observed magnitude: ≈ 0.12. For calibration, the same design on the same samples detected E1 at −0.220 (MDE for E1: 0.215; power for the observed E1 effect ≈ 0.82), so the design *can* resolve module shifts of ~0.2 log2CPM — it simply did not observe one in M3. The permutation null (P = 0.42) and the parametric CI agree; the problem is not the null itself but its characterization.

【Why it matters】 "Correctly-powered" asserts that the design could have detected a meaningful effect and did not. In fact the 80%-power resolution is 0.179 log2CPM — 3.7× the observed effect — and the CI includes shifts up to +0.079 and down to −0.176, i.e. it comfortably contains effects of the size the same experiment detected in E1 (−0.220) and N3 (+0.391). A reader relying on "correctly-powered" would conclude the stiffness programme is inert to effects of biological interest; the data only exclude shifts ≥ ~0.18 log2CPM. This is the manuscript's headline "most consequential finding" (§4.3), so the overclaim propagates into the Discussion and Conclusions.

【Specific fix】 Replace the two sentences at manuscript_v1.0.0.md:71 beginning "We therefore report a correctly-powered null" with:

> The pre-specified primary endpoint — the M3 difference between HZ-serum exosomes and control exosomes — was −0.049 log2CPM (95% Welch confidence interval −0.176 to +0.079; exact permutation P = 0.42; BH q = 0.46). Given the observed within-group SD of 0.109 log2CPM and n = 7 versus 7, the minimal detectable difference at 80% power (two-sided α = 0.05) is 0.179 log2CPM, and the design had ≈ 12% power for an effect of the observed magnitude; the null is therefore bounded only to exclude shifts of roughly 0.18 log2CPM or larger — a bound that still contains effects of the size observed in other modules of the same samples (E1, −0.220). We accordingly report the primary endpoint as a bounded null: within 36 hours of exosome exposure, the neuronal ECM–integrin–Hippo programme shows no shift exceeding the design's resolution.

(Averaging 56 genes does not rescue the claim: the 0.109 SD is already the post-averaging, per-sample module-score SD, and the MDE follows from it directly.)

---

## Issue 2 — Permutation granularity: reported P values are Monte-Carlo estimates with a structurally anti-conservative floor; exact enumeration is feasible and changes the small P values

【Problem】 With B = 5,000 draws but only C(14,7) = 3,432 (7v7), C(12,5) = 792 (7v5) and C(12,6) = 924 (6v6) distinct label assignments, every reported P is a sampling estimate, and the script floors P at 1/B (`analysis/scripts/layer1_mechano.py:83`, `p = max(p, 1.0 / B)`) — a floor below the smallest attainable two-sided P for every design in the paper.

【Evidence】 I replicated the script's Monte-Carlo null exactly (same seed and call order): all 24 reported `p_perm` values reproduce to machine precision, so the numbers are not fabricated — they are what the documented pipeline produces. Exact enumeration of all distinct assignments gives:

| contrast | module | reported p_perm | exact P (k/N) |
|---|---|---|---|
| HZexo vs CtrlExo | E1 | 0.0112 | **0.0128** (44/3,432) |
| HZexo vs CtrlExo | M3 (primary) | 0.416 | 0.4219 (1,448/3,432) |
| HZexo vs CtrlExo | N3 | 0.0006 | 0.0017 (6/3,432) |
| PHNexo vs CtrlExo | N3 | **0.0002** | **0.00126** (1/792) |
| PHNexo vs CtrlExo | E1 | 0.0040 | 0.0051 (4/792) |
| VZV vs Mock | M1 | 0.0514 | 0.0498 (46/924) |
| VZV vs Mock | M4 | 0.0242 | 0.0303 (28/924) |

Minimum attainable two-sided P: 2/3,432 = 0.00058 (7v7), 1/792 = 0.00126 (7v5), 2/924 = 0.00216 (6v6) — all above the 1/B floor of 0.0002, so the cap can only understate P. It did so once: **N3 under PHN exosomes is reported as P = 0.0002** (manuscript_v1.0.0.md:83, :87) although the exact attainable value is 1/792 = 0.00126. Forensics: in the script's 5,000 draws, zero reached the observed extremeness; the identity assignment was drawn 8 times but its statistic computes 3.6 × 10⁻¹5 *below* `diff_obs` (different summation order), so the `>=` comparison fails every time; the mirror labeling was never drawn; P = 0 was then capped up to 0.0002 — an anti-conservative value 6.3× below the exact P.

【Why it matters】 The E1 result (the paper's key positive finding) survives: exact P = 0.0128 vs reported 0.0112 — credible, not a granularity artifact, and the claim "minimum attainable P ≈ 0.0003" is in fact 0.00058 for the balanced designs. But three reported numbers are wrong or misleading in the anti-conservative direction (N3 PHN P = 0.0002 and its q = 0.0016; N3 HZexo P = 0.0006 vs exact 0.0017), and the M4-under-VZV "suppression" (P = 0.024) weakens to 0.030. A journal referee rerunning the script gets the same wrong values, which is worse than a one-off typo: it is a reproducible defect in the inference layer.

【Specific fix】 Delete the cap at `layer1_mechano.py:83` and replace the Monte-Carlo loop with exact enumeration (≤ 3,432 iterations — instant), e.g. in `perm_null`: iterate over all C(n, n_B) assignments of the pooled labels, statistic = mean(B) − mean(A), two-sided P = #{|stat| ≥ |obs|}/C(n, n_B), with a float tolerance of 1e-12 so the observed assignment and its mirror count. Then in Methods (§2.4, manuscript_v1.0.0.md:57) replace the permutation sentence with:

> Label-permutation nulls were computed by exact enumeration of all distinct label assignments (C(14,7) = 3,432 for the 7-versus-7 contrasts, C(12,5) = 792 for the PHN contrast, C(12,6) = 924 for the direct-infection contrast); the two-sided P value is the fraction of assignments at least as extreme as the observed difference.

Update the affected quoted values: E1 under HZ exosomes P = 0.013 (not 0.011); N3 under HZ exosomes P = 0.0017 (not 0.0006); N3 under PHN exosomes P = 0.0013 (not 0.0002); M4 under VZV P = 0.030 (not 0.024).

---

## Issue 3 — BH verification: the reported q values are arithmetically correct, but they inherit the capped P

【Problem】 Verify the reported BH-adjusted q values (M3 q = 0.46, E1 q = 0.030, N2 q = 0.022, N3 q ≈ 0.005; PHN contrast M1 q = 0.021, E1 q = 0.016) as BH step-up values across the 8 modules within each contrast.

【Evidence】 Recomputed BH (step-up, m = 8, within contrast) from the reported `p_perm` values: **all 24 q values in `bh_q` match my recomputation to four decimal places** (e.g. HZexo: N3 0.0006→q 0.0048, N2 0.0056→0.0224, E1 0.0112→0.0299, M3 0.416→0.4598 after step-up from M4's 0.4598; PHN: M1 0.0078→0.0208, E1 0.0040→0.0160). The scheme matches the pre-specified description ("BH across the eight modules within each contrast", manuscript_v1.0.0.md:57). Two caveats: (a) recomputing from **exact** permutation P values shifts the small q's — N3 PHN q = 0.0101 (vs reported 0.0016, built on the capped P), N3 HZexo q = 0.0140 (vs 0.0048), E1 HZexo q = 0.0342 (vs 0.0299), E1 PHN q = 0.0202 (vs 0.0160); all conclusions survive. (b) The primary-contrast E1 result is robust even to the stricter alternative of correcting across all 24 module tests (BH q ≈ 0.045 using reported P; ≈ 0.051 using exact P) — i.e. at the margin, not comfortably.

【Why it matters】 Confirms the multiplicity layer is honestly implemented and correctly described; the only defect is upstream (the capped P feeding the N3 PHN q). The all-24-test check is worth one sentence in the paper because it is the strongest available statement about E1.

【Specific fix】 Keep the within-contrast BH as pre-specified. After switching to exact P (Issue 2), report q from exact P (E1 q = 0.034, N2 q = 0.023, N3 q = 0.014 in the primary contrast). Optionally add to §3.3: "The E1 result remains at the margin of significance under correction across all 24 module-level tests (BH q ≈ 0.05)."

---

## Issue 4 — "Double dissociation" is asserted from a significant-vs-not pattern; the correct interaction test supports only a one-sided (E1) dissociation

【Problem】 The double-dissociation claim (manuscript_v1.0.0.md:77–79; repeated in the Abstract, :19, and §4.2, :97) rests on M1 under direct infection P = 0.051/0.047 and E1 under direct infection P = 0.996 versus E1 under HZ exosomes P = 0.011 and M1 under the same contrast P = 0.109 — i.e. on "significant vs not significant", which is not a test of dissociation, and is contradicted in effect size by the M1 leg.

【Evidence】 I computed the correct test — route × module interaction as a difference-of-differences on per-sample (E1 − M1) module scores, with within-experiment label permutation (20,000 resamples) — from the reproduced module scores:

- Route effect on E1: DiD = (HZexo − CtrlExo) − (VZV − Mock) = **−0.2201 log2CPM, permutation P = 0.025** (Welch-style t = −2.73, df = 18.5, P = 0.013).
- Route effect on M1: DiD = −0.0276, **permutation P = 0.63** — and the sign is opposite to the claimed mirror: M1's point estimate under HZ exosomes (−0.078) is *larger* than under direct infection (−0.050).
- Overall route × module interaction: DiD = −0.1925, **permutation P = 0.0015** (t = −3.73, P = 0.0012) — significant, but driven entirely by the E1 leg.

So the data support: E1 responds selectively to the exosome route; M1 responds weakly and non-selectively to both routes. There is no statistical evidence that direct infection *selectively* engages the mechanogated module. (Caveat: the DiD compares two experiments with different control conditions — mock vs control exosomes — and is valid only under an additive, module-independent baseline offset between experiments; with n = 6–7 per group it is hypothesis-generating regardless.)

【Why it matters】 "Double dissociation" is the paper's central conceptual claim (title-level: "route-dependent"), and the mirror-image framing is what licenses the Discussion's route-dependence argument (§4.2). As it stands the claim is half effect-size-contradicted (M1) and half untested (the interaction). The M1-under-infection effect also would not survive correction for the 8 modules (BH q = 0.21), so even its nominal P = 0.051 carries no confirmatory weight.

【Specific fix】 Replace manuscript_v1.0.0.md:79 (the paragraph "Direct VZV infection produced the mirror-image pattern…") with:

> Direct VZV infection was associated with a small M1 shift (−0.050 log2CPM; exact permutation P = 0.050; Welch P = 0.047; BH q = 0.21) and no E1 shift (+0.0005; P = 1.00), whereas HZ-serum exosomes suppressed E1 (−0.220; P = 0.013; q = 0.034) with M1 unchanged (−0.078; P = 0.11). Testing the dissociation directly as a route × module interaction on per-sample (E1 − M1) differences, the route effect on E1 differed significantly between perturbation routes (difference-of-differences −0.220 log2CPM; permutation P = 0.025), whereas the route effect on M1 did not (−0.028; P = 0.63) — the M1 point estimate under HZ exosomes is in fact larger than under direct infection. The overall route × module interaction was significant (DiD −0.193; permutation P = 0.0015) but is driven entirely by the E1 contrast. We therefore describe a route-selective suppression of the electrochemical nociceptor apparatus by exosomes rather than a mirror-image double dissociation, and treat the complementary M1 pattern as hypothesis-generating.

And in the Abstract (:19), replace "A double dissociation emerged across perturbation routes" with "The electrochemical response was route-selective: HZ exosomes suppressed E1 relative to direct infection (difference-of-differences −0.220 log2CPM, P = 0.025), while M1 showed no route selectivity (P = 0.63)." If the authors prefer to keep "double dissociation", they must add this analysis to the paper (spec: per-sample d = E1 − M1 in each experiment; DiD = [mean(d|HZ-exo) − mean(d|ctrl-exo)] − [mean(d|VZV) − mean(d|mock)]; null from independent within-experiment label permutations, B ≥ 20,000, two-sided; report DiD, P, and both legs with their P values) and state whether it was pre-specified.

---

## Issue 5 — CCI: keep as a one-line null calibration, never as evidence; current wording is acceptable but should be tightened

【Problem】 CCI is reported insensitive (all permutation P ≥ 0.82) and the manuscript already disclaims confirmatory use (manuscript_v1.0.0.md:87) — but the index is still given two sentences of Results space and its construction guarantees insensitivity.

【Evidence】 Recomputed from `layer1_results.json` CCI block: diffs +82.7 (P = 0.828), −74.3 (P = 0.855), −19.8 (P = 0.965) on a within-sample rank-difference scale of ≈ ±5,000 — i.e. the largest displacement is ~1.6% of scale. Because CCI is a within-sample *rank* difference between two gene sets, a uniform absolute-scale shift of all E1 genes (the observed −0.220 log2CPM) moves few ranks relative to ~43,000 genes and is undetectable by construction; with n = 7 vs 7 its MDE would be enormous. The null carries essentially no information about the channel-imbalance hypothesis in either direction.

【Why it matters】 Space spent on a structurally uninformative statistic invites the question of what it was for; the honest answer (pre-specified robustness check, null) is fine but should be one line, explicitly labelled as having no power for the observed effect.

【Specific fix】 Verdict: keep as calibration (it preserves the pre-registration trail), with this replacement for the CCI sentences at manuscript_v1.0.0.md:87:

> The channel-complementarity index, a pre-specified rank-based robustness check, did not differ between groups under any contrast (all exact permutation P ≥ 0.83); as a within-sample rank difference on a scale of thousands of genes it has no power to detect the absolute-scale E1 shift and is reported here only as a null calibration, not as a test of the channel-imbalance hypothesis.

(Alternative: delete the CCI sentences from §3.6 and the corresponding Methods sentence and keep the computation in the reproducibility package only.)

---

## Issue 6 — N2 neutral control: handling is adequate in substance, but the near-floor, effectively single-gene structure should be stated

【Problem】 N2 is nominally significant under HZ exosomes (P = 0.006, q = 0.022) at a near-zero baseline, and is interpreted as "a calibration benchmark, not a biological finding" (manuscript_v1.0.0.md:87). Is that adequate?

【Evidence】 Recomputed: N2 control mean 0.081, HZ mean 0.059 log2CPM (≈ 0.056 and 0.041 CPM); ~91% (control) and ~90% (HZ) of N2 gene–sample values are exactly zero; only 13 of 16 N2 genes are in the matrix; the module score is driven almost entirely by one gene — OR5A1 −0.290 while every other N2 gene moves ≤ 0.004. Exact permutation P = 0.0058; BH q = 0.023. With 8 modules × 3 contrasts tested, one nominal P ≈ 0.006 under the global null is unremarkable.

【Why it matters】 The calibration reading is correct, but as written a reader could take "nominally significant neutral module" as either a warning about the pipeline or a mysterious artifact. Stated quantitatively, N2 becomes the design's built-in false-positive demonstration — which *strengthens* the E1 claim by contrast (E1: effect 10× larger, high baseline ~3.5–3.7 log2CPM, coherent across 18 genes and 7 quoted genes).

【Specific fix】 Replace the N2 sentence at manuscript_v1.0.0.md:87 with:

> N2 (olfactory receptors) reached nominal significance under HZ exosomes (−0.022 log2CPM; exact permutation P = 0.006; q = 0.023) despite a near-zero baseline (control mean 0.081 log2CPM, with ~91% of gene–sample values exactly zero) and a module score driven almost entirely by a single gene (OR5A1 −0.290; all other N2 genes |Δ| ≤ 0.004); it is interpreted as a calibration benchmark demonstrating this design's small-sample false-positive behaviour — and, by contrast, the E1 suppression is tenfold larger, at a high baseline, and coherent across genes.

---

## Issue 7 — Internal contradiction: §3.2 claims M4 unchanged "in every contrast (all P ≥ 0.11)", but §3.4 reports M4 suppressed under direct infection (P = 0.024)

【Problem】 manuscript_v1.0.0.md:71 states "for M4 mechano-effectors in every contrast (all P ≥ 0.11)", which is false for two of the three contrasts and contradicts the manuscript's own §3.4.

【Evidence】 From `layer1_results.json` (and my exact enumeration): M4 under VZV vs mock = −0.054, p_perm = 0.0242 (exact 0.0303), BH q = 0.19 — the manuscript itself reports this as "M4 mechano-effectors were suppressed (−0.054; P = 0.024)" at manuscript_v1.0.0.md:79. M4 under PHN exosomes p_perm = 0.1084, also below 0.11. Only the primary contrast (P = 0.46) supports the claim.

【Why it matters】 A false "all P ≥ 0.11" in the primary-endpoint paragraph, contradicted two paragraphs later, undermines the reporting discipline the paper elsewhere demonstrates (and is exactly the kind of inconsistency a copy-editor or referee will flag).

【Specific fix】 Replace the clause "and for M4 mechano-effectors in every contrast (all P ≥ 0.11)" at manuscript_v1.0.0.md:71 with:

> whereas M4 mechano-effectors were unchanged under both exosome contrasts (P = 0.46 and P = 0.11) but nominally suppressed under direct VZV infection (−0.054; exact P = 0.030; BH q = 0.19), as reported below.

---

## Issue 8 — Gene-level P values are quoted without any multiplicity context

【Problem】 Gene-level Welch P values are presented as "hypothesis-supporting descriptive statistics" (manuscript_v1.0.0.md:57) yet are quoted as evidence throughout §3.2–3.3 (e.g. "TRPV1 (−0.567, P = 0.0009)", "COL4A1 (−0.381, P = 0.005)") with no statement of how many such tests are nominally significant.

【Evidence】 All 13 gene-level numbers I checked reproduce exactly from `layer1_gene_level.csv` (TRPV1 −0.567/P 0.00092; COL4A1 −0.381/0.0052; COL4A2 −0.627/0.0073; ADAMTS1 −0.479/0.013; TEAD1 −0.339/0.047; LOX +0.291/0.024; YAP1 +0.425/0.183; KCNS1 −0.393/0.017; SCN10A −0.384/0.0076; SCN9A −0.323/0.018; ASIC1 −0.181/0.019; ASIC2 −0.296/0.042; PIEZO2 −0.282/0.182). But the primary contrast yields **3,967 of 43,236 genes with nominal P < 0.05** (733 at P < 0.005; ~2,160 and ~216 expected under the null) — so a nominal P = 0.0009 is weak evidence on its own. The *coherence and magnitude* of the E1 gene shifts (all top genes negative, |Δ| 0.18–0.57 at a high baseline) is the real evidence, not the nominal P values.

【Why it matters】 Quoting uncorrected gene-level P values as "P = 0.0009" implies discovery-grade evidence; a referee who counts the genome-wide nominal hits will discount the gene-level support for both the E1 signature and the M3 "incoherence" argument.

【Specific fix】 Add one sentence to §2.4 (manuscript_v1.0.0.md:57): "Gene-level Welch P values are nominal and uncorrected (3,967 of 43,236 tested genes reach nominal P < 0.05 under the primary contrast, ≈ 2,160 expected under the null) and are reported only as direction-and-magnitude descriptors supporting the module-level inference." In §3.3, lead with effect sizes and drop the parenthetical P values, or replace them with "all |Δ| ≥ 0.18 and all negative".

---

## § Stands up (verified correct)

1. **Full numerical reproducibility of the module layer.** All 24 module-score differences (8 modules × 3 contrasts) and all 24 reported `p_perm` values reproduce exactly from the raw GEO count files through the documented pipeline, frozen panel, group assignment and seed (Monte-Carlo replication matched the reported P values to machine precision, including Welch/Wilcoxon P values). The analysis is genuine and traceable, not reverse-engineered.
2. **BH implementation is correct.** All 24 q values in `layer1_results.json:bh_q` are exact BH step-up values of the reported permutation P across the 8 modules within each contrast (matched to 4 d.p.); the scheme matches the pre-specified Methods description.
3. **Data-examination gate (§3.1) checks out.** PIEZO2 245.2 CPM and detected in 100% of samples; TRPV4 0.25, STOML3 0.01, LOX 0.41, MMP9 0.11, ITGB1 323.6 CPM — all reproduce from the raw matrices. Global-shift diagnostic verified: per-sample mean log2CPM across the 19 exosome samples spans 1.553–1.605 (claimed 1.55–1.61). Panel composition claims verified (M3 56/58 with CYR61/CTGF absent; N2 13/16; N3 17/18).
4. **The E1 secondary finding is method-robust.** Welch P = 0.0111, Wilcoxon P = 0.0175, exact permutation P = 0.0128 (44/3,432), BH q = 0.034 — four independent procedures agree, and the result sits at the margin even under correction across all 24 module tests (q ≈ 0.045–0.05).
5. **All gene-level numbers quoted in §3.2–3.3 reproduce** from `layer1_gene_level.csv`, and the genome-wide counts (129 up/174 down under HZ; 568/125 under PHN at |log2FC| > 0.5) match `layer1_global_de.csv`.
6. **The M3 null interpretation ("genuine null aggregation") is statistically sound**: within-M3 gene shifts are directionally mixed with individual genes (e.g. COL4A2 −0.627) moving far beyond the module-level MDE (0.179) while the module mean sits at −0.049 — a true aggregation null, not cancellation of a coherent shift.

---

## § Questions for the authors

1. What power calculation supported "correctly-powered … adequately powered at the gene-set level" (§3.2)? Our recomputation gives MDE = 0.179 log2CPM (80% power) and ≈ 12% power for the observed effect; please share the calculation if one exists.
2. Why is the permutation P floored at 1/B (`layer1_mechano.py:83`) rather than exactly enumerated (≤ 3,432 assignments)? Will you report exact P values, and correct N3-under-PHN from 0.0002 to 0.0013 (q from 0.0016 to 0.010)?
3. §3.2 says M4 is unchanged "in every contrast (all P ≥ 0.11)" while §3.4 reports M4 P = 0.024 under direct infection — which is intended?
4. Was the double dissociation pre-specified as a route × module interaction (difference-of-differences), or only as the pattern of separate P values? If the former, where in protocol v0.4?
5. For the PHN contrast only 792 distinct permutations exist, so the smallest attainable BH q is 8/792 = 0.010; do you agree that any "significance" from this contrast is structurally fragile and should be labelled nominal throughout?
6. Do you intend to add a multiplicity statement for the gene-level Welch tests (3,967 nominal P < 0.05 of 43,236 under the primary contrast), or restrict gene-level reporting to effect sizes?
7. Was any sensitivity analysis for CCI pre-specified? If not, do you prefer the tightened one-line calibration sentence or removal from the main text?

---

## § What I actually checked

**Files read:** `reviews/_PANEL_BRIEF.md`; `manuscript/manuscript_v1.0.0.md`; `analysis/scripts/layer1_mechano.py`; `analysis/config/mtp_panel.json`; `analysis/results/layer1/layer1_results.json`; `analysis/results/layer1/layer1_module_scores.csv`; `analysis/results/layer1/layer1_gene_level.csv`; `analysis/results/layer1/layer1_global_de.csv`; raw inputs `analysis/data/raw/GSE342782_Processed_DirectInf_neuronHD10s_BulkSeq_Counts.csv.gz` and `GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz` (read through the pipeline, gzip integrity confirmed by successful parse; byte sizes 622,501 and 884,411 match the manuscript).

**Computations run (all from the raw counts, reproducing `layer1_mechano.py` verbatim):** per-sample module scores for all 8 modules × 3 contrasts; Welch t/Wilcoxon re-verification; 95% Welch CIs, within-group SDs, noncentral-t MDE at 80% power and power-for-observed-effect for M3 and E1; Monte-Carlo replication of `perm_null` (seed 20261019, same call order) for all 24 tests; **exact enumeration** of all distinct label permutations (3,432 / 792 / 924) for all 24 tests; BH step-up recomputation from both reported and exact P; float-precision forensics on the N3/PHN identity assignment; route × module difference-of-differences with within-experiment permutation (B = 20,000) and Welch–Satterthwaite approximation; gene-level verification of 13 quoted statistics; N2 zero-fraction and per-gene diagnostics; CCI re-tabulation.

**Recomputed vs manuscript — discrepancies found:**
- "Correctly-powered null" (§3.2): unsupported; CI −0.176 to +0.079, MDE 0.179, power ≈ 0.12.
- N3 under PHN exosomes: reported P = 0.0002 (capped, unattainable) vs exact 0.00126; q 0.0016 vs 0.0101.
- N3 under HZ exosomes: reported 0.0006 vs exact 0.0017 (q 0.0048 vs 0.0140).
- E1 under HZ exosomes: reported 0.0112 vs exact 0.0128 (q 0.0299 vs 0.0342) — conclusion unchanged.
- M4 under VZV: reported 0.0242 vs exact 0.0303; and §3.2's "all P ≥ 0.11" is false (PHN M4 P = 0.108; VZV M4 P = 0.024).
- Double dissociation: significant-vs-not pattern; interaction test gives E1 leg P = 0.025 (significant), M1 leg P = 0.63 with sign opposite to the claim.
- Everything else I checked matched (see § Stands up), including all 24 BH q values from the reported P values, all w0 detection statistics, the global-shift range, all 13 gene-level statistics, and the genome-wide |log2FC| > 0.5 counts.

**Failed commands:** none; the audit ran to completion.

---

## Must-fix list (numbered)

1. **Replace the "correctly-powered null" claim** (§3.2, :71) with the CI + MDE quantification (paste-ready text in Issue 1); mirror the change in the Abstract and Conclusions where the null's strength is implied.
2. **Remove the 1/B cap and switch to exact permutation enumeration** (`layer1_mechano.py:83`); correct N3-under-PHN from P = 0.0002 to 0.0013 (q 0.0016 → 0.0101) and update all quoted permutation P values (E1 0.013; N3 HZexo 0.0017; M4 VZV 0.030).
3. **Downgrade the double dissociation** to the interaction-tested statement (paste-ready text in Issue 4) or add the difference-of-differences analysis and state its pre-specification status; fix the Abstract (:19) and §4.2 (:97) accordingly.
4. **Correct the false M4 claim** "all P ≥ 0.11" in §3.2 (:71) — it contradicts §3.4.
5. **Tighten the CCI reporting** to the one-line null-calibration sentence (or remove from main text).
6. **Quantify the N2 near-floor structure** in the calibration sentence (Issue 6).
7. **Add a multiplicity-context sentence for gene-level tests** and de-emphasize nominal gene-level P values in §3.2–3.3.

## Overall verdict

**Major revision (statistical reporting layer).** The underlying analysis is reproducible and honest at the pipeline level: every module-level number I could check reproduces from the raw data, the BH layer is correctly implemented, and the primary null and the E1 secondary finding survive exact recomputation. However, the inference layer as written contains one unsupported power claim that anchors the paper's headline interpretation, one structurally anti-conservative permutation floor that produced an unattainable P value (and a wrong q), an overclaimed "double dissociation" that the correct interaction test reduces to a one-sided E1 effect, and one internally contradictory null statement. None of the corrections changes the qualitative conclusions except the dissociation framing — but all are necessary for the statistical claims to be sound.
