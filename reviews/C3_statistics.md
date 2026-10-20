# C3 — Statistics audit (independent recomputation and deposit cross-check)

**Reviewer:** C3 (independent statistics auditor)

## Scope

I treated every number in v1.1.8 as a claim to be re-derived, not transcribed. Two independent lines of evidence:

1. **Shipped verifier, re-run from scratch** — `analysis/verify_round2/verify_round2.py` recomputes all Round-2 statistics from the raw count matrices and the frozen panel only, and compares against both the deposited artifacts and the manuscript's printed values. **Result: 114/114 checks PASS, exit 0.** Coverage: 8-module BH family ×3 contrasts + manuscript q ordering (N3 0.014 / N2 0.023 / E1 0.034 / M2 0.136 / M1 0.181 / N1 0.201 / M3·M4 0.462), DiDiD and its composite, M4 route difference (+0.0266; P = 0.5783), CCI family (full-set nulls, detected +215.6/P = 0.046, counterfactual +2,470/P = 0.0006, TRPA1 −5,451 ranks, E1 mean displacement 596), E1-core sensitivity (−0.2442; Welch P = 0.0037; perm P = 0.0023; CI −0.39 to −0.10 at Satterthwaite df 9.38), PTK2 exclusions (M3 −0.0475/P = 0.435; M4 −0.0238/P = 0.524), per-route DiD values, detected-gene M1 (−0.171; P = 0.046), E1−N1 benchmark (−0.064; P = 0.178).
2. **My own fresh recomputation of Table 1 and the §3.1 expression baseline** from the raw CSV.gz counts (not via the shipped scripts): CPM conversion, per-experiment means and detected fractions for all ten tabulated genes, plus the log2CPM values and cross-experiment ratios quoted in prose.

## Fresh recomputation results (raw counts, independent pipeline)

| Quantity | Manuscript (Table 1 / §3.1) | My recompute | Match |
|---|---|---|---|
| PIEZO2 mean CPM (DirectInf / SeraExo) | 245.2 / 164.1 | 245.24 / 164.13 | ✓ |
| P2RX3 mean CPM | 806.8 / 470.6 | 806.84 / 470.61 | ✓ |
| PIEZO1 mean CPM | 2.64 / 2.20 | 2.64 / 2.20 | ✓ |
| TRPV4 mean CPM | 0.25 / 0.19 | 0.25 / 0.19 | ✓ |
| STOML3 mean CPM | 0.01 / 0.00 | 0.01 / 0.00 | ✓ |
| ITGB1 mean CPM | 323.6 / 360.3 | 323.65 / 360.30 | ✓ |
| SCN10A mean CPM | 7.23 / 0.55 | 7.23 / 0.55 | ✓ |
| SCN9A mean CPM | 318.3 / 261.7 | 318.27 / 261.65 | ✓ |
| TRPV1 mean CPM | 122.3 / 95.6 | 122.27 / 95.58 | ✓ |
| TAC1 mean CPM | 65.7 / 68.9 | 65.73 / 68.91 | ✓ |
| Detected fractions | 1.00/1.00/0.89, 0.00, 1.00, 0.11 … | identical (all 20 values) | ✓ |
| PIEZO2 log2CPM, 12 DirectInf samples | 7.94 | 7.94 | ✓ |
| SCN9A log2CPM (all 12 / mock only) | 8.31 / 8.39 | 8.31 / 8.39 | ✓ |
| TRPV1 log2CPM (all 12) | 6.94 | 6.94 | ✓ |
| SCN10A cross-experiment ratio | "~13-fold" | 13.3 | ✓ |
| PIEZO2 cross-experiment ratio | "~1.5-fold" | 1.49 | ✓ |

## Pan-neuronal panel cross-check (§3.7)

The prose says "five pan-neuronal markers moved modestly … no marker survived Benjamini-Hochberg correction across the ten-gene panel". The deposit (`layer1_extra_checks.json` → `neuronal_integrity_markers`) contains exactly 10 genes; the five listed (NEFH P = 0.0061, TUBB3 0.012, NTRK1 0.0306, PRPH 0.0479, NEFL 0.0526) match the printed P values (0.006/0.012/0.031/0.048/0.053); ATF3 (+0.0002; P = 0.998) matches; the panel-wide BH q minimum is 0.06 > 0.05, so "no marker survived" is correct; and TAC1 (+0.2176; P = 0.3771) matches the §4.1/§4.4(x) non-reproduction statement (+0.22; P = 0.38). ✓

## Method-consistency checks on the prose

- §2.4's testing description (Welch t; exact label-permutation null with full enumeration and no Monte-Carlo/1/B floor; two-sided empirical P; BH across the eight modules per contrast; permutation-inversion CI [D − q0.975, D − q0.025]; MDE from pooled SD with non-central t) matches the implementation re-derived in line 1. ✓
- CI conventions: module CIs use Welch-Satterthwaite; E1-core sensitivity previously printed a pooled df = 12 interval, now printed at Satterthwaite df = 9.38 after the earlier print-error repair (−0.39 to −0.10); consistent throughout. ✓
- Every statistic quoted in Abstract/§3–§5 that I could map to a deposit matched it.

## Defects found in this review

None. The two print defects found at this stage of the pipeline (M3−PTK2 rounding; E1-core CI degrees of freedom) were repaired before this version; I re-verified both repairs hold in the shipped text (−0.047; −0.39 to −0.10).

## Verdict

Statistics are sound and fully traceable. Recommend acceptance on statistical grounds.
