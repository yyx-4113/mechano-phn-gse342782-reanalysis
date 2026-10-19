# Review B4 — Journal editor's desk + reporting-standard auditor

**Venue:** Journal of Pain Research (Dove Press), ISSN 1178-7090 — reviewed as Original Research, first submission
**Manuscript:** `manuscript/manuscript_v1.1.5.md` (+ compiled `manuscript_v1.1.5.docx`), `manuscript/cover_letter_JPR.md`
**Reviewer:** B4 (venue/editorial-desk compliance, citation integrity, cover-letter consistency)
**Date of review:** 20 October 2026

## Guidelines consulted (every rule invoked below is tied to a URL + access date)

| Rule invoked | Source (all accessed 20 Oct 2026) |
|---|---|
| Structured abstract required for Original Research; "Both types of abstracts should be no more than 300 words" | https://www.dovepress.com/author-guidelines/manuscript-structure (page states "Updated 15 April 2026") |
| "3–6 keywords" | same URL as above |
| Corresponding author: "Name, physical address, phone, fax, email"; "ORCID number(s) for all authors whenever available" | same URL as above |
| Required sections: Ethics approval and informed consent; Consent for publication; Data availability (where applicable); Funding; Competing interests; Authors' contributions; Acknowledgments; References | same URL as above |
| Citation style: "DMP follow the style adopted by the American Medical Association (AMA)… based on… Vancouver"; "Cite references sequentially in text, tables, and legends by superscript Arabic numerals with no parentheses… Numbers should be placed **after** punctuation marks"; "Reference list: List items **numerically**… in the order they are cited in the text"; "List **all** authors if six or less, otherwise list **first three only**, followed by 'et al.'"; journal names abbreviated per PubMed list | https://www.dovepress.com/author-guidelines/reference-stylesheet (page states "Updated 28 December 2022") |
| Retrospective/public-data ethics: "Where permission to use information from a database/repository is not required (e.g. where it is publicly available and unrestricted re-use is permitted via an open license), a statement to explain this must be included within the manuscript" | https://www.dovepress.com/editorial-policies/research-ethics |
| "Abstract 300 words; Plain language summary (optional); 3–6 keywords; Running header (shortened title); Corresponding author: name, physical address, phone, fax, email" (JPR-specific rendering of the same rules) | https://topj.lib.whu.edu.cn/show_tg.asp?iss=11787090 (mirror of the Dove Press JPR author-instructions page; cross-checked against the live Dove pages above) |
| "American spelling"; "Do not punctuate abbreviations eg, et al, ie"; "Spell out acronyms in the first instance in the abstract and paper"; "Ensure tables and figures are cited" | https://www.dovepress.com/author_guidelines.php?content_id=3503 (Research Manuscript Preparation) and the manuscript-structure page |

---

## 1. Abstract compliance

**1.1 Word count (my own count, three methods stated).** I extracted the block between `## Abstract` and `## 1. Introduction` (manuscript_v1.1.5.md:15–27) and counted:

- **Method A — token count** (regex `[A-Za-z0-9][A-Za-z0-9'-]*`, excluding the `**Keywords:**` line): **300 words**. Per section: Background 45, Methods 56, Results 127, Conclusions 51, Registration 16 (= 295) plus the five bold section labels "Background/Methods/Results/Conclusions/Registration" (5) = 300. This is identical to the count reported by the author's own compliance gate (`gate_jpr_compliance.py`, run output: "abstract <= 300 words (actual 300)").
- **Method B — whitespace split**, excluding the Keywords line: **298 words**.
- **Method C — whitespace split, including the Keywords line**: **310 words**.

Against the current Dove rule ("no more than 300 words", manuscript-structure page), the abstract is **compliant but with zero headroom**: it sits exactly at the limit under Method A and would exceed it under any counter that folds the keyword line or treats hyphenated compounds as two words (e.g., "route-dependent", "contrast-of-contrasts", "detected-gene" all appear in the abstract). A desk editor pasting the abstract into Word will read 298 and pass it; a stricter tokenizer will read 300 and pass it; but there is no margin, and any editorial trim requested in revision will push the author back to this boundary problem.

