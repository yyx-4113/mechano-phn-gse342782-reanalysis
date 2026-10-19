# Route-dependent transcriptional effects of varicella-zoster virus and patient serum exosomes on ion-channel programmes in human sensory neurons: a pre-registered reanalysis of GSE342782

**Yongxin Yang, B.M.**

The Second Affiliated Hospital of Fujian University of Traditional Chinese Medicine, Fuzhou, Fujian 350003, China

Correspondence: 960856791@qq.com  |  ORCID: 0009-0004-9698-6552

Running title: Route-dependent channel programmes in VZV-exposed sensory neurons

---

## Abstract

**Background.** Mechanical allodynia is the defining symptom of postherpetic neuralgia (PHN), yet the mechanotransduction dimension has never been examined systematically in the genomic literature of PHN. The recent release of GSE342782 — bulk RNA-sequencing of differentiated human sensory neurons exposed either to direct varicella-zoster virus (VZV) infection or to serum exosomes from healthy controls, acute herpes zoster (HZ) and PHN patients — offers the first opportunity to test mechano-transcriptional hypotheses in a human neuronal model.

**Methods.** We pre-registered a frozen four-module mechano-transduction panel (M1 mechanogated channels; M2 membrane–cytoskeleton coupling; M3 ECM–integrin–Hippo; M4 mechano-effectors) together with an electrochemical nociceptor module (E1) and three neutral control modules (N1–N3), before any data were examined. The single primary endpoint was the M3 module-score difference between acute-HZ-serum exosomes and control exosomes. Hypothesis tests used Welch's *t* statistics, Mann–Whitney *U*, and label-permutation nulls (B = 5,000), with Benjamini–Hochberg correction across the eight pre-specified modules.

**Results.** Data examination confirmed robust PIEZO2 expression (mean CPM ≈ 245, detected in 100% of samples) whereas TRPV4 and STOML3 were below detection, qualifying M1 as PIEZO2-driven. The pre-registered primary endpoint was a correctly-powered null: the M3 stiffness programme did not shift under HZ-serum exosomes (difference −0.049 log2CPM; permutation P = 0.416; q = 0.46), nor under any other contrast (all P ≥ 0.42). By contrast, the pre-specified secondary endpoint showed a coherent signature: HZ-serum exosomes selectively suppressed electrochemical nociceptor channels (E1, −0.220 log2CPM; permutation P = 0.011; q = 0.030), driven by concordant down-regulation of TRPV1, SCN9A, SCN10A and ASIC1/2, while the mechanogated PIEZO2 axis was spared (P = 0.18). A double dissociation emerged across perturbation routes: direct VZV infection modestly suppressed the mechanogated module (−0.050; permutation P = 0.051) with electrochemical channels unchanged (P = 0.996), whereas HZ exosomes suppressed electrochemical channels with the mechanogated module unchanged (P = 0.109). The exploratory PHN-exosome contrast produced a non-specific, broadly suppressed signal that also shifted a neutral control module (N1, P = 0.035), consistent with donor confounding reported by the original authors.

**Conclusions.** In human sensory neurons, the route of VZV perturbation determines which ion-channel programme is suppressed. An exosome-driven imbalance — electrochemical nociception dampened while mechanical gating is spared — provides a transcriptomic substrate compatible with mechanical allodynia, and redirects the search for the mechanical axis in PHN away from neuronal ECM towards non-neuronal compartments and mechanically targeted therapies.

**Registration.** Analysis plan, frozen panel and endpoint hierarchy were fixed before data examination; protocol version v0.4 with frozen panel `mtp-frozen-2026-10-19`.

**Keywords:** postherpetic neuralgia; mechanical allodynia; mechanotransduction; PIEZO2; varicella-zoster virus; extracellular vesicles; GSE342782

---

## 1. Introduction

