# 评审线程对初稿 1 的复核计算（2026-09-30）。只读，不改任何数据或结果文件。
# 用法：python3 draft1_review_checks.py <youwen 目录>（需 pandas、statsmodels、scipy）
# 内容：1. 组合检验（去声训、共有 140 条、两者同时）下的 H1a／H1c／去声交替，GEE 与声符内 MH
#       2. 按版本层 × 是否声训的中古四分剖面；核心层（共有且非声训）与其余亦声字的同音率比较
#       3. 方向基线：两端恰有一端为去声的字对里，形声字为去声一端的比例（按关系、按组）
#       4. 正文例字的版本层、声训、归部与王筠九字的中古关系
import sys, math, warnings
import pandas as pd, numpy as np
import statsmodels.api as sm, statsmodels.formula.api as smf
from statsmodels.stats.contingency_tables import StratifiedTable
from scipy.stats import fisher_exact
warnings.filterwarnings('ignore')
Y = sys.argv[1].rstrip('/') + '/'
d = pd.read_csv(Y + 'yisheng_dataset.csv', encoding='utf-8-sig', dtype=str)
A = d[d.in_analysis_set == 'True']
A = A[A.phonetic.isin(set(A[A.relation == '亦聲'].phonetic))].copy()
A['label'] = (A.relation == '亦聲').astype(int)
col = pd.read_csv(Y + 'yisheng_xiaoxu_collation_final.csv', encoding='utf-8-sig', dtype=str)
A['layer'] = A.sw_id.map(dict(zip(col.sw_id, col.layer)))
MC = A[A.mc_relation.notna()].copy()
DEP = {'member', 'head'}
MC['cat4'] = MC.apply(lambda r: 'identical' if r.mc_relation == 'identical' else ('alt_departing' if r.mc_qusheng_direction in DEP else 'alt_other') if r.mc_relation == 'tone_voicing_alt' else 'other', axis=1)
MC['identical'] = (MC.cat4 == 'identical').astype(int)
MC['alt_departing'] = (MC.cat4 == 'alt_departing').astype(int)
ALT = MC[MC.mc_relation == 'tone_voicing_alt'].copy()
ALT['member_dep'] = (ALT.mc_qusheng_direction == 'member').astype(int)

def cnt(df, y):
    L, O = df[df.label == 1], df[df.label == 0]
    return f'{int(L[y].sum())}/{len(L)} vs {int(O[y].sum())}/{len(O)}'
def gee(df, y):
    x = pd.DataFrame(dict(y=df[y].astype(int).values, label=df.label.values, phon=df.phonetic.values))
    g = smf.gee('y ~ label', groups='phon', data=x, family=sm.families.Binomial(), cov_struct=sm.cov_struct.Exchangeable()).fit()
    b, se = g.params['label'], g.bse['label']
    return f'GEE {math.exp(b):.2f} [{math.exp(b-1.96*se):.2f}, {math.exp(b+1.96*se):.2f}] p={g.pvalues["label"]:.2g}'
def mh(df, y):
    tabs = []
    for _, g in df.groupby('phonetic'):
        if g.label.nunique() < 2: continue
        a = int(((g.label == 1) & (g[y] == 1)).sum()); b = int(((g.label == 1) & (g[y] == 0)).sum())
        c = int(((g.label == 0) & (g[y] == 1)).sum()); e = int(((g.label == 0) & (g[y] == 0)).sum())
        tabs.append(np.array([[a, b], [c, e]], float))
    st = StratifiedTable(tabs); lo, hi = st.oddsratio_pooled_confint()
    return f'MH {st.oddsratio_pooled:.2f} [{lo:.2f}, {hi:.2f}] p={st.test_null_odds().pvalue:.2g} ({len(tabs)} phonetics)'
nopar = lambda df: df[df.paronomastic_gloss != 'True']
shared = lambda df: df[(df.label == 0) | (df.layer == 'both')]

print('== 1. 组合检验（普通字保留全部；GEE 与 v6 的“共有”口径略有不同，MH 相同）')
for nm, f in [('all', lambda x: x), ('no paronomastic', nopar), ('shared 140', shared), ('shared & no paronomastic (core)', lambda x: shared(nopar(x)))]:
    s, a = f(MC), f(ALT)
    print(f'{nm:32s} H1a identical      {cnt(s, "identical"):22s} {gee(s, "identical")}  {mh(s, "identical")}')
    print(f'{nm:32s} departing alt (all) {cnt(s, "alt_departing"):22s} {gee(s, "alt_departing")}  {mh(s, "alt_departing")}')
    print(f'{nm:32s} H1c member dep     {cnt(a, "member_dep"):22s} {gee(a, "member_dep")}  {mh(a, "member_dep")}')

print('\n== 2. 亦声字按版本层 × 声训的中古四分剖面（%）')
L = MC[MC.label == 1].copy()
L['grp'] = L.layer.fillna('?') + '/' + np.where(L.paronomastic_gloss == 'True', 'paronomastic', 'plain')
for g, s in list(L.groupby('grp')) + [('ORDINARY', MC[MC.label == 0])]:
    print(f'{g:24s} n={len(s):4d} ' + '  '.join(f'{k} {100*(s.cat4 == k).mean():.1f}' for k in ['identical', 'alt_departing', 'alt_other', 'other']))
core = (L.layer == 'both') & (L.paronomastic_gloss != 'True')
a1, n1, a2, n2 = int(L[core].identical.sum()), int(core.sum()), int(L[~core].identical.sum()), int((~core).sum())
print(f'core vs other labelled, identical: {a1}/{n1} vs {a2}/{n2}, Fisher p={fisher_exact([[a1, n1-a1], [a2, n2-a2]])[1]:.2g}')

print('\n== 3. 方向基线：两端恰有一端为去声')
ONE = MC[(MC.mc_tone_member == '去') != (MC.mc_tone_head == '去')].copy()
ONE['md'] = (ONE.mc_tone_member == '去').astype(int)
for rel in ['tone_voicing_alt', 'other']:
    for lab in [1, 0]:
        t = ONE[(ONE.mc_relation == rel) & (ONE.label == lab)]
        print(f'{rel:18s} label={lab}: compound is the departing end {int(t.md.sum())}/{len(t)}')

print('\n== 4. 例字')
for ch in '禮殯貧娶傾琀憙珥授妊腥仲字雊從政婚姻愾恇緉坪婢胖':
    for _, x in A[(A.char == ch) & (A.label == 1)].iterrows():
        print(ch, x.phonetic, x.mc_bs2014, x.head_mc_bs2014, x.mc_relation, x.mc_qusheng_direction, 'paronomastic=' + str(x.paronomastic_gloss), 'layer=' + str(x.layer), 'filed=' + str(x.filed_under_phonetic), 'type=' + str(x.identical_relation_type))
