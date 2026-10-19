#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Round-2 revision (v1.1.7) additional analyses, computed from raw GEO counts.

Deposits: analysis/results/layer1/layer1_round2_additions.json

Contents (all editor-verified before entering the manuscript):
  A. route_by_module_didid   — formal route x program interaction (E1-M1 composite, same orientation)
  B. m4_route_difference     — M4 route difference (removes significant-vs-not juxtaposition)
  C. cci_detected_only       — CCI restricted to detected genes (+ decomposition facts)
  D. cci_counterfactual      — CCI sensitivity to a uniform E1 shift
  E. e1_core_sensitivity     — canonical 13-channel E1 robustness
  F. ptk2_overlap_sensitivity— M3/M4 minus PTK2 (disclosed panel overlap)
  G. bh_table_hz             — all eight BH q values for the primary contrast
  H. within_m2_survivors     — EZR/PXN within-M2 BH survivors

Rank convention for CCI matches layer1_results.json: ascending ranks
(rank 1 = lowest expression), CCI = mean rank(M1) - mean rank(E1).
"""
import gzip, itertools, json, math, os
import pandas as pd
import numpy as np
from scipy import stats

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW = os.path.join(ROOT, "analysis", "data", "raw")
OUT = os.path.join(ROOT, "analysis", "results", "layer1")
SERA = os.path.join(RAW, "GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz")
DI = os.path.join(RAW, "GSE342782_Processed_DirectInf_neuronHD10s_BulkSeq_Counts.csv.gz")
PANEL = os.path.join(ROOT, "analysis", "config", "mtp_panel.json")

def load(p):
    return pd.read_csv(p, sep=",", index_col=0)

def L(df):
    cpm = df.div(df.sum(axis=0), axis=1) * 1e6
    return np.log2(1 + cpm)

sera = load(SERA); di = load(DI)
sL, dL = L(sera), L(di)
sera_cpm = sera.div(sera.sum(axis=0), axis=1) * 1e6
panel = json.load(open(PANEL, encoding="utf-8"))
mods = {k: list(v["genes"]) for k, v in panel.items() if isinstance(v, dict) and "genes" in v}
E1 = [g for g in mods[[k for k in mods if k.startswith("E1")][0]] if g in sL.index]
M1 = [g for g in mods[[k for k in mods if k.startswith("M1")][0]] if g in sL.index]
M3 = [g for g in mods[[k for k in mods if k.startswith("M3")][0]] if g in sL.index]
M4 = [g for g in mods[[k for k in mods if k.startswith("M4")][0]] if g in sL.index]
M2 = [g for g in mods[[k for k in mods if k.startswith("M2")][0]] if g in sL.index]
N3 = [g for g in mods[[k for k in mods if k.startswith("N3")][0]] if g in sL.index]
N1 = [g for g in mods[[k for k in mods if k.startswith("N1")][0]] if g in sL.index]
N2 = [g for g in mods[[k for k in mods if k.startswith("N2")][0]] if g in sL.index]

hz = [c for c in sera.columns if c.startswith("S")]
ctrl = [c for c in sera.columns if c.startswith("C")]
phn = [c for c in sera.columns if c.startswith("P")]
vzv = [c for c in di.columns if c.startswith("vzv")]
mock = [c for c in di.columns if c.startswith("mock")]

def perm_p(x, y):
    """Exact two-sided permutation P (full enumeration)."""
    n1, n2 = len(x), len(y)
    assert math.comb(n1 + n2, n1) <= 5_000_000
    obs = x.mean() - y.mean()
    both = np.concatenate([x, y])
    idx = range(n1 + n2)
    cnt = 0
    for comb in itertools.combinations(idx, n1):
        s = set(comb)
        g1 = np.array([both[i] for i in comb])
        g2 = np.array([both[i] for i in idx if i not in s])
        if abs(g1.mean() - g2.mean()) >= abs(obs) - 1e-12:
            cnt += 1
    return obs, cnt / math.comb(n1 + n2, n1)

def bh_q(pvals, labels):
    order = sorted(range(len(pvals)), key=lambda i: pvals[i])
    m = len(pvals)
    raw = [pvals[i] * m / (r + 1) for r, i in enumerate(order)]
    q = [0.0] * m
    q[-1] = min(1.0, raw[-1])
    for r in range(m - 2, -1, -1):
        q[r] = min(1.0, raw[r], q[r + 1])
    return {labels[i]: q[r] for r, i in enumerate(order)}

out = {}

# ---------- A. route x module DiDiD (consistent orientation) ----------
def composite(L, gA, gB, cols):
    a = L.loc[gA, cols].mean(axis=0)
    b = L.loc[gB, cols].mean(axis=0)
    return (a - b).values

cx_e = composite(sL, E1, M1, ctrl); sx_e = composite(sL, E1, M1, hz)
cx_i = composite(dL, E1, M1, mock); vx_i = composite(dL, E1, M1, vzv)
did_e = sx_e.mean() - cx_e.mean()
did_i = vx_i.mean() - cx_i.mean()
did_diff = did_e - did_i
be = np.concatenate([sx_e, cx_e]); bi = np.concatenate([vx_i, cx_i])
de_list = []
for ce in itertools.combinations(range(14), 7):
    s = set(ce)
    g1 = np.array([be[i] for i in ce]); g2 = np.array([be[i] for i in range(14) if i not in s])
    de_list.append(g1.mean() - g2.mean())
de_arr = np.array(de_list)
cnt = 0; tot = 0
for ci in itertools.combinations(range(12), 6):
    s = set(ci)
    g1 = np.array([bi[i] for i in ci]); g2 = np.array([bi[i] for i in range(12) if i not in s])
    d = g1.mean() - g2.mean()
    tot += 1
    cnt += int(np.sum(np.abs(de_arr - d) >= abs(did_diff) - 1e-12))
out["route_by_module_didid"] = {
    "composite": "E1 module score minus M1 module score, same orientation in both routes",
    "did_exosome": round(float(did_e), 4),
    "did_direct_infection": round(float(did_i), 4),
    "difference": round(float(did_diff), 4),
    "exact_perm_P": round(cnt / (tot * 3432), 5),
    "n_extreme": cnt, "n_null_partitions": tot * 3432,
    "note": "product of the two independent exact nulls (3432 x 924); SCN10A contributes to E1 only in the infection experiment",
}

# ---------- B. M4 route difference ----------
def mod_cols(L, genes, cols):
    return L.loc[[g for g in genes if g in L.index], cols].mean(axis=0).values
e4h = mod_cols(sL, M4, hz); e4c = mod_cols(sL, M4, ctrl)
i4v = mod_cols(dL, M4, vzv); i4m = mod_cols(dL, M4, mock)
d4e = e4h.mean() - e4c.mean(); d4i = i4v.mean() - i4m.mean(); d4diff = d4e - d4i
b4e = np.concatenate([e4h, e4c]); b4i = np.concatenate([i4v, i4m])
de4 = []
for ce in itertools.combinations(range(14), 7):
    s = set(ce)
    g1 = np.array([b4e[i] for i in ce]); g2 = np.array([b4e[i] for i in range(14) if i not in s])
    de4.append(g1.mean() - g2.mean())
de4 = np.array(de4)
cnt4 = 0; tot4 = 0
for ci in itertools.combinations(range(12), 6):
    s = set(ci)
    g1 = np.array([b4i[i] for i in ci]); g2 = np.array([b4i[i] for i in range(12) if i not in s])
    d = g1.mean() - g2.mean()
    tot4 += 1
    cnt4 += int(np.sum(np.abs(de4 - d) >= abs(d4diff) - 1e-12))
out["m4_route_difference"] = {
    "diff_exosome": round(float(d4e), 4), "diff_infection": round(float(d4i), 4),
    "route_difference": round(float(d4diff), 4),
    "exact_perm_P": round(cnt4 / (tot4 * 3432), 4),
    "n_extreme": cnt4, "n_null_partitions": tot4 * 3432,
}

# ---------- C. detected-gene CCI + decomposition ----------
def cci_per_sample(L, cpm, gA, gB):
    """CCI per sample; ascending ranks over all genes; mean rank(M1) - mean rank(E1)."""
    asc = L.rank(axis=0, ascending=True, method="average")
    a = asc.loc[gA].mean(axis=0)
    b = asc.loc[gB].mean(axis=0)
    return (a - b)

def cci_detected(L, cpm, gA, gB):
    asc = L.rank(axis=0, ascending=True, method="average")
    ad = [g for g in gA if cpm.loc[g].mean() > 1]
    bd = [g for g in gB if cpm.loc[g].mean() > 1]
    return asc.loc[ad].mean(axis=0) - asc.loc[bd].mean(axis=0), len(ad), len(bd)

full = cci_per_sample(sL, sera_cpm, M1, E1)
obs_full, p_full = perm_p(full[hz].values, full[ctrl].values)
det, n_ad, n_bd = cci_detected(sL, sera_cpm, M1, E1)
obs_det, p_det = perm_p(det[hz].values, det[ctrl].values)
# rank displacement decomposition (descending ranks; positive = moved downward)
desc = sL.rank(axis=0, ascending=False, method="average")
disp_e1 = desc.loc[E1, hz].mean(axis=1) - desc.loc[E1, ctrl].mean(axis=1)
disp_m1 = desc.loc[M1, hz].mean(axis=1) - desc.loc[M1, ctrl].mean(axis=1)
trpa1 = "TRPA1"
disp_trpa1 = desc.loc[trpa1, hz].mean() - desc.loc[trpa1, ctrl].mean()
# top E1 downward displacements
top_e1 = disp_e1.sort_values(ascending=False).head(4)
out["cci_detected_only"] = {
    "n_m1_detected": n_ad, "n_e1_detected": n_bd,
    "m1_detected": [g for g in M1 if sera_cpm.loc[g].mean() > 1],
    "e1_detected": [g for g in E1 if sera_cpm.loc[g].mean() > 1],
    "difference": round(float(obs_det), 1), "exact_perm_P": round(float(p_det), 4),
    "full_set_difference": round(float(obs_full), 1), "full_set_perm_P": round(float(p_full), 4),
    "e1_mean_rank_displacement_down": round(float(disp_e1.mean()), 0),
    "m1_mean_rank_displacement_down": round(float(disp_m1.mean()), 0),
    "trpa1_mean_rank_displacement_down": round(float(disp_trpa1), 0),
    "trpa1_cpm_ctrl": round(float(sera_cpm.loc[trpa1, ctrl].mean()), 4),
    "trpa1_cpm_hz": round(float(sera_cpm.loc[trpa1, hz].mean()), 4),
    "top_e1_downward": {g: round(float(v), 0) for g, v in top_e1.items()},
}

# ---------- D. CCI counterfactual: uniform -0.2196 shift imposed on E1 of HZ ----------
shift = -0.2196
sL2 = sL.copy()
sL2.loc[E1, hz] = sL2.loc[E1, hz] + shift
asc2 = sL2.rank(axis=0, ascending=True, method="average")
cf = asc2.loc[M1].mean(axis=0) - asc2.loc[E1].mean(axis=0)
obs_cf, p_cf = perm_p(cf[hz].values, cf[ctrl].values)
out["cci_counterfactual_uniform_e1_shift"] = {
    "imposed_shift_log2cpm": shift,
    "cci_difference": round(float(obs_cf), 0), "exact_perm_P": round(float(p_cf), 5),
}

# ---------- E. E1-core sensitivity ----------
E1CORE = ["SCN9A", "SCN10A", "SCN11A", "TRPV1", "TRPM8", "ASIC1", "ASIC2", "ASIC3",
          "KCNS1", "KCNQ2", "KCNQ3", "CACNA2D1", "CACNA2D2"]
ec = [g for g in E1CORE if g in sL.index]
score = sL.loc[ec].mean(axis=0)
a, b = score[ctrl].values, score[hz].values
t, pw = stats.ttest_ind(b, a, equal_var=False)
obs, pp = perm_p(b, a)
det_ec = [g for g in ec if sera_cpm.loc[g].mean() > 1]
score_d = sL.loc[det_ec].mean(axis=0)
obs_d, pp_d = perm_p(score_d[hz].values, score_d[ctrl].values)
se_ec = math.sqrt(a.var(ddof=1) / len(a) + b.var(ddof=1) / len(b))
df_ec = se_ec**4 / ((a.var(ddof=1) / len(a))**2 / (len(a) - 1) + (b.var(ddof=1) / len(b))**2 / (len(b) - 1))
ci_w = stats.t.interval(0.95, df_ec, loc=b.mean() - a.mean(), scale=se_ec)
out["e1_core_sensitivity"] = {
    "genes": ec, "n_genes": len(ec),
    "difference": round(float(b.mean() - a.mean()), 4),
    "welch_P": round(float(pw), 4), "exact_perm_P": round(float(pp), 4),
    "welch_ci95": [round(float(ci_w[0]), 3), round(float(ci_w[1]), 3)],
    "welch_ci95_df": round(float(df_ec), 2),
    "detected_only_n": len(det_ec),
    "detected_only_difference": round(float(obs_d), 4),
    "detected_only_perm_P": round(float(pp_d), 4),
    "label": "post hoc robustness analysis; not part of the frozen panel",
}

# ---------- F. PTK2 overlap sensitivities ----------
m3_no = [g for g in M3 if g != "PTK2"]; m4_no = [g for g in M4 if g != "PTK2"]
s3 = sL.loc[m3_no].mean(axis=0); s4 = sL.loc[m4_no].mean(axis=0)
o3, p3 = perm_p(s3[hz].values, s3[ctrl].values)
o4, p4 = perm_p(s4[hz].values, s4[ctrl].values)
out["ptk2_overlap_sensitivity"] = {
    "m3_minus_ptk2": {"difference": round(float(o3), 4), "exact_perm_P": round(float(p3), 3), "n_genes": len(m3_no)},
    "m4_minus_ptk2": {"difference": round(float(o4), 4), "exact_perm_P": round(float(p4), 3), "n_genes": len(m4_no)},
    "note": "PTK2 is a member of both M3 and M4 in the frozen panel",
}

# ---------- G. BH table, primary contrast ----------
mnames = list(mods.keys())
pv = {}
for m in mnames:
    sc = sL.loc[[g for g in mods[m] if g in sL.index]].mean(axis=0)
    obs_m, p_m = perm_p(sc[hz].values, sc[ctrl].values)
    pv[m] = {"diff": round(float(obs_m), 4), "p_perm_exact": round(float(p_m), 4),
             "n_genes": len([g for g in mods[m] if g in sL.index])}
qtab = bh_q([pv[m]["p_perm_exact"] for m in mnames], mnames)
for m in mnames:
    pv[m]["bh_q"] = round(qtab[m], 4)
out["bh_table_hz_contrast"] = pv

# ---------- H. within-M2 BH survivors ----------
res = []
for g in [x for x in M2 if x in sL.index]:
    a, b = sL.loc[g, ctrl].values, sL.loc[g, hz].values
    t, p = stats.ttest_ind(b, a, equal_var=False)
    res.append((g, b.mean() - a.mean(), p))
order = sorted(range(len(res)), key=lambda i: res[i][2])
mq = bh_q([r[2] for r in res], [r[0] for r in res])
out["within_m2_survivors"] = {
    g: {"log2fc": round(res[i][1], 4), "welch_P": round(res[i][2], 5), "q_within_M2": round(mq[g], 4)}
    for g, i in zip([r[0] for r in res], range(len(res))) if mq[g] < 0.05
}
out["within_m2_n_tested"] = len(res)

# ---------- write ----------
path = os.path.join(OUT, "layer1_round2_additions.json")
with open(path, "w", encoding="utf-8") as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
print(json.dumps(out, indent=1, ensure_ascii=False)[:4000])
print("written:", path)
