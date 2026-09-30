# v7 补充分析（2026-09-29，Claude）：不改任何既有数据或结果文件，只读 yisheng_dataset.csv 等，另写 yisheng_models_v7_checks.csv
# 1. 中古音四分剖面：同音 / 涉及去声的声调清浊交替 / 其他声调清浊交替 / 其他差异（互斥，分母为两端都有中古音的全部字对）
# 2. 声符内（分层）比较：Mantel-Haenszel 合并 OR 与 CMH 检验，只用同时有亦声与普通成员的声符；补 GEE 只校正依赖、不消除声符间基线差异的缺口
# 3. H1c 两步分解的精度：是否涉及去声；涉及去声时哪一端为去声（条件最大似然 OR 与精确 95% CI）
# 4. H1b 上古 R 类拆分：涉及 *-s 的 R 与不涉及 *-s 的 R（"其他词缀"）
# 5. 段注"形聲包會意"等按语所及的普通形声字（探索性、描述性）：与其他普通形声字、与亦声字比较中古同音率
# 6. 非去声交替的细分（描述性）：只差清浊 / 只差平上声调 / 两者兼有，分母为两端都有中古音的非同音字对
# 7. 去掉以声符释字的声训（paronomastic_gloss）后重算 H1a、H1c 与去声交替（GEE 与声符内 MH），供“检验 × 假设”汇总表
# 8. 方向的基线（描述性）：两端恰有一端为去声的字对中，形声字一端为去声的比例，按中古关系（只差声调清浊 / 其他差异）分列，亦声与普通合计
# 9. 亦声字对按传本分层的中古音四分剖面（描述性）：两本共有层 对 仅大徐层（yisheng_xiaoxu_collation_final.csv 的 layer）
# 10. “其他差异”字对的描述：声母韵母都不同的比例；上古两端都有构拟时 R 类的比例；盲编样本中这类亦声字对的语义编码
# 11. 未归本部的亦声字按层比较中古同音（H3 与归部构成无关的检查）；声训式释义按层分布（均为描述性）
# 12. 语义相关字对内部：标注是否仍预测同音或去声交替（区分“意义在先”的字形解释与本文解释的关键比较；样本小，只作描述）
#     12b 合并两组看各中古音类别中的相关比例；12c（2026-09-30）在亦声组、普通组内分别比较相关对与不相关对的同音或去声交替比例
# 13. 段注按语的字头数（全部 9,833 个字头，一个字头只计一次；口径同文献线程的 duan_phrase_count.py）
# 14. 组合检验（评审初稿 1 的 D1）：去声训、两本共有、两者同时（核心层）、去王筠九字、去归本部 40 条时的 H1a、去声交替、H1c，GEE 与声符内 MH；
#     除“去声训”和“核心层”两行同时去掉普通字中的声训外，去掉的只是亦声字，普通字全部保留（与 v6 “共有”行只保留仍有共有标注之声符的普通字不同，故共有行 GEE 为 1.83 而非 1.94；声符内 MH 两种口径相同）；
#     另报亦声字按层 × 是否声训的四分剖面，以及核心层与其余亦声字的同音率比较
# 15.（2026-09-30）H4 与段注删标两项比较的双侧 Fisher p：归本部的亦声字 对 其余亦声字；段注删去标注的 对 段注保留的（计数同 yisheng_summary.csv 的 H4、H3 行，该文件只有单侧 p）
# 16.（2026-09-30）盲编样本的抽样框（评审初稿 3 的 T1）：50 个普通对中有 4 个所在声符唯一的亦声字是新附，不在 172 个声符的比较组内；去掉后重算 H2，并在其余 79 对上重算描述性 logit 模型
#     第 10、12 节读盲编工作表 blind_coding_sheet_llm_coded.xlsx（两位作者的编码与盲编子代理逐项相同）与 yisheng_claude_codes.csv，合并方式同 manuscript_checks.py
# 用法（在 youwen/scripts 下）：python3 yisheng_v7_checks.py .. <shuowen/data 目录>
# shuowen/data 来自 https://github.com/shuowenjiezi/shuowen （与 load.py 相同的开放数据）
import sys, os, json, math, csv, warnings
import pandas as pd, numpy as np
import statsmodels.api as sm, statsmodels.formula.api as smf
from statsmodels.stats.contingency_tables import StratifiedTable
from scipy.stats import fisher_exact
from scipy.stats.contingency import odds_ratio
warnings.filterwarnings('ignore')
outdir, swdir = sys.argv[1], sys.argv[2]
d = pd.read_csv(os.path.join(outdir, 'yisheng_dataset.csv'), encoding='utf-8-sig', dtype=str)
A = d[d.in_analysis_set == 'True']
yph = set(A[A.relation == '亦聲'].phonetic)
A = A[A.phonetic.isin(yph)].copy()
A['label'] = (A.relation == '亦聲').astype(int)
MC = A[A.mc_relation.notna()].copy()
DEP = {'member', 'head'}
def cat4(r):
    if r.mc_relation == 'identical': return 'identical'
    if r.mc_relation == 'tone_voicing_alt': return 'alt_departing' if r.mc_qusheng_direction in DEP else 'alt_other'
    return 'other'
