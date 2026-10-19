# A4 — Venue & reporting-standards review
**Target venue:** Journal of Pain Research (Dove Medical Press), article type "Original Research" (research article / bioinformatics reanalysis)
**Reviewed:** `manuscript/manuscript_v1.0.0.md` (157 lines), `manuscript/cover_letter_JPR.md` (33 lines)
**Guideline baseline:** Dove Medical Press Author Guidelines, current live pages (journal home; *Author Guidelines* index; *Manuscript structure*; *Manuscript preparation*; *Reference stylesheet*; *Clinical trials*), retrieved 2026-10-19. JPR-specific points cross-checked against the journal page (ISSN 1178-7090; Editor-in-Chief M. Schatman). Where the two conflict I follow the live Dove pages.

## 0. What JPR/Dove actually requires (extracted baseline)

| Requirement | Dove/JPR rule (as published) |
|---|---|
| Abstract | Structured abstract **required** for original research; **≤ 300 words** |
| Plain Language Summary | **Optional** (≤ 250 words, after Abstract, before Introduction) — not a compliance item here |
| Keywords | **3–6 keywords** |
| References | AMA/Vancouver: sequential **superscript Arabic numerals**, no parentheses, placed after punctuation; reference list **numerical in order of citation**; journal names abbreviated per PubMed; ≤ 6 authors listed, else first 3 + "et al." |
| Ethics | "All research studies on humans (individuals, samples or **data**) or animals must include a statement on ethics approval… A statement confirming the name of the IRB… must be included within the manuscript. The relevant reference/permit numbers should also be included." |
| Other mandatory declaration sections | Consent for publication; Data availability; Funding; Competing interests; **Authors' contributions**; Acknowledgments |
| Tables/figures | "Ensure tables and figures are cited"; each submitted as a separate file |
| Trial registration | Only for clinical trials (WHO/ICMJE-approved registries); registration number must appear in the manuscript. **Not applicable** to a public-data reanalysis — see §V6 for the separate "pre-registered" claim problem |
| Data sharing statement | Required only for manuscripts reporting clinical trial data — not applicable |
| Protocol deposit | protocols.io deposit **encouraged**, with DOI, linked in Methods |
| Title page | Author names, affiliations (dept, institution, city, state, country), **ORCID whenever available**, corresponding author name/physical address/phone/email |
| Language/format | Microsoft Word; double-spaced; 3-cm margins; page numbers; **line numbers**; **American spelling**; native-speaker editing expected; word counts not fixed (shorter items ~1000–3000 words) |

---

## V1. 【Problem】The abstract is 422 words, exceeding Dove's hard 300-word limit for structured abstracts.

【Evidence】`manuscript/manuscript_v1.0.0.md:13–25` (whole Abstract section). Word count computed from the file: 422 words (whitespace split of the section between `## Abstract` and `## 1. Introduction`, markdown markers stripped). The current "Registration." paragraph (line 23, ~24 words) and the duplicated coverage of the direct-infection pattern in both Results and Conclusions are the main overflow.

【Why it matters】Dove states structured abstracts "should be no more than 300 words." Editorial screening checks this mechanically; an over-length abstract is a standard reason for editorial return before review, and it delays the manuscript by a full round-trip.

【Specific fix】Replace lines 15–23 with the following paste-ready 284-word structured abstract (verified count; keep the four standard headings, move the registration sentence into Methods of the main text):

> **Background.** Mechanical allodynia defines postherpetic neuralgia (PHN), yet the mechanotransduction dimension has never been systematically examined in its genomic literature. GSE342782 — bulk RNA-sequencing of differentiated human sensory neurons exposed to direct varicella-zoster virus (VZV) infection or to serum exosomes from healthy controls, acute herpes zoster (HZ), and PHN patients — allows mechano-transcriptional hypotheses to be tested in a human neuronal model.
>
> **Methods.** We prospectively specified a frozen four-module mechanotransduction panel (M1 mechanogated channels; M2 membrane–cytoskeleton coupling; M3 ECM–integrin–Hippo; M4 mechano-effectors), an electrochemical nociceptor module (E1), and three neutral control modules (N1–N3) before any data were examined. The single primary endpoint was the M3 module-score difference between acute-HZ-serum exosomes and control exosomes. Hypothesis tests used Welch's *t* statistics, Mann–Whitney *U*, and label-permutation nulls (B = 5,000), with Benjamini–Hochberg correction across the eight modules.
>
> **Results.** PIEZO2 was robustly expressed (mean CPM ≈ 245; detected in 100% of samples) whereas TRPV4 and STOML3 were below detection, making M1 PIEZO2-driven. The primary endpoint was a null (−0.049 log2CPM; permutation P = 0.416; q = 0.46), as was M3 under every contrast. The pre-specified secondary endpoint E1 was suppressed (−0.220; P = 0.011; q = 0.030) via concordant down-regulation of TRPV1, SCN9A, SCN10A and ASIC1/2, with PIEZO2 spared (P = 0.18). Direct VZV infection showed the mirror pattern (M1 −0.050; P = 0.051; E1 P = 0.996). The exploratory PHN-exosome contrast was non-specific (neutral module N1 also shifted, P = 0.035) and confounded (donors older, almost all female).
>
> **Conclusion.** In human sensory neurons, the route of VZV perturbation determines which ion-channel programme is suppressed: exosomes dampen electrochemical nociception while sparing mechanical gating — a transcriptomic substrate compatible with mechanical allodynia that redirects the mechanical axis in PHN towards non-neuronal compartments.

