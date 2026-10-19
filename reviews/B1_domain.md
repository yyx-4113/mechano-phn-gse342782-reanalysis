# B1 — Domain review: mechanotransduction / pain neuroscience / VZV neurovirology

**Manuscript:** `manuscript/manuscript_v1.1.5.md` — "Route-dependent transcriptional effects of varicella-zoster virus and patient serum exosomes on ion-channel programs in human sensory neurons: a prospectively specified reanalysis of GSE342782" (Yongxin Yang, B.M.)
**Venue:** Journal of Pain Research, Original Research. Reviewed as a first submission; no prior-round artifacts consulted.
**Verdict: Major revision.** The underlying analysis is statistically impeccable — I independently recomputed 30+ headline numbers from the raw counts and every one reproduced exactly — but the scholarly apparatus around it (two wrong reference records, one citation that does not support its claim, a trial protocol cited as efficacy evidence, an internal-revision-history leftover, and a title/abstract claim set stronger than the paper's own hedged conclusions) requires substantial correction before publication.

---

## A. Clinical and definitional accuracy

### A1. PHN definition sentence is clinically acceptable but the citation is indirect and the phrase "after the rash" is ambiguous

【Problem】The opening definition — "Postherpetic neuralgia (PHN) is defined by dermatomal pain persisting at least 90 days after the acute herpes zoster rash" (manuscript:33) — cites refs [1] (a blood-transcriptomics paper) and [20] (a pharmacologic-management guideline), neither of which is a definitional source, and "after the acute herpes zoster rash" conflates rash onset with rash healing.
【Evidence】manuscript:33 cites ^1,20^ for the definition. Ref [20] (Dworkin et al., Pain 2007;132:237-251, DOI verified) is a treatment-recommendations paper; ref [1] (Wang et al., Front Cell Infect Microbiol 2024;14:1425393, PMID 39211798 verified) profiles blood transcripts. The standard operational definition — pain persisting ≥90 days (3 months) after rash onset — is given by Johnson & Rice (N Engl J Med 2014;371:1526-1533) and is also stated in the source study itself ("persisting beyond 3 months after herpes zoster", Niemeyer et al., Ann Neurol 2026, PMID 42734212 verified).
【Why it matters】A journal of pain research will expect the field's definitional citation; anchoring a definition sentence to a transcriptomics paper weakens the opening claim and invites a copy-editor query.
【Specific fix】Replace the sentence with: "Postherpetic neuralgia (PHN) is defined as dermatomal pain persisting at least 90 days after the onset of the acute herpes zoster rash, and is clinically characterized in a substantial subset of patients by mechanical allodynia — innocuous cutaneous stimuli transduced as pain.^3,20^" and add: "[20a] Johnson RW, Rice AS. Postherpetic neuralgia. N Engl J Med. 2014;371(16):1526-1533. doi:10.1056/NEJMcp1403062." (or cite ref [3], Niemeyer 2026, which uses the identical 3-month threshold).

### A2. "Mechanical allodynia is a cardinal symptom of PHN" overstates its prevalence

【Problem】The abstract and introduction call mechanical allodynia "a cardinal symptom of PHN" (manuscript:17, 33), implying it is near-universal; in the clinical literature allodynia (particularly dynamic mechanical allodynia) is common but present in only a subset of PHN patients, and constant burning pain is the more universal feature.
【Evidence】manuscript:17 ("Mechanical allodynia is a cardinal symptom of postherpetic neuralgia (PHN)") and manuscript:33 ("is clinically characterized by mechanical allodynia"). The cited definitional literature describes PHN as a syndrome of constant pain, paroxysmal pain and allodynia, not allodynia alone.
【Why it matters】The entire paper is framed around allodynia as the clinical motivation; if the framing symptom is not as universal as stated, the clinical relevance claim inherits the overstatement. Reviewers with clinical pain experience will notice.
【Specific fix】Replace manuscript:33's second clause with: "…and is clinically characterized in many patients by mechanical allodynia — innocuous cutaneous stimuli transduced as pain — which motivates the focus on mechanotransduction in this reanalysis." In the abstract (manuscript:17), replace "a cardinal symptom of PHN" with "a common and disabling feature of PHN".

### A3. The Chesler 2016 citation does not support the "tactile-allodynia defects" claim

【Problem】manuscript:116 states "human loss-of-function causes mechanosensation and tactile-allodynia defects,^19^", but Chesler et al. 2016 (NEJM 375:1355-1364, PMID 27653382, DOI verified) reports selective loss of discriminative touch and proprioception in two patients; mechanical pain thresholds (pinprick, pressure) and thermal pain thresholds were essentially normal, and no allodynia phenotype was reported.
【Evidence】Verified against the published abstract and full text (PMC5911918): patients had "selective loss of discriminative touch perception" and "profoundly decreased proprioception"; Patient 1's mechanical pain thresholds including pinprick and pressure pain were similar to controls; no mention of allodynia anywhere in the report.
【Why it matters】This is a citation–claim mismatch in the paper's core mechanistic argument (the M1/Piezo2 discussion); a reader checking the reference will find the claim unsupported, and it slightly misrepresents the human genetics of PIEZO2 to the journal's pain-research audience.
【Specific fix】Replace the clause with: "…and human loss-of-function causes selective loss of discriminative touch and proprioception,^19^". If the authors want the human pain-relevant point, the correct anchor is Murthy 2018 [15] (PIEZO2 required for mechanical pain/allodynia in mice, conserved requirement implied by the human touch phenotype), not Chesler.

### A4. ESWT efficacy claims: a trial protocol is cited as evidence of benefit, and the protocol duplicates the RCT already cited

【Problem】The introduction (manuscript:35) and discussion (manuscript:126) state that ESWT "has shown benefit in small herpetic-neuralgia trials^4,7–9^", but ref [9] is a study protocol (Chen et al., Trials 2020;21:573, DOI 10.1186/s13063-020-04564-z, PMID 32641142 — title verified: "…study protocol of a randomized controlled trial"), which reports no outcomes. Furthermore, [9] is the protocol of the same West China Hospital trial whose results are reported in [7] (Chen et al., Front Neurol 2022;13:948024, PMID 36226089), so citing both as independent efficacy evidence double-counts one trial.
【Evidence】Crossref/PubMed verification of [9]: publication type is a protocol; the author list (Chen L, Zhou R, Sun F, Weng Y, Ye L, Yang P) and institution overlap with [7] (Chen L, Qing A, Zhu T, Yang P, Ye L, West China Hospital). [8] (Lee 2020, PMID 32195953) is an uncontrolled 13-patient pilot in which only within-group reductions were shown. [4] (Yeon 2025, PMID 41091131, n = 10 vs 9) showed within-group pain reduction and between-group separation only for itch measures. Only [7] is randomized, and it found no time-by-group interaction — which the manuscript does disclose accurately.
【Why it matters】"Shown benefit in small trials^4,7–9^" reads as three-plus positive trials; in truth the herpetic-neuralgia ESWT evidence base at submission is two small uncontrolled/single-blind studies plus one 100-patient RCT with a null interaction. The ESWT sentences are contextual, but overstating them invites a methods-literate reviewer to discount the whole mechanotherapy framing.
【Specific fix】In manuscript:35 and manuscript:126, replace "has shown benefit in small herpetic-neuralgia trials^4,7–9^" with: "has shown within-group benefit in small uncontrolled or single-blind studies^4,8^ and, in the largest randomized trial (n = 100), lower between-group NRS scores without a significant time-by-group interaction^7^ (protocol for that trial:^9^)". Retain ref [9] only as the protocol citation for [7], not as independent efficacy evidence.

### A5. VZV and exosome biology is accurately represented, but the paper never cites VZV neuropathogenesis literature

【Problem】The introduction attributes the disease model to VZV and serum exosomes (manuscript:33-35) yet the reference list contains no citation for VZV latency in DRG, reactivation, or VZV virology; the only VZV source is the data-deposition study [3].
【Evidence】Reference list (manuscript:174-214): the only VZV-related items are [3] (Niemeyer 2026) and the dataset accessions. The source study itself anchors its introduction in the VZV-pathogenesis literature (e.g., Gershon AA, Breuer J, Cohen JI, et al. Varicella zoster virus infection. Nat Rev Dis Primers. 2015;1:15016, verified via the source study's reference list).
【Why it matters】For a VZV-neurovirology-adjacent claim set (direct infection vs exosome route), the canonical pathogenesis review is expected by the readership; its absence also leaves the sentence "intracellular viral replication and systemic extracellular-vesicle signaling are not interchangeable models" (manuscript:122) without any virological grounding.
【Specific fix】Add to the introduction, first paragraph: "VZV establishes latency in dorsal root and cranial nerve ganglia and reactivates to cause herpes zoster and PHN.^3a^" with: "[3a] Gershon AA, Breuer J, Cohen JI, et al. Varicella zoster virus infection. Nat Rev Dis Primers. 2015;1:15016. doi:10.1038/nrdp.2015.16."

---

## B. Mechanistic interpretation

### B1. The "route-dependent channel-class signal" interpretation is honestly hedged, and the mRNA–function decoupling argument is applied consistently — this is a strength, with one residual tension in the abstract

【Problem】No over-claim remains in the body text: the full-module interaction (P = 0.0017) is disclosed as post hoc and is retracted in favor of the detected-gene subset (P = 0.16) everywhere it appears, and the E1-vs-N1 non-separability is carried into the conclusions. The residual tension is that the abstract still asserts "M1 was at most marginally shifted (P = 0.11; PIEZO2 P = 0.18)" without the disclosed detection-floor caveat (detected-only M1 flips to P = 0.046), and asserts exosomes "but not direct VZV infection" down-regulated the nociceptor program although TRPV1 itself fell under direct infection (-0.149 log2CPM, P = 0.008 — recomputed, identical to the manuscript's §3.4).
【Evidence】manuscript:21 (abstract) vs manuscript:96 (§3.4: "TRPV1 mRNA also fell under direct VZV infection (-0.149 log2CPM, Welch P = 0.008)… roughly a quarter of the HZ-exosome effect"), manuscript:106 and manuscript:138 (detected-only M1 P = 0.046 disclosed in body and conclusions).
【Why it matters】Abstracts are read without the body; a reader who checks only the abstract receives a cleaner dichotomy than the paper itself endorses. This is exactly the coherence issue this journal's editors police.
【Specific fix】Replace the abstract sentence "M1 was at most marginally shifted (P = 0.11; PIEZO2 P = 0.18), and E1 was not separable from its neutral control (E1 - N1 = -0.064, P = 0.18)" with: "M1 was not significantly shifted at the full-module level (P = 0.11; PIEZO2 P = 0.18) but flipped to nominal significance when restricted to detected genes (P = 0.046), so M1 is resolution-limited rather than confirmed spared; and E1 was not separable from its neutral control (E1 - N1 = -0.064, P = 0.18)". Add to the abstract's Conclusions sentence: "…while direct VZV infection produced only a smaller, gene-level TRPV1 decrease without a module-level E1 shift."

### B2. "Piezo/TRP signaling" is only half-supported by the cited mechanism papers

【Problem】manuscript:35 and manuscript:126 attribute ESWT's proposed mechanisms to "integrin-FAK-p38MAPK and Piezo/TRP signaling in non-neuronal model systems;^10,11^", but neither cited paper involves a TRP channel: [10] is integrin-FAK-p38MAPK in TNF-α-stimulated human tenocytes (verified), and [11] is Piezo1-mediated bimodal Ca²⁺/FAK signaling under laser-induced shockwaves in non-neuronal cells (verified).
【Evidence】[10] Ge et al., Am J Transl Res 2023;15:3229-3239 (PMID 37303680, abstract verified: rESWT → FAK phosphorylation up, p38MAPK phosphorylation down in tenocytes). [11] Pan et al., EMBO J 2022;41(17):e111799 (PMID 35844093, abstract verified: Piezo1, laser-induced shockwaves, Ca²⁺ and FAK, SHP2 intermediate; no TRP family member).
【Why it matters】"Piezo/TRP" implies a channel family the citations do not cover; since the manuscript elsewhere prides itself on citing only what its references support, this is an avoidable inconsistency that a mechanosensation reviewer will flag.
【Specific fix】Replace both occurrences of "Piezo/TRP signaling" with "Piezo1–FAK signaling", i.e. "…and Piezo1–FAK signaling in non-neuronal model systems;^10,11^".

### B3. TRPA1 is listed as a mechanogated channel without acknowledging that its direct mechanosensitivity is contested

【Problem】M1 is defined as "mechanogated channels" and includes TRPA1 (manuscript:49), but TRPA1's status as a directly mechanogated channel is contested in the current mechanosensation literature (it is firmly implicated in inflammation- and injury-related mechanical hypersensitivity, while direct mechanical gating has been repeatedly challenged).
【Evidence】manuscript:49 (frozen panel M1 = PIEZO1, PIEZO2, TRPV4, STOML3, KCNK2/4, TMEM150C, P2RX3, TRPA1). My recomputation confirms TRPA1 is effectively undetected in this dataset (mean CPM 0.02 in the exosome experiment), so the error is currently harmless to the results — but the panel definition as written is not defensible per the current literature.
【Why it matters】The frozen panel is a methods artifact readers will reuse; propagating an outdated "TRPA1 = mechanogated" claim in a mechanotransduction paper is exactly the kind of domain error this venue should not carry.
【Specific fix】In manuscript:49, append to the M1 definition: "(TRPA1 is included for completeness; its direct mechanical gating is debated in the current literature, and it is effectively undetected in this dataset)". No re-analysis needed since TRPA1 sits at the detection floor.

### B4. The E1 "classical nociceptor" module mixes ligand-gated synaptic receptors with voltage-gated nociceptor channels, and the paper should justify or tighten it

【Problem】E1 is described as "the electrochemical nociceptor module (SCN9A, SCN10A, SCN11A, TRPV1, TRPM8, ASIC1/2/3, and related genes)" (manuscript:19, 49) but the actual 18 genes include GRIA1, GRIA2, GRIN2B (ionotropic glutamate receptors), P2RX7 (purinergic, not nociceptor-specific) and CACNA1H (T-type Ca²⁺ channel); three of these five are below the detection floor in the exosome experiment (GRIA1 0.08 CPM, GRIN2B 0.29, TRPM8 0.52 — recomputed).
【Evidence】Frozen panel `mtp_panel.json` E1 list vs manuscript:19's abbreviated description; my recomputed E1 detection-floor genes: SCN10A (0.55), TRPM8 (0.52), KCNQ3 (0.78), GRIN2B (0.29), GRIA1 (0.08 CPM).
【Why it matters】The E1-vs-N1 non-separability (E1 - N1 = -0.064, P = 0.178) is the paper's most important qualification, and module heterogeneity is a plausible contributor; conversely, I verified that a tightened canonical-channel E1 gives a *stronger* signal (13 genes: diff -0.244, permutation P = 0.0023), so tightening costs the paper nothing and strengthens the claim.
【Specific fix】Either add one sentence to §2.2 justifying each non-canonical member (e.g., GRIA1/GRIA2/GRIN2B as excitatory receptors reported in human DRG neurons per Nguyen 2021 [21]), or re-run the sensitivity I specify: "E1-core = SCN9A, SCN10A, SCN11A, TRPV1, TRPM8, ASIC1, ASIC2, ASIC3, KCNS1, KCNQ2, KCNQ3, CACNA2D1, CACNA2D2; module score = mean log2(1+CPM); HZ-exo vs control-exo, Welch t and exact permutation; report diff, both P values, and 95% CI." Expected values from my recomputation: diff = -0.244 log2CPM, permutation P = 0.0023 (Welch P = 0.0037); detected-only subset (10 genes): diff = -0.257, P = 0.0029.

### B5. The median-of-ratios robustness check is correctly concluded but is described differently from how it must have been computed

【Problem】§2.3 (manuscript:55) describes the robustness check as "a DESeq2-style median-of-ratios normalization at matched scale" and reports E1 -0.194 / P = 0.015, M3 -0.024 / P = 0.64. However, re-normalizing SF-scaled counts back to CPM is mathematically identical to plain CPM (CPM is scale-invariant), so the reported values cannot come from "MOR-normalized CPM" as described; they reproduce exactly only if size factors are computed on the CPM matrix (17,922 genes with non-zero counts in all 19 samples) and applied as log2(1 + CPM/SF). The artifact's stored size factors (counts-based, e.g., C11 = 1.0671) are not the ones that generate the reported module values.
【Evidence】My recomputation: MOR-then-CPM gives E1 -0.2196 (identical to plain CPM, as expected from scale invariance); log2(1 + CPM/SF_CPM) gives E1 -0.1940, permutation P = 0.0152, M3 -0.0237, P = 0.6399, interaction -0.1358, P = 0.0017 — matching `layer1_norm_robustness.json` to 3-4 decimals; the JSON's stored size factors match my counts-based SFs (C11 = 1.0671 etc.) but do not generate those module values.
【Why it matters】The robustness claim itself survives under any variant (E1 remains significant, M3 remains null), so no conclusion is threatened — but the methods sentence describes a computation that cannot produce the quoted numbers, which is a reproducibility defect in a paper whose selling point is exact reproducibility.
【Specific fix】Replace the sentence in §2.3 with: "…the primary contrast was repeated under a DESeq2-style median-of-ratios sensitivity: size factors were computed as the median of CPM/gene-wise-geometric-mean ratios across the 17,922 genes with non-zero counts in all 19 exosome samples and applied on the CPM scale as log2(1 + CPM/size factor); every headline conclusion was unchanged (E1 -0.194, permutation P = 0.015; M3 -0.024, P = 0.64; E1 - M1 interaction P = 0.0017)." Also align the size factors stored in `layer1_norm_robustness.json` with the transform actually used.

---

## C. Literature coverage and reference integrity

### C1. Reference [15] (Murthy) has the wrong year, volume and issue

【Problem】The reference list gives "Sci Transl Med. 2019;11(486):eaat9897" but the paper was published in 2018, volume 10, issue 462.
【Evidence】PubMed record PMID 30305457: "Sci Transl Med. 2018 Oct 10;10(462):eaat9897"; Crossref DOI 10.1126/scitranslmed.aat9897: volume 10, issue 462, published 2018-10-10; the correct citation also appears in the reference list of Sánchez-Carranza 2024 [18].
【Why it matters】A miscited volume/year/issue on one of the paper's two central mechanotransduction references is a basic reference-integrity error that reviewers and editors check first.
【Specific fix】Replace with: "[15] Murthy SE, Loud MC, Daou I, et al. The mechanosensitive ion channel Piezo2 mediates sensitivity to mechanical pain in mice. Sci Transl Med. 2018;10(462):eaat9897. doi:10.1126/scitranslmed.aat9897. PMID: 30305457."

### C2. Reference [21] (Nguyen) lists two authors who are not on the paper

【Problem】The reference reads "Nguyen MQ, von Buchholtz LJ, Reker AN, Rycroft KM, Ma J" but the eLife paper's authors are Nguyen, von Buchholtz, Reker, Ryba and Davidson; "Rycroft KM" and "Ma J" do not appear.
【Evidence】PubMed PMID 34825887 and the eLife article page (DOI 10.7554/eLife.71752): authors are Minh Q Nguyen, Lars J von Buchholtz, Ashlie N Reker, Nicholas JP Ryba, Steve Davidson. Crossref confirms the same five.
【Why it matters】[21] carries the paper's only citation for adult human DRG class structure and for the claim that "PIEZO2 is widely expressed across adult human DRG neuronal classes" (manuscript:132) — a wrong author list on that reference undermines the model-biology discussion.
【Specific fix】Replace with: "[21] Nguyen MQ, von Buchholtz LJ, Reker AN, Ryba NJP, Davidson S. Single-nucleus transcriptomic analysis of human dorsal root ganglion neurons. Elife. 2021;10:e71752. doi:10.7554/eLife.71752. PMID: 34825887."

### C3. Reference [12] is a GEO accession, not the publication it describes

【Problem】Ref [12] cites the dataset (GSE314229, "Adv Sci 2026") instead of the journal article whose claim the manuscript relies on ("in bone-callus single-cell data, ESWT released extracellular vesicles through an ATP/P2X7R/p38MAPK axis acting on mesenchymal rather than neuronal cells").
【Evidence】The study exists as a publication: Xie X, et al. "Early radial extracorporeal shockwave stimulation on proximal tibial circular osteotomy site enhanced heterotopic skin wound healing via small extracellular vesicles." Adv Sci (Weinh). 2026;13(16):e17257; DOI 10.1002/advs.202517257; PMID 41504389; GEO GSE314229 / BioProject PRJNA1390297. The abstract confirms: "Single-cell sequencing revealed mesenchymal stem cells as the likely sEV source, with rESWT triggering sEV release through ATP/P2X7R/p38MAPK pathway" — so the manuscript's substantive claim is accurate; only the citation form is wrong.
【Why it matters】A GEO accession is not a peer-reviewed source and carries no author accountability; journals do not accept dataset links in place of the article for a mechanistic claim.
【Specific fix】Replace with: "[12] Xie X, et al. Early radial extracorporeal shockwave stimulation on proximal tibial circular osteotomy site enhanced heterotopic skin wound healing via small extracellular vesicles. Adv Sci (Weinh). 2026;13(16):e17257. doi:10.1002/advs.202517257. PMID: 41504389. (Data: GSE314229.)" Optionally note in §4.3 that the study concerns wound healing in a rat osteotomy model, not pain.

### C4. The foundational Piezo2 mechanotransduction papers are missing

【Problem】The manuscript's central claim that "Piezo2 is a mechanotransduction channel" (manuscript:116) is cited to Woo 2014 [14], which is specifically about Merkel-cell mechanotransduction; the discovery and DRG-expression papers that ground the claim are absent.
【Evidence】[14] (Woo et al., Nature 2014;509:622-626, verified) shows Piezo2 is required for Merkel-cell mechanotransduction. The canonical citations — Coste B, et al. Piezo1 and Piezo2 are essential components of distinct mechanically activated cation channels. Science. 2010;330:55-60; and Ranade SS, et al. Piezo2 is the major transducer of mechanical forces for touch sensation in mice. Nature. 2014;516:121-125 — are both verifiable (they appear in [18]'s reference list).
【Why it matters】A mechanotransduction-focused paper in a pain journal must anchor "Piezo2 is a mechanotransduction channel" to the discovery/DRG papers; citing only the Merkel-cell paper leaves the nociceptor-relevant expression claim (Nguyen 2021) doing all the work.
【Specific fix】Add the two references and amend the sentence: "Piezo2 is a mechanically activated cation channel expressed by touch receptors and by a large fraction of DRG neurons,^14,18a,18b^…" with: "[18a] Coste B, Mathur J, Schmidt M, et al. Piezo1 and Piezo2 are essential components of distinct mechanically activated cation channels. Science. 2010;330(6001):55-60. doi:10.1126/science.1193270. [18b] Ranade SS, Woo SH, Dubin AE, et al. Piezo2 is the major transducer of mechanical forces for touch sensation in mice. Nature. 2014;516(7529):121-125. doi:10.1038/nature13912."

### C5. The "growing literature on extracellular-vesicle-mediated pain signaling" claim is uncited

【Problem】§4.2 (manuscript:122) asserts that identifying exosomes as the plausible systemic-to-neuronal carrier is "aligning with the growing literature on extracellular-vesicle-mediated pain signaling" — with no reference number attached anywhere in that paragraph.
【Evidence】manuscript:122, second sentence; the paragraph cites nothing. Verified candidate sources exist: Simeoli R, et al. Exosomal cargo including microRNA regulates sensory neuron to macrophage communication after nerve trauma. Nat Commun. 2017;8:1778 (PMID 29176651); Picco F, et al. Macrophage to neuron communication via extracellular vesicles in neuropathic pain conditions. Heliyon. 2025;11(1):e41268 (PMID 39811367) — the latter directly shows macrophage-to-sensory-neuron EV transfer (miR-155 → Ship1/IL-6) attenuating neuropathic mechanical hypersensitivity.
【Why it matters】An uncited field-level claim is exactly what an independent reviewer is instructed to flag; it also undersells the paper's most translational paragraph.
【Specific fix】Append to the sentence: "…aligning with the growing literature on extracellular-vesicle-mediated pain signaling, in which DRG-neuron- and macrophage-derived EVs bidirectionally regulate nociceptive signaling and neuropathic mechanical hypersensitivity.^18c,18d^" with: "[18c] Simeoli R, et al. Nat Commun. 2017;8:1778. doi:10.1038/s41467-017-01841-5. PMID: 29176651. [18d] Picco F, et al. Heliyon. 2025;11(1):e41268. doi:10.1016/j.heliyon.2024.e41268. PMID: 39811367."

### C6. Minor: DRG class citation would be strengthened by the mouse taxonomy paper, and "none has systematically interrogated" is an unverifiable absolute

【Problem】manuscript:33 claims "none has systematically interrogated the mechanotransduction machinery" (an absolute that cannot be verified from one cited paper), and the DRG-class discussion cites only the human snRNA-seq paper [21] with no mouse counterpart.
【Evidence】manuscript:33; [1] (Wang 2024) is the sole citation for the prior-literature characterization and is a single blood-transcriptomics study.
【Why it matters】"None has…" is falsifiable by a single counterexample a reviewer might know (e.g., skin/DRG transcriptomic studies in zoster or neuropathic pain that report mechanosensation gene sets); an over-broad novelty claim invites a challenge the authors cannot win.
【Specific fix】Soften to "to our knowledge, no published reanalysis has systematically interrogated the mechanotransduction machinery in PHN transcriptomic data,^1^" and optionally add the mouse DRG taxonomy for class context: "[21a] Usoskin D, et al. Unbiased classification of sensory neuron types by large-scale single-cell RNA sequencing. Nat Neurosci. 2015;18(1):145-153. doi:10.1038/nn.3881."

---

## D. Model biology

### D1. PTK2 (FAK) is silently duplicated between modules M3 and M4

【Problem】The frozen panel lists PTK2 in both M3 (ECM-integrin-Hippo, the primary-endpoint module) and M4 (mechano-effectors); the manuscript's panel description (manuscript:49) does not disclose this, and no sensitivity analysis addresses it.
【Evidence】`analysis/config/mtp_panel.json`: M3 contains "…P4HA1, P4HA2, PTK2, ILK…" and M4 contains "PTK2, SRC, YES1…". This matters specifically because the paper's ESWT-mechanism sentence invokes "integrin-FAK-p38MAPK" (manuscript:35, 126) — FAK is literally a member of both modules whose nulls the paper reports.
【Why it matters】A duplicated gene across a primary-endpoint module and a secondary module is a panel-construction defect; if a reader finds it before the authors disclose it, the "frozen panel" rigor claim is damaged. (My sensitivity recomputation shows the conclusions are unaffected: M3 minus PTK2 = -0.0475, permutation P = 0.435; M4 minus PTK2 = -0.0238, P = 0.524.)
【Specific fix】Add to §2.2: "PTK2 (FAK) appears in both M3 and M4; excluding it from either module did not change any conclusion (M3 minus PTK2: -0.048 log2CPM, P = 0.44; M4 minus PTK2: -0.024, P = 0.52)." Alternatively, remove PTK2 from M4 in a documented panel amendment.

### D2. HD10.6 is appropriate for the questions asked, and the paper's model caveats are accurate — one residual overreach in the title's "human sensory neurons"

【Problem】The model choice is defensible and well-caveated (immortalized embryonic v-myc line, tetracycline-regulatable, nociceptive phenotype per Raymon 1999 and Haberberger 2020 — both verified), and the limitations explicitly retitle "human sensory neurons" as "this embryonic clonal line" (manuscript:132). The residual issue is that the title itself (manuscript:1) still says "human sensory neurons" without qualification.
【Evidence】manuscript:1 (title) vs manuscript:132 ("the term 'human sensory neurons' in this paper should be read as 'this embryonic clonal line'"). Nothing biologically implausible was found for this model: PIEZO2-high (164 CPM) is consistent with adult human DRG class structure (Nguyen 2021: PIEZO2 across multiple classes, low in peptidergic nociceptors — verified); P2RX3-dominant M1 (470 CPM) and TRPV4/STOML3/MMP9 undetectability are internally consistent; the SCN10A cross-experiment baseline difference (7.23 vs 0.55 CPM, recomputed) is disclosed.
【Why it matters】Titles are indexed and quoted without the body; an unqualified "human sensory neurons" title on an embryonic clonal-line study is the single most likely phrase to be quoted out of context.
【Specific fix】Retitle to: "Route-dependent transcriptional effects of varicella-zoster virus and patient serum exosomes on ion-channel programs in an immortalized human sensory-neuron line (HD10.6): a prospectively specified reanalysis of GSE342782". (Keep the running title as is.)

---

## E. Title / abstract / results / discussion coherence

### E1. An undisclosed revision-history artifact survives in the limitations

【Problem】§4.4 (manuscript:134) begins "Three further constraints follow from the Round-4 internal benchmarks." In a first submission there is no "Round 4"; this sentence references an internal revision history the reader cannot see and implies undisclosed prior peer review.
【Evidence】manuscript:134, first clause. (Consistently, the deposited extra-checks artifact carries a matching provenance note — but neither belongs in the manuscript text.)
【Why it matters】This is the single most damaging sentence in the manuscript for a first-submission review: it signals that the text was not prepared for this venue's process, and an editor may question the "prospectively specified" framing more broadly. It must be removed.
【Specific fix】Replace the opening clause with: "Three further constraints deserve emphasis."

### E2. The title's "route-dependent transcriptional effects" asserts more than the paper's own conclusions support

【Problem】The title states route dependence as an established transcriptional effect, whereas the paper's conclusion is that the channel-class imbalance is gene-level, nominal, hypothesis-generating, that the interaction is dilution-limited (P = 0.16 among detected genes), and that direct infection yields no supported M1 effect (interaction P = 0.19).
【Evidence】manuscript:1 (title) vs manuscript:96 (interaction non-significant in detected-gene subset; "dilution-limited than as a confirmed biological dissociation"), manuscript:122 ("best stated as 'exosomes yield a clear E1 signal; direct infection does not yield a selective M1 signal'"), manuscript:138 (conclusions: "hypothesis-generating").
【Why it matters】Title–conclusion mismatch on the paper's headline claim is a standard desk-rejection or major-revision trigger at this venue; it also contradicts the paper's otherwise exemplary self-hedging.
【Specific fix】Retitle to: "Divergent effects of direct varicella-zoster virus infection and patient serum exosomes on ion-channel programs in an immortalized human sensory-neuron line: a prospectively specified reanalysis of GSE342782" (or, if the authors prefer to keep "route-dependent", add "gene-level, hypothesis-generating" to the subtitle).

### E3. Two smaller reporting-precision issues

【Problem】(a) §3.3 calls SCN10A's nominal down-regulation "the second-strongest in E1", but by effect size it is third (TRPV1 -0.567, KCNS1 -0.393, SCN10A -0.384 — recomputed); by P value it is second (0.0009, 0.0076, 0.0174). (b) The M3 "minimum detectable effect at 80% power was 0.18 log2CPM" is computed from the observed SD and is a post hoc sensitivity, not a design-stage power calculation, and is not labeled as such.
【Evidence】manuscript:92 ("the second-strongest in E1"); my recomputed E1 gene-level ranking confirms both rankings. manuscript:88 ("the minimum detectable effect at 80% power was 0.18 log2CPM"); I verified the value itself (3.04 × pooled SD 0.1095 × √(2/7) = 0.178 ≈ 0.18, using the observed SD).
【Why it matters】(a) is ambiguous in a sentence that supports the paper's central gene-level claim; (b) conflates observed power with design power, a distinction this journal's statistically literate readers will notice.
【Specific fix】(a) Replace "the second-strongest in E1" with "the second-smallest P value within E1". (b) Replace with "the minimum detectable effect at 80% power, computed from the observed group SDs as a post hoc sensitivity, was 0.18 log2CPM".

### E4. Reproducibility-package version drift

【Problem】The manuscript (v1.1.5) points to a deposited package tagged v1.1.4, and claims "The package regenerates every number in this manuscript" — a version mismatch between manuscript and artifact.
【Evidence】manuscript:3 (version v1.1.5) vs manuscript:146 ("(tag v1.1.4)").
【Why it matters】Small, but it is the kind of detail a reproducibility-focused editor checks; my own recomputation confirms the deposited pipeline does regenerate the numbers, so retagging is trivial.
【Specific fix】Update the tag reference to the v1.1.5 deposit (or state "tag v1.1.5 or later").

---

## § Stands up (verified correct — do not change)

1. **Every recomputed statistic matches.** I independently recomputed from the raw GEO counts: M3 primary endpoint (-0.0489 vs manuscript -0.049; permutation P = 0.4219 vs 0.42; Welch CI -0.176/+0.079 vs "-0.18 to +0.08"; MDE 0.1786 vs 0.18); E1 (-0.2196, P = 0.0128, q = 0.0342, CI -0.377/-0.062 vs "-0.220, P = 0.013, q = 0.034, CI -0.38 to -0.06"); M1 (-0.0780, P = 0.1131); N1 (-0.1558, P = 0.1509); N3 (+0.3914, P = 0.0017); interaction (-0.1417, P = 0.0017); detected-only interaction (-0.0718, P = 0.1573 vs "-0.072, P = 0.16"); E1 - N1 (-0.0638, P = 0.1783 vs "-0.064, P = 0.18"); TRPV1 (-0.567, P = 0.0009, within-E1 q = 0.0165 vs 0.017); KCNS1/SCN9A/ASIC1/ASIC2 q = 0.069-0.127 (vs "0.07-0.13"); PIEZO2 (-0.282, P = 0.1816, CI -0.718/+0.154 vs "-0.282, P = 0.18, CI approximately -0.72 to +0.15"); VZV-vs-mock M1 (perm P = 0.0498, Welch 0.0466); VZV TRPV1 (-0.1487, P = 0.0080); VZV PIEZO2 (-0.1438, P = 0.0213); TAC1 (+0.2176, P = 0.3771); ATF3 (+0.0002, P = 0.9983); all five pan-neuronal markers (NEFH -0.2205/P = 0.0061 … NEFL -0.1113/P = 0.0526); the M3 gene-level incoherence values (COL4A2 -0.627/P = 0.0073; ADAMTS1 -0.479/P = 0.0130; COL4A1 -0.381/P = 0.0052; TEAD1 -0.339/P = 0.0469; LOX +0.291/P = 0.0240; YAP1 +0.425/P = 0.1834); KCNQ2/KCNQ3 within-family q values (0.497/0.366 in E1; 0.564/0.500 in N1); the entire Table 1 detection baseline (PIEZO2 245.2/164.1 CPM; P2RX3 806.8/470.6; SCN10A 7.23/0.55 with 11% detection; TRPV4 0.25/0.19; STOML3 0.01/0.00; ITGB1 323.6/360.3; SCN9A log2CPM 8.31/8.39; TRPV1 6.94/7.02; OR5A1 0.89 CPM, 32% detection); the ribosomal shift (138 RPL/RPS genes, 3.23% → 4.22% of library, recomputed exactly); per-sample mean log2CPM range 1.553-1.605 (vs "1.55 to 1.61"); CCI null (P = 0.83, sign convention rank(M1) - rank(E1), reproduced with average-tie ranks); and the group assignment itself (series-matrix sample titles confirm 7 control / 5 PHN / 7 acute-zoster EV groups, C/P/S prefixes correct). All values identical to the manuscript.

2. **The PHN definition is clinically standard.** "Dermatomal pain persisting at least 90 days after the acute herpes zoster rash" matches the operational definition used in the source study ("persisting beyond 3 months after herpes zoster", Niemeyer 2026, verified) and the wider clinical literature; only the citation anchor needs strengthening (item A1).

3. **The characterization of the source study is accurate.** "Down-regulation of canonical nociceptive ion channels, induction of substance-P-related neuropeptides, and ECM-remodeling signals" (manuscript:35) matches the Niemeyer 2026 abstract verbatim in substance ("Canonical nociceptive ion channels were downregulated whereas substance P was upregulated"; "elevated extracellular matrix remodeling pathways"); the donor age/sex confounding attribution is consistent with the brief's note.

4. **The ESWT trial characterization is accurate where it counts.** The manuscript's claim that "the largest randomized trial reported pain reduction without a significant time-by-group interaction" [7] is exactly right (Chen 2022, n = 100: "There was no time × group interaction in the mixed model analysis", NRS and SDS lower in the ESWT group) — verified against the published abstract. Yeon 2025 [4] and Lee 2020 [8] are correctly described as small studies. Only the protocol-as-evidence issue (A4) needs fixing.

5. **The mechanosensation interpretation is literature-consistent.** Piezo2 gain-of-function sensitizing nociceptors and driving ongoing activity via relief of voltage block [18] is an accurate reading of Sánchez-Carranza 2024 ("hyper-sensitive PIEZO2 channels were sufficient alone to drive ongoing activity, even in isolated nociceptive neurons"); "Piezo2 is required for mechanical pain" [15] is accurate (Murthy 2018: capsaicin- and SNI-induced allodynia absent in Piezo2-deficient mice); the PIEZO2-across-human-DRG-classes claim [21] is accurate (Nguyen 2021: PIEZO2 high in proprioceptive H15, H9, H12 and H10 classes, low in peptidergic nociceptors). The mRNA–function decoupling argument is applied *consistently* — to E1 (down transcript, sensitized function), to M1/Piezo2 (unchanged transcript, post-translationally sensitized function), and to M3 — and the paper explicitly states the symmetry obligation and honors it (manuscript:116).

6. **The "hypothesis-generating" framing is honest throughout.** Every place a stronger claim was available, the paper withdraws it: the primary endpoint is reported as a bounded null with an MDE; the module-level interaction is retracted in favor of the detected-gene subset; the E1-vs-N1 non-separability is disclosed in abstract, results, discussion and conclusions; the PHN contrast is declared non-specific and confounded; the post hoc nature of the interaction test is disclosed with a Bonferroni-adjusted value; the CCI is reported as a null negative control rather than spun. This is unusually disciplined reporting and should be preserved verbatim.

7. **The E1 finding is robust to the module-construction concerns I raise.** Tightening E1 to canonical nociceptor channels strengthens it (13 genes: -0.244, P = 0.0023), and removing the N1-overlapping genes leaves it essentially unchanged (-0.223, P = 0.0023); the E1-vs-N1 difference remains non-significant either way (-0.072, P = 0.174 without shared genes). The binding constraint on interpretation is therefore the N1 calibration, not module composition — and the paper says so.

---

## § Questions for the authors

1. Can you provide timestamped evidence (repository tag/commit creation date) that protocol v0.4 and panel `mtp-frozen-2026-10-19` predate data examination, given that the GEO series became public on 02 Sep 2026 and the panel tag is dated 19 Oct 2026?
2. Which size-factor construction generated the median-of-ratios values in `layer1_norm_robustness.json` (E1 -0.194 etc.)? My recomputation reproduces them exactly only with CPM-derived size factors, while the JSON stores counts-derived size factors — which is authoritative?
3. Was the M3 primary endpoint re-run with CCN1/CCN2 aliases included (the artifact's `sensitivity_m3_alias_ccn1_ccn2` shows -0.048, P = 0.42, unchanged)? If so, why is this not mentioned in §3.2?
4. Do you plan to request the donor-level age/sex table from the original authors to quantify the PHN-donor confounding, or is the qualitative attribution from the source study the final position?
5. In §3.3, "the second-strongest in E1" — by effect size or by P value? (They give different answers; see item E3.)
6. Should E1 include GRIA1/GRIA2/GRIN2B and P2RX7 as "classical nociceptor" members, given that three of the five non-canonical members sit at the detection floor in the exosome experiment?
7. Is the exosome dose (particle equivalents per mL) for the 36-h exposure reported anywhere in the source study? This bounds any dose-response speculation.
8. Do you consider TRPA1's inclusion in M1 defensible given the contested mechanogating literature, and would you accept the parenthetical qualification proposed in item B3?

---

## § What I actually checked

**Files read in full:** `manuscript/manuscript_v1.1.5.md` (all sections including abstract, tables, data availability, ethics, all 21 references); `analysis/config/mtp_panel.json` (frozen panel); `analysis/results/layer1/layer1_results.json`; `layer1_global_de.csv`; `layer1_extra_checks.json`; `layer1_norm_robustness.json`; raw inputs `GSE342782_Processed_DirectInf_neuronHD10s_BulkSeq_Counts.csv.gz`, `GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz`, `GSE342782_series_matrix.txt.gz`.

**Independent recomputations from the raw counts** (CPM → log2(1+CPM) → per-gene module means; Welch t; exact label permutation over all C(n1+n2, n1) partitions; BH within module), manuscript value vs my value — all identical:
M3 primary -0.049 / P 0.42 (mine -0.0489 / 0.4219); E1 -0.220 / P 0.013 / q 0.034 (mine -0.2196 / 0.0128 / 0.0342); M1 -0.078 / P 0.11 (-0.0780 / 0.1131); N1 -0.156 / P 0.151 (-0.1558 / 0.1509); N3 +0.391 / P 0.002 (+0.3914 / 0.0017); interaction -0.142 / P 0.0017 (-0.1417 / 0.0017); detected-only interaction -0.072 / P 0.16 (-0.0718 / 0.1573); E1-N1 -0.064 / P 0.178 (-0.0638 / 0.1783); TRPV1 -0.567 / P 0.0009 / q 0.017 (-0.567 / 0.0009 / 0.0165); PIEZO2 -0.282 / P 0.18 (-0.282 / 0.1816); VZV-vs-mock M1 P 0.05 (0.0498); VZV TRPV1 -0.149 / P 0.008 (-0.1487 / 0.0080); M3 MDE 0.18 (0.1786); detection baseline all 10 Table-1 rows (identical); ribosomal shift 138 genes 3.23%→4.22% (identical); per-sample mean log2CPM 1.55-1.61 (1.553-1.605); CCI null P ≥ 0.82 (0.83, reproduced with average-tie ranks; sign convention rank(M1)-rank(E1) = -5016/-4933, identical); MOR robustness E1 -0.194 / P 0.015 and M3 -0.024 / P 0.64 and interaction P 0.0017 (reproduced as -0.1940/0.0152, -0.0237/0.6399, -0.1358/0.0017 using CPM-derived size factors); global DE screen 568 up/125 down PHN and 129/174 HZ (manuscript matches deposited CSV; my fold-change-only screen gives the same ballpark, definition-dependent); TAC1 +0.22 / P 0.38 (+0.2176 / 0.3771); ATF3 and five pan-neuronal markers (identical). Additional sensitivities I computed for this review: M3 minus PTK2 (-0.0475, P = 0.435); M4 minus PTK2 (-0.0238, P = 0.524); E1-core 13 canonical channels (-0.2442, P = 0.0023); E1 minus KCNQ2/3 (-0.2230, P = 0.0023); E1-N1 without shared genes (-0.0721, P = 0.1737). **No numerical discrepancy with the manuscript was found anywhere.**

**Reference verification (PubMed/Crossref/publisher pages):** [1] Wang 2024 (PMID 39211798 — correct; blood RNA-seq, type-I IFN/immune programs — supports its cited claim); [2] Liang 2023 (DOI 10.3389/fimmu.2023.1183378 — correct); [3] Niemeyer 2026 (PMID 42734212, DOI 10.1002/ana.78352 — correct; author order Niemeyer/Frietze/Lewis correct; abstract confirms channel-down/substance-P-up/ECM-remodeling); [4] Yeon 2025 (PMID 41091131 — correct); [5] Raymon 1999 (DOI/PMID correct); [6] Haberberger 2020 (correct); [7] Chen 2022 (PMID 36226089 — correct; no time-by-group interaction confirmed); [8] Lee 2020 (PMID 32195953 — correct; uncontrolled n = 13 pilot); [9] Chen 2020 (PMID 32641142 — correct but is a protocol; see A4); [10] Ge 2023 (PMID 37303680 — correct; tenocytes, integrin-FAK-p38MAPK); [11] Pan 2022 (PMID 35844093 — correct; Piezo1/Ca/FAK, no TRP); [12] GSE314229 — the underlying publication is Xie et al., Adv Sci 2026;13(16):e17257, DOI 10.1002/advs.202517257, PMID 41504389 (claim verified: MSC-derived sEV via ATP/P2X7R/p38MAPK); [13] Cox 2006 (correct); [14] Woo 2014 (correct); [15] Murthy — DOI/PMID correct but **year/volume/issue wrong** (2019;11(486) → 2018;10(462)); [16] Li & Dewey 2011 (correct); [17] BH 1995 (correct); [18] Sánchez-Carranza 2024 (PMID 38984717 — correct; supports the GOF/voltage-block claims); [19] Chesler 2016 (PMID 27653382 — reference correct but **cited claim unsupported**, see A3); [20] Dworkin 2007 (correct, but indirect for a definition); [21] Nguyen 2021 (PMID 34825887 — reference otherwise correct but **two authors wrong**, see C2).

**Group-assignment check:** series-matrix sample titles confirm "control sera EV" × 7, "PHN sera EV" × 5, "acute zoster sera EV" × 7, matching the C/P/S column prefixes and the 7/5/7 sizes; DirectInf titles confirm mock × 6 / VZV × 6, harvest 4 days post-infection.

---

## Must-fix list (ordered by severity)

1. **Remove the revision-history artifact** — "Three further constraints follow from the Round-4 internal benchmarks" (manuscript:134) cannot appear in a first submission. Replace with "Three further constraints deserve emphasis." (Item E1.)
2. **Fix the two wrong reference records** — [15] Murthy: 2018;10(462), not 2019;11(486); [21] Nguyen: authors are Ryba NJP and Davidson S, not "Rycroft KM, Ma J". (Items C1, C2.)
3. **Correct the unsupported Chesler claim** — "tactile-allodynia defects" is not in Chesler 2016; replace with "selective loss of discriminative touch and proprioception". (Item A3.)
4. **Recalibrate the title** — "Route-dependent transcriptional effects…" asserts more than the paper's own conclusion; retitle with the HD10.6 qualification and/or "divergent". (Items E2, D2.)
5. **Add the M1 resolution-limit caveat to the abstract** and the gene-level TRPV1 decrease under direct VZV infection, so the abstract's claim set matches §3.4/§3.6. (Item B1.)
6. **Stop citing the trial protocol [9] as efficacy evidence**; re-cast the ESWT sentence as within-group benefit in small studies plus one RCT with a null interaction, and note [9] is [7]'s protocol. (Item A4.)
7. **Replace the GEO-accession citation [12]** with Xie et al., Adv Sci 2026;13(16):e17257 (DOI 10.1002/advs.202517257). (Item C3.)
8. **Disclose the PTK2 duplication between M3 and M4** with the (unchanged) sensitivity values, or remove PTK2 from one module by documented amendment. (Item D1.)
9. **Fix the "Piezo/TRP signaling" attribution** to "Piezo1–FAK signaling" per refs [10, 11]. (Item B2.)
10. **Add the missing must-cite literature**: Coste 2010 and Ranade 2014 (Piezo2 foundational); Gershon 2015 (VZV pathogenesis); Johnson & Rice 2014 (PHN definition); Simeoli 2017 and Picco 2024/2025 (the uncited EV–pain-signaling claim in §4.2). (Items A1, A5, C4, C5.)
11. **Specify the actual median-of-ratios transform** in §2.3 (CPM-derived size factors, log2(1+CPM/SF)) and align the artifact's stored size factors. (Item B5.)
12. **Smaller precision fixes**: soften "cardinal symptom of PHN" (A2); qualify TRPA1's mechanogating (B3); justify or tighten E1's non-canonical members, optionally reporting the E1-core sensitivity (B4); "second-strongest" → "second-smallest P value" (E3a); label the MDE as post hoc (E3b); update the reproducibility tag to v1.1.5 (E4); soften "none has systematically interrogated" (C6).

**One-sentence justification for the verdict:** The analysis itself is exemplary and fully reproducible — every number I checked matches to three or four decimals — but the manuscript as submitted carries two incorrect reference records, one unsupported citation claim, a protocol cited as efficacy evidence, an undisclosed revision-history sentence, and a title/abstract claim set stronger than its own conclusions, all of which require substantive correction before it can be considered for publication.