MC['cat4'] = MC.apply(cat4, axis=1)
OC = A[A.morph_relation_auto.notna()].copy()
NI_OC = OC[OC.morph_relation_auto != 'I'].copy()
NI_OC['R_s'] = ((NI_OC.morph_relation_auto == 'R') & NI_OC.morph_affix_detail.fillna('').str.contains('-s')).astype(int)
NI_OC['R_nos'] = ((NI_OC.morph_relation_auto == 'R') & ~NI_OC.morph_affix_detail.fillna('').str.contains('-s')).astype(int)
ALT = MC[MC.mc_relation == 'tone_voicing_alt'].copy()
DEPP = ALT[ALT.mc_qusheng_direction.isin(DEP)].copy()
NI_MC = MC[MC.mc_relation != 'identical'].copy()

out = []
def counts(df, y):
    L = df[df.label == 1]; O = df[df.label == 0]
    return int(L[y].sum()), len(L), int(O[y].sum()), len(O)
def gee(df, y):
    x = pd.DataFrame(dict(y=df[y].astype(int).values, label=df.label.values, phon=df.phonetic.values))
    if x.y.nunique() < 2: return None
    g = smf.gee('y ~ label', groups='phon', data=x, family=sm.families.Binomial(), cov_struct=sm.cov_struct.Exchangeable()).fit()
    b, se = g.params['label'], g.bse['label']
    return math.exp(b), math.exp(b - 1.96 * se), math.exp(b + 1.96 * se), g.pvalues['label']
def mh(df, y):
    tabs = []
    for p, g in df.groupby('phonetic'):
        if g.label.nunique() < 2: continue
        a = int(((g.label == 1) & (g[y] == 1)).sum()); b = int(((g.label == 1) & (g[y] == 0)).sum())
        c = int(((g.label == 0) & (g[y] == 1)).sum()); e = int(((g.label == 0) & (g[y] == 0)).sum())
        tabs.append(np.array([[a, b], [c, e]], dtype=float))
    if not tabs: return None
    st = StratifiedTable(tabs)
    lo, hi = st.oddsratio_pooled_confint()
    t = st.test_null_odds(correction=False)
    L = sum(t_[0].sum() for t_ in tabs); O = sum(t_[1].sum() for t_ in tabs)
    return len(tabs), int(L), int(O), st.oddsratio_pooled, lo, hi, t.pvalue
def add(section, name, df, y, note=''):
    a, n1, c, n0 = counts(df, y)
    r = dict(section=section, comparison=name, labelled_hits=a, labelled_n=n1, ordinary_hits=c, ordinary_n=n0,
             labelled_rate=round(a / n1, 3) if n1 else '', ordinary_rate=round(c / n0, 3) if n0 else '')
    g = gee(df, y)
    if g: r.update(gee_OR=round(g[0], 2), gee_CI95=f'{g[1]:.2f}-{g[2]:.2f}', gee_p_two_sided='%.2g' % g[3])
    m = mh(df, y)
    if m: r.update(mh_strata=m[0], mh_labelled_n=m[1], mh_ordinary_n=m[2], mh_OR=round(m[3], 2), mh_CI95=f'{m[4]:.2f}-{m[5]:.2f}', cmh_p_two_sided='%.2g' % m[6])
    fe = fisher_exact([[a, n1 - a], [c, n0 - c]])
    r['fisher_p_two_sided'] = '%.2g' % fe[1]
    r['note'] = note
    out.append(r)

# 0. 与既有结果对账（应得 63/177 vs 133/858；16/33 vs 43/150）
MC['identical'] = (MC.cat4 == 'identical').astype(int)
ALT['member_dep'] = (ALT.mc_qusheng_direction == 'member').astype(int)
assert counts(MC, 'identical') == (63, 177, 133, 858), counts(MC, 'identical')
assert counts(ALT, 'member_dep') == (16, 33, 43, 150), counts(ALT, 'member_dep')

# 1. 四分剖面
for k in ['identical', 'alt_departing', 'alt_other', 'other']:
    MC[k] = (MC.cat4 == k).astype(int)
    add('MC profile (all MC pairs)', f'MC category: {k}', MC, k, 'mutually exclusive categories; denominators = all pairs with MC readings at both ends')
