#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Editor independent verification of the Round-2 additions and every
Round-2-derived number printed in manuscript v1.1.7.

Reads ONLY the raw GEO counts + the frozen panel + the deposited artifacts;
recomputes everything from scratch and compares. Exits non-zero on any FAIL.
This script is part of the reproducibility package: run it before tagging a
manuscript release.

    python analysis/verify_round2/verify_round2.py

v2 (2026-10-20)
---------------
FIX: v1's M4-route combined null mistakenly reused the E1-M1 *composite*
exosome permutation distribution (de_arr built from both_e = composite
scores) instead of the M4-only module-score distribution, producing
P=0.6731 instead of the deposited 0.5783. The M4-only null is the correct
one for the M4 route-difference statistic (the interaction is computed on
the M4 module, not on the E1-M1 composite). v2 rebuilds both4_e from the
M4 module scores, mirroring layer1_round2_additions.py section B.

EXTEND: v1 covered only 8-module BH, DiDiD, M4 route, CCI, within-module
survivors. v2 additionally independently recomputes every other Round-2
addition that entered manuscript v1.1.7:
  - E1-core (13 canonical channels) sensitivity, Welch + exact perm + CI
    (Welch-Satterthwaite df convention, matching the main results)
  - PTK2 overlap sensitivity (M3-PTK2, M4-PTK2)
  - CCI counterfactual (uniform -0.2196 shift imposed on E1 of HZ)
  - per-route DiD P values (exosome full, infection, detected-gene subset)
  - detected-gene M1 module shift
  - E1-vs-N1 per-sample benchmark
  - CCI decomposition facts (top E1 downward displacements, TRPA1, means)
Every recomputed value is compared against the deposited artifact
(analysis/results/layer1/layer1_round2_additions.json, layer1_results.json,
layer1_extra_checks.json) and, where the deposit is rounded, against the
value printed in manuscript v1.1.7.

v2b (2026-10-20, after v2 found two manuscript print errors):
  - manuscript M3-PTK2 difference printed -0.048; full precision is
    -0.0474965, so the correct 3-dp print is -0.047. Reference updated.
  - manuscript E1-core Welch CI printed "-0.38 to -0.11" from a df=12
    (pooled) interval; the correct Welch-Satterthwaite interval is
    [-0.388, -0.101], printed "-0.39 to -0.10". The deposit
    (layer1_round2_additions.json) was regenerated accordingly (diff
    confirmed: only welch_ci95 changed, plus new welch_ci95_df=9.38).
    References updated to the Satterthwaite convention.
