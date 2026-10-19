#!/usr/bin/env python3
"""Generate SHA-256 MANIFEST.json over all deposited reproducibility artifacts.

Excludes: .workbuddy/, __pycache__/, *.pyc, the unused GSE64345 raw file,
and this script itself.
"""
import hashlib, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

EXCLUDE_DIRS = {".workbuddy", "__pycache__", ".git", "archive", ".tmpcheck"}
EXCLUDE_FILES = {"make_manifest.py"}
EXCLUDE_SUFFIX = {".pyc"}
EXCLUDE_PATH_FRAGMENTS = ["GSE64345"]  # downloaded but unused raw data

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

records = {}
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
    for fn in sorted(filenames):
        if fn in EXCLUDE_FILES or fn.endswith(tuple(EXCLUDE_SUFFIX)):
            continue
        full = os.path.join(dirpath, fn)
        if any(frag in full for frag in EXCLUDE_PATH_FRAGMENTS):
            continue
        rel = os.path.relpath(full, ROOT)
        # only include files under tracked top-level dirs
        top = rel.split(os.sep)[0]
        if top in ("analysis", "manuscript", ".github"):
            records[rel] = sha256(full)

# ---- root-level provenance docs (README, LICENSE, CITATION.cff, protocol, SOP, etc.) ----
ROOT_DOCS = ("README.md", "LICENSE", "CITATION.cff", "MANIFEST.json",
             "GITHUB_DEPOSIT_SOP.md", "author_verification_statement.md",
             "PROTOCOL_机械应力与PHN.md", ".gitignore",
             "analysis/scripts/make_manifest.py")
for name in ROOT_DOCS:
    p = os.path.join(ROOT, name)
    if os.path.exists(p):
        records[name] = sha256(p)

out = {
    "generated": "2026-10-19",
    "algorithm": "sha256",
    "repository": "https://github.com/yyx-4113/mechano-phn-gse342782-reanalysis",
    "tag": "v1.1.4",
    "files": records,
}
with open(os.path.join(ROOT, "MANIFEST.json"), "w") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print(f"MANIFEST.json written: {len(records)} files")
for k in sorted(records):
    print(f"  {k}: {records[k][:16]}...")
