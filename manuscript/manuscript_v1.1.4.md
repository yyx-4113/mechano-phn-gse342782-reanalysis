# Route-dependent transcriptional effects of varicella-zoster virus and patient serum exosomes on ion-channel programs in human sensory neurons: a prospectively specified reanalysis of GSE342782

**Yongxin Yang, B.M.**

Department of Anesthesiology, The Second Affiliated Hospital of Fujian University of Traditional Chinese Medicine, No. 282 Wusi Road, Fuzhou, Fujian 350003, China

Correspondence: Yongxin Yang — 960856791@qq.com | ORCID: 0009-0004-9698-6552

Telephone: +86-591-8787-8130 (institutional switchboard) | Fax: not available (institution publishes no fax line)

Running title: Route-dependent channel programs in VZV-exposed sensory neurons

---

## Abstract

**Background.** Mechanical allodynia is a cardinal symptom of postherpetic neuralgia (PHN), yet mechanotransduction is rarely examined in PHN transcriptomics. GSE342782 — RNA-sequencing of human sensory neurons exposed to varicella-zoster virus (VZV) or to serum exosomes from controls, acute herpes zoster (HZ) and PHN patients — permits a test.

**Methods.** Before analysis we froze a four-module mechanotransduction panel (M1 mechanogated; M2 membrane-cytoskeleton; M3 ECM-integrin-Hippo; M4 mechano-effectors) plus an electrochemical nociceptor module (E1) and three neutral controls. The single primary endpoint was the M3 module-score difference between HZ-serum and control exosomes. Inference used Welch t, Mann-Whitney U and exact label-permutation nulls with Benjamini-Hochberg correction across eight modules.

**Results.** M3 did not shift under HZ-serum exosomes (difference -0.049 log2CPM; permutation P = 0.42; 95% CI -0.18 to +0.08; minimum detectable effect 0.18 log2CPM) — a bounded null. HZ-serum exosomes suppressed the nociceptor module (E1, -0.220 log2CPM; P = 0.013; q = 0.034), led by TRPV1, the only gene surviving Benjamini-Hochberg correction within E1 (q = 0.017); KCNS1, SCN9A, ASIC1 and ASIC2 were only nominally down (within-E1 q 0.07-0.13). M1 was at most marginally shifted (P = 0.11; PIEZO2 P = 0.18), and E1 was not separable from its neutral control (E1 - N1 = -0.064, P = 0.18). A post hoc interaction (P = 0.0017) was non-significant among detected genes (P = 0.16). The exploratory PHN-exosome contrast was non-specific and donor-confounded.

**Conclusions.** In this 36-h exposure of an immortalized embryonic dorsal-root-ganglion line, HZ-serum exosomes — but not direct VZV infection — down-regulated the electrogenic nociceptor program, with only TRPV1 surviving within-module correction, while the ECM-Hippo stiffness program was inert within a bounded null. Relevance to PHN allodynia is hypothesis-generating, not evidence of mechanism in patients.

**Registration.** Protocol v0.4 and frozen panel `mtp-frozen-2026-10-19` were deposited before data examination; no external registry entry.

**Keywords:** postherpetic neuralgia; mechanical allodynia; mechanotransduction; PIEZO2; varicella-zoster virus; extracellular vesicles

---

## 1. Introduction

Postherpetic neuralgia (PHN) is defined by dermatomal pain persisting at least 90 days after the acute herpes zoster rash, and is clinically characterized by mechanical allodynia — innocuous cutaneous stimuli transduced as pain.^1,20^ Mendelian-randomization analyses have begun to map the causal determinants of PHN risk.^2^ The symptom is, at its core, a disturbance of mechanotransduction, yet the genomic literature of PHN has seldom examined it through that lens. Published bioinformatic reanalyses of PHN cohorts have concentrated on interferon, immune, and inflammatory programs;^1^ none has systematically interrogated the mechanotransduction machinery — mechanogated ion channels, the membrane-cytoskeleton interface, or the extracellular-matrix (ECM)-integrin-Hippo axis.

Two developments make such an examination timely. First, Niemeyer and colleagues released GSE342782, a bulk RNA-sequencing resource in which differentiated HD10.6 human sensory neurons were exposed to direct VZV infection (harvested 4 days post-infection) or to serum-derived exosomes from healthy controls, patients with acute HZ, or patients with PHN.^3^ The original study reported down-regulation of canonical nociceptive ion channels, induction of substance-P-related neuropeptides, and ECM-remodeling signals, but did not examine these findings through a mechanotransduction lens. Second, extracorporeal shockwave therapy (ESWT) — the deliberate application of controlled mechanical stress — has shown benefit in small herpetic-neuralgia trials^4,7–9^ (although the largest randomized trial reported pain reduction without a significant time-by-group interaction)^7^, and its proposed mechanisms involve integrin-FAK-p38MAPK and Piezo/TRP signaling in non-neuronal model systems;^10,11^ none of these studies tested a YAP/TAZ or neuronal-channel mechanism in PHN, so any link to the present neuronal transcriptome is speculative. The mechanical axis is invoked at both the disease end (allodynia) and the treatment end (mechanotherapy) of PHN, yet no study has connected them transcriptomically, and the present data do not.

