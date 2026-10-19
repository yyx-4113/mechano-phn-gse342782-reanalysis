#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Layer 1 结果可视化：Fig2 四维 score 条形 + 中性对照并列 + CCI。
读取 layer1_results.json，输出 PNG 到 results/layer1/fig/。"""
import json, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from pathlib import Path
OUT = str(Path(__file__).resolve().parents[1] / "results" / "layer1")
FIG = os.path.join(OUT, "fig")
os.makedirs(FIG, exist_ok=True)
with open(os.path.join(OUT, "layer1_results.json")) as f:
    R = json.load(f)

# ---- Fig2a: HZexo vs CtrlExo 模块差 + 置换P，M 系列 vs 中性对照并列 ----
lab = "HZexo_vs_CtrlExo"
mods = R["contrasts"][lab]
order = ["M1_mechanogated_channels", "M2_membrane_cytoskeleton", "M3_ecm_integrin_hippo",
         "M4_mechano_effectors", "E1_classical_nociceptor",
         "N1_voltage_gated_control", "N2_olfactory_control", "N3_ribosomal_control"]
diffs, ps, cols, lbls = [], [], [], []
cmap = {"M": "#c0392b", "E": "#2980b9", "N": "#7f8c8d"}
label_map = {
    "M1_mechanogated_channels": "M1\nmechanogated\nchannels",
    "M2_membrane_cytoskeleton": "M2\nmembrane-\ncytoskeleton",
    "M3_ecm_integrin_hippo": "M3\nECM-integrin-\nHippo",
    "M4_mechano_effectors": "M4\nmechano-\neffectors",
    "E1_classical_nociceptor": "E1\nclassical\nnociceptor",
    "N1_voltage_gated_control": "N1\nvoltage-gated",
    "N2_olfactory_control": "N2\nolfactory",
    "N3_ribosomal_control": "N3\nribosomal",
}
for m in order:
    c = mods[m]
    diffs.append(c["diff_B_minus_A"])
    ps.append(c["p_perm_exact"])
    tag = m[0]
    cols.append(cmap.get(tag, "#000"))
    lbls.append(label_map[m])

diffs = np.array(diffs); ps = np.array(ps)
fig, ax = plt.subplots(figsize=(9.5, 5.5))
x = np.arange(len(order))
bars = ax.bar(x, diffs, color=cols, edgecolor="black", linewidth=0.6)
ymax = max(diffs.max(), 0); ymin = min(diffs.min(), 0)
rng = (ymax - ymin) or 0.1
ax.set_ylim(ymin - 0.18*rng, ymax + 0.30*rng)
for xi, (d, p) in enumerate(zip(diffs, ps)):
    star = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"
    ax.text(xi, d + (0.02*rng if d >= 0 else -0.02*rng), f"{d:+.3f}\n{star}", ha="center",
            va="bottom" if d >= 0 else "top", fontsize=8)
ax.axhline(0, color="black", lw=0.8)
ax.set_xticks(x); ax.set_xticklabels(lbls, fontsize=8)
ax.set_ylabel("Module score diff\n(HZ-exo − Ctrl-exo, log2CPM)")
ax.set_title("Fig 2a. Mechanical-transduction module scores: HZ-exo vs Ctrl-exo\n(red=M-mechano, blue=E1, grey=neutral controls; dashed = detection floor)")
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color="#c0392b", label="M1–M4 mechano modules"),
                   Patch(color="#2980b9", label="E1 classical nocireptor"),
                   Patch(color="#7f8c8d", label="N1–N3 neutral controls")],
          fontsize=8, loc="upper left", framealpha=0.9)
ax.text(0.99, 0.02, "*P < 0.05, **P < 0.01, ***P < 0.001 (exact permutation P)\nn = 7 vs 7; bars are group-mean module-score differences",
        transform=ax.transAxes, ha="right", va="bottom", fontsize=8, style="italic")
plt.tight_layout(); plt.savefig(os.path.join(FIG, "fig2a_module_scores.png"), dpi=150); plt.close()

# ---- Fig2b: CCI across contrasts ----
cci = R["CCI"]
clabs = list(cci.keys())
cd = [cci[k]["diff_B_minus_A"] for k in clabs]
cp = [cci[k]["p_perm_exact"] for k in clabs]
fig, ax = plt.subplots(figsize=(8, 4.5))
xb = np.arange(len(clabs)); b = ax.bar(xb, cd, color="#8e44ad", edgecolor="black", lw=0.6)
for xi, (d, p) in enumerate(zip(cd, cp)):
    star = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"
    ax.text(xi, d + (0.01 if d >= 0 else -0.02), f"{d:+.3f}\n{star}", ha="center",
            va="bottom" if d >= 0 else "top", fontsize=9)
ax.axhline(0, color="black", lw=0.8)
ax.set_xticks(xb); ax.set_xticklabels(clabs, rotation=20, ha="right", fontsize=8)
ax.set_ylabel("CCI diff (M1 vs E1 mean-rank)")
ax.set_title("Fig 2d. Channel-complementarity index (CCI) by contrast (all ns; exact permutation P ≥ 0.82)")
plt.tight_layout(); plt.savefig(os.path.join(FIG, "fig2d_cci.png"), dpi=150); plt.close()

print("figures written:", os.listdir(FIG))

# ---- Fig2b: E1 经典伤害性通道基因级 LFC（真实阳性，重编号自 Fig 2c）----
import pandas as pd
gl = pd.read_csv(os.path.join(OUT, "layer1_gene_level.csv"))
gl = gl[gl["contrast"] == "HZexo_vs_CtrlExo"]
e1 = R["contrasts"]["HZexo_vs_CtrlExo"]["E1_classical_nociceptor"]
tg = sorted(e1["top_genes"], key=lambda x: -abs(x[1]))[:10]
gn = [t[0] for t in tg]; gv = [t[1] for t in tg]
pv = {r["gene"]: r["welch_p"] for _, r in gl.iterrows() if r["gene"] in set(gn)}
fig, ax = plt.subplots(figsize=(7.6, 4.8))
colors = ["#c0392b" if v < 0 else "#27ae60" for v in gv]
ax.barh(range(len(gn)), gv, color=colors, edgecolor="black", lw=0.5)
ax.set_yticks(range(len(gn))); ax.set_yticklabels(gn, fontsize=9)
for i, g in enumerate(gn):
    p = pv.get(g, float("nan"))
    mark = "*" if p < 0.05 else "ns"
    ax.text(gv[i] - 0.02, i, f"{gv[i]:+.3f}  {mark}", ha="right", va="center", fontsize=8)
ax.axvline(0, color="black", lw=0.8)
ax.set_xlim(min(gv) - 0.28, 0.05)
ax.set_xlabel("log2CPM difference (HZ-exo − Ctrl-exo)")
ax.set_title("Fig 2b. E1 genes with the largest HZ-exo effects; only TRPV1 survives\nwithin-module BH within E1 (q = 0.017); bars selected by |effect size|, * = nominal P < 0.05", fontsize=9.5)
plt.tight_layout(); plt.savefig(os.path.join(FIG, "fig2b_E1_genes.png"), dpi=150); plt.close()
print("fig2b (E1 genes) added")
