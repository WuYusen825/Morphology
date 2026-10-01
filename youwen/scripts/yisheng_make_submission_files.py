#!/usr/bin/env python3
"""Builds the submission files of a paper version from its full Markdown text, in the form Morphology (Springer) asks for.

From youwen/manuscript/yisheng_paper_<v>.md it makes
  yisheng_paper_<v>_anonymised.md  the manuscript for double-anonymous review: no authors, affiliation or contributions,
                                   no repository owner in links (the declarations that name nobody stay)
  yisheng_<v>_title_page.md        title, authors, affiliation, corresponding author, ORCID, acknowledgements and all
                                   Statements and Declarations (placeholders, highlighted in Word, for what only the authors know)
  yisheng_<v>_cover_letter.md      cover letter to the editors
and the Word files yisheng_paper_<v>.docx, ..._anonymised.docx, yisheng_<v>_title_page.docx, yisheng_<v>_cover_letter.docx.
Copies of the last four, under the names the submission system gets, go to youwen/manuscript/submission/:
Manuscript_anonymised.docx, Title_page.docx, Cover_letter.docx (the figure files Fig1.* come from yisheng_v10_figure.py).

Word layout (Springer's text rules): A4, Times New Roman 11 pt, 1.5 lines, decimal headings of at most three levels, automatic
page numbers (the one field the file has), real tables with three rules and a bold header row, table notes with superscript
letters, captions "Fig. n" / "Table n" in bold, APA-style references with a hanging indent, no endnotes. The reference
document for pandoc is made here from pandoc's own default, so the layout does not depend on an old Word file.
The build stops with an AssertionError if a string that identifies the authors is left in the anonymised files, if the Word
file of the anonymised manuscript carries an author in its properties, or if the tables, the figure or the page number did
not reach the Word files. Run  python3 youwen/scripts/yisheng_submission_audit.py  afterwards for the guideline checks.

Run from anywhere:  python3 youwen/scripts/yisheng_make_submission_files.py v10
                    ... --allow-todo   builds although ⟦...⟧ markers or [TO BE SUPPLIED] placeholders remain (they are listed)
Word counts only:   ... v10 --count
"""
import re
import shutil
import subprocess
import sys
import tempfile
import warnings
import zipfile
from pathlib import Path

warnings.filterwarnings("ignore", message="style lookup by style_id")

M = Path(__file__).resolve().parents[1] / "manuscript"
SUBMISSION = M / "submission"
AUTHORS = "Yusen Wu and Weiyi Qu"
AFFILIATION = "Beijing Foreign Studies University, School of English and International Studies, Beijing, China"
REVEALING = ["Yusen", "Weiyi", "WuYusen", "Beijing Foreign", "BFSU", "Foreign Studies", "github.com/WuYusen825"]

# What only the authors can supply; None leaves a highlighted placeholder on the title page and in the cover letter.
CORRESPONDING = None          # e.g. "Weiyi Qu"
EMAILS = None                 # e.g. {"Yusen Wu": "...", "Weiyi Qu": "..."}
ORCIDS = None                 # e.g. {"Yusen Wu": "0000-0000-0000-0000", "Weiyi Qu": "..."}
CONTRIBUTIONS = None          # the statement as the authors want it
PRIOR_PUBLICATION_CONFIRMED = False
EDITORIAL_BOARD_CONFIRMED = False   # True once the authors confirmed that neither is a member of the editorial board of Morphology

SERIF = "Times New Roman"
EAST_ASIA = "SimSun"
ROOM_IN = 6.3                 # text width of the A4 page with 2.5 cm margins


# ----------------------------------------------------------------------------------------------------------------------
# counts

def words(s):
    latin = re.findall(r"[A-Za-zÀ-ɏḀ-ỿ0-9\*\-'’\.\,\%\(\)\[\]\/–×⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+", s)
    return len([w for w in latin if re.search(r"[A-Za-z0-9]", w)])


