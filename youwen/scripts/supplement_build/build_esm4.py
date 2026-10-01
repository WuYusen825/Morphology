"""Build ESM_4.pdf from ESM_4_final.md (internal; not shipped)."""
import sys, re
sys.path.insert(0, '/tmp/claude-0/-home-user-Morphology/7d9f6fd5-d830-551f-9a43-e3ebcc390a52/scratchpad/esm/work')
import markdown
from esm_common import *
from pdf_common import *

md = (ESM / 'work/ESM_4_final.md').read_text(encoding='utf-8')
# python-markdown needs four spaces for nested lists; the source uses two
md = '\n'.join((' ' * (2 * (len(l) - len(l.lstrip(' ')))) + l.lstrip(' ')) if l.startswith('  ') else l for l in md.split('\n'))
# the identification block (first lines up to the first '---') goes into a framed box
head, rest = md.split('\n---\n', 1)
body = markdown.markdown(rest, extensions=['tables', 'sane_lists'])
hb = markdown.markdown(head, extensions=['sane_lists'])
hb = hb.replace('<h1>', '<h1 style="margin-bottom:4pt">', 1)
m = re.match(r'(<h1[^>]*>.*?</h1>)(.*)', hb, re.S)
body_html = m.group(1) + '<div class="idblock">' + m.group(2) + '</div>' + body
out = STAGE / 'ESM_4.pdf'
n = render_pdf(body_html, out, 'Online Resource 4: analysis plan for the enlarged coding', 'Online Resource 4', ESM / 'work/pdfbuild')
print('pages', n, out.stat().st_size)
print('missing glyphs:', missing_glyphs(body_html, out))
