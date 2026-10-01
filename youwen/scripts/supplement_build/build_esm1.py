"""Build ESM_1.pdf from ESM_1_template.md (internal; not shipped)."""
import sys, re, html
sys.path.insert(0, '/tmp/claude-0/-home-user-Morphology/7d9f6fd5-d830-551f-9a43-e3ebcc390a52/scratchpad/esm/work')
import markdown
import pandas as pd
from esm_common import *
from pdf_common import *

tpl = (ESM / 'work/ESM_1_template.md').read_text(encoding='utf-8')
assert not re.search(r'[\U00010000-\U0010FFFF]', tpl), 'non-BMP character in the template (the PDF font has no glyph): use the code point'

DICTS = {}


def dict_table(esm_file, sheet):
    d = pd.read_excel(STAGE / f'{esm_file}.xlsx', sheet_name='data_dictionary', dtype=str, keep_default_na=False)
    d = d[d.sheet == sheet]
    assert len(d) > 0, (esm_file, sheet)
    # the columns that the sheet really has
    cols = list(pd.read_excel(STAGE / f'{esm_file}.xlsx', sheet_name=sheet, nrows=0).columns)
    assert list(d.column) == cols, (sheet, set(d.column) ^ set(cols))
    rows = []
    for _, r in d.iterrows():
        col, desc = r['column'], r['description']
        if col.endswith('_codepoint'):
            desc = f'Unicode code points (U+XXXX) of the character in column <code>{html.escape(col[:-10])}</code>'
        else:
            desc = html.escape(desc)
        rows.append(f'<tr><td class="c"><code>{html.escape(col)}</code></td><td>{desc}</td></tr>')
    DICTS[(esm_file, sheet)] = len(d)
    return ('<table class="dict"><thead><tr><th>Column</th><th>Description</th></tr></thead><tbody>' + ''.join(rows) + '</tbody></table>')


prompt = (ESM / 'work/prompt_template.txt').read_text(encoding='utf-8')
# the items block is shown as a placeholder line, the rest verbatim
prompt = prompt.replace('{items}', '[one line per item: item number, phonetic, its gloss, member, its gloss; tab-separated]')

id_block = ('<div class="idblock">'
            '<p><b>Article title</b> What does \'also phonetic\' mark? The <i>Shuōwén</i>\'s <i>yìshēng</i> label, homophony and derivation in Old Chinese</p>'
            f'<p><b>Journal</b> {JOURNAL}</p>'
            f'<p><b>Authors</b> {WITHHELD}</p>'
            f'<p><b>Corresponding author (affiliation, e-mail)</b> {WITHHELD}</p>'
            f'<p><b>Caption</b> {html.escape(CAPTIONS[1][1])}</p>'
            '</div>')

body = markdown.markdown(tpl, extensions=['tables', 'sane_lists', 'fenced_code'])
n_ph = 0
for m in re.findall(r'<p>\{\{DICT:(ESM_\d):(\w+)\}\}</p>', body):
    n_ph += 1
    body = body.replace(f'<p>{{{{DICT:{m[0]}:{m[1]}}}}}</p>', dict_table(*m))
assert n_ph == 7, n_ph
assert body.count('<table>\n<thead>\n<tr>\n<th>Article</th>') == 1
body = body.replace('<table>\n<thead>\n<tr>\n<th>Article</th>', '<table class="wide1">\n<thead>\n<tr>\n<th>Article</th>')
assert '<p>{{IDBLOCK}}</p>' in body
body = body.replace('<p>{{IDBLOCK}}</p>', id_block)
assert '{{PROMPT}}' in body
body = body.replace('{{PROMPT}}', html.escape(prompt.rstrip('\n')))
assert '{{' not in body, re.findall(r'\{\{[^}]*\}\}', body)

extra_css = '<style>p.cap { break-after: avoid; margin-bottom: 2pt; } table.dict td.c { white-space: nowrap; width: 21%; } table.dict td { font-size: 8.4pt; } pre { font-size: 7.6pt; } table.wide1 th:first-child, table.wide1 td:first-child { width: 22%; } table.keep { break-inside: avoid; } table.t5 th:nth-child(1), table.t5 td:nth-child(1) { width: 19%; } table.t5 th:nth-child(2), table.t5 td:nth-child(2) { width: 43%; } table.t5 th:nth-child(3), table.t5 td:nth-child(3) { width: 21%; } table.t5 th:nth-child(4), table.t5 td:nth-child(4) { width: 17%; }</style>'
body = body.replace('<p><strong>Guide table', '<p class="cap"><strong>Guide table')
# a short table that must not be split across two pages (its caption stays with it)
for no in ('6',):
    i = body.index(f'<p class="cap"><strong>Guide table {no}</strong>')
    j = body.index('<table>', i)
    body = body[:j] + '<table class="keep">' + body[j + len('<table>'):]
i = body.index('<p class="cap"><strong>Guide table 5</strong>')
j = body.index('<table>', i)
body = body[:j] + '<table class="t5">' + body[j + len('<table>'):]
html_body = extra_css + body
out = STAGE / 'ESM_1.pdf'
n = render_pdf(html_body, out, 'Online Resource 1: guide to the electronic supplementary material', 'Online Resource 1', ESM / 'work/pdfbuild')
print('pages', n, out.stat().st_size, 'dictionary rows', DICTS)
print('missing glyphs:', missing_glyphs(html_body, out))
(ESM / 'work/ESM_1_body.html').write_text(html_body, encoding='utf-8')
