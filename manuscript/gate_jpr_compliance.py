#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""JPR (Dove Press) submission-compliance gate.

独立于 gate_consistency.py：后者校验"稿件数字 == 产物数字"（自洽性），
本脚本校验"稿件形态 == 期刊要求"（合规性）。两者都绿才算可投稿。

检查项均从 Author Guidelines (Dove Medical Press) 派生：
  - 结构化摘要 <= 300 词
  - 关键词 3-6 个
  - 参考文献编号连续 (1..N)
  - 美式拼写（无 -ise/-isation/-our 等英式残留）
  - 图表须在正文中被引用
  - 通讯作者须含邮箱 / 通信地址 / 电话
  - 必备声明章节齐全

用法: python gate_jpr_compliance.py
退出码 0 表示全部通过。
"""
import re
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
MD_PATH = _ROOT / "manuscript" / "manuscript_v1.1.4.md"

PASS = 0
FAIL = 0
LINES = []


def chk(label, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        LINES.append(f"PASS  {label}" + (f"  [{detail}]" if detail else ""))
    else:
        FAIL += 1
        LINES.append(f"FAIL  {label}  [{detail}]")


def words(s):
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'-]*", s))


def main():
    if not MD_PATH.exists():
        print(f"missing manuscript: {MD_PATH}")
        return 1
    t = MD_PATH.read_text(encoding="utf-8")

    # ---- 1. abstract <= 300 words (excluding the Keywords line) ----
    m = re.search(r"## Abstract(.*?)\n## ", t, re.S)
    chk("abstract block present", bool(m))
    if m:
        core = m.group(1).split("**Keywords:**")[0]
        n = words(core)
        chk(f"abstract <= 300 words (actual {n})", n <= 300, f"limit 300, got {n}")

    # ---- 2. keywords 3-6 ----
    kw = re.search(r"\*\*Keywords:\*\*(.*)", t)
    if kw:
        k = [x.strip() for x in kw.group(1).strip("* ").split(";") if x.strip()]
        chk(f"keywords count 3-6 (actual {len(k)})", 3 <= len(k) <= 6, "; ".join(k))
    else:
        chk("keywords line present", False)

    # ---- 3. references contiguous 1..N ----
    nums = [int(x) for x in re.findall(r"^\[(\d+)\]", t, re.M)]
    chk(f"reference numbering contiguous 1..N (N={len(nums)})",
        bool(nums) and nums == list(range(1, len(nums) + 1)))

    # ---- 4. American spelling ----
    brit = ["programme", "signalling", "immortalised", "emphasise", "centred",
            "hypothesised", "analysed", "organised", "recognised", "behaviour",
            "tumour", "labelled", "modelling", "utilised", "favour", "licence",
            "defence", "haemat", "oesophag", "paediatric", "standardised",
            "characterised", "minimise", "maximise", "optimise"]
    hits = {w: len(re.findall(w, t, re.I)) for w in brit if re.search(w, t, re.I)}
    chk("no British-spelling residue", not hits, str(hits) if hits else "clean")

    # ---- 5. figures and tables cited in text ----
    for fig in ["Figure 1", "Figure 2a", "Figure 2b", "Figure 2c", "Figure 2d"]:
        chk(f"{fig} cited in text", fig in t)
    chk("Table 1 cited in text", "Table 1" in t)

    # ---- 6. corresponding author contact block ----
    chk("corresponding e-mail present", bool(re.search(r"[\w.+-]+@[\w-]+\.\w+", t)))
    chk("ORCID present", "ORCID" in t)
    chk("postal address present", "Fuzhou, Fujian 350003" in t)
    chk("telephone present", bool(re.search(r"Tel(ephone)?\s*:", t, re.I)))
    chk("fax present", bool(re.search(r"Fax\s*:", t, re.I)))

    # ---- 7. mandatory sections ----
    for sec in ["## Abstract", "## Data availability",
                "## Ethics approval and consent to participate",
                "## Consent for publication", "## Author contributions",
                "## Declaration of interests", "## Funding", "## References"]:
        chk(f"section present: {sec.replace('## ', '')}", sec in t)

    # ---- 8. running title ----
    chk("running title present", bool(re.search(r"Running title\s*:", t, re.I)))

    # ---- 9. no truncated / placeholder fragments ----
    for bad in ["[truncated]", "TODO", "XXX", "Lorem", "[insert"]:
        chk(f"no placeholder '{bad}'", bad not in t)

    out = "\n".join(LINES)
    print(out)
    print()
    print(f"TOTAL {PASS + FAIL} checks | PASS {PASS} | FAIL {FAIL}")
    rep = _ROOT / "analysis" / "results" / "layer1" / "gate_jpr_compliance_report.txt"
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text(out + f"\n\nTOTAL {PASS + FAIL} | PASS {PASS} | FAIL {FAIL}\n",
                   encoding="utf-8")
    print("report ->", rep)
    return 0 if FAIL == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
