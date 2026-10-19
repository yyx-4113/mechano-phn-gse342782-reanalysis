#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Round-2 B2 verification: does the E1-vs-M1 selectivity interaction survive
fair normalization (detected-only genes)? Computes the exact-permutation
interaction P both for ALL panel genes (reproduces manuscript) and for
detected-only genes (mean CPM > 1), plus a gene-level selectivity check."""
import json, gzip, os, csv
import numpy as np
import pandas as pd
from scipy import stats
from itertools import combinations

ROOT = "D:/2026.10/机械应力"
RAW = os.path.join(ROOT, "analysis/data/raw")
CFG = os.path.join(ROOT, "analysis/config/mtp_panel.json")

def load_counts(path):
    rows = {}
    with gzip.open(path, "rt") as f:
        r = csv.reader(f); header = next(r); samples = [h for h in header[1:]]
        for row in r:
            g = row[0].strip()
            if not g or g.upper() in ("NA","GENE_SYMBOL"): continue
            try: vals = [float(v) for v in row[1:]]
            except ValueError: continue
            if g in rows: continue
            rows[g] = vals
    return pd.DataFrame(rows, index=samples).T

def to_cpm(df):
    return df.div(df.sum(axis=0), axis=1) * 1e6
def log2cpm(df):
    return np.log2(1 + to_cpm(df))

def perm_exact(diff_obs, values, idx_a, idx_b):
    values = np.asarray(values, dtype=float).ravel()
    pool = np.concatenate([idx_a, idx_b]); na = len(idx_a)
    obs_abs = abs(diff_obs); dists = []
    for idx in combinations(range(len(pool)), na):
        a = values[pool[list(idx)]]
        mask = np.ones(len(pool), dtype=bool); mask[list(idx)] = False
        dists.append(values[pool[mask]].mean() - a.mean())
    dist = np.asarray(dists)
    p = float((np.abs(dist) >= obs_abs - 1e-12).mean())
    return p

with open(CFG) as f: PANEL = json.load(f)
M1 = PANEL["M1_mechanogated_channels"]["genes"]; E1 = PANEL["E1_classical_nociceptor"]["genes"]

se = load_counts(os.path.join(RAW, "GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz"))
L_se = log2cpm(se); cpm_se = to_cpm(se)
se_groups = {s: ("ctrl_exo" if s.startswith("C") else "phn_exo" if s.startswith("P") else "hz_exo" if s.startswith("S") else None) for s in se.columns}
idx_a = [i for i,s in enumerate(se.columns) if se_groups[s]=="ctrl_exo"]
idx_b = [i for i,s in enumerate(se.columns) if se_groups[s]=="hz_exo"]

def interaction_p(genes_x, genes_y, label):
    gx = [g for g in genes_x if g in L_se.index]
    gy = [g for g in genes_y if g in L_se.index]
    sx = L_se.loc[gx].mean(axis=0).values
    sy = L_se.loc[gy].mean(axis=0).values
    d = sx - sy
    diff_obs = d[idx_b].mean() - d[idx_a].mean()
    p = perm_exact(diff_obs, d, idx_a, idx_b)
    return {"genes_x": len(gx), "genes_y": len(gy), "diff": round(diff_obs,4), "p_exact": p}

print("=== EXOSOME HZ vs CTRL: E1-vs-M1 interaction ===")
full = interaction_p(E1, M1, "all")
print("  ALL panel genes:      nE1=%d nM1=%d  diff=%+.4f  p_exact=%.4g" % (full["genes_x"], full["genes_y"], full["diff"], full["p_exact"]))

det_e1 = [g for g in E1 if cpm_se.loc[g].mean() > 1]
det_m1 = [g for g in M1 if cpm_se.loc[g].mean() > 1]
det = interaction_p(det_e1, det_m1, "detected")
print("  DETECTED only (CPM>1): nE1=%d nM1=%d  diff=%+.4f  p_exact=%.4g" % (det["genes_x"], det["genes_y"], det["diff"], det["p_exact"]))

# also report module diffs under detected-only
def mod_diff(genes, idx_a, idx_b):
    g = [x for x in genes if x in L_se.index and cpm_se.loc[x].mean() > 1]
    s = L_se.loc[g].mean(axis=0).values
    return s[idx_b].mean() - s[idx_a].mean()
print("  detected E1 module diff = %+.4f ; detected M1 module diff = %+.4f" % (mod_diff(E1, idx_a, idx_b), mod_diff(M1, idx_a, idx_b)))

# Gene-level selectivity: per-gene welch P for each module under HZ vs Ctrl
A = L_se.iloc[:, idx_a].values; B = L_se.iloc[:, idx_b].values
t, p = stats.ttest_ind(B.T, A.T, axis=0, equal_var=False)
print("\n=== GENE-LEVEL selectivity (HZ vs Ctrl, Welch P) ===")
for mod, genes in [("E1", E1), ("M1", M1)]:
    g = [x for x in genes if x in L_se.index]
    ps = {x: p[L_se.index.get_loc(x)] for x in g}
    sig = [x for x,v in ps.items() if v < 0.05]
    print("  %s: %d genes, individually significant (P<0.05): %d -> %s" % (mod, len(g), len(sig), sorted(sig, key=lambda x: ps[x])[:8]))