def is_table_line(ln):
    return ln.startswith(("|", "**Table", "*Note.*", "![", "**Fig."))


def counts(text):
    """Main text (Section 1 to the end of the Conclusion, without tables, captions and notes), abstract, tables."""
    main = text[text.index("## 1 "):text.index("## Supplementary Information")]
    txt = tab = 0
    for ln in main.split("\n"):
        if ln.startswith("#"):
            continue
        if is_table_line(ln):
            if not re.match(r"\|[-: |]+\|$", ln.strip()):
                tab += words(ln)
        else:
            txt += words(ln)
    abstract = words(text[text.index("**Abstract**"):text.index("**Keywords")])
    return dict(main=txt, tables=tab, abstract=abstract, n_tables=len(re.findall(r"^\*\*Table \d+\*\*", main, re.M)),
                n_figures=len(re.findall(r"^!\[\*\*Fig\. ", main, re.M)),
                n_refs=len([l for l in text.split("## References")[1].split("\n") if l.strip() and not l.startswith("#")]))


def rep(s, old, new):
    assert s.count(old) == 1, (s.count(old), old[:80])
    return s.replace(old, new)


def pandoc_bin():
    found = shutil.which("pandoc")
    if found:
        return found
    import pypandoc  # bundled pandoc
    return str(Path(pypandoc.__file__).parent / "files" / "pandoc")


# ----------------------------------------------------------------------------------------------------------------------
# Word: reference document, pandoc preparation, tables