# 2. 声符内比较：主结果
add('within-series', 'H1a MC identical (within phonetic)', MC, 'identical', 'MH pooled over phonetics with both labelled and ordinary members')
add('within-series', 'H1c member departing | tone/voicing alternation (within phonetic)', ALT, 'member_dep')
ALT['any_dep'] = ALT.mc_qusheng_direction.isin(DEP).astype(int)
add('within-series', 'departing tone involved | tone/voicing alternation', ALT, 'any_dep', 'step 1 of the H1c decomposition')
NI_MC['alt_other'] = (NI_MC.cat4 == 'alt_other').astype(int)
NI_MC['alt_departing'] = (NI_MC.cat4 == 'alt_departing').astype(int)
add('within-series', 'non-departing tone/voicing alternation | non-identical MC pairs', NI_MC, 'alt_other', 'the MC part of H1b once departing-tone alternations are set aside')
add('within-series', 'departing-tone alternation | non-identical MC pairs', NI_MC, 'alt_departing')
# 3. 方向（涉及去声时成员为去声）
DEPP['member_dep'] = (DEPP.mc_qusheng_direction == 'member').astype(int)
add('direction', 'member departing | departing-tone alternation', DEPP, 'member_dep', 'step 2 of the H1c decomposition')
a, n1, c, n0 = counts(DEPP, 'member_dep')
orc = odds_ratio([[a, n1 - a], [c, n0 - c]], kind='conditional')
ci = orc.confidence_interval(0.95)
out.append(dict(section='direction', comparison='member departing | departing-tone alternation: conditional MLE OR (exact CI)',
                labelled_hits=a, labelled_n=n1, ordinary_hits=c, ordinary_n=n0, labelled_rate=round(a / n1, 3), ordinary_rate=round(c / n0, 3),
                gee_OR=round(orc.statistic, 2), gee_CI95=f'{ci.low:.2f}-{ci.high:.2f}', note='columns gee_OR/gee_CI95 here hold the conditional MLE OR and its exact 95% CI'))
# 4. 上古 R 类拆分
NI_OC['R'] = (NI_OC.morph_relation_auto == 'R').astype(int)
add('OC R split', 'OC R (any) | non-identical OC pairs', NI_OC, 'R', 'H1b-OC as in yisheng_models.csv')
add('OC R split', 'OC R involving *-s | non-identical OC pairs', NI_OC, 'R_s', 'R with a suffix change involving -s (affix detail contains -s)')
add('OC R split', 'OC R not involving *-s | non-identical OC pairs', NI_OC, 'R_nos', 'other affixes and alternations only')

# 6. 非去声交替的细分（描述性，只报 Fisher 双侧 p）
def alt_sub(r):
    if r.cat4 != 'alt_other': return ''
    v = r.mc_voicing_differs == 'True'; t = r.mc_tone_member != r.mc_tone_head
    if v and not t: return 'voicing_only'
    if t and not v: return 'level_rising_only'
    return 'voicing_and_level_rising'
NI_MC['alt_sub'] = NI_MC.apply(alt_sub, axis=1)
for k, lab in [('voicing_only', 'voicing only'), ('level_rising_only', 'level/rising tone only'), ('voicing_and_level_rising', 'voicing and level/rising tone')]:
    NI_MC[k] = (NI_MC.alt_sub == k).astype(int)
    a, n1, c, n0 = counts(NI_MC, k)
    out.append(dict(section='MC other alternations split (descriptive)', comparison=f'non-departing alternation, {lab} | non-identical MC pairs',
                    labelled_hits=a, labelled_n=n1, ordinary_hits=c, ordinary_n=n0, labelled_rate=round(a / n1, 3), ordinary_rate=round(c / n0, 3),
                    fisher_p_two_sided='%.2g' % fisher_exact([[a, n1 - a], [c, n0 - c]])[1], note='descriptive; subcategories of alt_other'))

# 7. 去掉声训后的 H1a、H1c（GEE 与声符内 MH）
NOPAR = MC[MC.paronomastic_gloss != 'True'].copy()
add('paronomastic glosses removed', 'H1a MC identical, paronomastic glosses removed', NOPAR, 'identical', 'expected counts as in v6 Table 2: 40/126 vs 131/848')
ALT_NP = ALT[ALT.paronomastic_gloss != 'True'].copy()
add('paronomastic glosses removed', 'H1c member departing | tone/voicing alternation, paronomastic glosses removed', ALT_NP, 'member_dep')
NOPAR['alt_departing'] = (NOPAR.cat4 == 'alt_departing').astype(int)
add('paronomastic glosses removed', 'departing-tone alternation | all MC pairs, paronomastic glosses removed', NOPAR, 'alt_departing')

