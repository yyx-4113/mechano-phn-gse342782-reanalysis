#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Layer 1 + W0：GSE342782 四维 mechano-score、CCI、置换零分布、组间比较。
v2 (2026-10-19, revision round 1)——相对 v1 的变更（均有评审报告驱动）：
  - perm_null: Monte-Carlo (B=5000) → 精确枚举全部 C(n1+n2, n1) 个标签置换，
    并移除 1/B 下限（PHN N3 的报点曾低于可达最小值 1/792）。
  - 新增 BH 步骤（8 模块族内、基于精确置换 P）→ results["bh_q"]，
    修复 v1 中 bh_q 无脚本产出的可复现性缺口。
  - 新增 contrast-of-contrasts 交互检验（外泌体实验内 E1 vs M1；直接感染实验内 M1 vs E1）。
  - 新增 MDE（80% 功效, non-central-t）与置换反转 CI、Welch CI。
  - 新增检出基因敏感性分析（module score 限制于 mean CPM>1 的基因）。
  - 新增 TAC1/CALCA/CALCB 观察项（来源研究的竞争性解释）。
  - 新增别名敏感性（M3: CYR61/CTGF → CCN1/CCN2；N3: RPS4 → RPS4X）。
  - baseline 键 mock_mean_log2cpm → directinf_all_mean_log2cpm（原键实为 12 样本全体均值）。
  - 新增落盘 layer1_gene_level.csv（全基因 Welch）与 layer1_global_de.csv（全局 DE 计数）。
  - 移除死代码 cci_per_sample。
纪律（不变）：
  - MTP panel 来自 analysis/config/mtp_panel.json（分析前冻结，事后未因结果增改）
  - 主对比 = HZ-exo vs control-exo（规避 PHN 供体年龄/性别混杂）
  - 所有 P 值同时给 t-test / Wilcoxon / 精确置换分位
  - 产物写 JSON + CSV，附 MANIFEST（sha256），不硬编码任何结论数字
