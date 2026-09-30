# 扩大盲编：第二次回答替换的敏感性分析（X5，2026-09-30，Claude 数据线程；探索性，事后，不进判读）。
# 来源：撰稿线程（v9）经协调者提出。第一遍（pass 1）第 3、6 批各有一份“第二次回答”（同一代理实例或同一提示的重新运行给了两份），
#       按分析前写定的规则（analysis_plan.md §7：每个代理实例第一份完整合格的回答算数）没有用。
#       这里把这两批的第二次回答代替第一次回答，重算主检验和相关检验，看结论是否靠那条规则。评审手算的主检验是 OR 2.39 [1.38, 4.14]。
# 命名：撰稿线程称之为“S6 敏感性”，与分析计划 §4.3 的 S6（只算 Y）不同；这里记为 X5。
# 用法（在仓库根目录）：python3 youwen/ext_coding/ext_second_answer_sensitivity.py
# 读：ext_items_key.csv、ext_codes_long.csv、raw/pass1_b03.txt、raw/pass1_b06.txt 及两者的 *_second_answer_not_used.txt、yisheng_models_ext_coding.csv
# 写：ext_second_answer_sensitivity_output.txt、yisheng_models_ext_second_answer.csv、ext_second_answer_items.csv
# 说明：gee()/mh()/verdict()/add()/frame()/battery() 与 ext_author_check.py 中的同名函数相同（后者又与 ext_analysis.py 相同）。
#       先用“不替换”的数据重现 yisheng_models_ext_coding.csv 的对应各行（identity check），再做替换。只读已有文件，不改任何既有文件。
import os, re, csv, math, warnings
import numpy as np, pandas as pd
import statsmodels.api as sm, statsmodels.formula.api as smf
from statsmodels.stats.contingency_tables import StratifiedTable
from scipy.stats import fisher_exact, norm
warnings.filterwarnings('ignore')
E = os.path.join('youwen', 'ext_coding')
SESOI = 2.0
BATCHES = (3, 6)

lines = []
def out(s=''): lines.append(s)

# ---------- 读入 ----------
key = pd.read_csv(os.path.join(E, 'ext_items_key.csv'), encoding='utf-8-sig', dtype=str)
C = pd.read_csv(os.path.join(E, 'ext_codes_long.csv'), encoding='utf-8-sig', dtype=str)
for c in ['label', 'near', 'ident']: C[c] = C[c].astype(int)
C['cat4'] = C.cat4.replace('nan', np.nan)
assert C.sw_id.is_unique and len(C) == 767

LINE = re.compile(r'^\s*(\d+)\s*[\t,|]\s*([YENX])\s*[\t,|]\s*([123])\s*(?:[\t,|]\s*(.*))?$')
def parse(path, n):          # 与 ext_analysis.py 的 parse() 相同
    got = {}
    for ln in open(path, encoding='utf-8'):
        m = LINE.match(ln.rstrip('\n'))
        if m:
            i = int(m.group(1))
            if i in got: raise ValueError(f'{path}: item {i} twice')
            got[i] = (m.group(2), int(m.group(3)), (m.group(4) or '').strip())
    missing = sorted(set(range(1, n + 1)) - set(got))
    if missing: raise ValueError(f'{path}: missing items {missing}')
    extra = sorted(set(got) - set(range(1, n + 1)))
    if extra: raise ValueError(f'{path}: unexpected items {extra}')
    return got

# ---------- 1. 两份回答：逐批读入，并核对第一份回答与 ext_codes_long.csv 里的 code1 相同 ----------
first, second = {}, {}           # sw_id -> 四类代码
batch_of = {}
rows = []
for b in BATCHES:
    sub = key[key.p1_batch.astype(int) == b]
    n = len(sub)
    g1 = parse(os.path.join(E, 'raw', f'pass1_b{b:02d}.txt'), n)
    g2 = parse(os.path.join(E, 'raw', f'pass1_b{b:02d}_second_answer_not_used.txt'), n)
    for _, r in sub.iterrows():
        i = int(r.p1_item)
        rows.append(dict(batch=b, item=i, sw_id=r.sw_id, role=r.role, first=g1[i][0], second=g2[i][0], conf1=g1[i][1], conf2=g2[i][1]))
        if r.role == 'new':
            first[r.sw_id], second[r.sw_id] = g1[i][0], g2[i][0]; batch_of[r.sw_id] = b
I = pd.DataFrame(rows)
new_ids = set(first)
chk = C[C.sw_id.isin(new_ids)]
assert len(chk) == len(new_ids) == 97 + 96 and (chk.code1.values == [first[s] for s in chk.sw_id]).all()     # 第一份回答与分析用的 code1 逐条相同
I.to_csv(os.path.join(E, 'ext_second_answer_items.csv'), index=False, encoding='utf-8-sig')