Here we report a prospectively specified reanalysis of GSE342782 with a frozen mechano-transduction panel, a single pre-specified primary endpoint, neutral-control calibration, and full permutation-based inference. The analysis was designed to answer three questions. (i) Are the mechanotransduction modules detectable, and do they shift, in human sensory neurons exposed to VZV or patient exosomes? (ii) Does the ECM-Hippo "stiffness program" — the hypothesized core of the mechanical axis — respond to any perturbation route? (iii) Do direct viral infection and exosome-mediated signaling converge on, or dissociate between, mechanogated versus electrochemical channel programs?

## 2. Methods

### 2.1 Data source and design

GSE342782 (GEO accession GSE342782; BioProject PRJNA1508885) comprises two experiments in differentiated HD10.6 human sensory neurons.^3^ Experiment 1 ("DirectInf"): mock infection (n = 6) versus VZV infection (n = 6), harvested 4 days post-infection. Experiment 2 ("SeraExo"): 36-hour exposure to serum-derived exosomes from healthy controls (n = 7), patients with acute HZ (n = 7), or patients with PHN (n = 5). Processed RSEM gene-level counts were downloaded directly from the GEO supplementary files (DirectInf counts, 622,501 bytes; SeraExo counts, 884,411 bytes; gzip integrity verified). Sample-to-group assignment used the column prefixes of the count matrices (C = control, P = PHN, S = acute zoster), which match the group sizes reported in the series metadata (7/5/7).

### 2.2 Prospectively specified analysis plan

Before any expression data were examined, the following were fixed in writing and deposited in a versioned public protocol (protocol v0.4; panel tag `mtp-frozen-2026-10-19`):

- **Frozen panel.** Four mechano-transduction modules — M1 mechanogated channels (PIEZO1, PIEZO2, TRPV4, STOML3, KCNK2/4, TMEM150C, P2RX3, TRPA1), M2 membrane-cytoskeleton coupling (20 genes), M3 ECM-integrin-Hippo (58 genes), M4 mechano-effectors (25 genes) — plus E1, an electrochemical nociceptor module (SCN9A, SCN10A, SCN11A, TRPV1, TRPM8, ASIC1/2/3, and related genes, excluding M1 members), and three neutral controls: N1 voltage-gated channels, N2 olfactory receptors, N3 ribosomal proteins. Module coverage after matching against the count matrix: M1-M4 and E1-N1 were fully represented (9/9, 20/20, 56/58, 25/25, 18/18, 17/17 genes); M3 lacked CYR61 and CTGF (56/58); N2 lacked OR6A1, OR10A1, OR13C1 (13/16); N3 lacked RPS4 (17/18; an RPS4X ortholog was present).
- **Primary endpoint.** The M3 module-score difference between HZ-serum exosomes and control exosomes (direction, effect size, permutation quantile). All other tests were pre-classified as secondary (E1 and M1 under the same contrast; the "channel-imbalance" hypothesis) or exploratory (PHN-exosome contrast; direct-infection contrast).
- **Donor-confounding safeguard.** Because the original authors reported that the PHN exosome donors were older and almost exclusively female,^3^ the PHN contrast was pre-designated exploratory and the HZ-versus-control contrast was designated the primary comparison.

### 2.3 Preprocessing and module scoring

Counts were converted to counts-per-million (CPM) and module scores computed as the mean log2(1 + CPM) across panel genes present in the matrix. Detection was defined as CPM > 1. Throughout this paper the shorthand "log2CPM" denotes log2(1 + CPM); the unit offset avoids undefined values for zero-count genes and is applied identically to every gene and sample.

### 2.4 Statistical testing

Group differences in module scores were tested with Welch's *t*-test and the Mann-Whitney *U*-test, and calibrated against an exact label-permutation null that enumerates every C(n1+n2, n1) partition of the observed per-sample module scores (no Monte-Carlo approximation, no 1/B floor), reporting a two-sided empirical P value and the observed difference's percentile within the null. Benjamini-Hochberg false-discovery-rate correction was applied across the eight modules within each contrast. The channel-complementarity index (CCI) — the within-sample difference between the mean expression rank of M1 genes and that of E1 genes across all 43,236 matrix genes — was computed per sample and compared between groups with the same permutation scheme. Gene-level contrasts were evaluated as Welch *t*-tests on log2(1 + CPM) values and, for genes belonging to a panel module, were further subjected to Benjamini–Hochberg correction within that module (reported as q_within_module). Both the uncorrected P values and the within-module q values are presented as descriptive support for the module-level findings, not as separately corrected discovery claims.

### 2.5 Reproducibility

All analyses were executed in Python 3.14.5 (NumPy 2.5.1, pandas 3.0.5, SciPy 1.18.0, Matplotlib 3.11.1). Every result file carries a SHA-256 manifest linking it to the exact input files and the frozen panel. All numerical values quoted in this manuscript are traceable to the reproducibility package — the module- and contrast-level results in `layer1_results.json` and the gene-level results in `layer1_gene_level.csv` (which now includes a within-module Benjamini–Hochberg q), both under the SHA-256 MANIFEST.

