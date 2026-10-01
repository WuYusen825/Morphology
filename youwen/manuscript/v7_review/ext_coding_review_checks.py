# Reviewer's independent recomputation of the extended blind coding (read-only).
# Builds the frame from yisheng_dataset.csv, parses the raw agent answers itself,
# takes the original 90 codes from blind_coding_sheet_llm_coded.xlsx, and refits the tests.
import os, re, csv, math, glob, warnings
import pandas as pd, numpy as np, openpyxl
import statsmodels.api as sm, statsmodels.formula.api as smf
from statsmodels.stats.contingency_tables import StratifiedTable
from scipy.stats import fisher_exact, norm
warnings.filterwarnings('ignore')
import sys
# usage: python3 ext_coding_review_checks.py <youwen dir with yisheng_dataset.csv> <youwen/ext_coding from PR #4 checkout>
Y = sys.argv[1] if len(sys.argv) > 1 else '/mnt/project-files/youwen'
E = sys.argv[2] if len(sys.argv) > 2 else 'youwen/ext_coding'

# ---- frame (as in yisheng_v7_checks.py) ----
d = pd.read_csv(f'{Y}/yisheng_dataset.csv', encoding='utf-8-sig', dtype=str)
A = d[d.in_analysis_set == 'True']
yph = set(A[A.relation == '亦聲'].phonetic)
A = A[A.phonetic.isin(yph)].copy()
A['label'] = (A.relation == '亦聲').astype(int)
DEP = {'member', 'head'}
def cat4(r):
    if pd.isna(r.mc_relation): return np.nan
    if r.mc_relation == 'identical': return 'identical'
    if r.mc_relation == 'tone_voicing_alt': return 'alt_departing' if r.mc_qusheng_direction in DEP else 'alt_other'
    return 'other'
A['cat4'] = A.apply(cat4, axis=1)
LAY = {r['sw_id']: r['layer'] for r in csv.DictReader(open(f'{Y}/yisheng_xiaoxu_collation_final.csv', encoding='utf-8-sig'))}
A['layer'] = A.sw_id.map(LAY)
print('frame', A.label.sum(), (A.label == 0).sum(), A.phonetic.nunique())
assert A.duplicated(['sw_id', 'phonetic']).sum() == 0

# ---- original 100 blind codes ----
ws = openpyxl.load_workbook(f'{Y}/blind_coding_sheet_llm_coded.xlsx')['编码']
O = pd.DataFrame(list(ws.iter_rows(min_row=2, values_only=True)), columns=['item', 'series', 'sgloss', 'char', 'cgloss', 'code', 'conf', 'note'])
O = O[O.item.notna()]
O = O.merge(A[['sw_id', 'phonetic', 'char', 'shuowen_gloss']], left_on=['series', 'char'], right_on=['phonetic', 'char'], how='inner')
O = O[[str(g).startswith(str(c)[:3]) or str(c) == 'None' for g, c in zip(O.shuowen_gloss, O.cgloss)]]
print('original items in frame', len(O), 'dup keys', O.duplicated(['phonetic', 'char']).sum())

# ---- raw answers, parsed independently ----
K = pd.read_csv(f'{E}/ext_items_key.csv', encoding='utf-8-sig', dtype=str)
def parse(path):
    out = {}
    for line in open(path, encoding='utf-8'):
        m = re.match(r'^\s*(\d+)\s*\t\s*([YENX])\s*\t\s*([123])\b', line)
        if m: out.setdefault(int(m.group(1)), m.group(2))
    return out
codes = {1: {}, 2: {}}
for p in (1, 2):
    for b in range(1, 8):
        got = parse(f'{E}/raw/pass{p}_b{b:02d}.txt')
        kb = K[K[f'p{p}_batch'].astype(int) == b]
        assert len(got) == len(kb), (p, b, len(got), len(kb))
        for _, r in kb.iterrows():
            codes[p][(r.phonetic, r.char)] = got[int(r[f'p{p}_item'])]