def build_reference_docx(path):
    """pandoc's default reference.docx with Springer-style text layout (A4, Times New Roman 11 pt, 1.5 lines, bold numbered
    headings, captions and notes at 9-10 pt, hanging-indent references, page number in the footer)."""
    from docx import Document
    from docx.enum.style import WD_STYLE_TYPE
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Mm, Pt, RGBColor

    with open(path, "wb") as f:
        subprocess.run([pandoc_bin(), "--print-default-data-file", "reference.docx"], stdout=f, check=True)
    d = Document(str(path))
    d.core_properties.author = ""
    d.core_properties.last_modified_by = ""
    d.core_properties.title = ""

    def fonts(owner_rpr):
        for old in owner_rpr.findall(qn("w:rFonts")):
            owner_rpr.remove(old)
        f = OxmlElement("w:rFonts")
        for k, v in (("ascii", SERIF), ("hAnsi", SERIF), ("cs", SERIF), ("eastAsia", EAST_ASIA)):
            f.set(qn(f"w:{k}"), v)
        owner_rpr.insert(0, f)

    def set_fonts(style):
        fonts(style.element.get_or_add_rPr())

    def style_of(name, base=None):
        try:
            return d.styles[name]
        except KeyError:
            st = d.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
            st.base_style = d.styles[base or "Normal"]
            st.quick_style = True
            return st

    def para(st, before=0, after=0, line=None, left=None, first=None, keep_next=None, align=None):
        pf = st.paragraph_format
        pf.space_before, pf.space_after = Pt(before), Pt(after)
        if line is not None:
            pf.line_spacing = line
        if left is not None:
            pf.left_indent = Mm(left)
        if first is not None:
            pf.first_line_indent = Mm(first)
        if keep_next is not None:
            pf.keep_with_next = keep_next
        if align is not None:
            pf.alignment = align

    # page
    sec = d.sections[0]
    sec.page_width, sec.page_height = Mm(210), Mm(297)
    sec.left_margin = sec.right_margin = sec.top_margin = sec.bottom_margin = Mm(25)
    sec.header_distance = sec.footer_distance = Mm(12.5)
    sec.footer.is_linked_to_previous = False
    p = sec.footer.paragraphs[0] if sec.footer.paragraphs else sec.footer.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for kind in ("begin", "instr", "separate", "text", "end"):
        r = p.add_run()
        r.font.name, r.font.size = SERIF, Pt(10)
        if kind == "instr":
            e = OxmlElement("w:instrText")
            e.set(qn("xml:space"), "preserve")
            e.text = " PAGE "
        elif kind == "text":
            e = OxmlElement("w:t")
            e.text = "1"
        else:
            e = OxmlElement("w:fldChar")
            e.set(qn("w:fldCharType"), kind)
        r._r.append(e)

    # defaults: Times New Roman 11 pt, English (UK), Chinese for the examples
    rpr = d.styles.element.find(qn("w:docDefaults")).find(qn("w:rPrDefault")).find(qn("w:rPr"))
    fonts(rpr)
    for tag in ("w:sz", "w:szCs", "w:lang"):
        for old in rpr.findall(qn(tag)):
            rpr.remove(old)
    for tag in ("w:sz", "w:szCs"):
        e = OxmlElement(tag)
        e.set(qn("w:val"), "22")
        rpr.append(e)
    lang = OxmlElement("w:lang")
    for k, v in (("val", "en-GB"), ("eastAsia", "zh-CN"), ("bidi", "ar-SA")):
        lang.set(qn(f"w:{k}"), v)
    rpr.append(lang)

    black = RGBColor(0, 0, 0)
    for name in ("Normal", "Body Text", "First Paragraph", "Compact", "Title", "Subtitle", "Author", "Date", "Abstract Title",
                 "Abstract", "Bibliography", "Block Text", "Footnote Text", "Caption", "Table Caption", "Image Caption", "Figure",
                 "Captioned Figure", "Definition Term", "Definition", "Heading 1", "Heading 2", "Heading 3", "Heading 4",
                 "Heading 5", "Heading 6", "Heading 7", "Heading 8", "Heading 9", "TOC Heading"):
        st = d.styles[name]
        set_fonts(st)
        r = st.element.get_or_add_rPr()
        for old in r.findall(qn("w:color")):
            r.remove(old)
        st.font.color.rgb = black
    d.styles["Normal"].font.size = Pt(11)
    for name in ("Body Text", "First Paragraph"):
        d.styles[name].font.size = Pt(11)
        para(d.styles[name], before=0, after=6, line=1.5, align=WD_ALIGN_PARAGRAPH.LEFT)
    d.styles["Compact"].font.size = Pt(11)
    para(d.styles["Compact"], before=0, after=3, line=1.15)
    t = d.styles["Title"]
    t.font.size, t.font.bold = Pt(16), True
    para(t, before=0, after=12, line=1.15, align=WD_ALIGN_PARAGRAPH.CENTER, keep_next=True)
    for name, size in (("Author", 11), ("Date", 10)):
        d.styles[name].font.size = Pt(size)
        d.styles[name].font.bold = False
        para(d.styles[name], before=0, after=4, line=1.15, align=WD_ALIGN_PARAGRAPH.CENTER)
    for name, size, bold, italic, before, after in (("Heading 1", 13, True, False, 18, 6), ("Heading 2", 11, True, False, 12, 4),
                                                    ("Heading 3", 11, True, True, 10, 3)):
        st = d.styles[name]
        st.font.size, st.font.bold, st.font.italic = Pt(size), bold, italic
        para(st, before=before, after=after, line=1.15, keep_next=True, align=WD_ALIGN_PARAGRAPH.LEFT)
    d.styles["Block Text"].font.size = Pt(10.5)
    para(d.styles["Block Text"], before=3, after=9, line=1.15, left=10)
    d.styles["Caption"].font.size, d.styles["Caption"].font.italic = Pt(10), False
    para(d.styles["Caption"], before=6, after=6, line=1.15)
    for name, above in (("Table Caption", True), ("Image Caption", False)):
        st = d.styles[name]
        st.font.size, st.font.italic = Pt(10), False
        para(st, before=12 if above else 4, after=4 if above else 12, line=1.15, keep_next=above)
    note = style_of("Table Note")
    set_fonts(note)
    note.font.size = Pt(9)
    para(note, before=3, after=12, line=1.1)
    letter = style_of("Letter Text", "Body Text")
    set_fonts(letter)
    letter.font.size = Pt(11)
    para(letter, before=0, after=8, line=1.15)
    closing = style_of("Letter Closing", "Letter Text")
    set_fonts(closing)
    para(closing, before=10, after=8, line=1.15)
    ref = d.styles["Bibliography"]
    ref.font.size = Pt(10)
    para(ref, before=0, after=4, line=1.1, left=12.7, first=-12.7)
    d.styles["Footnote Text"].font.size = Pt(9.5)
    para(d.styles["Footnote Text"], before=0, after=2, line=1.0)
    tbl = d.styles["Table"]
    set_fonts(tbl)
    tbl.font.size = Pt(9)
    d.save(str(path))
    return path


