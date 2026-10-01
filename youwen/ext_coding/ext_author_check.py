# 扩大盲编：作者核验结果的处理（2026-09-30，Claude 数据线程）。按 analysis_plan.md §4.5：
#   (1) 报告作者判断与第一次、第二次盲编的一致率和 κ；
#   (2) 用作者改判值替换后重做检验（敏感性分析），主检验仍按 §4.2，不因此改动。
# 用法（在仓库根目录）：python3 youwen/ext_coding/ext_author_check.py
# 读：ext_check_sheet_author_filled.xlsx（Qu 交回的核验表，原样保存）、ext_check_key.csv、ext_codes_long.csv
# 写：ext_author_check_output.txt（一致率、κ、交叉表）、yisheng_models_ext_author_check.csv（改判后的检验）
# 说明：gee()/mh()/verdict()/add()/frame() 与 ext_analysis.py 中的同名函数逐字相同（该脚本按预登记写定，不作修改；
#       本脚本先用“不替换”的数据重现 ext_analysis.py 的结果，见 `identity check`，再做替换）。
import os, re, csv, math, random, warnings
import numpy as np, pandas as pd, openpyxl
import statsmodels.api as sm, statsmodels.formula.api as smf
from statsmodels.stats.contingency_tables import StratifiedTable
from scipy.stats import fisher_exact, norm
warnings.filterwarnings('ignore')
E = os.path.join('youwen', 'ext_coding')
SESOI = 2.0
SEED_BOOT, N_BOOT = 20260935, 2000

# ---------- 读入 ----------
ws = openpyxl.load_workbook(os.path.join(E, 'ext_check_sheet_author_filled.xlsx'))['核验']
A = pd.DataFrame(list(ws.iter_rows(min_row=2, values_only=True)),
                 columns=['check_id', 'why', 'phon', 'pg', 'char', 'mg', 'author', 'p1s', 'p2s', 'note'])
K = pd.read_csv(os.path.join(E, 'ext_check_key.csv'), encoding='utf-8-sig', dtype=str)
A['check_id'] = A.check_id.astype(str)
M = A.merge(K, on='check_id', suffixes=('', '_k'))
assert len(A) == len(M) == 126
assert (M.phon == M.phonetic).all() and (M['char'] == M['char_k']).all() and (M.p1s == M.p1_code).all() and (M.p2s == M.p2_code).all()
assert M.author.isin(list('YENX')).all() and M.check_id.is_unique
M['dis'] = (M.why_k == '两次不一致')
assert int(M.dis.sum()) == 76 and int((~M.dis).sum()) == 50

C = pd.read_csv(os.path.join(E, 'ext_codes_long.csv'), encoding='utf-8-sig', dtype=str)
for c in ['label', 'near', 'ident']: C[c] = C[c].astype(int)
C['cat4'] = C.cat4.replace('nan', np.nan)
assert C.sw_id.is_unique and len(C) == 767

lines = []
def out(s=''): lines.append(s)

# ---------- 1. 一致率与 κ ----------
def kappa(a, b):
    a, b = list(a), list(b); n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    cats = set(a) | set(b)
    pe = sum((a.count(k) / n) * (b.count(k) / n) for k in cats)
    return ((po - pe) / (1 - pe) if pe < 1 else float('nan')), po
def wkappa(x, y, w):
    """加权 κ：按权重 w 重复条目（w 为浮点），x、y 为类别序列。"""
    x, y, w = np.array(x), np.array(y), np.array(w, float)
    tot = w.sum(); po = w[x == y].sum() / tot
    pe = sum(w[x == k].sum() / tot * w[y == k].sum() / tot for k in set(x) | set(y))
    return (po - pe) / (1 - pe) if pe < 1 else float('nan'), po
def views(s):
    return {'四类': list(s), '相关(Y/E)/不相关': [c in 'YE' for c in s], 'Y/非Y': [c == 'Y' for c in s]}