# 8. 方向的基线（描述性）
ONE = MC[(MC.mc_tone_member == '去') != (MC.mc_tone_head == '去')].copy()
ONE['member_dep'] = (ONE.mc_tone_member == '去').astype(int)
t_alt = ONE[ONE.mc_relation == 'tone_voicing_alt']; t_oth = ONE[ONE.mc_relation == 'other']
a, n1, c, n0 = int(t_alt.member_dep.sum()), len(t_alt), int(t_oth.member_dep.sum()), len(t_oth)
out.append(dict(section='direction baseline (descriptive)', comparison='member is the departing-tone end, pairs with exactly one departing end: tone/voicing-only pairs (labelled columns) vs pairs differing in other ways too (ordinary columns); labelled and ordinary compounds pooled',
                labelled_hits=a, labelled_n=n1, ordinary_hits=c, ordinary_n=n0, labelled_rate=round(a / n1, 3), ordinary_rate=round(c / n0, 3),
                fisher_p_two_sided='%.2g' % fisher_exact([[a, n1 - a], [c, n0 - c]])[1], note='baseline for the configuration effect; columns here are not labelled vs ordinary'))
for lab, nm in [(1, 'labelled'), (0, 'ordinary')]:
    sub = t_oth[t_oth.label == lab]
    out.append(dict(section='direction baseline (descriptive)', comparison=f'member is the departing-tone end, pairs differing in other ways too, {nm} compounds only',
                    labelled_hits=int(sub.member_dep.sum()), labelled_n=len(sub), labelled_rate=round(sub.member_dep.mean(), 3), note='descriptive'))

# 9. 亦声字对按传本分层的中古音四分剖面（描述性）
LAY = {r['sw_id']: r['layer'] for r in csv.DictReader(open(os.path.join(outdir, 'yisheng_xiaoxu_collation_final.csv'), encoding='utf-8-sig'))}
MC['layer'] = MC.sw_id.map(LAY)
LB = MC[(MC.label == 1) & (MC.layer == 'both')]; LD = MC[(MC.label == 1) & (MC.layer == 'daxu_only')]
for k in ['identical', 'alt_departing', 'alt_other', 'other']:
    a, n1, c, n0 = int(LB[k].sum()), len(LB), int(LD[k].sum()), len(LD)
    out.append(dict(section='labelled pairs by recension layer (descriptive)', comparison=f'MC category: {k}; shared layer (labelled columns) vs Da Xu-only layer (ordinary columns)',
                    labelled_hits=a, labelled_n=n1, ordinary_hits=c, ordinary_n=n0, labelled_rate=round(a / n1, 3), ordinary_rate=round(c / n0, 3),
                    fisher_p_two_sided='%.2g' % fisher_exact([[a, n1 - a], [c, n0 - c]])[1], note='labelled pairs only; undecidable layer (%d pairs) left out' % int(((MC.label == 1) & (MC.layer == 'unknown')).sum())))

# 10. “其他差异”字对的描述
INI = sorted(['p', 'ph', 'b', 'm', 't', 'th', 'd', 'n', 'tr', 'trh', 'dr', 'nr', 'ts', 'tsh', 'dz', 's', 'z', 'tsr', 'tsrh', 'dzr', 'sr', 'zr',
              'tsy', 'tsyh', 'dzy', 'ny', 'sy', 'zy', 'k', 'kh', 'g', 'ng', "'", 'x', 'h', 'y', 'l'], key=len, reverse=True)
def mc_split(x):  # 与 yisheng.py 的 split 相同：BS 中古音转写拆成声母、韵（不含调）、调
    tone = {'X': '上', 'H': '去'}.get(x[-1:], '')
    body = x[:-1] if tone else x
    if not tone: tone = '入' if body.endswith(('p', 't', 'k')) else '平'
    ini = next((i for i in INI if body.startswith(i)), '')
    return ini, body[len(ini):], tone
FAR = MC[MC.cat4 == 'other'].copy()
def both_differ(r):
    a, b = mc_split(r.mc_bs2014), mc_split(r.head_mc_bs2014)
    return int(a[0] != b[0] and a[1] != b[1])
FAR['ini_and_fin'] = FAR.apply(both_differ, axis=1)
a, n1, c, n0 = counts(FAR, 'ini_and_fin')
out.append(dict(section='remote pairs (descriptive)', comparison='MC initial and final both differ | pairs in the other-difference category',
                labelled_hits=a, labelled_n=n1, ordinary_hits=c, ordinary_n=n0, labelled_rate=round(a / n1, 3), ordinary_rate=round(c / n0, 3),
                fisher_p_two_sided='%.2g' % fisher_exact([[a, n1 - a], [c, n0 - c]])[1], note='descriptive; the rest differ in initial only or in final only (tone may also differ)'))