# 代码列：codeS = 两批都换；codeS3 / codeS6 = 只换一批
C['codeS'] = C.code1; C['codeS3'] = C.code1; C['codeS6'] = C.code1
for s in new_ids:
    k = C.index[C.sw_id == s][0]
    C.at[k, 'codeS'] = second[s]
    if batch_of[s] == 3: C.at[k, 'codeS3'] = second[s]
    else: C.at[k, 'codeS6'] = second[s]

# ---------- 2. 统计工具（与 ext_author_check.py 相同） ----------
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

battery('code1', 'identity_pass1')
battery('codeS', 'second_b3_b6')
battery('codeS3', 'second_b3_only')
battery('codeS6', 'second_b6_only')

# identity check：不替换时应重现 ext_analysis.py 的结果
ref = pd.read_csv(os.path.join(E, 'yisheng_models_ext_coding.csv'), encoding='utf-8-sig', dtype=str).fillna('')
chkmap = {'P1': 'P1', 'S1': 'S1', 'S2': 'S2', 'S3': 'S3', 'X3': 'X3', 'S8': 'S8 H2 related (Y/E) ~ label | all coded pairs in the MC frame, X excluded, pass-1 codes', 'X4': 'X4'}
ok = True; msgs = []
for r in [x for x in res if x['tier'] == 'identity_pass1']:
    tag = r['test'].split(' ')[0]
    if tag not in chkmap: continue
    m = ref[ref.test.str.startswith(chkmap[tag])]
    m = m[m.tier != 'descriptive']
    if tag == 'X4': m = m[m.test.str.startswith('X4 ')]
    if len(m) != 1: ok = False; msgs.append(f'{tag}: {len(m)} rows in reference'); continue
    m = m.iloc[0]
    same = all(str(r.get(c, '')) == m[c] for c in ['group1_hits', 'group1_n', 'group0_hits', 'group0_n', 'gee_OR', 'gee_CI95', 'gee_p_one_sided', 'mh_OR', 'mh_CI95'])
    if not same: ok = False; msgs.append(f'{tag}: differs')
assert ok, msgs

# ---------- 3. 输出 ----------
def kappa(a, b):
    a, b = list(a), list(b); n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    cats = set(a) | set(b)
    pe = sum((a.count(k) / n) * (b.count(k) / n) for k in cats)
    return ((po - pe) / (1 - pe) if pe < 1 else float('nan')), po
def fmt(r):
    if r is None: return '—'
    g = f"{r['group1_hits']}/{r['group1_n']} vs {r['group0_hits']}/{r['group0_n']}"
    o = f", OR {r['gee_OR']} [{r['gee_CI95'].replace('-', ', ')}], p1 {r['gee_p_one_sided']}" if 'gee_OR' in r else ', 不可估'
    if 'p1_raw' in r and 0.04 <= r['p1_raw'] <= 0.06: o += f"（单侧 p 精确值 {r['p1_raw']:.4f}，贴着 .05 的界）"
    if r.get('mh_OR', '') != '': o += f"; MH {r['mh_OR']} [{r['mh_CI95'].replace('-', ', ')}]"
    return g + o

out('第二次回答替换的敏感性分析（X5；探索性，事后，不进判读）')
out('做法：第一遍（pass 1）第 3、6 批各有一份“第二次回答”，按分析前写定的规则（每个代理实例第一份完整合格的回答算数）没有用。')
out('这里把这两批新条目的第一次回答换成第二次回答，其余不变（原 100 条的盲编码、第二遍盲编不动），重算主检验和相关检验。')
out('第 3 批的第二份回答是同一代理实例在同一上下文里交的，不独立于第一份；第 6 批的第二份是同一提示的重新运行，独立于第一份（analysis_plan.md §7）。')
out('撰稿线程称之为“S6 敏感性”，与分析计划 §4.3 的 S6（只算 Y）不同；这里记为 X5。')
out('')
out('一、两份回答的差别（新条目，不含锚定条目）')
def cls3(c): return 'R' if c in ('Y', 'E') else ('X' if c == 'X' else 'U')
for b in BATCHES:
    s = I[(I.batch == b) & (I.role == 'new')]
    k4, p4 = kappa(s['first'], s['second'])
    c1 = [cls3(c) for c in s['first']]; c2 = [cls3(c) for c in s['second']]
    k3, p3 = kappa(c1, c2)
    x_ch = int(((s['first'] == 'X') != (s['second'] == 'X')).sum())
    out(f'  第 {b} 批（{len(s)} 个新条目）：四类（Y/E/N/X）相同 {int((s["first"] == s["second"]).sum())}/{len(s)}（{p4:.1%}，κ {k4:.3f}）；三类（相关 Y/E、不相关 N、专名 X）相同 {sum(x == y for x, y in zip(c1, c2))}/{len(s)}（{p3:.1%}，κ {k3:.3f}）；其中 X 与非 X 不同 {x_ch} 条')