## 3. Results

### 3.1 Data examination: PIEZO2 and P2RX3 are robustly expressed; TRPV4 and STOML3 are not detectable

The prospectively specified data-examination gate established the expression baseline of the model (Table 1); the design and analysis pipeline are summarized in Figure 1. The HD10.6 line — a tetracycline-regulatable v-myc immortalized embryonic dorsal root ganglion clonal line, not an iPSC-derived model^5,6^ — expressed PIEZO2 at high levels (mean CPM 245.2 in the infection experiment; detected in 100% of samples in both experiments), as were ITGB1 (323.6 CPM) and the electrochemical nociceptor channels SCN9A (mean log2CPM 8.31 across all 12 samples; 8.39 in mock samples only) and TRPV1 (6.94 across all 12 samples; 7.02 in mock samples only). In contrast, TRPV4 (0.25 CPM), STOML3 (0.01 CPM), LOX (0.41 CPM) and MMP9 (0.11 CPM) fell below the detection threshold. Within M1, P2RX3 was the most abundant transcript (806.8 CPM in the infection experiment; 470.6 CPM in the exosome experiment), exceeding PIEZO2 (245.2 / 164.1 CPM); four of nine M1 genes sat at or below the detection floor. Two consequences follow. First, the technical risk that the model fails to express PIEZO2 is refuted, but M1 is more precisely a P2RX3/PIEZO2-dominated module than a PIEZO2-dominated one. Second, inference about TRPV4-, STOML3- or MMP9-centered mechanisms is out of scope for this dataset.

**Table 1. Detection baseline of mechanotransduction-relevant genes (mean CPM; detected = CPM > 1 in 100% of samples unless noted).**

| Gene | DirectInf mean CPM | DirectInf detected fraction | SeraExo mean CPM | SeraExo detected fraction |
|---|---|---|---|---|
| PIEZO2 | 245.2 | 1.00 | 164.1 | 1.00 |
| P2RX3 | 806.8 | 1.00 | 470.6 | 1.00 |
| PIEZO1 | 2.64 | 1.00 | 2.20 | 0.89 |
| TRPV4 | 0.25 | 0.00 | 0.19 | 0.00 |
| STOML3 | 0.01 | 0.00 | 0.00 | 0.00 |
| ITGB1 | 323.6 | 1.00 | 360.3 | 1.00 |
| SCN10A | 7.23 | 1.00 | 0.55 | 0.11 |
| SCN9A | 318.3 | 1.00 | 261.7 | 1.00 |
| TRPV1 | 122.3 | 1.00 | 95.6 | 1.00 |
| TAC1 | 65.7 | 1.00 | 68.9 | 1.00 |

### 3.2 Primary endpoint: the ECM-Hippo stiffness program is transcriptionally inert within a bounded null

The pre-specified primary endpoint — the M3 difference between HZ-serum exosomes and control exosomes — was -0.049 log2CPM (permutation P = 0.42; BH q = 0.46). We therefore report a bounded null: with seven versus seven samples and a 56-gene module, the minimum detectable effect at 80% power was 0.18 log2CPM, and the observed difference sits well inside its 95% confidence interval (Welch -0.18 to +0.08; permutation-inversion -0.16 to +0.06). The null was not contrast-specific: M3 was likewise unchanged under direct VZV infection (P = 0.85), under PHN exosomes (P = 0.83), and M4 mechano-effectors was null under HZ exosomes (P = 0.46) but, notably, was suppressed under direct VZV infection (-0.054; P = 0.03). At the gene level the M3 module was directionally incoherent — COL4A1 (-0.381, P = 0.005), COL4A2 (-0.627, P = 0.007), ADAMTS1 (-0.479, P = 0.013) and TEAD1 (-0.339, P = 0.047) moved downward while LOX (+0.291, P = 0.024) and YAP1 (+0.425, P = 0.18) moved upward (these are uncorrected nominal P values across 56 genes, shown only to illustrate directional incoherence) — indicating genuine null aggregation rather than cancellation of a coherent shift. We emphasize that this null is a substantive result: at the neuronal mRNA level, and within 36 hours of exosome exposure, the stiffness program does not respond to VZV-related perturbation.

### 3.3 Secondary endpoint: HZ-serum exosomes suppress electrochemical nociceptor channels with channel-class selectivity

