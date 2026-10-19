#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Layer 1 + W0：GSE342782 四维 mechano-score、CCI、置换零分布、组间比较。
纪律：
  - MTP panel 来自 analysis/config/mtp_panel.json（分析前冻结）
  - 主对比 = HZ-exo vs control-exo（规避 PHN 供体年龄/性别混杂）
  - 所有 P 值同时给 t-test / Wilcoxon / 置换零分布分位
  - 产物写 JSON + CSV，附 MANIFEST（sha256），不硬编码任何结论数字
"""
import json, gzip, os, hashlib, csv
import numpy as np
import pandas as pd
from scipy import stats

RAW = "D:/2026.10/机械应力/analysis/data/raw"
OUT = "D:/2026.10/机械应力/analysis/results/layer1"
CFG = "D:/2026.10/机械应力/analysis/config/mtp_panel.json"
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

def perm_null(diff_obs, mat, idx_a, idx_b, B=5000, seed=20261019):
    """对 module score 差做标签置换零分布，返回 (p_two-sided, percentile)。"""
    rng = np.random.default_rng(seed)
    n = mat.shape[1]
    labels = np.array([0]*len(idx_a) + [1]*len(idx_b))
    pool = np.concatenate([idx_a, idx_b])
    dist = np.empty(B)
    for b in range(B):
        perm = rng.permutation(labels)
        a = pool[perm == 0]; bb = pool[perm == 1]
        dist[b] = mat[:, bb].mean() - mat[:, a].mean()
    p = (np.abs(dist) >= abs(diff_obs)).mean()
    p = max(p, 1.0 / B)
    perc = (dist <= diff_obs).mean() * 100
    return float(p), float(perc)

# ---------- 载入 panel ----------
with open(CFG) as f:
    PANEL = json.load(f)
MODULES = {k: v["genes"] for k, v in PANEL.items() if k not in ("panel_version", "note")}

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

w0_genes = ["PIEZO1", "PIEZO2", "TRPV4", "STOML3", "ITGB1", "YAP1", "LOX", "MMP9", "SCN9A", "TRPV1", "COL1A1", "FN1"]
w0 = {}
for g in w0_genes:
    rec = {}
    for tag, cpm, grp in [("DirectInf", cpm_di, di_groups), ("SeraExo", cpm_se, se_groups)]:
        if g in cpm.index:
            sub = cpm.loc[g]
            # 检测比例：CPM>1 的样本占比
            det = (sub > 1).mean()
            rec[tag] = {"mean_cpm": float(sub.mean()), "detect_frac_cpm1": float(det),
                        "mean_log2cpm": float(L_di.loc[g].mean()) if tag == "DirectInf" else float(L_se.loc[g].mean())}
        else:
            rec[tag] = None
    w0[g] = rec

# HD10 基线（mock 与 control-exo 的平均表达）
baseline = {}
for g in w0_genes:
    baseline[g] = {
        "mock_mean_log2cpm": float(L_di.loc[g].mean()) if g in L_di.index else None,
        "ctrl_exo_mean_log2cpm": float(L_se.loc[g].mean()) if g in L_se.index else None,
    }

# panel 基因在数据中缺失情况
panel_missing = {}
for mod, genes in MODULES.items():
    miss = [g for g in genes if g not in L_di.index and g not in L_se.index]
    panel_missing[mod] = miss

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
    diff_obs = sb.mean() - sa.mean()
    # 每个样本 module score
    sample_scores = sub.mean(axis=0).values
    all_scores_a = sample_scores[idx_a]
    all_scores_b = sample_scores[idx_b]
    t, pt = stats.ttest_ind(all_scores_b, all_scores_a, equal_var=False)
    u, pu = stats.mannwhitneyu(all_scores_b, all_scores_a, alternative="two-sided")
    p_perm, perc = perm_null(diff_obs, sub.values, idx_a, idx_b)
    return {
        "module": modname, "genes_used": len(gpresent), "genes_total": len(genes),
        "mean_A(%s)" % gA: float(sa.mean()), "mean_B(%s)" % gB: float(sb.mean()),
        "diff_B_minus_A": float(diff_obs),
        "t": float(t), "p_ttest": float(pt), "p_wilcoxon": float(pu),
        "p_perm": float(p_perm), "perm_percentile": float(perc),
        "top_genes": sorted(zip(gpresent, (sb - sa).values), key=lambda x: -abs(x[1]))[:8]
    }

contrasts = [
    # (experiment_log2cpm, groups, gA, gB, label)
    (L_se, se_groups, "ctrl_exo", "hz_exo", "HZexo_vs_CtrlExo"),
    (L_se, se_groups, "ctrl_exo", "phn_exo", "PHNexo_vs_CtrlExo"),
    (L_di, di_groups, "mock", "vzv", "VZV_vs_Mock"),
]
results = {"w0": w0, "baseline": baseline, "panel_missing": panel_missing, "contrasts": {}}
for Lm, grp, gA, gB, lab in contrasts:
    results["contrasts"][lab] = {}
    for mod, genes in MODULES.items():
        c = compare(Lm, grp, gA, gB, mod, genes)
        if c:
            results["contrasts"][lab][mod] = c

# ---------- CCI（通道互补指数）：M1 vs E1 在全部检出基因中的平均秩差 ----------
def cci_per_sample(Lm, present_all):
    """CCI = mean(rank of M1 genes) - mean(rank of E1 genes)，rank 按表达量在全部检出基因中升序。"""
    m1 = [g for g in MODULES["M1_mechanogated_channels"] if g in Lm.index]
    e1 = [g for g in MODULES["E1_classical_nociceptor"] if g in Lm.index]
    if len(m1) == 0 or len(e1) == 0:
        return None
    sub = Lm.loc[m1 + e1]
    ranks = sub.rank(axis=0, method="average")  # 每个基因在全部基因中的秩（需在全基因序上排）
    return None  # 占位，下面用全基因秩

def cci_full(Lm, grp, gA, gB, lab):
    present_all = list(Lm.index)
    rank_mat = Lm.rank(axis=0, method="average")  # 每个样本内：基因按表达量秩
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
    # 置换零
    rng = np.random.default_rng(20261019)
    labels = np.array([0]*len(idx_a) + [1]*len(idx_b))
    pool = np.concatenate([idx_a, idx_b])
    B = 5000
    dist = np.empty(B)
    for b in range(B):
        perm = rng.permutation(labels)
        a = pool[perm == 0]; bb = pool[perm == 1]
        dist[b] = cci[bb].mean() - cci[a].mean()
    p_perm = max((np.abs(dist) >= abs(diff_obs)).mean(), 1.0/B)
    perc = (dist <= diff_obs).mean() * 100
    return {"contrast": lab, "m1_n": len(m1), "e1_n": len(e1),
            "mean_CCI_A(%s)" % gA: float(cci[idx_a].mean()),
            "mean_CCI_B(%s)" % gB: float(cci[idx_b].mean()),
            "diff_B_minus_A": float(diff_obs),
            "p_ttest": float(pt), "p_wilcoxon": float(pu), "p_perm": float(p_perm),
            "perm_percentile": float(perc)}

results["CCI"] = {}
for Lm, grp, gA, gB, lab in contrasts:
    c = cci_full(Lm, grp, gA, gB, lab)
    if c:
        results["CCI"][lab] = c

# ---------- 写出 ----------
res_path = os.path.join(OUT, "layer1_results.json")
with open(res_path, "w") as f:
    json.dump(results, f, indent=2, default=str)

# 摘要 CSV（每对比每模块一行）
rows = []
for lab, mods in results["contrasts"].items():
    for mod, c in mods.items():
        rows.append({"contrast": lab, "module": mod, "genes_used": c["genes_used"],
                     "diff": round(c["diff_B_minus_A"], 4),
                     "p_ttest": c["p_ttest"], "p_wilcoxon": c["p_wilcoxon"], "p_perm": c["p_perm"],
                     "perm_pct": round(c["perm_percentile"], 1)})
csv_path = os.path.join(OUT, "layer1_module_scores.csv")
pd.DataFrame(rows).to_csv(csv_path, index=False)

cci_rows = []
for lab, c in results["CCI"].items():
    cci_rows.append({"contrast": lab, "diff_CCI": round(c["diff_B_minus_A"], 4),
                     "p_ttest": c["p_ttest"], "p_wilcoxon": c["p_wilcoxon"], "p_perm": c["p_perm"]})
pd.DataFrame(cci_rows).to_csv(os.path.join(OUT, "layer1_cci.csv"), index=False)

# MANIFEST
manifest = {
    "layer1_results.json": sha256(res_path),
    "layer1_module_scores.csv": sha256(csv_path),
    "inputs": {
        "DirectInf": sha256(os.path.join(RAW, "GSE342782_Processed_DirectInf_neuronHD10s_BulkSeq_Counts.csv.gz")),
        "SeraExo": sha256(os.path.join(RAW, "GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz")),
        "panel": sha256(CFG),
    }
}
with open(os.path.join(OUT, "MANIFEST.json"), "w") as f:
    json.dump(manifest, f, indent=2)

print("\n=== W0 关键检测限（DirectInf=mock/VZV 神经元；SeraExo=外泌体处理）===")
for g in ["PIEZO2", "PIEZO1", "TRPV4", "STOML3", "ITGB1", "YAP1", "LOX", "MMP9"]:
    w = w0[g]
    di = w.get("DirectInf"); se = w.get("SeraExo")
    print(f"  {g:8s} DI_detFrac={di['detect_frac_cpm1'] if di else 'NA':.2f} meanCPM={di['mean_cpm'] if di else 'NA':.2f} | SE_detFrac={se['detect_frac_cpm1'] if se else 'NA':.2f}")

print("\n=== Layer 1 主对比 HZexo_vs_CtrlExo（模块差 + 置换P）===")
for mod, c in results["contrasts"]["HZexo_vs_CtrlExo"].items():
    print(f"  {mod:30s} diff={c['diff_B_minus_A']:+.4f}  p_perm={c['p_perm']:.4g}  p_t={c['p_ttest']:.4g}")

print("\n=== CCI（M1 vs E1 平均秩差）===")
for lab, c in results["CCI"].items():
    print(f"  {lab:22s} diffCCI={c['diff_B_minus_A']:+.4f}  p_perm={c['p_perm']:.4g}")

print("\nDONE. results ->", OUT)