out('作者核验结果（Qu 交回的 ext_check_sheet_author_filled.xlsx，126 条：两次盲编不一致的全部 76 条 + 两次一致的条目中随机抽的 50 条）')
out('表中没有备注。据 Qu 在评审线程的说明（2026-09-30 16:42，经协调者转来；更正了我 13:24 对“一起”的误读）：126 条由两位作者各自分开核对，再汇总成这一张表，每条一个编码。在手的只有汇总表，所以下面是“作者汇总判断对 LLM”的一致度，不是作者间一致度；汇总时两人判断不同的条目怎么定，Qu 未说明。表上显示了抽查类型和两次盲编的编码，核验不独立于它们。')
out('')
out('作者判断的分布： ' + '，'.join(f'{k} {int((M.author == k).sum())}' for k in 'YENX'))
out('')
d, r = M[M.dis], M[~M.dis]
out('一、不一致的 76 条：作者站在哪一边')
out(f'  与第一次盲编相同 {int((d.author == d.p1_code).sum())}，与第二次盲编相同 {int((d.author == d.p2_code).sum())}，与两次都不同 {int(((d.author != d.p1_code) & (d.author != d.p2_code)).sum())}')
out('  交叉表（行 = 第一次/第二次，列 = 作者）：')
out(pd.crosstab(d.p1_code + '/' + d.p2_code, d.author).to_string())
out('')
out('二、随机抽的 50 条（两次盲编一致）：作者与共同编码的一致')
out(f'  四类一致 {int((r.author == r.p1_code).sum())}/50；相关/不相关一致 {int((r.author.isin(list("YE")) == r.p1_code.isin(list("YE"))).sum())}/50；X 与非 X 一致 {int(((r.author == "X") == (r.p1_code == "X")).sum())}/50')
out('  交叉表（行 = 共同编码，列 = 作者）：')
out(pd.crosstab(r.p1_code, r.author).to_string())
out('')

# 分层估计：不一致层是全数，随机层是从 601 条一致条目中随机抽 50 条
N_AGR, N_DIS = 677 - 76, 76
assert int((C.source == 'extended').sum()) == 677
W = np.where(M.dis, 1.0, N_AGR / 50)
def est(col, view):
    va, vb = views(M[col].values), views(M.author.values)
    return wkappa(va[view], vb[view], W)
rng = np.random.default_rng(SEED_BOOT)
di, ri = np.where(M.dis.values)[0], np.where(~M.dis.values)[0]
out('三、估计到全部 677 个新条目（不一致层全数，一致层按 601/50 加权）：作者与盲编的一致率和 κ')
out('  一致率是分层估计，κ 由加权后的交叉表算出；区间是分层自助法（2,000 次，种子 %d）的 95%% 百分位区间。' % SEED_BOOT)
out('  这是作者与 LLM 之间的一致度，不是作者间信度；作者判断也不是金标准，只是核验。')
est_rows = []
for col, nm in [('p1_code', '作者 vs 第一次盲编'), ('p2_code', '作者 vs 第二次盲编')]:
    for view in ['四类', '相关(Y/E)/不相关', 'Y/非Y']:
        k0, p0 = est(col, view)
        ks, ps = [], []
        for _ in range(N_BOOT):
            idx = np.concatenate([rng.choice(di, len(di)), rng.choice(ri, len(ri))])
            a = M[col].values[idx]; b = M.author.values[idx]; w = W[idx]
            va, vb = views(a), views(b)
            kk, pp = wkappa(va[view], vb[view], w)
            ks.append(kk); ps.append(pp)
        out(f'  {nm} | {view}: 一致率 {p0:.1%} [{np.nanpercentile(ps, 2.5):.1%}, {np.nanpercentile(ps, 97.5):.1%}]，κ = {k0:.3f} [{np.nanpercentile(ks, 2.5):.3f}, {np.nanpercentile(ks, 97.5):.3f}]')
out('')
out('  对照：两次盲编之间（新条目 677 条）四类 κ 0.817，相关/不相关 κ 0.833，Y/非Y κ 0.740（ext_kappa_output.txt）。')
out('')
out('四、按亦声/普通分组看一致（描述；作者做核验时看不到组别）')
for rel, nm in [('亦聲', '亦声组'), ('聲', '普通组')]:
    s = M[M.relation == rel]; sd = s[s.dis]; sr = s[~s.dis]
    out(f'  {nm}：核验 {len(s)} 条；其中不一致 {len(sd)} 条，作者同第一次 {int((sd.author == sd.p1_code).sum())}、同第二次 {int((sd.author == sd.p2_code).sum())}；随机 {len(sr)} 条，作者同共同编码 {int((sr.author == sr.p1_code).sum())}')
out('')

