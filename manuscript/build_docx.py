#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""manuscript .md -> .docx (Times New Roman 12pt, heading levels, tables, figures).
遵循用户约定：cover/manuscript 生成 Times New Roman 12pt；不使用花哨模板。
v1.1.0 修订：修正图插入层级（### 3.x 也是 h3），支持 markdown 表格渲染（Table 1）。
v1.1.7 修订：
  - MD/OUT 指向 manuscript_v1.1.7；
  - 图件改由 md 中的题注 blockquote 驱动插入（md 是题注的唯一来源，避免双份题注）；
  - 题注文件映射更新为重编号后的文件名（fig2b_E1_genes / fig2c_dissociation / fig2d_cci）。
"""
import re, os
from pathlib import Path
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

# 路径相对仓库根（manuscript/ 上溯一级），避免绝对路径不可移植
_ROOT = Path(__file__).resolve().parents[1]
MD = str(_ROOT / "manuscript" / "manuscript_v1.1.7.md")
FIG = str(_ROOT / "analysis" / "results" / "layer1" / "fig")
OUT = str(_ROOT / "manuscript" / "manuscript_v1.1.7.docx")

# 题注前缀 -> (图文件, 宽度 inch)。题注 blockquote 在 md 中的位置即插图位置。
FIG_MAP = {
    "Figure 1.":  ("fig1_design.png", 6.2),
    "Figure 2a.": ("fig2a_module_scores.png", 5.8),
    "Figure 2b.": ("fig2b_E1_genes.png", 5.8),
    "Figure 2c.": ("fig2c_dissociation.png", 5.8),
    "Figure 2d.": ("fig2d_cci.png", 5.8),
}

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

def add_rich(text, size=12, bold_all=False):
    """处理 **bold** / *italic* / ^superscript^(Dove 上标引用) 行内标记。"""
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 2.0  # Dove 要求双倍行距
    tokens = re.split(r"(\*\*.+?\*\*|\*.+?\*|\^.+?\^)", text)
    for t in tokens:
        if not t: continue
        if t.startswith("**") and t.endswith("**"):
            r = p.add_run(t[2:-2]); r.bold = True
        elif t.startswith("*") and t.endswith("*") and len(t) > 2:
            r = p.add_run(t[1:-1]); r.italic = True
        elif t.startswith("^") and t.endswith("^") and len(t) > 2:
            r = p.add_run(t[1:-1])
            r.font.superscript = True  # Dove: 上标阿拉伯数字，无括号
        else:
            r = p.add_run(t)
        r.font.name = "Times New Roman"; r.font.size = Pt(size)
        if bold_all: r.bold = True
    return p

def heading_text(line):
    """提取标题纯文本（去 # 与首尾空白）。"""
    return line.lstrip("#").strip()

def is_table_row(line):
    s = line.strip()
    return s.startswith("|") and s.endswith("|")

def is_separator(line):
    s = line.strip()
    return bool(re.fullmatch(r"\|\s*-{2,}.*\|", s)) or set(s) <= set("|-: ")

def render_table(rows):
    """rows: list of raw '| a | b | c |' 字符串（不含分隔行）。"""
    # 以首行定列数
    cells = [c.strip() for c in rows[0].strip().strip("|").split("|")]
    ncol = len(cells)
    table = doc.add_table(rows=1, cols=ncol)
    table.style = "Light Grid Accent 1"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = table.rows[0].cells
    for i, c in enumerate(cells):
        hdr[i].text = ""
        run = hdr[i].paragraphs[0].add_run(c)
        run.bold = True; run.font.name = "Times New Roman"; run.font.size = Pt(10)
    for r in rows[1:]:
        vals = [c.strip() for c in r.strip().strip("|").split("|")]
        vals = (vals + [""] * ncol)[:ncol]
        cells_ = table.add_row().cells
        for i, v in enumerate(vals):
            cells_[i].text = ""
            run = cells_[i].paragraphs[0].add_run(v)
            run.font.name = "Times New Roman"; run.font.size = Pt(10)
    doc.add_paragraph()

def add_figure(caption_text):
    """按题注文本前缀插图，然后输出题注（居中、斜体、10pt）。"""
    key = next((k for k in FIG_MAP if caption_text.startswith(k)), None)
    if key is not None:
        fn, width = FIG_MAP[key]
        fp = os.path.join(FIG, fn)
        if os.path.exists(fp):
            p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.add_run().add_picture(fp, width=Inches(width))
    add_par(caption_text, size=10, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

lines = open(MD, encoding="utf-8").read().splitlines()
i = 0
first_line = True
while i < len(lines):
    line = lines[i].rstrip()
    if not line.strip():
        i += 1; continue
    if is_table_row(line):
        # 收集连续表格行（跳过分隔行）
        tbl = []
        while i < len(lines) and is_table_row(lines[i]):
            if not is_separator(lines[i]):
                tbl.append(lines[i].rstrip())
            i += 1
        if len(tbl) >= 2:
            render_table(tbl)
        continue
    if line.startswith("# ") and first_line:
        add_par(heading_text(line), bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER)
        first_line = False
    elif line.startswith("# "):
        add_par(heading_text(line), bold=True, size=14)
    elif line.startswith("## "):
        add_par(heading_text(line), bold=True, size=12.5)
    elif line.startswith("### "):
        add_par(heading_text(line), bold=True, size=12)
    elif line.strip() == "---":
        pass
    elif line.startswith("> "):
        add_figure(line[2:].strip())
    elif line.startswith("- "):
        add_rich("• " + line[2:].strip(), size=12)
    elif line.startswith("[") and re.match(r"^\[\d+\]", line):
        add_par(line.strip(), size=11)
    elif line.startswith("**") and line.rstrip().endswith("**") and len(line) < 80:
        add_par(line.strip("*"), bold=True, size=12)
    else:
        add_rich(line.strip(), size=12)
    i += 1


# ---------- Dove 排版要求：连续行号 + 页脚页码 ----------
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

_sec = doc.sections[0]
_sectPr = _sec._sectPr
_ln = OxmlElement("w:lnNumType")
_ln.set(qn("w:countBy"), "1")
_ln.set(qn("w:start"), "1")
_ln.set(qn("w:numRestart"), "continuous")   # 连续行号
_ln.set(qn("w:distance"), "283")            # ~0.5 cm（twips）
_sectPr.append(_ln)

_footer = _sec.footer
_fp = _footer.paragraphs[0]
_fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
_fld = OxmlElement("w:fldSimple")
_fld.set(qn("w:instr"), "PAGE")
_run = OxmlElement("w:r")
_txt = OxmlElement("w:t")
_txt.text = "1"
_run.append(_txt)
_fld.append(_run)
_fp._p.append(_fld)

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