"""
import json, gzip, os, hashlib, csv
import numpy as np
import pandas as pd
from scipy import stats
from itertools import combinations
from pathlib import Path

# 路径相对仓库根（analysis/scripts/ 上溯两级），避免绝对路径不可移植
_ROOT = Path(__file__).resolve().parents[2]
RAW = str(_ROOT / "analysis" / "data" / "raw")
OUT = str(_ROOT / "analysis" / "results" / "layer1")
CFG = str(_ROOT / "analysis" / "config" / "mtp_panel.json")
os.makedirs(OUT, exist_ok=True)

# ---------- 工具 ----------
def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

def load_counts(path):
    """读取 GEO 提供的 RSEM counts csv.gz，第一列 gene_symbol。"""
    rows = {}
    with gzip.open(path, "rt") as f:
        r = csv.reader(f)
        header = next(r)
        samples = [h for h in header[1:]]
        for row in r:
            g = row[0].strip()
            if not g or g.upper() in ("NA", "GENE_SYMBOL"):
                continue
            vals = []
            ok = True
            for v in row[1:]:
                try:
                    vals.append(float(v))
                except ValueError:
                    ok = False
                    break
            if not ok:
                continue
            if g in rows:  # 重复符号取首个
                continue
            rows[g] = vals
    df = pd.DataFrame(rows, index=samples).T
    df.index.name = "gene_symbol"
    return df

def to_cpm(df):
    s = df.sum(axis=0)
    return df.div(s, axis=1) * 1e6

def log2cpm(df):
    return np.log2(1 + to_cpm(df))

def module_score(L, genes, present):
    """返回每样本 module score（log2CPM 均值），仅用数据中存在的基因。"""
    g = [x for x in genes if x in present]
    if len(g) == 0:
        return None, 0
    return L.loc[g].mean(axis=0).values, len(g)

def perm_exact(diff_obs, sample_scores, idx_a, idx_b):
    """对一维每样本统计量（module score / CCI / 交互差分）精确枚举全部 C(n1+n2, n1) 个标签置换。
    返回 (p_two_sided, percentile, n_perm)。diff_obs 必须由同一数组按同样分组均值计算，
    以保证恒等 split 与观测值逐位一致；平局容差 1e-12 仅纳入精确相等的 split。"""
    values = np.asarray(sample_scores, dtype=float).ravel()
    pool = np.concatenate([idx_a, idx_b])
    na = len(idx_a)
    obs_abs = abs(diff_obs)
    dist = np.empty(0)
    dists = []
    for idx in combinations(range(len(pool)), na):
        a = values[pool[list(idx)]]
        mask = np.ones(len(pool), dtype=bool)
        mask[list(idx)] = False
        bb = values[pool[mask]]
        dists.append(bb.mean() - a.mean())
    dist = np.asarray(dists)
    p = float((np.abs(dist) >= obs_abs - 1e-12).mean())
    perc = float((dist <= diff_obs + 1e-12).mean() * 100)
    return p, perc, len(dist)

def mde_80(n1, n2, s_pooled, alpha=0.05, power=0.80):
    """两样本 t 检验（等方差近似）在 80% 功效下的最小可检测差（原始单位）。"""
    df = n1 + n2 - 2
    tcrit = stats.t.ppf(1 - alpha / 2, df)
    from scipy.optimize import brentq
    def pw(d):
        nc = d * np.sqrt(n1 * n2 / (n1 + n2))
        val = stats.nct.sf(tcrit, df, nc) + stats.nct.cdf(-tcrit, df, nc)
        return float(np.nan_to_num(val, nan=1.0)) - power
    d_req = brentq(pw, 0.01, 6.0)
    return float(d_req * s_pooled)

def perm_ci_inversion(diff_obs, values, idx_a, idx_b):
    """置换反转 95% CI：CI = [D - q975(null), D - q025(null)]，null 为精确枚举零分布。"""
    pool = np.concatenate([idx_a, idx_b])
    na = len(idx_a)
    dist = []
    for idx in combinations(range(len(pool)), na):
        a = pool[list(idx)]
        mask = np.ones(len(pool), dtype=bool)
        mask[list(idx)] = False
        bb = pool[mask]
        dist.append(values[bb].mean() - values[a].mean())
    dist = np.asarray(dist)
    lo = diff_obs - np.quantile(dist, 0.975)
    hi = diff_obs - np.quantile(dist, 0.025)
    return float(lo), float(hi)

def welch_ci(x, y):
    """Welch 95% CI（y.mean - x.mean）。"""
    vx, vy = x.var(ddof=1), y.var(ddof=1)
    nx, ny = len(x), len(y)
    se = np.sqrt(vx / nx + vy / ny)
    dfw = (vx / nx + vy / ny) ** 2 / ((vx / nx) ** 2 / (nx - 1) + (vy / ny) ** 2 / (ny - 1))
    tc = stats.t.ppf(0.975, dfw)
    d = y.mean() - x.mean()
    return float(d - tc * se), float(d + tc * se)

def bh(pvals):
    """Benjamini–Hochberg q 值（输入为同族 P 值列表）。"""
    p = np.asarray(pvals, dtype=float)
    n = len(p)
    order = np.argsort(p)
    ranked = p[order] * n / (np.arange(n) + 1)
    ranked = np.minimum.accumulate(ranked[::-1])[::-1]
    q = np.empty(n)
    q[order] = np.minimum(ranked, 1.0)
    return q

# ---------- 载入 panel ----------
with open(CFG) as f:
    PANEL = json.load(f)
MODULES = {k: v["genes"] for k, v in PANEL.items() if k not in ("panel_version", "note")}
MODULE_ORDER = ["M1_mechanogated_channels", "M2_membrane_cytoskeleton", "M3_ecm_integrin_hippo",
                "M4_mechano_effectors", "E1_classical_nociceptor", "N1_voltage_gated_control",
                "N2_olfactory_control", "N3_ribosomal_control"]

# ---------- 载入数据 ----------
di = load_counts(os.path.join(RAW, "GSE342782_Processed_DirectInf_neuronHD10s_BulkSeq_Counts.csv.gz"))
se = load_counts(os.path.join(RAW, "GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz"))

# 样本分组（严格按 GEO 系列矩阵 Sample_title）
di_groups = {}
for s in di.columns:
    if "mock" in s: di_groups[s] = "mock"
    elif "vzv" in s: di_groups[s] = "vzv"
se_groups = {}
for s in se.columns:
    # SeraExo 列名前缀：C=control(7), P=PHN(5), S=acute zoster(7)，与论文样本数吻合
    if s.startswith("C"): se_groups[s] = "ctrl_exo"
    elif s.startswith("P"): se_groups[s] = "phn_exo"
    elif s.startswith("S"): se_groups[s] = "hz_exo"
    else: se_groups[s] = None

print("DirectInf samples:", di.shape, "groups:", di_groups)
print("SeraExo samples:", se.shape, "groups:", se_groups)

# ---------- W0 体检：检测限 + HD10 基线 ----------
L_di = log2cpm(di)
L_se = log2cpm(se)
cpm_di = to_cpm(di)
cpm_se = to_cpm(se)

w0_genes = ["PIEZO1", "PIEZO2", "TRPV4", "STOML3", "ITGB1", "YAP1", "LOX", "MMP9", "SCN9A", "TRPV1", "P2RX3", "SCN10A", "TAC1", "COL1A1", "FN1"]
w0 = {}
for g in w0_genes:
    rec = {}
    for tag, cpm in [("DirectInf", cpm_di), ("SeraExo", cpm_se)]:
        if g in cpm.index:
            sub = cpm.loc[g]
            det = (sub > 1).mean()
            rec[tag] = {"mean_cpm": float(sub.mean()), "detect_frac_cpm1": float(det),
                        "mean_log2cpm": float(L_di.loc[g].mean()) if tag == "DirectInf" else float(L_se.loc[g].mean())}
        else:
            rec[tag] = None
    w0[g] = rec

# HD10 基线（DirectInf 全部 12 样本 = mock + VZV；键名如实反映样本范围）
_mock_cols = [c for c in di.columns if di_groups[c] == "mock"]
baseline = {}
for g in w0_genes:
    baseline[g] = {
        "directinf_all_mean_log2cpm": float(L_di.loc[g].mean()) if g in L_di.index else None,
        "directinf_mock_only_mean_log2cpm": float(L_di[_mock_cols].loc[g].mean()) if g in L_di.index else None,
        "seraexo_all_mean_log2cpm": float(L_se.loc[g].mean()) if g in L_se.index else None,
    }

# panel 基因在数据中缺失情况（含别名核查）
ALIAS = {"CYR61": "CCN1", "CTGF": "CCN2", "RPS4": "RPS4X"}
panel_missing = {}
alias_present = {}
for mod, genes in MODULES.items():
    miss = [g for g in genes if g not in L_di.index and g not in L_se.index]
    panel_missing[mod] = miss
    alias_present[mod] = {g: (ALIAS[g] if g in ALIAS and ALIAS[g] in L_se.index else None) for g in miss}

# ---------- Layer 1：模块 score + 组间比较 ----------
def compare(mat_log2cpm, groups, gA, gB, modname, genes):
    present = set(mat_log2cpm.index)
    gpresent = [x for x in genes if x in present]
    if len(gpresent) < 2:
        return None
    sub = mat_log2cpm.loc[gpresent]
    idx_a = [i for i, s in enumerate(mat_log2cpm.columns) if groups[s] == gA]
    idx_b = [i for i, s in enumerate(mat_log2cpm.columns) if groups[s] == gB]
    sa = sub.iloc[:, idx_a].mean(axis=1)
    sb = sub.iloc[:, idx_b].mean(axis=1)
    # 每个样本 module score（一维）；diff 与置换统计量均由此数组计算，保证 FP 一致
    sample_scores = sub.mean(axis=0).values
    all_scores_a = sample_scores[idx_a]
    all_scores_b = sample_scores[idx_b]
    diff_obs = all_scores_b.mean() - all_scores_a.mean()
    t, pt = stats.ttest_ind(all_scores_b, all_scores_a, equal_var=False)
    u, pu = stats.mannwhitneyu(all_scores_b, all_scores_a, alternative="two-sided")
    p_perm, perc, n_perm = perm_exact(diff_obs, sample_scores, idx_a, idx_b)
    # CI（置换反转 + Welch）与 MDE
    ci_lo, ci_hi = perm_ci_inversion(diff_obs, sample_scores, idx_a, idx_b)
    w_lo, w_hi = welch_ci(all_scores_a, all_scores_b)
    s_pooled = np.sqrt((all_scores_a.var(ddof=1) + all_scores_b.var(ddof=1)) / 2)
    mde = mde_80(len(idx_a), len(idx_b), s_pooled)
    return {
        "module": modname, "genes_used": len(gpresent), "genes_total": len(genes),
        "mean_A(%s)" % gA: float(sa.mean()), "mean_B(%s)" % gB: float(sb.mean()),
        "diff_B_minus_A": float(diff_obs),
        "sd_A": float(all_scores_a.std(ddof=1)), "sd_B": float(all_scores_b.std(ddof=1)),
        "sd_pooled": float(s_pooled),
        "t": float(t), "p_ttest": float(pt), "p_wilcoxon": float(pu),
        "p_perm_exact": float(p_perm), "perm_percentile": float(perc), "n_permutations": int(n_perm),
        "ci95_perm_inversion": [ci_lo, ci_hi], "ci95_welch": [w_lo, w_hi],
        "mde_80pct": float(mde),
        "top_genes": sorted(zip(gpresent, (sb - sa).values), key=lambda x: -abs(x[1]))[:8]
    }

contrasts = [
    # (experiment_log2cpm, groups, gA, gB, label)
    (L_se, se_groups, "ctrl_exo", "hz_exo", "HZexo_vs_CtrlExo"),
    (L_se, se_groups, "ctrl_exo", "phn_exo", "PHNexo_vs_CtrlExo"),
    (L_di, di_groups, "mock", "vzv", "VZV_vs_Mock"),
]
results = {"w0": w0, "baseline": baseline, "panel_missing": panel_missing,
           "alias_check": alias_present, "contrasts": {}}
for Lm, grp, gA, gB, lab in contrasts:
    results["contrasts"][lab] = {}
    for mod in MODULE_ORDER:
        c = compare(Lm, grp, gA, gB, mod, MODULES[mod])
        if c:
            results["contrasts"][lab][mod] = c

# ---------- BH（8 模块族内，基于精确置换 P） ----------
bh_q = {}
for lab, mods in results["contrasts"].items():
    labs_order = [m for m in MODULE_ORDER if m in mods]
    pv = [mods[m]["p_perm_exact"] for m in labs_order]
    qv = bh(pv)
    bh_q[lab] = {m: float(q) for m, q in zip(labs_order, qv)}
results["bh_q"] = bh_q

# ---------- CCI（通道互补指数）：M1 vs E1 在全部基因中的平均秩差 ----------
def cci_full(Lm, grp, gA, gB, lab):
    rank_mat = Lm.rank(axis=0, method="average")  # 每个样本内：基因按表达量在全矩阵上排秩
    m1 = [g for g in MODULES["M1_mechanogated_channels"] if g in Lm.index]
    e1 = [g for g in MODULES["E1_classical_nociceptor"] if g in Lm.index]
    if len(m1) < 2 or len(e1) < 2:
        return None
    cci = (rank_mat.loc[m1].mean(axis=0) - rank_mat.loc[e1].mean(axis=0)).values
    idx_a = [i for i, s in enumerate(Lm.columns) if grp[s] == gA]
    idx_b = [i for i, s in enumerate(Lm.columns) if grp[s] == gB]
    diff_obs = cci[idx_b].mean() - cci[idx_a].mean()
    t, pt = stats.ttest_ind(cci[idx_b], cci[idx_a], equal_var=False)
    u, pu = stats.mannwhitneyu(cci[idx_b], cci[idx_a], alternative="two-sided")
    p_perm, perc, n_perm = perm_exact(diff_obs, cci.reshape(1, -1), idx_a, idx_b)
    return {"contrast": lab, "m1_n": len(m1), "e1_n": len(e1),
            "rank_space": "all_%d_genes" % Lm.shape[0],
            "mean_CCI_A(%s)" % gA: float(cci[idx_a].mean()),
            "mean_CCI_B(%s)" % gB: float(cci[idx_b].mean()),
            "diff_B_minus_A": float(diff_obs),
            "p_ttest": float(pt), "p_wilcoxon": float(pu),
            "p_perm_exact": float(p_perm), "n_permutations": int(n_perm)}

results["CCI"] = {}
for Lm, grp, gA, gB, lab in contrasts:
    c = cci_full(Lm, grp, gA, gB, lab)
    if c:
        results["CCI"][lab] = c

# ---------- contrast-of-contrasts 交互检验 ----------
# 外泌体实验内：(E1_HZ - E1_ctrl) - (M1_HZ - M1_ctrl)
# 直接感染实验内：(M1_VZV - M1_mock) - (E1_VZV - E1_mock)
def interaction(Lm, grp, modX, modY, gA, gB, lab):
    """每样本 (X_score - Y_score) 的组间差 = X、Y 两模块差分之差。"""
    sx = Lm.loc[[g for g in MODULES[modX] if g in Lm.index]].mean(axis=0).values
    sy = Lm.loc[[g for g in MODULES[modY] if g in Lm.index]].mean(axis=0).values
    d = sx - sy
    idx_a = [i for i, s in enumerate(Lm.columns) if grp[s] == gA]
    idx_b = [i for i, s in enumerate(Lm.columns) if grp[s] == gB]
    diff_obs = d[idx_b].mean() - d[idx_a].mean()
    p_perm, perc, n_perm = perm_exact(diff_obs, d.reshape(1, -1), idx_a, idx_b)
    t, pt = stats.ttest_ind(d[idx_b], d[idx_a], equal_var=False)
    return {"contrast": lab, "modules": "%s_minus_%s" % (modX, modY),
            "diff_B_minus_A": float(diff_obs), "p_ttest": float(pt),
            "p_perm_exact": float(p_perm), "n_permutations": int(n_perm),
            "module_diffs": {modX: results["contrasts"][lab][modX]["diff_B_minus_A"],
                             modY: results["contrasts"][lab][modY]["diff_B_minus_A"]}}

results["interaction"] = {
    "HZexo_vs_CtrlExo": interaction(L_se, se_groups, "E1_classical_nociceptor", "M1_mechanogated_channels", "ctrl_exo", "hz_exo", "HZexo_vs_CtrlExo"),
    "VZV_vs_Mock": interaction(L_di, di_groups, "M1_mechanogated_channels", "E1_classical_nociceptor", "mock", "vzv", "VZV_vs_Mock"),
}

# ---------- 检出基因交互检验（公平性校正：限制于 mean CPM>1 的基因） ----------
# 全模块交互（E1-M1）因 M1 含 4/9 未检出基因（值≈0）而被稀释，使 E1 看似更被选择性抑制；
# 限制于检出基因后重新计算，以检验选择性是否真实存在（Round-2 B2 修正）。
def interaction_detected(Lm, cpm_df, grp, modX, modY, gA, gB, lab):
    gx_all = [g for g in MODULES[modX] if g in Lm.index]
    gy_all = [g for g in MODULES[modY] if g in Lm.index]
    gx = [g for g in gx_all if cpm_df.loc[g].mean() > 1]
    gy = [g for g in gy_all if cpm_df.loc[g].mean() > 1]
    if len(gx) < 2 or len(gy) < 2:
        return None
    sx = Lm.loc[gx].mean(axis=0).values
    sy = Lm.loc[gy].mean(axis=0).values
    d = sx - sy
    idx_a = [i for i, s in enumerate(Lm.columns) if grp[s] == gA]
    idx_b = [i for i, s in enumerate(Lm.columns) if grp[s] == gB]
    diff_obs = d[idx_b].mean() - d[idx_a].mean()
    p_perm, perc, n_perm = perm_exact(diff_obs, d.reshape(1, -1), idx_a, idx_b)
    return {"contrast": lab, "modules": "%s_minus_%s" % (modX, modY),
            "n_%s" % modX: len(gx), "n_%s" % modY: len(gy),
            "diff_B_minus_A": float(diff_obs), "p_perm_exact": float(p_perm),
            "n_permutations": int(n_perm)}

results["interaction_detected_only"] = {
    "HZexo_vs_CtrlExo": interaction_detected(L_se, cpm_se, se_groups, "E1_classical_nociceptor", "M1_mechanogated_channels", "ctrl_exo", "hz_exo", "HZexo_vs_CtrlExo"),
    "VZV_vs_Mock": interaction_detected(L_di, cpm_di, di_groups, "M1_mechanogated_channels", "E1_classical_nociceptor", "mock", "vzv", "VZV_vs_Mock"),
}

# ---------- 检出基因敏感性分析 ----------
def detected_sensitivity(Lm, cpm_df, grp, gA, gB, lab):
    """module score 限制于该实验内 mean CPM > 1 的基因；报告 M1/M2/M3/M4/E1。"""
    out = {}
    for mod in ["M1_mechanogated_channels", "M2_membrane_cytoskeleton", "M3_ecm_integrin_hippo",
                "M4_mechano_effectors", "E1_classical_nociceptor"]:
        genes_all = [g for g in MODULES[mod] if g in Lm.index]
        det = [g for g in genes_all if cpm_df.loc[g].mean() > 1]
        if len(det) < 2:
            continue
        sub = Lm.loc[det]
        idx_a = [i for i, s in enumerate(Lm.columns) if grp[s] == gA]
        idx_b = [i for i, s in enumerate(Lm.columns) if grp[s] == gB]
        scores = sub.mean(axis=0).values
        diff_obs = scores[idx_b].mean() - scores[idx_a].mean()
        p_perm, perc, n_perm = perm_exact(diff_obs, scores, idx_a, idx_b)
        out[mod] = {"genes_used": len(det), "genes_total": len(genes_all),
                    "diff_B_minus_A": float(diff_obs), "p_perm_exact": float(p_perm)}
    return out

results["sensitivity_detected_genes"] = {
    "HZexo_vs_CtrlExo": detected_sensitivity(L_se, cpm_se, se_groups, "ctrl_exo", "hz_exo", "HZexo_vs_CtrlExo"),
    "PHNexo_vs_CtrlExo": detected_sensitivity(L_se, cpm_se, se_groups, "ctrl_exo", "phn_exo", "PHNexo_vs_CtrlExo"),
    "VZV_vs_Mock": detected_sensitivity(L_di, cpm_di, di_groups, "mock", "vzv", "VZV_vs_Mock"),
}

# ---------- 别名敏感性（M3 58 基因版：CYR61→CCN1, CTGF→CCN2） ----------
m3_alias = {}
for lab, Lm, grp, gA, gB in [("HZexo_vs_CtrlExo", L_se, se_groups, "ctrl_exo", "hz_exo"),
                              ("PHNexo_vs_CtrlExo", L_se, se_groups, "ctrl_exo", "phn_exo"),
                              ("VZV_vs_Mock", L_di, di_groups, "mock", "vzv")]:
    genes58 = [ALIAS.get(g, g) for g in MODULES["M3_ecm_integrin_hippo"]]
    genes58 = [g for g in genes58 if g in Lm.index]
    sub = Lm.loc[genes58]
    idx_a = [i for i, s in enumerate(Lm.columns) if grp[s] == gA]
    idx_b = [i for i, s in enumerate(Lm.columns) if grp[s] == gB]
    scores = sub.mean(axis=0).values
    diff_obs = scores[idx_b].mean() - scores[idx_a].mean()
    p_perm, _, n_perm = perm_exact(diff_obs, scores, idx_a, idx_b)
    m3_alias[lab] = {"genes_used": len(genes58), "diff_B_minus_A": float(diff_obs), "p_perm_exact": float(p_perm)}
results["sensitivity_m3_alias_ccn1_ccn2"] = m3_alias

# ---------- 神经肽观察（来源研究的竞争性解释；非冻结 panel 内容） ----------
neuropep = {}
for lab, Lm, grp, gA, gB in [("HZexo_vs_CtrlExo", L_se, se_groups, "ctrl_exo", "hz_exo"),
                              ("PHNexo_vs_CtrlExo", L_se, se_groups, "ctrl_exo", "phn_exo")]:
    idx_a = [i for i, s in enumerate(Lm.columns) if grp[s] == gA]
    idx_b = [i for i, s in enumerate(Lm.columns) if grp[s] == gB]
    rec = {}
    for g in ["TAC1", "CALCA", "CALCB", "TACR1"]:
        if g not in Lm.index:
            rec[g] = None
            continue
        a = Lm.loc[g].values[idx_a]; b = Lm.loc[g].values[idx_b]
        t, pt = stats.ttest_ind(b, a, equal_var=False)
        rec[g] = {"mean_A": float(a.mean()), "mean_B": float(b.mean()),
                  "diff_B_minus_A": float(b.mean() - a.mean()), "p_ttest": float(pt),
                  "mean_cpm_B": float(cpm_se.loc[g].values[idx_b].mean())}
    neuropep[lab] = rec
results["neuropeptide_observation"] = neuropep

# ---------- 基因级 Welch（全基因，描述性） + 全局 DE 计数 ----------
gene_rows = []
global_de = []
for Lm, grp, gA, gB, lab, cpm_df in [(L_se, se_groups, "ctrl_exo", "hz_exo", "HZexo_vs_CtrlExo", cpm_se),
                                      (L_se, se_groups, "ctrl_exo", "phn_exo", "PHNexo_vs_CtrlExo", cpm_se),
                                      (L_di, di_groups, "mock", "vzv", "VZV_vs_Mock", cpm_di)]:
    idx_a = [i for i, s in enumerate(Lm.columns) if grp[s] == gA]
    idx_b = [i for i, s in enumerate(Lm.columns) if grp[s] == gB]
    A = Lm.iloc[:, idx_a].values
    B = Lm.iloc[:, idx_b].values
    d = B.mean(axis=1) - A.mean(axis=1)
    t, p = stats.ttest_ind(B.T, A.T, axis=0, equal_var=False)
    for i, g in enumerate(Lm.index):
        gene_rows.append({"contrast": lab, "gene": g, "log2FC": round(float(d[i]), 4), "welch_p": float(p[i])})
    global_de.append({"contrast": lab, "threshold": "|log2FC|>0.5",
                      "n_up": int((d > 0.5).sum()), "n_down": int((d < -0.5).sum()),
                      "n_nominal_p_lt_0.05": int((p < 0.05).sum()), "n_genes": int(len(d))})

# ---------- 写出 ----------
res_path = os.path.join(OUT, "layer1_results.json")
with open(res_path, "w") as f:
    json.dump(results, f, indent=2, default=str)

# 摘要 CSV（每对比每模块一行）
rows = []
for lab, mods in results["contrasts"].items():
    for mod in MODULE_ORDER:
        if mod not in mods:
            continue
        c = mods[mod]
        rows.append({"contrast": lab, "module": mod, "genes_used": c["genes_used"],
                     "diff": round(c["diff_B_minus_A"], 4),
                     "p_ttest": c["p_ttest"], "p_wilcoxon": c["p_wilcoxon"], "p_perm_exact": c["p_perm_exact"],
                     "q_bh": bh_q[lab][mod], "perm_pct": round(c["perm_percentile"], 1),
                     "ci95_perm_lo": round(c["ci95_perm_inversion"][0], 4),
                     "ci95_perm_hi": round(c["ci95_perm_inversion"][1], 4),
                     "mde_80pct": round(c["mde_80pct"], 4)})
csv_path = os.path.join(OUT, "layer1_module_scores.csv")
pd.DataFrame(rows).to_csv(csv_path, index=False)

cci_rows = []
for lab, c in results["CCI"].items():
    cci_rows.append({"contrast": lab, "diff_CCI": round(c["diff_B_minus_A"], 4),
                     "p_ttest": c["p_ttest"], "p_wilcoxon": c["p_wilcoxon"], "p_perm_exact": c["p_perm_exact"]})
pd.DataFrame(cci_rows).to_csv(os.path.join(OUT, "layer1_cci.csv"), index=False)

gene_csv = os.path.join(OUT, "layer1_gene_level.csv")
pd.DataFrame(gene_rows).to_csv(gene_csv, index=False)
global_csv = os.path.join(OUT, "layer1_global_de.csv")
pd.DataFrame(global_de).to_csv(global_csv, index=False)

# MANIFEST（内层：本目录全部结果产物）
manifest = {
    "layer1_results.json": sha256(res_path),
    "layer1_module_scores.csv": sha256(csv_path),
    "layer1_cci.csv": sha256(os.path.join(OUT, "layer1_cci.csv")),
    "layer1_gene_level.csv": sha256(gene_csv),
    "layer1_global_de.csv": sha256(global_csv),
    "layer1_diag.json": sha256(os.path.join(OUT, "layer1_diag.json")),
    "inputs": {
        "DirectInf": sha256(os.path.join(RAW, "GSE342782_Processed_DirectInf_neuronHD10s_BulkSeq_Counts.csv.gz")),
        "SeraExo": sha256(os.path.join(RAW, "GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz")),
        "panel": sha256(CFG),
    }
}
with open(os.path.join(OUT, "MANIFEST.json"), "w") as f:
    json.dump(manifest, f, indent=2)

print("\n=== W0 关键检测限（DirectInf=mock/VZV 神经元；SeraExo=外泌体处理）===")
for g in ["PIEZO2", "P2RX3", "PIEZO1", "TRPV4", "STOML3", "ITGB1", "SCN10A", "SCN9A", "TRPV1", "TAC1"]:
    w = w0[g]
    di_r = w.get("DirectInf"); se_r = w.get("SeraExo")
    print("  %-8s DI_detFrac=%s meanCPM=%s | SE_detFrac=%s meanCPM=%s" % (
        g,
        ("%.2f" % di_r["detect_frac_cpm1"]) if di_r else "NA",
        ("%.2f" % di_r["mean_cpm"]) if di_r else "NA",
        ("%.2f" % se_r["detect_frac_cpm1"]) if se_r else "NA",
        ("%.2f" % se_r["mean_cpm"]) if se_r else "NA"))

print("\n=== Layer 1 主对比 HZexo_vs_CtrlExo（精确枚举置换）===")
for mod in MODULE_ORDER:
    c = results["contrasts"]["HZexo_vs_CtrlExo"][mod]
    print("  %-30s diff=%+.4f  p_exact=%.4g  q=%.4g  MDE=%.4f" % (
        mod, c["diff_B_minus_A"], c["p_perm_exact"], bh_q["HZexo_vs_CtrlExo"][mod], c["mde_80pct"]))

print("\n=== 交互检验（contrast-of-contrasts）===")
for lab, c in results["interaction"].items():
    print("  %-22s %-40s diff=%+.4f  p_exact=%.4g" % (lab, c["modules"], c["diff_B_minus_A"], c["p_perm_exact"]))

print("\n=== 检出基因交互检验（公平性校正：限定 CPM>1）===")
for lab, c in results["interaction_detected_only"].items():
    if c is None:
        print("  %s: skipped (insufficient detected genes)" % lab); continue
    print("  %-22s nE1=%d nM1=%d diff=%+.4f p_exact=%.4g" % (lab, c.get("n_E1_classical_nociceptor"), c.get("n_M1_mechanogated_channels"), c["diff_B_minus_A"], c["p_perm_exact"]))

print("\n=== 检出基因敏感性 ===")
for lab, mods in results["sensitivity_detected_genes"].items():
    for mod, c in mods.items():
        print("  %-22s %-30s n=%2d diff=%+.4f p_exact=%.4g" % (lab, mod, c["genes_used"], c["diff_B_minus_A"], c["p_perm_exact"]))

print("\n=== 别名敏感性 M3(58) ===")
for lab, c in m3_alias.items():
    print("  %-22s n=%d diff=%+.4f p_exact=%.4g" % (lab, c["genes_used"], c["diff_B_minus_A"], c["p_perm_exact"]))

print("\n=== 神经肽观察 ===")
for lab, rec in neuropep.items():
    print(" ", lab, {g: (None if v is None else round(v["diff_B_minus_A"], 4)) for g, v in rec.items()})

print("\n=== CCI（M1 vs E1 平均秩差，全基因秩空间）===")
for lab, c in results["CCI"].items():
    print("  %-22s diffCCI=%+.4f  p_exact=%.4g" % (lab, c["diff_B_minus_A"], c["p_perm_exact"]))

print("\n=== 全局 DE ===")
for r in global_de:
    print("  %-22s up=%d down=%d nominalP<0.05=%d/%d" % (r["contrast"], r["n_up"], r["n_down"], r["n_nominal_p_lt_0.05"], r["n_genes"]))

print("\nDONE. results ->", OUT)
