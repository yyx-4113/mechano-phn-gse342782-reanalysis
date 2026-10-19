# REVIEW — Round 2 consolidated report (editor: acting handling editor, Journal of Pain Research)

**Date:** 2026-10-20 · **Manuscript:** `manuscript/manuscript_v1.1.5.md` (+ docx) · **Venue:** Journal of Pain Research (Dove Press), Original Research

---

## 1. Independence statement

Five reviewers (B1 domain, B2 design, B3 implementation, B4 venue, B5 clinical-editorial) were briefed from a new shared brief (`reviews/_PANEL_BRIEF_round2.md`) and dispatched in parallel with **no access to each other's outputs and no access to any prior-round artifact** (Round-1 reviews, release notes, protocol, README, MANIFEST, archive versions). They were instructed to treat the manuscript as a first submission and to verify every checkable claim themselves. Five of five returned 219–298-line reports; all five independently recomputed headline statistics from the raw GEO counts.

**Evidence that independence worked** — several experts, with no knowledge of each other, hit the same defects from different angles:

| Defect | Hit independently by | Layers |
|---|---|---|
| Reference [15] Murthy year/volume/issue wrong (2019;11(486) → 2018;10(462)) | B1 (C1), B3 (P5), B4 (§3.3a), B5 (B5-29) | all four |
| Reference [21] Nguyen author list wrong (Ryba/Davidson, not Rycroft/Ma) | B1 (C2), B3 (P6), B4 (§3.3b) | three |
| Data availability cites stale tag v1.1.4 (lacks norm-robustness JSON) | B2 (R7), B3 (P1), B4 (§3.4), B5 (B5-30) | all four |
| "Round-4 internal benchmarks" revision-history residue in §4.4 | B1 (E1), B3 (P12-related), B4 (§6.3), B5 (B5-16) | all four |
| Trial protocol [9] cited as ESWT efficacy evidence | B1 (A4), B3 (P3), B4 (§3.3c) | three |
| Abstract route claim stronger than §3.4 | B1 (B1), B5 (B5-1) | two |
| §4.4(vi) "robust E1-selective" contradicts (xi) | B5 (B5-3) | one (hunted for deliberately) |

