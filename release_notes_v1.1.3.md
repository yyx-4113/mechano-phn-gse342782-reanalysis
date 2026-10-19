# Release v1.1.3 — JPR Round-3 expert review revisions (scientific honesty pass)

Round-3 revisions driven by a three-reviewer panel (biostatistics/methodology, pain
neuroscience/mechanotransduction, clinical pain medicine). The substantive results are unchanged
(M3 primary endpoint remains a bounded null; the E1 channel-imbalance signal remains the finding);
what changed is the **precision and modesty with which they are stated**, plus a new
multiplicity-control step that was previously missing from the pipeline.

## Scientific changes

### 1. Within-module Benjamini–Hochberg correction added to the pipeline (new)
Gene-level *P* values were previously reported nominally, with "individual E1 genes significant"
claimed without multiplicity control inside the module. The pipeline now applies BH **within each
module, within each contrast**, and writes the result to two artifacts:

- `analysis/results/layer1/layer1_gene_level.csv` — new column `q_within_module`
- `analysis/results/layer1/layer1_results.json` — new key `gene_level_bh`

Verified values for the main contrast (HZ-exo vs control-exo):

| Module | Gene | log2FC | Welch *P* | q within module |
|---|---|---|---|---|
| E1 | **TRPV1** | −0.567 | 0.0009 | **0.0165 (survives FDR)** |
| E1 | SCN10A | −0.384 | 0.0076 | 0.0684 |
| E1 | ASIC1 / KCNS1 / SCN9A | −0.18 / −0.39 / −0.32 | 0.019 / 0.017 / 0.018 | 0.0693 |
| E1 | ASIC2 | −0.296 | 0.042 | 0.1265 |
| M1 | PIEZO2 | −0.282 | 0.182 | 0.2905 |

**Only TRPV1 survives FDR within E1.** The manuscript now says so explicitly, and the consistency
gate locks this direction in place (assertions that TRPV1 q ≤ 0.05 and that KCNS1/SCN9A/ASIC1/ASIC2
q ≥ 0.05), so the text cannot silently drift back to "all genes significant".

### 2. Directionality paradox addressed head-on (§4.1)
Pro-nociceptive channel mRNAs go **down**, yet PHN mechanical allodynia implies hyperexcitability.
The discussion now offers a three-part reconciliation instead of deflecting to
"hypothesis-generating": (i) mRNA–function decoupling with post-translational sensitization as the
proximate driver; (ii) serum exosomes read as a *host signal* acting on neurons rather than a
read-out of the neuron's own state; (iii) model boundaries (36-h exposure, immortalized embryonic
DRG line). A clinically testable prediction is stated: serial measurement of the HZ-exosome
channel signature to predict PHN at 90 days.

### 3. Terminology and scope corrections
- §3.2: gene-level *P* values under M3 are labelled as uncorrected nominal values across 56 genes.
- §3.4: the "detected-gene only" analysis is explicitly identified as a **subset sensitivity
  analysis, not a multiplicity correction** (the previously truncated sentence fragment was repaired).
- §4.2: route-dependence wording softened to match what a single 36-h in vitro contrast can support.
- §4.3: ESWT demoted to contextual background, explicitly **not** evidence supporting these findings.
- §4.4: three new limitations — (viii) exosome cargo not experimentally verified; (ix) SCN10A shows a
  ~13-fold between-experiment CPM difference (7.23 vs 0.55), i.e. floor-limited; (x) the substance P
  / neuropeptide-switch observation did not reproduce here (TAC1 +0.22, *P* = 0.38).
- §2.4–§2.5: traceability statement corrected — gene-level statistics are traceable to
  `layer1_results.json` **and** `layer1_gene_level.csv` (both under the SHA-256 MANIFEST), not to the
  JSON alone as previously claimed.
- §5: conclusion rewritten to match the evidence strength.

## Consistency & reproducibility
- `gate_consistency.py`: **95/95 assertions PASS** (up from 87; the eight new assertions cover the
  within-E1 BH values and the two clarified wordings).
- Independent recomputation of the within-E1 BH values performed outside the pipeline; matches.
- `MANIFEST.json`: 38 deposited files, tag `v1.1.3`, SHA-256 over every artifact.
- Repository: https://github.com/yyx-4113/mechano-phn-gse342782-reanalysis (tag v1.1.3)

## Known open item (addressed in v1.1.4)
The Round-3 rewrites pushed the **structured abstract to 414 words, above JPR's 300-word limit**.
This release records the scientific state; the abstract is trimmed and a word-count assertion added
to the gate in v1.1.4.
