# Review A1 — domain/science layer (mechanotransduction, neuropathic pain, HZ/PHN clinical)

**Manuscript:** `manuscript/manuscript_v1.0.0.md` — *Route-dependent transcriptional effects of varicella-zoster virus and patient serum exosomes on ion-channel programmes in human sensory neurons: a pre-registered reanalysis of GSE342782*
**Venue:** Journal of Pain Research (research article / bioinformatics reanalysis)
**Reviewer:** A1 (pain mechanotransduction / neuropathic pain / HZ-PHN clinical)

All numbers cited below were recomputed by me independently from the raw GEO processed count matrices (CPM → log2(1+CPM), module score = per-sample mean across present panel genes, Welch *t*, Mann–Whitney *U*, label-permutation null B = 5,000, seed 20261019, BH across the eight modules), following the pipeline in `analysis/scripts/layer1_mechano.py`. Line numbers refer to `manuscript/manuscript_v1.0.0.md`.

---

## 1. Endpoint meaning / central claim

### Issue A1 — The central "channel-imbalance = substrate for mechanical allodynia" claim does not follow from the data as worded

【Problem】The headline inference — that acute-HZ-serum exosomes suppressing electrochemical nociceptor transcripts while not suppressing PIEZO2 transcripts is "a plausible molecular substrate for mechanical allodynia" — rests on three unsupported steps: (i) transcript abundance is treated as channel function; (ii) *suppression* of the electrogenic nociceptor apparatus (Nav1.7/Nav1.8, TRPV1, ASICs) is treated as producing a pain-generating state, when the opposite direction (reduced excitability) is the straightforward prediction; (iii) the signature is observed at the wrong disease stage — acute-HZ exosomes, whereas PHN is the chronic state, and the PHN-exosome contrast does **not** show the selective pattern.

【Evidence】
- Wording: Abstract (manuscript:21): "An exosome-driven imbalance — electrochemical nociception dampened while mechanical gating is spared — provides a transcriptomic substrate compatible with mechanical allodynia"; §4.1 (manuscript:93): "a neuron with dampened electrochemical nociception but intact mechanical gating is a neuron whose output is disproportionately driven by mechanical input — a plausible molecular substrate for the tactile allodynia that defines PHN"; Conclusions (manuscript:109): "offers a transcriptomic substrate for mechanical allodynia".
- "Spared" is a null, not a positive result: PIEZO2 under HZ exosomes = −0.282 log2CPM (Welch P = 0.18), i.e. a non-significant ~16% CPM decrease (recomputed group means: control 187.0 CPM → HZ 157.0 CPM). Under PHN exosomes PIEZO2 **is** significantly suppressed (−0.383; permutation P = 0.004; PHN mean 142.2 CPM). So "mechanical gating is spared" is true only of the acute-HZ contrast, is a non-result, and reverses in the PHN contrast.
- The E1 module contains Kv7.2/Kv7.3 (KCNQ2, KCNQ3) and Kv9.1 (KCNS1) — M-current subunits that *restrain* firing — plus ionotropic glutamate receptors (GRIA1/2, GRIN2B) and P2RX7 (`analysis/config/mtp_panel.json`). Uniform down-regulation of a module mixing excitability-promoting and excitability-limiting channels has no unambiguous functional sign. (Sensitivity check: excluding KCNQ2/KCNQ3/KCNS1, E1 = −0.212, Welch P = 0.0049 — the effect is real, but its *direction of functional meaning* is still ambiguous.)
- Several genes used in the signature are below the study's own detection threshold (CPM > 1, manuscript:53): in SeraExo, SCN10A is detected in 11% of samples (mean 0.55 CPM), TRPM8 in 0% (0.52 CPM), GRIN2B in 0% (0.29 CPM), GRIA1 in 0% (0.08 CPM), KCNQ3 in 32% (0.78 CPM). The Abstract's "concordant down-regulation of TRPV1, SCN9A, SCN10A and ASIC1/2" (manuscript:19) and §3.3 (manuscript:75) include genes that are essentially not expressed in this model.
- The original study interpreted the same channel-down-regulation pattern as maladaptive remodelling in a "failure-to-resolve" model (nociceptive channels down, substance P up, neurite outgrowth impaired, MMP-9 secreted) — not as an allodynia mechanism (Niemeyer et al., Ann Neurol 2026, DOI 10.1002/ana.78352, PMID 42734212; abstract text verified). The present manuscript's allodynia framing is its own extension and is presented without engaging that alternative reading.

【Why it matters】This is the paper's central claim and appears in the Abstract, §4.1 and §5. As written it is a transcript-to-behaviour inference that a pain-journal referee cannot verify and that the field will read as overreach: (a) it converts a null on PIEZO2 into a positive statement about preserved mechanical gating; (b) it draws a hyperalgesic conclusion from a hypociceptive-direction perturbation; (c) it attaches the claim to acute-HZ exosomes while the disease of interest is chronic PHN, where the pattern is non-specific. This is the single biggest threat to acceptance at a SCIE pain journal.

【Specific fix】Replace the claim in the Abstract (manuscript:21), §4.1 (manuscript:93) and §5 (manuscript:109) with a hypothesis-level statement, e.g.:

> "In this model, exosomes from patients with acute herpes zoster selectively reduced transcripts of electrochemical nociceptor channels (E1 module: −0.220 log2CPM, permutation P = 0.011) while transcripts of the mechanogated PIEZO2 axis were not significantly changed (−0.282, P = 0.18). Whether this transcriptional imbalance alters mechanosensitivity in vivo is unknown: transcript abundance is not channel function, the direction of the E1 shift is not unambiguously hypo- or hyper-excitability (the module includes M-current subunits), and functional validation (calcium imaging, patch-clamp, mechanical stimulation) is required before any link to mechanical allodynia can be asserted."

And add to §4.1 one sentence: "We note that the same down-regulation was interpreted by the original authors as part of a failure-to-resolve remodelling phenotype rather than as a pain-generating mechanism; our data cannot distinguish these readings."

---

### Issue A2 — "PHN is clinically defined by mechanical allodynia" is clinically false

【Problem】The manuscript's framing sentence asserts that mechanical allodynia is the *defining* feature of PHN, twice. This is not the accepted clinical definition and misinforms the entire motivation of the paper.