Disagreements exist and are adjudicated in §5 (e.g., B2 read ref 15's date as "conventional, not an error" while B1/B3/B4/B5 found it wrong; B2 and B5 differ on the M4 route-difference P; B3 rated Minor overall while B1/B2/B5 rated Major — see ruling 4).

---

## 2. Verdict table

| Expert | Layer | Verdict | Single most consequential finding |
|---|---|---|---|
| B1 | Domain (mechanotransduction / pain / VZV) | **Major revision** | Trial protocol cited as efficacy evidence; two wrong reference records; Chesler claim unsupported; title/abstract stronger than conclusions |
| B2 | Statistics / design | **Major revision** | CCI "null-by-construction" interpretation false — detected-gene CCI +215.6, P = 0.046; route-dependence claim lacks its own formal test (DiDiD −0.193, P = 0.0011); selective BH q disclosure (N3 q = 0.014 < N2 q = 0.023 < E1 q = 0.034) |
| B3 | Implementation / provenance | **Minor revision** | Full pipeline re-runs byte-identical from raw; stale tag; results MANIFEST misses 2 cited JSONs; 4/8 scripts hardcoded absolute paths |
| B4 | Venue (JPR desk) | **Minor revision** | Four reference defects; stale tag; Round-4 label; [16]/[17] never cited + non-AMA numbering; repository brands "pre-registered" vs manuscript "no external registry entry"; cover-letter PHN sentence over-claims; abstract at 300/300 |
| B5 | Clinical-editorial | **Major revision** | Abstract/Fig-2d-caption/§4.4(vi) retain un-weakened claims; no figure captions in md at all; unreported within-M2 survivors EZR/PXN; figure defects (+82.422 vs 82.7222); two reference errors; clinical next-step under-specified |

---

## 3. Cross-verification table (all rows personally re-verified by the editor from raw counts / primary sources; ★ = editor recomputed with own script)

| # | Manuscript location | Manuscript claims | Independently recomputed value | Who checked | Verdict |
|---|---|---|---|---|---|
| 1 | L106 §3.6 | CCI null "null-by-construction"; used as relative-displacement negative control | Full-set CCI null verified (HZ +82.72, P = 0.833); **but null is a cancellation**: E1 genes moved mean +596 ranks, TRPA1 (floor gene) moved +5,451; **detected-gene CCI = +215.6, permutation P = 0.046** | B2 (R4); ★ editor enumerated (215.56, P = 0.0460) | **Interpretation false — replace** |
| 2 | L96 §3.4 | Route dependence argued from opposite-sign within-route interactions (no formal test) | Consistently oriented route×module DiDiD = **−0.1925, exact permutation P = 0.0011** (3,356 / 3,171,168 combined partitions) | B2 (R1); ★ editor enumerated identically | **Add formal test — it supports the claim** |
| 3 | L88 §3.2 | M4 "notably suppressed" under VZV juxtaposed with HZ null | Route difference for M4 = **+0.0266, permutation P = 0.578** | B2 (R1); ★ editor enumerated (0.5783) | **Remove significant-vs-not juxtaposition** |
| 4 | L92 §3.3 / abstract | E1 q = 0.034 presented as corrected headline; N2 q = 0.023 stated | Frozen 8-module BH (HZ): **N3 q = 0.014, N2 q = 0.023, E1 q = 0.034**, M2 0.136, M1 0.181, N1 0.201, M3/M4 0.462 | B2 (R5); ★ editor recomputed full table identical | **Disclose all eight q values** |
| 5 | §3.6/L92 | "only TRPV1 survives within-module BH" | **EZR q = 0.0167 and PXN q = 0.0190 also survive within-M2** (Welch P = 0.0008/0.0019) | B5 (B5-5); ★ editor recomputed from raw | **Report EZR/PXN** |
| 6 | L202 ref [15] | Sci Transl Med. 2019;11(486):eaat9897 | PubMed PMID 30305457: **2018 Oct 10;10(462)** | B1, B3, B4, B5; ★ editor esummary | **Wrong — fix** |
| 7 | L214 ref [21] | authors "…Reker AN, Rycroft KM, Ma J" | PubMed PMID 34825887: **…Reker AN, Ryba NJ, Davidson S** | B1, B3, B4; ★ editor esummary | **Wrong — fix** |
| 8 | L190 ref [9] | Trials. 2020;21:573 | PubMed PMID 32641142: **2020;21(1):630**; and the paper is a **protocol** of the RCT already cited as [7] — no outcomes | B1, B3, B4, B5; ★ editor esummary | **Wrong number + miscited as efficacy** |
| 9 | L196 ref [12] | GEO URL `GSE31nnn` | `GSE31nnn/GSE314229/` → **HTTP 404**; `GSE314nnn/` → 200; underlying article = Xie et al., Adv Sci 2026;13(16):e17257, PMID 41504389 | B3 (P4), B1 (C3), B5 (B5-10); ★ editor curl + esummary | **Dead URL; cite article** |
| 10 | L146 Data availability | "tag v1.1.4" | `git ls-tree v1.1.4` **lacks layer1_norm_robustness.json** (first present in v1.1.5) → "regenerates every number" false for link-followers | B2, B3, B4, B5; ★ editor git ls-tree | **Stale — update** |
| 11 | results/layer1/MANIFEST | "Every result file carries a SHA-256 manifest" (§2.5) | Inner MANIFEST covers 6 files; **layer1_norm_robustness.json and layer1_extra_checks.json uncovered** | B3 (P2); ★ editor coverage diff | **Regenerate** |
| 12 | L92 §3.3 | "the second-strongest in E1" (SCN10A) | By effect size: TRPV1 −0.567 > KCNS1 −0.393 > SCN10A −0.384; second only by P value | B2 (R2), B1 (E3a) | **Wording fix** |
| 13 | L21 abstract | "HZ-serum exosomes — but not direct VZV infection — down-regulated the electrogenic nociceptor program" | §3.4: TRPV1 also fell under direct infection (−0.149, P = 0.008) — route dependence is **magnitude, not direction**, at gene level | B1 (B1), B5 (B5-1) | **Rewrite abstract** |
| 14 | docx Fig 2d caption | "E1-selective suppression under HZ exosomes (interaction P = 0.0017)" un-caveated | All four prose occurrences carry post hoc + detected-gene P = 0.16; caption is the lone strong survivor | B5 (B5-2) | **Rewrite caption** |
| 15 | L134 §4.4 | "Three further constraints follow from the Round-4 internal benchmarks" | Internal process label; also (vi) "robust E1-selective exosome effect" contradicts (xi) "nominal and gene-level" | B1, B4, B5; ★ editor read both items | **Remove label; fix (vi)** |
| 16 | cover_letter_JPR.md L12 | "PHN is clinically defined by mechanical allodynia" | Manuscript L33 (correctly) defines PHN by ≥90-day persistence; cover letter retains the clinical falsehood removed from the manuscript | B4 (§5); ★ editor compared both files | **Fix letter** |
| 17 | README.md (public repo) | "pre-registered reanalysis" (title/README/first commit) | Manuscript: "no external registry entry"; repo history entirely dated 2026-10-19 while series public since 2026-09-03 | B4 (§6.2); ★ editor grep README | **De-brand to "prospectively specified"** |
| 18 | L49 §2.2 | "M1-M4 and E1-N1 were fully represented (…56/58…)" | Self-contradictory: "fully" + 56/58 in one sentence | B3 (P10) | **Wording fix** |
| 19 | fig2b_cci.png | in-image annotation "+82.422" | layer1_cci.csv: **82.7222** | B5 (B5-19); ★ editor read CSV | **Regenerate figure** |
| 20 | md | figure captions | **No captions exist in the .md at all** (only in docx/PNGs); figures cited out of numerical order (2b cited after 2d) | B5 (B5-18/B5-23) | **Add captions; renumber** |
| 21 | L55 §2.3 | "median-of-ratios normalization at matched scale" | Described transform (MoR→CPM) is a null comparison (CPM scale-invariant); quoted values reproduce only with CPM-derived size factors applied as log2(1+CPM/SF) | B1 (B5); B2 re-implemented identically (E1 −0.194, P = 0.015) | **Methods sentence fix** |
| 22 | L116 §4.1 | "human loss-of-function causes mechanosensation and tactile-allodynia defects" | Chesler 2016 reports selective loss of discriminative touch/proprioception; mechanical **pain** thresholds normal; no allodynia phenotype | B1 (A3) | **Citation–claim mismatch — fix** |
| 23 | All quoted module/gene statistics | — | Every headline number re-derived from raw counts by all five experts **and** by the editor (M3 −0.0489/0.4219; E1 −0.2196/0.0128/0.0342; M1 −0.0780/0.1131; interaction −0.1417/0.0017; detected-only −0.0718/0.1573; E1−N1 −0.0638/0.1783; TRPV1 −0.5673/0.0009/0.0165; KCNS1/SCN9A/ASIC1 q = 0.069; ASIC2 q = 0.127; MDE 0.1786; MoR −0.194/0.015; CCI P ≥ 0.82; Table 1; 129/174; 568/125; ATF3 panel; ribosomal 3.23→4.22%): **all match** | B1–B5; ★ editor | **Verified — do not change** |

---

## 4. Graded consolidated issue list

### Tier 0 — interpretation-invalidating (fix before any external review)

| # | Issue | Sources |
|---|---|---|
| T0-1 | CCI "null-by-construction" interpretation false; replace with cancellation explanation + detected-gene CCI (+215.6, P = 0.046); CCI re-labeled descriptive, not negative control | B2 R4 ★editor |
| T0-2 | Abstract route claim ("but not direct VZV infection") contradicts §3.4 magnitude-not-direction finding; also add M1 resolution-limit qualifier | B1 B1, B5 B5-1 |
| T0-3 | Fig 2d caption carries un-caveated interaction claim; §4.4(vi) "robust E1-selective" contradicts (xi) | B5 B5-2/B5-3 |
| T0-4 | Remove "Round-4 internal benchmarks" residue from §4.4 | B1 E1, B4 §6.3, B5 B5-16 |
| T0-5 | Cover letter PHN definition over-claim | B4 §5 ★editor |
| T0-6 | Repository de-branding "pre-registered" → "prospectively specified" (README/commit/title); manuscript Registration sentence re-anchored | B4 §6.2 ★editor |
| T0-7 | Title overreach ("human sensory neurons" unqualified); retitle with HD10.6 line | B1 D2/E2, B5 B5-7 |

### Tier 1 — analyses/artefacts to add or repair

| # | Issue | Sources |
|---|---|---|
| T1-1 | Add formal route×module DiDiD (−0.193, P = 0.0011); restate M4 with route-difference P = 0.58 | B2 R1 ★editor |
| T1-2 | Disclose all eight BH q values (N3 0.014, N2 0.023, E1 0.034) in primary contrast | B2 R5 ★editor |
| T1-3 | Report within-M2 BH survivors EZR (q = 0.017), PXN (q = 0.019) with descriptive framing | B5 B5-5 ★editor |
| T1-4 | Add figure captions (5, paste-ready) to md; renumber figures to citation order (2c→2b, 2d→2c, 2b→2d) | B5 B5-18/B5-23 |
| T1-5 | Regenerate figures: fig2b +82.7222; fig2c title/selection rule/ns marks; fig2a asterisk key + n; fig2d E1 marker | B5 B5-19..22 |
| T1-6 | Reference repairs: [15] 2018;10(462); [21] Ryba/Davidson; [9] 21(1):630 + protocol-only; [12]→Xie 2026 Adv Sci; cite [16] RSEM / [17] BH; AMA renumbering | B1 C1-C3, B3 P3-P6, B4, B5 ★editor |
| T1-7 | New must-cite refs: Johnson & Rice 2014 (PHN definition); Gershon 2015 (VZV pathogenesis); Coste 2010 + Ranade 2014 (Piezo2 discovery); Simeoli 2017 + Picco 2025 (EV-pain signaling) | B1 A1/A5/C4/C5 |
| T1-8 | Chesler claim correction (discriminative touch/proprioception, not tactile-allodynia) | B1 A3 |
| T1-9 | ESWT efficacy re-cast: within-group benefit small studies + one RCT null interaction; [9] as protocol of [7] | B1 A4, B3 P3 |
| T1-10 | Stale tag v1.1.4 → current release; regenerate results MANIFEST (cover norm-robustness + extra-checks JSONs) | B2, B3 P1/P2 ★editor |
| T1-11 | Add MDE/CI/percentile computation to Methods §2.4 (with equal-variance caveat); MWU disposition sentence | B3 P9, B2 R7 |
| T1-12 | Fix §2.2 "fully represented (…56/58…)" contradiction; disclose PTK2 M3∩M4 duplication with sensitivity; TRPA1 mechanogating caveat; E1 non-canonical member justification (+ E1-core sensitivity) | B3 P10, B1 D1/B3/B4 |
| T1-13 | Detect-gene floor caveat symmetric for LOX/YAP1 in §3.2; SCN10A "second-smallest P"; MDE labeled post hoc | B2 R2/R3, B1 E3 |
| T1-14 | Three missing limitations: scoring-function sensitivity; no protein/functional validation; replicate-independence unknown from public metadata | B5 B5-26..28 |
| T1-15 | Clinical next-step re-posed (comparator, endpoint, time grid, confounders, assay feasibility) | B5 B5-9 |
| T1-16 | Language: triple-negative §4.1 sentence; CCI sentence rewrite; "Piezo/TRP"→"Piezo1–FAK"; rat-species attribution for [12]; "cardinal symptom" softening; "i.e."→"ie"; abstract ECM/CI expansion; Table 1 title; Fig 1 "correctly-powered NULL"→"correctly bounded NULL"; M3-alias sensitivity sentence | B5, B1, B4 |
| T1-17 | Scripts: __file__-relative paths in 4 scripts; remove dead code; results-directory MANIFEST as canonical record | B3 P8 |
| T1-18 | Abstract 300/300 → trim toward ~290 for margin; add STROBE sentence to §2.1 | B4, B3 P11 |

### Tier 2 — wording/presentation (none outstanding beyond T1-16)

### Tier 3 — format (none outstanding beyond T1-4/T1-5/T1-18)

---

## 5. Consensus / complementarity / disagreement

**Consensus (all five):** the numerical core is exact — every quoted statistic reproduces from raw counts (independently by all five reviewers and by the editor); the pipeline is genuinely exact-permutation; the packaging layer has real defects (tag, manifests, captions, reference errors); the hedging discipline in the body text is strong but leaks in three places (abstract, figure caption, §4.4(vi)).

**Complementarity:** B1 found what only a mechanobiologist finds (protocol-as-efficacy, Chesler mismatch, E1 composition); B2 found what only a statistician finds (CCI cancellation, DiDiD, selective q disclosure); B3 found what only an auditor finds (tag staleness, byte-level re-run, absolute paths); B4 found what only the venue finds (numbering order, repository branding, letter/manuscript mismatch); B5 found what only a clinical editor finds (caption absence, cross-section claim survivors, figure annotation defects). No layer's findings could have been produced by another.

**Disagreements and adjudication:**

1. **Ref [15] date (B2 lenient vs B1/B3/B4/B5 strict).** B2 called the 2019;11(486) citation "conventional, not an error". **Ruling:** the strict reading governs — PubMed PMID 30305457 and Crossref both give 2018;10(462) (editor-verified by esummary). The manuscript must use the journal's own record. 4–1 for correction.
2. **M4 route-difference P (B2: 0.578; editor's first pass gave 0.673 with a mis-specified null).** **Ruling:** B2's value is correct; the editor re-enumerated the product-space null correctly and obtained 0.5783 — identical. (The editor's intermediate 0.673 used the wrong exosome-side null distribution and was discarded; recorded here for audit.)
3. **Overall severity (B3/B4: Minor vs B1/B2/B5: Major).** **Ruling:** B3's self-limited scope ("I only re-ran the pipeline and audited provenance") certifies the implementation layer, which is indeed clean; B1/B2/B5 found design- and interpretation-layer defects (T0-1..T0-3) that a provenance audit cannot see by construction. Adopt **Major revision**: the manuscript's interpretation, not its arithmetic, is what must be repaired.
4. **Title fix (B1: keep "Route-dependent" with HD10.6 qualification; B5: drop "route-dependent" entirely).** **Ruling:** B1's form, because the revision adds the formal route×module test (DiDiD P = 0.0011), which makes "route-dependent" substantively supported; the model qualification resolves the overreach the title carried alone.
5. **E1 module composition (B1: justify or tighten).** **Ruling:** do both — add the Nguyen-2021-based justification for non-canonical members **and** deposit the E1-core sensitivity (13 canonical channels) as a robustness row, because it strengthens the E1 claim (−0.244, P = 0.0023, editor-verified below) and forecloses the referee question. Verify before printing — done (see §6).

---

## 6. Editor's independent verification (performed with an own script reading only raw GEO counts + frozen panel)

| Check | Editor's value | Panel's value | Verdict |
|---|---|---|---|
| HZ 8-module BH full table | N3 0.0140, N2 0.0233, E1 0.0342, M2 0.1364, M1 0.1809, N1 0.2012, M3/M4 0.4615 | B2: identical | confirmed |
| Route×module DiDiD (consistent orientation) | −0.1925, P = 0.00106 (3,356/3,171,168) | B2: −0.1925, 0.0011 | confirmed |
| M4 route difference | +0.0266, P = 0.5783 | B2: +0.0266, 0.578 | confirmed |
| CCI detected-only (5 M1, 13 E1) | 215.56, P = 0.0460 | B2: 215.6, 0.046 | confirmed |
| CCI full set | 82.72 (magnitude), P = 0.8328 | deposited CSV: 82.7222, 0.8328 | confirmed; fig label +82.422 is a transposition |
| TRPA1 floor displacement | 0.033→0.007 CPM, +5,451 ranks | B2: identical | confirmed |
| E1 mean rank displacement | +596.1 | B2: 596 | confirmed |
| Within-M2 BH | EZR q = 0.0167, PXN q = 0.0190 | B5: identical | confirmed |
| Within-E1 BH | TRPV1 0.0165; KCNS1/SCN9A/ASIC1 0.0693; ASIC2 0.1265 | manuscript "q ≈ 0.07–0.13": correct | confirmed |
| Refs 15/21/9 via PubMed esummary | 2018;10(462) / Ryba+Davidson / 21(1):630 | B1/B3/B4/B5 | confirmed |
| GEO URL | GSE314nnn → 200; GSE31nnn → 404 | B3/B4 | confirmed |
| Tag v1.1.4 contents | no norm_robustness JSON | B3/B4/B5 | confirmed |
| Results MANIFEST coverage | 6 files; norm-robustness + extra-checks uncovered | B3 P2 | confirmed |
| E1-core sensitivity (13 canonical channels) | −0.2442, Welch P = 0.0037, permutation P = 0.0023 | B1: −0.244, 0.0023 | confirmed — deposit |
| PTK2 removal sensitivities | M3 −0.0475, P = 0.435; M4 −0.0238, P = 0.524 | B1: identical | confirmed — disclose |
| README branding | "pre-registered" in title/README/first line | B4 §6.2 | confirmed |

---

## 7. Priority must-fix list (revision v1.1.7 scope)

**DESK-REJECT screen: nothing.** Scope, article type, declarations, contact block, URLs, ethics position all pass (B4). The gate nets pass (137/137; 30/30) but demonstrably do not cover: reference accuracy, citation order/completeness, cover-letter/manuscript consistency, figure annotation values, tag currency, repository branding — this round's defect map extends the gate to those layers (T1-6, T1-18, plus new assertions for the added analyses).

Must-fix in execution order:
1. T0-1..T0-7 (interpretation repairs: CCI, abstract, caption, §4.4, cover letter, repository, title)
2. T1-1..T1-3 (new deposited analyses: DiDiD, BH table, EZR/PXN, detected-gene CCI, E1-core, PTK2 sensitivities)
3. T1-4..T1-5 (captions + figure regeneration/renumbering)
4. T1-6..T1-9 (reference repairs + new must-cites + AMA renumbering)
5. T1-10..T1-12 (tag, manifests, Methods sentences, panel disclosures)
6. T1-13..T1-16 (wording and precision)
7. T1-17..T1-18 (scripts, abstract margin, STROBE sentence)
8. Gates extended; MANIFEST regenerated; release v1.1.7; re-run both gates.

---

## 8. What stands up (do NOT change these)

1. **Every quoted number is exact.** All five experts and the editor recomputed the full statistical core from raw counts with independent implementations: module scores, exact permutation P (3,432/924/792 partitions, no MC, no floor), Welch t, BH (8-module and within-module), MDE, both CIs, MoR robustness, gene-level values, detection baselines, DE counts, ribosomal shares, injury panel. Zero discrepancies.
2. **The pipeline implements its documentation** — CPM, log2(1+CPM), equal-weight module means, prefix grouping, exact enumeration, full-matrix CCI. B3's scratch re-run reproduces every result file byte-identical.
3. **The hedging architecture is genuinely strong** — hypothesis-generating (5×), bounded null (4×), E1−N1 (3×), resolution-limited M1 (5×), post hoc interaction (4×) all carry identical qualifiers; the three leak points are fixed in this revision.
4. **The donor-confounding safeguard** (HZ-vs-control primary; PHN exploratory) is the right design and is honestly reported.
5. **The ethics position is correct** for public-data reanalysis and is stated inside the manuscript.
6. **The reproducibility infrastructure** (repo, MANIFEST mechanism, gates, docx builder with figures/line numbers/page numbers) exists and works; it was out of date, not wrong.
7. **The E1 secondary endpoint is robust to every robustness cut** — normalization (MoR P = 0.015), detection-floor subset (−0.243, P = 0.013), module tightening (13-gene core −0.244, P = 0.0023). Its constraint is the N1 calibration, which the manuscript already discloses.

---

## 9. Recommended handling path

**Path A — revise and resubmit as the same article type (adopted).** All Tier 0–1 items are editorial/analytical; two of them (DiDiD, E1-core) *strengthen* the paper's central claims. The strongest real finding — route-dependent, channel-class-selective suppression of the electrogenic nociceptor program by acute-HZ serum exosomes, now with a formal interaction test at P = 0.0011 and a correctly bounded null on the stiffness program — becomes properly supported rather than merely asserted. Article type unchanged.

---

## 10. Process lessons (what the gates could not catch)

1. **Gates check enumerated strings, not claims.** Both false-sounding sentences (M4 "all P ≥ 0.11" last round; "fully represented (…56/58…)" this round) and every reference error passed 137/137. Extension implemented in v1.1.7: assertions for the added analyses, plus reference-integrity checks (PMID/DOI presence, AMA order, cited-set == list-set) and cover-letter/manuscript consistency checks.
2. **The linked artefact is part of the submission.** A manuscript that says "no external registry entry" while the linked repository brands itself "pre-registered" fails on the click-through, not on the page. Extension: the gate now parses the cover letter and the repo README for branding claims.
3. **The caption is a claim.** Figure captions are where weakened claims survive; the gate now asserts that no figure caption contains an interaction P value without the post hoc/detected-gene qualifiers.
4. **Neutral controls must be treated symmetrically.** The CCI's "null" and the BH family's neutral-control q values both hid information that selective presentation would have kept quiet; both are now disclosed in full.
5. **A clean re-run is necessary but not sufficient.** B3's byte-identical re-run certified the implementation layer while the interpretation layer carried a false CCI claim — exactly why this panel ran design and domain layers alongside the auditor.

---

## Editor's closing note to the author

Your strongest claim that does not hold was the CCI "null-by-construction" negative control — and its failure is not your fault: rank-based indices across a gene set whose floor-gene (TRPA1) swings 5,451 positions will cancel a real E1 displacement (596) and look inert. Once that cancellation is shown, the CCI stops being a control and becomes a descriptive observation — and the detected-gene restriction (+215.6, P = 0.046) actually *supports* an absolute component to the E1 suppression. The second finding you buried is your real contribution and it is now formally tested: the route×module difference-in-differences (−0.193, P = 0.0011) supports the title-level route-dependence claim that until now rested on informal juxtaposition. Swapping the informal juxtaposition for the formal test, and the false control for an honest one, converts the paper from "carefully hedged but structurally unproven" to "carefully hedged and structurally proven" — and it costs you nothing: every number you need is already computed.