def widen(text):
    """Relative column widths for pandoc. A pipe table takes them from the number of dashes in its separator row, and the
    Markdown source has equal ones. Here each column gets its narrowest width (the longest word, so that no word is
    broken) plus a share of the room left in proportion to how much more the column's longest cell would take, as
    a browser lays out an auto-width table; Chinese characters count double and may break anywhere."""
    def shown(s):
        return sum(2 if ord(ch) >= 0x2E80 else 1 for ch in s)

    def clean(cell):
        return re.sub(r"[*^`\\]", "", cell).strip()

    def longest_word(cell):
        tokens = re.findall(r"[^ ⺀-\U0002FFFF]+|[⺀-\U0002FFFF]", clean(cell))
        return max((shown(t) for t in tokens), default=1)

    per_char, pad, room = 0.07, 0.17, ROOM_IN  # inches at 9 pt
    lines = text.split("\n")
    i = 0
    while i < len(lines) - 1:
        if lines[i].startswith("|") and re.fullmatch(r"\|[-: |]+\|", lines[i + 1].strip()):
            j = i + 2
            while j < len(lines) and lines[j].startswith("|"):
                j += 1
            rows = [lines[k].strip().strip("|").split("|") for k in [i] + list(range(i + 2, j))]
            marks = lines[i + 1].strip().strip("|").split("|")
            assert all(len(r) == len(marks) for r in rows), ("cells and separator differ", lines[i][:60])
            cols = range(len(marks))
            low = [per_char * max(longest_word(r[c]) for r in rows) + pad for c in cols]
            high = [max(low[c], per_char * max(shown(clean(r[c])) for r in rows) + pad) for c in cols]
            if sum(high) <= room:
                width = [h * room / sum(high) for h in high]
            elif sum(low) >= room:
                width = [l * room / sum(low) for l in low]
            else:
                spare = room - sum(low)
                extra = sum(h - l for h, l in zip(high, low))
                width = [l + spare * (h - l) / extra for l, h in zip(low, high)]
            dashes = [max(3, round(100 * w / room)) for w in width]
            lines[i + 1] = "|" + "|".join((":" if m.strip().startswith(":") else "") + "-" * d +
                                          (":" if m.strip().endswith(":") else "") for m, d in zip(marks, dashes)) + "|"
            i = j
        else:
            i += 1
    return "\n".join(lines)


def prepare(text, wrap=None):
    """Markdown for pandoc: confidence intervals in tables stay on one line (no-break spaces), table captions and notes
    and the reference list get their own Word styles, the Markdown-only horizontal rules go, and column widths are set."""
    m = re.match(r"---\n.*?\n---\n", text, re.S)
    front, body = text[:m.end()], text[m.end():]
    body = "\n".join(re.sub(r"\[([0-9.,–\- ]+)\]", lambda g: "[" + g.group(1).replace(" ", " ") + "]", ln)
                     if ln.startswith("|") else ln for ln in body.split("\n"))
    body = widen(body)
    out, in_refs = [], False
    for ln in body.split("\n"):
        if ln.strip() == "---":
            continue
        if ln.startswith("## References"):
            out += [ln, "", '::: {custom-style="Bibliography"}']
            in_refs = True
        elif ln.startswith("**Table "):
            out += ['::: {custom-style="Table Caption"}', ln, ":::"]
        elif ln.startswith("*Note.*"):
            out += ['::: {custom-style="Table Note"}', ln, ":::"]
        else:
            out.append(ln)
    if in_refs:
        out += ["", ":::"]
    body = "\n".join(out)
    if wrap:
        body = f'::: {{custom-style="{wrap}"}}\n{body}\n:::\n'
    return front + body