【Evidence】
- §1 (manuscript:31): "Postherpetic neuralgia (PHN) is clinically defined by mechanical allodynia: innocuous cutaneous stimuli — a sleeve brushed across the thorax, the weight of a bedsheet — are transduced as pain."
- §4.1 (manuscript:93): "the tactile allodynia that defines PHN."
- Accepted definition: PHN is conventionally defined as dermatomal pain persisting ≥90 days after onset/healing of the acute zoster rash (Johnson RW, Rice ASC. N Engl J Med 2014;371:1526–1533, PMID 25317872, DOI 10.1056/NEJMcp1403062 — verified; ICD-11 chronic neuropathic pain classification: Scholz et al., Pain 2019;160:53–59, PMID 30586071; grading: Finnerup et al., Pain 2016;157:1599–1606, PMID 27115670). Mechanical allodynia is *frequent* in PHN but neither necessary nor sufficient: quantitative sensory testing in PHN shows heterogeneous profiles with prominent sensory loss, ongoing burning pain, lancinating pain and itch, and dynamic mechanical allodynia is present in a subset of patients only (Pfau et al., Pain 2014;155:1002–1015, PMID 24525274 — DFNS trunk reference data applied to chronic PHN). The source dataset itself defines PHN as "persisting beyond 3 months after herpes zoster" (Niemeyer et al. 2026 abstract, verified).

【Why it matters】A factually incorrect definition of the target disease in the first sentence of the Introduction is an immediate credibility loss for a pain-journal readership, and it propagates into the abstract, the mechanistic claim (A1) and the conclusion. It also licenses the paper's unjustified leap from "allodynia is the defining symptom" to "any channel imbalance is an allodynia substrate".

【Specific fix】Replace §1 first sentence with:

> "Postherpetic neuralgia (PHN) — pain persisting at least 90 days after the acute herpes zoster rash — is the most common neuropathic pain of infectious origin, and a large subset of patients report mechanically evoked pain (dynamic mechanical allodynia to brush or clothing), which quantitative sensory testing localises to a gain of tactile (not noxious) mechanosensory function alongside coexisting sensory loss [Johnson & Rice 2014; Scholz 2019; Finnerup 2016; Pfau 2014]."

and delete "that defines PHN" in §4.1 (manuscript:93).

---

## 2. Must-cite literature (reference list [1]–[14] is too thin; placeholders [2] and [6])

### Issue B1 — Placeholder [6] cannot be filled honestly; the sentence it supports is false

【Problem】Reference [6] is a placeholder ("Clinical guideline literature on mechanical allodynia as the defining symptom of PHN", manuscript:138) supporting a false claim (A2). No guideline defines PHN by mechanical allodynia, so the placeholder has no honest completion.

【Evidence】manuscript:138 ([6] placeholder); the claim it supports at manuscript:31 and manuscript:93 (see A2). The authors' own verification note (manuscript:156) flags [6] as incomplete before final submission.

【Why it matters】Placeholders cited in support of key clinical sentences are a desk-reject-level defect at Dove Press if unresolved, and here the underlying claim is also wrong.

【Specific fix】Replace [6] with: Johnson RW, Rice ASC. Postherpetic neuralgia. N Engl J Med. 2014;371(16):1526–1533 (PMID 25317872); Finnerup NB, et al. Neuropathic pain: an updated grading system for research and clinical practice. Pain. 2016;157(8):1599–1606 (PMID 27115670); Scholz J, et al. The IASP classification of chronic pain for ICD-11: chronic neuropathic pain. Pain. 2019;160(1):53–59 (PMID 30586071); Pfau DB, et al. Pain. 2014;155(5):1002–1015 (PMID 24525274). Then rewrite the sentence per Issue A2.

### Issue B2 — Placeholder [2] is not a citable publication and does not support the sentence it is attached to

【Problem】[2] (manuscript:130) is an internal audit note about FinnGen endpoint drift (144→313→490→554 cases across releases R5–R13), not a publication, yet it is cited in §1 as evidence that "published bioinformatic reanalyses of PHN cohorts have concentrated on interferon, immune and inflammatory programmes [1–3]".

【Evidence】manuscript:31–33 and manuscript:130. Real, verified published MR studies of PHN with FinnGen endpoints exist and would support that sentence, e.g. Wang H, Chen G, Gong Q, Wu J, Chen P. Systemic inflammatory regulators are associated with two common types of neuropathic pain: a bidirectional Mendelian randomization study. Int Immunopharmacol. 2024;143(Pt 2):113466 (PMID 39471697 — verified; reports IFNγ, MCP3, IL-16 associations with PHN), and Liang X, Fan X. Bidirectional two-sample Mendelian randomization analysis reveals a causal effect of interleukin-18 levels on postherpetic neuralgia risk. Front Immunol. 2023;14:1183378 (PMID 37304287 — verified). A proteome-wide MR (NMRAL1) using FinnGen R12 (490 PHN cases) also exists (PMC12117202).

【Why it matters】Citing a non-publication as reference [2] in a submitted manuscript is a formal defect; and if the FinnGen endpoint-drift work is the authors' own analysis, it must not be presented as prior literature.

【Specific fix】Replace [2] with the Wang et al. 2024 (PMID 39471697) and/or Liang & Fan 2023 (PMID 37304287) citations. If the authors performed their own FinnGen MR, present it as an original analysis with a data-availability statement, or delete it from the reference list.

### Issue B3 — Must-cite missing papers (verified identifiers)

【Problem】For a pain-mechanism paper whose entire claim is about PIEZO2, nociceptor channels, exosomes and an iPSC sensory-neuron model, the reference list omits the primary literature on all four topics.

【Evidence】Verified citations that should be added (all PMIDs/DOIs confirmed during this review):

*PHN definitions, guidelines, recent reviews*
1. Johnson RW, Rice ASC. N Engl J Med 2014;371:1526–1533. PMID 25317872. DOI 10.1056/NEJMcp1403062.
2. Scholz J, et al. Pain 2019;160(1):53–59. PMID 30586071. DOI 10.1097/j.pain.0000000000001365.
3. Finnerup NB, et al. Pain 2016;157(8):1599–1606. PMID 27115670. DOI 10.1097/j.pain.0000000000000492.
4. Pfau DB, et al. Pain 2014;155(5):1002–1015. PMID 24525274 (PHN QST reference data).
5. Truini A, et al. Joint EAN–EFIC–NeuPSIG guidelines on neuropathic pain assessment. Eur J Neurol 2023;30:2177–2196. PMID 37253688.
6. Identifying and Evaluating Biological Markers of Postherpetic Neuralgia: A Comprehensive Review. Pain Ther 2024;13(5):1095–1117. PMID 39126594.

