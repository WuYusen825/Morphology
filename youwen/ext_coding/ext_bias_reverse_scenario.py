# 扩大盲编：偏差敏感性的反方向情景（S3，2026-09-30，Claude 数据线程；探索性，事后，不进判读）。
# 来源：独立评审对 v9 的意见（协调者 23:46 转来）。ext_bias_sensitivity.py（摘要 §8）只看一个方向：普通组里真实不相关的字对被错编成“相关”，会把近音差别造大。
#       这里看反方向：亦声组里第一次盲编编为无关的 31 对，如果按标注本身算相关（即编码人漏判了联系），把它们并入相关组，
#       会把亦声组的近音比例拉低（这 31 对里近音的只有一小部分）。评审按表 8 的计数手算近音 OR 约 2.17，要求用脚本算出区间。
# 用法（在仓库根目录）：python3 youwen/ext_coding/ext_bias_reverse_scenario.py
# 读：ext_codes_long.csv、yisheng_models_ext_coding.csv
# 写：ext_bias_reverse_scenario_output.txt、yisheng_bias_reverse_scenario.csv
# 说明：gee()/mh()/verdict()/add() 与 ext_second_answer_sensitivity.py 中的同名函数相同（后者又与 ext_analysis.py 相同）。
#       先用不并入的数据重现 yisheng_models_ext_coding.csv 里的 P1，再做并入。只读已有文件，不改任何既有文件；没有新的编码。
#       没有随机数：结果是确定的。
import os, csv, math, warnings
import numpy as np, pandas as pd
import statsmodels.api as sm, statsmodels.formula.api as smf
from statsmodels.stats.contingency_tables import StratifiedTable
from scipy.stats import fisher_exact, norm
warnings.filterwarnings('ignore')
E = os.path.join('youwen', 'ext_coding')
SESOI = 2.0
lines = []
def out(s=''): lines.append(s)

C = pd.read_csv(os.path.join(E, 'ext_codes_long.csv'), encoding='utf-8-sig', dtype=str)
for c in ['label', 'near', 'ident']: C[c] = C[c].astype(int)
C['cat4'] = C.cat4.replace('nan', np.nan)
assert len(C) == 767 and C.sw_id.is_unique

# ---------- 统计工具（与 ext_second_answer_sensitivity.py 相同） ----------
res = []
def gee(df, formula, term):
    x = df.copy()
    for cs in [sm.cov_struct.Exchangeable(), sm.cov_struct.Independence()]:
        try:
            g = smf.gee(formula, groups='phonetic', data=x, family=sm.families.Binomial(), cov_struct=cs).fit()
            b, se = g.params[term], g.bse[term]
            if np.isfinite(b) and np.isfinite(se) and 0 < se < 10 and abs(b) < 10:
                return dict(OR=math.exp(b), lo=math.exp(b - 1.96 * se), hi=math.exp(b + 1.96 * se),
                            p2=2 * norm.sf(abs(b / se)), p1=norm.sf(b / se))
        except Exception:
            pass
    return None
def mh(df, y):
    tabs = []
    for _, g in df.groupby('phonetic'):
        if g.label.nunique() < 2: continue
        tabs.append(np.array([[((g.label == 1) & (g[y] == 1)).sum(), ((g.label == 1) & (g[y] == 0)).sum()],
                              [((g.label == 0) & (g[y] == 1)).sum(), ((g.label == 0) & (g[y] == 0)).sum()]], dtype=float))
    if not tabs: return None
    st = StratifiedTable(tabs); lo, hi = st.oddsratio_pooled_confint()
    return dict(strata=len(tabs), OR=st.oddsratio_pooled, lo=lo, hi=hi, p=st.test_null_odds(correction=False).pvalue)
def verdict(g):
    if g is None: return 'not estimable (GEE; e.g. complete separation)'
    c = g['p1'] < 0.05; a = g['hi'] < SESOI
    if c and a: return 'mixed: excess significant but upper CI below 2 (small residual sound effect)'
    if c: return 'supports C (same word / minimal derivation)'
    if a: return 'supports A (meaning-first)'
    return 'indeterminate'
def add(tier, name, df, y, x='label', formula=None, note='', decide=False):
    L, O = df[df[x] == 1], df[df[x] == 0]
    r = dict(tier=tier, test=name, n=len(df), n_phonetics=df.phonetic.nunique(),
             group1_hits=int(L[y].sum()), group1_n=len(L), group0_hits=int(O[y].sum()), group0_n=len(O),
             group1_rate=round(L[y].mean(), 3) if len(L) else '', group0_rate=round(O[y].mean(), 3) if len(O) else '')
    g = gee(df, formula or f'{y} ~ {x}', x)
    if g:
        r.update(gee_OR=round(g['OR'], 2), gee_CI95=f"{g['lo']:.2f}-{g['hi']:.2f}", gee_p_one_sided='%.2g' % g['p1'], gee_p_two_sided='%.2g' % g['p2'],
                 gee_p_one_sided_exact='%.4g' % g['p1'], p1_raw=g['p1'])
    if x == 'label' and formula is None:
        m = mh(df, y)
        if m: r.update(mh_strata=m['strata'], mh_OR=round(m['OR'], 2), mh_CI95=f"{m['lo']:.2f}-{m['hi']:.2f}", cmh_p_two_sided='%.2g' % m['p'])
    a, n1, c, n0 = r['group1_hits'], r['group1_n'], r['group0_hits'], r['group0_n']
    if n1 and n0: r['fisher_p_two_sided'] = '%.2g' % fisher_exact([[a, n1 - a], [c, n0 - c]])[1]
    if decide: r['verdict'] = verdict(g)
    r['note'] = note
    res.append(r); return g