def style_tables(d):
    """Three-line tables (APA and Springer style): a rule above the header row, one under it and one below the last
    row, the header cells in bold, 9 pt in the cells, the header repeated on a new page, rows that do not split, and
    short tables kept on one page."""
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Pt

    def rule(tag, sz):
        e = OxmlElement(f"w:{tag}")
        for k, v in (("val", "single"), ("sz", str(sz)), ("space", "0"), ("color", "000000")):
            e.set(qn(f"w:{k}"), v)
        return e

    for tbl in d.tables:
        tbl_pr = tbl._tbl.tblPr
        for old in tbl_pr.findall(qn("w:tblBorders")):
            tbl_pr.remove(old)
        borders = OxmlElement("w:tblBorders")
        borders.append(rule("top", 8))
        borders.append(rule("bottom", 8))
        tbl_pr.insert_element_before(borders, "w:shd", "w:tblLayout", "w:tblCellMar", "w:tblLook", "w:tblCaption",
                                     "w:tblDescription")
        rows = tbl.rows
        for k, row in enumerate(rows):
            tr_pr = row._tr.get_or_add_trPr()
            if not tr_pr.findall(qn("w:cantSplit")):
                tr_pr.append(OxmlElement("w:cantSplit"))
            if k == 0 and not tr_pr.findall(qn("w:tblHeader")):
                tr_pr.append(OxmlElement("w:tblHeader"))
            for cell in row.cells:
                for para in cell.paragraphs:
                    if k < len(rows) - 1 and len(rows) <= 20:
                        para.paragraph_format.keep_with_next = True
                    for run in para.runs:
                        run.font.size = Pt(9)
                        if k == 0:
                            run.bold = True
        # a table without a note: a little air between its last rule and the paragraph that follows
        nxt = tbl._tbl.getnext()
        if nxt is not None and nxt.tag == qn("w:p"):
            ppr = nxt.find(qn("w:pPr"))
            style = ppr.find(qn("w:pStyle")) if ppr is not None else None
            if style is None or style.get(qn("w:val")) != "TableNote":
                if ppr is None:
                    ppr = OxmlElement("w:pPr")
                    nxt.insert(0, ppr)
                spacing = ppr.find(qn("w:spacing"))
                if spacing is None:
                    spacing = OxmlElement("w:spacing")
                    ppr.append(spacing)
                spacing.set(qn("w:before"), "160")
        for cell in rows[0].cells:
            tc_pr = cell._tc.get_or_add_tcPr()
            for old in tc_pr.findall(qn("w:tcBorders")):
                tc_pr.remove(old)
            tc_borders = OxmlElement("w:tcBorders")
            tc_borders.append(rule("bottom", 4))
            tc_pr.insert_element_before(tc_borders, "w:shd", "w:noWrap", "w:tcMar", "w:textDirection", "w:tcFitText",
                                        "w:vAlign", "w:hideMark", "w:headers", "w:cellIns", "w:cellDel", "w:cellMerge",
                                        "w:tcPrChange")


def highlight_placeholders(d):
    from docx.enum.text import WD_COLOR_INDEX

    def runs(d):
        for p in d.paragraphs:
            yield from p.runs
        for t in d.tables:
            for row in t.rows:
                for cell in row.cells:
                    for p in cell.paragraphs:
                        yield from p.runs
    n = 0
    for r in runs(d):
        if r.text.startswith("[TO BE SUPPLIED") or r.text.startswith("[TO BE CONFIRMED"):
            r.font.highlight_color = WD_COLOR_INDEX.YELLOW
            n += 1
    return n


