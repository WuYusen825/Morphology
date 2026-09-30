#!/usr/bin/env python3
"""Builds the submission files of a paper version from its full Markdown text.

From youwen/manuscript/yisheng_paper_<v>.md it makes
  yisheng_paper_<v>_anonymised.md  the manuscript for double-blind review: no authors, affiliation, funding or
                                   competing-interest statements, no repository owner in links
  yisheng_<v>_title_page.md        authors, affiliation, corresponding author (placeholders), declarations
and the three Word files (pandoc, styles from yisheng_paper_v6.docx). The build stops with an AssertionError if
a string that identifies the authors is left in the anonymised files, if the Word file of the anonymised
manuscript carries an author in its properties, or if the tables or the figure did not reach the Word files.

Run from anywhere:  python3 youwen/scripts/yisheng_make_submission_files.py v9
Word counts only:   python3 youwen/scripts/yisheng_make_submission_files.py v9 --count

The anonymisation rules below are written for the v9 wording; when the declarations or the data statement
change, the asserts say which rule no longer matches.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

M = Path(__file__).resolve().parents[1] / "manuscript"
AUTHORS = "Yusen Wu and Weiyi Qu"
AFFILIATION = "School of English and International Studies, Beijing Foreign Studies University"
REVEALING = ["Yusen", "Weiyi", "WuYusen", "Beijing Foreign", "BFSU", "github.com/WuYusen825"]


def words(s):
    latin = re.findall(r"[A-Za-zÀ-ɏḀ-ỿ0-9\*\-'’\.\,\%\(\)\[\]\/–×⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+", s)
    return len([w for w in latin if re.search(r"[A-Za-z0-9]", w)])


def is_table_line(ln):
    return ln.startswith(("|", "**Table", "*Note.*", "![", "**Figure"))


def counts(text):
    """Main text (Section 1 to the end of the Conclusion, without tables, captions and notes), abstract, tables."""
    main = text[text.index("## 1 "):text.index("**Data availability")]
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
                n_figures=len(re.findall(r"^!\[\*\*Figure", main, re.M)),
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


def make_docx(md, docx, author):
    subprocess.run([pandoc_bin(), md.name, "-o", docx.name, "--reference-doc=yisheng_paper_v6.docx",
                    "--resource-path=."], cwd=M, check=True)
    from docx import Document
    d = Document(str(docx))
    d.core_properties.author = author
    d.core_properties.last_modified_by = author
    d.save(str(docx))


def main(v, count_only=False):
    full = M / f"yisheng_paper_{v}.md"
    t = full.read_text(encoding="utf-8")
    c = counts(t)
    print(c)
    if count_only:
        return
    rounded = round(c["main"], -2)

    # anonymised manuscript
    a = t
    a = rep(a, f'author:\n  - "{AUTHORS}"\n  - "{AFFILIATION}"\n', "")
    a = re.sub(r'^date: ".*"$', f'date: "Anonymised manuscript for double-blind review ({v})"', a, count=1, flags=re.M)
    a = rep(a, "The dataset, codes and analysis scripts are available at [WuYusen825/Morphology](https://github.com/WuYusen825/Morphology), in `youwen/`.",
            "The dataset, codes and analysis scripts are in the project repository, in the folder `youwen/`; an anonymised copy is provided to the reviewers through the submission system.")
    a = rep(a, "**Declarations** *Funding.* The authors received no funding for this work. *Competing interests.* The authors have no competing interests to declare. *Ethics.* Not applicable; the study analyses historical texts. *Coding.* Yusen Wu and Weiyi Qu each coded",
            "**Declarations** *Ethics.* Not applicable; the study analyses historical texts. *Coding.* The two authors each coded")
    for bad in REVEALING:
        assert bad not in a, bad
    body = a.split("## References")[0]
    assert not re.search(r"\bWu\b|\bQu\b", body), re.findall(r".{30}\b(?:Wu|Qu)\b.{30}", body)
    anon = M / f"yisheng_paper_{v}_anonymised.md"
    anon.write_text(a, encoding="utf-8")

    # title page
    title = re.search(r'^title: "(.*)"$', t, re.M).group(1)
    tp = f'''---
title: "Title page: {title}"
---

**Title** {title}

**Authors** {AUTHORS}

**Affiliation** {AFFILIATION} (both authors)

**Corresponding author** [name, e-mail address and ORCID to be supplied by the authors]

**Author contributions** [to be supplied by the authors if the journal requires a statement]

**Funding** The authors received no funding for this work.

**Competing interests** The authors have no competing interests to declare.

**Acknowledgements** None.

**Data availability** The dataset, codes and analysis scripts are available at [WuYusen825/Morphology](https://github.com/WuYusen825/Morphology), in `youwen/`. An archived snapshot with a DOI will be deposited before publication; for review, an anonymised copy is provided. (This page identifies the authors and is submitted separately from the anonymised manuscript.)

**Manuscript** The anonymised manuscript is `yisheng_paper_{v}_anonymised.docx`, about {rounded:,} words of main text (abstract {c["abstract"]} words) with {c["n_tables"]} tables, {c["n_figures"]} figure and {c["n_refs"]} references.
'''
    page = M / f"yisheng_{v}_title_page.md"
    page.write_text(tp, encoding="utf-8")

    # Word files
    outs = [(full, M / f"yisheng_paper_{v}.docx", AUTHORS), (anon, M / f"yisheng_paper_{v}_anonymised.docx", ""),
            (page, M / f"yisheng_{v}_title_page.docx", "")]
    for md, docx, author in outs:
        make_docx(md, docx, author)
    from docx import Document
    d = Document(str(outs[1][1]))
    assert d.core_properties.author == "" and d.core_properties.last_modified_by == ""
    import zipfile
    z = zipfile.ZipFile(outs[1][1])
    for n in z.namelist():
        if n.endswith((".xml", ".rels")):
            blob = z.read(n).decode("utf-8", "ignore")
            for bad in REVEALING:
                assert bad not in blob, (bad, n)
    for md, docx, _ in outs[:2]:
        doc = Document(str(docx))
        assert len(doc.tables) == c["n_tables"], (docx.name, len(doc.tables), c["n_tables"])
        assert len(doc.inline_shapes) == c["n_figures"], (docx.name, len(doc.inline_shapes))
        text = "\n".join(p.text for p in doc.paragraphs)
        for ch in "𠔁𨻺䢈":
            assert ch in text, (docx.name, ch)
    print("wrote", ", ".join(p.name for _, p, _ in outs))


if __name__ == "__main__":
    args = [x for x in sys.argv[1:] if not x.startswith("--")]
    main(args[0] if args else "v9", "--count" in sys.argv)