Under the same primary contrast, the pre-specified secondary module E1 (electrochemical nociceptor channels) was significantly suppressed (-0.220 log2CPM; exact permutation P = 0.013; Welch P = 0.011; BH q = 0.034; 95% CI -0.38 to -0.06; Figure 2a), whereas all four mechano-modules were not at the full-module level (M1 -0.078, P = 0.11; M2 -0.148, P = 0.068). Gene-level analysis showed a downward shift across the classical nociceptor apparatus, but the support is weaker than a module-level claim once within-module multiplicity is considered. In an uncorrected, descriptive screen (Welch *t*; E1 n = 18 genes), TRPV1 was down (-0.567, P = 0.0009) and remained significant after Benjamini–Hochberg correction within the E1 module (q = 0.017; Figure 2c); KCNS1 (-0.393, P = 0.017), SCN9A (-0.323, P = 0.018), ASIC1 (-0.181, P = 0.019) and ASIC2 (-0.296, P = 0.042) were nominally significant but did not survive within-E1 correction (q ≈ 0.07–0.13). By contrast, no mechanogated M1 gene reached P < 0.05 (PIEZO2 P = 0.18, PIEZO1 P = 0.10, P2RX3 P = 0.076). SCN10A (Nav1.8) is excluded from the confirmed list: its mean CPM in the exosome experiment was 0.55 (detected in only 11% of samples), below the study's own detection threshold, although its nominal down-regulation (log2FC -0.384, P = 0.008, the second-strongest in E1) is reported as a floor-limited descriptive value, not a confirmed signal. PIEZO2 — the dominant mechanogated channel of this model — was not suppressed (-0.282, P = 0.18; 95% CI approximately -0.72 to +0.15), a resolution-limited null at the gene level. We therefore report the channel-class imbalance as a gene-level, nominal signal led by TRPV1 rather than a confirmed module-level selective suppression; the M1 pattern is itself resolution-limited, because restricting to detected genes flips M1 to significant (P = 0.046, §3.6), so neither "spared" nor "confirmed down" is established for M1. Critically, E1 must also be judged against its own neutral control: the per-sample (E1 - N1) difference shifted by only -0.064 log2CPM under HZ exosomes (exact permutation P = 0.178; Welch P = 0.187), i.e. E1 is not separable from N1 at the module level. The channel-class imbalance therefore survives as a gene-level, family-corrected signal led by TRPV1, not as a demonstrated module-level selectivity over control channels.

### 3.4 Route dependence tested by contrast-of-contrasts, not by significant-versus-not

To test whether the route determines which channel program shifts, we computed the interaction (difference-in-differences) between the E1 and M1 module scores. For the exosome contrast, (E1 difference - M1 difference) = -0.142 log2CPM with exact permutation P = 0.0017 (Figure 2d); for the direct-infection contrast, (M1 difference - E1 difference) = -0.051 with exact permutation P = 0.19, so the reciprocal "M1-selective" pattern is not supported at the interaction level. However, the exosome interaction does not survive a sensitivity analysis for detection-floor asymmetry between modules: M1 contains 4/9 genes below the detection threshold (each contributing ≈0 and diluting its module mean), whereas E1 contains 5/18. Restricting both modules to detected genes (mean CPM > 1) removes this dilution and yields a much smaller interaction (-0.072) that is not significant (exact permutation P = 0.16). Note that this detected-gene analysis is a *subset* sensitivity, not a multiplicity correction; it also shows M1 itself shifting downward in the detected-gene subset (P = 0.046, §3.6), so the apparent full-module selectivity is better described as dilution-limited than as a confirmed biological dissociation. The channel-class imbalance is instead suggested at the gene level on a nominal, uncorrected basis — TRPV1 survives within-E1 correction, KCNS1/SCN9A/ASIC1/2 are nominally down, and no M1 gene reaches P < 0.05 (PIEZO2 P = 0.18) — but remains hypothesis-generating pending family-corrected confirmation. We disclose that the contrast-of-contrasts interaction test was specified post hoc (not in the original frozen analysis plan) and is reported as exploratory; because two routes were tested, the nominal interaction P should be read with that multiplicity in mind (the 2-route Bonferroni-adjusted exosome interaction P = 0.0034 remains significant, but the detected-gene subset analysis above renders the selectivity non-significant). The VZV picture remains weak and inconsistent: direct infection drove M1 downward (-0.050; Welch P = 0.047) while E1 was unchanged (+0.0005; P = 0.996), and individual E1 genes were nominally down under HZ exosomes (TRPV1 P < 0.001, SCN9A P = 0.018, ASIC1/2 P ≤ 0.042) whereas no M1 gene reached significance (PIEZO2 P = 0.18), consistent with a gene-level, route-dependent E1 signal rather than a module-level selective suppression. The route dependence is one of magnitude rather than direction: TRPV1 mRNA also fell under direct VZV infection (-0.149 log2CPM, Welch P = 0.008, within-E1 q = 0.144), roughly a quarter of the HZ-exosome effect (-0.567); PIEZO2 likewise fell modestly under direct infection (-0.144, P = 0.021).

### 3.5 Exploratory PHN-exosome contrast: non-specific and confounded

PHN-serum exosomes produced larger and broader shifts than HZ exosomes: M1 (-0.119; P = 0.009; q = 0.024), E1 (-0.197; P = 0.005; q = 0.020), M2 (-0.178; P = 0.030) — but also the neutral control N1 (-0.198; P = 0.039), together with 568 genes up- and 125 down-regulated at |log2FC| > 0.5 (versus 129/174 under HZ exosomes) and a large ribosomal induction (N3 +0.577; P = 0.001; q = 0.010). Because a "specific" mechanistic signal cannot be distinguished from a neutral control module shifting in the same direction, and because the PHN donor group is older and almost exclusively female,^3^ we report this contrast as non-specific and confounded, and it plays no confirmatory role in our conclusions.