(Every number in this replacement is taken unchanged from the manuscript's own Results text and matches the results JSON — see §Stands up. Note "prospectively specified" replaces "pre-registered" per §V6; if the authors obtain a genuine registry entry, "pre-registered" may be restored.)

## V2. 【Problem】Four mandatory Dove declaration sections are missing entirely from the manuscript: Ethics approval and informed consent, Consent for publication, Authors' contributions, and Acknowledgments.

【Evidence】The manuscript ends at line 124 with "Data availability" (113–116), "Declaration of interests" (118–120) and "Funding" (122–124) only; there is no ethics/consent statement anywhere in the file (no occurrence of "ethic", "consent", or "IRB" in the 157 lines). Dove: "All research studies on humans (individuals, samples or data)… must include a statement on ethics approval and, when human research is involved, consent… the name of the IRB… must be included within the manuscript."

【Why it matters】These are checklist items at submission; a missing ethics statement for a study built on human donor data (GSE342782 derives from patient serum exosomes) is a standard desk-return. The absence also leaves the cover letter's ethics sentence (cover_letter_JPR.md:18) unsupported inside the manuscript itself.

【Specific fix】Insert after the Funding section (after line 124), paste-ready:

> ## Ethics approval and informed consent
>
> This study is a secondary analysis of publicly available, de-identified data (GEO accession GSE342782) generated from an established iPSC-derived human sensory-neuron model. No new human participants, human samples, or animals were involved, and this analysis was therefore exempt from institutional ethics review; no new ethics approval or informed consent was required. The original study, which generated the data, obtained all required institutional ethics approvals and informed consent from donors, as described in the original publication [4].
>
> ## Consent for publication
>
> Not applicable.
>
> ## Authors' contributions
>
> The author confirms sole responsibility for the following: study conception and design, data analysis and interpretation of results, and manuscript preparation.
>
> ## Acknowledgments
>
> None.

Do **not** invent an IRB name or approval number for the reanalysis — the truthful exempt-secondary-analysis framing above is what Dove accepts for public-data reanalyses, and it matches the cover letter.

## V3. 【Problem】The keyword list contains 7 entries; Dove allows 3–6.

【Evidence】`manuscript/manuscript_v1.0.0.md:25`: "postherpetic neuralgia; mechanical allodynia; mechanotransduction; PIEZO2; varicella-zoster virus; extracellular vesicles; GSE342782" — 7 keywords. Dove guideline: "3–6 keywords."

【Why it matters】A trivial but mechanically checked item; also "GSE342782" is a dataset accession, not a concept, and indexing it as a keyword adds noise.

【Specific fix】Replace line 25 with:

> **Keywords:** postherpetic neuralgia; mechanical allodynia; mechanotransduction; PIEZO2; varicella-zoster virus; extracellular vesicles

(6 keywords; the GEO accession is already given in the title, Abstract, and Data availability.)

## V4. 【Problem】References [2] and [6] are placeholders — descriptive prose with no actual citation — and are load-bearing in the Introduction.

【Evidence】`manuscript/manuscript_v1.0.0.md:130`: "[2] PHN Mendelian-randomization analyses based on FinnGen postherpetic-neuralgia endpoints (endpoint drift 144→313→490→554 cases across releases R5–R13; FinnGen R13 manifest verified 2026-10-19)." — no authors, journal, year, or identifier. `manuscript/manuscript_v1.0.0.md:138`: "[6] Clinical guideline literature on mechanical allodynia as the defining symptom of PHN." — likewise no citation. Both are cited in text: [2] within "[1–3]" at line 31, [6] within "[5,6]" at line 33.

【Why it matters】Dove: "authors are responsible for the accuracy and completeness of their references." Un-cited-in-fact references will be caught at editorial screening and are a documented desk-return trigger. Worse, the claim they support is currently mis-catalogued: [3] (line 132) is a *rat* DRG microarray and [2] is a Mendelian-randomization study — neither is a "bioinformatic reanalysis of PHN cohorts," the phrase they are cited to support at line 31.

【Specific fix】Either supply complete AMA-style citations for the FinnGen MR analysis and for one clinical guideline defining mechanical allodynia as the cardinal PHN symptom (e.g., a PHN guideline with volume/pages/DOI), or delete both. If deleted, renumber and rewrite line 31 as:

> Published bioinformatic reanalyses of PHN cohorts have concentrated on interferon, immune and inflammatory programmes [1], and none has systematically interrogated the mechanotransduction machinery — mechanogated ion channels, the membrane–cytoskeleton interface, or the extracellular-matrix (ECM)–integrin–Hippo axis.

(Also move [3] and [9] — GEO dataset accessions — out of the numbered reference list into the Data availability section, or reformat them per AMA electronic-material style: "NCBI Gene Expression Omnibus. GSE64345 [data set]. Available from: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE64nnn/GSE64345/. Accessed October 19, 2026.")

## V5. 【Problem】The trailing "Reference verification note" is an internal author-side artefact that must not be in a submission.

【Evidence】`manuscript/manuscript_v1.0.0.md:156` (block quote beginning "**Reference verification note.** Items [1], [5], [7], [8] were verified on 2026-10-19…"). This is internal QA metadata, including an admission that two references "still require formal citations."

【Why it matters】If it reaches the handling editor it signals an unfinished submission and invites a desk-reject; it also discloses, in the author's own words, that the reference list is incomplete.

【Specific fix】Delete line 156 in its entirety. Note for the authors: the note reveals that [4] — the primary data source, cited for every result — was **not** in the verified set. I verified it independently (see §Stands up): Niemeyer CS, Frietze S, Lewis SWR, et al. "Circulating Exosomes Drive Persistent Neuronal Dysfunction in Post-Herpetic Neuralgia Patients." *Ann Neurol*. 2026. doi:10.1002/ana.78352. PMID: 42734212. The reference is real, but its list entry is incomplete (see V8).

## V6. 【Problem】The word "pre-registered" is used in the title, abstract, Section 2.2, Section 5, and the cover letter, but no registration on any recognized registry exists, and the only public time-stamps are dated the day the data were downloaded and the manuscript assembled.

【Evidence】
- A repository-wide search for registry identifiers (OSF, ClinicalTrials.gov, PROSPERO, AsPredicted, registry, registration) returns **no registration number, DOI, or registry URL** anywhere; the only artefacts are the self-assigned strings "protocol v0.4" (`manuscript/manuscript_v1.0.0.md:23,45`) and "panel tag `mtp-frozen-2026-10-19`" (lines 1, 23, 45, 116).
- `mtp-frozen-2026-10-19` is **not a git tag**: it is the `panel_version` string inside `analysis/config/mtp_panel.json` (key `panel_version`). The repository has exactly one tag, `v1.0.0`.
- The public GitHub repository shows tag `v1.0.0` dated **Oct 19, 2026** — the submission day. Local git history contains only two commits, both dated 2026-10-19 ("Initial deposit").
- Local file timestamps: the GEO files were downloaded 2026-10-19 09:20–09:38 (`GSE342782_Processed_DirectInf…csv.gz` 09:22; `…SeraExo…csv.gz` 09:24); the "frozen" panel JSON was written **09:22:16** — i.e., interleaved with the data download, not demonstrably before any data examination.

【Why it matters】In the biomedical literature, "pre-registered" is a term of art: an entry in a recognized registry (OSF Registries, ClinicalTrials.gov, AsPredicted, PROSPERO…) bearing an external, tamper-evident time-stamp that **precedes** data examination. A self-archived protocol plus a git tag created on submission day does not establish temporal precedence; a skeptical reviewer can and will test the claim, and "pre-registered" in the **title** is the most exposed position. If the precedence cannot be evidenced, the correct word is "prospectively specified in a time-stamped, publicly archived protocol" — which is still a genuine methodological strength. (Dove itself only *requires* registration for clinical trials; this is a credibility issue, not a Dove rule violation.)

【Specific fix】Two honest options — pick one:
1. **Reword (recommended if no pre-examination registry entry exists).** Replace "pre-registered" with "prospectively specified" in the title (line 1), abstract Methods (line 17), Section 2.2 heading (line 43) and first sentence (line 45), Introduction (line 35), Conclusions (line 109), and cover letter (lines 4, 10, 12, 16). Title replacement:
   > Route-dependent transcriptional effects of varicella-zoster virus and patient serum exosomes on ion-channel programmes in human sensory neurons: a prospectively specified reanalysis of GSE342782
   And replace abstract line 23's "Registration." paragraph by folding into Methods: "The analysis plan, frozen panel and endpoint hierarchy were specified in writing before data examination and are publicly archived (protocol v0.4; panel tag mtp-frozen-2026-10-19)."
2. **Register now and cite it.** Deposit the frozen panel + endpoint hierarchy on OSF Registries or protocols.io (Dove explicitly encourages protocols.io deposits with a DOI) and cite the DOI in the abstract — but only claim "pre-registered" if the registration time-stamp genuinely precedes data examination; otherwise the registration documents the plan, not its precedence, and option 1's wording still applies.

## V7. 【Problem】Section 3.1 cites "(Table 1)" but no Table 1 exists in the manuscript, and none of the five figures in the reproducibility package is cited anywhere in the text.

【Evidence】`manuscript/manuscript_v1.0.0.md:67` contains the only table/figure callout in the file: "…established the expression baseline of the model (Table 1)." There is no Table 1 (or any table) in the manuscript, and the string "Figure" never occurs in the manuscript text. The reproducibility package contains five figures with captions (`fig1_design.png`, `fig2a_module_scores.png`, `fig2b_cci.png`, `fig2c_E1_genes.png`, `fig2d_dissociation.png`; captions are defined in `manuscript/build_docx.py`). Dove: "Ensure tables and figures are cited"; each figure/table must also be submitted as a separate file.

【Why it matters】A callout to a non-existent table is a hard formatting fail at editorial screening, and five uncited figures cannot be included — the manuscript currently has no display items at all, which for a data-heavy reanalysis weakens it and contradicts the Data availability claim that "all figures" are included (line 116).

【Specific fix】Either delete the parenthetical "(Table 1)" at line 67, or add Table 1 with the values already computed (from `analysis/results/layer1/layer1_results.json`, `w0` block), e.g.:

> **Table 1. Expression baseline of panel genes in the HD10 sensory-neuron model (mean CPM and detection fraction, CPM > 1, by experiment).**
>
> | Gene | DirectInf mean CPM | DirectInf detected | SeraExo mean CPM | SeraExo detected |
> |---|---|---|---|---|
> | PIEZO2 | 245.2 | 6/6 | 164.1 | 19/19 |
> | ITGB1 | 323.6 | 6/6 | 360.3 | 19/19 |
> | SCN9A | 318.3 | 6/6 | 261.7 | 19/19 |
> | TRPV1 | 122.3 | 6/6 | 95.6 | 19/19 |
> | PIEZO1 | 2.64 | 6/6 | 2.20 | 17/19 |
> | TRPV4 | 0.25 | 0/6 | 0.19 | 0/19 |
> | STOML3 | 0.008 | 0/6 | 0.000 | 0/19 |
> | LOX | 0.41 | 0/6 | 0.40 | 1/19 |
> | MMP9 | 0.11 | 0/6 | 0.001 | 0/19 |

(Values verified against `layer1_results.json` lines 15–97.) Additionally, add in-text callouts, e.g.: in §2.1 or §3.1 — "The study design and pre-registered analysis pipeline are summarized in Figure 1."; in §3.2 — "Module-score differences for the primary contrast are shown in Figure 2a."; in §3.6 — "…the channel-complementarity index (Figure 2b) and the gene-level shifts within E1 (Figure 2c)."; in §3.4 — "The route × module dissociation is shown in Figure 2d." Submit each figure as a separate high-resolution file per Dove's figures-and-tables specification.

## V8. 【Problem】In-text citations use bracketed numbers, Dove/AMA requires superscript Arabic numerals, and references [9]–[12] are listed but never cited in the text.

【Evidence】The manuscript cites as "[1–3]" (line 31), "[4]" (line 33), "[5,6]" (line 33), "[7,8]" (line 33), "[5–8,13,14]" (line 101). A full-text search shows "[9]", "[10]", "[11]", "[12]" occur **only** in the reference list (lines 144, 146, 148, 150) and nowhere in the body. Dove stylesheet: "Cite references sequentially in text, tables, and legends by superscript Arabic numerals with no parentheses, eg, 1 or 3,4 or 10–15. Numbers should be placed after punctuation marks."

【Why it matters】Reference style is one of the two most common editorial-return reasons (per Dove's own guidance to authors); uncited list items break the "numbered in order of citation" rule and will be queried.

【Specific fix】Convert all in-text citations to superscript numerals after punctuation (e.g., "…inflammatory programmes.1–3"). For the uncited items: [10] DESeq2, [11] RSEM and [12] Benjamini–Hochberg should either be cited where the methods are described (e.g., after "Processed RSEM gene-level counts" at line 41 for [11]; after "Benjamini–Hochberg false-discovery-rate correction" at line 57 for [12]; [10] DESeq2 is arguably unnecessary since DESeq2 was not used — delete it) or removed. After deleting placeholders per V4 and renumbering, re-check that the list is strictly sequential in order of first citation. Also complete [4] per AMA: "Niemeyer CS, Frietze S, Lewis SWR, et al. Circulating exosomes drive persistent neuronal dysfunction in post-herpetic neuralgia patients. Ann Neurol. 2026. doi:10.1002/ana.78352" (14 authors → first three + et al.).

## V9. 【Problem】Section 3.2 states M4 was unchanged "in every contrast (all P ≥ 0.11)", which is contradicted by the manuscript's own Section 3.4 and by the results file.

【Evidence】`manuscript/manuscript_v1.0.0.md:71`: "…and for M4 mechano-effectors in every contrast (all P ≥ 0.11)." But `manuscript/manuscript_v1.0.0.md:79` reports "M4 mechano-effectors were suppressed (-0.054; P = 0.024)" under direct VZV infection, and `analysis/results/layer1/layer1_results.json` (VZV_vs_Mock → M4: `diff −0.0544`, `p_perm 0.0242`) confirms it. The HZ-exosome (P = 0.46) and PHN-exosome (P = 0.108) contrasts are indeed null; only the direct-infection contrast is not.

【Why it matters】A self-contradiction inside the Results section is exactly what reviewers pounce on; it also slightly misstates the "inert stiffness programme" narrative by sweeping a real M4 effect under direct infection into a false "every contrast" claim.

【Specific fix】Replace the clause at line 71 with:

> The null was not contrast-specific: M3 was likewise unchanged under direct VZV infection (+0.012; P = 0.85) and under PHN exosomes (−0.017; P = 0.84). M4 mechano-effectors were unchanged under both exosome contrasts (all P ≥ 0.11) but were suppressed under direct VZV infection (−0.054; P = 0.024), as reported below.

## V10. 【Problem】Section 2.3 claims "all other modules were fully represented" in the count matrix; two control modules were not.

【Evidence】`manuscript/manuscript_v1.0.0.md:53`: "…(M3 used 56 of 58 genes: CYR61 and CTGF were absent from the count matrix; all other modules were fully represented)." But `analysis/results/layer1/layer1_results.json`, `panel_missing` block, lists N2 missing OR6A1, OR10A1, OR13C1 (13 of 16 used) and N3 missing RPS4 (17 of 18 used).

【Why it matters】The neutral controls are the calibration backbone of the paper; an inaccurate statement about their composition undermines the very reporting discipline the paper advertises (§3.6), and a reviewer diffing the panel against the matrix will find it.

【Specific fix】Replace the parenthetical at line 53 with:

> (M3 used 56 of 58 genes: CYR61 and CTGF were absent from the count matrix; N2 used 13 of 16 (OR6A1, OR10A1, OR13C1 absent); N3 used 17 of 18 (RPS4 absent); all other modules were fully represented.)

## V11. 【Problem】The traceability claim in §2.5 is inaccurate: gene-level P values and the PHN genome-wide counts are not in any deposited results file.

【Evidence】`manuscript/manuscript_v1.0.0.md:61`: "All numerical values quoted in this manuscript are traceable to `layer1_results.json` in the reproducibility package." However, `layer1_results.json` contains only module-level statistics plus per-gene **differences** (no gene-level P values); `analysis/results/layer1/MANIFEST.json` covers only three result files; the PHN genome-wide counts at line 83 ("568 genes up- and 125 down-regulated at |log2FC| > 0.5") appear in no deposited file (`layer1_diag.json` records only the HZ counts, 129/174). I recomputed the gene-level Welch P values from the raw GEO counts and they are correct (see §Stands up) — but they are not *deposited*, so the sentence as written is false.

【Why it matters】A false traceability sentence is a reproducibility red flag that a data-availability-minded reviewer or editor will test in one click; it is cheap to fix and expensive to be caught on.

【Specific fix】Deposit a gene-level results CSV (columns: contrast, gene, log2FC, Welch P) and a global-DE CSV (contrast, n_up, n_down, threshold) into the reproducibility package, extend `MANIFEST.json` to cover them, and rewrite line 61 as:

> Every result file carries a SHA-256 manifest linking it to the exact input files and the frozen panel. All numerical values quoted in this manuscript are reproducible from the deposited raw GEO counts, the frozen panel, and the deposited result files (module-level: `layer1_results.json`; gene-level: `layer1_gene_level.csv`; genome-wide counts: `layer1_global_de.csv`).

## V12. 【Problem】The cover letter contains an internal note disclosing that it was drafted for retargeting to other journals.

【Evidence】`manuscript/cover_letter_JPR.md:33`: "*Note: this letter is drafted for Journal of Pain Research and can be retargeted to BMC Anesthesiology (or another SCIE candidate) by changing the salutation and the scope paragraph; the scientific content is journal-agnostic.*"

【Why it matters】If this reaches the handling editor it advertises parallel/serial journal shopping — a serious credibility hit at a journal that is a COPE member, and entirely avoidable.

【Specific fix】Delete line 33. (Also fine to keep: the letter correctly states originality and non-duplicate submission at line 20.)

## V13. 【Problem】The cover letter overstates the certainty of the direct-infection dissociation and the "correctly-powered" null relative to the manuscript.

【Evidence】`manuscript/cover_letter_JPR.md:14`: "…whereas direct viral infection shows the complementary pattern" — stated flatly. The manuscript itself is more careful: `manuscript/manuscript_v1.0.0.md:79` reports M1 −0.050 with **permutation P = 0.051** and adds "this dissociation should be read as hypothesis-generating." Separately, cover_letter_JPR.md:16 says "We report a correctly-powered null at the primary endpoint," but no power calculation appears anywhere in the manuscript; §3.2 (line 71) only asserts adequacy ("with seven versus seven samples and a 56-gene module, the study was adequately powered at the gene-set level") without a computation.

【Why it matters】Cover letters are read first; an editor who spots an unqualified claim the manuscript itself qualifies will discount the letter's reliability, and "correctly-powered" with n = 7 vs 7 invites a methodological challenge the manuscript has not pre-empted.

【Specific fix】In the cover letter, replace "…whereas direct viral infection shows the complementary pattern;" with:

> …whereas direct viral infection showed the complementary, hypothesis-generating pattern (M1 −0.050, permutation P = 0.051; E1 unchanged, P = 0.996);

and replace "We report a correctly-powered null at the primary endpoint" with:

> We report a null at the primary endpoint whose observed difference sits well inside its permutation null,

(or, better, add an actual power calculation — α, target effect, achieved power at n = 7 vs 7 — to the supplement and keep the original wording; see §Questions.)

## V14. 【Problem】British spellings throughout, against Dove's explicit American-spelling requirement.

【Evidence】Examples: "programmes" (title line 1; running title line 9; lines 19, 21, 31, 35, 69, 71, 99, 101, 109), "emphasise" (line 71), "hypothesised" (line 67), "re-analysed" (line 132), "characterised/recognised"-family forms where present. Dove: "American spelling (all components of a manuscript must be in English)" and manuscripts are expected to be "reviewed and edited by a native speaker of English" before submission.

【Why it matters】House style is checked at screening; a global spelling pass is a one-hour fix but a guaranteed query if skipped.

【Specific fix】Global copy-edit to American spelling: programme→program, emphasise→emphasize, hypothesised→hypothesized, re-analysed→reanalyzed, etc. (title, running title, abstract, body, figure captions, cover letter).

## V15. 【Problem】Title-page and submission-format items incomplete: no phone number for the corresponding author; markdown backticks and working-file artifacts in the text; submission mechanics (Word, double-spacing, line numbers) not yet met.

【Evidence】Dove title page requires "name, physical address, phone, fax, email" for the corresponding author; `manuscript/manuscript_v1.0.0.md:7` gives email and ORCID only (no phone). Backticks appear in the manuscript text at lines 23, 45, 61, 116 (`mtp-frozen-2026-10-19`, `layer1_results.json`). The file is Markdown; Dove requires Microsoft Word, double-spaced, 3-cm margins, page numbers and line numbers. A docx builder exists (`manuscript/build_docx.py`) but its output must be checked for these mechanics.

【Why it matters】Minor individually, but each is a checklist tick at upload; missing line numbers/page setup is a common reason editorial staff return files before sending to review.

【Specific fix】Add a phone number to line 7; strip all backticks and markdown syntax from the submission text; produce the submission as .docx with double spacing, 3-cm margins, page numbers, and line numbers (the build script should be verified against Dove's manuscript template).

## V16. 【Problem】Data availability statement is substantively correct but not in Dove's declarative house format.

【Evidence】`manuscript/manuscript_v1.0.0.md:113–116` lists the GEO FTP URL, the GitHub repository with tag v1.0.0, and the SHA-256 MANIFEST. Dove asks for "a statement about where data supporting the results reported in the manuscript can be found and about data sharing including, where applicable, links to the publicly archived datasets… which additional unpublished data, if any, are available, to whom, and how."

【Why it matters】Low-risk item, but reformatting removes a query and aligns with the journal's Declarations layout.

【Specific fix】Replace lines 113–116 with:

> ## Data availability
>
> The data that support the findings of this study are openly available in the NCBI Gene Expression Omnibus under accession GSE342782 (https://ftp.ncbi.nlm.nih.gov/geo/series/GSE342nnn/GSE342782/). The complete reproducibility package — analysis scripts, frozen panel (tag `mtp-frozen-2026-10-19`), all result files with a SHA-256 manifest, and all figures — is available at https://github.com/yyx-4113/mechano-phn-gse342782-reanalysis (release v1.0.0) and regenerates every number in this manuscript from the raw GEO files. There are no additional unpublished data from this study.

(Remove backticks in the Word version.)

---

## Stands up

1. **Every number I recomputed from the raw data matches the manuscript exactly.** I re-derived, from `analysis/data/raw/GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz` (43236 genes × 19 samples; group prefixes give 7 C / 7 S / 5 P, matching manuscript line 41), the HZ-vs-control Welch tests on log2(1+CPM): COL4A1 −0.381/P = 0.0052 (ms line 71: −0.381, P = 0.005); COL4A2 −0.627/P = 0.0073 (−0.627, 0.007); ADAMTS1 −0.479/P = 0.0130 (−0.479, 0.013); TEAD1 −0.339/P = 0.0469 (−0.339, 0.047); LOX +0.291/P = 0.0240 (+0.291, 0.024); YAP1 +0.425/P = 0.1834 (+0.425, 0.18); TRPV1 −0.567/P = 0.0009 (line 75: −0.567, 0.0009); KCNS1 −0.393/P = 0.0174 (−0.393, 0.017); SCN10A −0.384/P = 0.0076 (−0.384, 0.008); SCN9A −0.323/P = 0.0182 (−0.323, 0.018); ASIC1 −0.181/P = 0.0193 (−0.181, 0.019); ASIC2 −0.296/P = 0.0422 (−0.296, 0.042); PIEZO2 −0.282/P = 0.1816 (−0.282, 0.18). My independent M3 module score (56 genes present, per the frozen panel) reproduces `layer1_results.json` to 15 significant digits (diff −0.04887804878732682; Welch P 0.41992303587515784 vs deposited 0.41992303587515856). All module-level diffs, permutation P values and BH q values quoted in the manuscript match the deposited JSON (e.g., M3 −0.049/0.416/q 0.46; E1 −0.220/0.011/q 0.030; N2 −0.022/0.006/q 0.022; N3 +0.391/0.0006; PHN M1 −0.119/0.008/q 0.021, E1 −0.197/0.004/q 0.016, N1 −0.198/0.035, N3 +0.577/0.0002; VZV M1 −0.050/0.051, Welch 0.047, E1 +0.0005/0.996; CCI all permutation P ≥ 0.82; per-sample mean log2CPM range 1.553–1.605 → quoted 1.55–1.61; HZ global DE 129/174). Detection-baseline values (PIEZO2 245.2 CPM, ITGB1 323.6, SCN9A log2CPM 8.31, TRPV1 6.94, TRPV4 0.25, STOML3 0.01, LOX 0.41, MMP9 0.11) all match. The raw file byte sizes quoted at line 41 (622,501 and 884,411) are exactly right on disk, and B = 5,000 / seed 20261019 are the actual defaults in `analysis/scripts/layer1_mechano.py:71`.
2. **The primary data citation [4] is real and correctly characterized.** Niemeyer CS, Frietze S, Lewis SWR, et al., *Ann Neurol* 2026, doi:10.1002/ana.78352 (PMID 42734212): "Circulating Exosomes Drive Persistent Neuronal Dysfunction in Post-Herpetic Neuralgia Patients." The original study's design (direct VZV infection vs control/acute-HZ/PHN serum exosomes on human nociceptive neurons, 36-h exposure), its reported findings (down-regulation of canonical nociceptive ion channels, substance-P up-regulation, ECM-remodeling signals), and its stated PHN-donor confounds (older, almost exclusively male→female skew: "patients with PHN were older… the PHN group also contained only one male subject") match the manuscript's descriptions at lines 33, 49, 83, 101 and 105.
3. **The cover letter's ethics framing is correct for a public-data reanalysis.** cover_letter_JPR.md:18 ("No new human-subject research, patient recruitment, or animal work was conducted; no additional ethics approval or informed consent was required beyond that of the original data deposition") is the right substantive position for de-identified public GEO data; the defect is only that this statement is missing from the manuscript itself (V2).
4. **Abstract–body numerical consistency holds.** Every Results claim in the abstract (line 19) matches the body text and the results JSON: M3 −0.049/P = 0.416/q = 0.46; "nor under any other contrast (all P ≥ 0.42)" — the other two contrasts are 0.838 and 0.846, so this is true as written; E1 −0.220/P = 0.011/q = 0.030; PIEZO2 spared P = 0.18; VZV M1 −0.050/P = 0.051 and E1 P = 0.996; PHN N1 P = 0.035; "mean CPM ≈ 245, detected in 100% of samples."
5. **Reproducibility infrastructure exists and is internally consistent.** `MANIFEST.json` carries SHA-256 hashes for all three deposited result files and all three inputs (two count matrices + frozen panel); the GitHub repository and tag v1.0.0 are live; the gate script (`manuscript/gate_consistency.py`, 74 assertions) has a report dated 2026-10-19. The infrastructure is real — the problems are in the manuscript's claims *about* it (V6, V11), not in the infrastructure itself.

## Questions for the authors

1. What is the basis for "correctly-powered null" at the primary endpoint (n = 7 vs 7)? Please provide the power calculation (α, target effect size, achieved power) or adopt the rewording in V13.
2. Is there any external, time-stamped artefact (OSF registration, protocols.io DOI, dated email, preprint of the protocol) that predates the first examination of the GSE342782 expression data? If yes, cite it in the abstract; if no, adopt the "prospectively specified" wording.
3. Please complete or withdraw references [2] and [6], and confirm whether [3] and [9] (GEO datasets) should move to Data availability rather than the numbered list.
4. Where will the gene-level Welch P values and the PHN genome-wide counts (568/125) be deposited, so that the §2.5 traceability sentence becomes true?
5. Please confirm the original study's ethics approval details as reported in Niemeyer et al. (IRB name/number) so the ethics statement can cite them.
6. Will Table 1 and Figures 1–2d be submitted as separate files per Dove's figures-and-tables specification, and are the in-text callouts in V7 acceptable?
7. Please confirm the manuscript is not under consideration elsewhere (the cover letter note at line 33 must be deleted regardless).
8. Please supply a phone number for the corresponding author (Dove title-page requirement).

## What I actually checked

- **Read in full:** `manuscript/manuscript_v1.0.0.md`; `manuscript/cover_letter_JPR.md`; the live Dove Medical Press author-guidelines pages (journal home; Author Guidelines index; Manuscript structure; Manuscript preparation; Reference stylesheet; Clinical trials); `analysis/results/layer1/layer1_results.json`; `analysis/results/layer1/layer1_diag.json`; `analysis/results/layer1/MANIFEST.json`; `analysis/config/mtp_panel.json` (keys and version field only); figure captions in `manuscript/build_docx.py`.
- **Guideline facts used:** structured abstract required for original research, ≤300 words; 3–6 keywords; Plain Language Summary optional; AMA/Vancouver superscript sequential references; mandatory Declarations sections (ethics, consent for publication, data availability, funding, competing interests, authors' contributions, acknowledgments); "Ensure tables and figures are cited"; registration required only for clinical trials; protocols.io deposit encouraged; Word format, double-spaced, 3-cm margins, page + line numbers, American spelling.
- **Ran:** word counts of the abstract (422) and main text (2401, within Dove's general 1000–3000 range for shorter items); full-text searches for citation markers ([9]–[12] confirmed uncited in text), British spellings, and registry identifiers (OSF/ClinicalTrials.gov/PROSPERO/AsPredicted — none found); directory listings with timestamps of the raw data, panel, and results files; local `git log`/`git tag`; the public GitHub tags page for the reproducibility repository (tag v1.0.0, dated Oct 19, 2026).
- **Recomputed from raw data** (`GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz`, pipeline reproduced per `layer1_mechano.py`: CPM → log2(1+CPM) → module mean / per-gene Welch): 13 gene-level differences and P values and the M3 module difference and Welch P — all matched the manuscript and the deposited JSON exactly (values listed in §Stands up). Group sizes 7/7/5 verified from the matrix; raw file byte sizes verified on disk; B = 5,000 and seed 20261019 verified in the analysis script.
- **Discrepancies found (mine, not the manuscript's):** none in the recomputed values. **Discrepancies found in the manuscript (vs its own results files):** the "M4 all P ≥ 0.11" claim (V9; actual VZV P = 0.024); "all other modules fully represented" (V10; N2 13/16, N3 17/18); the traceability sentence (V11); the un-deposited PHN counts 568/125 (V11).
- **Not verified in this pass (belongs to other reviewers / out of venue scope):** the statistical validity of the permutation calibration and the "correctly-powered" assertion; the provenance of the 568/125 PHN counts (no deposited source found); PIEZO2/TRPV4 biological claims; the FinnGen endpoint-drift numbers inside placeholder [2].

---

## Must-fix list (in priority order)

1. **[DESK-REJECT]** Add the missing Declarations: Ethics approval and informed consent, Consent for publication, Authors' contributions, Acknowledgments (V2 — paste-ready text supplied).
2. **[DESK-REJECT]** Cut the abstract from 422 to ≤300 words (V1 — paste-ready 284-word replacement supplied).
3. **[DESK-REJECT]** Delete the "Reference verification note" (V5, manuscript line 156).
4. **[DESK-REJECT]** Resolve placeholder references [2] and [6]; remove or cite the uncited [9]–[12]; renumber; convert in-text citations to AMA superscript style (V4, V8).
5. **[DESK-REJECT]** Either add Table 1 or delete the "(Table 1)" callout at line 67; add in-text callouts for Figures 1 and 2a–2d and submit them as separate files (V7).
6. **[MAJOR]** Remove or substantiate "pre-registered" (title, abstract, §2.2, §5, cover letter); the registry evidence does not currently exist (V6).
7. **[MAJOR]** Fix the internal contradictions: §3.2 M4 "all P ≥ 0.11" (V9) and §2.3 "fully represented" (V10).
8. **[MAJOR]** Cover letter: delete the journal-shopping note (V12); qualify the direct-infection claim and the "correctly-powered" phrase (V13).
9. **[MINOR]** Keywords 7 → 6 (V3); American-spelling pass (V14); title/phone/Word-format mechanics (V15); Data availability reformat (V16).
10. **[MINOR]** Deposit gene-level and global-DE result files and correct the §2.5 traceability sentence (V11).

**Overall editorial verdict:** Return for editorial revision — do **not** send to review as submitted. The science is numerically sound: every value I could recompute from the raw GEO data matched the manuscript exactly, the primary data citation is real and correctly characterized, the ethics position is right in substance, and the topic fits JPR's scope (neuropathic-pain mechanisms) well. What stands between this manuscript and review is entirely presentation-layer: a 122-word abstract overage, four missing declaration sections, two placeholder references, an internal QA note, a missing table, uncited figures, wrong citation style, and an unverifiable "pre-registered" claim. All ten must-fix items are editorial fixes requiring no new experiments; items 1–5 should be cleared before the manuscript re-enters the pipeline, and item 6 should be resolved honestly (reword, or produce a registry entry) before any reviewer sees the word "pre-registered" in the title.