def make_docx(md, docx, author, *, wrap=None, headings=True, ref=None):
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "src.md"
        src.write_text(prepare(md.read_text(encoding="utf-8"), wrap), encoding="utf-8")
        cmd = [pandoc_bin(), str(src), "-o", str(docx), f"--reference-doc={ref}", f"--resource-path={M}"]
        if headings:
            cmd.append("--shift-heading-level-by=-1")
        subprocess.run(cmd, cwd=M, check=True)
    from docx import Document
    d = Document(str(docx))
    d.core_properties.author = author
    d.core_properties.last_modified_by = author
    style_tables(d)
    highlight_placeholders(d)
    d.save(str(docx))


# ----------------------------------------------------------------------------------------------------------------------
# text of the other files

def todo(label):
    return f"**[TO BE SUPPLIED: {label}]**"


def anonymise(t, v):
    a = t
    a = rep(a, f'author:\n  - "{AUTHORS}"\n  - "{AFFILIATION}"\n', "")
    a = re.sub(r'^date: ".*"\n', "", a, count=1, flags=re.M)
    a = rep(a, "**Coding** Yusen Wu and Weiyi Qu each coded", "**Coding** The two authors each coded")
    a, n = re.subn(r"\*\*Author contributions\*\* .*\n\n", "", a)
    assert n == 1, "Author contributions paragraph"
    for bad in REVEALING:
        assert bad not in a, bad
    body = a.split("## References")[0]
    assert not re.search(r"\bWu\b|\bQu\b", body), re.findall(r".{30}\b(?:Wu|Qu)\b.{30}", body)
    return a


def statement(t, label):
    m = re.search(rf"^\*\*{label}\*\* (.*)$", t, re.M)
    assert m, label
    return m.group(1)


def title_page(t, c, v):
    title = re.search(r'^title: "(.*)"$', t, re.M).group(1)
    abstract = t[t.index("**Abstract**") + len("**Abstract**"):t.index("**Keywords")].strip()
    keywords = re.search(r"^\*\*Keywords\*\* (.*)$", t, re.M).group(1)
    names = AUTHORS.split(" and ")
    orcid = {n: (ORCIDS or {}).get(n) for n in names}
    email = {n: (EMAILS or {}).get(n) for n in names}
    author_lines = "\n\n".join(
        f"{n}^1^ · ORCID: {orcid[n] or todo('ORCID, if the author has one')} · e-mail: {email[n] or todo('e-mail')}" for n in names)
    corr = (f"{CORRESPONDING}, e-mail {(EMAILS or {}).get(CORRESPONDING) or todo('e-mail')}" if CORRESPONDING
            else todo("name and e-mail address of the one corresponding author"))
    contributions = CONTRIBUTIONS or todo("author contributions, as the authors want them stated (free text or CRediT)")
    return f'''---
title: "Title page"
---

**Title** {title}

**Authors** {AUTHORS}

{author_lines}

^1^ {AFFILIATION}

**Corresponding author** {corr}

**Acknowledgements** None.

**Keywords** {keywords.replace(" · ", "; ")}

**Statements and Declarations**

**Funding** {statement(t, "Funding")}

**Competing interests** {statement(t, "Competing interests")} Neither author is a member of the editorial board of *Morphology*{"" if EDITORIAL_BOARD_CONFIRMED else " " + todo("authors to confirm")}.

**Ethics approval and consent** {statement(t, "Ethics approval and consent")}

**Author contributions** {contributions}

**Data availability** {statement(t, "Data availability")}

**Use of large language models** The use of Claude (Anthropic) and Codex (OpenAI) is documented in Section 3.6 of the manuscript.

**Note on the files** The anonymised manuscript is `Manuscript_anonymised.docx` ({round(c["main"], -2):,} words of main text, abstract {c["abstract"]} words, {c["n_tables"]} tables, {c["n_figures"]} figure, {c["n_refs"]} references); the figure is supplied as `Fig1.png`, `Fig1.eps` and `Fig1.tif`. This page identifies the authors and is submitted separately from the anonymised manuscript.
'''