"""
import gzip, json, math, itertools, os, sys
import pandas as pd
import numpy as np
from scipy import stats

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW = os.path.join(ROOT, "analysis", "data", "raw")
SERA = os.path.join(RAW, "GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz")
DI = os.path.join(RAW, "GSE342782_Processed_DirectInf_neuronHD10s_BulkSeq_Counts.csv.gz")
PANEL = json.load(open(os.path.join(ROOT, "analysis", "config", "mtp_panel.json"), encoding="utf-8"))
DEP = os.path.join(ROOT, "analysis", "results", "layer1")
R2 = json.load(open(os.path.join(DEP, "layer1_round2_additions.json"), encoding="utf-8"))
R1 = json.load(open(os.path.join(DEP, "layer1_results.json"), encoding="utf-8"))
EX = json.load(open(os.path.join(DEP, "layer1_extra_checks.json"), encoding="utf-8"))

CHECKS = []  # (label, recomputed, reference, ok)

def chk(label, got, want, tol=6e-4):
    ok = abs(float(got) - float(want)) <= tol
    CHECKS.append((label, got, want, ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}: recomputed={got:.6g}  reference={want:.6g}")
    return ok

def chk_int(label, got, want):
    ok = int(got) == int(want)
    CHECKS.append((label, got, want, ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}: recomputed={int(got)}  reference={int(want)}")
    return ok

def load(path):
    return pd.read_csv(path, sep=",", index_col=0)

def L(df):
    cpm = df.div(df.sum(axis=0), axis=1) * 1e6
    return np.log2(1 + cpm)

sera = load(SERA); di = load(DI)
sL, dL = L(sera), L(di)
sera_cpm = sera.div(sera.sum(axis=0), axis=1) * 1e6
di_cpm = di.div(di.sum(axis=0), axis=1) * 1e6

mods = {k: list(v["genes"]) for k, v in PANEL.items() if isinstance(v, dict) and "genes" in v}
names = list(mods.keys())
E1 = [g for g in mods[[k for k in mods if k.startswith("E1")][0]] if g in sL.index]
M1 = [g for g in mods[[k for k in mods if k.startswith("M1")][0]] if g in sL.index]
M2 = [g for g in mods[[k for k in mods if k.startswith("M2")][0]] if g in sL.index]
M3 = [g for g in mods[[k for k in mods if k.startswith("M3")][0]] if g in sL.index]
M4 = [g for g in mods[[k for k in mods if k.startswith("M4")][0]] if g in sL.index]
N1 = [g for g in mods[[k for k in mods if k.startswith("N1")][0]] if g in sL.index]

hz = [c for c in sera.columns if c.startswith("S")]
ctrl = [c for c in sera.columns if c.startswith("C")]
phn = [c for c in sera.columns if c.startswith("P")]
vzv = [c for c in di.columns if c.startswith("vzv")]
mock = [c for c in di.columns if c.startswith("mock")]
print("group sizes (ctrl/hz/phn/mock/vzv):", len(ctrl), len(hz), len(phn), len(mock), len(vzv))
print({k: len(v) for k, v in mods.items()})

def mod_score(Lmat, genes):
    present = [g for g in genes if g in Lmat.index]
    return Lmat.loc[present].mean(axis=0), len(present)

def perm_p(x, y):
    """Exact two-sided permutation P (full enumeration), mirrors deposited perm_p."""
    n1, n2 = len(x), len(y)
    obs = x.mean() - y.mean()
    both = np.concatenate([x, y])
    cnt = 0
    for comb in itertools.combinations(range(n1 + n2), n1):
        s = set(comb)
        g1 = np.array([both[i] for i in comb])
        g2 = np.array([both[i] for i in range(n1 + n2) if i not in s])
        if abs(g1.mean() - g2.mean()) >= abs(obs) - 1e-12:
            cnt += 1
    return obs, cnt / math.comb(n1 + n2, n1)

def bh_q(pairs):
    """pairs: list of (label, p). BH step-up, mirrors deposited bh_q."""
    order = sorted(range(len(pairs)), key=lambda i: pairs[i][1])
    m = len(pairs)
    raw = [pairs[i][1] * m / (r + 1) for r, i in enumerate(order)]
    q = [0.0] * m
    q[-1] = min(1.0, raw[-1])
    for r in range(m - 2, -1, -1):
        q[r] = min(1.0, raw[r], q[r + 1])
    return {pairs[i][0]: q[r] for r, i in enumerate(order)}

def split_diffs(both, n1):
    out = []
    for comb in itertools.combinations(range(len(both)), n1):
        s = set(comb)
        g1 = np.array([both[i] for i in comb])
        g2 = np.array([both[i] for i in range(len(both)) if i not in s])
        out.append(g1.mean() - g2.mean())
    return np.array(out)

# ================= 1. eight-module BH, HZ contrast =================
scores = {m: mod_score(sL, mods[m])[0] for m in names}
pv = {}
for m in names:
    obs, p = perm_p(scores[m][hz].values, scores[m][ctrl].values)
    pv[m] = (obs, p)
qtab = bh_q([(m, pv[m][1]) for m in names])
print("\n=== 1. HZ contrast: 8-module BH (editor recompute) ===")
dep_bh = R2["bh_table_hz_contrast"]
for m in sorted(names, key=lambda m: pv[m][1]):
    print(f"{m:35s} diff={pv[m][0]:+.4f} perm_P={pv[m][1]:.4f} q={qtab[m]:.4f}")
    chk(f"BH diff {m}", round(pv[m][0], 4), dep_bh[m]["diff"])
    chk(f"BH perm P {m}", round(pv[m][1], 4), dep_bh[m]["p_perm_exact"])
    chk(f"BH q {m}", round(qtab[m], 4), dep_bh[m]["bh_q"])
# manuscript printed q ordering (3.6): N3 .014 N2 .023 E1 .034 M2 .136 M1 .181 N1 .201 M3/M4 .462
def _full(prefix):
    return [m for m in names if m.startswith(prefix)][0]
for pfx, want in [("N3", 0.014), ("N2", 0.023), ("E1", 0.034), ("M2", 0.136),
                  ("M1", 0.181), ("N1", 0.201), ("M3", 0.462), ("M4", 0.462)]:
    chk(f"BH q vs manuscript {pfx}", round(qtab[_full(pfx)], 3), want, tol=6e-4)

# ================= 2. route x module DiDiD (E1 - M1 composite) =================
def composite(Lmat, genesA, genesB, cols):
    a, _ = mod_score(Lmat, genesA)
    b, _ = mod_score(Lmat, genesB)
    return a[cols].values - b[cols].values

cx_exo = composite(sL, E1, M1, ctrl); sx_exo = composite(sL, E1, M1, hz)
cx_inf = composite(dL, E1, M1, mock); vx_inf = composite(dL, E1, M1, vzv)
did_exo = sx_exo.mean() - cx_exo.mean()
did_inf = vx_inf.mean() - cx_inf.mean()
did_diff = did_exo - did_inf
both_e = np.concatenate([sx_exo, cx_exo])
both_i = np.concatenate([vx_inf, cx_inf])
de_arr = split_diffs(both_e, len(hz))
cnt = 0
for comb_i in itertools.combinations(range(len(both_i)), len(vzv)):
    s = set(comb_i)
    g1i = np.array([both_i[i] for i in comb_i])
    g2i = np.array([both_i[i] for i in range(len(both_i)) if i not in s])
    di_ = g1i.mean() - g2i.mean()
    cnt += int(np.sum(np.abs(de_arr - di_) >= abs(did_diff) - 1e-12))
denom = 3432 * 924
print("\n=== 2. route x module DiDiD (consistent orientation E1-M1) ===")
print(f"did_exo={did_exo:+.4f} did_inf={did_inf:+.4f} diff={did_diff:+.4f} "
      f"perm P={cnt/denom:.5f} ({cnt}/{denom})")
chk("DiDiD did_exosome", round(did_exo, 4), R2["route_by_module_didid"]["did_exosome"])
chk("DiDiD did_infection", round(did_inf, 4), R2["route_by_module_didid"]["did_direct_infection"])
chk("DiDiD difference", round(did_diff, 4), R2["route_by_module_didid"]["difference"])
chk("DiDiD exact perm P", round(cnt / denom, 5), R2["route_by_module_didid"]["exact_perm_P"], tol=1e-5)
chk_int("DiDiD n_extreme", cnt, R2["route_by_module_didid"]["n_extreme"])
chk_int("DiDiD n_null_partitions", denom, R2["route_by_module_didid"]["n_null_partitions"])
chk("DiDiD P vs manuscript 0.0011", round(cnt / denom, 4), 0.0011)

# ================= 3. M4 route difference (FIXED null) =================
s4_hz, _ = mod_score(sL, M4); s4_ctrl, _ = mod_score(sL, M4)
s4_vzv, _ = mod_score(dL, M4); s4_mock, _ = mod_score(dL, M4)
d4_exo = s4_hz[hz].mean() - s4_ctrl[ctrl].mean()
d4_inf = s4_vzv[vzv].mean() - s4_mock[mock].mean()
d4_diff = d4_exo - d4_inf
both4_e = np.concatenate([s4_hz[hz].values, s4_ctrl[ctrl].values])
both4_i = np.concatenate([s4_vzv[vzv].values, s4_mock[mock].values])
de4_arr = split_diffs(both4_e, len(hz))
cnt4 = 0
for comb_i in itertools.combinations(range(len(both4_i)), len(vzv)):
    s = set(comb_i)
    g1i = np.array([both4_i[i] for i in comb_i])
    g2i = np.array([both4_i[i] for i in range(len(both4_i)) if i not in s])
    di_ = g1i.mean() - g2i.mean()
    cnt4 += int(np.sum(np.abs(de4_arr - di_) >= abs(d4_diff) - 1e-12))
print("\n=== 3. M4 route difference (M4-only null, FIXED) ===")
print(f"d4_exo={d4_exo:+.4f} d4_inf={d4_inf:+.4f} diff={d4_diff:+.4f} "
      f"perm P={cnt4/denom:.4f} ({cnt4}/{denom})")
chk("M4 route diff_exosome", round(d4_exo, 4), R2["m4_route_difference"]["diff_exosome"])
chk("M4 route diff_infection", round(d4_inf, 4), R2["m4_route_difference"]["diff_infection"])
chk("M4 route route_difference", round(d4_diff, 4), R2["m4_route_difference"]["route_difference"])
chk("M4 route exact perm P", round(cnt4 / denom, 4), R2["m4_route_difference"]["exact_perm_P"])
chk_int("M4 route n_extreme", cnt4, R2["m4_route_difference"]["n_extreme"])
chk("M4 route P vs manuscript 0.58", round(cnt4 / denom, 2), 0.58)

# ================= 4. E1-core sensitivity =================
E1CORE = ["SCN9A", "SCN10A", "SCN11A", "TRPV1", "TRPM8", "ASIC1", "ASIC2", "ASIC3",
          "KCNS1", "KCNQ2", "KCNQ3", "CACNA2D1", "CACNA2D2"]
ec = [g for g in E1CORE if g in sL.index]
score = sL.loc[ec].mean(axis=0)
a_c, b_h = score[ctrl].values, score[hz].values
t_ec, pw = stats.ttest_ind(b_h, a_c, equal_var=False)
obs_ec, pp_ec = perm_p(b_h, a_c)
det_ec = [g for g in ec if sera_cpm.loc[g].mean() > 1]
score_d = sL.loc[det_ec].mean(axis=0)
obs_ecd, pp_ecd = perm_p(score_d[hz].values, score_d[ctrl].values)
se = math.sqrt(a_c.var(ddof=1) / len(a_c) + b_h.var(ddof=1) / len(b_h))
ci12 = stats.t.interval(0.95, len(a_c) + len(b_h) - 2,
                        loc=b_h.mean() - a_c.mean(), scale=se)
# Welch-Satterthwaite df for comparison
df_w = se**4 / ((a_c.var(ddof=1)/len(a_c))**2/(len(a_c)-1) + (b_h.var(ddof=1)/len(b_h))**2/(len(b_h)-1))
ciw = stats.t.interval(0.95, df_w, loc=b_h.mean() - a_c.mean(), scale=se)
print("\n=== 4. E1-core sensitivity (13 canonical channels) ===")
print(f"n={len(ec)} diff={obs_ec:+.4f} Welch P={pw:.4g} perm P={pp_ec:.4f}")
print(f"CI df=12 (as deposited): [{ci12[0]:.4f}, {ci12[1]:.4f}]")
print(f"CI Welch-Satterthwaite df={df_w:.2f}: [{ciw[0]:.4f}, {ciw[1]:.4f}]")
print(f"detected-only n={len(det_ec)} diff={obs_ecd:+.4f} perm P={pp_ecd:.4f}")
dep_ec = R2["e1_core_sensitivity"]
chk_int("E1-core n_genes", len(ec), dep_ec["n_genes"])
chk("E1-core difference", round(obs_ec, 4), dep_ec["difference"])
chk("E1-core Welch P", round(pw, 4), dep_ec["welch_P"])
chk("E1-core exact perm P", round(pp_ec, 4), dep_ec["exact_perm_P"])
chk("E1-core CI low (Welch df)", round(ciw[0], 3), dep_ec["welch_ci95"][0], tol=1.5e-3)
chk("E1-core CI high (Welch df)", round(ciw[1], 3), dep_ec["welch_ci95"][1], tol=1.5e-3)
chk("E1-core CI df (Satterthwaite)", round(df_w, 2), dep_ec["welch_ci95_df"], tol=0.01)
chk("E1-core CI low vs manuscript -0.39", round(ciw[0], 2), -0.39, tol=6e-3)
chk("E1-core CI high vs manuscript -0.10", round(ciw[1], 2), -0.10, tol=6e-3)
chk_int("E1-core detected n", len(det_ec), dep_ec["detected_only_n"])
chk("E1-core detected difference", round(obs_ecd, 4), dep_ec["detected_only_difference"])
chk("E1-core detected perm P", round(pp_ecd, 4), dep_ec["detected_only_perm_P"])
print(f"[INFO] pooled-df12 CI (superseded) = [{ci12[0]:.3f}, {ci12[1]:.3f}]; "
      f"Welch-Satterthwaite CI (df={df_w:.2f}) = [{ciw[0]:.3f}, {ciw[1]:.3f}] "
      f"is the deposited and printed convention (manuscript -0.39 to -0.10)")

# ================= 5. PTK2 overlap sensitivity =================
m3_no = [g for g in M3 if g != "PTK2"]; m4_no = [g for g in M4 if g != "PTK2"]
s3, n3g = mod_score(sL, m3_no); s4, n4g = mod_score(sL, m4_no)
o3, p3 = perm_p(s3[hz].values, s3[ctrl].values)
o4, p4 = perm_p(s4[hz].values, s4[ctrl].values)
print("\n=== 5. PTK2 overlap sensitivity ===")
print(f"M3-PTK2: n={n3g} diff={o3:+.4f} perm P={p3:.4f}")
print(f"M4-PTK2: n={n4g} diff={o4:+.4f} perm P={p4:.4f}")
dep_pt = R2["ptk2_overlap_sensitivity"]
chk_int("M3-PTK2 n_genes", n3g, dep_pt["m3_minus_ptk2"]["n_genes"])
chk("M3-PTK2 difference", round(o3, 4), dep_pt["m3_minus_ptk2"]["difference"])
chk("M3-PTK2 perm P", round(p3, 3), dep_pt["m3_minus_ptk2"]["exact_perm_P"], tol=1e-3)
chk("M3-PTK2 vs manuscript -0.047/0.44", round(o3, 3), -0.047, tol=1e-3)
chk("M3-PTK2 P vs manuscript 0.44", round(p3, 2), 0.44)
chk_int("M4-PTK2 n_genes", n4g, dep_pt["m4_minus_ptk2"]["n_genes"])
chk("M4-PTK2 difference", round(o4, 4), dep_pt["m4_minus_ptk2"]["difference"])
chk("M4-PTK2 perm P", round(p4, 3), dep_pt["m4_minus_ptk2"]["exact_perm_P"], tol=1e-3)
chk("M4-PTK2 vs manuscript -0.024/0.52", round(o4, 3), -0.024, tol=1e-3)
chk("M4-PTK2 P vs manuscript 0.52", round(p4, 2), 0.52)

# ================= 6. CCI: full, detected-only, decomposition, counterfactual =================
def cci_per_sample(Lmat, cpm, gA, gB):
    """CCI = mean ascending rank(M1) - mean ascending rank(E1), per sample."""
    asc = Lmat.rank(axis=0, ascending=True, method="average")
    return asc.loc[gA].mean(axis=0) - asc.loc[gB].mean(axis=0)

full_cci = cci_per_sample(sL, sera_cpm, M1, E1)
obs_full, p_full = perm_p(full_cci[hz].values, full_cci[ctrl].values)

def cci_detected(Lmat, gA, gB):
    asc = Lmat.rank(axis=0, ascending=True, method="average")
    ad = [g for g in gA if sera_cpm.loc[g].mean() > 1]
    bd = [g for g in gB if sera_cpm.loc[g].mean() > 1]
    return asc.loc[ad].mean(axis=0) - asc.loc[bd].mean(axis=0), len(ad), len(bd)

det_cci, n_ad, n_bd = cci_detected(sL, M1, E1)
obs_det, p_det = perm_p(det_cci[hz].values, det_cci[ctrl].values)

desc = sL.rank(axis=0, ascending=False, method="average")
disp_e1 = desc.loc[E1, hz].mean(axis=1) - desc.loc[E1, ctrl].mean(axis=1)
disp_m1 = desc.loc[M1, hz].mean(axis=1) - desc.loc[M1, ctrl].mean(axis=1)
disp_trpa1 = desc.loc["TRPA1", hz].mean() - desc.loc["TRPA1", ctrl].mean()
top_e1 = disp_e1.sort_values(ascending=False).head(4)

# counterfactual: uniform -0.2196 log2CPM shift imposed on E1 of HZ
shift = -0.2196
sL2 = sL.copy()
sL2.loc[E1, hz] = sL2.loc[E1, hz] + shift
asc2 = sL2.rank(axis=0, ascending=True, method="average")
cf = asc2.loc[M1].mean(axis=0) - asc2.loc[E1].mean(axis=0)
obs_cf, p_cf = perm_p(cf[hz].values, cf[ctrl].values)

print("\n=== 6. CCI (M1 rank - E1 rank convention) ===")
print(f"full set: diff={obs_full:+.4f} perm P={p_full:.4f}")
print(f"detected only ({n_ad} M1, {n_bd} E1): diff={obs_det:+.4f} perm P={p_det:.4f}")
print(f"E1 mean downward displacement: {disp_e1.mean():+.1f}; M1: {disp_m1.mean():+.1f}; "
      f"TRPA1: {disp_trpa1:+.1f}")
print("top E1 downward:", {g: round(float(v)) for g, v in top_e1.items()})
print(f"TRPA1 mean CPM ctrl={sera_cpm.loc['TRPA1', ctrl].mean():.4f} "
      f"hz={sera_cpm.loc['TRPA1', hz].mean():.4f}")
print(f"counterfactual shift {shift}: CCI diff={obs_cf:+.1f} perm P={p_cf:.5f}")

dep_cci = R2["cci_detected_only"]
chk("CCI full difference", round(obs_full, 1), dep_cci["full_set_difference"], tol=0.06)
chk("CCI full perm P", round(p_full, 4), dep_cci["full_set_perm_P"])
chk_int("CCI detected n_m1", n_ad, dep_cci["n_m1_detected"])
chk_int("CCI detected n_e1", n_bd, dep_cci["n_e1_detected"])
chk("CCI detected difference", round(obs_det, 1), dep_cci["difference"], tol=0.06)
chk("CCI detected perm P", round(p_det, 3), dep_cci["exact_perm_P"], tol=1e-3)
chk("CCI detected vs manuscript +215.6", round(obs_det, 1), 215.6, tol=0.06)
chk("CCI detected P vs manuscript 0.046", round(p_det, 3), 0.046, tol=1e-3)
chk("CCI e1 mean displacement", round(disp_e1.mean(), 0), dep_cci["e1_mean_rank_displacement_down"], tol=1.0)
chk("CCI m1 mean displacement", round(disp_m1.mean(), 0), dep_cci["m1_mean_rank_displacement_down"], tol=1.0)
chk("CCI TRPA1 displacement", round(disp_trpa1, 0), dep_cci["trpa1_mean_rank_displacement_down"], tol=1.0)
chk("CCI TRPA1 cpm ctrl", round(sera_cpm.loc["TRPA1", ctrl].mean(), 4), dep_cci["trpa1_cpm_ctrl"], tol=1e-4)
chk("CCI TRPA1 cpm hz", round(sera_cpm.loc["TRPA1", hz].mean(), 4), dep_cci["trpa1_cpm_hz"], tol=1e-4)
for g, want in dep_cci["top_e1_downward"].items():
    chk(f"CCI top E1 down {g}", round(float(top_e1[g]), 0), want, tol=1.0)
for g, want in [("GRIA1", 2868), ("SCN10A", 1396), ("TRPV1", 1042), ("GRIN2B", 1025)]:
    chk(f"CCI top E1 down vs manuscript {g}", round(float(disp_e1[g]), 0), want, tol=1.0)
dep_cf = R2["cci_counterfactual_uniform_e1_shift"]
chk("CCI counterfactual imposed shift", shift, dep_cf["imposed_shift_log2cpm"])
chk("CCI counterfactual difference", round(obs_cf, 0), dep_cf["cci_difference"], tol=1.0)
chk("CCI counterfactual perm P", round(p_cf, 5), dep_cf["exact_perm_P"], tol=1e-5)
chk("CCI counterfactual vs manuscript +2470", round(obs_cf, 0), 2470, tol=1.0)
chk("CCI counterfactual P vs manuscript 0.0006", round(p_cf, 4), 0.0006, tol=1e-4)

# ================= 7. per-route DiD P values =================
print("\n=== 7. per-route DiD (E1 - M1) P values ===")
obs_didexo, p_didexo = perm_p(sx_exo, cx_exo)
print(f"exosome: diff={obs_didexo:+.4f} perm P={p_didexo:.4f}")
chk("DiD exosome diff vs manuscript -0.142", round(obs_didexo, 3), -0.142, tol=1e-3)
chk("DiD exosome P vs manuscript 0.0017", round(p_didexo, 4), 0.0017)

obs_didinf, p_didinf = perm_p(vx_inf, cx_inf)
print(f"infection (E1-M1): diff={obs_didinf:+.4f} perm P={p_didinf:.4f}")
chk("DiD infection diff (E1-M1) vs deposit did_infection",
    round(obs_didinf, 4), R2["route_by_module_didid"]["did_direct_infection"])
chk("DiD infection magnitude vs manuscript 0.051", round(abs(obs_didinf), 3), 0.051, tol=1e-3)
chk("DiD infection P vs manuscript 0.19", round(p_didinf, 2), 0.19)

det_e1 = [g for g in E1 if sera_cpm.loc[g].mean() > 1]
det_m1 = [g for g in M1 if sera_cpm.loc[g].mean() > 1]
dd_det = (sL.loc[det_e1].mean(axis=0) - sL.loc[det_m1].mean(axis=0))
obs_diddet, p_diddet = perm_p(dd_det[hz].values, dd_det[ctrl].values)
print(f"detected-gene DiD: diff={obs_diddet:+.4f} perm P={p_diddet:.4f}")
chk("DiD detected diff vs manuscript -0.072", round(obs_diddet, 3), -0.072, tol=1e-3)
chk("DiD detected P vs manuscript 0.16", round(p_diddet, 2), 0.16)

# detected-gene M1 module shift (manuscript 3.6: -0.171, P = 0.046)
m1_det_score = sL.loc[det_m1].mean(axis=0)
obs_m1det, p_m1det = perm_p(m1_det_score[hz].values, m1_det_score[ctrl].values)
print(f"detected-gene M1 module: diff={obs_m1det:+.4f} perm P={p_m1det:.4f} (n={len(det_m1)})")
chk("detected M1 diff vs manuscript -0.171", round(obs_m1det, 3), -0.171, tol=1e-3)
chk("detected M1 P vs manuscript 0.046", round(p_m1det, 3), 0.046, tol=1e-3)

# ================= 8. E1 vs N1 per-sample benchmark =================
sE1, _ = mod_score(sL, E1); sN1, _ = mod_score(sL, N1)
bench = sE1 - sN1
obs_b, p_b = perm_p(bench[hz].values, bench[ctrl].values)
t_b, pw_b = stats.ttest_ind(bench[hz].values, bench[ctrl].values, equal_var=False)
print("\n=== 8. E1 - N1 per-sample benchmark (HZ vs Ctrl) ===")
print(f"diff={obs_b:+.4f} perm P={p_b:.4f} Welch P={pw_b:.4f}")
dep_b = EX["e1_vs_n1_benchmark"]["HZexo_vs_CtrlExo"]
chk("E1-N1 difference", round(obs_b, 4), dep_b["diff_hz_exo_minus_ctrl_exo"])
chk("E1-N1 perm P", round(p_b, 4), dep_b["perm_p"])
chk("E1-N1 Welch P", round(pw_b, 4), dep_b["welch_p"])
chk("E1-N1 diff vs manuscript -0.064", round(obs_b, 3), -0.064, tol=1e-3)
chk("E1-N1 perm P vs manuscript 0.178", round(p_b, 3), 0.178, tol=1e-3)
chk("E1-N1 Welch P vs manuscript 0.187", round(pw_b, 3), 0.187, tol=1e-3)

# ================= 9. E1 module Welch CI (manuscript 3.3: -0.38 to -0.06) =================
e1_mod = R1["contrasts"]["HZexo_vs_CtrlExo"]["E1_classical_nociceptor"]
a_m, b_m = sE1[ctrl].values, sE1[hz].values
t_m, pw_m = stats.ttest_ind(b_m, a_m, equal_var=False)
se_m = math.sqrt(a_m.var(ddof=1)/len(a_m) + b_m.var(ddof=1)/len(b_m))
df_m = se_m**4 / ((a_m.var(ddof=1)/len(a_m))**2/(len(a_m)-1) + (b_m.var(ddof=1)/len(b_m))**2/(len(b_m)-1))
ci_m = stats.ttest_ind(b_m, a_m, equal_var=False).confidence_interval(0.95)
print("\n=== 9. E1 module CI (HZ vs Ctrl) ===")
print(f"diff={b_m.mean()-a_m.mean():+.4f} Welch P={pw_m:.4f} CI95=[{ci_m.low:.4f}, {ci_m.high:.4f}] (df={df_m:.2f})")
chk("E1 module diff", round(b_m.mean()-a_m.mean(), 4), round(e1_mod["diff_B_minus_A"], 4))
chk("E1 module Welch P", round(pw_m, 4), round(e1_mod["p_ttest"], 4))
chk("E1 module CI low", round(ci_m.low, 3), round(e1_mod["ci95_welch"][0], 3), tol=1e-3)
chk("E1 module CI high", round(ci_m.high, 3), round(e1_mod["ci95_welch"][1], 3), tol=1e-3)
chk("E1 module CI low vs manuscript -0.38", round(ci_m.low, 2), -0.38, tol=6e-3)
chk("E1 module CI high vs manuscript -0.06", round(ci_m.high, 2), -0.06, tol=6e-3)

# ================= summary =================
n_pass = sum(1 for *_, ok in CHECKS if ok)
print(f"\n===== EDITOR VERIFY SUMMARY: {n_pass}/{len(CHECKS)} checks PASS =====")
for label, got, want, ok in CHECKS:
    if not ok:
        print(f"  FAIL: {label}: recomputed={got} reference={want}")
if n_pass != len(CHECKS):
    sys.exit(1)
print("All editor verification checks passed.")
