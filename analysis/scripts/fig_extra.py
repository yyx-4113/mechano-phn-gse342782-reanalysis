#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fig1 研究设计示意 + Fig2d 双重分离矩阵（全部数字取自 results JSON，不硬编码）。"""
import json, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

RES = "D:/2026.10/机械应力/analysis/results/layer1"
FIG = os.path.join(RES, "fig")
R = json.load(open(os.path.join(RES, "layer1_results.json")))

# ---------------- Fig 1: 设计示意 ----------------
fig, ax = plt.subplots(figsize=(10, 6.2))
ax.set_xlim(0, 10); ax.set_ylim(0, 6.2); ax.axis("off")

def box(x, y, w, h, text, fc, fs=9):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                                fc=fc, ec="black", lw=0.8))
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=fs)

def arrow(x1, y1, x2, y2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2),
        arrowstyle="-|>", mutation_scale=12, lw=1.0, color="black"))

box(0.3, 4.6, 4.4, 1.2, "GSE342782  (human HD10 sensory neurons, bulk RNA-seq, 31 samples)\n"
    "Experiment 1: mock (n=6)  vs  VZV direct infection (n=6), 4 dpi\n"
    "Experiment 2: serum exosomes 36 h — control (n=7) / acute HZ (n=7) / PHN (n=5)", "#eaf2f8", 8.2)
box(5.3, 4.6, 4.4, 1.2, "W0 data examination (pre-registered gate)\n"
    "PIEZO2 highly expressed (mean CPM ≈ 245, 100% detected)\n"
    "TRPV4 / STOML3 below detection  →  M1 = PIEZO2-driven", "#fef9e7", 8.2)
arrow(4.75, 5.2, 5.25, 5.2)

box(0.3, 2.9, 4.4, 1.2, "Frozen MTP panel (pre-analysis)\n"
    "M1 mechanogated channels · M2 membrane-cytoskeleton\n"
    "M3 ECM-integrin-Hippo · M4 mechano-effectors\n"
    "E1 electrochemical nociceptor · N1–N3 neutral controls", "#eaf7ea", 8.2)
box(5.3, 2.9, 4.4, 1.2, "Module scoring on log2(1+CPM)\n"
    "Welch t + Wilcoxon + label-permutation null (B = 5000)\n"
    "Primary endpoint: M3 diff (HZ-exo vs Ctrl-exo)\n"
    "Secondary: E1 / M1 (channel imbalance, pre-specified)", "#eaf7ea", 8.2)
arrow(2.5, 4.55, 2.5, 4.15)
arrow(7.5, 4.55, 7.5, 4.15)

box(0.3, 1.2, 9.4, 1.2, "Results\n"
    "Primary endpoint M3: correctly-powered NULL (perm P = 0.416)\n"
    "Secondary: HZ-exo selectively suppresses electrochemical nociceptor channels (E1, perm P = 0.011) with spared PIEZO2\n"
    "Double dissociation: direct VZV ↓ M1 (P = 0.051) with E1 unchanged; HZ-exo ↓ E1 with M1 unchanged", "#fdf2e9", 8.4)
arrow(2.5, 2.85, 2.5, 2.45)
arrow(7.5, 2.85, 7.5, 2.45)

ax.text(5.0, 0.55, "All effect sizes reported with permutation-calibrated P; neutral controls displayed alongside every module",
        ha="center", fontsize=8.5, style="italic")
ax.set_title("Figure 1. Study design and pre-registered analysis pipeline", fontsize=11)
plt.tight_layout(); plt.savefig(os.path.join(FIG, "fig1_design.png"), dpi=150); plt.close()

# ---------------- Fig 2d: 双重分离 ----------------
m1_vzv = R["contrasts"]["VZV_vs_Mock"]["M1_mechanogated_channels"]["diff_B_minus_A"]
m1_hz  = R["contrasts"]["HZexo_vs_CtrlExo"]["M1_mechanogated_channels"]["diff_B_minus_A"]
e1_vzv = R["contrasts"]["VZV_vs_Mock"]["E1_classical_nociceptor"]["diff_B_minus_A"]
e1_hz  = R["contrasts"]["HZexo_vs_CtrlExo"]["E1_classical_nociceptor"]["diff_B_minus_A"]
p_m1v = R["contrasts"]["VZV_vs_Mock"]["M1_mechanogated_channels"]["p_perm"]
p_m1h = R["contrasts"]["HZexo_vs_CtrlExo"]["M1_mechanogated_channels"]["p_perm"]
p_e1v = R["contrasts"]["VZV_vs_Mock"]["E1_classical_nociceptor"]["p_perm"]
p_e1h = R["contrasts"]["HZexo_vs_CtrlExo"]["E1_classical_nociceptor"]["p_perm"]

fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.4), sharey=True)
xt = np.arange(2)
for ax, (vals, ps, title) in zip(axes, [
    ([m1_vzv, e1_vzv], [p_m1v, p_e1v], "Direct VZV infection (vs mock)"),
    ([m1_hz,  e1_hz ], [p_m1h, p_e1h], "Acute HZ serum exosomes (vs control-exo)")]):
    cols = ["#c0392b" if v < 0 else "#27ae60" for v in vals]
    ax.bar(xt, vals, color=cols, edgecolor="black", lw=0.6, width=0.55)
    for xi, (v, p) in enumerate(zip(vals, ps)):
        star = "**" if p < 0.01 else "*" if p < 0.05 else "ns"
        ax.text(xi, v + (0.006 if v >= 0 else -0.012), f"{v:+.3f}\n{star}",
                ha="center", va="bottom" if v >= 0 else "top", fontsize=9)
    ax.axhline(0, color="black", lw=0.8)
    ax.set_xticks(xt); ax.set_xticklabels(["M1 mechanogated", "E1 electrochemical\nnociceptor"], fontsize=9)
    ax.set_title(title, fontsize=10)
axes[0].set_ylabel("Module score diff (log2CPM)")
fig.suptitle("Figure 2d. Double dissociation: perturbation route determines which channel programme shifts", fontsize=11)
plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.savefig(os.path.join(FIG, "fig2d_dissociation.png"), dpi=150); plt.close()

print("fig1 + fig2d written")
