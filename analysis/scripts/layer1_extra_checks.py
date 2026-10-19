#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Layer 1 补充检验（Round 4 专家审稿新增，分析前未预指定 → 全部标记为 post hoc / 探索性）。

新增内容（均为审稿人提出、作者独立复算确认）：
  1. **E1 vs N1 基准检验**：E1 是否真的优于它自己的中性对照 N1（电压门控通道）。
     这是"通道类别选择性"能否成立的关键内部基准。
  2. **神经元完整性 / 损伤标志物**：ATF3 与神经元标志物面板，用于区分
     "特异性通道调控" 与 "非特异性轻度神经元反应 / 细胞毒性"。
  3. **TRPV1 在直接感染路径下的表现**：检验"路径依赖性"是方向性还是仅量级差异。
  4. **基线均值的两种分母口径**：DirectInf 全体 12 样本 vs 仅 mock 6 样本。
  5. **OR5A1 检测基线 + PIEZO2 基因级 95% CI**：补齐稿件中使用但此前无产物的数字。

输出：analysis/results/layer1/layer1_extra_checks.json  (纳入 MANIFEST)
"""
import gzip
import itertools
import json
import os
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

_ROOT = Path(__file__).resolve().parents[2]
RAW = _ROOT / "analysis" / "data" / "raw"
CFG = _ROOT / "analysis" / "config" / "mtp_panel.json"
OUT = _ROOT / "analysis" / "results" / "layer1" / "layer1_extra_checks.json"

PANEL = json.load(open(CFG, encoding="utf-8"))
MODS = {k: v["genes"] for k, v in PANEL.items() if isinstance(v, dict) and "genes" in v}


# ---------- 基础工具（自实现，不依赖 layer1_mechano.py） ----------
def load(fn):
    return pd.read_csv(gzip.open(RAW / fn, "rt"), index_col=0)


def log_cpm(mat):
    return np.log2(1 + mat / mat.sum(axis=0) * 1e6)


def perm_exact_p(values, n_a, observed):
    """枚举全部 C(n, n_a) 划分；values 已按 [A..., B...] 排列。双侧经验 P。"""
    n = len(values)
    diffs = []
    for comb in itertools.combinations(range(n), n_a):
        mask = np.zeros(n, dtype=bool)
        mask[list(comb)] = True
        diffs.append(values[mask].mean() - values[~mask].mean())
    diffs = np.asarray(diffs)
    return float(np.mean(np.abs(diffs) >= abs(observed) - 1e-12)), int(len(diffs))


def module_scores(L, genes):
    gs = [g for g in genes if g in L.index]
    return L.loc[gs].mean(axis=0), gs


def did_benchmark(L, groups, gA, gB, mod_x, mod_y):
    """模块 X 与模块 Y 的差值（(X-Y) 每样本），再做两组置换检验。"""
    a = [c for c in L.columns if groups[c] == gA]
    b = [c for c in L.columns if groups[c] == gB]
    sx, _ = module_scores(L[a + b], MODS[mod_x])
    sy, _ = module_scores(L[a + b], MODS[mod_y])
    d = (sx - sy).values
    obs = d[:len(a)].mean() - d[len(a):].mean()
    p, nperm = perm_exact_p(d, len(a), obs)
    w = stats.ttest_ind(d[:len(a)], d[len(a):], equal_var=False)
    return {"diff_%s_minus_%s" % (gA, gB): round(float(obs), 4),
            "perm_p": round(float(p), 4), "n_permutations": nperm,
            "welch_p": round(float(w.pvalue), 4),
            "mean_%s" % gA: round(float(d[:len(a)].mean()), 4),
            "mean_%s" % gB: round(float(d[len(a):].mean()), 4)}


def gene_contrast(L, groups, gA, gB, gene):
    a = [c for c in L.columns if groups[c] == gA]
    b = [c for c in L.columns if groups[c] == gB]
    va, vb = L.loc[gene, a].values, L.loc[gene, b].values
    t = stats.ttest_ind(va, vb, equal_var=False)
    ci = t.confidence_interval(0.95)
    return {"log2FC": round(float(va.mean() - vb.mean()), 4),
            "welch_p": round(float(t.pvalue), 4),
            "ci95": [round(float(ci.low), 3), round(float(ci.high), 3)],
            "mean_%s" % gA: round(float(va.mean()), 3),
            "mean_%s" % gB: round(float(vb.mean()), 3)}


def bh(ps):
    ps = np.asarray([p for p in ps if np.isfinite(p)], dtype=float)
    if len(ps) == 0:
        return []
    order = np.argsort(ps)
    q = np.empty_like(ps)
    prev = 1.0
    n = len(ps)
    for rank, i in enumerate(order[::-1]):
        prev = min(prev, ps[i] * n / (n - rank))
        q[i] = prev
    return q


# ---------- 载入 ----------
se = load("GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz")
di = load("GSE342782_Processed_DirectInf_neuronHD10s_BulkSeq_Counts.csv.gz")
L_se, L_di = log_cpm(se), log_cpm(di)
CPM_se = se / se.sum(axis=0) * 1e6
CPM_di = di / di.sum(axis=0) * 1e6

g_se = {c: ("ctrl_exo" if c.startswith("C") else "hz_exo" if c.startswith("S")
            else "phn_exo" if c.startswith("P") else None) for c in se.columns}
g_di = {c: ("mock" if "mock" in c else "vzv" if "vzv" in c else None) for c in di.columns}

res = {"note": "Post hoc / exploratory checks added after Round-4 peer review; "
               "not part of the pre-specified frozen analysis plan.",
       "panel_version": PANEL["panel_version"]}

# ---------- 1. E1 vs N1 基准 ----------
res["e1_vs_n1_benchmark"] = {
    "HZexo_vs_CtrlExo": did_benchmark(L_se, g_se, "hz_exo", "ctrl_exo",
                                      "E1_classical_nociceptor", "N1_voltage_gated_control"),
    "VZV_vs_Mock": did_benchmark(L_di, g_di, "vzv", "mock",
                                 "E1_classical_nociceptor", "N1_voltage_gated_control"),
}
res["e1_vs_n1_benchmark"]["HZexo_vs_CtrlExo"]["interpretation"] = (
    "E1 is not separable from its own neutral control N1 at the module level: "
    "the (E1 - N1) difference is small and non-significant.")

# ---------- 2. 神经元完整性 / 损伤标志物 ----------
markers = ["ATF3", "NEFH", "TUBB3", "NEFL", "PRPH", "NTRK1", "SPP1", "GAL", "TAC1", "CALCA"]
mk = {}
for g in markers:
    if g in L_se.index:
        mk[g] = gene_contrast(L_se, g_se, "hz_exo", "ctrl_exo", g)
    else:
        mk[g] = {"log2FC": None, "welch_p": None, "note": "absent from matrix"}
qs = bh([mk[g]["welch_p"] for g in markers if mk[g]["welch_p"] is not None])
i = 0
for g in markers:
    if mk[g]["welch_p"] is not None:
        mk[g]["bh_q_across_markers"] = round(float(qs[i]), 4)
        i += 1
res["neuronal_integrity_markers"] = {
    "contrast": "HZexo_vs_CtrlExo",
    "genes": mk,
    "interpretation": "ATF3 (injury marker) is unchanged, so the E1 shift is not attributable "
                      "to overt cytotoxicity; however several pan-neuronal markers also move "
                      "modestly, so a non-specific mild neuronal reaction cannot be excluded.",
}

# ---------- 3. TRPV1 在两条路径下的表现 ----------
trpv1 = {"HZexo_vs_CtrlExo": gene_contrast(L_se, g_se, "hz_exo", "ctrl_exo", "TRPV1"),
         "VZV_vs_Mock": gene_contrast(L_di, g_di, "vzv", "mock", "TRPV1")}
# TRPV1 在 E1 模块内的 BH q（两条路径各算一次）
for lab, (L, grp, gA, gB) in {
        "HZexo_vs_CtrlExo": (L_se, g_se, "hz_exo", "ctrl_exo"),
        "VZV_vs_Mock": (L_di, g_di, "vzv", "mock")}.items():
    genes = MODS["E1_classical_nociceptor"]
    ps = {}
    for g in genes:
        if g in L.index:
            a = [c for c in L.columns if grp[c] == gA]
            b = [c for c in L.columns if grp[c] == gB]
            t = stats.ttest_ind(L.loc[g, a].values, L.loc[g, b].values, equal_var=False)
            if np.isfinite(t.pvalue):
                ps[g] = float(t.pvalue)
    q = bh(list(ps.values()))
    qmap = dict(zip(ps.keys(), q))
    trpv1[lab]["q_within_E1"] = round(float(qmap.get("TRPV1", float("nan"))), 4)
res["trpv1_by_route"] = trpv1
res["trpv1_by_route"]["interpretation"] = (
    "TRPV1 mRNA falls under BOTH routes; the route dependence is one of magnitude "
    "(HZ-exo approximately -0.57 vs direct VZV approximately -0.15), not of direction.")

# ---------- 4. 基线均值两种分母口径 ----------
base = {}
for g in ["PIEZO2", "P2RX3", "ITGB1", "SCN9A", "TRPV1", "TRPV4", "STOML3"]:
    if g not in L_di.index:
        continue
    mock = [c for c in L_di.columns if g_di[c] == "mock"]
    base[g] = {
        "directinf_all12_mean_log2cpm": round(float(L_di.loc[g].mean()), 3),
        "directinf_mock_only_mean_log2cpm": round(float(L_di.loc[g, mock].mean()), 3),
        "directinf_all12_mean_cpm": round(float(CPM_di.loc[g].mean()), 2),
    }
res["baseline_denominators"] = {
    "note": "Manuscript section 3.1 previously mixed two denominators: PIEZO2/ITGB1/P2RX3 were "
            "all-12-sample means whereas SCN9A/TRPV1 were mock-only means.",
    "genes": base,
}

# ---------- 5. OR5A1 检测基线 + PIEZO2 基因级 CI ----------
det = {}
for g in ["OR5A1", "PIEZO2", "TRPV4", "STOML3", "SCN10A"]:
    if g not in L_se.index:
        continue
    det[g] = {"seraexo_mean_cpm": round(float(CPM_se.loc[g].mean()), 3),
              "seraexo_detected_fraction": round(float((CPM_se.loc[g] > 1).mean()), 3),
              "HZexo_vs_CtrlExo": gene_contrast(L_se, g_se, "hz_exo", "ctrl_exo", g)}
res["detection_baseline_extras"] = det

OUT.parent.mkdir(parents=True, exist_ok=True)
json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("written:", OUT)
print(json.dumps(res["e1_vs_n1_benchmark"], ensure_ascii=False, indent=2))
print(json.dumps({k: v for k, v in res["trpv1_by_route"].items() if k != "interpretation"},
                 ensure_ascii=False, indent=2))