FAR_OC = FAR[FAR.morph_relation_auto.notna()].copy()
FAR_OC['oc_R'] = (FAR_OC.morph_relation_auto == 'R').astype(int)
a, n1, c, n0 = counts(FAR_OC, 'oc_R')
out.append(dict(section='remote pairs (descriptive)', comparison='OC relation R (affix or regular alternation only) | other-difference pairs with OC forms at both ends',
                labelled_hits=a, labelled_n=n1, ordinary_hits=c, ordinary_n=n0, labelled_rate=round(a / n1, 3), ordinary_rate=round(c / n0, 3),
                fisher_p_two_sided='%.2g' % fisher_exact([[a, n1 - a], [c, n0 - c]])[1], note='descriptive; OC categories as in youwen_criteria.md'))

# 盲编样本（第 10、12 节共用；合并方式同 manuscript_checks.py）
import openpyxl
ws = openpyxl.load_workbook(os.path.join(outdir, 'blind_coding_sheet_llm_coded.xlsx'))['编码']
S = pd.DataFrame(list(ws.iter_rows(min_row=2, values_only=True)), columns=['item', 'series', 'sgloss', 'char', 'cgloss', 'code', 'conf', 'note'])
CC = pd.read_csv(os.path.join(outdir, 'yisheng_claude_codes.csv'), encoding='utf-8-sig', dtype=str)
S['item'] = S['item'].astype(str); S = S.merge(CC, on='item', suffixes=('', '_c'))
assert (S.char == S.char_c).all()
S = S.merge(d[['phonetic', 'char', 'relation', 'in_analysis_set', 'sw_id']], left_on=['series', 'char'], right_on=['phonetic', 'char'], how='left', suffixes=('', '_d'))
S = S[(S.relation_d == S.relation) | S.relation_d.isna() | ~S.item.duplicated(keep=False)]
S = S[(S.in_analysis_set == 'True') & (S.code != 'X')].copy()
S['label'] = (S.relation_d == '亦聲').astype(int)
assert (int(S.label.sum()), int((S.label == 0).sum())) == (33, 50), (int(S.label.sum()), int((S.label == 0).sum()))
S['related'] = S.code.isin(['Y', 'E']).astype(int)
S = S.merge(MC[['sw_id', 'phonetic', 'cat4']], on=['sw_id', 'phonetic'], how='left')
SL = S[(S.label == 1) & (S.cat4 == 'other')]
out.append(dict(section='remote pairs (descriptive)', comparison='coded semantically related (Y or E) | labelled other-difference pairs in the blind-coded sample',
                labelled_hits=int(SL.related.sum()), labelled_n=len(SL), labelled_rate=round(SL.related.mean(), 3) if len(SL) else '', note='descriptive; chars: ' + ''.join(SL.char)))

# 11. 未归本部的亦声字按层比较中古同音；声训按层分布（描述性）
NF = MC[(MC.label == 1) & (MC.filed_under_phonetic != 'True') & MC.layer.isin(['both', 'daxu_only'])]
a, n1, c, n0 = int(NF[NF.layer == 'daxu_only'].identical.sum()), int((NF.layer == 'daxu_only').sum()), int(NF[NF.layer == 'both'].identical.sum()), int((NF.layer == 'both').sum())
out.append(dict(section='recension layers (descriptive)', comparison='MC identical among labels not filed under their phonetic: Da Xu-only (labelled columns) vs shared (ordinary columns)',
                labelled_hits=a, labelled_n=n1, ordinary_hits=c, ordinary_n=n0, labelled_rate=round(a / n1, 3), ordinary_rate=round(c / n0, 3),
                fisher_p_two_sided='%.2g' % fisher_exact([[a, n1 - a], [c, n0 - c]])[1], note='H3 without the filed-under labels (37 of the 40 are in the shared layer)'))
YE = A[A.label == 1].copy(); YE['layer'] = YE.sw_id.map(LAY); YE['par'] = (YE.paronomastic_gloss == 'True').astype(int)
a, n1, c, n0 = int(YE[YE.layer == 'daxu_only'].par.sum()), int((YE.layer == 'daxu_only').sum()), int(YE[YE.layer == 'both'].par.sum()), int((YE.layer == 'both').sum())
out.append(dict(section='recension layers (descriptive)', comparison='paronomastic gloss (gloss uses the phonetic) among labelled entries: Da Xu-only (labelled columns) vs shared (ordinary columns)',
                labelled_hits=a, labelled_n=n1, ordinary_hits=c, ordinary_n=n0, labelled_rate=round(a / n1, 3), ordinary_rate=round(c / n0, 3),
                fisher_p_two_sided='%.2g' % fisher_exact([[a, n1 - a], [c, n0 - c]])[1], note='entries, not pairs; all 202 labelled entries of the two layers'))

