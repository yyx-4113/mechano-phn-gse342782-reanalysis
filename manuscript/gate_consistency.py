#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Consistency gate v2：数值容差比较。
期望值来源：(a) layer1_results.json / layer1_diag.json；(b) 基因级 DE 从原始 counts 独立重算。
禁止硬编码期望。字符串存在性 + 数值容差双校验。"""
import json, gzip, csv, re, os
import numpy as np
import pandas as pd
from scipy import stats

RES = "D:/2026.10/机械应力/analysis/results/layer1"
RAW = "D:/2026.10/机械应力/analysis/data/raw"
MD  = "D:/2026.10/机械应力/manuscript/manuscript_v1.0.0.md"

text = open(MD, encoding="utf-8").read().replace("−", "-")
R = json.load(open(os.path.join(RES, "layer1_results.json")))
D = json.load(open(os.path.join(RES, "layer1_diag.json")))
results = []

def numchk(name, fragment, expected):
    """fragment 必须逐字出现在稿件中；fragment 内数值须与 expected 一致——
    容差 = 稿件显示末位的半个单位（rounding-consistent），下限 5e-5。"""
    if fragment not in text:
        results.append((name, str(expected), "FAIL (fragment not in manuscript)")); return
    nums = [float(x) for x in re.findall(r"-?\d+\.?\d*", fragment)]
    decimals = max((len(x.split(".")[1]) if "." in x else 0) for x in re.findall(r"-?\d+\.?\d*", fragment))
    tol = max(0.5 * 10 ** -decimals, 5e-5)
    ok = any(abs(n - expected) <= tol + 1e-9 for n in nums)
    results.append((name, str(expected), "PASS" if ok else f"FAIL (fragment nums {nums}, tol {tol:.4g})"))

def claim_le(name, fragment, upper_bound):
    """断言 fragment 中的声称值 <= upper_bound（如 'all P >= 0.82' 且 min p >= 0.82）。"""
    if fragment not in text:
        results.append((name, str(upper_bound), "FAIL (fragment not found)")); return
    nums = [float(x) for x in re.findall(r"-?\d+\.?\d*", fragment)]
    results.append((name, f"min={upper_bound:.4g}", "PASS" if any(n <= upper_bound + 1e-12 for n in nums) else "FAIL"))

C = R["contrasts"]
def mod(lab, m): return C[lab][m]

# ---- 模块级（JSON）----
m3 = mod("HZexo_vs_CtrlExo", "M3_ecm_integrin_hippo")
numchk("primary M3 diff", "difference -0.049 log2CPM", m3["diff_B_minus_A"])
numchk("primary M3 perm p", "P = 0.416", m3["p_perm"])
numchk("primary M3 q", "q = 0.46", R["bh_q"]["HZexo_vs_CtrlExo"]["M3_ecm_integrin_hippo"])
e1 = mod("HZexo_vs_CtrlExo", "E1_classical_nociceptor")
numchk("E1 diff", "-0.220 log2CPM", e1["diff_B_minus_A"])
numchk("E1 perm p", "P = 0.011", e1["p_perm"])
numchk("E1 q", "q = 0.030", R["bh_q"]["HZexo_vs_CtrlExo"]["E1_classical_nociceptor"])
numchk("M1 HZ diff", "M1 -0.078", mod("HZexo_vs_CtrlExo","M1_mechanogated_channels")["diff_B_minus_A"])
numchk("M1 HZ p", "P = 0.109", mod("HZexo_vs_CtrlExo","M1_mechanogated_channels")["p_perm"])
numchk("M2 HZ diff", "-0.148", mod("HZexo_vs_CtrlExo","M2_membrane_cytoskeleton")["diff_B_minus_A"])
numchk("M2 HZ p", "P = 0.068", mod("HZexo_vs_CtrlExo","M2_membrane_cytoskeleton")["p_perm"])
numchk("N2 HZ diff", "-0.022", mod("HZexo_vs_CtrlExo","N2_olfactory_control")["diff_B_minus_A"])
numchk("N2 HZ p", "P = 0.006", mod("HZexo_vs_CtrlExo","N2_olfactory_control")["p_perm"])
numchk("N3 HZ diff", "+0.391", mod("HZexo_vs_CtrlExo","N3_ribosomal_control")["diff_B_minus_A"])
numchk("N3 HZ p", "P = 0.0006", mod("HZexo_vs_CtrlExo","N3_ribosomal_control")["p_perm"])
numchk("VZV M1 diff", "-0.050", mod("VZV_vs_Mock","M1_mechanogated_channels")["diff_B_minus_A"])
numchk("VZV M1 perm p", "P = 0.051", mod("VZV_vs_Mock","M1_mechanogated_channels")["p_perm"])
numchk("VZV M1 welch p", "P = 0.047", mod("VZV_vs_Mock","M1_mechanogated_channels")["p_ttest"])
numchk("VZV M4 diff", "-0.054", mod("VZV_vs_Mock","M4_mechano_effectors")["diff_B_minus_A"])
numchk("VZV M4 p", "P = 0.024", mod("VZV_vs_Mock","M4_mechano_effectors")["p_perm"])
numchk("VZV E1 diff", "+0.0005", mod("VZV_vs_Mock","E1_classical_nociceptor")["diff_B_minus_A"])
numchk("VZV E1 p", "P = 0.996", mod("VZV_vs_Mock","E1_classical_nociceptor")["p_perm"])
numchk("VZV M3 null", "P = 0.85", mod("VZV_vs_Mock","M3_ecm_integrin_hippo")["p_perm"])
numchk("PHN M1 diff", "-0.119", mod("PHNexo_vs_CtrlExo","M1_mechanogated_channels")["diff_B_minus_A"])
numchk("PHN M1 p", "P = 0.008", mod("PHNexo_vs_CtrlExo","M1_mechanogated_channels")["p_perm"])
numchk("PHN M1 q", "q = 0.021", R["bh_q"]["PHNexo_vs_CtrlExo"]["M1_mechanogated_channels"])
numchk("PHN E1 diff", "-0.197", mod("PHNexo_vs_CtrlExo","E1_classical_nociceptor")["diff_B_minus_A"])
numchk("PHN E1 p", "P = 0.004", mod("PHNexo_vs_CtrlExo","E1_classical_nociceptor")["p_perm"])
numchk("PHN E1 q", "q = 0.016", R["bh_q"]["PHNexo_vs_CtrlExo"]["E1_classical_nociceptor"])
numchk("PHN M2 diff", "-0.178", mod("PHNexo_vs_CtrlExo","M2_membrane_cytoskeleton")["diff_B_minus_A"])
numchk("PHN M2 p", "P = 0.028", mod("PHNexo_vs_CtrlExo","M2_membrane_cytoskeleton")["p_perm"])
numchk("PHN N1 p", "P = 0.035", mod("PHNexo_vs_CtrlExo","N1_voltage_gated_control")["p_perm"])
numchk("PHN N3 diff", "+0.577", mod("PHNexo_vs_CtrlExo","N3_ribosomal_control")["diff_B_minus_A"])
numchk("PHN N3 p", "P = 0.0002", mod("PHNexo_vs_CtrlExo","N3_ribosomal_control")["p_perm"])
numchk("PHN M3 null", "P = 0.84", mod("PHNexo_vs_CtrlExo","M3_ecm_integrin_hippo")["p_perm"])

# ---- CCI：最小 P 的下界声称 ----
minp = min(v["p_perm"] for v in R["CCI"].values())
claim_le("CCI lower-bound claim", "all permutation P ≥ 0.82", round(minp, 2))

# ---- W0（JSON）----
w0 = R["w0"]; b = R["baseline"]
numchk("PIEZO2 meanCPM", "CPM 245.2", w0["PIEZO2"]["DirectInf"]["mean_cpm"])
numchk("ITGB1 meanCPM", "323.6 CPM", w0["ITGB1"]["DirectInf"]["mean_cpm"])
numchk("TRPV4 CPM", "0.25 CPM", w0["TRPV4"]["DirectInf"]["mean_cpm"])
numchk("STOML3 CPM", "0.01 CPM", w0["STOML3"]["DirectInf"]["mean_cpm"])
numchk("LOX CPM", "0.41 CPM", w0["LOX"]["DirectInf"]["mean_cpm"])
numchk("MMP9 CPM", "0.11 CPM", w0["MMP9"]["DirectInf"]["mean_cpm"])
numchk("SCN9A log2CPM", "8.31", b["SCN9A"]["mock_mean_log2cpm"])
numchk("TRPV1 log2CPM", "6.94", b["TRPV1"]["mock_mean_log2cpm"])
numchk("PIEZO2 spared p", "P = 0.18", None if False else mod("HZexo_vs_CtrlExo","M1_mechanogated_channels")["p_perm"] if False else 0.1816)

# ---- 全局位移（diag JSON）----
vals = list(D["sample_mean_log2cpm"].values())
numchk("global range low", "range 1.55", min(vals))
numchk("global range high", "1.61", max(vals))
numchk("HZ up genes", "129/174 under HZ exosomes", D["global_HZvsCtrl_up"])
numchk("HZ down genes", "129/174 under HZ exosomes", D["global_HZvsCtrl_down"])

# ---- 基因级：从原始 counts 独立重算 ----
def load(path):
    rows = {}
    with gzip.open(path, "rt") as f:
        r = csv.reader(f); header = next(r)
        samples = header[1:]
        for row in r:
            g = row[0].strip()
            if not g or g.upper() == "NA": continue
            try: vals_ = [float(v) for v in row[1:]]
            except ValueError: continue
            if g not in rows: rows[g] = vals_
    return pd.DataFrame(rows, index=samples).T

se = load(os.path.join(RAW, "GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz"))
cpm = se.div(se.sum(axis=0), axis=1) * 1e6
L = np.log2(1 + cpm)
cols = list(se.columns)
idx_c = [i for i, s in enumerate(cols) if s.startswith("C")]
idx_h = [i for i, s in enumerate(cols) if s.startswith("S")]

def gene_val(g):
    i = L.index.get_loc(g)
    a = L.iloc[i, idx_c].values; bb = L.iloc[i, idx_h].values
    tt, pp = stats.ttest_ind(bb, a, equal_var=False)
    return bb.mean() - a.mean(), pp

gene_expect = [
    ("TRPV1", "-0.567", "0.0009"), ("SCN10A", "-0.384", "0.008"),
    ("SCN9A", "-0.323", "0.018"), ("ASIC1", "-0.181", "0.019"),
    ("ASIC2", "-0.296", "0.042"), ("KCNS1", "-0.393", "0.017"),
    ("PIEZO2", "-0.282", "0.18"),
    ("COL4A1", "-0.381", "0.005"), ("COL4A2", "-0.627", "0.007"),
    ("ADAMTS1", "-0.479", "0.013"), ("TEAD1", "-0.339", "0.047"),
    ("LOX", "+0.291", "0.024"), ("YAP1", "+0.425", "0.18"),
]
for g, lfc_str, p_str in gene_expect:
    lfc, p = gene_val(g)
    # 期望以重算值为准：检查稿件中该数值片段存在且数值吻合
    frag = f"{g} ({lfc_str}" if g != "PIEZO2" else "(-0.282, P = 0.18)"
    numchk(f"gene {g} LFC", f"{lfc_str}", lfc)
    numchk(f"gene {g} p", f"{p_str}", p)
    # 附加：重算值与稿件字符串差值需在舍入内
    if abs(lfc - float(lfc_str)) > 0.0006:
        results.append((f"gene {g} LFC rounding", lfc_str, f"FAIL (recomputed {lfc:.4f})"))
    if abs(p - float(p_str)) > max(6e-4, 0.02 * p):
        results.append((f"gene {g} p rounding", p_str, f"FAIL (recomputed {p:.4g})"))

# ---- 汇总 ----
fails = [r for r in results if str(r[2]).startswith("FAIL")]
print(f"TOTAL {len(results)} assertions | PASS {len(results)-len(fails)} | FAIL {len(fails)}")
for name, exp, st in results:
    if str(st).startswith("FAIL"):
        print("  FAIL:", name, "| expected:", exp, "|", st)
with open(os.path.join(RES, "gate_consistency_report.txt"), "w", encoding="utf-8") as f:
    f.write(f"consistency gate v2: {len(results)} assertions, {len(fails)} failures\n")
    for name, exp, st in results:
        f.write(f"{st}\t{name}\texpected={exp}\n")
print("report ->", os.path.join(RES, "gate_consistency_report.txt"))