# ---------- 2. 改判后的敏感性分析 ----------
# 所有两次盲编不一致的新条目（76）都在核验表里，其余未核验的新条目两次编码相同。
# 所以“以作者判断替换核验过的 126 条”得到的数据，与用第一次或第二次盲编作底得到的相同，只有一份。
auth = dict(zip(M.sw_id, M.author))
C['codeA'] = [auth.get(s, c1) for s, c1 in zip(C.sw_id, C.code1)]
unchecked_ext = C[(C.source == 'extended') & (~C.sw_id.isin(auth))]
assert (unchecked_ext.code1 == unchecked_ext.code2).all()
n_change = int(sum(auth[s] != c1 for s, c1 in zip(M.sw_id, M.p1_code)))
out('五、改判后的敏感性分析')
out(f'  以作者判断替换核验过的 126 条（其余新条目两次盲编相同，原 90 条仍用原盲编值）。与第一次盲编的编码不同的有 {n_change} 条，与第二次不同的有 {int((M.author != M.p2_code).sum())} 条。')
for rel, nm in [('亦聲', '亦声'), ('聲', '普通')]:
    s = M[M.relation == rel]
    out(f'  其中{nm}对：与第一次不同 {int((s.author != s.p1_code).sum())}/{len(s)}')

out('  改判的方向（作者相对第一次盲编；只算核验过的 126 条，描述性，作者看不到组别）：')
def trans(a, b):
    ra, rb = a in 'YE', b in 'YE'
    if a == b: return '不变'
    if (a == 'X') != (b == 'X'): return 'X→非X' if a == 'X' else '非X→X'
    if ra and not rb: return '相关→不相关'
    if rb and not ra: return '不相关→相关'
    return '相关内 Y/E 之间'
for rel, nm in [('亦聲', '亦声对'), ('聲', '普通对')]:
    s_ = M[M.relation == rel]
    tt = pd.Series([trans(a, b) for a, b in zip(s_.p1_code, s_.author)]).value_counts()
    out(f'    {nm}（{len(s_)} 条）： ' + '，'.join(f'{k} {v}' for k, v in tt.items()))
from scipy.stats import binomtest
n1_, n2_ = int((d.author == d.p1_code).sum()), int((d.author == d.p2_code).sum())
out(f'  不一致的 76 条中，作者与两次盲编之一相同的 {n1_ + n2_} 条里，站在第二次一边的 {n2_} 条（同第一次 {n1_} 条）；对称的二项检验双侧 p = {binomtest(n2_, n1_ + n2_, 0.5).pvalue:.2g}（描述性）。')
out('')

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
        r.update(gee_OR=round(g['OR'], 2), gee_CI95=f"{g['lo']:.2f}-{g['hi']:.2f}", gee_p_one_sided='%.2g' % g['p1'], gee_p_two_sided='%.2g' % g['p2'])
    if x == 'label' and formula is None:
        m = mh(df, y)
        if m: r.update(mh_strata=m['strata'], mh_OR=round(m['OR'], 2), mh_CI95=f"{m['lo']:.2f}-{m['hi']:.2f}", cmh_p_two_sided='%.2g' % m['p'])
    a, n1, c, n0 = r['group1_hits'], r['group1_n'], r['group0_hits'], r['group0_n']
    if n1 and n0: r['fisher_p_two_sided'] = '%.2g' % fisher_exact([[a, n1 - a], [c, n0 - c]])[1]
    if decide: r['verdict'] = verdict(g)
    r['note'] = note
    res.append(r); return g
def frame(code_col, related=('Y', 'E'), sub=None):
    x = C[C.cat4.notna() & (C[code_col] != 'X')].copy()
    x['related'] = x[code_col].isin(related).astype(int)
    return x if sub is None else sub(x)