# 12. 语义相关字对内部：标注与读音
R_ = S[(S.related == 1) & S.cat4.notna()].copy()
R_['near'] = R_.cat4.isin(['identical', 'alt_departing']).astype(int)
R_['ident'] = (R_.cat4 == 'identical').astype(int)
for y, lab in [('near', 'MC identical or departing-tone alternation'), ('ident', 'MC identical')]:
    a, n1, c, n0 = counts(R_, y)
    out.append(dict(section='related pairs only (descriptive)', comparison=f'{lab} | blind-coded pairs coded related (Y or E) with MC readings',
                    labelled_hits=a, labelled_n=n1, ordinary_hits=c, ordinary_n=n0, labelled_rate=round(a / n1, 3), ordinary_rate=round(c / n0, 3),
                    fisher_p_two_sided='%.2g' % fisher_exact([[a, n1 - a], [c, n0 - c]])[1], note='the comparison that would separate a meaning-first account from one in which the label also tracks sound; too few related ordinary pairs to decide'))

# 12b. 盲编样本合并两组：各中古音类别中被编为语义相关的比例（描述性；"意义在先"解释所需的前提）
S_ = S[S.cat4.notna()]
for k in ['identical', 'alt_departing', 'alt_other', 'other']:
    g = S_[S_.cat4 == k]
    out.append(dict(section='related pairs only (descriptive)', comparison=f'coded related (Y or E) | MC category {k}, labelled and ordinary pooled',
                    labelled_hits=int(g.related.sum()), labelled_n=len(g), labelled_rate=round(g.related.mean(), 3) if len(g) else '', note='descriptive; blind-coded sample'))

# 12c. 分组看相关与读音（回应评审初稿 2 的 R2）：在亦声组内、普通组内分别比较相关对与不相关对的“同音或去声交替”比例
for grp, glab in [(1, 'labelled pairs'), (0, 'ordinary pairs')]:
    g = S_[S_.label == grp].copy(); g['near'] = g.cat4.isin(['identical', 'alt_departing']).astype(int)
    r1, r0 = g[g.related == 1], g[g.related == 0]
    a, n1, c, n0 = int(r1.near.sum()), len(r1), int(r0.near.sum()), len(r0)
    out.append(dict(section='related pairs only (descriptive)', comparison=f'MC identical or departing-tone alternation within {glab}: coded related (labelled columns) vs coded unrelated (ordinary columns)',
                    labelled_hits=a, labelled_n=n1, ordinary_hits=c, ordinary_n=n0, labelled_rate=round(a / n1, 3), ordinary_rate=round(c / n0, 3),
                    fisher_p_two_sided='%.2g' % fisher_exact([[a, n1 - a], [c, n0 - c]])[1], note='columns reused: here "labelled" = related pairs and "ordinary" = unrelated pairs of the one group named'))

# 13. 段注按语的字头数
import glob
DP = ['形聲包會意', '形聲中有會意', '形聲兼會意', '會意兼形聲', '會意包形聲']
dn, anyn, nfiles = {p_: 0 for p_ in DP}, 0, 0
for f in sorted(glob.glob(os.path.join(swdir, '*.json'))):
    j = json.load(open(f, encoding='utf-8')); nfiles += 1
    t_ = json.dumps(j.get('duan_notes'), ensure_ascii=False)
    hit = False
    for p_ in DP:
        if p_ in t_: dn[p_] += 1; hit = True
    anyn += hit
for p_ in DP:
    out.append(dict(section='Duan notes: head entries (descriptive)', comparison=f'head entries whose Duan notes contain {p_}', labelled_hits=dn[p_], labelled_n=nfiles, note='each head entry counted once'))
out.append(dict(section='Duan notes: head entries (descriptive)', comparison='head entries whose Duan notes contain any of the five phrases', labelled_hits=anyn, labelled_n=nfiles, note='each head entry counted once'))

# 14. 组合检验
ALT['layer'] = ALT.sw_id.map(LAY)
WANG9 = set('貧愾恇娶婚姻婢緉坪')
FILTERS = [('paronomastic glosses removed', lambda x: x[x.paronomastic_gloss != 'True']),
           ('shared labels only', lambda x: x[(x.label == 0) | (x.layer == 'both')]),
           ('core: shared labels without paronomastic glosses', lambda x: x[(x.paronomastic_gloss != 'True') & ((x.label == 0) | (x.layer == 'both'))]),
           ("Wang Yun's nine rejected labels removed", lambda x: x[(x.label == 0) | ~x.char.isin(WANG9)]),
           ('labels filed under own phonetic removed', lambda x: x[(x.label == 0) | (x.filed_under_phonetic != 'True')])]