N = K[K.role == 'new'].copy()
N['code1'] = [codes[1][(a, b)] for a, b in zip(N.phonetic, N.char)]
N['code2'] = [codes[2][(a, b)] for a, b in zip(N.phonetic, N.char)]

# anchors: compare with original codes
AN = K[K.role == 'anchor'].copy()
AN['p1'] = [codes[1][(a, b)] for a, b in zip(AN.phonetic, AN.char)]
AN['p2'] = [codes[2][(a, b)] for a, b in zip(AN.phonetic, AN.char)]
AN = AN.merge(O[['sw_id', 'code']], on='sw_id')
print('anchors', len(AN), 'p1==orig', (AN.p1 == AN.code).sum(), 'p2==orig', (AN.p2 == AN.code).sum(), 'key orig_code==sheet', (AN.orig_code == AN.code).sum())

# ---- merge with frame ----
C = pd.concat([O[['sw_id', 'code']].rename(columns={'code': 'code1'}).assign(code2=lambda x: x.code1, origin='orig'),
               N[['sw_id', 'code1', 'code2']].assign(origin='new')])
C = C.merge(A, on='sw_id', how='left', validate='one_to_one')
assert C.sw_id.notna().all()
print('coded in frame', len(C), 'labelled', C.label.sum(), 'ordinary', (C.label == 0).sum())
print('ordinary without MC', ((C.label == 0) & C.cat4.isna()).sum(), 'labelled without MC', ((C.label == 1) & C.cat4.isna()).sum())

# compare with the data thread's long file
L = pd.read_csv(f'{E}/ext_codes_long.csv', encoding='utf-8-sig', dtype=str)
M = C.merge(L[['sw_id', 'code1', 'code2', 'cat4', 'label', 'source']], on='sw_id', suffixes=('', '_L'))
print('long-file rows', len(L), 'matched', len(M), 'code1 diff', (M.code1 != M.code1_L).sum(), 'code2 diff (new only)', ((M.code2 != M.code2_L) & (M.origin == 'new')).sum(),
      'cat4 diff', (M.cat4.fillna('na') != M.cat4_L.fillna('na')).sum())

def kappa(a, b):
    a, b = list(a), list(b); cats = sorted(set(a) | set(b)); n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    pe = sum((a.count(c) / n) * (b.count(c) / n) for c in cats)
    return (po - pe) / (1 - pe), po
rel = lambda s: ['R' if c in 'YE' else c if c == 'X' else 'U' for c in s]
print('kappa new p1 vs p2 four-way %.3f (%.3f)' % kappa(N.code1, N.code2), 'related %.3f (%.3f)' % kappa(rel(N.code1), rel(N.code2)))

def gee(df, y, x='label', formula=None):
    f = formula or f'{y} ~ {x}'
    g = smf.gee(f, groups='phonetic', data=df, family=sm.families.Binomial(), cov_struct=sm.cov_struct.Exchangeable()).fit()
    b, se = g.params[x], g.bse[x]
    return 'OR %.2f [%.2f, %.2f] p1=%.2g' % (math.exp(b), math.exp(b - 1.96 * se), math.exp(b + 1.96 * se), norm.sf(b / se))
def mh(df, y, x='label'):
    t = []
    for _, g in df.groupby('phonetic'):
        if g[x].nunique() < 2: continue
        t.append(np.array([[((g[x] == 1) & (g[y] == 1)).sum(), ((g[x] == 1) & (g[y] == 0)).sum()],
                           [((g[x] == 0) & (g[y] == 1)).sum(), ((g[x] == 0) & (g[y] == 0)).sum()]]) + 0.0)
    st = StratifiedTable(t); lo, hi = st.oddsratio_pooled_confint()
    return 'MH %.2f [%.2f, %.2f] strata=%d cmh p=%.2g' % (st.oddsratio_pooled, lo, hi, len(t), st.test_null_odds(correction=False).pvalue)