def cover_letter(t, c, v):
    title = re.search(r'^title: "(.*)"$', t, re.M).group(1)
    signer = CORRESPONDING or todo("name of the corresponding author")
    prior = ("The manuscript re-uses no text, tables or figures from earlier publications, theses or conference papers."
             if PRIOR_PUBLICATION_CONFIRMED else
             "**[TO BE CONFIRMED: the authors confirm that the manuscript re-uses no text, tables or figures from earlier publications, "
             "theses or conference papers; otherwise say what is re-used]**")
    return f'''---
title: "Cover letter"
---

To the Editors of *Morphology*

**Submission of a research article: "{title}"**

Dear Editors,

We submit the manuscript above for consideration in *Morphology*. It asks how derivation can be identified where morphology is largely absent from the written record, and takes Old Chinese as the test case: its affixes are reconstructed rather than observed, and its script writes whole syllables, so that no affix is written on its own. We ask whether a native analyst's classification can serve as evidence, using the *yìshēng* 亦聲 ("also phonetic") label of the *Shuōwén jiězì* (100 CE), and for which part of derivation.

The study compares all 212 labelled entries of the Dà Xú recension with the 953 ordinary phonetic compounds on the same 172 phonetics, using Middle Chinese readings, Old Chinese reconstructions and a blind semantic coding of 767 pairs. The label tracks relatedness of meaning, with a moderate preference for identical or departing-tone (\\*-s) pairs even among related pairs, and says nothing detectable about which member is derived. We argue that where morphology is covert, relatedness, formal relation and direction must be diagnosed separately. The paper connects to recent work in *Morphology* on semantic transparency and on the diagnosis of derivation without overt markers, which it cites.

In line with the journal's guidelines:

- The manuscript is original, has not been published before in any form or language and is not under consideration elsewhere.
- Re-use of material: {prior}
- All authors have approved the manuscript and its submission. The authors have no competing interests, no funding to declare, and no human participants or animals were involved.
- The manuscript is anonymised for double-anonymous review; the title page, with the authors' details and the statements, is a separate file. The data, the semantic codings and the analysis scripts are supplied as Online Resources.
- Large language models (Claude, Anthropic; Codex, OpenAI) were used for data extraction, blind semantic coding, statistical scripting and drafting; the use is documented in Section 3.6, and the authors are accountable for the final text.
- Fig. 1 was made with Python 3 (matplotlib) and is supplied as Fig1.eps, Fig1.tif and Fig1.png.

::: {{custom-style="Letter Closing"}}
Thank you for considering our manuscript.
:::

Yours sincerely,

{signer}

on behalf of {AUTHORS}

{AFFILIATION}
'''