# ---------- 数据：与主检验相同的框（框内、有中古音、第一次盲编不是 X） ----------
P = C[C.cat4.notna() & (C.code1 != 'X')].copy()
assert len(P) == 634 and int(P.label.sum()) == 172
P['related'] = P.code1.isin(['Y', 'E']).astype(int)
L0 = P[(P.label == 1) & (P.related == 0)]                 # 亦声、第一次盲编编为无关
assert len(L0) == 31
P['fold_all'] = ((P.related == 1) | (P.label == 1)).astype(int)                          # 31 对全部并入
P['fold_far'] = ((P.related == 1) | ((P.label == 1) & (P.near == 0))).astype(int)        # 只并入其中不近音的（最不利的取法）
assert int(P.fold_all.sum()) == int(P.related.sum()) + 31

VARS = [('control', '对照：主检验（第一次盲编，编为相关的字对）', 'related'),
        ('fold_all', 'S3：亦声对里编为无关的 31 对全部并入相关组', 'fold_all'),
        ('fold_far', 'S3 的最不利取法：只并入 31 对里不近音的那些', 'fold_far')]
for tier, nm, col in VARS:
    add(tier, 'P1r near ~ label | related', P[P[col] == 1], 'near', decide=True)
    add(tier, 'S1r MC identical ~ label | related', P[P[col] == 1], 'ident', decide=True)

# identity check：不并入时应重现 yisheng_models_ext_coding.csv 的 P1
ref = pd.read_csv(os.path.join(E, 'yisheng_models_ext_coding.csv'), encoding='utf-8-sig', dtype=str).fillna('')
for tag, refname in [('P1r', 'P1'), ('S1r', 'S1')]:
    m = ref[ref.test.str.startswith(refname + ' ') & (ref.tier != 'descriptive')]
    assert len(m) == 1, (tag, len(m))
    m = m.iloc[0]
    r = [x for x in res if x['tier'] == 'control' and x['test'].startswith(tag + ' ')][0]
    assert all(str(r.get(c, '')) == m[c] for c in ['group1_hits', 'group1_n', 'group0_hits', 'group0_n', 'gee_OR', 'gee_CI95', 'gee_p_one_sided', 'mh_OR', 'mh_CI95']), tag

# ---------- 输出 ----------
def fmt(r):
    g = f"{r['group1_hits']}/{r['group1_n']} vs {r['group0_hits']}/{r['group0_n']}"
    o = f", OR {float(r['gee_OR']):.2f} [{r['gee_CI95'].replace('-', ', ')}], p1 {r['gee_p_one_sided']}" if 'gee_OR' in r else ', 不可估'
    if 'p1_raw' in r and 0.04 <= r['p1_raw'] <= 0.06: o += f"（单侧 p 精确值 {r['p1_raw']:.4f}，贴着 .05 的界）"
    if r.get('mh_OR', '') != '': o += f"; MH {r['mh_OR']} [{r['mh_CI95'].replace('-', ', ')}]"
    return g + o
def crude(r):
    a, n1, c, n0 = r['group1_hits'], r['group1_n'], r['group0_hits'], r['group0_n']
    return (a * (n0 - c)) / ((n1 - a) * c)
byt = {(r['tier'], r['test'].split(' ')[0]): r for r in res}

out('偏差敏感性的反方向情景（S3；探索性，事后，不进判读）')
out('来源：独立评审对 v9 的意见（经协调者转来）。摘要 §8 的临界点分析只看一个方向：普通组里真实不相关的字对被错编成“相关”，会把近音差别造大。')
out('这里看反方向：亦声组里第一次盲编编为无关的 31 对，如果按标注本身算相关（即编码人漏判了联系），把它们并入相关组，再比近音。')
out('这是一个极端情景，不是估计：它假定这 31 对都真有意义联系，所以是一个压力测试。')
out('')
out('一、31 对是什么')
n_near = int(L0.near.sum())
out(f'  框内 634 对：亦声 172（编为相关 {int(((P.label == 1) & (P.related == 1)).sum())}、编为无关 {len(L0)}），普通 462（编为相关 {int(((P.label == 0) & (P.related == 1)).sum())}、编为无关 {int(((P.label == 0) & (P.related == 0)).sum())}）。')
cats = L0.cat4.value_counts()
out(f'  亦声编为无关的 31 对：近音 {n_near}（{n_near / len(L0):.0%}），不近音 {len(L0) - n_near}（{(len(L0) - n_near) / len(L0):.0%}）。' +
    '中古音类别：' + '，'.join(f'{k} {v}' for k, v in cats.items()) + '。')