Donor-level age and sex are not present in the deposited GEO metadata for these samples (which report only cell line and treatment), so the confounding cannot be quantified from public data; it is documented in the original publication^3^ and is the reason this contrast is treated as exploratory rather than confirmatory. Gene-level P values within this contrast are reported without any claim of family-wise control, and no clinical inference about PHN as a disease of patients is drawn from it.

### 3.6 Neutral controls, calibration, and reporting discipline

Three neutral-control observations qualify the interpretation. First, N2 (olfactory receptors) reached nominal significance under HZ exosomes (-0.022; P = 0.006; q = 0.023) despite a magnitude near the detection floor: the signal rests on a single low-baseline gene (OR5A1, 0.89 CPM, 32% detection). This is precisely why the plan mandates reporting effect size alongside every P value; N2 is interpreted as a calibration benchmark, not a biological finding. Second, N3 (ribosomal proteins) was induced by HZ exosomes (+0.391; P = 0.002) and more strongly by PHN exosomes (+0.577; P = 0.001) — it behaves as an exposure (positive) control reflecting a genuine translational-program response to exosome exposure, not as a neutral baseline. Third, N1 overlaps E1 by two genes (KCNQ2, KCNQ3) that move with E1 under PHN exosomes; the N1 "control" signal under PHN therefore shares machinery with the E1 signal and is disclosed as such. Because these two genes belong to both modules, their within-module q values are family-specific and are reported separately rather than as a single number: under the primary contrast, KCNQ3 has q = 0.366 within E1 and q = 0.500 within N1, and KCNQ2 has q = 0.497 within E1 and q = 0.564 within N1; neither is significant in either family. Global-shift diagnostics confirmed no genome-wide drift confounded the module scores: per-sample mean log2CPM values were near-identical across all 19 exosome samples (range 1.55 to 1.61). The CCI did not differ between groups under any contrast (all permutation P >= 0.82; Figure 2b), consistent with the rank-based CCI being null-by-construction at the absolute scale that drives the module-level E1 signal; CCI is reported as a relative-displacement negative control, not as confirmatory evidence. A sensitivity analysis restricting module scores to detected genes (CPM > 1) left the conclusions unchanged for E1 but narrowed the M1 null: under HZ exosomes, detected-gene M1 flipped to -0.171 (P = 0.046), indicating that the "spared" M1 interpretation is resolution-limited and should be read alongside the gene-level PIEZO2 null (P = 0.18).

### 3.7 Neuronal integrity: the E1 shift is not attributable to overt injury

To distinguish a specific channel effect from a non-specific neuronal reaction or cytotoxicity, we examined the injury marker ATF3 and a pan-neuronal panel (post hoc). ATF3 was unchanged under HZ exosomes (+0.0002 log2CPM, P = 0.998), so the E1 suppression cannot be attributed to overt neuronal injury or cell loss. However, several pan-neuronal markers moved modestly in the same direction (NEFH -0.221, P = 0.006; TUBB3 -0.183, P = 0.012; NTRK1 -0.202, P = 0.031; PRPH -0.128, P = 0.048; NEFL -0.111, P = 0.053), so a mild, non-specific neuronal response accompanying the exosome exposure cannot be excluded; no marker survived Benjamini-Hochberg correction across the ten-gene panel. This pattern bounds the interpretation in both directions: it argues against cytotoxicity as the explanation for the E1 shift, while cautioning that the shift is not demonstrably channel-specific at the level of the whole transcriptome.

## 4. Discussion

### 4.1 A route-dependent, gene-level channel signal — hypothesis-generating, not a proven allodynia substrate

The central empirical contribution of this reanalysis is a gene-level channel-class imbalance: acute-HZ serum exosomes suppress the electrochemical nociceptor apparatus (led by TRPV1, with nominal down-regulation of KCNS1, Nav1.7/SCN9A and ASIC1/2) more than the mechanically gated one (E1 genes nominally down; only TRPV1 survives within-E1 correction; no M1 gene significant), while the ECM-Hippo stiffness program is inert within a bounded null. The full-module interaction that initially suggested selective E1 suppression (P = 0.0017) did not survive a detected-gene subset analysis (P = 0.16), so we do not present it as a confirmed dissociation. We deliberately do not present this as a transcriptomic "substrate for mechanical allodynia." The established mechanotransduction literature points the opposite way: allodynia is predominantly a gain of mechanosensory function — Piezo2 is a mechanotransduction channel (Woo et al., 2014) whose gain-of-function sensitizes nociceptors and increases mechanical pain sensitivity (Sánchez-Carranza et al., 2024); indeed, that same work implies allodynia requires intact Piezo2 function, whereas our data show the mechanogated channels were not up-regulated (PIEZO2 gene-level P = 0.18), so the mechanical-axis narrative is not supported by the present measurements. Piezo2 is required for mechanical pain in mice (Murthy et al., 2019) and human loss-of-function causes mechanosensation and tactile-allodynia defects (Chesler et al., 2016), and SCN9A loss-of-function causes congenital insensitivity to pain (Cox et al., 2006).