def battery(code_col, tag):
    P = frame(code_col); PR = P[P.related == 1]
    add(tag, 'P1 near ~ label | related', PR, 'near', decide=True)
    add(tag, 'S1 MC identical ~ label | related', PR, 'ident', decide=True)
    NP = frame(code_col, sub=lambda x: x[x.paronomastic_gloss != 'True'])
    add(tag, 'S2 near ~ label | related, paronomastic glosses removed', NP[NP.related == 1], 'near', decide=True)
    SH = frame(code_col, sub=lambda x: x[(x.label == 0) | (x.layer == 'both')])
    add(tag, 'S3 near ~ label | related, labels shared with Xiao Xu only', SH[SH.related == 1], 'near', decide=True)
    CORE = frame(code_col, sub=lambda x: x[(x.paronomastic_gloss != 'True') & ((x.label == 0) | (x.layer == 'both'))])
    add(tag, 'X3 near ~ label | related, shared and non-paronomastic (exploratory)', CORE[CORE.related == 1], 'near', decide=True)
    PY = frame(code_col, related=('Y',))
    add(tag, 'S6 near ~ label | coded Y only', PY[PY.related == 1], 'near', decide=True)
    PE = frame(code_col, related=('E',))
    add(tag, 'X1 near ~ label | coded E only (exploratory)', PE[PE.related == 1], 'near')
    add(tag, 'S8 H2 related ~ label | all coded pairs, X excluded', P, 'related')
    add(tag, 'S9 near ~ related + label: coefficient of label', P, 'near', x='label', formula='near ~ related + label')
    add(tag, 'S9 near ~ related + label: coefficient of related', P, 'near', x='related', formula='near ~ related + label')
    ex = PR[PR.source == 'extended']
    add(tag, 'X4 near ~ label | related, new items only (exploratory)', ex, 'near')

battery('code1', 'identity_pass1')      # 对照：应与 yisheng_models_ext_coding.csv 中第一次盲编的各行相同
battery('codeA', 'author_adjudicated')  # 作者判断替换核验过的 126 条

# identity check：不替换时应重现 ext_analysis.py 的结果
ref = pd.read_csv(os.path.join(E, 'yisheng_models_ext_coding.csv'), encoding='utf-8-sig', dtype=str).fillna('')
chk = {'P1': 'P1', 'S1': 'S1', 'S2': 'S2', 'S3': 'S3', 'X3': 'X3', 'S8': 'S8 H2 related (Y/E) ~ label | all coded pairs in the MC frame, X excluded, pass-1 codes', 'X4': 'X4'}
ok = True; msgs = []
for r in [x for x in res if x['tier'] == 'identity_pass1']:
    tag = r['test'].split(' ')[0]
    if tag not in chk: continue
    m = ref[ref.test.str.startswith(chk[tag])]
    m = m[m.tier != 'descriptive']
    if tag == 'X4': m = m[m.test.str.startswith('X4 ')]
    if len(m) != 1: ok = False; msgs.append(f'{tag}: {len(m)} rows in reference'); continue
    m = m.iloc[0]
    same = all(str(r.get(c, '')) == m[c] for c in ['group1_hits', 'group1_n', 'group0_hits', 'group0_n', 'gee_OR', 'gee_CI95', 'gee_p_one_sided', 'mh_OR', 'mh_CI95'])
    if not same: ok = False; msgs.append(f'{tag}: differs')
out('')
out('  identity check（不替换，用第一次盲编）：' + ('与 yisheng_models_ext_coding.csv 中相应各行逐格相同' if ok else '有不同：' + '；'.join(msgs)))
out('')
out('  检验                                   | 第一次盲编（对照）                       | 作者判断替换后')
def fmt(r):
    if r is None: return '—'
    g = f"{r['group1_hits']}/{r['group1_n']} vs {r['group0_hits']}/{r['group0_n']}"
    o = f", OR {r['gee_OR']} [{r['gee_CI95'].replace('-', ', ')}], p1 {r['gee_p_one_sided']}" if 'gee_OR' in r else ', 不可估'
    if r.get('mh_OR', '') != '': o += f"; MH {r['mh_OR']} [{r['mh_CI95'].replace('-', ', ')}]"
    return g + o
byname = {}
for r in res: byname.setdefault(r['test'], {})[r['tier']] = r
for name, dd in byname.items():
    out(f"  {name}\n      对照： {fmt(dd.get('identity_pass1'))}\n      替换： {fmt(dd.get('author_adjudicated'))}" + (f"\n      规则： {dd['author_adjudicated'].get('verdict', '')}" if dd['author_adjudicated'].get('verdict') else ''))

cols = ['tier', 'test', 'n', 'n_phonetics', 'group1_hits', 'group1_n', 'group1_rate', 'group0_hits', 'group0_n', 'group0_rate',
        'gee_OR', 'gee_CI95', 'gee_p_one_sided', 'gee_p_two_sided', 'mh_strata', 'mh_OR', 'mh_CI95', 'cmh_p_two_sided', 'fisher_p_two_sided', 'verdict', 'note']
with open(os.path.join(E, 'yisheng_models_ext_author_check.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for r in res: w.writerow({k: r.get(k, '') for k in cols})
open(os.path.join(E, 'ext_author_check_output.txt'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
print('\n'.join(lines))