lay = L0.layer.value_counts(); srcs = L0.source.value_counts()
out('  这 31 对的来源：' + '，'.join(f'{ {"both": "大小徐共有", "daxu_only": "大徐独有", "unknown": "大小徐对照未定"}.get(k, k)} {v}' for k, v in lay.items()) +
    f'；带声训释义的 {int((L0.paronomastic_gloss == "True").sum())}；新编条目 {int(srcs.get("extended", 0))}、原 100 条 {int(srcs.get("original_100", 0))}。')
Lr = P[(P.label == 1) & (P.related == 1)]
out(f'  对照：亦声里编为相关的 {len(Lr)} 对，近音 {int(Lr.near.sum())}（{Lr.near.mean():.0%}）。所以并入的 31 对近音比例低得多，会把亦声组的近音比例往下拉。')
out('')
out('二、主检验在三种取法下（近音 ~ 亦声，相关字对；GEE 按声符聚类，单侧 p；规则：p < .05 且置信区间上限 ≥ 2 支持 C）')
for tier, nm, col in VARS:
    r = byt[(tier, 'P1r')]
    out(f'  {nm}')
    out(f'      {fmt(r)}；合并（未加权）OR {crude(r):.2f}；规则：{r["verdict"]}')
out('')
out('三、同音（S1 的口径）在三种取法下')
for tier, nm, col in VARS:
    r = byt[(tier, 'S1r')]
    out(f'  {nm}')
    out(f'      {fmt(r)}；合并（未加权）OR {crude(r):.2f}；规则：{r["verdict"]}')
out('')
ra = byt[('fold_all', 'P1r')]; rc = byt[('control', 'P1r')]; rf = byt[('fold_far', 'P1r')]
out('四、与评审手算对照')
out(f'  评审按表 8 的计数手算：81/172 对 23/79，OR 约 2.17。本脚本：{fmt(ra)}；合并（未加权）OR {crude(ra):.2f}。')
out(f'  评审的 2.17 是未加权的合并优势比（脚本算出 {crude(ra):.2f}，一致）；GEE 按声符聚类，点估计是 {float(ra["gee_OR"]):.2f}，比合并值低，区间以 GEE 为准。' if abs(crude(ra) - 2.17) < 0.005 else f'  评审的 2.17 与脚本的合并优势比 {crude(ra):.2f} 对不上，差异如实报告。')
out('')
out('说明：')
out('  1. 探索性的事后分析；主检验仍是 analysis_plan.md §4.2 的第一次盲编结果，规则没有改动；没有新编码，不改官方数字。')
out(f'  2. 并入的 31 对整体近音比例只有 {n_near}/{len(L0)}（{n_near / len(L0):.0%}），低于亦声组原来的 {Lr.near.mean():.0%}，所以全部并入会把亦声组的近音比例拉低；拉得最低的取法是只并入其中不近音的 {len(L0) - n_near} 对（近音的不并入）。合并（未加权）OR：不并入 {crude(rc):.2f}，全部并入 {crude(ra):.2f}，只并入不近音的 {crude(rf):.2f}。GEE 的估计见第二节；只算了这几种取法，没有枚举所有子集。')
out(f'  3. 结果：全部并入后 GEE OR {float(ra["gee_OR"]):.2f} [{ra["gee_CI95"].replace("-", ", ")}]，对照 {float(rc["gee_OR"]):.2f} [{rc["gee_CI95"].replace("-", ", ")}]，最不利的取法 {float(rf["gee_OR"]):.2f} [{rf["gee_CI95"].replace("-", ", ")}]。三者的置信区间下限都在 1 以上，按规则都判为“支持 (C)”（上限 ≥ 2 且单侧 p < .05）；但点估计降到了 2 上下，即最小关心效应的位置。')
out('  4. 两个方向合起来看：普通组假阳的方向（ext_bias_sensitivity_output.txt）在假阳率够大时能把 OR 降到 1；这个反方向即使取最极端的办法，OR 也降不到 1，只是降到 2 上下。')
out('  5. GEE 与合并优势比的加权不同：评审手算的 2.17 是合并优势比，GEE 的主检验是按声符聚类的，论文里引用 GEE 的数。')

cols = ['tier', 'test', 'n', 'n_phonetics', 'group1_hits', 'group1_n', 'group1_rate', 'group0_hits', 'group0_n', 'group0_rate',
        'gee_OR', 'gee_CI95', 'gee_p_one_sided', 'gee_p_one_sided_exact', 'gee_p_two_sided', 'mh_strata', 'mh_OR', 'mh_CI95', 'cmh_p_two_sided', 'fisher_p_two_sided', 'verdict', 'note']
with open(os.path.join(E, 'yisheng_bias_reverse_scenario.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for r in res: w.writerow({k: r.get(k, '') for k in cols})
open(os.path.join(E, 'ext_bias_reverse_scenario_output.txt'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
print('\n'.join(lines))