**【Problem】** The abstract is exactly at the 300-word limit under the strictest tokenization (300/300) and at 310 if the keyword line is counted, leaving no compliance headroom.
**【Evidence】** manuscript_v1.1.5.md:17–27; my Method A count = 300 (matches the author's gate output "actual 300"); Method B = 298; Method C = 310. JPR limit = 300 words (Dove manuscript-structure page, accessed 20 Oct 2026).
**【Why it matters】** A one-word addition during revision — or a production desk using a different counter — turns a passing abstract into a format-rejection item; the journal screens this before peer review.
**【Specific fix】** Trim ~20 words from the Results section (the longest, 127 words). Paste-ready replacement for the second sentence of Results (manuscript_v1.1.5.md:21), saving 8 words:
> "M3 did not shift under HZ-serum exosomes (difference -0.049 log2CPM; permutation P = 0.42; 95% CI -0.18 to +0.08; minimum detectable effect 0.18 log2CPM), a bounded null."
and for the fourth sentence of Results, saving 12 words:
> "A post hoc interaction (P = 0.0017) was non-significant among detected genes (P = 0.16), and the exploratory PHN-exosome contrast was non-specific and donor-confounded."
(Resulting Method A count ≈ 280.)

**1.2 Keywords.** Six keywords: postherpetic neuralgia; mechanical allodynia; mechanotransduction; PIEZO2; varicella-zoster virus; extracellular vesicles (manuscript_v1.1.5.md:27). This is within the Dove "3–6 keywords" rule (manuscript-structure page, accessed 20 Oct 2026). Compliant.

**1.3 Structured abstract.** Original Research requires a structured abstract; the manuscript uses Background/Methods/Results/Conclusions/Registration headings (manuscript_v1.1.5.md:17–25). Compliant. The "Registration" heading is non-standard for Dove but is an allowed heading set and its content is a disclosure, not a violation.

---

## 2. Required declaration sections (presence, non-emptiness, ordering)

All Dove-required sections are present, non-empty, and in the conventional post-Conclusions order:

| Section (Dove name) | Manuscript location | Content | Status |
|---|---|---|---|
| Ethics approval and consent to participate | manuscript_v1.1.5.md:148–150 | Secondary analysis of public de-identified GEO data; no new human/animal work; cites source deposition ^3^ | Present, non-empty; consistent with Dove's public-repository clause (editorial-policies/research-ethics, accessed 20 Oct 2026) |
| Consent for publication | manuscript_v1.1.5.md:152–154 | "Not applicable." | Present |
| Author contributions | manuscript_v1.1.5.md:156–158 | "YY conceived the study, performed the analysis, wrote the manuscript, and is solely responsible for its content." | Present |
| Acknowledgments | manuscript_v1.1.5.md:160–162 | "None." | Present |
| Declaration of interests | manuscript_v1.1.5.md:164–166 | "None declared." | Present (Dove's "Competing interests" declaration) |
| Funding | manuscript_v1.1.5.md:168–170 | "None." | Present |
| Data availability | manuscript_v1.1.5.md:142–146 | GEO FTP URL + GitHub package URL + SHA-256 MANIFEST statement | Present — but see §3.4 below (cited tag is stale) |
| References | manuscript_v1.1.5.md:172–214 | 21 numbered entries | Present — but see §3.2–3.3 |

Ordering (Abstract → body → Conclusions → Data availability → Ethics → Consent for publication → Author contributions → Acknowledgments → Declaration of interests → Funding → References) matches the Dove manuscript-structure page. No ordering defect.

---

## 3. Citation style, references, and URL integrity

**3.1 In-text citation format.** The `.md` uses `^N^` markers; the compiled `manuscript_v1.1.5.docx` contains **24 superscript runs** (`vertAlign w:val="superscript"` in `word/document.xml`), i.e., the submission file implements AMA/Vancouver superscript numerals, placed after punctuation (e.g., "allodynia.^1,20^" manuscript_v1.1.5.md:33). Compliant with "superscript Arabic numerals with no parentheses… placed after punctuation marks" (reference-stylesheet page, accessed 20 Oct 2026).

**3.2 Citation–reference completeness and numbering order (TWO DEFECTS).** I parsed every in-text marker and compared with the 21-entry list:

- **Uncited references: [16] (Li & Dewey, RSEM) and [17] (Benjamini & Hochberg) appear in the reference list but are never cited in text.** No `^16^` or `^17^` marker exists anywhere in the body.
- **Non-sequential numbering.** First-appearance order of citations in the text is [1, 20, 2, 3, 4, 7, 8, 9, 10, 11, 5, 6, 14, 18, 15, 19, 13, 12, 21] — e.g., reference 20 is cited second (manuscript_v1.1.5.md:33) and reference 14 is cited before references 5 and 6 (manuscript_v1.1.5.md:116). AMA/Vancouver requires numbering "in the order they are cited in the text" (reference-stylesheet page).

**【Problem】** References [16] and [17] are listed but never cited, and the reference list is not numbered in order of first citation, both violating the journal's AMA/Vancouver rule.
**【Evidence】** manuscript_v1.1.5.md:204 ([16]), 206 ([17]) have no in-text counterpart; first-appearance sequence [1,20,2,3,4,7,8,9,10,11,5,6,14,18,15,19,13,12,21] recomputed by me from the `^N^` markers; Dove rule quoted from https://www.dovepress.com/author-guidelines/reference-stylesheet (accessed 20 Oct 2026).
**【Why it matters】** Uncited list entries and out-of-order numbering are automatic desk-check failures at Dove (the reference desk verifies "all facts and references are correct" and AMA order); they also make the "every number traceable" reproducibility claim harder for a copyeditor to audit.
**【Specific fix】** Cite both method references at their natural first mention, then renumber the whole list by first appearance. Paste-ready insertions: in §2.1 after "Processed RSEM gene-level counts" (manuscript_v1.1.5.md:43) add "^16^"; in §2.4 after "Benjamini-Hochberg false-discovery-rate correction was applied" (manuscript_v1.1.5.md:59) add "^17^". After renumbering, the new order of first appearance is [1, 20, 2, 3, 4, 7, 8, 9, 10, 11, 5, 6, 14, 18, 15, 19, 13, 12, 21, 16, 17] and the list must be renumbered accordingly (Wang→1; Liang→2; Niemeyer→3; Yeon→4; Raymon→5; Haberberger→6; Chen 2022→7; Lee→8; Chen 2020→9; Ge→10; Pan→11; GSE314229→12; Cox→13; Woo→14; Murthy→15; Li & Dewey→16; Benjamini & Hochberg→17; Sánchez-Carranza→18; Chesler→19; Dworkin→20; Nguyen→21 happens to survive only if [16]/[17] are cited after [21]'s first appearance — verify against the final text).

**3.3 Reference accuracy (verified one by one against PubMed, 20 Oct 2026).** 18 of 21 references verify exactly. Four defects:

(a) **[15] Murthy et al. — wrong year, volume and issue.** Manuscript: "Sci Transl Med. 2019;11(486):eaat9897" (manuscript_v1.1.5.md:202). PubMed record for PMID 30305457 (accessed 20 Oct 2026): "Sci Transl Med. 2018 Oct 10;**10(462)**:eaat9897", DOI 10.1126/scitranslmed.aat9897. The paper was published 10 October 2018; "2019;11(486)" is wrong on all three fields. This reference supports a central mechanistic claim ("Piezo2 is required for mechanical pain in mice", cited in §4.1, manuscript_v1.1.5.md:116).

(b) **[21] Nguyen et al. — two wrong author names.** Manuscript: "Nguyen MQ, von Buchholtz LJ, Reker AN, **Rycroft KM, Ma J**" (manuscript_v1.1.5.md:214). PubMed record for PMID 34825887 (accessed 20 Oct 2026) lists "Nguyen MQ, von Buchholtz LJ, Reker AN, **Ryba NJP, Davidson S**". "Rycroft KM" and "Ma J" do not appear on this paper. This reference supports the adult-DRG baseline claim in §4.4 (manuscript_v1.1.5.md:132).

(c) **[9] Chen et al. — paraphrased title.** Manuscript: "Efficacy and safety of extracorporeal shockwave therapy for patients with postherpetic neuralgia: study protocol of a randomized controlled trial" (manuscript_v1.1.5.md:190). PubMed title (PMID 32641142, accessed 20 Oct 2026): "Efficacy and safety of **the** extracorporeal shockwave therapy **in** patients with postherpetic neuralgia: study protocol of a randomized controlled trial". Authors, journal, year, volume, DOI all verify; only the title is inexact.

(d) **[14] Woo et al. — title hyphenation.** Manuscript: "Piezo2 is required for Merkel cell mechanotransduction" (manuscript_v1.1.5.md:200); PubMed title is "Merkel**-**cell mechanotransduction" (PMID 24717433, accessed 20 Oct 2026). Trivial, but AMA copies the published title.

References verifying exactly (PMID/DOI resolves; authors, title, journal, year, volume/issue/pages match): [1] Wang 39211798; [2] Liang 37304287; [3] Niemeyer 42734212 (DOI 10.1002/ana.78352); [4] Yeon 41091131; [5] Raymon 10377351; [6] Haberberger 32636736; [7] Chen 36226089; [8] Lee 32195953; [10] Ge 37303680; [11] Pan 35844093; [13] Cox 17167479; [16] Li & Dewey 21816040; [18] Sánchez-Carranza 38984717; [19] Chesler 27653382; [20] Dworkin 17920770. Reference [17] (Benjamini & Hochberg, J R Stat Soc B 1995;57(1):289–300) has no PMID; the citation details are correct as printed. Reference [12] is a GEO record (GSE314229) rather than the underlying article — see Questions.

**【Problem】** Four reference entries contain factual errors (wrong year/volume/issue in [15]; two non-existent authors in [21]; inexact title in [9]; title hyphenation in [14]).
**【Evidence】** manuscript_v1.1.5.md:202, 214, 190, 200 vs PubMed records PMID 30305457, 34825887, 32641142, 24717433 (all accessed 20 Oct 2026), quoted above.
**【Why it matters】** The Terms of Publication warrant that "all facts and references are correct" (https://www.dovepress.com/author_guidelines.php?content_id=771, accessed 20 Oct 2026). A citation to a paper with two invented author names — supporting a stated limitation — is the single most credibility-damaging class of desk-check finding, and reference [15]'s wrong year/volume/issue propagates into any downstream citation of this article.
**【Specific fix】** Replace the four entries with the following paste-ready text:
> [15] Murthy SE, Loud MC, Daou I, et al. The mechanosensitive ion channel Piezo2 mediates sensitivity to mechanical pain in mice. Sci Transl Med. 2018;10(462):eaat9897. doi:10.1126/scitranslmed.aat9897. PMID: 30305457.
> [21] Nguyen MQ, von Buchholtz LJ, Reker AN, Ryba NJP, Davidson S. Single-nucleus transcriptomic analysis of human dorsal root ganglion neurons. Elife. 2021;10:e71752. doi:10.7554/eLife.71752. PMID: 34825887.
> [9] Chen L, Zhou R, Sun F, Weng Y, Ye L, Yang P. Efficacy and safety of the extracorporeal shockwave therapy in patients with postherpetic neuralgia: study protocol of a randomized controlled trial. Trials. 2020;21:573. doi:10.1186/s13063-020-04564-z. PMID: 32641142.
> [14] Woo SH, Ranade S, Weyer AD, et al. Piezo2 is required for Merkel-cell mechanotransduction. Nature. 2014;509(7502):622-626. doi:10.1038/nature13251. PMID: 24717433.

**3.4 Data availability URLs — resolution status and a version defect.**

- GEO FTP URL (https://ftp.ncbi.nlm.nih.gov/geo/series/GSE342nnn/GSE342782/): **HTTP 200**, directory listing live (matrix/, miniml/, soft/, suppl/). The suppl/ listing (HTTP 200) shows `GSE342782_Processed_DirectInf_neuronHD10s_BulkSeq_Counts.csv.gz` (608K) and `GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz` (864K) — consistent with the manuscript's stated byte counts (622,501 and 884,411 bytes; 622,501/1024 = 607.9K, 884,411/1024 = 863.9K) and with the local downloaded copies (identical sizes, verified).
- GitHub URL (https://github.com/yyx-4113/mechano-phn-gse342782-reanalysis): **HTTP 200**, public repository; releases exist for v1.0.0 through v1.1.6 (all dated 19 Oct 2026).

The defect: the manuscript's Data availability cites "**tag v1.1.4**" (manuscript_v1.1.5.md:146) while the submitted manuscript is version **v1.1.5**, and the repository contains a v1.1.5 release ("scientific content final") and even a v1.1.6 release. I inspected the file tree at tag v1.1.4 (20 Oct 2026): `analysis/results/layer1/` there contains MANIFEST.json, layer1_cci.csv, layer1_diag.json, layer1_extra_checks.json, layer1_gene_level.csv, layer1_global_de.csv, layer1_module_scores.csv, layer1_results.json — but **not** `layer1_norm_robustness.json`, the very file cited in §2.3 for the median-of-ratios robustness numbers (manuscript_v1.1.5.md:55, "E1 -0.194, permutation P = 0.015; M3 -0.024, P = 0.64"). That file appears only from tag v1.1.5 onward. The v1.1.4 release note also records a 119-assertion consistency gate versus 137/137 for the submitted manuscript.

**【Problem】** The Data availability statement points to tag v1.1.4, a superseded version that does not contain `layer1_norm_robustness.json` and predates the submitted v1.1.5 text, so the cited package cannot "regenerate every number in this manuscript".
**【Evidence】** manuscript_v1.1.5.md:146 ("(tag v1.1.4). The package regenerates every number in this manuscript") vs manuscript_v1.1.5.md:55 (cites `layer1_norm_robustness.json`); GitHub tree at v1.1.4 lacks that file (fetched 20 Oct 2026); v1.1.5 tree contains it; repository releases list shows v1.1.4 (15:56), v1.1.5 (16:30), v1.1.6 (16:32) on 19 Oct 2026.
**【Why it matters】** The data-availability policy requires a statement of "where data supporting the results reported in the manuscript can be found" with links to publicly archived datasets (manuscript-structure page, accessed 20 Oct 2026). A cited tag that cannot reproduce the submitted numbers converts the manuscript's strongest trust asset into a broken promise, and the version drift (v1.1.4 cited, v1.1.5 submitted, v1.1.6 existing) reads as careless version control to a handling editor.
**【Specific fix】** Replace the Data availability sentence (manuscript_v1.1.5.md:146) with:
> Reproducibility package (analysis scripts, frozen panel `mtp-frozen-2026-10-19`, result JSON/CSV with SHA-256 MANIFEST, all figures): https://github.com/yyx-4113/mechano-phn-gse342782-reanalysis (tag v1.1.5, the version of this manuscript). The package regenerates every number in this manuscript from the raw GEO files. SHA-256 checksums for all deposited artifacts are provided in `MANIFEST.json`.

---

## 4. Title page

All Dove-required corresponding-author elements are present (manuscript_v1.1.5.md:3–11 and the same block at the head of the .docx): name (Yongxin Yang), degree (B.M.), affiliation with department/institution/street/city/province/postcode/country, email (960856791@qq.com), ORCID (0009-0004-9698-6552), telephone (+86-591-8787-8130, labeled institutional switchboard), fax (explicitly "not available (institution publishes no fax line)"), and a running title ("Route-dependent channel programs in VZV-exposed sensory neurons", 11 words). The degree claim "B.M." is used consistently in the manuscript, cover letter and repository metadata; no inconsistent degree claim exists. The email is a personal (qq.com) address rather than an institutional one — permitted by Dove (only "email" is required) and consistent across all documents. No defect found.

---

## 5. Cover letter vs manuscript consistency (exclusive to this review)

I checked every factual claim in `cover_letter_JPR.md` against the manuscript. All 15 numeric/statistical claims match exactly: E1 P = 0.013 / q = 0.034; TRPV1 P = 0.0009, within-E1 q = 0.017; KCNS1/Nav1.7/ASIC1–2 q ≈ 0.07–0.13; PIEZO2 P = 0.18; MDE 0.18 log2CPM; CI -0.18 to +0.08; interaction P = 0.0017 → detected-gene P = 0.16; E1 - N1 = -0.064, P = 0.178; median-of-ratios E1 P = 0.015, M3 P = 0.64. The title matches the manuscript title character-for-character. The ethics statement, model identity ("tetracycline-regulatable v-myc immortalized embryonic dorsal root ganglion clonal line, not an iPSC-derived model and not DRG tissue"), the "no competing interests and no funding" declaration, and the originality/exclusivity statements all match the manuscript's own declarations. No template or journal-shopping residue is present ("Dear Editor", no other journal named, no reviewer-suggestion boilerplate beyond the neutral "Suggested reviewers can be provided on request").

**One mismatch found:**

**【Problem】** The cover letter redefines PHN by its symptom ("PHN is clinically defined by mechanical allodynia"), whereas the manuscript defines PHN by duration and characterizes mechanical allodynia as a symptom — a subtle over-claim in the letter's opening.
**【Evidence】** cover_letter_JPR.md:12: "Postherpetic neuralgia (PHN) is clinically defined by mechanical allodynia, yet the mechanotransduction machinery that underlies this cardinal symptom…" vs manuscript_v1.1.5.md:33: "Postherpetic neuralgia (PHN) is defined by dermatomal pain persisting at least 90 days after the acute herpes zoster rash, and is clinically characterized by mechanical allodynia — innocuous cutaneous stimuli transduced as pain." The manuscript's careful definition/characterization distinction (and its citation ^1,20^ to the definitional literature) is dropped in the letter.
**【Why it matters】** Editors read the letter first; a symptom-level definition of the disease overstates the clinical anchor of the paper and sits awkwardly next to the manuscript's own, more precise framing — exactly the kind of letter/manuscript dissonance that invites a scope query before review.
**【Specific fix】** Replace the first sentence of cover_letter_JPR.md:12 with:
> Postherpetic neuralgia (PHN) — dermatomal pain persisting at least 90 days after the acute herpes zoster rash — is clinically characterized by mechanical allodynia, yet the mechanotransduction machinery that underlies this cardinal symptom has never been systematically examined in the genomic literature of the disease.

**Registration wording.** The cover letter says "the analysis plan was specified prospectively before any data were examined" (cover_letter_JPR.md:16); the manuscript's Registration block says "Protocol v0.4 and frozen panel `mtp-frozen-2026-10-19` were deposited before data examination; no external registry entry" (manuscript_v1.1.5.md:25). These are consistent and appropriately hedged. The residual issue is the *linked artifact's* branding — see §6.2.

---

## 6. Reporting-standard honesty

**6.1 STROBE / reporting-guideline statement.** This is a secondary analysis of public observational expression data. In substance, the manuscript reports the STROBE-relevant items for a reanalysis: data source with accession and BioProject (manuscript_v1.1.5.md:43), sample sizes per group (7/7/5, verified by me from the count-matrix column prefixes and the series metadata), detection thresholds, statistical methods with software versions (manuscript_v1.1.5.md:59, 63), effect sizes with CIs, multiplicity handling, and a limitations section that names what cannot be reported (donor age/sex absent from GEO metadata, manuscript_v1.1.5.md:102 — I confirmed from the series matrix that `Sample_characteristics_ch1` carries only cell line/cell type/treatment). What is missing is an explicit reporting-guideline statement. Dove does not mandate one, but for a reanalysis the desk should not have to infer compliance.

**【Problem】** No reporting guideline is invoked for a study type (secondary analysis of existing data) that has an applicable standard (STROBE), and the items that cannot be reported from public metadata are not framed as such.
**【Evidence】** No occurrence of "STROBE", "reporting guideline", or equivalent anywhere in manuscript_v1.1.5.md (verified by text search); Dove manuscript-structure page lists no such mandate, so this is a credibility, not a compliance, gap.
**【Why it matters】** Naming the standard converts the limitations list into an auditable checklist and pre-empts the standard reviewer question ("why no reporting guideline?") for a data-reuse paper.
**【Specific fix】** Add one sentence at the end of §2.1 (manuscript_v1.1.5.md:43):
> Because this is a secondary analysis of publicly deposited data, reporting follows the items of STROBE applicable to analyses of existing datasets; items that depend on information absent from the public metadata (donor age, sex, and collection dates) are explicitly identified as unreportable.

**6.2 Pre-specification claims and the linked artifact's branding.** The manuscript's wording is honest: "deposited before data examination; no external registry entry" (manuscript_v1.1.5.md:25). Two problems remain. First, the claim is unverifiable from outside: the entire repository history (including the "Initial deposit" commit and the protocol file) is dated 19 October 2026, while the GSE342782 series has been public since 3 September 2026 (FTP directory timestamps), so the "before data examination" claim rests entirely on author attestation — an editor cannot time-stamp it. Second, the repository that the Data availability statement links to publicly brands itself as a "**pre-registered** reanalysis" in its title, description, README heading, and initial commit message ("Pre-registered reanalysis of GSE342782…", "pre-registered protocol (v0.4)"), which conflicts with the manuscript's explicit "no external registry entry" and reads as registry-level over-claiming to any editor who clicks the link. The README is also stale relative to the submission (it describes "manuscript v1.0.0", a "74 assertions" gate, and states that bibliographic identifiers for references [1,5,7,8] "must be inserted from verified sources at submission" — all long superseded).

**【Problem】** The prospectively-specified claim cannot be time-stamp-verified, and the linked repository publicly uses the stronger term "pre-registered", contradicting the manuscript's "no external registry entry" disclosure.
**【Evidence】** manuscript_v1.1.5.md:25 vs https://github.com/yyx-4113/mechano-phn-gse342782-reanalysis (title, About, README, and initial commit dd77226, all fetched 20 Oct 2026); all repository commits dated 19 Oct 2026; GSE342782 public since 3 Sep 2026 (ftp.ncbi.nlm.nih.gov directory timestamps).
**【Why it matters】** "Pre-registered" implies an external, time-stamped registry entry; using it for a same-day GitHub deposit is precisely the over-claim that editorial offices and post-publication commentators screen for, and it undercuts the credibility of the genuinely careful disclosure the manuscript itself makes.
**【Specific fix】** (i) Change the repository title, About description, and README first line from "Pre-registered reanalysis of GSE342782" to "Prospectively specified reanalysis of GSE342782 (protocol and panel deposited before data examination; no external registry entry)". (ii) In the Registration block (manuscript_v1.1.5.md:25), replace with the paste-ready sentence:
> Protocol v0.4 and frozen panel `mtp-frozen-2026-10-19` were committed to the public repository before any expression data were examined (initial deposit time-stamp available from the repository commit history); no external registry entry exists.
(iii) Update the repository README to describe the current manuscript version and gate, removing the stale "manuscript v1.0.0 / 74 assertions / identifiers to be inserted" caveats.

**6.3 Internal QA artifacts in the submission text.** One residue found: §4.4 opens "Three further constraints follow from the **Round-4 internal benchmarks**" (manuscript_v1.1.5.md:134). "Round-4" is an internal revision-cycle label meaningless to any reader; the sentence also breaks the limitations numbering flow (items (i)–(x) then (xi)–(xiii) under a new "constraints" umbrella that a reader cannot decode). No other placeholder/QA text exists (I searched for TODO/XXX/FIXME/[insert]/version strings; the only hits are the legitimate "data-examination gate" of §3.1 and the panel/version tags).

**【Problem】** An internal revision-cycle label ("Round-4 internal benchmarks") is left in the Limitations text of the submission.
**【Evidence】** manuscript_v1.1.5.md:134: "Three further constraints follow from the Round-4 internal benchmarks. (xi) The E1 signal is not separable from the neutral N1 control…"
**【Why it matters】** Any editor reading this sentence will ask what "Round-4" refers to; unexplained internal process language in a submitted manuscript signals weak final proofing and, in this case, hints at a revision history the journal has no visibility into.
**【Specific fix】** Replace the sentence with:
> Three further constraints were identified during analysis. (xi) The E1 signal is not separable from the neutral N1 control at the module level: …

**6.4 Post hoc disclosures.** The post hoc nature of the interaction test and the neuronal-integrity panel is disclosed in the results text itself (manuscript_v1.1.5.md:96, 110) and the PHN contrast is labeled exploratory wherever it appears. This is the correct, editor-acceptable pattern and should not be changed.

---

## § Stands up (verified correct — do not change)

1. **Every headline number reproduces from the raw counts.** I independently recomputed from `analysis/data/raw/` (own loader, own permutation code, CPM = counts/column-sum×10⁶, log2(1+CPM) scoring, panel from `analysis/config/mtp_panel.json`): PIEZO2 DirectInf mean CPM 245.2 and SeraExo 164.1; P2RX3 806.8 / 470.6; M3 HZ-vs-control diff -0.049 with exact permutation P = 0.4219; E1 -0.220 with P = 0.0128; N2 -0.022 with P = 0.0058; M1 -0.078 with P = 0.1131; TRPV1 log2FC -0.567 Welch P = 0.0009; PIEZO2 -0.282 P = 0.1816; SCN9A -0.323 P = 0.0182; KCNS1 -0.393 P = 0.0174; ATF3 +0.0002 P = 0.998; TAC1 +0.218 P = 0.377. All identical to the manuscript's printed values at the printed precision. Group sizes 7/7/5 confirmed from column prefixes and series metadata.
2. **Both compliance gates run clean on this machine.** `gate_jpr_compliance.py`: 30/30 PASS (abstract 300/300, keywords 6, numbering contiguous, American spelling, figure/table callouts, contact block, all mandatory sections, running title, no placeholders). `gate_consistency.py`: 137/137 PASS including its independent raw-count recompute of the primary-endpoint permutation P. No discrepancy between gate output and manuscript values.
3. **Data availability URLs resolve.** GEO FTP series and suppl directories HTTP 200 with file sizes matching the manuscript's stated byte counts exactly; GitHub repository HTTP 200 and public, with releases covering the cited tag.
4. **Required declaration sections are complete, non-empty, and correctly ordered**, and the ethics statement matches Dove's own clause for unrestricted public-data reuse (editorial-policies/research-ethics) — it states the exemption basis rather than leaving the section empty.
5. **Title page is complete** (name, degree, affiliation, full postal address, email, ORCID, phone, fax note, running title) and the "B.M." degree is consistent across manuscript, cover letter, and repository.
6. **Citation mechanics are correct**: superscript numerals after punctuation in the compiled .docx (24 superscript runs), en-dash ranges, PubMed journal abbreviations, "et al." after three authors for lists >6, and DOIs/PMIDs on nearly every entry.
7. **The compiled .docx is complete and faithful to the .md**: all sections, all 21 references, and the same (erroneous) reference text — so every fix listed here applies identically to both files.
8. **Cover letter discipline**: title matches the manuscript exactly, every number matches the manuscript, ethics/funding/interests statements match, and there is no template or journal-shopping residue — one wording fix only (§5).

---

## § Questions for the authors

1. Which tag should the Data availability statement cite for the submitted version — v1.1.5, or v1.1.6 ("cover letter aligned with v1.1.5 science")? Please make the cited tag identical to the submitted manuscript version.
2. Can you provide the time-stamp evidence for "deposited before data examination" (initial commit SHA and UTC timestamp, and the date expression data were first examined)? The repository history is entirely dated 19 Oct 2026, while the series has been public since 3 Sep 2026.
3. Will you remove "pre-registered" from the repository title/description/README, given the manuscript's "no external registry entry" statement?
4. Reference [12] cites the GEO record GSE314229; the underlying article (Xie X et al., Adv Sci (Weinh). 2026;13(16):e17257; PMID 41504389) is the peer-reviewed source of the ATP/P2X7R/p38MAPK claim. Would you prefer to cite the article (optionally alongside the accession)?
5. A plain language summary is optional per the journal — do you intend to add one (≤250 words)?
6. For §3.4's post hoc interaction: do you agree the current wording ("initially suggested… reported as exploratory/post hoc") is the framing you want in print, or would you prefer the stronger "post hoc and hypothesis-generating only"?

---

## § What I actually checked

**Files read in full:** `manuscript/manuscript_v1.1.5.md` (214 lines, all truncated single-line paragraphs re-read via `sed`/`fold`), `manuscript/cover_letter_JPR.md`, `manuscript/manuscript_v1.1.5.docx` (unzipped `word/document.xml`: 24 superscript runs; title-page block; all sections and 21 references present, matching the .md including its errors), `manuscript/gate_jpr_compliance.py`, `manuscript/gate_consistency.py`.

**Commands run:** `gate_jpr_compliance.py` → 30/30 PASS (exit 0). `gate_consistency.py` → 137/137 PASS (exit 0). Own abstract word counts (Methods A/B/C above: 300/298/310; per-section 45/56/127/51/16). Own citation-parse: cited set {1–15,18–21}, list {1–21}, uncited [16],[17], first-appearance order non-sequential. Own recompute from raw counts of 12 values (all identical; see Stands up 1). Local raw file sizes: 622,501 / 884,411 / 3,563 bytes (manuscript states the first two exactly).

**URLs fetched (all 20 Oct 2026):** Dove manuscript-structure page; Dove reference-stylesheet page; Dove research-ethics policy; Dove manuscript-preparation page; Dove author-guidelines index; JPR journal page; JPR instructions mirror (topj.lib.whu.edu.cn). GitHub repository root, /tags, /releases, /commits, /tree/v1.1.4/analysis/results/layer1, /tree/v1.1.5/analysis/results/layer1. GEO FTP series directory and /suppl/. PubMed records for PMIDs 39211798, 37304287, 42734212, 41091131, 10377351, 32636736, 36226089, 32195953, 32641142, 37303680, 35844093, 17167479, 24717433, 30305457, 21816040, 38984717, 27653382, 17920770, 34825887. GEO accession viewer for GSE314229.

**Gate-vs-my-own-check discrepancies:** none on numbers (137/137 gate assertions and my 12 independent recomputes agree with the manuscript). The compliance gate's own output, however, encodes the two problems I flag independently: it reports the abstract at exactly 300/300 (no headroom) and it does not check citation order, citation completeness, or reference accuracy — the four reference errors and the [16]/[17] issue pass its net.

---

## Must-fix list (ordered by severity; items 1–6 required before the manuscript goes to external review)

1. **Reference [21] contains two authors who are not on the paper** ("Rycroft KM, Ma J"; actual: Ryba NJP, Davidson S) — manuscript_v1.1.5.md:214. Use the paste-ready replacement in §3.3(b). *(Reference accuracy; journal warrants "all facts and references are correct".)*
2. **Reference [15] has the wrong year, volume and issue** (manuscript "2019;11(486)"; actual 2018;10(462)) — manuscript_v1.1.5.md:202. Paste-ready replacement in §3.3(a).
3. **Data availability cites a superseded tag (v1.1.4) that lacks `layer1_norm_robustness.json`** and cannot regenerate the numbers in the submitted v1.1.5 manuscript — manuscript_v1.1.5.md:146. Paste-ready replacement in §3.4.
4. **"Round-4 internal benchmarks" internal-process label left in the Limitations** — manuscript_v1.1.5.md:134. Paste-ready replacement in §6.3.
5. **References [16] and [17] are never cited, and the list is not numbered in order of first citation** (first appearance runs [1,20,2,3,4,7,8,9,10,11,5,6,14,18,15,19,13,12,21]) — cite ^16^ in §2.1 and ^17^ in §2.4, then renumber per §3.2.
6. **Repository publicly brands the work "pre-registered" while the manuscript states "no external registry entry"** — rename repository title/About/README and adopt the paste-ready Registration sentence in §6.2.
7. **Reference [9] title inexact** ("for patients with" → "the … in patients with") — manuscript_v1.1.5.md:190; replacement in §3.3(c).
8. **Cover letter redefines PHN by its symptom** ("clinically defined by mechanical allodynia") — cover_letter_JPR.md:12; replacement in §5.
9. **Abstract sits exactly at the 300-word limit** (300/300 strict tokenization; 310 with keywords) — trim ~20 words per §1.1.
10. **Minor mechanical items:** "i.e." → "ie" (manuscript_v1.1.5.md:92, Dove "do not punctuate abbreviations"); expand ECM and CI at first use in the abstract (manuscript_v1.1.5.md:19, 21; Dove "spell out acronyms in the first instance in the abstract and paper"); [14] title hyphenation "Merkel cell" → "Merkel-cell" (manuscript_v1.1.5.md:200); add the STROBE sentence to §2.1 (§6.1); optionally cite the Adv Science article for [12].

**Desk-reject screen:** nothing rises to desk rejection — scope fits the journal, article type is correct, all mandatory sections and contact elements are present, the abstract is within the limit, and every scientific number I could recompute is correct. The must-fix items are mechanical/editorial and require no new analysis.

---

## Verdict: **Minor revision** — the science is verified and internally honest, and acceptance hinges only on correcting four reference errors, re-pointing the data-availability tag, removing one internal-process label, and tightening the abstract and letter wording; none of these requires new analysis.