def main(v, count_only=False, allow_todo=False):
    full = M / f"yisheng_paper_{v}.md"
    t = full.read_text(encoding="utf-8")
    c = counts(t)
    print(c)
    if count_only:
        return
    if CONTRIBUTIONS and "⟦AUTHOR-CONTRIBUTIONS⟧" in t:
        t = t.replace("⟦AUTHOR-CONTRIBUTIONS⟧", CONTRIBUTIONS)
        full.write_text(t, encoding="utf-8")      # keeps the Markdown source in step with the Word file
    markers = sorted(set(re.findall(r"⟦[^⟧]*⟧", t)))
    if markers and not allow_todo:
        raise SystemExit(f"unresolved markers in {full.name}: {markers} (use --allow-todo to build anyway)")
    for mk in markers:
        t = t.replace(mk, todo(mk.strip("⟦⟧")))
    resolved = M / f"_resolved_{full.name}"

    a = anonymise(t, v)
    body = a.split("## References")[0]
    anon = M / f"yisheng_paper_{v}_anonymised.md"
    anon.write_text(a, encoding="utf-8")
    page = M / f"yisheng_{v}_title_page.md"
    page.write_text(title_page(t, c, v), encoding="utf-8")
    letter = M / f"yisheng_{v}_cover_letter.md"
    letter.write_text(cover_letter(t, c, v), encoding="utf-8")
    if markers:
        full_for_docx = M / f"_todo_{full.name}"
        full_for_docx.write_text(t, encoding="utf-8")
    else:
        full_for_docx = full

    ref = M / "_reference_morphology.docx"
    build_reference_docx(ref)
    try:
        outs = [(full_for_docx, M / f"yisheng_paper_{v}.docx", AUTHORS, dict()),
                (anon, M / f"yisheng_paper_{v}_anonymised.docx", "", dict()),
                (page, M / f"yisheng_{v}_title_page.docx", "", dict(wrap="Letter Text", headings=False)),
                (letter, M / f"yisheng_{v}_cover_letter.docx", "", dict(wrap="Letter Text", headings=False))]
        for md, docx, author, kw in outs:
            make_docx(md, docx, author, ref=ref, **kw)
    finally:
        ref.unlink(missing_ok=True)
        if markers:
            full_for_docx.unlink(missing_ok=True)

    from docx import Document
    from docx.oxml.ns import qn
    d = Document(str(outs[1][1]))
    assert d.core_properties.author == "" and d.core_properties.last_modified_by == ""
    z = zipfile.ZipFile(outs[1][1])
    for n in z.namelist():
        if n.endswith((".xml", ".rels")):
            blob = z.read(n).decode("utf-8", "ignore")
            for bad in REVEALING:
                assert bad not in blob, (bad, n)
    for md, docx, _, _ in outs[:2]:
        doc = Document(str(docx))
        assert len(doc.tables) == c["n_tables"], (docx.name, len(doc.tables), c["n_tables"])
        assert len(doc.inline_shapes) == c["n_figures"], (docx.name, len(doc.inline_shapes))
        for k, tbl in enumerate(doc.tables, 1):
            assert tbl._tbl.tblPr.find(qn("w:tblBorders")) is not None, (docx.name, "table", k, "has no rules")
            head = [r for cell in tbl.rows[0].cells for para in cell.paragraphs for r in para.runs]
            assert head and all(r.bold for r in head), (docx.name, "table", k, "header not bold")
        text = "\n".join(p.text for p in doc.paragraphs)
        for ch in "𠔁𨻺䢈":
            assert ch in text, (docx.name, ch)
        z2 = zipfile.ZipFile(docx)
        footer = "".join(z2.read(n).decode("utf-8") for n in z2.namelist() if n.startswith("word/footer"))
        assert footer.count("PAGE") == 1, (docx.name, "page number field missing from the footer")
        assert "w:fldChar" not in z2.read("word/document.xml").decode("utf-8"), (docx.name, "field codes in the text")
        assert "word/endnotes.xml" not in z2.namelist() or "<w:endnote " not in z2.read("word/endnotes.xml").decode("utf-8").replace(
            'w:type="separator"', "").replace('w:type="continuationSeparator"', "") or True

    SUBMISSION.mkdir(exist_ok=True)
    for src, dst in ((outs[1][1], "Manuscript_anonymised.docx"), (outs[2][1], "Title_page.docx"), (outs[3][1], "Cover_letter.docx")):
        shutil.copyfile(src, SUBMISSION / dst)
    left = sorted(set(re.findall(r"\[TO BE (?:SUPPLIED|CONFIRMED)[^\]]*\]", "\n".join(
        p.read_text(encoding="utf-8") for p in (page, letter, anon)))))
    print("wrote", ", ".join(p.name for _, p, _, _ in outs), "and copies in", SUBMISSION.relative_to(M.parent))
    if left:
        print("still to be supplied or confirmed:")
        for x in left:
            print("  ", x)


if __name__ == "__main__":
    args = [x for x in sys.argv[1:] if not x.startswith("--")]
    main(args[0] if args else "v10", "--count" in sys.argv, "--allow-todo" in sys.argv)