*Piezo2 mechanotransduction in somatosensory neurons*
7. Coste B, et al. Piezo1 and Piezo2 are essential components of distinct mechanically activated cation channels. Science 2010;330:55–60. PMID 20813920. DOI 10.1126/science.1193270.
8. Ranade SS, et al. Piezo2 is the major transducer of mechanical forces for touch sensation in mice. Nature 2014;516:121–125. PMID 25471886. DOI 10.1038/nature13980. (Note: the widely misquoted PMID 25140144 belongs to an unrelated psychology paper; use 25471886.)
9. Woo SH, et al. Piezo2 is required for Merkel cell mechanotransduction. Nature 2014;509:622–626. DOI 10.1038/nature13251 (PMID not independently verified here — verify before submission).
10. Szczot M, Nickolls AR, Lam RM, Chesler AT. The Form and Function of PIEZO2. Annu Rev Biochem 2021;90:507–534. PMID 34153212. DOI 10.1146/annurev-biochem-081720-023244. (Also the best available source on protocol-dependent PIEZO2 expression in iPSC-derived sensory neurons — see Issue D1.)

*PIEZO2 / mechanochannels in pain and allodynia — the mechanistically decisive literature for this paper's claim*
11. Murthy SE, et al. The mechanosensitive ion channel Piezo2 mediates sensitivity to mechanical pain in mice. Sci Transl Med 2018;10(462):eaat9897. PMID 30305457.
12. PIEZO2 mediates injury-induced tactile pain in mice and humans. Sci Transl Med 2018;10(462):eaat9892. PMID 30305456. (Loss-of-function PIEZO2 abolishes post-inflammatory tactile allodynia — i.e. preserved PIEZO2 is *permissive* for allodynia, which is the citation the authors' argument actually needs.)
13. Obeidat AM, et al. Piezo2 expressing nociceptors mediate mechanical sensitization in experimental osteoarthritis. Nat Commun 2023;14:2479. PMID 37120427.
14. Fernández-Trillo J, et al. Piezo2 mediates mechanical sensitivity and injury-induced hypersensitivity in MrgprD-expressing nociceptors. Pain 2026 (Apr). PMID 41925518. DOI 10.1097/j.pain.0000000000003954.
15. Habib AM, et al. MDFIC2 is a PIEZO channel modulator that can alleviate mechanical allodynia associated with neuropathic pain. Proc Natl Acad Sci USA 2025;122:e2512426122. PMID 41201821. (Post-translational PIEZO gating control in neuropathic pain — directly supports the authors' §4.3(iii) argument, currently uncited.)
16. Shin SM, Itson-Zoske B, Fan F, Gani U, Rahman M, Hogan QH, Yu H. Peripheral sensory neurons and non-neuronal cells express functional Piezo1 channels. Mol Pain 2023;19:17448069231174315. PMID 37247618. (Piezo1 in satellite glia; Yoda1-induced mechanical hypersensitivity reversed by GsMTx4 — supports §4.3(i)'s non-neuronal-compartment argument with a real citation.)

*Nav1.7/Nav1.8 nociception*
17. Bennett DL, Woods CG. Painful and painless channelopathies. Lancet Neurol 2014;13(6):587–599. PMID 24813307. DOI 10.1016/S1474-4422(14)70024-9.
18. Bennett DL, Clark AJ, Huang J, Waxman SG, Dib-Hajj SD. The role of voltage-gated sodium channels in pain signaling. Physiol Rev 2019;99:1079–1151. DOI 10.1152/physrev.00052.2017 (PMID not independently verified — verify before submission).

*Exosome/EV pain signalling*
19. Cata JP, Uhelski ML, Gorur A, Dougherty PM. Nociception and Pain: New Roles for Exosomes. Neuroscientist 2022;28(4):349–363. PMID 34166130. DOI 10.1177/10738584211027105.
20. Sun Q, et al. Pain 2025 (exosomal miR-1306-3p from primary sensory neurons → chronic visceral pain via spinal P2X3). PMID 39907482. DOI 10.1097/j.pain.0000000000003537.
21. Xing Y, et al. Cell Death Dis 2024 (DRG-derived exosomes → microglial activation, miR-16-5p). PMID 38750549. DOI 10.1186/s40659-024-00513-1.

*iPSC sensory-neuron model limitations*
22. Szczot et al. 2021 (item 10) — documents that published iPSC sensory-neuron protocols yield heterogeneous populations "with uncertain identities", and that NGN2-pulsed differentiation biases toward large-diameter PIEZO2-positive touch-like neurons.
23. Characterization of human iPSC-derived sensory neurons and their functional assessment using multi-electrode array. Sci Rep 2024. DOI 10.1038/s41598-024-55602-8 (PMID not independently verified — verify before submission). Reports that many sensory-channel transcripts in hiPSC-derived sensory neurons remain below adult human DRG levels, attributed to immaturity.

【Why it matters】The paper's novelty claim ("none has systematically interrogated the mechanotransduction machinery", manuscript:31) and its mechanistic argument both stand or fall on this literature. As submitted, a reader cannot tell whether the authors know that PIEZO2 is (a) largely LTMR-restricted in adult DRG, (b) necessary for injury-induced tactile allodynia, and (c) subject to post-translational gating control in neuropathic pain. Citing items 11–16 changes the paper from "we found a channel imbalance" to "we found a channel imbalance, and here is why it could matter — or not".

【Specific fix】Add items 1–3 and 7–8 (minimum), plus 11–12 and 19–20 (mechanistic core), plus 22 (model limits), with in-text discussion at §3.1, §4.1 and §4.3 as specified in Issues A1, D1, E1.

---

## 3. Clinical / technical falsehoods in Introduction and Discussion

### Issue C1 — ESWT evidence is overstated, and is cited alongside a placeholder as if it were clinical evidence

【Problem】"ESWT — the deliberate application of controlled mechanical stress — has shown clinical benefit in herpetic neuralgia [5,6]" (manuscript:33). The cited clinical evidence is one 13-patient uncontrolled pilot and one 19-patient single-blind RCT; [6] is a placeholder about the PHN definition, not a clinical study; and [14] is a trial protocol with no results.

【Evidence】
- [5] Yeon JE, et al. Pain Pract 2025;25(8):e70085 (PMID 41091131, verified): single-blind randomised study, n = 10 ESWT vs n = 9 sham; the authors themselves call it preliminary.
- [13] Lee SH, et al. Medicine 2020;99(12):e19516 (PMID 32195953, verified): 13 patients, no control arm.
- [14] Chen L, et al. Trials 2020;21:573 (PMID 32641142, as listed): protocol only, no results.
- [6] is a placeholder (manuscript:138). §4.3 (manuscript:101) again cites [5–8,13,14] as the clinical-mechanistic bridge.

【Why it matters】"Has shown clinical benefit" is an evidence-grade claim a JPR referee will check; the actual base is small, single-centre, preliminary. Overstating it undermines the mechanotherapy framing in §4.3 and the Conclusion's "mechanically targeted therapies" (manuscript:21).

【Specific fix】Replace with: "ESWT has shown promise in herpetic neuralgia in a small uncontrolled pilot (n = 13) [Lee 2020] and a preliminary single-blind randomised trial (n = 19) [Yeon 2025], with a larger randomised trial registered [Chen 2020]; the evidence base remains preliminary and no adequately powered trial has been completed." Remove [6] from this citation.

### Issue C2 — The absolute novelty claims are unverifiable as written, and the broader framing is outdated

【Problem】Two absolute claims: "the mechanotransduction dimension has never been examined systematically in the genomic literature of PHN" (manuscript:15) and "The same mechanical axis therefore appears at both the disease end (allodynia) and the treatment end (mechanotherapy) of PHN, yet no study has connected them at the transcriptomic level" (manuscript:33).

【Evidence】The transcriptomic-level claim may survive, but the framing that the mechanical axis is unconnected to neuropathic pain does not: mechanochannel contributions to neuropathic mechanical hypersensitivity are established at the molecular level (PIEZO2 necessary for injury-induced tactile allodynia, PMIDs 30305456/30305457; Piezo2+ nociceptors in CCI and osteoarthritis models, PMIDs 41925518/37120427; MDFIC2–PIEZO gating control in spared-nerve-injury allodynia, PMID 41201821; satellite-glia Piezo1 in mechanical hypersensitivity, PMID 37247618). Also note that [1] (Wang et al. 2024, PMID 39211798, verified) is a published PHN blood-transcriptome study — the sentence at manuscript:31 citing it as evidence of immune/inflammatory focus is fair, but "never examined" is still absolute.

【Why it matters】Absolute novelty claims are the standard trigger for adversarial referee checking; a single counter-example (e.g., PMID 30305456) makes the Introduction read as uninformed. Additionally, the present study does not itself "connect" the two ends — it contains no ESWT data — so the sentence sets up a bridge the paper does not build.

【Specific fix】Hedge both claims ("To our knowledge, no published transcriptomic study of PHN cohorts has systematically interrogated the mechanotransduction machinery…") and add one sentence acknowledging the animal-level mechanistic literature (PMIDs 30305456, 37247618) that connects mechanochannels to neuropathic mechanical pain, so that the paper's contribution is correctly positioned as the first *human-neuron transcriptomic* test rather than the first connection of the axis to pain.

---

## 4. Model appropriateness (HD10 iPSC-derived sensory neurons)

### Issue D1 — The PIEZO2-high / TRPV4-absent baseline is atypical of adult nociceptors in ways the paper does not disclose, and the "PIEZO2 failure risk" claim needs a source

【Problem】The authors report the PIEZO2-high / TRPV4-absent baseline as a boundary condition (§3.1 manuscript:67; §4.4(i) manuscript:105) and claim it "refutes" a hypothesised risk that iPSC-derived neurons fail to express PIEZO2. Both the disclosure and the claim are incomplete: the line's phenotype deviates from adult DRG nociceptors in additional, more consequential ways that bear directly on the allodynia inference.

【Evidence】Recomputed baselines (mean CPM, SeraExo; DirectInf in parentheses): PIEZO2 245 (164) — high; TRPV1 122 (96) — high; SCN9A 318 (262) — high; P2RX3 807 (471) — very high; TAC1 66; NTRK1 152; PRDM12 20 — consistent with a nociceptor-lineage identity. But: SCN10A (Nav1.8) 0.55 CPM, detected in 11% of samples; TRPM8 0.52 CPM, 0% detected; TRPA1 0.02 CPM, 0%; TRPV4 0.25 CPM, 0%; STOML3 0.008 CPM, 0%. In adult DRG, Nav1.8, TRPM8 and TRPA1 are canonical nociceptor markers, while PIEZO2 is concentrated in low-threshold mechanoreceptors and Merkel-cell complexes and is largely excluded from TRPV1-positive peptidergic C-fibers (Ranade 2014, PMID 25471886; Szczot 2021, PMID 34153212). The very high co-expression of PIEZO2 with TRPV1/TAC1/NTRK1 in one line is therefore not an adult nociceptor configuration, and is compatible with an immature or LTMR-biased phenotype — iPSC sensory-neuron protocols are documented to yield heterogeneous populations of uncertain subtype identity, with NGN2-pulsed protocols biasing toward PIEZO2-positive touch-like neurons (Szczot 2021, PMID 34153212). The claim that "the hypothesised technical risk that induced-pluripotent-stem-cell-derived neurons fail to express PIEZO2 is refuted in this model" (manuscript:67) cites no source for the hypothesised risk.

【Why it matters】The paper's bridge from "this line" to "PHN nociceptors" depends on the line being a reasonable nociceptor proxy. The undisclosed deviations (Nav1.8/TRPM8/TRPA1 essentially absent; PIEZO2+TRPV1 co-dominance; P2RX3 dominating the M1 module) mean the "spared PIEZO2" observation may describe an LTMR-like or immature phenotype rather than nociceptor biology — which weakens the allodynia inference further (compounding Issue A1).

【Specific fix】(a) In §3.1 and §4.4(i), disclose the full phenotype: "SCN10A (0.55 CPM, detected in 11% of samples), TRPM8, TRPA1, TRPV4 and STOML3 were at or below detection; PIEZO2 was co-expressed with high TRPV1/TAC1/NTRK1, a combination not typical of adult DRG nociceptors, in which PIEZO2 is largely restricted to low-threshold mechanoreceptors [Ranade 2014; Szczot 2021]; the phenotype is consistent with an immature or mechanoreceptor-biased population." (b) Cite the source of the "PIEZO2-failure" technical risk or delete the claim. (c) Add a marker-panel table (PIEZO1/2, TRPV1/4, TRPA1, TRPM8, SCN9A/10A/11A, P2RX3, NTRK1/2/3, RET, RUNX1, PRDM12, TH, TAC1, POU4F1, ISL1) with per-group CPM and detection fractions to the supplement.

### Issue D2 — "M1 is effectively a PIEZO2-dominated module" is numerically wrong

【Problem】The manuscript states M1 is "effectively a PIEZO2-dominated module" (manuscript:67), but P2RX3 contributes ~2.9× more to the M1 score than PIEZO2, and PIEZO1 — not PIEZO2 — shows the largest within-module shift under HZ exosomes.

【Evidence】Recomputed SeraExo means: P2RX3 470.6 CPM (log2CPM 8.85) vs PIEZO2 164.1 CPM (7.32); TMEM150C 16.1 CPM (4.09); PIEZO1 2.2 CPM (1.63); TRPV4 0.19; STOML3 0.00; KCNK2 0.66; KCNK4 3.21; TRPA1 0.02. Within-M1 HZ-vs-control shifts: PIEZO1 −0.374 (P = 0.10), P2RX3 −0.304, PIEZO2 −0.282 (P = 0.18). The M1 score is therefore P2RX3-dominated, and the "mechanogated channel" framing of P2RX3 (an ATP-gated channel, non-peptidergic nociceptor marker) within M1 is itself questionable.

【Why it matters】The "double dissociation" narrative treats M1 as the PIEZO2 module; if PIEZO2 contributes <30% of the M1 signal, the dissociation is as much about P2RX3/PIEZO1 as about PIEZO2, and the mechanistic story told in §4.1 ("the mechanogated PIEZO2 axis was spared") overstates PIEZO2's role in the module-level result.

【Specific fix】Replace with: "M1 is dominated by P2RX3 (mean 471 CPM), with PIEZO2 the second-largest contributor (164 CPM); within-module shifts under HZ exosomes were largest for PIEZO1 (−0.374, P = 0.10) and P2RX3 (−0.304), with PIEZO2 at −0.282 (P = 0.18)." Consider a PIEZO2-only gene-level contrast as the primary mechanogated test.

### Issue D3 — The "inert stiffness programme" conclusion is partly a non-expression null (YAP1/WWTR1 at/below detection)

【Problem】§3.2 (manuscript:71) and §4.3 (manuscript:101) describe the ECM–integrin–Hippo module as "transcriptionally inert" / "what did not move", and use this to redirect the field. But the Hippo output arm of the module is essentially not expressed in this model, so the null is uninformative about YAP/TAZ-dependent mechanotranscription — the very thing the "stiffness programme" is supposed to measure.

【Evidence】Recomputed SeraExo means: YAP1 1.04 CPM (detected in 32% of samples), WWTR1 (TAZ) 0.69 CPM (21%), ANKRD1 0.007 CPM (0%), CYR61 and CTGF absent from the matrix — while upstream Hippo kinases are expressed (LATS1 47.0, MOB1A 44.5, STK4 44.3, NF2 88.2, AMOTL1 55.0 CPM) and integrin/focal-adhesion components are robustly expressed (ITGB1 360, ILK 108, PTK2 108, LIMS1 74, VCL 102, ZYX 116 CPM). The gene-level "upward" moves the manuscript cites for YAP1 (+0.425, P = 0.18; manuscript:71) are therefore computed on a gene below the study's own CPM > 1 detection threshold. The boundary conditions disclosed at §3.1 (manuscript:67) and §4.4(v) (manuscript:105) mention TRPV4/STOML3/MMP9 and the CYR61/CTGF absence but do not mention YAP1/WWTR1.

【Why it matters】"The ECM–integrin–Hippo programme — the transcriptional core of cellular mechanotransduction — was inert" is the paper's second headline claim (and the basis of the "redirection" in §4.3 and the Conclusion). If the Hippo effectors are not expressed, the correct statement is "this model does not express the YAP/TAZ transcriptional output of the stiffness programme", which is a statement about the model, not about PHN biology — and it removes the paper's licence to "redirect the search" on evidential grounds.

【Specific fix】Add to §3.1/§4.4(v): "YAP1 (1.0 CPM, 32% of samples) and WWTR1 (0.7 CPM, 21%) were at or below detection, and the canonical YAP/TAZ targets CYR61/CTGF were absent; the M3 null therefore cannot be read as evidence about YAP/TAZ-dependent mechanotranscription, which is in any case regulated predominantly by nuclear translocation rather than mRNA abundance." Temper §4.3's "most consequential finding" framing accordingly.

### Issue D4 — Section 3.1/4.4 boundary statements are otherwise honest but incomplete

【Problem】The boundary-condition statements (manuscript:67, 105) correctly flag the iPSC model, the 36-h window, bulk RNA-seq, donor confounding, missing genes and the borderline M1 effect — but omit the three boundary conditions that matter most for the central claim (D1 phenotype deviations; D3 Hippo non-expression; and the fact that "spared PIEZO2" is a null with a non-zero negative point estimate).

【Evidence】manuscript:67 and manuscript:105 vs. the recomputed values in Issues A1, D1, D3.

【Why it matters】A referee reads §4.4 as the authors' own list of what the data cannot say; if the list is incomplete in exactly the places where the Abstract overreaches, the limitations section reads as curating the boundary rather than disclosing it.

【Specific fix】Extend §4.4(i) and (v) with the D1 and D3 content; add "(viii) 'PIEZO2 spared' denotes a non-significant difference (P = 0.18) with a point estimate of −0.28 log2CPM; under PHN exosomes PIEZO2 was significantly reduced (−0.383, P = 0.004)."

---

## 5. ESWT mechanism (Introduction and Discussion 4.3)

### Issue E1 — References [7] and [8] do not contain the mechanism the manuscript attributes to them

【Problem】The Introduction states that ESWT's "molecular mechanism is increasingly mapped onto integrin–FAK–p38MAPK signalling and Piezo/TRP-dependent YAP/TAZ nuclear translocation [7,8]" (manuscript:33), and §4.3 repeats "the molecular machinery engaged by ESWT (integrin–FAK–p38MAPK; Piezo/TRP–YAP/TAZ)" (manuscript:101). Neither cited reference demonstrates YAP/TAZ translocation, and neither is a pain or neuronal study.

【Evidence】
- [7] Ge R, et al. Am J Transl Res 2023;15(5):3229–3239 (PMID 37303680, verified): rESWT in TNF-α-stimulated **human tenocytes**; integrin–FAK–p38MAPK. A tendon-cell anti-inflammation study.
- [8] Pan Y, et al. EMBO J 2022;41(17):e111799 (PMID 35844093, DOI 10.15252/embj.2022111799, verified): **laser-induced shockwaves + FRET biosensors** showing bimodal Piezo1→Ca2+/FAK signalling (transient Ca2+ ↑FAK; sustained Ca2+ ↓FAK) via SHP2. It contains no YAP/TAZ data and is a biophysics paper, not an ESWT-clinical-mechanism paper.
- [9] GSE314229 is correctly described (Xie X, et al. Adv Sci 2026;13(16):e17257, PMID 41504389, verified: rESWT triggers sEV release via ATP/P2X7R/p38MAPK in a rat tibial-osteotomy wound-healing model) — but it is a bone/wound-healing study, which the manuscript does not qualify.

【Why it matters】The ESWT paragraph is the paper's only clinical bridge, and its two mechanistic citations are a tenocyte paper and a laser-shockwave biophysics paper presented as if they mapped ESWT's analgesic mechanism in PHN. A mechanobiology-literate referee will flag this immediately, and it contaminates the §4.3 "point of contact between the allodynia substrate identified here and the clinical benefit of controlled mechanical stimulation".

【Specific fix】Rewrite with correctly attributed, better-verified references: Dupont S, et al. Role of YAP/TAZ in mechanotransduction. Nature 2011;474:179–183 (PMID 21654799, verified) for YAP/TAZ as mechanotransducers; Li HX, Zhang ZC, Peng J. Low-intensity extracorporeal shock wave therapy promotes recovery of sciatic nerve injury and the role of mechanical sensitive YAP/TAZ signaling pathway for nerve regeneration. Chin Med J 2021 (PMID 34845995, verified — LiESWT upregulates YAP/TAZ in Schwann cells and perineurial fibroblasts after nerve injury) and Zhao Z, et al. Stem Cell Res Ther 2021;12:19 (PMID 33413606, verified — rESW promotes YAP nuclear translocation) for shockwave→YAP/TAZ. Proposed replacement sentence:

> "Mechanistically, shockwave-induced mechanotransduction has been linked to integrin–FAK–p38MAPK signalling in mesenchymal cell types [Ge 2023], to bimodal Piezo1–Ca2+–FAK responses under laser-induced shockwaves [Pan 2022], and to YAP/TAZ activation in Schwann cells and perineurial fibroblasts after nerve injury [Li 2021] and in bone stem/progenitor cells [Zhao 2021]; YAP/TAZ are bona fide nuclear relays of matrix mechanics [Dupont 2011]. Whether any of this operates in nociceptors or satellite glia in PHN is unknown."

---

## 6. Panel construction and internal consistency (verifiable defects)

### Issue F1 — Methods claim "all other modules were fully represented" is false

【Problem】§2.3 (manuscript:53) states that only M3 lost genes and "all other modules were fully represented". N2 lost three genes and N3 lost one.

【Evidence】Verified directly from the processed count matrices: OR6A1, OR10A1 and OR13C1 are absent from both matrices (N2 used 13 of 16 genes); RPS4 is absent (N3 used 17 of 18). The same facts are recorded in `analysis/results/layer1/layer1_results.json` (`panel_missing`), so the error is in the manuscript text, not the analysis. (M3's 56/58 with CYR61/CTGF absent is correct.)

【Why it matters】A false completeness statement in Methods about the frozen panel is exactly the kind of error that erodes trust in the pre-registration discipline the paper leans on.

【Specific fix】Replace with: "M3 used 56 of 58 genes (CYR61 and CTGF absent from the count matrix), N2 used 13 of 16 (OR6A1, OR10A1, OR13C1 absent) and N3 used 17 of 18 (RPS4 absent); all other modules were fully represented."

### Issue F2 — Section 3.2's "M4 unchanged in every contrast (all P ≥ 0.11)" contradicts Section 3.4 and the data

【Problem】§3.2 (manuscript:71) claims "for M4 mechano-effectors in every contrast (all P ≥ 0.11)", but M4 is significantly suppressed under direct VZV infection — as §3.4 itself reports.

【Evidence】Recomputed VZV-vs-mock M4: −0.054 log2CPM, permutation P = 0.0242 (Welch P = 0.028). §3.4 (manuscript:79) correctly states "M4 mechano-effectors were suppressed (-0.054; P = 0.024)". §3.2's parenthetical is therefore false and internally contradictory.

【Why it matters】Internal contradictions on numbers that any referee can recompute in minutes are disproportionately damaging in a paper whose selling point is numerical discipline.

【Specific fix】Delete the clause "and for M4 mechano-effectors in every contrast (all P ≥ 0.11)" from §3.2, or restate as "M4 was unchanged under both exosome contrasts (P ≥ 0.11) but suppressed under direct VZV infection (−0.054, P = 0.024; §3.4)".

### Issue F3 — The "double dissociation" is supported by an interaction test the authors did not run, and that test is batch-confounded

【Problem】The Abstract reports "A double dissociation emerged across perturbation routes" (manuscript:19) and the Conclusions state "direct viral infection showed the complementary pattern" (manuscript:109), while §3.4 (manuscript:79) itself concedes the claim "should be read as hypothesis-generating" because it rests on a borderline effect (M1/VZV, P = 0.051) plus nulls. As presented, the dissociation is asserted from simple effects only.

【Evidence】I computed the route × module interaction (2 × 2: M1 vs E1 under VZV-infection vs HZ-exosome): interaction = −0.193 log2CPM, label-permutation P < 0.0002 (0/5,000). So the dissociation is statistically real — but **route and experiment are perfectly collinear** (the VZV route exists only in the DirectInf batch and the exosome route only in the SeraExo batch), so any batch × module effect is indistinguishable from a route × module effect. With n = 6 vs 6 and 7 vs 7 in two separate experiments, this cannot be resolved within the dataset. Additionally, M4 also shifts under VZV (P = 0.024), so the pattern is not a clean two-module dissociation.

【Why it matters】The dissociation is arguably the paper's most interesting result and deserves a proper test; conversely, presenting it as "emerged" without the interaction analysis — and without stating that route ≡ batch — overstates what two independent experiments can support.

【Specific fix】Add the interaction test to the results (report the interaction effect and permutation P, as above), add the explicit caveat that route and experimental batch are collinear and that confirmation requires both routes within one experiment, and align the Abstract/Conclusions with §3.4's hypothesis-generating framing.

### Issue F4 — Modules are not gene-disjoint; the "neutral control" N1 shares genes with E1

【Problem】The panel is not a set of independent modules: PTK2 appears in both M3 and M4, and KCNQ2 and KCNQ3 appear in both E1 and N1 (`analysis/config/mtp_panel.json`). N1 is therefore not a clean neutral control for the E1 hypothesis, and the BH correction across "eight pre-specified modules" (manuscript:17) treats non-independent tests as a family.

【Evidence】Gene-list overlap verified from the frozen panel: M3 ∩ M4 = {PTK2}; E1 ∩ N1 = {KCNQ2, KCNQ3}. This matters concretely for §3.5/§3.6, where the PHN contrast's "non-specificity" argument rests on N1 shifting (−0.198, P = 0.035) — a shift that is partly carried by the two genes N1 shares with the experimental module E1. (Under HZ exosomes, N1 = −0.156, P = 0.147, non-significant, so the calibration conclusion is unaffected for the primary contrast.)

【Why it matters】The neutral-control calibration is one of the paper's genuine methodological strengths; disclosing the overlap (or removing it) protects that strength from a trivial referee objection.

【Specific fix】State the overlap in §2.2 and add a sensitivity analysis: N1 restricted to the 15 non-E1 genes, and M4 restricted to the 24 non-M3 genes, recomputed and reported in the supplement.

---

## 7. Stands up (things I suspected and verified as correct)

1. **Every quoted module-level statistic reproduces exactly** from the raw GEO counts under an independent reimplementation of the pipeline (same seed): M3 HZ-exo −0.0489 (permutation P = 0.416), E1 HZ-exo −0.2196 (P = 0.0112), M1 HZ-exo −0.078 (P = 0.109), M2 −0.148 (P = 0.068), M1 VZV −0.0504 (P = 0.0514), M4 VZV −0.0544 (P = 0.0242), E1 VZV +0.0005 (P = 0.9958), M1 PHN −0.119 (P = 0.0078), E1 PHN −0.197 (P = 0.0040), N1 PHN −0.198 (P = 0.0352), N3 HZ +0.391 (P = 0.0006), N3 PHN +0.577 (P = 0.0002). BH q-values also reproduce.
2. **The W0 baseline table reproduces exactly**: PIEZO2 245.2 CPM (DirectInf), 164.1 (SeraExo), 100% detected in both; TRPV4 0.25; STOML3 0.008; LOX 0.41; MMP9 0.11; ITGB1 323.6; SCN9A log2CPM 8.31; TRPV1 6.94.
3. **Gene-level Welch P values reproduce**: TRPV1 0.0009, SCN10A 0.008, SCN9A 0.018, ASIC1 0.019, ASIC2 0.042, PIEZO2 0.18; M3 genes COL4A1 0.005, COL4A2 0.007, ADAMTS1 0.013, TEAD1 0.047, LOX 0.024, YAP1 0.18. (The four "downward" M3 genes the manuscript cites are all genuinely expressed: COL4A1 9.0, COL4A2 95.6, ADAMTS1 6.5, TEAD1 44.3 CPM — only the LOX/YAP1 pair is sub-detection; see Issue D3.)
4. **Group assignment by column prefix is correct**: verified against the GEO series metadata — C = control sera EV (n = 7), P = PHN sera EV (n = 5), S = acute zoster sera EV (n = 7); mock n = 6 / VZV n = 6; MOI 0.003, harvest 4 dpi; 36-h exosome exposure; 12-day differentiation. No sample misassignment.
5. **The donor-confounding statement is corroborated by the original publication**: the PHN group was older than control and HZ groups and contained only one male subject (Niemeyer et al. 2026, limitations — verified). The pre-designation of the PHN contrast as exploratory is therefore well-founded.
6. **Reference [4] is real and correctly described**: Niemeyer CS, … Bubak AN. Circulating Exosomes Drive Persistent Neuronal Dysfunction in Post-Herpetic Neuralgia Patients. Ann Neurol 2026 (PMID 42734212, DOI 10.1002/ana.78352). The manuscript's summary of its findings (nociceptive channel down-regulation, substance-P up-regulation, ECM remodelling, neurite-outgrowth impairment, MMP-9 secretion without cytotoxicity) matches the published abstract.
7. **Global-shift and DE-count diagnostics reproduce**: per-sample mean log2CPM across the 19 exosome samples spans 1.553–1.605 (manuscript:87 says 1.55–1.61); |log2FC| > 0.5 counts reproduce at 129 up/174 down (HZ) and 568/125 (PHN), and 33/20 (VZV).
8. **The primary endpoint is a correctly-powered null and is reported as such** — not spun — and the N2 near-floor significance (manuscript:87) and the CCI null (manuscript:87) are disclosed and correctly de-emphasised rather than used as evidence. This is rarer and better practice than usual.
9. **The E1 result is robust to the Kv7 composition concern**: excluding KCNQ2/KCNQ3/KCNS1, E1 = −0.212, Welch P = 0.0049.
10. **Reference [9] is real and correctly characterised** (GSE314229; Xie et al., Adv Sci 2026;13(16):e17257, PMID 41504389: rESWT-triggered sEV release via ATP/P2X7R/p38MAPK). Its non-pain context is the issue (Issue E1), not its existence.

---

## 8. Questions for the authors

1. Was the "channel-imbalance" hypothesis (and the M1/E1 module definitions) frozen and timestamped before any data were examined? The GitHub tag v1.0.0 is contemporaneous with submission; a time-stamped public deposit (e.g., OSF/Zenodo with creation date) would settle pre-registration conclusively.
2. What is the source of the "hypothesised technical risk that iPSC-derived neurons fail to express PIEZO2" (manuscript:67)? Please cite or delete.
3. Can you provide donor-level metadata (age, sex) for the exosome samples and a sensitivity analysis adjusted or stratified for them? The PHN contrast is confounded by age/sex on the original authors' own account; a regression of module scores on group + age (n = 5 PHN limits power, but should be attempted and reported).
4. Was any functional assay performed or is one planned (Ca2+ imaging, MEA, patch-clamp, mechanical stimulation) to test whether the E1 shift alters mechanosensitivity? Without it, the allodynia link remains untested.
5. TAC1 (substance P) trended upward under HZ exosomes in my recomputation (58.5 → 70.7 CPM, +0.22 log2CPM, P = 0.38, non-significant), consistent in direction with the original study's reported substance-P upregulation. How does the "dampened electrochemical nociception" reading accommodate a simultaneously rising neuropeptide arm?
6. Was a route × module interaction test considered? I compute it as significant (−0.19, permutation P < 0.0002) but batch-confounded; do you agree it cannot be de-confounded within GSE342782?
7. What is the cellular identity of the PIEZO2-expressing cells in HD10 cultures (single-cell data, or marker co-staining)? Given the PIEZO2-high/TRPV1-high co-expression, subtype composition is central to interpretation.
8. Should the PHN-exosome contrast be reported at all in the Abstract (manuscript:19–21), given that the authors themselves designate it exploratory and confounded, and given that it does not show the claimed selective pattern?

---

## 9. What I actually checked

**Read in full:** `manuscript/manuscript_v1.0.0.md`; `analysis/config/mtp_panel.json`; `analysis/results/layer1/layer1_results.json`; `analysis/results/layer1/layer1_diag.json`; `analysis/results/layer1/layer1_module_scores.csv`; `analysis/results/layer1/layer1_global_de.csv`; head of `analysis/results/layer1/layer1_gene_level.csv`; `analysis/scripts/layer1_mechano.py`; GEO series matrix `GSE342782_series_matrix.txt.gz` (all sample-level metadata).

**Recomputed from the raw count matrices** (`GSE342782_Processed_DirectInf_neuronHD10s_BulkSeq_Counts.csv.gz`, `GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz`), reproducing the authors' pipeline (CPM, log2(1+CPM), module scores, Welch t, Mann–Whitney U, permutation null B = 5,000 seed 20261019): all W0 baselines; all 24 module contrasts across three group comparisons; gene-level diffs and Welch P values for the quoted E1 and M3 genes; global DE counts at |log2FC| > 0.5; per-sample mean log2CPM; panel gene presence/absence per module; detection fractions (CPM > 1) for all E1/M1 genes and key markers; M1 and E1 gene-level composition; E1 sensitivity analysis excluding Kv7 genes; route × module interaction by label permutation; TAC1 group means. **Discrepancies found between manuscript text and data: two** (Issue F1: "all other modules fully represented"; Issue F2: "M4 … every contrast (all P ≥ 0.11)"). **Discrepancies between manuscript text and published literature: three** (Issue A2: PHN definition; Issue C1: ESWT evidence grade and citation pairing; Issue E1: attribution of YAP/TAZ mechanism to [7][8]). All other checked numbers matched exactly.

**Literature verified with identifiers:** [1] PMID 39211798; [4] PMID 42734212 / DOI 10.1002/ana.78352; [5] PMID 41091131; [7] PMID 37303680; [8] PMID 35844093 / DOI 10.15252/embj.2022111799; [9] PMID 41504389 / GSE314229; [13] PMID 32195953; [14] PMID 32641142 (as listed in the manuscript; protocol paper — no results published). [2] and [6] are placeholders (Issues B1, B2). Items marked "PMID not independently verified" in Issue B3 (Woo 2014, Bennett 2019 Physiol Rev, Sci Rep 2024 iPSC-SN characterisation) should be re-verified by the authors before submission; every other citation I propose carries a PMID or DOI I confirmed. Note for the authors: the frequently cited PMID 25140144 for Ranade et al. 2014 is **wrong** (it is a psychology paper); the correct PMID is 25471886.

**Not verifiable by me:** the pre-registration claim itself (protocol v0.4 / frozen panel `mtp-frozen-2026-10-19`) — I take it as asserted; a public time-stamped deposit would make it checkable (Question 1). The donor age/sex metadata are not in the GEO series matrix; the corroborating statement comes from the original paper's published limitations.

---

## 10. Must-fix list (numbered, in priority order)

1. Rewrite the central allodynia-substrate claim (Abstract manuscript:21; §4.1 manuscript:93; §5 manuscript:109) to a hypothesis-level statement per Issue A1; stop treating the PIEZO2 null as preserved mechanical gating.
2. Correct the false PHN definition (manuscript:31, manuscript:93) and fill placeholder [6] with Johnson & Rice 2014 (PMID 25317872), Finnerup 2016 (PMID 27115670), Scholz 2019 (PMID 30586071), Pfau 2014 (PMID 24525274).
3. Replace placeholder [2] with a real citation (Wang 2024 PMID 39471697 and/or Liang & Fan 2023 PMID 37304287), or remove and reframe (Issue B2).
4. Correct §2.3 (manuscript:53): N2 lost 3 genes, N3 lost 1 gene (Issue F1).
5. Correct §3.2 (manuscript:71): M4 is suppressed under VZV (P = 0.024); delete the contradictory "all P ≥ 0.11" clause (Issue F2).
6. Re-grade the ESWT evidence statement (manuscript:33) and remove [6] from the [5,6] pairing (Issue C1).
7. Replace the mis-attributed ESWT-mechanism sentence (manuscript:33, 101) with Dupont 2011, Li 2021, Zhao 2021 and qualified language (Issue E1).
8. Add the must-cite literature of Issue B3 (minimum: PHN definitions; Coste 2010; Ranade 2014; Szczot 2021; Murthy 2018 / PIEZO2-allodynia 2018; Cata 2022; Bennett & Woods 2014) and discuss it in §3.1/§4.1/§4.3.
9. Disclose the full HD10 phenotype (SCN10A/TRPM8/TRPA1 at or below detection; PIEZO2–TRPV1 co-dominance) and the YAP1/WWTR1 near-absence in §3.1/§4.4; temper "transcriptionally inert" and the "redirection" claim (Issues D1, D3).
10. Fix "M1 is effectively a PIEZO2-dominated module" → P2RX3-dominated, and report within-module gene contributions (Issue D2).
11. Add the route × module interaction test with the route≡batch caveat, and align Abstract/Conclusions with §3.4's hypothesis-generating framing (Issue F3).
12. Disclose panel gene overlap (PTK2 in M3/M4; KCNQ2/KCNQ3 in E1/N1) and add the disjoint-module sensitivity analysis (Issue F4).
13. Hedge the absolute novelty claims (manuscript:15, 33) with "to our knowledge" and acknowledge the animal-level mechanochannel–pain literature (Issue C2).

---

## 11. Overall verdict

**Major revision.** The statistical core is genuine and unusually well disciplined: every number I could recompute reproduced exactly, the primary endpoint is an honestly reported correctly-powered null, the neutral-control and global-shift diagnostics are sound, and the route-dependence observation is statistically real (interaction P < 0.0002). The blockers are on the interpretation side: the central claim converts a null on PIEZO2 plus a suppression of electrogenic channels into "a plausible molecular substrate for mechanical allodynia" without functional evidence and in the wrong disease stage; the paper opens with a clinically false definition of PHN; two verifiable factual errors sit in Methods/Results; the ESWT evidence grade is overstated and its mechanistic citations are mis-attributed; the two placeholders support load-bearing sentences; and the mechanistically decisive literature (PIEZO2 in allodynia, EV pain signalling, iPSC-SN limits, Nav channelopathies) is absent. All of these are fixable in text and citations without new experiments, but the Abstract, Introduction and Conclusion need substantive rewriting, not cosmetic editing, before the paper can be recommended for Journal of Pain Research.
