"""HTML -> PDF helpers (internal; not shipped)."""
import subprocess, re, html
from pathlib import Path
import pymupdf

CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'

CSS = """
@page { size: A4; margin: 19mm 17mm 20mm 17mm;
        @bottom-center { content: "%(footer)s · page " counter(page) " of " counter(pages); font: 8pt "Liberation Sans", Arial, sans-serif; color: #555; } }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: "Liberation Serif", "Times New Roman", "WenQuanYi Zen Hei", serif; font-size: 10pt; line-height: 1.34; color: #111; }
h1 { font: bold 17pt "Liberation Sans", Arial, "WenQuanYi Zen Hei", sans-serif; margin: 0 0 6pt 0; }
h2 { font: bold 13pt "Liberation Sans", Arial, "WenQuanYi Zen Hei", sans-serif; margin: 15pt 0 4pt 0; border-bottom: 0.6pt solid #999; padding-bottom: 1.5pt; break-after: avoid; }
h3 { font: bold 11pt "Liberation Sans", Arial, "WenQuanYi Zen Hei", sans-serif; margin: 11pt 0 3pt 0; break-after: avoid; }
h4 { font: bold 10pt "Liberation Sans", Arial, "WenQuanYi Zen Hei", sans-serif; margin: 8pt 0 2pt 0; break-after: avoid; }
p { margin: 0 0 5pt 0; text-align: left; }
ul, ol { margin: 0 0 5pt 0; padding-left: 15pt; } li { margin: 0 0 2pt 0; }
code { font-family: "Liberation Mono", "DejaVu Sans Mono", "WenQuanYi Zen Hei", monospace; font-size: 8.6pt; background: #f1f1f1; padding: 0 1.5pt; }
pre { font-family: "Liberation Mono", "DejaVu Sans Mono", "WenQuanYi Zen Hei", monospace; font-size: 8pt; line-height: 1.25; background: #f4f4f4; border: 0.5pt solid #ccc; padding: 4pt 5pt; white-space: pre-wrap; word-break: break-word; margin: 0 0 6pt 0; }
pre code { background: none; padding: 0; font-size: inherit; }
table { border-collapse: collapse; width: 100%%; margin: 3pt 0 8pt 0; font-size: 8.6pt; line-height: 1.25; }
th, td { border: 0.5pt solid #8a8a8a; padding: 2pt 3.5pt; vertical-align: top; text-align: left; }
th { background: #e6edf7; font-family: "Liberation Sans", Arial, "WenQuanYi Zen Hei", sans-serif; font-weight: bold; }
tr { break-inside: avoid; }
thead { display: table-header-group; }
td code, th code { font-size: 8pt; }
td.num, th.num { text-align: right; }
.idblock { border: 0.6pt solid #999; background: #f5f7fa; padding: 5pt 8pt; margin: 0 0 8pt 0; font-size: 9.5pt; }
.idblock p { margin: 0 0 2pt 0; }
.note { font-size: 9pt; color: #333; }
.zh { font-family: "WenQuanYi Zen Hei", "Liberation Serif", serif; }
hr { border: 0; border-top: 0.6pt solid #999; margin: 8pt 0; }
blockquote { margin: 0 0 6pt 10pt; padding-left: 8pt; border-left: 2pt solid #bbb; font-size: 9.3pt; }
"""


def render_pdf(body_html, out_pdf, title, footer, workdir):
    workdir = Path(workdir); workdir.mkdir(exist_ok=True)
    doc = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{html.escape(title)}</title><style>{CSS % {"footer": footer}}</style></head><body>{body_html}</body></html>'
    hp = workdir / (Path(out_pdf).stem + '.html')
    hp.write_text(doc, encoding='utf-8')
    tmp = workdir / (Path(out_pdf).stem + '_raw.pdf')
    r = subprocess.run([CHROME, '--headless=new', '--no-sandbox', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={tmp}', f'file://{hp}'],
                       capture_output=True, text=True, timeout=300)
    assert tmp.exists(), r.stderr[-1500:]
    d = pymupdf.open(tmp)
    d.set_metadata({'title': title, 'author': '', 'subject': '', 'keywords': '', 'creator': '', 'producer': ''})
    try: d.del_xml_metadata()
    except Exception: pass
    d.save(out_pdf, garbage=3, deflate=True)
    n = len(d); d.close()
    return n


def pdf_text(pdf):
    d = pymupdf.open(pdf)
    t = '\n'.join(p.get_text() for p in d)
    d.close()
    return t


def missing_glyphs(html_text, pdf):
    """Characters that appear in the HTML text but not in the PDF text (a font without the glyph draws nothing)."""
    body = re.sub(r'<[^>]+>', '', html_text)
    body = html.unescape(body)
    pt = pdf_text(pdf)
    return sorted({c for c in body if ord(c) > 0x7F and not c.isspace() and c not in pt})
