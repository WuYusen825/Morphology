# Exploratory checks behind the numbers quoted in outline.md (topic thread, 2026-09-24).
# NOT the confirmatory analysis: the pilot thread owns the dataset and the final statistics.
# Usage: python3 exploratory_checks.py <yisheng_dataset.csv> <shuowen repo data dir>
# Exclusions: string false hits where 亦 is itself the phonetic (帟 奕 弈 迹);
# Xu Xuan's 新附 (approximated as the trailing run of entries without Duan notes in each radical,
# except 否, which Duan keeps in 不部); 省聲 rows. All are provisional until checked on the 1963 facsimile.
import csv, json, glob, sys, re, collections
from math import comb

def fisher_greater(a, b, c, d):
    # one-sided Fisher exact test: is a/(a+b) greater than c/(c+d)?
    n1, n2, k = a + b, c + d, a + c
    tot = comb(n1 + n2, k)
    return sum(comb(n1, x) * comb(n2, k - x) for x in range(a, min(n1, k) + 1)) / tot

ds, swdir = sys.argv[1], sys.argv[2]
D = {}
for f in glob.glob(swdir + '/*.json'):
    d = json.load(open(f)); D[d['id']] = d
has = lambda i: any((n.get('explanation') or '').strip() or (n.get('note') or '').strip() for n in D[i]['duan_notes'])
byrad = collections.defaultdict(list)
for i in sorted(D): byrad[D[i]['radical']].append(i)
xinfu = set()
for ids in byrad.values():
    for i in reversed(ids):
        if has(i): break
        xinfu.add(i)
xinfu -= {i for i in D if D[i]['wordhead'] == '否'}
FALSE_HITS = set('帟奕弈迹')

R = list(csv.DictReader(open(ds, encoding='utf-8-sig')))
R = [r for r in R if r['relation'] in ('亦聲', '聲') and int(r['sw_id']) not in xinfu
     and not (r['relation'] == '亦聲' and r['char'] in FALSE_HITS)]
yi = [r for r in R if r['relation'] == '亦聲']
print('analysis set: 亦聲', len(yi), 'phonetics', len(set(r['phonetic'] for r in yi)),
      '| 聲', sum(r['relation'] == '聲' for r in R))

def table(rows, pred, label):
    g = {k: [r for r in rows if r['relation'] == k] for k in ('亦聲', '聲')}
    a = sum(map(pred, g['亦聲'])); c = sum(map(pred, g['聲']))
    n1, n2 = len(g['亦聲']), len(g['聲'])
    p = fisher_greater(a, n1 - a, c, n2 - c)
    print(f'  {label:<28} 亦聲 {a}/{n1} ({a/n1:.1%})  聲 {c}/{n2} ({c/n2:.1%})  one-sided p={p:.2g}')

def matched(rows):
    kinds = collections.defaultdict(set)
    for r in rows: kinds[r['phonetic']].add(r['relation'])
    keep = {k for k, v in kinds.items() if v == {'亦聲', '聲'}}
    return [r for r in rows if r['phonetic'] in keep], len(keep)

# Old Chinese level (BS 2014 via cddb; categories from morph.py)
oc = [r for r in R if r['morph_relation_auto'] not in ('', 'NA')]
for name, rows in (('OC, all phonetics', oc), ('OC, matched phonetics', None)):
    if rows is None: rows, k = matched(oc); name += f' (n={k})'
    print(name)
    table(rows, lambda r: r['morph_relation_auto'] == 'I', 'I identical')
    table(rows, lambda r: r['morph_relation_auto'] == 'R', 'R affix/alternation only')
    table(rows, lambda r: r['morph_relation_auto'] in ('I', 'R'), 'I+R')

# Middle Chinese level (Guangyun positions in BS 2014 MC notation)
VOICE = {'b': 'p', 'd': 't', 'dr': 'tr', 'dz': 'ts', 'dzr': 'tsr', 'dzy': 'tsy', 'g': 'k', 'z': 's', 'zr': 'sr', 'zy': 'sy', 'h': 'x'}
INI = sorted(['p', 'ph', 'b', 'm', 't', 'th', 'd', 'n', 'tr', 'trh', 'dr', 'nr', 'ts', 'tsh', 'dz', 's', 'z', 'tsr', 'tsrh', 'dzr',
              'sr', 'zr', 'tsy', 'tsyh', 'dzy', 'ny', 'sy', 'zy', 'k', 'kh', 'g', 'ng', "'", 'x', 'h', 'y', 'l'], key=len, reverse=True)
def split(s):
    s = s.strip()
    tone = s[-1] if s[-1:] in ('X', 'H') else ''
    body = s[:-1] if tone else s
    if body.endswith(('p', 't', 'k')): tone = 'R'
    ini = next((i for i in INI if body.startswith(i)), '')
    return ini, body[len(ini):], tone
def mc_rel(r):
    a, b = r['mc_bs2014'], r['head_mc_bs2014']
    if not a or not b or '|' in a or '|' in b: return None
    A, B = split(a), split(b)
    if A == B: return 'same'
    if A[1] == B[1] and VOICE.get(A[0], A[0]) == VOICE.get(B[0], B[0]):
        return 'qu' if A[2] == 'H' and B[2] != 'H' else 'alt'
    return 'other'
mc = [r for r in R if mc_rel(r)]
for name, rows in (('MC, all phonetics', mc), ('MC, matched phonetics', None)):
    if rows is None: rows, k = matched(mc); name += f' (n={k})'
    print(name)
    table(rows, lambda r: mc_rel(r) == 'same', 'identical syllable')
    table(rows, lambda r: mc_rel(r) in ('alt', 'qu'), 'tone/voicing alternation')
    table(rows, lambda r: mc_rel(r) == 'qu', 'directional qusheng')