cc = C[C.sw_id.isin(new_ids)].copy()
cc['c1'] = cc.code1; cc['c2'] = cc.codeS
inframe = cc[cc.cat4.notna()]
out(f'  两批新条目中有中古音的 {len(inframe)} 个（亦声 {int(inframe.label.sum())}、普通 {int((inframe.label == 0).sum())}）；这些条目里第一次与第二次回答的四类代码相同 {int((inframe.c1 == inframe.c2).sum())} 个。')
out('  第一次回答 → 第二次回答的变动（框内新条目，按组别；X 为专名）：')
for l, nm in [(1, '亦声'), (0, '普通')]:
    s = inframe[inframe.label == l]
    def cls(c): return 'X' if c == 'X' else ('相关' if c in ('Y', 'E') else '不相关')
    tt = pd.Series([f'{cls(a)}→{cls(b)}' for a, b in zip(s.c1, s.c2) if cls(a) != cls(b)]).value_counts()
    out(f'    {nm}（{len(s)} 个）：' + ('，'.join(f'{k} {v}' for k, v in tt.items()) if len(tt) else '没有变动'))
out('')
out('二、主检验的表（框内、有中古音、不是 X；相关对里近音）')
for code_col, nm in [('code1', '对照（第一次回答，分析用的）'), ('codeS', '替换（第 3、6 批用第二次回答）'), ('codeS3', '只换第 3 批'), ('codeS6', '只换第 6 批')]:
    P = frame(code_col); PR = P[P.related == 1]
    L, O = PR[PR.label == 1], PR[PR.label == 0]
    out(f'  {nm}：框内 {len(P)} 对，其中编为相关 {len(PR)} 对（亦声 {len(L)}、普通 {len(O)}）；近音 亦声 {int(L.near.sum())}/{len(L)}，普通 {int(O.near.sum())}/{len(O)}')
out('')
out('三、检验（GEE 按声符聚类，单侧 p；规则：p < .05 且置信区间上限 ≥ 2 支持 C）')
byname = {}
for r in res: byname.setdefault(r['test'], {})[r['tier']] = r
tiers = [('identity_pass1', '对照（第一次回答）'), ('second_b3_b6', '替换（第 3、6 批）'), ('second_b3_only', '只换第 3 批'), ('second_b6_only', '只换第 6 批')]
for name, dd in byname.items():
    out(f'  {name}')
    for t, nm in tiers:
        rr = dd.get(t)
        out(f'      {nm}： {fmt(rr)}' + (f'；规则：{rr["verdict"]}' if rr is not None and rr.get('verdict') else ''))
out('')
pp = byname['P1 near ~ label | related']
out('四、与评审手算对照')
out(f'  评审线程手算的主检验（第 3、6 批换成第二次回答）：OR 2.39 [1.38, 4.14]。本脚本：{fmt(pp["second_b3_b6"])}。')
g_ = pp['second_b3_b6']
same = ('gee_OR' in g_) and abs(float(g_['gee_OR']) - 2.39) < 0.005 and g_['gee_CI95'] == '1.38-4.14'
out('  ' + ('数值对得上。' if same else '数值对不上（见上面本脚本的数，差异如实报告，不取评审的数）。'))
out('')
out('说明：')
out('  1. 这是探索性的事后分析。主检验仍是 analysis_plan.md §4.2 的第一次回答结果（OR 2.35），分析前写定的规则没有改动。')
out('  2. 替换只涉及两批新条目（共 193 个，其中框内的见第一节）；原 100 条的盲编码、第二遍盲编、作者核验都不动。')
out('  3. 第 3 批的第二份回答与第一份出自同一上下文，不是独立的再编码；第 6 批的第二份是同一提示的独立重新运行。“只换第 3 批”“只换第 6 批”两行用来看各自的作用。')
out('  4. 没有把两份回答合并成一个“共识”，也没有做任何新的编码。')

cols = ['tier', 'test', 'n', 'n_phonetics', 'group1_hits', 'group1_n', 'group1_rate', 'group0_hits', 'group0_n', 'group0_rate',
        'gee_OR', 'gee_CI95', 'gee_p_one_sided', 'gee_p_one_sided_exact', 'gee_p_two_sided', 'mh_strata', 'mh_OR', 'mh_CI95', 'cmh_p_two_sided', 'fisher_p_two_sided', 'verdict', 'note']
with open(os.path.join(E, 'yisheng_models_ext_second_answer.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for r in res: w.writerow({k: r.get(k, '') for k in cols})
open(os.path.join(E, 'ext_second_answer_sensitivity_output.txt'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
print('\n'.join(lines))
