#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""归一化稳健性检验（Round-4 审稿新增，post hoc）。

背景：HZ 外泌体组出现核糖体基因（N3）显著诱导（+0.391, P = 0.0017），
核糖体转录本占文库比例上升会组成性稀释非核糖体基因，可能人为制造"普遍下调"。
本脚本用 DESeq2 风格的 median-of-ratios (MoR) 归一化重跑主对比，检验
E1 信号是否为归一化假象。

注意：CPM 是尺度不变的 —— 先做 MoR 再算 CPM 会得到与直接 CPM 完全相同的
结果（假对比）。因此本脚本把两种方案放到**同一量纲**下比较：
  方案 A（默认）：library-size CPM -> log2(1+CPM)
  方案 B（MoR）  ：counts / MoR size factor -> CPM -> log2(1+CPM)
两者都用 size factor 校正后的计数再算 CPM，量纲一致，差异才真实反映归一化选择。

输出：analysis/results/layer1/layer1_norm_robustness.json（纳入 MANIFEST）
"""
import gzip
import itertools
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

_ROOT = Path(__file__).resolve().parents[2]
RAW = _ROOT / "analysis" / "data" / "raw"
CFG = _ROOT / "analysis" / "config" / "mtp_panel.json"
OUT = _ROOT / "analysis" / "results" / "layer1" / "layer1_norm_robustness.json"

PANEL = json.load(open(CFG, encoding="utf-8"))
MODS = {k: v["genes"] for k, v in PANEL.items() if isinstance(v, dict) and "genes" in v}


def perm_exact_p(values, n_a, observed):
    n = len(values)
    diffs = []
    for comb in itertools.combinations(range(n), n_a):
        m = np.zeros(n, dtype=bool)
        m[list(comb)] = True
        diffs.append(values[m].mean() - values[~m].mean())
    diffs = np.asarray(diffs)
    return float(np.mean(np.abs(diffs) >= abs(observed) - 1e-12)), int(len(diffs))


def mor_size_factors(counts):
    """DESeq2 median-of-ratios：仅用所有样本中计数均 > 0 的基因。"""
    c = counts.values.astype(float)
    keep = np.all(c > 0, axis=1)
    logc = np.log(c[keep])
    ref = logc.mean(axis=1, keepdims=True)          # 几何均值参考
    ratios = logc - ref
    sf = np.exp(np.median(ratios, axis=0))
    return sf, int(keep.sum())


def build(counts, sf=None):
    """mode A (sf=None): log2(1 + CPM)，CPM = count / libsize * 1e6
       mode B (sf given): log2(1 + count / sf_cpm)，sf_cpm 为**缩放到 CPM 量纲**的
       median-of-ratios size factor。

    两个陷阱（本次都踩过并修正，务必保持）：
      1) 不要写成"MoR 归一化后再算 CPM" —— CPM 尺度不变，会得到与方案 A
         逐位相同的结果（假对比，什么都检验不出来）。
      2) 不要直接对原始计数取 log2(1 + count/sf) —— count/sf 与 CPM 相差
         约 5 个数量级，+1 伪计数在低表达基因上占主导，会把效应严重压缩
         （实测 E1 因此从 -0.219 歪到 -0.345）。必须先把 sf 缩放到与
         CPM 同量纲，两种方案的差异才只反映归一化选择本身。"""
    c = counts.values.astype(float)
    libsize = c.sum(axis=0)
    if sf is None:
        scaled = c / libsize * 1e6
    else:
        sf_cpm = sf / np.exp(np.mean(np.log(sf))) * (np.exp(np.mean(np.log(libsize))) / 1e6)
        scaled = c / sf_cpm
    return pd.DataFrame(np.log2(1 + scaled), index=counts.index, columns=counts.columns)


def contrast(L, groups, gA, gB, genes):
    a = [c for c in L.columns if groups[c] == gA]
    b = [c for c in L.columns if groups[c] == gB]
    gs = [g for g in genes if g in L.index]
    s = L.loc[gs].mean(axis=0)
    va, vb = s[a].values, s[b].values
    diff = float(va.mean() - vb.mean())
    lab = np.array([1] * len(a) + [0] * len(b))
    p, nperm = perm_exact_p(s[a + b].values, len(a), diff)
    return {"diff": round(diff, 4), "perm_p": round(p, 4),
            "welch_p": round(float(stats.ttest_ind(va, vb, equal_var=False).pvalue), 4),
            "n_permutations": nperm, "genes_used": len(gs)}


counts = pd.read_csv(gzip.open(RAW / "GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz", "rt"),
                     index_col=0)
groups = {c: ("ctrl_exo" if c.startswith("C") else "hz_exo" if c.startswith("S")
              else "phn_exo" if c.startswith("P") else None) for c in counts.columns}

sf, n_gene_mor = mor_size_factors(counts)
L_cpm = build(counts, None)
L_mor = build(counts, sf)

# 核糖体基因文库占比（两种口径一致，仅取决于 counts）
ribo = [g for g in counts.index if g.startswith(("RPL", "RPS"))]
share = counts.loc[ribo].sum(axis=0) / counts.sum(axis=0) * 100
ctrl = [c for c in counts.columns if groups[c] == "ctrl_exo"]
hz = [c for c in counts.columns if groups[c] == "hz_exo"]

res = {
    "note": "Post hoc robustness check (Round-4 review). CPM is scale-invariant, so the "
            "comparison is done at matched scale: library-size-normalised CPM vs "
            "median-of-ratios-normalised CPM, both then log2(1+CPM).",
    "ribosomal_gene_share_pct": {
        "n_ribosomal_genes": len(ribo),
        "ctrl_exo_mean": round(float(share[ctrl].mean()), 3),
        "hz_exo_mean": round(float(share[hz].mean()), 3),
    },
    "mor_genes_used": n_gene_mor,
    "mor_size_factors": {c: round(float(v), 4) for c, v in zip(counts.columns, sf)},
    "HZexo_vs_CtrlExo": {},
}

for mod, genes in MODS.items():
    res["HZexo_vs_CtrlExo"][mod] = {
        "library_size_cpm": contrast(L_cpm, groups, "hz_exo", "ctrl_exo", genes),
        "median_of_ratios": contrast(L_mor, groups, "hz_exo", "ctrl_exo", genes),
    }

# E1 - M1 交互（两种归一化下）
for tag, L in [("library_size_cpm", L_cpm), ("median_of_ratios", L_mor)]:
    a = [c for c in L.columns if groups[c] == "hz_exo"]
    b = [c for c in L.columns if groups[c] == "ctrl_exo"]
    sE = L.loc[[g for g in MODS["E1_classical_nociceptor"] if g in L.index]].mean(axis=0)
    sM = L.loc[[g for g in MODS["M1_mechanogated_channels"] if g in L.index]].mean(axis=0)
    d = (sE - sM)[a + b].values
    obs = d[:len(a)].mean() - d[len(a):].mean()
    p, nperm = perm_exact_p(d, len(a), obs)
    res.setdefault("interaction_E1_minus_M1", {})[tag] = {
        "diff": round(float(obs), 4), "perm_p": round(p, 4), "n_permutations": nperm}

OUT.parent.mkdir(parents=True, exist_ok=True)
json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("written:", OUT)
print("ribosomal share: ctrl %.3f%% -> hz %.3f%% (%d genes)" % (
    res["ribosomal_gene_share_pct"]["ctrl_exo_mean"],
    res["ribosomal_gene_share_pct"]["hz_exo_mean"], len(ribo)))
for mod in ["M3_ecm_integrin_hippo", "E1_classical_nociceptor", "M1_mechanogated_channels",
            "N1_voltage_gated_control", "N3_ribosomal_control"]:
    r = res["HZexo_vs_CtrlExo"][mod]
    print("  %-28s CPM %8.4f (P=%.4f) | MoR %8.4f (P=%.4f)" % (
        mod, r["library_size_cpm"]["diff"], r["library_size_cpm"]["perm_p"],
        r["median_of_ratios"]["diff"], r["median_of_ratios"]["perm_p"]))
print("  interaction E1-M1:", json.dumps(res["interaction_E1_minus_M1"], ensure_ascii=False))
