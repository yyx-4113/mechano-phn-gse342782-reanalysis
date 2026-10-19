# B5 — Clinical editorial review (anesthesiologist / pain clinician; language and figures auditor)

**Manuscript:** `manuscript/manuscript_v1.1.5.md` (214 lines; cross-checked against the compiled `manuscript_v1.1.5.docx`, which carries the five figure images and the only figure captions in the package)
**Venue:** Journal of Pain Research — Original Research
**Frame:** reviewed as a first submission. No prior-round material was consulted.

---

## 1. Cross-section consistency (abstract / results / discussion / limitations / conclusions read as a whole)

### B5-1. The abstract's route claim is stronger than the Results section's own walk-back — a direction claim survives where only a magnitude claim is supported

【Problem】The Abstract Conclusions state that HZ-serum exosomes — "but not direct VZV infection" — down-regulated the electrogenic nociceptor program, while §3.4 explicitly states that the route dependence is one of magnitude, not direction, because TRPV1 (the lead gene) also falls under direct VZV infection.
【Evidence】`manuscript_v1.1.5.md:23` (Abstract): "HZ-serum exosomes — but not direct VZV infection — down-regulated the electrogenic nociceptor program, with only TRPV1 surviving within-module correction, while the ECM-Hippo stiffness program was inert within a bounded null." vs `manuscript_v1.1.5.md:96` (§3.4): "The route dependence is one of magnitude rather than direction: TRPV1 mRNA also fell under direct VZV infection (-0.149 log2CPM, Welch P = 0.008, within-E1 q = 0.144), roughly a quarter of the HZ-exosome effect (-0.567); PIEZO2 likewise fell modestly under direct infection (-0.144, P = 0.021)." I verified both numbers from the deposited gene-level table (`analysis/results/layer1/layer1_gene_level.csv`, contrast `VZV_vs_Mock`: TRPV1 −0.1487, P = 0.0080, q = 0.1435; PIEZO2 −0.1438, P = 0.0213) — they are exact. The module-level E1 difference under direct infection is indeed null (+0.0005, P = 0.996; `layer1_module_scores.csv`), so the abstract sentence is defensible only at the module level, but the attached clause "with only TRPV1 surviving within-module correction" invites the gene-level reading, under which the abstract is contradicted by §3.4.
【Why it matters】The abstract is the most-read part of the paper and the part a clinician will quote. As written, it asserts a direction-level route dissociation ("exosomes yes, direct infection no") that the Results section has already retracted to magnitude-only. A referee who reads §3.4 will flag the abstract as inconsistent, and the discrepancy undermines the paper's otherwise exemplary hedging discipline.
【Specific fix】Replace the sentence at line 23 with: "In this 36-h exposure of an immortalized embryonic dorsal-root-ganglion line, HZ-serum exosomes suppressed the electrogenic nociceptor module, with only TRPV1 surviving within-module correction, whereas direct VZV infection produced no module-level E1 shift and reduced TRPV1 to a lesser degree; the ECM-Hippo stiffness program showed no detectable transcriptional response within a bounded null." (Also aligns the abstract with §4.3's "'no detectable response' is the claim, not 'inert by mechanism'".)

### B5-2. The Figure 2d caption carries the un-weakened interaction claim; every prose occurrence is caveated

【Problem】The Figure 2d caption (present in the .docx build; see B5-16 on caption absence from the .md) states the interaction result without the post hoc designation and without the detected-gene sensitivity analysis that renders it non-significant — the one place in the package where the strong version of the claim survives intact.
【Evidence】`manuscript_v1.1.5.docx`, Figure 2d caption: "Perturbation route and channel programme: E1-selective suppression under HZ exosomes (interaction P = 0.0017); reciprocal VZV pattern not significant (P = 0.19)." Compare the four caveated occurrences: Abstract (`manuscript_v1.1.5.md:21`): "A post hoc interaction (P = 0.0017) was non-significant among detected genes (P = 0.16)."; §3.4 (line 96): "...does not survive a sensitivity analysis for detection-floor asymmetry between modules... yields a much smaller interaction (-0.072) that is not significant (exact permutation P = 0.16)... We disclose that the contrast-of-contrasts interaction test was specified post hoc..."; §4.1 (line 116): "The full-module interaction that initially suggested selective E1 suppression (P = 0.0017) did not survive a detected-gene subset analysis (P = 0.16), so we do not present it as a confirmed dissociation."; Conclusions (line 138): same construction. (Values verified: −0.1417/P = 0.001748 and −0.0718/P = 0.1573, `layer1_results.json` keys `interaction` and `interaction_detected_only`.)
【Why it matters】Figure captions are read independently of the text; a clinician or referee scanning the figure list sees "E1-selective suppression (P = 0.0017)" presented as established. This is precisely the failure mode the rest of the manuscript works hard to avoid, and it will be caught.
【Specific fix】Replace the caption with: "Figure 2d. Perturbation route and channel program: module-score shifts by route (nominal; not a confirmed dissociation). Under acute-HZ serum exosomes the full-module E1−M1 interaction was −0.142 log2CPM (exact permutation P = 0.0017), but this post hoc test was not significant when both modules were restricted to detected genes (−0.072; P = 0.16); under direct VZV infection the reciprocal interaction was not significant (−0.051; P = 0.19). n = 7 vs 7 (exosomes) and 6 vs 6 (direct infection)."

### B5-3. §4.4 contradicts itself: (vi) calls the exosome effect "robust E1-selective"; (xi) says selectivity is "nominal and gene-level, not a demonstrated module-level dissociation"

【Problem】Within the same Limitations section, item (vi) describes "the robust E1-selective exosome effect" as the foundation of the route-dependence claim, while item (xi) states that any claim of channel-class selectivity is nominal and gene-level.
【Evidence】`manuscript_v1.1.5.md:132`: "(vi) The direct-infection M1 effect is borderline (permutation P = 0.05) and the reciprocal dissociation is unsupported by the interaction test (P = 0.19); the route-dependence claim rests on the robust E1-selective exosome effect and requires confirmation in independent models." vs `manuscript_v1.1.5.md:134`: "(xi) The E1 signal is not separable from the neutral N1 control at the module level: N1 itself shifted by -0.156 log2CPM under HZ exosomes (permutation P = 0.151) versus E1 -0.220 (P = 0.013), and their difference gives E1 - N1 = -0.064 (P = 0.178). Any claim of channel-class selectivity is therefore nominal and gene-level, not a demonstrated module-level dissociation." (Both sets of numbers verified: N1 −0.1558/P = 0.1509, E1 −0.2196/P = 0.0128 in `layer1_module_scores.csv`; E1−N1 = −0.0638/P = 0.1783 in `layer1_results.json` key `e1_vs_n1_benchmark`.)
【Why it matters】The E1 suppression versus control exosomes is robust; the E1 *selectivity* (versus M1 and versus N1) is the fragile part. Calling the compound "robust E1-selective effect" re-imports the weakness the same paragraph later disclaims, and a careful referee will quote the two items against each other.
【Specific fix】In (vi), replace "the route-dependence claim rests on the robust E1-selective exosome effect and requires confirmation in independent models" with "the route-dependence claim rests on the robust module-level E1 suppression under exosomes, while its E1-selective aspect is nominal and gene-level (see xi), and requires confirmation in independent models".

### B5-4. §3.2 presents a non-significant-after-correction M4 result as "suppressed" without its q value

【Problem】§3.2 describes M4 under direct VZV infection as "notably... suppressed (-0.054; P = 0.03)" without noting that the Benjamini-Hochberg q across the eight modules is 0.20 — i.e., the result does not survive the paper's own multiplicity control, and §4.4(vi) elsewhere calls the direct-infection module effects "borderline".
【Evidence】`manuscript_v1.1.5.md:88`: "M4 mechano-effectors was null under HZ exosomes (P = 0.46) but, notably, was suppressed under direct VZV infection (-0.054; P = 0.03)." Deposited values (`layer1_module_scores.csv`, `VZV_vs_Mock`): diff −0.0544, permutation P = 0.0303, BH q = 0.1991. The P values quoted in this sentence are also unlabeled (they are permutation P values), unlike §3.3/§3.4 which label the test.
【Why it matters】"Suppressed (P = 0.03)" reads as a positive finding; with q = 0.20 it is a nominal, uncorrected signal. The Results section is otherwise scrupulous about this distinction, so this sentence is an outlier a referee will use to argue the paper overstates module-level effects under direct infection.
【Specific fix】Replace with: "M4 mechano-effectors was null under HZ exosomes (permutation P = 0.46) and only nominally reduced under direct VZV infection (-0.054; permutation P = 0.03; BH q = 0.20 across the eight modules), a borderline signal reported for completeness."

### B5-5. Two genes that survive within-module BH correction in M2 (EZR, PXN) are never reported — the "only TRPV1 survives" narrative is incomplete

【Problem】The manuscript reports within-module BH q values for E1 genes but never discloses that two M2 (membrane-cytoskeleton) genes also survive within-module correction under HZ exosomes — both down-regulated, with smaller P values than several E1 genes the paper does discuss.
【Evidence】Recomputed from `analysis/results/layer1/layer1_gene_level.csv` (contrast `HZexo_vs_CtrlExo`, within-module BH q < 0.05): EZR −0.3346, Welch P = 0.00083, q = 0.0167 (module M2); PXN −0.2102, Welch P = 0.0019, q = 0.0190 (module M2). Neither gene appears anywhere in `manuscript_v1.1.5.md`; §3.3 (line 92) reports only the E1 within-module q values, and §2.4 (line 59) promises within-module q values "for genes belonging to a panel module" as a general product. The in-image title of Figure 2c states "only TRPV1 survives within-module BH (q = 0.017)" without the E1 qualifier that the Abstract (line 21: "the only gene surviving Benjamini-Hochberg correction within E1") correctly carries.
【Why it matters】A referee who opens the deposited gene-level table (which the manuscript advertises as regenerating every number) will find EZR and PXN immediately and will ask whether the mechano-module "inertness" narrative was filtered. Selective reporting of within-module hits — even ones explicitly framed as descriptive — is a credibility risk that is cheap to eliminate.
【Specific fix】Add to §3.3 after the E1 gene-level paragraph: "Within the membrane-cytoskeleton module M2, two genes also survived within-module correction (EZR, -0.335, Welch P = 0.0008, q = 0.017; PXN, -0.210, P = 0.002, q = 0.019); because the M2 module as a whole was not shifted (P = 0.068), these are reported as descriptive gene-level observations and are not claimed as module-level effects." Also amend the Figure 2c in-image title to "only TRPV1 survives within-module BH within E1 (q = 0.017)".

### B5-6. Minor symmetry gap: the Abstract's M1 description omits the "resolution-limited" qualifier that every other occurrence carries

【Problem】The Abstract describes M1 as "at most marginally shifted (P = 0.11; PIEZO2 P = 0.18)" without the resolution-limit qualifier (detected-gene subset flips M1 to P = 0.046) that §3.3, §3.4, §3.6, §4.4(v) and the Conclusions all carry.
【Evidence】`manuscript_v1.1.5.md:21` vs `manuscript_v1.1.5.md:106` ("detected-gene M1 flipped to -0.171 (P = 0.046), indicating that the 'spared' M1 interpretation is resolution-limited") and line 138 ("M1 itself resolution-limited, flipping to significant when detected genes only are analyzed, P = 0.046"). Verified: `layer1_results.json` key `sensitivity_detected_genes` → M1, 5 genes, −0.1709, P = 0.0460.
【Why it matters】"At most marginally shifted" is weaker than "spared" and is not a stronger claim, so this is a completeness issue rather than a contradiction — but the Abstract is the one place a reader gets the M1 result without its central caveat.
【Specific fix】Replace "M1 was at most marginally shifted (P = 0.11; PIEZO2 P = 0.18)" with "M1 was at most marginally shifted and is itself resolution-limited (P = 0.11; PIEZO2 P = 0.18; detected-gene subset P = 0.046)".

---

## 2. Clinical claims calibration (what a pain clinician could read as a claim about PHN patients)

### B5-7. The title promises "human sensory neurons" and "route-dependent effects" at a strength the data do not carry

【Problem】The title asserts "route-dependent transcriptional effects ... on ion-channel programs in human sensory neurons"; the model is a single immortalized embryonic clonal line, and the paper's own §3.4/§4.2 state that route dependence is magnitude-level and not a confirmed dissociation.
【Evidence】`manuscript_v1.1.5.md:1` (title) vs `manuscript_v1.1.5.md:132` (§4.4(i)): "the term 'human sensory neurons' in this paper should be read as 'this embryonic clonal line'", and line 122 (§4.2): "the route difference is best stated as 'exosomes yield a clear E1 signal; direct infection does not yield a selective M1 signal' rather than a confirmed cross-program dissociation." The Limitations section explicitly retracts the two things the title asserts.
【Why it matters】Titles are indexed, quoted, and read without the caveats. For a JPR readership, a title implying route-dependent channel effects in human neurons from a 36-h exposure of an embryonic line overstates the evidence and invites a desk-level calibration objection.
【Specific fix】Replace the title with: "Transcriptional effects of varicella-zoster virus and patient serum exosomes on ion-channel programs in a human sensory-neuron cell line (HD10.6): a prospectively specified reanalysis of GSE342782". (If the authors prefer to keep "route-dependent", the minimum edit is to qualify the model: "...in human sensory neurons (HD10.6 embryonic line)"; the data support the qualified form only.)

### B5-8. "Mechanical allodynia is a cardinal symptom of PHN" overstates its prevalence and role

【Problem】The opening sentence calls mechanical allodynia a cardinal symptom of PHN; PHN is defined by persistent dermatomal pain, and mechanical allodynia is a common but non-universal associated feature (a subset of patients; dynamic mechanical allodynia is not present in all).
【Evidence】`manuscript_v1.1.5.md:17`: "Mechanical allodynia is a cardinal symptom of postherpetic neuralgia (PHN), yet mechanotransduction is rarely examined in PHN transcriptomics." The manuscript's own definitional anchor (`manuscript_v1.1.5.md:33`, citing ref 20) defines PHN by pain persistence ≥90 days, not by allodynia.
【Why it matters】The entire rationale of the paper hangs on this sentence; overstating the symptom's status weakens the motivation in the eyes of pain-clinician referees and is the kind of calibration error that colors the whole read.
【Specific fix】Replace with: "Mechanical allodynia — innocuous cutaneous stimuli transduced as pain — is a common and clinically prominent feature of postherpetic neuralgia (PHN), yet mechanotransduction is rarely examined in PHN transcriptomics."

### B5-9. The proposed clinical next step (serial exosome measurement in patients) is not yet well-posed

【Problem】The clinical proposal in §4.1 measures "this exosome phenotype" serially in patients, but the phenotype is an in-vitro transcriptional response of the HD10.6 line to exosomes — not a property of the exosomes that can be measured in a patient sample without the reporter assay — and the proposal names no comparator, endpoint definition, time grid, or confounders.
【Evidence】`manuscript_v1.1.5.md:118`: "Clinically, this raises a testable question: if acute-HZ serum exosomes carry a channel-suppressive signature to sensory neurons, then serial measurement of this exosome phenotype in patients from rash onset through 90 days could test whether its presence or persistence predicts progression to PHN — a hypothesis this dataset cannot answer but which frames the next clinical step." The same section concedes the balance "cannot be tested without protein-level or electrophysiological data", and §3.5 (line 100) reports the PHN-exosome contrast — the contrast closest to the proposal — as "non-specific and confounded".
【Why it matters】As written, a reader could infer a simple longitudinal biomarker study (measure exosomes, predict PHN). The actual proposal requires a bioassay whose reproducibility, dose-dependence (§4.4(xiii): dose "not independently quantified or dose-ranged"), and specificity (the PHN-exosome non-specificity) are all unestablished. A vague next step is the most common reason a JPR referee asks for deletion of the clinical paragraph.
【Specific fix】Replace the sentence with: "Clinically, this raises a testable question: whether the channel-suppressive response of sensory neurons to acute-HZ serum exosomes is transient or persistent, and whether its persistence distinguishes patients whose pain resolves from those who progress to PHN. A well-posed test would enrol consecutive patients with acute herpes zoster at rash onset, collect serum before antiviral treatment where feasible, expose the same HD10.6 assay to blinded exosome aliquots at fixed intervals (for example baseline and 2, 4, 8, and 12 weeks), pre-specify PHN at 90 days as the endpoint with progression-free patients as the comparator group, and adjust for age, sex, and analgesic exposure. The assay's reproducibility, its dependence on exosome dose, and the non-specific PHN-exosome behaviour observed here would all need to be resolved before such a study could be powered; the present data only motivate it."

### B5-10. The ESWT context paragraph cites a rat single-cell dataset without saying so

【Problem】§4.3 invokes "bone-callus single-cell data" as evidence that ESWT-released vesicles act on mesenchymal rather than neuronal cells, without noting that the underlying dataset (ref 12, GSE314229) is a rat tibial-osteotomy model.
【Evidence】`manuscript_v1.1.5.md:126`: "in bone-callus single-cell data, ESWT released extracellular vesicles through an ATP/P2X7R/p38MAPK axis acting on mesenchymal rather than neuronal cells,^12^". Ref 12 (`manuscript_v1.1.5.md:196`) is the GEO accession; the series record (GSE314229) is "Early Radial Extracorporeal Shockwave Stimulation on Proximal Tibial Circular Osteotomy Site Enhanced Heterotopic Skin Wound Healing via Small Extracellular Vesicles", organism Rattus norvegicus. The manuscript otherwise handles the species issue carefully (e.g., §4.1's mouse/human Piezo2 literature is correctly attributed).
【Why it matters】The compartmental argument ("not neuronal cells") is load-bearing for the paper's redirection of the mechanical-axis search; readers are entitled to know it rests on rodent bone-wound data, not human or neuronal data.
【Specific fix】Replace with: "in single-cell data from a rat bone-callus model, ESWT released extracellular vesicles through an ATP/P2X7R/p38MAPK axis acting on mesenchymal rather than neuronal cells,^12^".

---

## 3. Language and register

### B5-11. British spelling "programme" survives in the Figure 2d caption

【Problem】The Figure 2d caption uses the British "programme"; the manuscript body uses American "program" throughout.
【Evidence】`manuscript_v1.1.5.docx`, Figure 2d caption: "Perturbation route and channel programme: ...". Body usage: "channel programs" (title, line 1), "ECM-Hippo stiffness program" (§3.2, line 88), "translational-program response" (§3.6, line 106). (I checked the whole .md and .docx text for normalisation/behaviour/colour/centre/whilst/amongst — this is the only instance.)
【Why it matters】JPR requires American English; a lone British spelling in a caption is an easy editorial rejection point.
【Specific fix】In the Figure 2d caption, change "channel programme" to "channel program" (use the replacement caption drafted in B5-2, which is already corrected).

### B5-12. "down-regulated" (text) vs "downregulated" (figure titles) is inconsistent

【Problem】The body hyphenates "down-regulated"/"up-regulated"; the in-image figure titles use the closed form "downregulated".
【Evidence】`manuscript_v1.1.5.md:23` ("down-regulated the electrogenic nociceptor program"), line 118 ("up-regulated substance P"), line 134 ("up-regulation of substance P") vs the Figure 2c in-image title: "Classical nociceptor channels (E1) downregulated by acute HZ serum exosomes". Only three hyphenated instances exist in the .md; the closed form appears only inside the PNGs.
【Why it matters】Inconsistent hyphenation of the paper's central verb across text and figures is the kind of copy-editing catch that survives to proof stage and looks careless.
【Specific fix】Standardize on the hyphenated "down-regulated"/"up-regulated" in the figure titles (or, if the journal prefers the closed form, change the three body instances — pick one and apply it everywhere including captions).

### B5-13. §4.1 contains a three-deep negative stack that is hard to parse

【Problem】"Our data therefore exclude transcriptional up-regulation of the mechanogated program in this model; they do not exclude Piezo2-dependent mechanical sensitization, and we do not read the M1 null as refuting a mechanical axis in PHN." — exclude / do not exclude / do not read ... as refuting in one sentence.
【Evidence】`manuscript_v1.1.5.md:116`.
【Why it matters】This is the paper's most important interpretive sentence for a mechanotransduction audience; the triple negative obscures exactly the distinction (transcript vs function) the paragraph is trying to make, and it is the sentence most likely to be misquoted.
【Specific fix】Replace with: "Our data therefore show no transcriptional up-regulation of the mechanogated program in this model. Piezo2-dependent mechanical sensitization remains possible, because Piezo2 function is regulated post-translationally — most directly by relief of its voltage block — so the M1 null should not be read as evidence against a mechanical axis in PHN."

### B5-14. The CCI sentence in §3.6 is unreadable as written ("null-by-construction at the absolute scale")

【Problem】"consistent with the rank-based CCI being null-by-construction at the absolute scale that drives the module-level E1 signal" does not parse; the intended meaning (the CCI compares within-sample ranks between two gene sets and therefore cannot see absolute shifts common to both) is recoverable only with effort.
【Evidence】`manuscript_v1.1.5.md:106`: "The CCI did not differ between groups under any contrast (all permutation P >= 0.82; Figure 2b), consistent with the rank-based CCI being null-by-construction at the absolute scale that drives the module-level E1 signal; CCI is reported as a relative-displacement negative control, not as confirmatory evidence." (The P ≥ 0.82 claim is verified: `layer1_cci.csv`, permutation P = 0.833/0.851/0.965.)
【Why it matters】The CCI is one of the paper's two neutral-control pillars; if its logic cannot be understood, the negative control cannot do its rhetorical work, and referees will ask what "null-by-construction" is supposed to mean (it is not null by construction — it is a relative measure that happens to be insensitive here).
【Specific fix】Replace with: "The CCI did not differ between groups under any contrast (all permutation P >= 0.82; Figure 2b). Because the CCI compares within-sample expression ranks between the M1 and E1 gene sets, it is insensitive to absolute expression shifts that affect both modules; it is reported here as a relative-displacement negative control, not as confirmatory evidence."

### B5-15. §3.1 mixes units and denominators across genes in one sentence

【Problem】PIEZO2 and ITGB1 are quoted as mean CPM (all 12 infection-experiment samples), while SCN9A and TRPV1 are quoted as mean log2CPM with both denominators — in the same sentence, with the switch unflagged.
【Evidence】`manuscript_v1.1.5.md:69`: "...expressed PIEZO2 at high levels (mean CPM 245.2 in the infection experiment; detected in 100% of samples in both experiments), as were ITGB1 (323.6 CPM) and the electrochemical nociceptor channels SCN9A (mean log2CPM 8.31 across all 12 samples; 8.39 in mock samples only) and TRPV1 (6.94 across all 12 samples; 7.02 in mock samples only)." (All values verified against `layer1_results.json` keys `w0` and `baseline`: PIEZO2 245.24 CPM; SCN9A 8.3137 all-12 / 8.3907 mock-only; TRPV1 6.9422 / 7.0166.)
【Why it matters】Table 1 reports these same genes in CPM; the text reports some of them in log2CPM. A reader checking Table 1 against §3.1 will find different numbers for the same genes and no key to reconcile them.
【Specific fix】Replace with: "...expressed PIEZO2 at high levels (mean 245.2 CPM; mean log2CPM 7.94 across all 12 infection-experiment samples; detected in 100% of samples in both experiments), as were ITGB1 (323.6 CPM) and the electrochemical nociceptor channels SCN9A (mean log2CPM 8.31 across all 12 samples; 8.39 in mock samples only) and TRPV1 (6.94 across all 12 samples; 7.02 in mock samples only)."

### B5-16. The manuscript references its own internal review rounds

【Problem】§4.4 introduces items (xi)-(xiii) as following "from the Round-4 internal benchmarks" — a first submission to JPR cannot refer to internal revision rounds.
【Evidence】`manuscript_v1.1.5.md:134`: "Three further constraints follow from the Round-4 internal benchmarks."
【Why it matters】Any handling editor will strike this; it also implicitly tells referees the manuscript has been through rounds they cannot see, which compromises the review frame.
【Specific fix】Replace with: "Three further constraints qualify the interpretation."

### B5-17. Smaller register/tense items

【Problem】Three lower-severity language items: (a) §4.3 opens with a self-assessment of consequence ("Perhaps the most consequential finding for the mechanotransduction field is what did not move"); (b) the VZV-route paragraph sits at the end of §3.4 although it describes direct-infection results that logically belong with §3.5's route/contrast material; (c) §4.4(vii) "The analysis is hypothesis-generating throughout: no causal or therapeutic claim is made" is a double-barreled sentence whose second clause restates the first.
【Evidence】(a) `manuscript_v1.1.5.md:126`; (b) the paragraph beginning "The VZV picture remains weak and inconsistent:" at `manuscript_v1.1.5.md:96`, after the interaction disclosure; (c) `manuscript_v1.1.5.md:132`.
【Why it matters】Individually minor; collectively they are the kind of polish that separates "accept with minor edits" from "major revision" in a language-sensitive journal.
【Specific fix】(a) "The most informative result for the mechanotransduction field may be what did not move." (b) Move the "The VZV picture remains weak and inconsistent" paragraph to the start of §3.5, or retitle §3.4 and fold it there. (c) "The analysis is hypothesis-generating throughout: no causal, mechanistic, or therapeutic claim is made."

---

## 4. Table 1, figure callouts, and the missing figure captions

### B5-18. The .md manuscript contains no figure captions at all — captions exist only inside the .docx build and inside the PNG titles

【Problem】All five figures are cited in text, but `manuscript_v1.1.5.md` contains no caption text anywhere; the only captions in the package live in the compiled .docx (as paragraphs following each embedded image), and the PNGs carry their own in-image titles. If the .md is the submission source, the figures arrive uncaptioned; if the .docx is, its captions are stale in one case (B5-2) and one uses British spelling (B5-11).
【Evidence】Grep of `manuscript_v1.1.5.md`: figure callouts at lines 69 ("Figure 1"), 92 ("Figure 2a", "Figure 2c"), 96 ("Figure 2d"), 106 ("Figure 2b"); no "Figure N." caption paragraph exists (contrast the Table 1 title at line 71). The .docx contains five images and five caption paragraphs, including the uncaveated Figure 2d caption quoted in B5-2.
【Why it matters】JPR requires a caption for every figure; captions must also carry the statistical qualifiers that the in-image titles cannot (they are clipped, see B5-20). As submitted, a typesetter receiving the .md would have to invent captions.
【Specific fix】Add the following five captions to the .md (and use them in the .docx), replacing the existing .docx captions:

- "Figure 1. Study design and prospectively specified analysis pipeline. GSE342782 comprises two experiments in differentiated HD10.6 human sensory neurons (31 samples): mock infection (n = 6) versus direct VZV infection (n = 6), harvested 4 days post-infection; and 36-hour exposure to serum-derived exosomes from healthy controls (n = 7), patients with acute herpes zoster (n = 7), or patients with PHN (n = 5). The frozen pre-analysis panel (M1-M4 mechanotransduction modules, E1 electrochemical nociceptor module, N1-N3 neutral controls) and the pre-registered data-examination gate are shown, followed by module scoring on log2(1+CPM) with Welch t, Mann-Whitney U, and exact label-permutation inference. The single pre-specified primary endpoint is M3 under HZ exosomes versus control exosomes; E1 and M1 under the same contrast are secondary; the PHN-exosome and direct-infection contrasts are exploratory."
- "Figure 2a. Module-score differences (HZ-exo minus control-exo, log2CPM) for the primary contrast, with neutral controls displayed alongside. E1 (-0.220; exact permutation P = 0.013; BH q = 0.034) is the only biological module significantly shifted; N3 (+0.391; P = 0.002) responds as an exposure control and N2 (-0.022; P = 0.006) rests on a single low-baseline gene; M1-M4 and N1 are not significant at the full-module level. *P < 0.05, **P < 0.01 (exact permutation P); n = 7 versus 7."
- "Figure 2b. Gene-level differences within E1 for the primary contrast (Welch t on log2(1+CPM)); the eight E1 genes with the largest absolute differences are shown. Only TRPV1 survives Benjamini-Hochberg correction within the module (q = 0.017); KCNS1, SCN9A, ASIC1 and ASIC2 are nominally significant (q approximately 0.07-0.13); SCN10A lies below the detection floor in the exosome experiment (mean CPM 0.55; detected in 11% of samples) and is shown for completeness only; KCNQ2 and CACNA1H are not statistically distinguishable from zero (P = 0.47 and P = 0.24) and are shown because of their effect sizes."
- "Figure 2c. Route-dependent channel-program shifts (nominal; not a confirmed dissociation). Left: direct VZV infection versus mock; right: HZ exosomes versus control exosomes. The full-module E1-M1 interaction under HZ exosomes (-0.142 log2CPM; exact permutation P = 0.0017) is a post hoc test and does not survive restriction of both modules to detected genes (-0.072; P = 0.16); the reciprocal interaction under direct infection is not significant (-0.051; P = 0.19). n = 6 versus 6 and 7 versus 7."
- "Figure 2d. Channel-complementarity index (CCI) differences by contrast (all non-significant; exact permutation P >= 0.82). The CCI — the within-sample difference between mean expression ranks of the M1 and E1 gene sets across all 43,236 matrix genes — is a relative-displacement negative control. n = 7/7 (HZ exosomes), 5/7 (PHN exosomes), 6/6 (direct infection)."

(These captions assume the renumbering in B5-23.)

### B5-19. Figure 2b's numeric annotation does not match the deposited data

【Problem】The first bar of Figure 2b is annotated "+82.422", but the deposited CCI result for that contrast is +82.7222 — a transposed digit.
【Evidence】Figure 2b in-image annotation (verified by magnification): "+82.422" above the HZexo_vs_CtrlExo bar. `analysis/results/layer1/layer1_cci.csv`: `HZexo_vs_CtrlExo,82.7222`. The other two bars (-74.344, -19.792) match the CSV exactly.
【Why it matters】A number printed on a figure that differs from the deposited artifact is a data-integrity flag in the referee's eyes, even when the difference is a typo; it also invites re-examination of every other figure annotation.
【Specific fix】Regenerate Figure 2b with the annotation "+82.722" (or add the exact permutation P values 0.83/0.85/0.97 to the three bars so the annotation is checkable against the caption).

### B5-20. Figure 2c shows two statistically null genes as indistinguishable red bars, its title is clipped, and its selection rule is unstated

【Problem】Figure 2c plots eight E1 genes, of which two (KCNQ2, P = 0.47; CACNA1H, P = 0.24) are far from significant yet are drawn identically to the significant ones with no per-gene P or q annotation; the in-image title is cut off at the right edge ("...(q = 0"); and neither the figure nor its caption states how the eight genes were selected (they are the eight largest |log2FC|, not the eight smallest P values).
【Evidence】Recomputed from `layer1_gene_level.csv` (`HZexo_vs_CtrlExo`): KCNQ2 −0.2111, Welch P = 0.4694; CACNA1H −0.2972, P = 0.2410; by contrast the six nominally significant E1 genes are TRPV1, SCN10A, KCNS1, SCN9A, ASIC1, ASIC2. The top-8 by |log2FC| are exactly the eight genes shown. The clipped title ends "...only TRPV1 survives within-module BH (q = 0" (confirmed by magnified inspection of the PNG).
【Why it matters】A clinician reading the figure sees eight red bars "downregulated by acute HZ serum exosomes" and will assume all eight are hits; the two null genes inflate the apparent breadth of the suppression. The clipped title looks like a production error, and the unstated selection rule (|log2FC| rather than significance) is the kind of thing referees ask about explicitly.
【Specific fix】Annotate each bar with its Welch P (or asterisks for nominal P < 0.05) and mark KCNQ2/CACNA1H as ns; shorten the in-image title to "Fig 2c. E1 genes with the largest HZ-exo effects; only TRPV1 survives within-module BH within E1 (q = 0.017)" so it fits the canvas; and state the selection rule in the caption (drafted in B5-18).

### B5-21. Figure 2a: the asterisk key is undefined and there are no n labels or effect-size uncertainty

【Problem】Figure 2a uses "*" and "**" markers with no legend entry defining them, gives no group sizes, and shows point estimates without any uncertainty (no CI whiskers, no per-sample values).
【Evidence】Figure 2a legend defines only the three color classes (M1-M4 mechano modules, E1, N1-N3 neutral controls); the markers on E1 (*), N2 (**) and N3 (**) are unexplained in-figure. E1 P = 0.013, N2 P = 0.006, N3 P = 0.002 (`layer1_module_scores.csv`) are consistent with * = P < 0.05, ** = P < 0.01, but this is nowhere stated. n = 7 vs 7 appears nowhere on the figure.
【Why it matters】Undefined significance symbols are the most common figure-desk rejection at Dove Press titles; without n or uncertainty a bar chart of seven-versus-seven module scores also overstates precision — a point the manuscript itself makes elsewhere ("the plan mandates reporting effect size alongside every P value", line 106).
【Specific fix】Add to the caption or figure: "*P < 0.05, **P < 0.01 (exact permutation P); bars are group-mean differences, n = 7 versus 7; whiskers show the permutation-inversion 95% CI where available." (The caption drafted in B5-18 includes the key and n; adding CI whiskers is recommended but optional.)

### B5-22. Figure 2d: the most significant bar in the paper carries no significance annotation, while null bars carry "ns"

【Problem】In the right-hand panel of Figure 2d, the E1 bar (-0.220; P = 0.013 — the paper's principal positive result) has no significance marker, while every null bar in both panels is labeled "ns" and the borderline M1 bar is labeled "*".
【Evidence】Figure 2d, right panel ("Acute HZ serum exosomes (vs control-exo)"): M1 bar labeled "-0.078 ns"; E1 bar labeled "-0.220" with no marker. Verified values: E1 −0.2196, permutation P = 0.0128 (`layer1_module_scores.csv`).
【Why it matters】An unannotated significant bar next to annotated null bars reads as an omission of the key result; it also breaks the figure's own visual grammar.
【Specific fix】Add "*" (P < 0.05) to the right-panel E1 bar and state the marker key in the caption (drafted in B5-18).

### B5-23. Figures are cited out of numerical order

【Problem】Figure 2b is first cited in §3.6, after Figures 2a/2c (§3.3) and 2d (§3.4); journals require citation in numerical order.
【Evidence】Callout order in `manuscript_v1.1.5.md`: line 92 ("Figure 2a", "Figure 2c"), line 96 ("Figure 2d"), line 106 ("Figure 2b").
【Why it matters】Mechanical compliance point; also currently confusing because the CCI panel (2b) is the last figure discussed.
【Specific fix】Renumber the panels so citation order is sequential: current 2c (E1 genes) → Figure 2b; current 2d (dissociation) → Figure 2c; current 2b (CCI) → Figure 2d. Update the three in-text callouts and the in-image titles accordingly; the captions drafted in B5-18 already use this numbering.

### B5-24. Table 1: caption/column mismatch, missing denominators, and unit mismatch with §3.1

【Problem】The Table 1 title defines detection as "CPM > 1 in 100% of samples unless noted" while the columns report detection as a fraction; the table gives no per-experiment n; and the table reports SCN9A/TRPV1 in CPM while §3.1 quotes the same genes in log2CPM.
【Evidence】`manuscript_v1.1.5.md:71` (title) and lines 73-84 (columns "DirectInf mean CPM / DirectInf detected fraction / SeraExo mean CPM / SeraExo detected fraction"; e.g., PIEZO1 SeraExo fraction 0.89 — verified against raw counts: 17/19 samples with CPM > 1). §3.1 (line 69) quotes SCN9A/TRPV1 in log2CPM. All Table 1 values verified against `layer1_results.json` key `w0` (PIEZO2 245.2/164.1; P2RX3 806.8/470.6; ITGB1 323.6/360.3; SCN10A 7.23/0.55 with fractions 1.00/0.11; TRPV1 122.3/95.6; TAC1 65.7/68.9; TRPV4 0.25/0.19; STOML3 0.01/0.00; SCN9A 318.3/261.7; PIEZO1 2.64/2.20) — identical.
【Why it matters】The detection baseline is the paper's data-examination gate and the foundation of the "resolution-limited M1" argument; its presentation should be unambiguous about what "detected" means and over how many samples.
【Specific fix】Replace the Table 1 title with: "Table 1. Detection baseline of mechanotransduction-relevant genes (mean CPM per experiment; detected fraction = fraction of samples with CPM > 1; DirectInf n = 12, SeraExo n = 19)." Optionally add a "mean log2CPM" pair of columns so the table and §3.1 share one set of numbers.

### B5-25. Figure 1's results box uses the phrase "correctly-powered NULL"

【Problem】"Primary endpoint M3: correctly-powered NULL (exact permutation P = 0.42; MDE 0.18 log2CPM)" — a null result is not "correctly-powered"; the study had 80% power for effects ≥ 0.18 log2CPM.
【Evidence】Figure 1, lower results box; MDE 0.1786 verified in `layer1_module_scores.csv` (column `mde_80pct`).
【Why it matters】"Correctly-powered null" is a category error that a statistically literate referee will pounce on; the intended meaning (a null with a stated detectable-effect bound) is already well expressed elsewhere in the manuscript as "bounded null".
【Specific fix】Change to "Primary endpoint M3: correctly bounded NULL (exact permutation P = 0.42; 80% power for effects >= 0.18 log2CPM)".

---

## 5. Limitations completeness against an anesthesiology/pain readership

§4.4 already covers, and covers well: the immortalized embryonic single-clone model (i); the 36-h window (ii); bulk RNA-seq's blindness to composition and post-translational regulation (iii); PHN donor age/sex confounding (iv); missing/below-detection panel genes (v); the borderline direct-infection M1 effect and unsupported reciprocal dissociation (vi); hypothesis-generating status throughout (vii); unverified exosome identity/co-isolated factors (viii); cross-experiment baseline differences (ix); the unreplicated substance-P observation (x); E1-N1 non-separability (xi); unmanipulated substrate stiffness (xii); and unquantified exosome dose (xiii). I verified each against the deposited artifacts and found them accurate. Four items a JPR referee would still raise are missing:

### B5-26. Missing: the module score is an unweighted mean, and its robustness to the scoring function is untested

【Problem】All module-level inference rests on an unweighted mean of log2(1+CPM) across panel genes; no alternative scoring (gene-weighted, rank-based, or first principal component) was tested, and this is not stated as a limitation.
【Evidence】`manuscript_v1.1.5.md:55` (§2.3): "module scores computed as the mean log2(1 + CPM) across panel genes present in the matrix". The only scoring sensitivity reported anywhere is the detection-floor subset analysis (§3.4/§3.6) and the median-of-ratios normalization check (§2.3, `layer1_norm_robustness.json`). §4.4 (lines 130-134) does not mention scoring-function choice.
【Why it matters】The primary endpoint is a null whose interpretation ("inert within a bounded null") depends on the score definition; a methods referee will ask whether a PC1- or rank-based score moves M3. The gene-level results are reported alongside precisely to hedge this, but the limitation should say so.
【Specific fix】Add to §4.4: "(xiv) Module scores are unweighted means of log2(1+CPM) across panel genes; alternative scorings (rank-based, gene-weighted, or first principal component) were not tested, so the module-level P values are conditional on this scoring choice — one reason the gene-level results are reported alongside every module-level claim."

### B5-27. Missing: no protein or functional validation of the channel signal

【Problem】The paper's central clinical hook is a change in "the electrogenic nociceptor program", but no protein, localization, or electrophysiological measurement exists; §4.4(iii) covers bulk RNA-seq's blindness to post-translational regulation only implicitly.
【Evidence】`manuscript_v1.1.5.md:118`: "we cannot test this balance without protein-level or electrophysiological data" (raised in Discussion) — but §4.4's item (iii) says only "Bulk RNA-sequencing reports neither cell-composition changes nor post-translational mechanotransduction", without stating that no protein or functional assay was performed.
【Why it matters】For a pain-clinician readership, mRNA down-regulation of TRPV1/Nav1.7 says nothing directly about channel function or excitability; stating this once, plainly, in Limitations pre-empts the standard referee demand.
【Specific fix】Add to §4.4: "(xv) All findings are transcriptional: no protein abundance, membrane localization, or electrophysiological measurement was performed, so channel function — the quantity relevant to allodynia — is not directly assessed."

### B5-28. Missing: whether the exosome replicates are independent donors or technical replicates is not stated and cannot be determined from public metadata

【Problem】The analysis treats n = 7 (control), n = 7 (HZ), n = 5 (PHN) as independent units, but the public GEO metadata (which §3.5 notes "report only cell line and treatment") do not establish whether the replicates are independent donor sera.
【Evidence】`manuscript_v1.1.5.md:43` (group sizes), line 100/102 ("Donor-level age and sex are not present in the deposited GEO metadata for these samples (which report only cell line and treatment)"). The series matrix sample titles read "HD10 treated with control sera EV replicate 1-7" etc., without donor identifiers. §4.4 does not list replicate independence as a constraint.
【Why it matters】If any replicates are technical (same donor serum, split), the effective n — and therefore the MDE 0.18 bound on which the primary null rests — is smaller than stated. This is the first question a careful statistician-referee asks about a 7-vs-7 design.
【Specific fix】Add to §4.4: "(xvi) Whether the exosome-treated replicates represent independent donor sera or include technical replicates cannot be determined from the public metadata; the effective sample size, and hence the minimum detectable effect, is conditional on their independence."

### B5-29. Reference errors: two citations resolve to the wrong bibliographic details

【Problem】Two references carry incorrect volume/issue/year details although their PMIDs and DOIs are correct.
【Evidence】(1) `manuscript_v1.1.5.md:190` ref [9]: "Trials. 2020;21:573" — Crossref (10.1186/s13063-020-04564-z) and PubMed (PMID 32641142) both give Trials 2020;21(1):630, article number 630, not 573. (2) `manuscript_v1.1.5.md:202` ref [15]: "Sci Transl Med. 2019;11(486):eaat9897" — Crossref (10.1126/scitranslmed.aat9897) and PubMed (PMID 30305457) both give Sci Transl Med 2018;10(462):eaat9897. The remaining 18 references (PMIDs 39211798, 37304287, 42734212, 41091131, 10377351, 32636736, 36226089, 32195953, 37303680, 35844093, 17167479, 24717433, 21816040, 38984717, 27653382, 17920770, 34825887, and the Benjamini-Hochberg JRSSB 1995 citation) were each checked against PubMed/Crossref and are correct in authors, title, journal, year, volume, and pages.
【Why it matters】Citation errors in a manuscript whose selling point is reproducibility are disproportionately damaging; both are trivially fixable.
【Specific fix】[9] → "Chen L, Zhou R, Sun F, Weng Y, Ye L, Yang P. Efficacy and safety of extracorporeal shockwave therapy in patients with postherpetic neuralgia: study protocol of a randomized controlled trial. Trials. 2020;21(1):630. doi:10.1186/s13063-020-04564-z. PMID: 32641142." [15] → "Murthy SE, Loud MC, Daou I, et al. The mechanosensitive ion channel Piezo2 mediates sensitivity to mechanical pain in mice. Sci Transl Med. 2018;10(462):eaat9897. doi:10.1126/scitranslmed.aat9897. PMID: 30305457."

### B5-30. Data availability cites a package tag one version behind the manuscript

【Problem】The reproducibility package is cited at tag v1.1.4 while the manuscript is v1.1.5.
【Evidence】`manuscript_v1.1.5.md:146`: "...(tag v1.1.4). The package regenerates every number in this manuscript from the raw GEO files."
【Why it matters】If v1.1.5 changed any number or figure, the cited tag cannot regenerate them; if it did not, the mismatch still invites the question.
【Specific fix】Either update the tag to the v1.1.5 release (and confirm the figures, including the corrected Figure 2b annotation from B5-19, are regenerated) or state explicitly that the v1.1.4 package regenerates every number in this version unchanged.

---

## Stands up (things I suspected but found correct — do not change these)

1. **Every headline number I recomputed from the raw counts matches the manuscript exactly.** From `GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz` (43,236 genes x 19 samples): E1 HZ-exo vs control-exo = −0.2196 (Welch P = 0.0111; exact permutation P = 0.0128 of 3,432 partitions); M3 = −0.0489 (P = 0.4199 / 0.4219); M1 = −0.0780 (P = 0.1209 / 0.1131); N1 = −0.1558 (P = 0.1563); per-sample E1−N1 = −0.0638 (P = 0.1867); TRPV1 = −0.5673 (P = 0.00092). Welch 95% CIs reproduce the manuscript's quoted intervals (E1 −0.38 to −0.06; M3 −0.18 to +0.08). Sample assignment from column prefixes was verified against the series metadata (control 7 / PHN 5 / acute zoster 7; mock 6 / VZV 6; 31 samples; 4 dpi; 36 h).
2. **The cross-section hedging discipline is genuinely strong.** I specifically hunted for stronger survivors of weakened claims: "hypothesis-generating" (5 occurrences), "bounded null / MDE 0.18" (4 occurrences), "E1−N1 = −0.064, P = 0.18" (3 occurrences), "resolution-limited M1 / P = 0.046" (5 occurrences), and "post hoc interaction P = 0.0017 vs detected-gene P = 0.16" (4 occurrences) all carry identical qualifiers everywhere they appear. The only violations are B5-1 (abstract), B5-2 (Figure 2d caption), and B5-3 (§4.4(vi)).
3. **Clinical bounding of model findings survives everywhere except the title and abstract.** §4.4's overarching caution ("No finding here describes chronic PHN biology in living patients"), §3.5's "no clinical inference about PHN as a disease of patients is drawn from it", and the Abstract's "hypothesis-generating, not evidence of mechanism in patients" are all present, consistent, and correctly placed.
4. **The ESWT literature is characterized accurately.** Ref 7 (Chen 2022) indeed reports pain reduction with no significant time-by-group interaction in the mixed model — the manuscript's "largest randomized trial" superlative is defensible (Yeon 2025: n = 19; Lee 2020: pilot), and the PHN definition (dermatomal pain ≥90 days) matches the cited standard.
5. **Table 1 and the §3.1 detection narrative are numerically exact** (see B5-24 evidence), including the "four of nine M1 genes at or below the detection floor" (TRPV4 0.19, STOML3 0.00, KCNK2 0.66, TRPA1 0.02 CPM) and "E1 contains 5/18" (SCN10A 0.55, TRPM8 0.52, KCNQ3 0.78, GRIN2B 0.29, GRIA1 0.08 CPM) claims, and the detected-gene M1 subset (5 genes, −0.171, P = 0.046).
6. **The neutral-control architecture is real, not decorative.** N2's floor-limited signal is disclosed with its single-gene driver (OR5A1, 0.89 CPM, 32% detection), N3 is correctly reinterpreted as an exposure control, the KCNQ2/KCNQ3 E1-N1 gene overlap is disclosed with family-specific q values (0.366/0.500 and 0.497/0.564 — verified), and the median-of-ratios robustness check (E1 −0.194/P = 0.015; M3 −0.024/P = 0.64; ribosomal share 3.23%→4.22%) is correctly reported in §2.3.
7. **No British spellings or hyphenation drift in the body text** — the only instances in the package are the two flagged in B5-11 and B5-12.

## Questions for the authors

1. Why are the within-M2 Benjamini-Hochberg survivors EZR (q = 0.017) and PXN (q = 0.019) absent from the Results, given that within-module q values are reported for E1 genes and §2.4 presents them as a general product?
2. What selection rule produced the eight genes in Figure 2c (it appears to be the eight largest |log2FC|), and can the two statistically null genes be visually marked?
3. Which confidence interval is quoted in the Abstract and §3.3 for E1 (−0.38 to −0.06) — Welch or permutation inversion? The permutation-inversion interval for the same contrast is −0.395 to −0.044 (`layer1_module_scores.csv`); please label the interval type wherever a CI is given.
4. PTK2 (FAK) is a member of both M3 and M4 (`analysis/config/mtp_panel.json`). Was this overlap intended, and does the positive dependence it induces between two of the eight modules affect the Benjamini-Hochberg family?
5. What are the exact permutation P values behind the three "ns" bars in Figure 2b (the text reports P ≥ 0.82)?
6. Should the Data availability tag be updated to v1.1.5 (B5-30), and does the cited package contain the corrected Figure 2b annotation?
7. For the clinical next step (B5-9): what comparator population, endpoint definition, time grid, and assay-reproducibility data are envisaged before a serial-measurement study could be powered?

## What I actually checked

- **Read in full:** `manuscript/manuscript_v1.1.5.md` (all 214 lines; long single-line paragraphs expanded); the compiled `manuscript_v1.1.5.docx` (figure images, caption paragraphs, embedded media); Table 1; Data availability; Ethics; Author contributions; all 21 references.
- **Figures viewed and audited:** fig1_design.png, fig2a_module_scores.png, fig2b_cci.png (annotation magnified), fig2c_E1_genes.png (title magnified), fig2d_dissociation.png — each against its in-text description and the deposited data.
- **Recomputed from raw counts** (`analysis/data/raw/GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz`, CPM then log2(1+CPM), module = mean over present panel genes, Welch t and exact permutation over all C(14,7) = 3,432 partitions): E1, M3, M1, N1, E1−N1, TRPV1, detection fractions, and module-gene detection counts. All identical to the manuscript and to `layer1_module_scores.csv` / `layer1_gene_level.csv`.
- **Trusted deposited artifacts (named):** `layer1_results.json` (keys `w0`, `baseline`, `interaction`, `interaction_detected_only`, `sensitivity_detected_genes`, `e1_vs_n1_benchmark`, `neuropeptide_observation`, `gene_level_bh`, `panel_missing`, `alias_check`); `layer1_extra_checks.json` (neuronal-integrity markers, TRPV1 by route, detection-baseline extras); `layer1_norm_robustness.json`; `layer1_diag.json`; `layer1_cci.csv`; `layer1_global_de.csv`; `analysis/config/mtp_panel.json` (module membership; identified the undisclosed M3∩M4 PTK2 overlap).
- **References checked** against PubMed (esummary) and Crossref for all PMIDs/DOIs: 19 of 21 correct; errors at ref [9] (article number) and ref [15] (year/volume/issue). GSE314229 confirmed to exist (rat tibial osteotomy sEV study).
- **Clinical claims sanity-checked externally:** PHN ≥90-day definition; Chen 2022 ESWT RCT (no time-by-group interaction confirmed); Yeon 2025 ESWT trial size (n = 19) for the "largest trial" superlative.
- **Discrepancies found (all reported above):** abstract route claim (B5-1); Figure 2d caption (B5-2); §4.4(vi) vs (xi) (B5-3); §3.2 M4 wording (B5-4); unreported EZR/PXN (B5-5); title (B5-7); "cardinal symptom" (B5-8); clinical proposal (B5-9); rat species omission (B5-10); "programme" (B5-11); down-regulated/downregulated (B5-12); CCI sentence (B5-14); "Round-4" reference (B5-16); missing captions (B5-18); Figure 2b annotation +82.422 vs 82.7222 (B5-19); Figure 2c content/clipping (B5-20); Figure 2a key (B5-21); Figure 2d missing marker (B5-22); citation order (B5-23); Table 1 title (B5-24); Figure 1 wording (B5-25); limitations gaps (B5-26 to B5-28); ref errors (B5-29); tag mismatch (B5-30). All other checked values were identical to the manuscript.

## Must-fix list (ordered by severity)

1. **B5-1** — Abstract route claim ("but not direct VZV infection down-regulated the electrogenic nociceptor program") contradicts §3.4's magnitude-not-direction finding; paste-ready replacement given.
2. **B5-18** — No figure captions exist in the manuscript .md at all; five paste-ready captions drafted (fixes the journal requirement and subsumes B5-11).
3. **B5-2** — Figure 2d caption states the un-caveated interaction claim (P = 0.0017) with no post hoc designation and no detected-gene P = 0.16; paste-ready replacement given.
4. **B5-5** — Within-M2 BH survivors EZR (q = 0.017) and PXN (q = 0.019) are unreported; add the drafted §3.3 sentence and bound the Figure 2c title claim to E1.
5. **B5-3** — §4.4(vi) "robust E1-selective exosome effect" contradicts §4.4(xi); paste-ready replacement given.
6. **B5-7** — Title asserts "human sensory neurons" and "route-dependent effects" beyond what the data support; paste-ready replacement given.
7. **B5-19** — Figure 2b annotation "+82.422" mismatches the deposited 82.7222; regenerate the figure.
8. **B5-29** — Two reference errors: ref [9] Trials article number (573 → 630) and ref [15] Murthy year/volume/issue (2019;11(486) → 2018;10(462)).
9. **B5-4** — §3.2 M4 "suppressed (P = 0.03)" lacks its BH q = 0.20; paste-ready replacement given.
10. **B5-9** — Clinical next-step proposal is under-specified (no comparator, endpoint, time grid, confounders, assay feasibility); paste-ready replacement given.
11. **B5-8** — "Mechanical allodynia is a cardinal symptom of PHN" overstates; paste-ready replacement given.
12. **B5-20 / B5-21 / B5-22** — Figure 2c (unmarked null genes, clipped title), Figure 2a (undefined asterisk key, no n), Figure 2d (unannotated significant bar): regenerate with the drafted annotations.
13. **B5-26 / B5-27 / B5-28** — Add the three missing limitations (scoring-function sensitivity; no protein/functional validation; replicate independence unknown from public metadata).
14. **B5-16** — Remove the "Round-4 internal benchmarks" reference from §4.4.
15. **B5-14 / B5-13 / B5-12 / B5-15 / B5-11** — Language items: unreadable CCI sentence, triple-negative §4.1 sentence, down-regulated/downregulated inconsistency, §3.1 mixed units/denominators, "programme".
16. **B5-23 / B5-24 / B5-25 / B5-30 / B5-10 / B5-6 / B5-17** — Remaining presentation items: figure renumbering, Table 1 title, Figure 1 wording, package tag, rat-species attribution, abstract M1 qualifier, smaller register items.

**Verdict: Major revision.** The science is carefully bounded and the numbers I recomputed are exact, but the abstract, one figure caption, and §4.4(vi) still carry versions of claims the manuscript elsewhere weakens, the figures need regeneration, two references are wrong, and the captions are missing from the submission source — all fixable without new analysis.