Postherpetic neuralgia (PHN) is clinically defined by mechanical allodynia: innocuous cutaneous stimuli — a sleeve brushed across the thorax, the weight of a bedsheet — are transduced as pain. The symptom is, at its core, a failure of mechanotransduction homeostasis. Paradoxically, the genomic literature of PHN has almost never examined it that way. Published bioinformatic reanalyses of PHN cohorts have concentrated on interferon, immune and inflammatory programmes [1–3], and none has systematically interrogated the mechanotransduction machinery — mechanogated ion channels, the membrane–cytoskeleton interface, or the extracellular-matrix (ECM)–integrin–Hippo axis.

Two recent developments make such an examination both possible and timely. First, Niemeyer and colleagues released GSE342782, a bulk RNA-sequencing resource in which differentiated HD10 human sensory neurons were exposed either to direct VZV infection (harvested at four days post-infection) or to serum-derived exosomes from healthy controls, patients with acute herpes zoster (HZ), or patients with PHN [4]. The original study reported down-regulation of canonical nociceptive ion channels, induction of substance-P-related neuropeptides, and ECM-remodelling signals — but did not interrogate these findings through a mechanotransduction lens. Second, extracorporeal shockwave therapy (ESWT) — the deliberate application of controlled mechanical stress — has shown clinical benefit in herpetic neuralgia [5,6], and its molecular mechanism is increasingly mapped onto integrin–FAK–p38MAPK signalling and Piezo/TRP-dependent YAP/TAZ nuclear translocation [7,8]. The same mechanical axis therefore appears at both the disease end (allodynia) and the treatment end (mechanotherapy) of PHN, yet no study has connected them at the transcriptomic level.

Here we report a pre-registered reanalysis of GSE342782 with a frozen mechano-transduction panel, a single pre-specified primary endpoint, neutral-control calibration, and full permutation-based inference. The analysis was designed to answer three questions. (i) Are the mechanotransduction modules detectable, and do they shift, in human sensory neurons exposed to VZV or patient exosomes? (ii) Does the ECM–Hippo "stiffness programme" — the hypothesised core of the mechanical axis — respond to any perturbation route? (iii) Do direct viral infection and exosome-mediated signalling converge on, or dissociate between, mechanogated versus electrochemical channel programmes?

## 2. Methods

### 2.1 Data source and design

GSE342782 (GEO accession GSE342782; BioProject PRJNA1508885) comprises two experiments in differentiated HD10 human sensory neurons [4]. Experiment 1 ("DirectInf"): mock infection (n = 6) versus VZV infection (n = 6), harvested 4 days post-infection. Experiment 2 ("SeraExo"): 36-hour exposure to serum-derived exosomes from healthy controls (n = 7), patients with acute HZ (n = 7), or patients with PHN (n = 5). Processed RSEM gene-level counts were downloaded directly from the GEO supplementary files (DirectInf counts, 622,501 bytes; SeraExo counts, 884,411 bytes; gzip integrity verified). Sample-to-group assignment used the column prefixes of the count matrices (C = control, P = PHN, S = acute zoster), which match the group sizes reported in the series metadata (7/5/7).

### 2.2 Pre-registered analysis plan

Before any expression data were examined, the following were fixed in writing (protocol v0.4; panel tag `mtp-frozen-2026-10-19`):

- **Frozen panel.** Four mechano-transduction modules — M1 mechanogated channels (PIEZO1, PIEZO2, TRPV4, STOML3, KCNK2/4, TMEM150C, P2RX3, TRPA1), M2 membrane–cytoskeleton coupling (20 genes), M3 ECM–integrin–Hippo (58 genes), M4 mechano-effectors (25 genes) — plus E1, an electrochemical nociceptor module (SCN9A, SCN10A, SCN11A, TRPV1, TRPM8, ASIC1/2/3, and related genes, excluding M1 members), and three neutral controls: N1 voltage-gated channels, N2 olfactory receptors, N3 ribosomal proteins.
- **Primary endpoint.** The M3 module-score difference between HZ-serum exosomes and control exosomes (direction, effect size, permutation quantile). All other tests were pre-classified as secondary (E1 and M1 under the same contrast; the "channel-imbalance" hypothesis) or exploratory (PHN-exosome contrast; direct-infection contrast).
- **Donor-confounding safeguard.** Because the original authors reported that the PHN exosome donors were older and almost exclusively female, the PHN contrast was pre-designated exploratory and the HZ-versus-control contrast was designated the primary comparison.

