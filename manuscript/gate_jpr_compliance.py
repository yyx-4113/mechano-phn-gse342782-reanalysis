#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""JPR (Dove Press) submission-compliance gate.
v1.1.9 修订（降 AI 痕迹润色后）：
  - MD_PATH 指向 manuscript_v1.1.9.md；VERSION 更新为 v1.1.9；
  - 润色未改任何数字/引文/论点（numeric set-diff v1.1.7→v1.1.8 双向为空；
    摘要词数仍为 294，≤300），故全部断言沿用。
v1.1.7 修订（Round-2 审稿后）：
  - MD_PATH 指向 manuscript_v1.1.7.md；
  - 新增：引用完整性（cited set == list set）、AMA 首次出现顺序、
    图题注存在性与题注限定词（interaction P 必须带 post hoc / detected-gene 限定）、
    无内部轮次标签、无 "pre-registered" 品牌、tag 版本一致、
    cover letter / README 与稿件一致性；
  - 英式拼写词表扩充（artefact/enrol/behaviour 等）。
独立于 gate_consistency.py：后者校验"稿件数字 == 产物数字"（自洽性），
本脚本校验"稿件形态 == 期刊要求"（合规性）。两者都绿才算可投稿。

检查项均从 Author Guidelines (Dove Medical Press) 派生：
  - 结构化摘要 <= 300 词
  - 关键词 3-6 个
  - 参考文献编号连续 (1..N)、全部被正文引用、按首次出现顺序编号
  - 美式拼写（无 -ise/-isation/-our 等英式残留）
  - 图表须在正文中被引用；每张图须有题注
  - 通讯作者须含邮箱 / 通信地址 / 电话
  - 必备声明章节齐全
  - 无内部流程标签 / 占位符 / 超前品牌声明

用法: python gate_jpr_compliance.py
退出码 0 表示全部通过。
"""
import re
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
MD_PATH = _ROOT / "manuscript" / "manuscript_v1.1.9.md"
LETTER_PATH = _ROOT / "manuscript" / "cover_letter_JPR.md"
README_PATH = _ROOT / "README.md"
VERSION = "v1.1.9"

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
    body, _, refs = t.partition("## References")

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
    nums = [int(x) for x in re.findall(r"^\[(\d+)\]", refs, re.M)]
    chk(f"reference numbering contiguous 1..N (N={len(nums)})",
        bool(nums) and nums == list(range(1, len(nums) + 1)))

    # ---- 3b. citation completeness: every listed reference is cited in text ----
    cites = []
    for c in re.findall(r"\^([\d,\-]+)\^", body):
        for part in c.split(","):
            if "-" in part:
                a, b = part.split("-"); cites.extend(range(int(a), int(b) + 1))
            else:
                cites.append(int(part))
    chk("cited set == listed set (no uncited references)",
        bool(nums) and set(cites) == set(nums),
        f"uncited: {sorted(set(nums) - set(cites))}")
    seen = []
    for n in cites:
        if n not in seen:
            seen.append(n)
    chk("AMA first-appearance order is sequential",
        seen == sorted(seen) and seen == nums,
        f"order: {seen}")

    # ---- 3c. reference-year presence (every entry carries a publication year) ----
    no_year = [ln.split("]")[0] + "]" for ln in refs.splitlines()
               if re.match(r"^\[\d+\]", ln) and not re.search(r"\b(19|20)\d{2}\b", ln)]
    chk("every reference entry carries a year", not no_year, str(no_year))

    # ---- 4. American spelling ----
    brit = ["programme", "signalling", "immortalised", "emphasise", "centred",
            "hypothesised", "analysed", "organised", "recognised", "behaviour",
            "tumour", "labelled", "modelling", "utilised", "favour", "licence",
            "defence", "haemat", "oesophag", "paediatric", "standardised",
            "characterised", "minimise", "maximise", "optimise", "artefact",
            "enrol ", "colour", "normalisation"]
    hits = {w: len(re.findall(w, t, re.I)) for w in brit if re.search(w, t, re.I)}
    chk("no British-spelling residue", not hits, str(hits) if hits else "clean")

    # ---- 5. figures and tables cited in text ----
    for fig in ["Figure 1", "Figure 2a", "Figure 2b", "Figure 2c", "Figure 2d"]:
        chk(f"{fig} cited in text", fig in body)
    chk("Table 1 cited in text", "Table 1" in body)

    # ---- 5b. every figure has a caption in the md ----
    caps = re.findall(r"^> (Figure [12][a-d]?)\.", t, re.M)
    have = set(caps)
    chk("all 5 figure captions present in md",
        have == {"Figure 1", "Figure 2a", "Figure 2b", "Figure 2c", "Figure 2d"},
        f"found: {sorted(have)}")

    # ---- 5c. caption claim discipline: interaction P in captions must be qualified ----
    cap_text = "\n".join(ln for ln in t.splitlines() if ln.startswith("> "))
    if "P = 0.0017" in cap_text:
        ok = ("post hoc" in cap_text.lower()) and ("0.16" in cap_text)
        chk("figure caption carrying interaction P is qualified (post hoc + detected-gene P = 0.16)", ok)
    else:
        chk("no unqualified interaction P in captions", True)

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

    # ---- 9. no truncated / placeholder / internal-process fragments ----
    for bad in ["[truncated]", "TODO", "XXX", "Lorem", "[insert",
                "Round-4", "Round 4", "internal benchmark"]:
        chk(f"no placeholder/internal label '{bad}'", bad not in t)

    # ---- 9b. branding discipline: no pre-registration claim (no external registry) ----
    chk("no 'pre-registered' branding in manuscript", not re.search(r"pre-?registered", t, re.I))
    chk("registration sentence states no external registry entry",
        "no external registry entry" in t)

    # ---- 9c. data-availability tag currency ----
    chk(f"data availability cites tag {VERSION}",
        f"tag {VERSION}" in t, f"looking for 'tag {VERSION}'")

    # ---- 10. cover letter / README consistency ----
    if LETTER_PATH.exists():
        L = LETTER_PATH.read_text(encoding="utf-8")
        title = t.splitlines()[0].lstrip("# ").strip()
        chk("cover letter title matches manuscript title", title in L)
        chk("cover letter does not redefine PHN by its symptom",
            "clinically defined by mechanical allodynia" not in L)
        chk("cover letter has no pre-registered branding",
            not re.search(r"pre-?registered", L, re.I))
    else:
        chk("cover letter present", False)
    if README_PATH.exists():
        R = README_PATH.read_text(encoding="utf-8")
        chk("repository README has no pre-registered branding",
            not re.search(r"pre-?registered", R, re.I))
    else:
        chk("repository README present", False)

    out = "\n".join(LINES)
    print(out)
    print()
    print(f"TOTAL {PASS + FAIL} checks | PASS {PASS} | FAIL {FAIL}")
    rep = _ROOT / "analysis" / "results" / "layer1" / "gate_jpr_compliance_report.txt"
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text(out + f"\n\nTOTAL {PASS + FAIL} checks | PASS {PASS} | FAIL {FAIL}\n",
                   encoding="utf-8")
    print("report ->", rep)
    return 0 if FAIL == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
