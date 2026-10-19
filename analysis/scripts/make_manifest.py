#!/usr/bin/env python3
"""Generate the root SHA-256 MANIFEST.json over all deposited reproducibility
artifacts (working tree).

Usage: python analysis/scripts/make_manifest.py <tag>   (default: v1.1.7)

Excludes: .workbuddy/, __pycache__/, *.pyc, manuscript/archive/ (superseded
manuscript versions), reviewer scratch dirs (analysis/scratch_*, _B3_audit/),
the unused GSE64345 raw file, and this script itself. Relative keys use
forward slashes for cross-platform verification; MANIFEST.json itself is not
hashed (a manifest cannot contain its own digest — its integrity is carried
by the release SHA-256 file and the git tag).
"""
import hashlib, json, os, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TAG = sys.argv[1] if len(sys.argv) > 1 else "v1.1.7"
GENERATED = datetime.date.today().isoformat()

EXCLUDE_DIRS = {".workbuddy", "__pycache__", ".git", "archive", ".tmpcheck",
                "scratch_B2", "scratch_B3", "scratch_editor", "_B3_audit"}
EXCLUDE_FILES = {"make_manifest.py"}
EXCLUDE_SUFFIX = {".pyc"}
EXCLUDE_PATH_FRAGMENTS = ["GSE64345", "scratch_", "_B3_audit"]  # local scratch; unused raw data

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
        rel = os.path.relpath(full, ROOT).replace(os.sep, "/")
        # only include files under tracked top-level dirs (rel uses "/")
        top = rel.split("/")[0]
        if top in ("analysis", "manuscript", "reviews", ".github"):
            records[rel] = sha256(full)

# ---- root-level provenance docs (README, LICENSE, CITATION.cff, protocol, SOP, etc.) ----
# NOTE: MANIFEST.json itself is deliberately NOT hashed (a manifest cannot
# contain its own digest); its integrity is carried by the release SHA-256
# file and the git tag.
ROOT_DOCS = ("README.md", "LICENSE", "CITATION.cff",
             "GITHUB_DEPOSIT_SOP.md", "author_verification_statement.md",
             "PROTOCOL_机械应力与PHN.md", ".gitignore", "requirements.txt",
             "analysis/scripts/make_manifest.py")
ROOT_DOCS += tuple(sorted(fn for fn in os.listdir(ROOT)
                          if fn.startswith("release_notes_") and fn.endswith(".md")))
for name in ROOT_DOCS:
    p = os.path.join(ROOT, name)
    if os.path.exists(p):
        records[name] = sha256(p)

out = {
    "generated": GENERATED,
    "algorithm": "sha256",
    "repository": "https://github.com/yyx-4113/mechano-phn-gse342782-reanalysis",
    "tag": TAG,
    "files": records,
}
with open(os.path.join(ROOT, "MANIFEST.json"), "w") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print(f"MANIFEST.json written: {len(records)} files")
for k in sorted(records):
    print(f"  {k}: {records[k][:16]}...")