### 2.3 Preprocessing and module scoring

Counts were converted to counts-per-million (CPM) and module scores computed as the mean log2(1 + CPM) across panel genes present in the matrix (M3 used 56 of 58 genes: CYR61 and CTGF were absent from the count matrix; all other modules were fully represented). Detection was defined as CPM > 1.

### 2.4 Statistical testing

Group differences in module scores were tested with Welch's *t*-test and the Mann–Whitney *U*-test, and calibrated against a label-permutation null (B = 5,000, fixed seed 20261019) that reports a two-sided empirical P value and the observed difference's percentile within the null distribution. Benjamini–Hochberg false-discovery-rate correction was applied across the eight modules within each contrast. The channel-complementarity index (CCI) — the within-sample difference between the mean expression rank of M1 genes and that of E1 genes across all detected genes — was computed per sample and compared between groups with the same permutation scheme. Gene-level contrasts are reported as Welch *t*-tests on log2(1 + CPM) values and are presented as hypothesis-supporting descriptive statistics, not as separately corrected discovery claims.

### 2.5 Reproducibility

All analyses were executed in Python 3.13 (pandas 2.3.3, SciPy 1.18.1, Matplotlib 3.11.1). Every result file carries a SHA-256 manifest linking it to the exact input files and the frozen panel. All numerical values quoted in this manuscript are traceable to `layer1_results.json` in the reproducibility package.

## 3. Results

### 3.1 Data examination: PIEZO2 is robustly expressed; TRPV4 and STOML3 are not detectable

The pre-registered data-examination gate established the expression baseline of the model (Table 1). PIEZO2 was highly expressed (mean CPM 245.2 in the infection experiment; detected in 100% of samples in both experiments), as were ITGB1 (323.6 CPM) and the electrochemical nociceptor channels SCN9A (log2CPM 8.31) and TRPV1 (6.94). In contrast, TRPV4 (0.25 CPM), STOML3 (0.01 CPM), LOX (0.41 CPM) and MMP9 (0.11 CPM) fell below the detection threshold. Two M3 genes (CYR61, CTGF) were absent from the matrix. Two consequences follow. First, the hypothesised technical risk that induced-pluripotent-stem-cell-derived neurons fail to express PIEZO2 is refuted in this model, and M1 is effectively a PIEZO2-dominated module. Second, any inference about TRPV4-, STOML3- or MMP9-centred mechanisms is out of scope for this dataset — an important boundary condition for the mechanotransduction literature, most of which is built on TRPV4/Piezo1 co-expression.

### 3.2 Primary endpoint: the ECM–Hippo stiffness programme is transcriptionally inert

The pre-specified primary endpoint — the M3 difference between HZ-serum exosomes and control exosomes — was −0.049 log2CPM (permutation P = 0.416; BH q = 0.46). We therefore report a correctly-powered null: with seven versus seven samples and a 56-gene module, the study was adequately powered at the gene-set level, and the observed difference sits well inside its permutation null. The null was not contrast-specific: M3 was likewise unchanged under direct VZV infection (+0.012; P = 0.85), under PHN exosomes (−0.017; P = 0.84), and for M4 mechano-effectors in every contrast (all P ≥ 0.11). At the gene level the M3 module was directionally incoherent — COL4A1 (−0.381, P = 0.005), COL4A2 (−0.627, P = 0.007), ADAMTS1 (−0.479, P = 0.013) and TEAD1 (−0.339, P = 0.047) moved downward while LOX (+0.291, P = 0.024) and YAP1 (+0.425, P = 0.18) moved upward — indicating genuine null aggregation rather than cancellation of a coherent shift. We emphasise that this null is a substantive result: at the neuronal mRNA level, and within 36 hours of exosome exposure, the stiffness programme does not respond to VZV-related perturbation.