def cnt(df, y): return '%d/%d vs %d/%d' % (df[df.label == 1][y].sum(), (df.label == 1).sum(), df[df.label == 0][y].sum(), (df.label == 0).sum())

def prep(col):
    T = C[(C[col] != 'X') & C.cat4.notna()].copy()
    T['related'] = T[col].isin(['Y', 'E']).astype(int)
    T['near'] = T.cat4.isin(['identical', 'alt_departing']).astype(int)
    T['ident'] = (T.cat4 == 'identical').astype(int)
    return T
T = prep('code1'); R = T[T.related == 1]
print('\nP1', cnt(R, 'near'), gee(R, 'near'), '|', mh(R, 'near'), 'clusters', R.phonetic.nunique())
print('S1 ident', cnt(R, 'ident'), gee(R, 'ident'), '|', mh(R, 'ident'))
R2 = R[(R.paronomastic_gloss != 'True')]; print('S2 nopar', cnt(R2, 'near'), gee(R2, 'near'))
R3 = R[(R.label == 0) | (R.layer == 'both')]; print('S3 shared', cnt(R3, 'near'), gee(R3, 'near'))
X3 = R3[R3.paronomastic_gloss != 'True']; print('X3 core', cnt(X3, 'near'), gee(X3, 'near'))
T2 = prep('code2'); R5 = T2[T2.related == 1]; print('S5 pass2', cnt(R5, 'near'), gee(R5, 'near'), '|', mh(R5, 'near'))
print('H2 pass1', cnt(T, 'related'), gee(T, 'related'))
print('H2 pass2', cnt(T2, 'related'), gee(T2, 'related'))
print('S9 near~related+label', gee(T, 'near', 'related', 'near ~ related + label'), '| label', gee(T, 'near', 'label', 'near ~ related + label'))
for g, nm in [(1, 'labelled'), (0, 'ordinary')]:
    x = T[T.label == g]; print(' S9', nm, 'related near %d/%d, unrelated near %d/%d' % (x[x.related == 1].near.sum(), (x.related == 1).sum(), x[x.related == 0].near.sum(), (x.related == 0).sum()))
print('related by cat4 (labelled, ordinary):'); print(pd.crosstab(R.cat4, R.label))

# binary related kappa (X counted as unrelated)
rb = lambda s: ['R' if c in 'YE' else 'U' for c in s]
print('\nkappa related binary (X as unrelated) %.3f (%.3f)' % kappa(rb(N.code1), rb(N.code2)))
# robustness: use the unused second answers for pass-1 batches 3 and 6
alt = dict(codes[1])
for b in (3, 6):
    got = parse(f'{E}/raw/pass1_b{b:02d}_second_answer_not_used.txt')
    kb = K[K.p1_batch.astype(int) == b]
    for _, r in kb.iterrows(): alt[(r.phonetic, r.char)] = got[int(r.p1_item)]
N2 = N.copy(); N2['code1'] = [alt[(a, b)] for a, b in zip(N2.phonetic, N2.char)]
C2 = pd.concat([O[['sw_id', 'code']].rename(columns={'code': 'code1'}), N2[['sw_id', 'code1']]]).merge(A, on='sw_id')
T3 = C2[(C2.code1 != 'X') & C2.cat4.notna()].copy(); T3['related'] = T3.code1.isin(['Y', 'E']).astype(int); T3['near'] = T3.cat4.isin(['identical', 'alt_departing']).astype(int)
R6 = T3[T3.related == 1]
print('P1 with second answers for p1 b03/b06:', cnt(R6, 'near'), gee(R6, 'near'))
# P1 on new items only / original 90 only
Rn = R[R.sw_id.isin(N.sw_id)]; print('P1 new items only', cnt(Rn, 'near'), gee(Rn, 'near'))
# sample strata check
k = K[K.role == 'new']; print(k.stratum.value_counts().to_dict())
o = A[(A.label == 0) & A.cat4.notna()]
print('ordinary with MC', len(o), 'with OC forms (morph_relation_auto notna)', o.morph_relation_auto.notna().sum())
