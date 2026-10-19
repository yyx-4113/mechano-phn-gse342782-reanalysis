#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Layer 1 诊断：基因级 DE + 全局位移核查（决定主叙事是否需切换预案）。"""
import json, os, gzip, csv
import numpy as np
import pandas as pd
from scipy import stats

RAW = "D:/2026.10/机械应力/analysis/data/raw"
CFG = "D:/2026.10/机械应力/analysis/config/mtp_panel.json"
OUT = "D:/2026.10/机械应力/analysis/results/layer1"
with open(CFG) as f:
    PANEL = json.load(f)

def load_counts(path):
    rows = {}
    with gzip.open(path, "rt") as f:
        r = csv.reader(f); next(r)
        for row in r:
            g = row[0].strip()
            if not g: continue
            try: vals = [float(v) for v in row[1:]]
            except ValueError: continue
            if g not in rows: rows[g] = vals
    return pd.DataFrame(rows, index=[h for h in pd.read_csv(path.replace('.gz',''), nrows=1, header=None).iloc[0,1:]]).T

# 用已有函数重读
import importlib.util
spec = importlib.util.spec_from_file_location("l1", os.path.join(os.path.dirname(__file__), "layer1_mechano.py"))
# 直接重算更稳
def load(path):
    rows = {}
    with gzip.open(path, "rt") as f:
        r = csv.reader(f); next(r)
        for row in r:
            g = row[0].strip()
            if not g or g.upper() == "NA": continue
            try: vals = [float(v) for v in row[1:]]
            except ValueError: continue
            if g not in rows: rows[g] = vals
    return pd.DataFrame(rows).T
di = load(os.path.join(RAW, "GSE342782_Processed_DirectInf_neuronHD10s_BulkSeq_Counts.csv.gz"))
se = load(os.path.join(RAW, "GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz"))
se.columns = ["C11","C15","C18","C2","C20","C21","C5","P1","P10","P4","P7","P9","S17","S24","S27","S34","S44","S45","S62"]
cpm = se.div(se.sum(axis=0), axis=1)*1e6
L = np.log2(1+cpm)
grp = {s:("ctrl" if s.startswith("C") else "phn" if s.startswith("P") else "hz") for s in se.columns}
idx_ctrl = [i for i,s in enumerate(se.columns) if grp[s]=="ctrl"]
idx_hz = [i for i,s in enumerate(se.columns) if grp[s]=="hz"]
idx_phn = [i for i,s in enumerate(se.columns) if grp[s]=="phn"]

# 1) 全局位移：每基因 HZ vs ctrl Welch t，统计上/下调数量
genes = L.index.values
tstat,pval = np.zeros(len(genes)),np.zeros(len(genes))
for i in range(len(genes)):
    a = L.iloc[i, idx_ctrl].values; b = L.iloc[i, idx_hz].values
    if a.std()==0 and b.std()==0:
        tstat[i]=0; pval[i]=1
    else:
        tt,pp = stats.ttest_ind(b,a,equal_var=False); tstat[i]=tt; pval[i]=pp
logfc = L.iloc[:,idx_hz].mean(axis=1).values - L.iloc[:,idx_ctrl].mean(axis=1).values
up = (logfc>0.5).sum(); down=(logfc<-0.5).sum()
print(f"全局位移(HZ vs ctrl): 上调(|LFC|>0.5) {up} 基因, 下调 {down} 基因, 共 {len(genes)}")
# 样本级全局均值位移
print("各样本全局 mean log2CPM:", dict(zip(se.columns, np.round(L.mean(axis=0).values,3))))

# 2) 基因级 DE within panel
def gene_de(mod_genes, label):
    print(f"\n--- {label} 基因级 (HZ vs ctrl) ---")
    out=[]
    for g in mod_genes:
        if g not in L.index: 
            print(f"  {g}: 不在数据"); continue
        i = L.index.get_loc(g)
        a = L.iloc[i, idx_ctrl].values; b = L.iloc[i, idx_hz].values
        tt,pp = stats.ttest_ind(b,a,equal_var=False)
        lfc = b.mean()-a.mean()
        out.append((g,lfc,pp))
    out.sort(key=lambda x:-abs(x[1]))
    for g,lfc,pp in out[:12]:
        print(f"  {g:10s} LFC={lfc:+.3f} p={pp:.4g}")
    return out

M1 = PANEL["M1_mechanogated_channels"]["genes"]
M3 = PANEL["M3_ecm_integrin_hippo"]["genes"]
E1 = PANEL["E1_classical_nociceptor"]["genes"]
gene_de(M1, "M1 mechanogated")
gene_de(M3, "M3 ECM-integrin-Hippo")
gene_de(E1, "E1 classical nociceptor")

# 3) PHN vs ctrl 基因级 E1/M3
print("\n=== PHN vs ctrl 全局 ===")
t2,p2=np.zeros(len(genes)),np.zeros(len(genes))
for i in range(len(genes)):
    a=L.iloc[i,idx_ctrl].values; b=L.iloc[i,idx_phn].values
    if a.std()==0 and b.std()==0: t2[i]=0;p2[i]=1
    else:
        tt,pp=stats.ttest_ind(b,a,equal_var=False); t2[i]=tt;p2[i]=pp
lfc2=L.iloc[:,idx_phn].mean(axis=1).values-L.iloc[:,idx_ctrl].mean(axis=1).values
print(f"PHN vs ctrl 上调(|LFC|>0.5) {(lfc2>0.5).sum()} 下调 {(lfc2<-0.5).sum()}")

# 保存诊断
diag = {"global_HZvsCtrl_up": int(up), "global_HZvsCtrl_down": int(down),
        "sample_mean_log2cpm": dict(zip(se.columns, np.round(L.mean(axis=0).values,3).tolist()))}
with open(os.path.join(OUT,"layer1_diag.json"),"w") as f:
    json.dump(diag,f,indent=2)
print("\nDONE diag")