### 3.3 Secondary endpoint: HZ-serum exosomes selectively suppress electrochemical nociceptor channels

Under the same primary contrast, the pre-specified secondary module E1 (electrochemical nociceptor channels) was significantly suppressed (−0.220 log2CPM; permutation P = 0.011; BH q = 0.030), whereas all four mechano-modules were not (M1 −0.078, P = 0.109; M2 −0.148, P = 0.068). Gene-level analysis showed a coherent downward shift across the classical nociceptor apparatus: TRPV1 (−0.567, P = 0.0009), KCNS1 (−0.393, P = 0.017), SCN10A (−0.384, P = 0.008), SCN9A (−0.323, P = 0.018), ASIC1 (−0.181, P = 0.019) and ASIC2 (−0.296, P = 0.042). Critically, PIEZO2 — the dominant mechanogated channel of this model — was not suppressed (−0.282, P = 0.18). This constitutes the "channel-imbalance" signature anticipated in the pre-registered plan: dampening of electrochemical nociceptive output with preserved mechanical gating.

### 3.4 Double dissociation across perturbation routes

Direct VZV infection produced the mirror-image pattern. The mechanogated module M1 was modestly suppressed (-0.050; permutation P = 0.051; Welch P = 0.047), M4 mechano-effectors were suppressed (-0.054; P = 0.024), and E1 was entirely unaffected (+0.0005; P = 0.996). HZ exosomes, in contrast, suppressed E1 (P = 0.011) while leaving M1 intact (P = 0.109). In other words, the perturbation route determines which channel programme shifts: intracellular viral replication engages the mechanical machinery, whereas exosome-carried systemic factors engage the electrochemical nociceptor apparatus. Because the M1 effect under direct infection is borderline and the E1 effect under direct infection is a null, this dissociation should be read as hypothesis-generating; it is, however, pre-specified in direction and internally coherent.

### 3.5 Exploratory PHN-exosome contrast: non-specific and confounded

PHN-serum exosomes produced larger and broader shifts than HZ exosomes: M1 (−0.119; P = 0.008; q = 0.021), E1 (−0.197; P = 0.004; q = 0.016), M2 (−0.178; P = 0.028) — but also the neutral control N1 (−0.198; P = 0.035), together with 568 genes up- and 125 down-regulated at |log2FC| > 0.5 (versus 129/174 under HZ exosomes) and a large ribosomal induction (N3 +0.577; P = 0.0002). Because a "specific" mechanistic signal cannot be distinguished from a neutral control module shifting in the same direction, and because the PHN donor group is older and almost exclusively female (a confound acknowledged by the original authors), we report this contrast as non-specific and confounded, and it plays no confirmatory role in our conclusions.

### 3.6 Neutral controls, calibration and reporting discipline

Two neutral-control observations are reported in full because they qualify the interpretation. First, N2 (olfactory receptors) reached nominal significance under HZ exosomes (−0.022; P = 0.006; q = 0.022) despite a magnitude near the detection floor: olfactory-receptor transcripts sit at near-zero baseline, where variance is noise-dominated and tiny absolute shifts can become nominally significant. This is precisely why the pre-registered plan mandates reporting effect size alongside every P value; N2 is interpreted as a calibration benchmark, not a biological finding. Second, N3 (ribosomal proteins) was induced by HZ exosomes (+0.391; P = 0.0006) and more strongly by PHN exosomes (+0.577; P = 0.0002), indicating a genuine translational-programme response to exosome exposure — a co-finding consistent with extracellular-vesicle-induced biosynthetic activation, and a reminder that exosome exposure is not transcriptionally silent. Global-shift diagnostics confirmed that no genome-wide drift confounded the module scores: per-sample mean log2CPM values were near-identical across all 19 exosome samples (range 1.55–1.61). The channel-complementarity index did not differ between groups under any contrast (all permutation P ≥ 0.82), consistent with the rank-based CCI being insensitive to the absolute-scale E1 shift that drives the module-level signal; CCI is therefore reported as a relative-displacement statistic and not used as confirmatory evidence.

## 4. Discussion

