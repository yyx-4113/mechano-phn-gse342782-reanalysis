# Round 4 — Editor's synthesis and decision (post-polish verification review)

**Editor:** acting handling editor, Journal of Pain Research
**Manuscript:** v1.1.8 (de-AI language revision of the Round-3-accepted v1.1.7)
**Panel:** C1 semantic-drift audit · C2 domain (fresh eyes) · C3 statistics · C4 language/compliance
**Decision:** **ACCEPT after one required micro-repair — to ship as v1.1.9.** No further review cycle required.

## Why this round existed

v1.1.8 changed prose only: 54 em-dashes removed, de-AI vocabulary, one count made precise. Programmatic checks had confirmed the numeric sets are unchanged. What those checks cannot show is whether any sentence quietly changed meaning. A language-only revision of an accepted manuscript is precisely where silent damage hides, so the polish was re-reviewed rather than waved through.

## Findings across the panel

| # | Finding | Reviewer | Severity | Disposition |
|---|---|---|---|---|
| 1 | §3.1: apposition never closed — "…not an iPSC-derived model^16,17^ expressed PIEZO2 at high levels" (first dash → comma, second dash deleted without comma) | C1 | Required fix | **Repair in v1.1.9** |
| 2 | §3.4: "SCN10A contributes to E1 only in the infection experiment" — imprecise (gene is in E1 on both routes; contribution differs) | C1, C4 | Advisory | **Repair in v1.1.9** (one clause) |
| 3 | §3.3 "ie" without periods | C4 | Style, previously ruled | **Retained** — no evidence to overturn a recorded prior decision; normalizable at proof |
| 4 | §3.3 section title states module-level suppression while body qualifies it as nominal/gene-level | C2 | Non-blocking observation | **Retained** — declarative section titles are journal-normal; body qualifies immediately |
| 5 | §3.6 prose "normalization sensitivity analysis" vs artifact `layer1_norm_robustness.json` | C1 | Cosmetic | **Retained** — file cited verbatim in §2.5; traceability intact |
| 6 | 40-block semantic drift audit: 0 meaning changes; 4 changes improve precision (list in C1) | C1 | — | Confirmed safe |
| 7 | Statistics: verifier 114/114 re-run; Table 1 + §3.1 expression baseline recomputed independently from raw counts (22/22 values match); pan-neuronal panel = 10 genes, q-min 0.06, five listed markers match | C3 | — | Confirmed sound |
| 8 | Language/compliance: em-dash 0, hedges intact, AMA mechanics pass, JPR checklist complete | C4 | — | Confirmed |

## What each reviewer independently established

- **C1** adjudicated all 40 diff blocks: 39 meaning-preserving (punctuation or vocabulary class), 1 defect (finding 1). Numbers, citations, captions and all ~130 gated fragments verified untouched between versions.
- **C2** found the claim calibration unusually disciplined (selectivity, M1 null, ESWT, PHN contrast all correctly fenced) and verified the domain claims I checked against the literature the manuscript cites; no domain objection.
- **C3** re-ran the shipped verifier (114/114) and independently rebuilt Table 1 and the §3.1 baseline from raw counts — every value matches, including the ~13-fold SCN10A and ~1.5-fold PIEZO2 cross-experiment ratios.
- **C4** confirmed the polish achieved its goal without stripping functional hedging; re-ran the full submission checklist; ruled on the two style questions.

## Required actions (all text-only, both riding in v1.1.9)

1. §3.1: insert the closing comma — "not an iPSC-derived model^16,17^, expressed PIEZO2 at high levels".
2. §3.4: "contributes to E1 only" → "contributes appreciably to the E1 score only".

## Acceptance conditions (mechanical, verified before the decision letter issues)

- numeric set-diff v1.1.8 → v1.1.9 empty both directions (already true of the two required edits — punctuation only);
- gate_consistency and gate_jpr_compliance green on the new text (update the "ie" fragment check to remain satisfied — the phrase is untouched — and the version/tag assertions to v1.1.9);
- editor verifier re-run 114/114;
- docx rebuilt and structure-verified; md↔docx numeric diff zero;
- packaging cascade (README, CITATION.cff, MANIFEST, release notes, tag, Release) re-pointed to v1.1.9.

## Decision

The manuscript is scientifically accepted (Round 3) and now linguistically verified (Round 4). The two repairs are punctuation-class and carry no scientific risk. **Upon their application and the mechanical acceptance conditions above, v1.1.9 is the final submission version; no further expert review is required.** Repositories, manifest and release are to be re-synchronized to tag v1.1.9 before the package is handed back for upload.