# Gloss confound: the definition part of the gloss (before 从) contains the phonetic character
defn = lambda g: g.split('从')[0]
print('Gloss contains phonetic')
table(R, lambda r: r['phonetic'] in defn(r['shuowen_gloss']), 'definition contains phonetic')

# Duan Yucai layer: does Duan's emended Shuowen text (duan_notes[].explanation) carry 亦聲 for the same entries?
def duan_text(i): return ''.join((n.get('explanation') or '') for n in D[i]['duan_notes'])
xu_ids = {int(r['sw_id']) for r in yi}
pat = re.compile(r'亦聲')
duan_ids = set()
for i in D:
    if i in xinfu: continue
    t = duan_text(i)
    for m in pat.finditer(t):
        if t[max(0, m.start() - 1)] in '从从' and D[i]['wordhead'] in FALSE_HITS: continue
        duan_ids.add(i)
duan_ids -= {i for i in D if D[i]['wordhead'] in FALSE_HITS}
print('Duan layer: Duan 亦聲 entries', len(duan_ids), '| both', len(xu_ids & duan_ids),
      '| Xu only (Duan drops)', len(xu_ids - duan_ids), '| Duan only (Duan adds)', len(duan_ids - xu_ids))
print('  Xu-only:', ''.join(sorted(D[i]['wordhead'] for i in xu_ids - duan_ids)))
print('  Duan-only:', ''.join(sorted(D[i]['wordhead'] for i in duan_ids - xu_ids)))

# H3 feasibility: MC relation by label stability across Da Xu and Duan (exploratory; small n)
allrows = {int(r['sw_id']): r for r in R}
layers = {'Xu and Duan (stable)': xu_ids & duan_ids, 'Xu only (Duan drops)': xu_ids - duan_ids,
          'Duan only (Duan adds)': duan_ids - xu_ids, 'neither (plain 聲)': {int(r['sw_id']) for r in R if r['relation'] == '聲'} - duan_ids}
print('MC relation by Da Xu / Duan label layer')
for name, ids in layers.items():
    rs = [allrows[i] for i in ids if i in allrows and mc_rel(allrows[i])]
    c = collections.Counter(mc_rel(r) for r in rs); n = len(rs)
    print(f'  {name:<24} n={n:<4} identical {c["same"]} ({c["same"]/max(n,1):.0%})  alternation {c["alt"]+c["qu"]}  of which qusheng-derivative {c["qu"]}')

# H1c direction test, conditional on the pair differing only in tone and/or initial voicing
print('Direction among tone/voicing alternations')
for lab in ('亦聲', '聲'):
    rs = [r for r in mc if r['relation'] == lab and mc_rel(r) in ('alt', 'qu')]
    rev = [r for r in rs if split(r['head_mc_bs2014'])[2] == 'H' and split(r['mc_bs2014'])[2] != 'H']
    print(f'  {lab}: n={len(rs)}  member departing-tone {sum(mc_rel(r)=="qu" for r in rs)}  head departing-tone {len(rev)}')
a = sum(1 for r in mc if r['relation'] == '亦聲' and mc_rel(r) == 'qu'); n1 = sum(1 for r in mc if r['relation'] == '亦聲' and mc_rel(r) in ('alt', 'qu'))
c = sum(1 for r in mc if r['relation'] == '聲' and mc_rel(r) == 'qu'); n2 = sum(1 for r in mc if r['relation'] == '聲' and mc_rel(r) in ('alt', 'qu'))
print(f'  member-is-departing among alternations: 亦聲 {a}/{n1} vs 聲 {c}/{n2}, one-sided p={fisher_greater(a, n1-a, c, n2-c):.2g}')
print('  亦聲 departing-tone derivatives:', ' '.join(f"{r['char']}/{r['phonetic']}" for r in mc if r['relation'] == '亦聲' and mc_rel(r) == 'qu'))

# H1b conditional on non-identity (identity set aside)
print('Conditional on non-identical pairs')
ni_oc = [r for r in oc if r['morph_relation_auto'] != 'I']
table(ni_oc, lambda r: r['morph_relation_auto'] == 'R', 'OC R among non-identical')
m, k = matched(ni_oc); table(m, lambda r: r['morph_relation_auto'] == 'R', f'OC R non-ident, matched ({k})')
ni_mc = [r for r in mc if mc_rel(r) != 'same']
table(ni_mc, lambda r: mc_rel(r) in ('alt', 'qu'), 'MC alternation among non-ident')
m, k = matched(ni_mc); table(m, lambda r: mc_rel(r) in ('alt', 'qu'), f'MC alt non-ident, matched ({k})')
table(ni_mc, lambda r: mc_rel(r) == 'alt', 'MC alt without member-qu')

# H4: Wang Yun's third kind (分別文之在本部者), read as labels on characters filed in the section headed by their own phonetic
own = [r for r in R if r['relation'] == '亦聲' and D[int(r['sw_id'])]['radical'] == r['phonetic']]
print('Wang kind 3: labelled entries filed under their own phonetic', len(own), 'of', len(yi),
      '| 聲 entries filed under their own phonetic', sum(1 for r in R if r['relation'] == '聲' and D[int(r['sw_id'])]['radical'] == r['phonetic']))
for name, grp in (('filed under own phonetic', own), ('other labels', [r for r in yi if r not in own])):
    rs = [r for r in grp if mc_rel(r)]; c = collections.Counter(mc_rel(r) for r in rs)
    print(f'  {name:<26} MC n={len(rs)} identical {c["same"]} ({c["same"]/len(rs):.0%})  alternation {c["alt"]+c["qu"]}  other {c["other"]}')