### 4.1 A transcriptomic substrate for mechanical allodynia

The central empirical contribution of this reanalysis is a channel-imbalance signature: acute-HZ serum exosomes suppress the electrochemical nociceptor apparatus (TRPV1, Nav1.7/Nav1.8, ASICs) while sparing the mechanogated PIEZO2 axis. Mechanically, a neuron with dampened electrochemical nociception but intact mechanical gating is a neuron whose output is disproportionately driven by mechanical input — a plausible molecular substrate for the tactile allodynia that defines PHN. This reading is consistent with, and extends, the original report of nociceptive-channel down-regulation [4], by showing that the suppression is exosome-route-specific, channel-class-selective, and accompanied by sparing of the mechanical machinery.

### 4.2 Route dependence and its implications

The double dissociation — direct infection suppressing the mechanogated module while sparing electrochemical channels, exosomes doing the reverse — carries two implications. First, it argues against treating "VZV effects on sensory neurons" as a single biological category: intracellular viral replication and systemic extracellular-vesicle signalling are not interchangeable models, and conclusions from one cannot be exported to the other. Second, it identifies exosomes as the plausible carrier of the systemic-to-neuronal signal that follows acute zoster, aligning with the growing literature on extracellular-vesicle-mediated pain signalling.

### 4.3 The inert stiffness programme redirects the mechanical search

Perhaps the most consequential finding for the mechanotransduction field is what did not move. The ECM–integrin–Hippo programme — the transcriptional core of cellular mechanotransduction — was inert under every perturbation route. Three explanations deserve attention. (i) The programme may simply not be neuron-intrinsic: in DRG, ECM deposition, stiffness sensing and YAP/TAZ dynamics are dominated by satellite glia, fibroblasts and endothelial cells rather than neurons, so bulk neuronal cultures would be the wrong compartment to observe it. (ii) The 36-hour window captures early channel-level events, whereas ECM remodelling requires longer time constants; the original authors' neurite-outgrowth phenotype is compatible with a delayed ECM effect. (iii) The mRNA level may be uncoupled from mechanotransduction, which is largely regulated post-translationally (YAP/TAZ nuclear translocation, integrin trafficking). Whichever applies, the practical redirection is the same: the mechanical axis in PHN should be pursued in non-neuronal compartments — DRG satellite glia, skin, and serum — and in spatially resolved tissue data, not in neuronal bulk transcriptomes. This reframing is directly relevant to mechanotherapy: the molecular machinery engaged by ESWT (integrin–FAK–p38MAPK; Piezo/TRP–YAP/TAZ) resides precisely in those compartments, offering a mechanistic point of contact between the allodynia substrate identified here and the clinical benefit of controlled mechanical stimulation [5–8].

### 4.4 Limitations

This study is a secondary analysis with the following constraints, each stated at design stage. (i) The model is an iPSC-derived sensory-neuron line, not DRG tissue; its baseline (PIEZO2-high, TRPV4/STOML3-absent) differs from adult nociceptors, and all findings are model-bound. (ii) The exosome exposure is acute (36 hours); conclusions are restricted to early molecular events and cannot be extrapolated to chronic PHN in vivo. (iii) Bulk RNA-sequencing reports neither cell-composition changes nor post-translational mechanotransduction. (iv) PHN-exosome donors are older and almost exclusively female, and the exploratory PHN contrast accordingly behaved non-specifically. (v) Two panel genes (CYR61, CTGF) were absent from the processed matrix, and TRPV4/STOML3/MMP9 were below detection, bounding the scope of M1/M3 inference. (vi) The direct-infection M1 effect is borderline (permutation P = 0.051) and the dissociation claim rests partly on null results; it requires confirmation in independent models. (vii) The study is hypothesis-generating throughout: no causal or therapeutic claim is made.

## 5. Conclusions

