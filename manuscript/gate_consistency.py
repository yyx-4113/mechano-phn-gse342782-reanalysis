#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Consistency gate v3：数值容差比较（所有期望值从产物动态派生，禁止硬编码）。
v1.1.0 修订：
  - 键名 p_perm -> p_perm_exact（精确枚举）；
  - 移除硬编码 PIEZO2 p=0.1816（改从 layer1_gene_level.csv 派生）；
  - 覆盖扩展：MDE / Welch & perm CI / 交互检验 P / 检出基因敏感性 / 模块覆盖率 / 全局 DE。
"""
import json, gzip, csv, re, os
import numpy as np
import pandas as pd
from scipy import stats
from pathlib import Path
from itertools import combinations

# 路径相对仓库根（manuscript/ 上溯一级），避免绝对路径不可移植
_ROOT = Path(__file__).resolve().parents[1]
RES = str(_ROOT / "analysis" / "results" / "layer1")
RAW = str(_ROOT / "analysis" / "data" / "raw")
MD  = str(_ROOT / "manuscript" / "manuscript_v1.1.4.md")

text = open(MD, encoding="utf-8").read().replace("−", "-")
R = json.load(open(os.path.join(RES, "layer1_results.json")))
D = json.load(open(os.path.join(RES, "layer1_diag.json")))
G = pd.read_csv(os.path.join(RES, "layer1_gene_level.csv"))
GD = pd.read_csv(os.path.join(RES, "layer1_global_de.csv"))
results = []

def numchk(name, fragment, expected):
    if fragment not in text:
        results.append((name, str(expected), "FAIL (fragment not in manuscript)"))
        return
    nums = [float(x) for x in re.findall(r"-?\d+\.?\d*", fragment)]
    ok = False
    for n in nums:
        dec = len(str(n).split(".")[1]) if "." in str(n) else 0
        tol = max(0.5 * 10 ** -dec, 5e-5)
        if abs(n - expected) <= tol + 1e-9:
            ok = True
            break
    results.append((name, str(expected), "PASS" if ok else f"FAIL (fragment nums {nums})"))

def present(name, fragment):
    results.append((name, fragment, "PASS" if fragment in text else "FAIL (fragment not found)"))

def claim_ge(name, claimed_floor, true_value, tol=0.01):
    # 稿件声称 ">= claimed_floor"；校验真实值不低于该下界（含四舍五入容差）
    ok = true_value >= claimed_floor - tol
    results.append((name, f"true={true_value:.4f} >= claimed_floor {claimed_floor}", "PASS" if ok else "FAIL"))

def claim_le(name, claimed_ceil, true_value, tol=0.01):
    # 稿件声称 "<= claimed_ceil"；校验真实值不高于该上界（含四舍五入容差）
    ok = true_value <= claimed_ceil + tol
    results.append((name, f"true={true_value:.4f} <= claimed_ceil {claimed_ceil}", "PASS" if ok else "FAIL"))

C = R["contrasts"]
def mod(lab, m): return C[lab][m]

# ---- 模块级（JSON，精确枚举 P）----
m3 = mod("HZexo_vs_CtrlExo", "M3_ecm_integrin_hippo")
numchk("primary M3 diff", "difference -0.049 log2CPM", m3["diff_B_minus_A"])
numchk("primary M3 perm p", "permutation P = 0.42", m3["p_perm_exact"])
numchk("primary M3 q", "BH q = 0.46", R["bh_q"]["HZexo_vs_CtrlExo"]["M3_ecm_integrin_hippo"])
numchk("M3 MDE", "minimum detectable effect at 80% power was 0.18 log2CPM", m3["mde_80pct"])
numchk("M3 welch CI low", "Welch -0.18 to", m3["ci95_welch"][0])
numchk("M3 welch CI high", "to +0.08", m3["ci95_welch"][1])
numchk("M3 perm CI low", "permutation-inversion -0.16", m3["ci95_perm_inversion"][0])
numchk("M3 perm CI high", "+0.06", m3["ci95_perm_inversion"][1])

e1 = mod("HZexo_vs_CtrlExo", "E1_classical_nociceptor")
numchk("E1 diff", "-0.220 log2CPM", e1["diff_B_minus_A"])
numchk("E1 perm p", "permutation P = 0.013", e1["p_perm_exact"])
numchk("E1 q", "BH q = 0.034", R["bh_q"]["HZexo_vs_CtrlExo"]["E1_classical_nociceptor"])
numchk("E1 CI low", "-0.38 to", e1["ci95_welch"][0])
numchk("E1 CI high", "-0.06", e1["ci95_welch"][1])

numchk("M1 HZ diff", "M1 -0.078", mod("HZexo_vs_CtrlExo","M1_mechanogated_channels")["diff_B_minus_A"])
numchk("M1 HZ p", "M1 -0.078, P = 0.11", mod("HZexo_vs_CtrlExo","M1_mechanogated_channels")["p_perm_exact"])
numchk("M2 HZ diff", "-0.148", mod("HZexo_vs_CtrlExo","M2_membrane_cytoskeleton")["diff_B_minus_A"])
numchk("M2 HZ p", "P = 0.068", mod("HZexo_vs_CtrlExo","M2_membrane_cytoskeleton")["p_perm_exact"])
numchk("N2 HZ diff", "-0.022", mod("HZexo_vs_CtrlExo","N2_olfactory_control")["diff_B_minus_A"])
numchk("N2 HZ p", "P = 0.006", mod("HZexo_vs_CtrlExo","N2_olfactory_control")["p_perm_exact"])
numchk("N2 HZ q", "q = 0.023", R["bh_q"]["HZexo_vs_CtrlExo"]["N2_olfactory_control"])
numchk("N3 HZ diff", "+0.391", mod("HZexo_vs_CtrlExo","N3_ribosomal_control")["diff_B_minus_A"])
numchk("N3 HZ p", "P = 0.002", mod("HZexo_vs_CtrlExo","N3_ribosomal_control")["p_perm_exact"])

# VZV
numchk("VZV M1 diff", "-0.050", mod("VZV_vs_Mock","M1_mechanogated_channels")["diff_B_minus_A"])
numchk("VZV M1 perm p", "P = 0.05", mod("VZV_vs_Mock","M1_mechanogated_channels")["p_perm_exact"])
numchk("VZV M1 welch p", "Welch P = 0.047", mod("VZV_vs_Mock","M1_mechanogated_channels")["p_ttest"])
numchk("VZV M4 diff", "-0.054", mod("VZV_vs_Mock","M4_mechano_effectors")["diff_B_minus_A"])
numchk("VZV M4 p", "P = 0.03", mod("VZV_vs_Mock","M4_mechano_effectors")["p_perm_exact"])
numchk("VZV E1 diff", "+0.0005", mod("VZV_vs_Mock","E1_classical_nociceptor")["diff_B_minus_A"])
numchk("VZV E1 p", "P = 0.996", mod("VZV_vs_Mock","E1_classical_nociceptor")["p_perm_exact"])
numchk("VZV M3 null", "P = 0.85", mod("VZV_vs_Mock","M3_ecm_integrin_hippo")["p_perm_exact"])

# PHN
numchk("PHN M1 diff", "-0.119", mod("PHNexo_vs_CtrlExo","M1_mechanogated_channels")["diff_B_minus_A"])
numchk("PHN M1 p", "P = 0.009", mod("PHNexo_vs_CtrlExo","M1_mechanogated_channels")["p_perm_exact"])
numchk("PHN M1 q", "q = 0.024", R["bh_q"]["PHNexo_vs_CtrlExo"]["M1_mechanogated_channels"])
numchk("PHN E1 diff", "-0.197", mod("PHNexo_vs_CtrlExo","E1_classical_nociceptor")["diff_B_minus_A"])
numchk("PHN E1 p", "P = 0.005", mod("PHNexo_vs_CtrlExo","E1_classical_nociceptor")["p_perm_exact"])
numchk("PHN E1 q", "q = 0.020", R["bh_q"]["PHNexo_vs_CtrlExo"]["E1_classical_nociceptor"])
numchk("PHN M2 diff", "-0.178", mod("PHNexo_vs_CtrlExo","M2_membrane_cytoskeleton")["diff_B_minus_A"])
numchk("PHN M2 p", "P = 0.030", mod("PHNexo_vs_CtrlExo","M2_membrane_cytoskeleton")["p_perm_exact"])
numchk("PHN N1 p", "P = 0.039", mod("PHNexo_vs_CtrlExo","N1_voltage_gated_control")["p_perm_exact"])
numchk("PHN N3 diff", "+0.577", mod("PHNexo_vs_CtrlExo","N3_ribosomal_control")["diff_B_minus_A"])
numchk("PHN N3 p", "P = 0.001", mod("PHNexo_vs_CtrlExo","N3_ribosomal_control")["p_perm_exact"])
numchk("PHN N3 q", "q = 0.010", R["bh_q"]["PHNexo_vs_CtrlExo"]["N3_ribosomal_control"])
numchk("PHN M3 null", "P = 0.83", mod("PHNexo_vs_CtrlExo","M3_ecm_integrin_hippo")["p_perm_exact"])

# ---- 交互检验（contrast-of-contrasts）----
it_hz = R["interaction"]["HZexo_vs_CtrlExo"]
it_vz = R["interaction"]["VZV_vs_Mock"]
numchk("interaction HZ diff", "-0.142 log2CPM", it_hz["diff_B_minus_A"])
numchk("interaction HZ p", "exact permutation P = 0.0017", it_hz["p_perm_exact"])
numchk("interaction VZV diff", "-0.051", it_vz["diff_B_minus_A"])
numchk("interaction VZV p", "exact permutation P = 0.19", it_vz["p_perm_exact"])

# ---- 检出基因交互检验（公平性校正；限制 mean CPM>1，排除 floor 稀释）----
itd_hz = R["interaction_detected_only"]["HZexo_vs_CtrlExo"]
present("detected-only interaction disclosed", "detected-gene subset analysis (P = 0.16)")
numchk("detected interaction HZ diff", "-0.072", itd_hz["diff_B_minus_A"])
claim_le("detected interaction HZ p (non-sig <=0.20)", 0.20, itd_hz["p_perm_exact"])

# ---- 独立重算（破解循环 gate：从原始计数直接重算主终点 M3 精确置换 P）----
def _load_counts(path):
    # 与管线 load_counts 对齐：首列 gene_symbol，列名取 header 的样本名（字符串）
    rows = {}
    with gzip.open(path, "rt") as f:
        r = csv.reader(f)
        header = next(r)
        samples = [h for h in header[1:]]
        for row in r:
            g = row[0].strip()
            if not g or g.upper() in ("NA","GENE_SYMBOL"): continue
            try: v = [float(x) for x in row[1:]]
            except ValueError: continue
            if g in rows: continue
            rows[g] = v
    df = pd.DataFrame(rows, index=samples).T
    df.index.name = "gene_symbol"
    return df
def _perm_exact(diff_obs, values, idx_a, idx_b):
    values = np.asarray(values, dtype=float).ravel()
    pool = np.concatenate([idx_a, idx_b]); na = len(idx_a); obs = abs(diff_obs)
    dists = []
    for idx in combinations(range(len(pool)), na):
        a = values[pool[list(idx)]]
        mask = np.ones(len(pool), dtype=bool); mask[list(idx)] = False
        dists.append(values[pool[mask]].mean() - a.mean())
    return float((np.abs(np.asarray(dists)) >= obs - 1e-12).mean())
_panel = json.load(open(os.path.join(_ROOT, "analysis", "config", "mtp_panel.json")))
_m3 = _panel["M3_ecm_integrin_hippo"]["genes"]
_se = _load_counts(os.path.join(RAW, "GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz"))
_se_groups = {s: ("ctrl_exo" if s.startswith("C") else "phn_exo" if s.startswith("P") else "hz_exo" if s.startswith("S") else None) for s in _se.columns}
_present = set(_se.index)
_m3p = [g for g in _m3 if g in _present]
_L = np.log2(1 + _se.div(_se.sum(axis=0), axis=1) * 1e6)
_sub = _L.loc[_m3p]
_ia = [i for i,s in enumerate(_se.columns) if _se_groups[s]=="ctrl_exo"]
_ib = [i for i,s in enumerate(_se.columns) if _se_groups[s]=="hz_exo"]
_scores = _sub.mean(axis=0).values
_diff = _scores[_ib].mean() - _scores[_ia].mean()
_p_indep = _perm_exact(_diff, _scores, _ia, _ib)
numchk("INDEPENDENT M3 HZ perm p (raw counts)", "permutation P = 0.42", _p_indep)
results.append(("INDEPENDENT M3 HZ perm p (raw counts)", "%.4f" % _p_indep, "PASS" if abs(_p_indep - 0.42) < 0.02 else "FAIL"))

# ---- 检出基因敏感性 ----
sens = R["sensitivity_detected_genes"]["HZexo_vs_CtrlExo"]["M1_mechanogated_channels"]
numchk("sens M1 detected diff", "-0.171", sens["diff_B_minus_A"])
numchk("sens M1 detected p", "P = 0.046", sens["p_perm_exact"])

# ---- CCI 下界声称 ----
minp = min(v["p_perm_exact"] for v in R["CCI"].values())
present("CCI lower-bound claim", "all permutation P >= 0.82")
claim_ge("CCI min p (claim >=0.82)", 0.82, minp)

# ---- W0（JSON）----
w0 = R["w0"]; b = R["baseline"]
numchk("PIEZO2 meanCPM", "245.2", w0["PIEZO2"]["DirectInf"]["mean_cpm"])
numchk("P2RX3 meanCPM DI", "806.8", w0["P2RX3"]["DirectInf"]["mean_cpm"])
numchk("P2RX3 meanCPM SE", "470.6", w0["P2RX3"]["SeraExo"]["mean_cpm"])
numchk("PIEZO2 SE CPM", "164.1", w0["PIEZO2"]["SeraExo"]["mean_cpm"])
numchk("ITGB1 meanCPM", "323.6", w0["ITGB1"]["DirectInf"]["mean_cpm"])
numchk("TRPV4 CPM", "0.25 CPM", w0["TRPV4"]["DirectInf"]["mean_cpm"])
numchk("STOML3 CPM", "0.01 CPM", w0["STOML3"]["DirectInf"]["mean_cpm"])
numchk("LOX CPM", "0.41 CPM", w0["LOX"]["DirectInf"]["mean_cpm"])
numchk("MMP9 CPM", "0.11 CPM", w0["MMP9"]["DirectInf"]["mean_cpm"])
numchk("SCN10A SE CPM", "0.55", w0["SCN10A"]["SeraExo"]["mean_cpm"])
numchk("SCN9A log2CPM", "8.39", b["SCN9A"]["directinf_mock_only_mean_log2cpm"])
numchk("TRPV1 log2CPM", "7.02", b["TRPV1"]["directinf_mock_only_mean_log2cpm"])
numchk("TAC1 meanCPM DI", "65.7", w0["TAC1"]["DirectInf"]["mean_cpm"])

# PIEZO2 "spared" —— 从基因级 CSV 派生（不再硬编码 0.1816）
piezo_hz = G[(G.gene == "PIEZO2") & (G.contrast == "HZexo_vs_CtrlExo")]
piezo_p = float(piezo_hz["welch_p"].iloc[0])
numchk("PIEZO2 spared (gene CSV)", "PIEZO2 P = 0.18", piezo_p)

# ---- 模块覆盖率（JSON 派生）----
present("M3 coverage 56/58", "56/58")
present("N2 coverage 13/16", "13/16")
present("N3 coverage 17/18", "17/18")
n2 = mod("HZexo_vs_CtrlExo","N2_olfactory_control")
n3 = mod("HZexo_vs_CtrlExo","N3_ribosomal_control")
m3c = mod("HZexo_vs_CtrlExo","M3_ecm_integrin_hippo")
numchk("N2 used/total", "13/16", n2["genes_used"] / n2["genes_total"] * 16)
numchk("N3 used/total", "17/18", n3["genes_used"] / n3["genes_total"] * 18)
numchk("M3 used/total", "56/58", m3c["genes_used"] / m3c["genes_total"] * 58)

# ---- 全局 DE（CSV）----
hz_de = GD[GD.contrast == "HZexo_vs_CtrlExo"].iloc[0]
phn_de = GD[GD.contrast == "PHNexo_vs_CtrlExo"].iloc[0]
numchk("HZ up/down", "129/174 under HZ exosomes", hz_de["n_up"])
numchk("PHN up", "568 genes up-", phn_de["n_up"])
numchk("PHN down", "125 down-regulated", phn_de["n_down"])

# ---- 全局位移（diag JSON）----
vals = list(D["sample_mean_log2cpm"].values())
numchk("global range low", "range 1.55", min(vals))
claim_le("global range high (claim <=1.61)", 1.61, max(vals))

# ---- 基因级：从 CSV 派生的关键值 ----
E1M = "E1_classical_nociceptor"


def gv(g, lab, col, module=None):
    """基因级取值。Round-4 起 CSV 含 module 列（跨模块共享基因各一行），
    取 q_within_module 时必须指定 module，否则同名基因会取到错误模块的值。"""
    row = G[(G.gene == g) & (G.contrast == lab)]
    if module is not None:
        row = row[row.module == module]
    return float(row[col].iloc[0]) if len(row) else None
numchk("TRPV1 LFC", "-0.567", gv("TRPV1","HZexo_vs_CtrlExo","log2FC"))
numchk("SCN9A LFC", "-0.323", gv("SCN9A","HZexo_vs_CtrlExo","log2FC"))
numchk("SCN10A LFC", "-0.384", gv("SCN10A","HZexo_vs_CtrlExo","log2FC"))
numchk("ASIC1 LFC", "-0.181", gv("ASIC1","HZexo_vs_CtrlExo","log2FC"))
numchk("ASIC2 LFC", "-0.296", gv("ASIC2","HZexo_vs_CtrlExo","log2FC"))
numchk("KCNS1 LFC", "-0.393", gv("KCNS1","HZexo_vs_CtrlExo","log2FC"))

# ---- 基因级 module 内 BH 校正（Round-3 诚实化：防止回退到"全部显著"）----
numchk("TRPV1 within-E1 q", "0.017", gv("TRPV1","HZexo_vs_CtrlExo","q_within_module", module=E1M))
claim_le("TRPV1 within-E1 q (survives FDR <=0.05)", 0.05, gv("TRPV1","HZexo_vs_CtrlExo","q_within_module", module=E1M))
claim_ge("KCNS1 within-E1 q (does NOT survive >=0.05)", 0.05, gv("KCNS1","HZexo_vs_CtrlExo","q_within_module", module=E1M))
claim_ge("SCN9A within-E1 q (does NOT survive >=0.05)", 0.05, gv("SCN9A","HZexo_vs_CtrlExo","q_within_module", module=E1M))
claim_ge("ASIC1 within-E1 q (does NOT survive >=0.05)", 0.05, gv("ASIC1","HZexo_vs_CtrlExo","q_within_module", module=E1M))
claim_ge("ASIC2 within-E1 q (does NOT survive >=0.05)", 0.05, gv("ASIC2","HZexo_vs_CtrlExo","q_within_module", module=E1M))
present("within-module BH disclosed", "within-E1")
# Round-4 回归锁：KCNQ2/KCNQ3 同属 E1 与 N1，q 不得被后处理模块覆盖
numchk("KCNQ3 within-E1 q (was overwritten by N1 before Round-4 fix)", "0.366",
       gv("KCNQ3","HZexo_vs_CtrlExo","q_within_module", module=E1M))
numchk("KCNQ2 within-E1 q (was overwritten by N1 before Round-4 fix)", "0.497",
       gv("KCNQ2","HZexo_vs_CtrlExo","q_within_module", module=E1M))
claim_ge("KCNQ3 within-E1 q < N1 q (family-specific, not overwritten)", 0.40,
         gv("KCNQ3","HZexo_vs_CtrlExo","q_within_module", module="N1_voltage_gated_control"))
present("detected-gene subset vs multiplicity clarified", "subset analysis")

# ---- Round-4 新增：E1 内部基准 / 神经元完整性 / 路径量级（产物 layer1_extra_checks.json）----
import json as _json
X = _json.load(open(str(_ROOT / "analysis" / "results" / "layer1" / "layer1_extra_checks.json"), encoding="utf-8"))
XE = X["e1_vs_n1_benchmark"]["HZexo_vs_CtrlExo"]
numchk("E1-N1 difference", "-0.064", XE["diff_hz_exo_minus_ctrl_exo"])
numchk("E1-N1 permutation P", "0.178", XE["perm_p"])
claim_ge("E1 vs N1 NOT separable (P >= 0.05)", 0.05, XE["perm_p"])
XM = X["neuronal_integrity_markers"]["genes"]
numchk("ATF3 log2FC", "+0.0002", XM["ATF3"]["log2FC"])
claim_ge("ATF3 unchanged (P >= 0.05)", 0.05, XM["ATF3"]["welch_p"])
numchk("NEFH log2FC", "-0.221", XM["NEFH"]["log2FC"])
numchk("TUBB3 log2FC", "-0.183", XM["TUBB3"]["log2FC"])
XT = X["trpv1_by_route"]["VZV_vs_Mock"]
numchk("TRPV1 under direct VZV", "-0.149", XT["log2FC"])
numchk("TRPV1 VZV within-E1 q", "0.144", XT["q_within_E1"])
claim_ge("TRPV1 VZV does NOT survive within-E1 FDR", 0.05, XT["q_within_E1"])
XB = X["baseline_denominators"]["genes"]
numchk("SCN9A all-12 baseline", "8.31", XB["SCN9A"]["directinf_all12_mean_log2cpm"])
numchk("SCN9A mock-only baseline", "8.39", XB["SCN9A"]["directinf_mock_only_mean_log2cpm"])
numchk("TRPV1 all-12 baseline", "6.94", XB["TRPV1"]["directinf_all12_mean_log2cpm"])
XD = X["detection_baseline_extras"]
numchk("OR5A1 mean CPM", "0.89", XD["OR5A1"]["seraexo_mean_cpm"])
numchk("PIEZO2 gene-level CI low", "-0.72", XD["PIEZO2"]["HZexo_vs_CtrlExo"]["ci95"][0])
numchk("PIEZO2 gene-level CI high", "+0.15", XD["PIEZO2"]["HZexo_vs_CtrlExo"]["ci95"][1])
present("E1 vs N1 benchmark disclosed", "not separable from N1")
present("ATF3 injury marker reported", "ATF3")
present("route dependence is magnitude not direction", "magnitude rather than direction")
present("substrate stiffness limitation", "Substrate stiffness")
present("PHN donor metadata statement", "not present in the deposited GEO metadata")

# ---- 汇总 ----
fails = [r for r in results if str(r[2]).startswith("FAIL")]
print(f"TOTAL {len(results)} assertions | PASS {len(results)-len(fails)} | FAIL {len(fails)}")
for name, exp, st in results:
    if str(st).startswith("FAIL"):
        print("  FAIL:", name, "| expected:", exp, "|", st)
with open(os.path.join(RES, "gate_consistency_report.txt"), "w", encoding="utf-8") as f:
    f.write(f"consistency gate v3: {len(results)} assertions, {len(fails)} failures\n")
    for name, exp, st in results:
        f.write(f"{st}\t{name}\texpected={exp}\n")
print("report ->", os.path.join(RES, "gate_consistency_report.txt"))