for fname, f in FILTERS:
    add('combined checks', f'H1a MC identical | {fname}', f(MC), 'identical', 'labelled entries dropped, all ordinary compounds kept')
    add('combined checks', f'departing-tone alternation | all MC pairs | {fname}', f(MC), 'alt_departing', 'labelled entries dropped, all ordinary compounds kept')
    add('combined checks', f'H1c member departing | tone/voicing alternation | {fname}', f(ALT), 'member_dep', 'labelled entries dropped, all ordinary compounds kept')
LL = MC[MC.label == 1].copy()
LL['par'] = np.where(LL.paronomastic_gloss == 'True', 'paronomastic', 'plain')
for (lay_, par_), g in LL.groupby(['layer', 'par']):
    for k in ['identical', 'alt_departing', 'alt_other', 'other']:
        out.append(dict(section='labelled pairs by layer and gloss type (descriptive)', comparison=f'MC category {k} | {lay_} layer, {par_} gloss',
                        labelled_hits=int(g[k].sum()), labelled_n=len(g), labelled_rate=round(g[k].mean(), 3), note='descriptive'))
core = (LL.layer == 'both') & (LL.paronomastic_gloss != 'True')
a, n1, c, n0 = int(LL[core].identical.sum()), int(core.sum()), int(LL[~core].identical.sum()), int((~core).sum())
out.append(dict(section='labelled pairs by layer and gloss type (descriptive)', comparison='MC identical: core labels (labelled columns) vs all other labels (ordinary columns)',
                labelled_hits=a, labelled_n=n1, ordinary_hits=c, ordinary_n=n0, labelled_rate=round(a / n1, 3), ordinary_rate=round(c / n0, 3),
                fisher_p_two_sided='%.2g' % fisher_exact([[a, n1 - a], [c, n0 - c]])[1], note='core = shared by both recensions and without a paronomastic gloss'))

# 5. 段注按语（探索性）
PATS = ['形聲包會意', '形聲中有會意', '會意包形聲', '會意兼形聲', '亦聲']
def duan_flag(sw):
    try: j = json.load(open(os.path.join(swdir, f'{sw}.json'), encoding='utf-8'))
    except FileNotFoundError: return False
    t = ' '.join(n.get('note', '') for n in j.get('duan_notes', []))
    return any(p in t for p in PATS)
OM = MC[MC.label == 0].copy(); OM['duan_flag'] = OM.sw_id.map(duan_flag)
fl = OM[OM.duan_flag]; nf = OM[~OM.duan_flag]; lab = MC[MC.label == 1]
fi, nfi, li = int(fl.identical.sum()), int(nf.identical.sum()), int(lab.identical.sum())
p1 = fisher_exact([[fi, len(fl) - fi], [nfi, len(nf) - nfi]])[1]
p2 = fisher_exact([[li, len(lab) - li], [fi, len(fl) - fi]])[1]
out.append(dict(section='Duan notes (exploratory)', comparison='MC identical: ordinary compounds with a Duan meaningful-phonetic note (labelled columns) vs other ordinary compounds (ordinary columns)',
                labelled_hits=fi, labelled_n=len(fl), ordinary_hits=nfi, ordinary_n=len(nf), labelled_rate=round(fi / len(fl), 3), ordinary_rate=round(nfi / len(nf), 3),
                fisher_p_two_sided='%.2g' % p1, note='notes matched: ' + '/'.join(PATS) + '; flagged chars: ' + ''.join(fl.char)))
out.append(dict(section='Duan notes (exploratory)', comparison='MC identical: labelled (labelled columns) vs Duan-noted ordinary compounds (ordinary columns)',
                labelled_hits=li, labelled_n=len(lab), ordinary_hits=fi, ordinary_n=len(fl), labelled_rate=round(li / len(lab), 3), ordinary_rate=round(fi / len(fl), 3),
                fisher_p_two_sided='%.2g' % p2, note='descriptive; 21 or so items only'))
fa = int(fl.alt_departing.sum()); nfa = int(nf.alt_departing.sum())
out.append(dict(section='Duan notes (exploratory)', comparison='MC departing-tone alternation: Duan-noted ordinary (labelled columns) vs other ordinary (ordinary columns)',
                labelled_hits=fa, labelled_n=len(fl), ordinary_hits=nfa, ordinary_n=len(nf), labelled_rate=round(fa / len(fl), 3), ordinary_rate=round(nfa / len(nf), 3),
                fisher_p_two_sided='%.2g' % fisher_exact([[fa, len(fl) - fa], [nfa, len(nf) - nfa]])[1], note='descriptive'))