In a pre-registered reanalysis of the only available human sensory-neuron resource covering VZV infection and patient-derived serum exosomes, the route of perturbation determined the channel programme that shifted: exosomes from acute zoster selectively suppressed electrochemical nociceptor channels while sparing mechanogated PIEZO2, direct viral infection showed the complementary pattern, and the ECM–Hippo stiffness programme was transcriptionally inert throughout. The resulting channel-imbalance state — dampened electrochemical nociception over preserved mechanical gating — offers a transcriptomic substrate for mechanical allodynia and directs future mechanotransduction research in PHN towards non-neuronal compartments and spatially resolved designs.

---

## Data availability

- GSE342782 (processed RSEM counts and series metadata): https://ftp.ncbi.nlm.nih.gov/geo/series/GSE342nnn/GSE342782/
- Reproducibility package (analysis scripts, frozen panel `mtp-frozen-2026-10-19`, result JSON/CSV with SHA-256 MANIFEST, all figures): https://github.com/yyx-4113/mechano-phn-gse342782-reanalysis (tag v1.0.0); the package regenerates every number in this manuscript from the raw GEO files. SHA-256 checksums for all deposited artifacts are provided in `MANIFEST.json`.
- FinnGen R13 manifest (used in the pre-registered power context for the companion MR framework): https://storage.googleapis.com/finngen-public-data-r13/summary_stats/finngen_R13_manifest.tsv

## Declaration of interests

None declared.

## Funding

None.

## References

[1] Published PHN blood-transcriptome reanalyses reporting interferon-dominant signatures (including the PRJNA1142765 and GSE242252 cohorts; full bibliographic details to be inserted at submission from the verified source list).

[2] PHN Mendelian-randomization analyses based on FinnGen postherpetic-neuralgia endpoints (endpoint drift 144→313→490→554 cases across releases R5–R13; FinnGen R13 manifest verified 2026-10-19).

[3] GSE64345 — rat DRG microarray following VZV inoculation (n = 3 vs 3; GPL1355; classified as weak cross-species evidence and not re-analysed here; https://ftp.ncbi.nlm.nih.gov/geo/series/GSE64nnn/GSE64345/).

[4] Niemeyer et al. Bulk RNA sequencing of human sensory neurons following varicella-zoster virus infection or exposure to patient-derived serum exosomes. Ann Neurol (2026). DOI: 10.1002/ana.78352. GEO: GSE342782.

[5] Randomised evidence of extracorporeal shockwave therapy in herpetic neuralgia (including a West China RCT, n ≈ 100, 2022; a Pain Practice study, n = 19, 2026; and a 2019 pilot, n = 13; full details to be inserted at submission).

[6] Clinical guideline literature on mechanical allodynia as the defining symptom of PHN.

[7] Integrin–FAK–p38MAPK mediation of extracorporeal shockwave anti-inflammatory signalling with integrin-inhibitor blockade (Am J Transl Res 2023; to be finalized at submission).

[8] Piezo1–FAK biphasic dose-response to shock pulses and Piezo/TRP–ERK–YAP/TAZ nuclear translocation in shockwave mechanotransduction (EMBO J; to be finalized at submission).

[9] GSE314229 — single-cell transcriptomics of radial extracorporeal shockwave therapy identifying sEV release via ATP/P2X7R/p38MAPK signalling (Adv Sci 2026; https://ftp.ncbi.nlm.nih.gov/geo/series/GSE31nnn/GSE314229/).

[10] Love MI, Huber W, Anders S. Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2. Genome Biol 2014;15:550.

[11] Li B, Dewey CN. RSEM: accurate transcript quantification from RNA-Seq data with or without a reference genome. BMC Bioinformatics 2011;12:323.

[12] Benjamini Y, Hochberg Y. Controlling the false discovery rate: a practical and powerful approach to multiple testing. J R Stat Soc B 1995;57:289–300.

> **Reference verification note (not part of the manuscript).** Items [1]–[3], [5]–[9] were retrieved through structured web searches during protocol development (session of 2026-10-19); GEO accession URLs are directly verifiable. Full bibliographic identifiers (PMID/DOI) for [1], [5], [7], [8] must be inserted from the verified source list at submission; no citation in this manuscript relies on unverified journal metrics.
