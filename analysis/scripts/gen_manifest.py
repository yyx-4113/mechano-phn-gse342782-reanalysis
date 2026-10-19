#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Regenerate analysis/results/layer1/MANIFEST.json (SHA-256).

Covers, per v1.1.7 reproducibility requirements:
  - every layer1_* result artifact in analysis/results/layer1/
  - all figure PNGs in analysis/results/layer1/fig/
  - both gate reports (consistency + JPR compliance)
  - analysis inputs: the two raw GEO count matrices and the frozen panel

Usage: python analysis/scripts/gen_manifest.py
"""
import hashlib, json, os, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT_DIR = os.path.join(ROOT, "analysis", "results", "layer1")
RAW_DIR = os.path.join(ROOT, "analysis", "data", "raw")
PANEL = os.path.join(ROOT, "analysis", "config", "mtp_panel.json")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


manifest = {
    "manifest_version": "2",
    "generated_utc": datetime.datetime.now(datetime.timezone.utc)
    .strftime("%Y-%m-%dT%H:%M:%SZ"),
    "files": {},
    "figures": {},
    "gate_reports": {},
    "inputs": {},
}

# result artifacts (exclude MANIFEST itself and the fig/ subdir)
for fn in sorted(os.listdir(OUT_DIR)):
    p = os.path.join(OUT_DIR, fn)
    if not os.path.isfile(p) or fn == "MANIFEST.json":
        continue
    if fn.startswith("gate_") and fn.endswith("_report.txt"):
        manifest["gate_reports"][fn] = sha256(p)
    else:
        manifest["files"][fn] = sha256(p)

# figures
fig_dir = os.path.join(OUT_DIR, "fig")
if os.path.isdir(fig_dir):
    for fn in sorted(os.listdir(fig_dir)):
        p = os.path.join(fig_dir, fn)
        if os.path.isfile(p):
            manifest["figures"][fn] = sha256(p)

# inputs
for fn in sorted(os.listdir(RAW_DIR)):
    p = os.path.join(RAW_DIR, fn)
    if os.path.isfile(p) and fn.endswith((".csv.gz", ".txt.gz")):
        manifest["inputs"]["raw/" + fn] = sha256(p)
if os.path.isfile(PANEL):
    manifest["inputs"]["config/mtp_panel.json"] = sha256(PANEL)

out = os.path.join(OUT_DIR, "MANIFEST.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=1, ensure_ascii=False)
n = len(manifest["files"]) + len(manifest["figures"]) + len(manifest["gate_reports"]) + len(manifest["inputs"])
print(f"MANIFEST written: {out} ({n} entries: {len(manifest['files'])} files, "
      f"{len(manifest['figures'])} figures, {len(manifest['gate_reports'])} gate reports, "
      f"{len(manifest['inputs'])} inputs)")