The directionality must be addressed explicitly. We observe reduced steady-state transcript of pro-nociceptive channels (TRPV1, Nav1.7, ASICs), yet PHN mechanical allodynia is a state of increased mechanosensitivity. Three non-mutually-exclusive reconciliations are biologically grounded. (i) mRNA–function decoupling: PHN allodynia is driven predominantly by post-translational sensitization of these channels (phosphorylation, trafficking, and inflammatory mediators such as NGF, PGE2 and bradykinin), so reduced steady-state transcript is fully compatible with functional hyperexcitability; the same decoupling applies to the inert M3 program, which is also largely post-translationally regulated. (ii) Exosome as host-signal readout: patient serum exosomes are a readout of the systemic milieu during acute HZ; the observed down-regulation may reflect a host-derived homeostatic or anti-nociceptive signal rather than a neuronal-autonomous pro-allodynia program, with allodynia arising where this containment fails. (iii) Model limitation: an embryonic clonal line cannot recapture in-vivo circuit-level hyperexcitability. We therefore do not present the shift as a direct allodynia mechanism; its relevance is hypothesis-generating and model-bound. Clinically, this raises a testable question: if acute-HZ serum exosomes carry a channel-suppressive signature to sensory neurons, then serial measurement of this exosome phenotype in patients from rash onset through 90 days could test whether its presence or persistence predicts progression to PHN — a hypothesis this dataset cannot answer but which frames the next clinical step. (The source study's report of up-regulated substance P is not reproduced here: TAC1 was +0.22 log2CPM, P = 0.38, under HZ exosomes.)

### 4.2 Route dependence and its implications

The interaction test shows the route of perturbation matters, but asymmetrically: exosomes from acute zoster produce a robust E1 suppression (a gene-level, nominal signal led by TRPV1), whereas direct VZV infection does not produce a statistically supported selective M1 effect. This argues against treating "VZV effects on sensory neurons" as a single biological category: intracellular viral replication and systemic extracellular-vesicle signaling are not interchangeable models, and conclusions from one cannot be exported to the other. It also identifies exosomes as the plausible carrier of the systemic-to-neuronal signal that follows acute zoster, aligning with the growing literature on extracellular-vesicle-mediated pain signaling. We note the E1≫M1 selectivity is not robust to detection-floor correction (§3.4), so the route difference is best stated as "exosomes yield a clear E1 signal; direct infection does not yield a selective M1 signal" rather than a confirmed cross-program dissociation.

### 4.3 The inert stiffness program redirects the mechanical search

Perhaps the most consequential finding for the mechanotransduction field is what did not move. The ECM-integrin-Hippo program — the transcriptional core of cellular mechanotransduction — showed no detectable transcriptional response under any perturbation route, within a bounded null (MDE 0.18 log2CPM); "no detectable response" is the claim, not "inert by mechanism". Three explanations deserve attention. (i) The program may not be neuron-intrinsic: in DRG, ECM deposition, stiffness sensing and YAP/TAZ dynamics are dominated by satellite glia, fibroblasts and endothelial cells rather than neurons, so bulk neuronal cultures are the wrong compartment to observe it. (ii) The 36-hour window captures early channel-level events, whereas ECM remodeling requires longer time constants. (iii) mRNA may be uncoupled from mechanotransduction, which is largely regulated post-translationally. Whichever applies, the practical redirection is the same: the mechanical axis in PHN should be pursued in non-neuronal compartments — DRG satellite glia, skin, and serum — and in spatially resolved tissue data. This reframing is relevant only as context for mechanotherapy: the machinery engaged by ESWT (integrin-FAK-p38MAPK; Piezo/TRP signaling) resides in those non-neuronal compartments,^10,11^ and ESWT has shown benefit in herpetic neuralgia in small trials,^4,7–9^ although the largest randomized trial reported pain reduction without a significant time-by-group interaction.^7^ We do not assert any YAP/TAZ- or neuronal-channel-specific ESWT mechanism: the cited works do not test such a mechanism, and the present data show the neuronal mechanogated and stiffness programs to be inert, so the ESWT literature is contextual background for future non-neuronal studies, not evidence supporting the present findings.

### 4.4 Limitations

Before the point-by-point constraints below, one overarching caution for clinical readers: every result in this study derives from a 36-hour exposure of an immortalized embryonic dorsal-root-ganglion clonal line (HD10.6) to patient-derived serum exosomes or VZV. No finding here describes chronic PHN biology in living patients, and the PHN-exosome donor group — the clinically most relevant contrast — is confounded by age and sex; conclusions about PHN as a disease of patients are out of scope.

This study is a secondary analysis with the following constraints, each stated at design stage. (i) The model is an immortalized embryonic DRG clonal line (HD10.6), not iPSC-derived neurons and not DRG tissue; its baseline (PIEZO2/P2RX3-high, TRPV4/STOML3-absent) differs from adult nociceptors, and all findings are model-bound. Because a single clone cannot represent the peptidergic/non-peptidergic/NF subtypes of adult DRG, the term "human sensory neurons" in this paper should be read as "this embryonic clonal line." (ii) The exosome exposure is acute (36 hours); conclusions are restricted to early molecular events and cannot be extrapolated to chronic PHN in vivo. (iii) Bulk RNA-sequencing reports neither cell-composition changes nor post-translational mechanotransduction. (iv) PHN-exosome donors are older and almost exclusively female, and the exploratory PHN contrast accordingly behaved non-specifically. (v) Two panel genes (CYR61, CTGF) were absent from the processed matrix, and TRPV4/STOML3/MMP9 were below detection, bounding the scope of M1/M3 inference (the absence of TRPV4 and STOML3 — the most mechanosensitive members of M1 — means the mechanogated module was not fully tested for mechanical-gating function; moreover P2RX3, a purinergic rather than mechanically gated receptor, dominates M1, so the "mechanogated" inference rests largely on PIEZO2, whose gene-level response was a resolution-limited null); SCN10A/Nav1.8 lay below the detection floor in the exosome experiment, so its down-regulation is descriptive only. (vi) The direct-infection M1 effect is borderline (permutation P = 0.05) and the reciprocal dissociation is unsupported by the interaction test (P = 0.19); the route-dependence claim rests on the robust E1-selective exosome effect and requires confirmation in independent models. (vii) The analysis is hypothesis-generating throughout: no causal or therapeutic claim is made. (viii) Exosome identity and cargo were not verified in this reanalysis; the neuronal response could reflect co-isolated soluble factors (cytokines, lipoproteins, free nucleic acids, ATP) rather than vesicular cargo, since standard serum-exosome preparations co-isolate such factors and no depletion/vesicle-disruption control was performed. (ix) SCN10A/Nav1.8 baseline differed markedly between the two GSE342782 experiments — mean CPM 7.23 in DirectInf versus 0.55 in SeraExo, a ~13-fold difference — constraining cross-experiment comparability of the E1 module. (x) The source study's reported up-regulation of substance P was not reproduced here (TAC1 +0.22 log2CPM, P = 0.38, under HZ exosomes); the present data show only the channel-downregulation pattern.

Three further constraints follow from the Round-4 internal benchmarks. (xi) The E1 signal is not separable from the neutral N1 control at the module level (E1 - N1 = -0.064, P = 0.178), so any claim of channel-class selectivity is nominal and gene-level, not a demonstrated module-level dissociation. (xii) Substrate stiffness, the primary determinant of cellular mechanotransduction, was neither manipulated nor measured: the neurons were cultured on standard plastic, so the absence of an ECM-Hippo response may reflect an unphysiological mechanical set-point rather than neuronal insensitivity. (xiii) The preparation is neurons alone; satellite glia, immune cells and spinal circuitry — the compartments in which PHN allodynia is generated and maintained — are absent, and the exosome dose was not independently quantified or dose-ranged, so no dose-response inference is possible.

## 5. Conclusions

In a prospectively specified reanalysis of the only available human sensory-neuron resource covering VZV infection and patient-derived serum exosomes, acute-HZ serum exosomes produced a route-dependent down-regulation of the electrogenic nociceptor program that, at the gene level and on a nominal basis, was not matched by the mechanically gated one (TRPV1 significant after within-E1 correction; KCNS1, SCN9A, ASIC1/2 nominally down; no M1 gene significant; M1 itself resolution-limited, flipping to significant when detected genes only are analyzed, P = 0.046), while the ECM-Hippo stiffness program was transcriptionally inert within a bounded null (minimum detectable effect 0.18 log2CPM) — an important negative result directing the mechanical-axis search toward non-neuronal compartments. The full-module interaction initially suggestive of selective E1 suppression (P = 0.0017) did not survive a detected-gene subset analysis (P = 0.16), so the channel-class imbalance is reported as gene-level and hypothesis-generating. The exploratory PHN-exosome contrast was non-specific and confounded by donor age and sex, and is reported as such. The relevance of these shifts to mechanical allodynia in PHN is hypothesis-generating and model-bound: all conclusions derive from a 36-h exposure of an immortalized embryonic dorsal-root-ganglion line and cannot be extrapolated to chronic PHN in living patients, but they frame a testable clinical question — whether the HZ-exosome channel-suppressive signature predicts progression to PHN.

---

## Data availability

GSE342782 (processed RSEM counts and series metadata): https://ftp.ncbi.nlm.nih.gov/geo/series/GSE342nnn/GSE342782/

Reproducibility package (analysis scripts, frozen panel `mtp-frozen-2026-10-19`, result JSON/CSV with SHA-256 MANIFEST, all figures): https://github.com/yyx-4113/mechano-phn-gse342782-reanalysis (tag v1.1.4). The package regenerates every number in this manuscript from the raw GEO files. SHA-256 checksums for all deposited artifacts are provided in `MANIFEST.json`.

## Ethics approval and consent to participate

This study is a secondary analysis of publicly available, de-identified GEO data (GSE342782). No new human-subject research, patient recruitment, or animal work was conducted; no additional ethics approval or informed consent was required beyond that of the original data deposition.^3^

## Consent for publication

Not applicable.

## Author contributions

YY conceived the study, performed the analysis, wrote the manuscript, and is solely responsible for its content.

## Acknowledgments

None.

## Declaration of interests

None declared.

## Funding

None.

## References

[1] Wang C, Zhang K, Bao Y, et al. Exploring blood transcriptomic signatures in patients with herpes zoster and postherpetic neuralgia. Front Cell Infect Microbiol. 2024;14:1425393. doi:10.3389/fcimb.2024.1425393. PMID: 39211798.

[2] Liang X, Fan Y. Bidirectional two-sample Mendelian randomization analysis reveals a causal effect of interleukin-18 levels on postherpetic neuralgia risk. Front Immunol. 2023;14:1183378. doi:10.3389/fimmu.2023.1183378. PMID: 37304287.

[3] Niemeyer CS, Frietze S, Lewis SWR, et al. Circulating exosomes drive persistent neuronal dysfunction in post-herpetic neuralgia patients. Ann Neurol. 2026. doi:10.1002/ana.78352. PMID: 42734212.

[4] Yeon JE, Ryu KH, Cho EA, et al. Efficacy of extracorporeal shockwave therapy for postherpetic neuralgia. Pain Pract. 2025;25(8):e70085. doi:10.1111/papr.70085. PMID: 41091131.

[5] Raymon HK, Thode S, Zhou J, et al. Immortalized human dorsal root ganglion cells differentiate into neurons with nociceptive properties. J Neurosci. 1999;19(13):5420-5428. doi:10.1523/JNEUROSCI.19-13-05420.1999. PMID: 10377351.

[6] Haberberger RV, Barry C, Matusica D. Immortalized dorsal root ganglion neuron cell lines. Front Cell Neurosci. 2020;14:184. doi:10.3389/fncel.2020.00184. PMID: 32636736.

[7] Chen L, Qing A, Zhu T, Yang P, Ye L. Effect and safety of extracorporeal shockwave therapy for postherpetic neuralgia: a randomized single-blind clinical study. Front Neurol. 2022;13:948024. doi:10.3389/fneur.2022.948024. PMID: 36226089.

[8] Lee SH, Ryu KH, Kim PO, et al. Efficacy of extracorporeal shockwave therapy in the treatment of postherpetic neuralgia: a pilot study. Medicine (Baltimore). 2020;99(12):e19516. doi:10.1097/MD.0000000000019516. PMID: 32195953.

[9] Chen L, Zhou R, Sun F, Weng Y, Ye L, Yang P. Efficacy and safety of extracorporeal shockwave therapy in patients with postherpetic neuralgia: study protocol of a randomized controlled trial. Trials. 2020;21:573. doi:10.1186/s13063-020-04564-z. PMID: 32641142.

[10] Ge R, Ruan B, Chen S, Bai S, Gao Q, Dong A. Radial extracorporeal shock wave therapy alleviates acute inflammation of human primary tenocytes through the integrin-FAK-p38MAPK pathway. Am J Transl Res. 2023;15(5):3229-3239. PMID: 37303680.

[11] Pan Y, Shi LZ, Yoon CW, et al. Mechanosensor Piezo1 mediates bimodal patterns of intracellular calcium and FAK signaling. EMBO J. 2022;41(17):e111799. doi:10.15252/embj.2022111799. PMID: 35844093.

[12] GSE314229 — single-cell transcriptomics of radial extracorporeal shockwave therapy identifying sEV release via ATP/P2X7R/p38MAPK signaling (Adv Sci 2026). https://ftp.ncbi.nlm.nih.gov/geo/series/GSE31nnn/GSE314229/ (accessed October 19, 2026).

[13] Cox JJ, Reimann F, Nicholas AK, et al. An SCN9A channelopathy causes congenital inability to experience pain. Nature. 2006;444(7121):894-898. doi:10.1038/nature05413. PMID: 17167479.

[14] Woo SH, Ranade S, Weyer AD, et al. Piezo2 is required for Merkel cell mechanotransduction. Nature. 2014;509(7502):622-626. doi:10.1038/nature13251. PMID: 24717433.

[15] Murthy SE, Loud MC, Daou I, et al. The mechanosensitive ion channel Piezo2 mediates sensitivity to mechanical pain in mice. Sci Transl Med. 2019;11(486):eaat9897. doi:10.1126/scitranslmed.aat9897. PMID: 30305457.

[16] Li B, Dewey CN. RSEM: accurate transcript quantification from RNA-Seq data with or without a reference genome. BMC Bioinformatics. 2011;12:323. doi:10.1186/1471-2105-12-323. PMID: 21816040.

[17] Benjamini Y, Hochberg Y. Controlling the false discovery rate: a practical and powerful approach to multiple testing. J R Stat Soc B. 1995;57(1):289-300.

[18] Sánchez-Carranza O, Chakrabarti S, Kühnemund J, et al. Piezo2 voltage-block regulates mechanical pain sensitivity. Brain. 2024;147(10):3487-3500. doi:10.1093/brain/awae227. PMID: 38984717.

[19] Chesler AT, Szczot M, Bharucha-Goebel D, et al. The role of PIEZO2 in human mechanosensation. N Engl J Med. 2016;375(14):1355-1364. doi:10.1056/NEJMoa1602812. PMID: 27653382.

[20] Dworkin RH, O'Connor AB, Backonja M, et al. Pharmacologic management of neuropathic pain: evidence-based recommendations. Pain. 2007;132(3):237-251. doi:10.1016/j.pain.2007.08.033. PMID: 17920770.
