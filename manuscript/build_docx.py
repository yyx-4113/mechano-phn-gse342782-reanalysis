#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""manuscript .md -> .docx（Times New Roman 12pt，标题层级，图表插入）。
遵循用户约定：cover/manuscript 生成 Times New Roman 12pt；不使用花哨模板。"""
import re, os
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

MD = "D:/2026.10/机械应力/manuscript/manuscript_v1.0.0.md"
FIG = "D:/2026.10/机械应力/analysis/results/layer1/fig"
OUT = "D:/2026.10/机械应力/manuscript/manuscript_v1.0.0.docx"

doc = Document()
style = doc.styles["Normal"]
style.font.name = "Times New Roman"
style.font.size = Pt(12)

def add_par(text, bold=False, size=12, align=None, italic=False):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.font.name = "Times New Roman"; r.font.size = Pt(size)
    r.bold = bold; r.italic = italic
    if align: p.alignment = align
    return p

def add_rich(text, size=12, style_bold_all=False):
    """处理 **bold** 与 *italic* 行内标记。"""
    p = doc.add_paragraph()
    tokens = re.split(r"(\*\*.+?\*\*|\*.+?\*)", text)
    for t in tokens:
        if not t: continue
        if t.startswith("**") and t.endswith("**"):
            r = p.add_run(t[2:-2]); r.bold = True
        elif t.startswith("*") and t.endswith("*") and len(t) > 2:
            r = p.add_run(t[1:-1]); r.italic = True
        else:
            r = p.add_run(t)
        r.font.name = "Times New Roman"; r.font.size = Pt(size)
        if style_bold_all: r.bold = True
    return p

lines = open(MD, encoding="utf-8").read().splitlines()
fig_inserted = set()
# 图插入映射：在特定标题后插入图
insert_after = {
    "2.3 Preprocessing and module scoring": None,  # 占位
}

i = 0
first_line = True
while i < len(lines):
    line = lines[i].rstrip()
    if not line.strip():
        i += 1; continue
    if line.startswith("# ") and first_line:
        add_par(line[2:].strip(), bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER)
        first_line = False
    elif line.startswith("# "):
        add_par(line[2:].strip(), bold=True, size=14)
    elif line.startswith("## "):
        add_par(line[3:].strip(), bold=True, size=12.5)
        # 在 Results 节后插图
        h = line[3:].strip()
        if h.startswith("3.4 Double dissociation"):
            for fn, cap in [("fig2a_module_scores.png", "Figure 2a. Module-score differences for the primary contrast (HZ-exo vs control-exo), with neutral controls displayed alongside. E1 is the only biological module significantly shifted."),
                            ("fig2b_cci.png", "Figure 2b. Channel-complementarity index (CCI) differences by contrast (all non-significant)."),
                            ("fig2c_E1_genes.png", "Figure 2c. Gene-level differences within E1 for the primary contrast: coherent suppression of classical nociceptor channels."),
                            ("fig2d_dissociation.png", "Figure 2d. Double dissociation between perturbation route and channel programme (M1 vs E1).")]:
                if fn not in fig_inserted:
                    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p.add_run().add_picture(os.path.join(FIG, fn), width=Inches(5.8))
                    add_par(cap, size=10, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)
                    fig_inserted.add(fn)
        elif h.startswith("3.1 Data examination") and "fig1_design.png" not in fig_inserted:
            p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.add_run().add_picture(os.path.join(FIG, "fig1_design.png"), width=Inches(6.2))
            add_par("Figure 1. Study design and pre-registered analysis pipeline.", size=10, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)
            fig_inserted.add("fig1_design.png")
    elif line.startswith("### "):
        add_par(line[4:].strip(), bold=True, size=12)
    elif line.strip() == "---":
        pass
    elif line.startswith("> "):
        add_par(line[2:].strip(), size=10, italic=True)
    elif line.startswith("- "):
        add_rich("• " + line[2:].strip(), size=12)
    elif re.match(r"^\[\d+\]", line) or line.startswith("[1]"):
        add_par(line.strip(), size=11)
    elif line.startswith("**") and line.rstrip().endswith("**") and len(line) < 80:
        add_par(line.strip("*"), bold=True, size=12)
    else:
        add_rich(line.strip(), size=12)
    i += 1

doc.save(OUT)
print("docx saved:", OUT)

# 字数统计（正文近似：摘要+正文，不含标题行/参考文献）
body = []
in_ref = False
for line in lines:
    s = line.strip()
    if s.startswith("## References"): in_ref = True
    if not s or s.startswith("#") or s == "---": continue
    if in_ref: continue
    body.append(s)
wc = len(" ".join(body).split())
print("main-text word count (incl. abstract, excl. refs):", wc)