# 15. H4 与段注删标：双侧 Fisher p（计数同 yisheng_summary.csv 的 H4、H3 行；该文件只报单侧 p）
LB = MC[MC.label == 1]
for g1, g0, lab_, note_ in [(LB[LB.filed_under_phonetic == 'True'], LB[LB.filed_under_phonetic != 'True'],
                             'labels filed under their own phonetic (labelled columns) vs other labels (ordinary columns)', 'H4; yisheng_summary.csv gives one-sided p = 0.15 for the same counts'),
                            (LB[LB.duan_label == '無'], LB[LB.duan_label == '亦聲'],
                             'labels Duan drops (labelled columns) vs labels Duan keeps (ordinary columns)', 'H3, Duan layer; entries without Duan text in the data left out')]:
    a, n1, c, n0 = int(g1.identical.sum()), len(g1), int(g0.identical.sum()), len(g0)
    out.append(dict(section='exploratory comparisons (two-sided)', comparison=f'MC identical: {lab_}',
                    labelled_hits=a, labelled_n=n1, ordinary_hits=c, ordinary_n=n0, labelled_rate=round(a / n1, 3), ordinary_rate=round(c / n0, 3),
                    fisher_p_two_sided='%.2g' % fisher_exact([[a, n1 - a], [c, n0 - c]])[1], note=note_))

# 16. 盲编样本的抽样框：比较组只含仍有亦声字的 172 个声符（yph）；4 个普通对的声符只有新附亦声字
g83 = gee(S, 'related')
assert round(g83[0], 1) == 22.0, g83          # 与 yisheng_models.csv 的 H2 相同
FR, OUT = S[S.phonetic.isin(yph)].copy(), S[~S.phonetic.isin(yph)]
a, n1, c, n0 = counts(FR, 'related'); g = gee(FR, 'related')
out.append(dict(section='blind sample frame', comparison='H2 related (Y or E) | ordinary pairs outside the 172-phonetic comparison frame removed',
                labelled_hits=a, labelled_n=n1, ordinary_hits=c, ordinary_n=n0, labelled_rate=round(a / n1, 3), ordinary_rate=round(c / n0, 3),
                gee_OR=round(g[0], 2), gee_CI95=f'{g[1]:.2f}-{g[2]:.2f}', gee_p_two_sided='%.2g' % g[3],
                fisher_p_two_sided='%.2g' % fisher_exact([[a, n1 - a], [c, n0 - c]])[1],
                note='removed: %d ordinary pairs (%s), all coded unrelated; all 83 pairs give GEE OR %.1f' % (len(OUT), '、'.join(OUT.phonetic + ':' + OUT.char), g83[0])))
FM = FR[FR.cat4.notna()].copy()
FM['ident'] = (FM.cat4 == 'identical').astype(int); FM['near'] = FM.cat4.isin(['identical', 'alt_departing']).astype(int)
for y, ylab in [('ident', 'MC identical'), ('near', 'MC identical or departing-tone alternation')]:
    lg = smf.logit(f'{y} ~ label + related', data=FM).fit(disp=0)
    for term, tlab in [('related', 'coded related'), ('label', 'label')]:
        b, (lo, hi) = lg.params[term], lg.conf_int().loc[term]
        out.append(dict(section='blind sample frame', comparison=f'descriptive logit on the {len(FM)} in-frame pairs: {ylab} ~ label + related | coefficient of {tlab}',
                        gee_OR=round(math.exp(b), 2), gee_CI95=f'{math.exp(lo):.2f}-{math.exp(hi):.2f}', gee_p_two_sided='%.2g' % lg.pvalues[term],
                        note='ordinary logistic regression, not GEE (columns gee_* hold its OR, Wald CI and p); same model as manuscript_checks.py on its 83 pairs'))

cols = ['section', 'comparison', 'labelled_hits', 'labelled_n', 'labelled_rate', 'ordinary_hits', 'ordinary_n', 'ordinary_rate', 'gee_OR', 'gee_CI95', 'gee_p_two_sided',
        'mh_strata', 'mh_labelled_n', 'mh_ordinary_n', 'mh_OR', 'mh_CI95', 'cmh_p_two_sided', 'fisher_p_two_sided', 'note']
with open(os.path.join(outdir, 'yisheng_models_v7_checks.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for r in out: w.writerow({k: r.get(k, '') for k in cols})
for r in out:
    print(r['section'], '|', r['comparison'], '|', f"{r.get('labelled_hits', '')}/{r.get('labelled_n', '')} vs {r.get('ordinary_hits', '')}/{r.get('ordinary_n', '')}",
          '| GEE', r.get('gee_OR', ''), r.get('gee_CI95', ''), r.get('gee_p_two_sided', ''), '| MH', r.get('mh_strata', ''), r.get('mh_OR', ''), r.get('mh_CI95', ''), r.get('cmh_p_two_sided', ''),
          '| Fisher', r.get('fisher_p_two_sided', ''))
