# 扩大盲编的分析（2026-09-30，Claude 数据线程）。分析计划见 analysis_plan.md；本脚本与计划同时提交，在任何编码之前写定。
# 用法（在仓库根目录）：python3 youwen/ext_coding/ext_analysis.py [--dry-run]
# 读：ext_items_key.csv、raw/pass{1,2}_b{01..07}.txt（编码代理的原始回答）、blind_coding_sheet_llm_coded.xlsx、
#     yisheng_claude_codes.csv、yisheng_dataset.csv、yisheng_xiaoxu_collation_final.csv
# 写：blind_coding_extended_pass1.xlsx、blind_coding_extended_pass2.xlsx（盲编表，不显示组别）
#     ext_codes_long.csv（每条的两次编码与组别、中古音类别，供复核）
#     yisheng_models_ext_coding.csv（主检验与次要检验；旧值写在 note 列）
#     ext_kappa_output.txt（两次盲编的 κ、锚定条目与原盲编的一致）
#     ext_check_sheet.xlsx、ext_check_key.csv（作者核验表：两次盲编的全部分歧 + 其余随机 50 条）
# --dry-run：用随机编码代替原始回答，只检查脚本能否跑通，输出写到 ext_coding/dryrun/，不作任何结论。
import os, re, sys, csv, math, random, warnings
import numpy as np, pandas as pd, openpyxl
import statsmodels.api as sm, statsmodels.formula.api as smf
from statsmodels.stats.contingency_tables import StratifiedTable
from scipy.stats import fisher_exact, norm
from openpyxl.styles import Font, Alignment
warnings.filterwarnings('ignore')
Y = 'youwen'; E = os.path.join(Y, 'ext_coding')
DRY = '--dry-run' in sys.argv
OUT = os.path.join(E, 'dryrun') if DRY else E
os.makedirs(OUT, exist_ok=True)
SEED_CHECK, N_CHECK_RANDOM, N_BATCH = 20260934, 50, 7
SESOI = 2.0  # 最小关心效应（analysis_plan.md §4）

key = pd.read_csv(os.path.join(E, 'ext_items_key.csv'), encoding='utf-8-sig', dtype=str)

# ---------- 1. 读原始回答 ----------
LINE = re.compile(r'^\s*(\d+)\s*[\t,|]\s*([YENX])\s*[\t,|]\s*([123])\s*(?:[\t,|]\s*(.*))?$')
def parse(path, n):
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
codes = {}
rng_dry = random.Random(1)
for p in (1, 2):
    for b in range(1, N_BATCH + 1):
        sub = key[key[f'p{p}_batch'].astype(int) == b]
        n = len(sub)
        if DRY:
            got = {i: (rng_dry.choice('YYEENNNNX'), rng_dry.choice([1, 2, 3]), '') for i in range(1, n + 1)}
        else:
            got = parse(os.path.join(E, 'raw', f'pass{p}_b{b:02d}.txt'), n)
        for _, r in sub.iterrows():
            c, conf, note = got[int(r[f'p{p}_item'])]
            codes[(p, r.sw_id)] = (c, conf, note)
for p in (1, 2):
    key[f'p{p}_code'] = [codes[(p, s)][0] for s in key.sw_id]
    key[f'p{p}_conf'] = [codes[(p, s)][1] for s in key.sw_id]
    key[f'p{p}_note'] = [codes[(p, s)][2] for s in key.sw_id]

# ---------- 2. 盲编表（与原表同样的列，外加批次；不显示组别） ----------
EXPL = ['扩大盲编（2026-09-30）：第 {p} 次独立盲编。编码人是独立的 LLM 子代理，每批一个新实例，不给任何文件，禁止读盘、上网。',
        '说明与原 100 条盲编相同（blind_coding_llm_protocol.md）；完整提示见 ext_coding/prompts/pass{p}_b*.txt，协议与分析计划见 ext_coding/analysis_plan.md。',
        'Y = 相同或近义；E = 经一步引申或推理才能连上；N = 看不出语义关系；X = 成员字是专名。把握 1–3。',
        '每批约 97 条新条目加 5 条锚定条目（原 100 条中的条目，锚定=是），条目顺序随机，两次编码的分批与顺序不同。本表不显示组别。']
for p in (1, 2):
    wb = openpyxl.Workbook(); g = wb.active; g.title = '说明'
    for line in EXPL: g.append([line.format(p=p)])
    g.column_dimensions['A'].width = 120
    ws = wb.create_sheet('编码')
    ws.append(['批次', '条目', '声符字', '声符字释义', '成员字', '成员字释义', '语义关系(Y/E/N/X)', '把握(1-3)', '备注', '锚定'])
    for _, r in key.sort_values([f'p{p}_batch', f'p{p}_item'], key=lambda s: s.astype(int)).iterrows():
        ws.append([int(r[f'p{p}_batch']), int(r[f'p{p}_item']), r.phonetic, r.phonetic_gloss, r.char, r.member_gloss,
                   r[f'p{p}_code'], int(r[f'p{p}_conf']), r[f'p{p}_note'], '是' if r.role == 'anchor' else ''])
    for col, w in zip('ABCDEFGHIJ', [6, 6, 8, 40, 8, 40, 14, 9, 24, 6]): ws.column_dimensions[col].width = w
    for c in ws[1]: c.font = Font(bold=True)
    ws.freeze_panes = 'A2'
    wb.save(os.path.join(OUT, f'blind_coding_extended_pass{p}.xlsx'))

# ---------- 3. 合并：框内全部已编码字对 ----------
d = pd.read_csv(os.path.join(Y, 'yisheng_dataset.csv'), encoding='utf-8-sig', dtype=str)
A = d[d.in_analysis_set == 'True']
yph = set(A[A.relation == '亦聲'].phonetic)
F = A[A.phonetic.isin(yph)].copy()
DEP = {'member', 'head'}
def cat4(r):
    if pd.isna(r.mc_relation): return np.nan
    if r.mc_relation == 'identical': return 'identical'
    if r.mc_relation == 'tone_voicing_alt': return 'alt_departing' if r.mc_qusheng_direction in DEP else 'alt_other'
    return 'other'
F['cat4'] = F.apply(cat4, axis=1)
M = F[F.cat4.notna()]
assert (int(((M.relation == '亦聲') & (M.cat4 == 'identical')).sum()), int((M.relation == '亦聲').sum()),
        int(((M.relation == '聲') & (M.cat4 == 'identical')).sum()), int((M.relation == '聲').sum())) == (63, 177, 133, 858)
LAY = {r['sw_id']: r['layer'] for r in csv.DictReader(open(os.path.join(Y, 'yisheng_xiaoxu_collation_final.csv'), encoding='utf-8-sig'))}
F['layer'] = F.sw_id.map(LAY)

ws = openpyxl.load_workbook(os.path.join(Y, 'blind_coding_sheet_llm_coded.xlsx'))['编码']
S = pd.DataFrame(list(ws.iter_rows(min_row=2, values_only=True)), columns=['item', 'series', 'sgloss', 'char', 'cgloss', 'code', 'conf', 'note'])
CC = pd.read_csv(os.path.join(Y, 'yisheng_claude_codes.csv'), encoding='utf-8-sig', dtype=str)
S['item'] = S['item'].astype(str); S = S.merge(CC[['item', 'char', 'relation']], on='item', suffixes=('', '_c'))
S = S.merge(F[['phonetic', 'char', 'relation', 'sw_id']], left_on=['series', 'char', 'relation'], right_on=['phonetic', 'char', 'relation'], how='left')
S = S[S.sw_id.notna()]
assert len(S) == 90

NEW = key[key.role == 'new']
rows = []
for _, r in S.iterrows():
    rows.append(dict(sw_id=r.sw_id, source='original_100', code1=r.code, code2=r.code, conf1=r.conf, conf2=r.conf))
for _, r in NEW.iterrows():
    rows.append(dict(sw_id=r.sw_id, source='extended', code1=r.p1_code, code2=r.p2_code, conf1=r.p1_conf, conf2=r.p2_conf))
C = pd.DataFrame(rows).merge(F[['sw_id', 'phonetic', 'char', 'relation', 'cat4', 'paronomastic_gloss', 'layer', 'mc_relation']], on='sw_id', how='left')
assert len(C) == 767 and C.sw_id.is_unique and C.relation.notna().all()
C['label'] = (C.relation == '亦聲').astype(int)
C['near'] = C.cat4.isin(['identical', 'alt_departing']).astype(int)
C['ident'] = (C.cat4 == 'identical').astype(int)
C.to_csv(os.path.join(OUT, 'ext_codes_long.csv'), index=False, encoding='utf-8-sig')

# ---------- 4. 统计工具 ----------
res = []
def gee(df, formula, term):
    x = df.copy()
    for cs, nm in [(sm.cov_struct.Exchangeable(), 'exchangeable'), (sm.cov_struct.Independence(), 'independence')]:
        try:
            g = smf.gee(formula, groups='phonetic', data=x, family=sm.families.Binomial(), cov_struct=cs).fit()
            b, se = g.params[term], g.bse[term]
            # |b| < 10 且 se < 10：排除完全分离时的发散估计（编码后加入，见 analysis_plan.md §7）
            if np.isfinite(b) and np.isfinite(se) and 0 < se < 10 and abs(b) < 10:
                return dict(OR=math.exp(b), lo=math.exp(b - 1.96 * se), hi=math.exp(b + 1.96 * se),
                            p2=2 * norm.sf(abs(b / se)), p1=norm.sf(b / se), cov=nm, n=len(x), clusters=x.phonetic.nunique())
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
        r.update(gee_OR=round(g['OR'], 2), gee_CI95=f"{g['lo']:.2f}-{g['hi']:.2f}", gee_p_one_sided='%.2g' % g['p1'], gee_p_two_sided='%.2g' % g['p2'], gee_cov=g['cov'])
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

# ---------- 5. 主检验 ----------
P = frame('code1'); PR = P[P.related == 1]
add('primary', 'P1 near (MC identical or departing-tone alternation) ~ label | pairs coded related (Y/E), pass-1 codes', PR, 'near', decide=True,
    note=f'one-sided test of OR > 1; smallest effect of interest OR {SESOI}; group1 = labelled, group0 = ordinary. '
         'Old (v7, 83-pair blind sample, descriptive): 14/25 vs 2/6, Fisher p 0.39 (yisheng_models_v7_checks.csv, related pairs only)')

# ---------- 6. 次要检验 ----------
add('secondary', 'S1 MC identical ~ label | related, pass-1 codes', PR, 'ident', decide=True, note='old (v7): 9/25 vs 1/6')
NP = frame('code1', sub=lambda x: x[x.paronomastic_gloss != 'True'])
add('secondary', 'S2 near ~ label | related, paronomastic glosses removed (both groups)', NP[NP.related == 1], 'near', decide=True)
SH = frame('code1', sub=lambda x: x[(x.label == 0) | (x.layer == 'both')])
add('secondary', 'S3 near ~ label | related, labels shared with Xiao Xu only (all ordinary kept)', SH[SH.related == 1], 'near', decide=True,
    note='definition of v7 Table 7: labelled entries dropped, all ordinary compounds kept')
# S4 = 主检验那一行的 mh_* 列（声符内 MH）
P2 = frame('code2'); P2R = P2[P2.related == 1]
add('secondary', 'S5 near ~ label | related, pass-2 codes for the new items (original blind codes for the 90 old items)', P2R, 'near', decide=True)
PY = frame('code1', related=('Y',))
add('secondary', 'S6 near ~ label | pairs coded Y only (strict relatedness), pass-1 codes', PY[PY.related == 1], 'near', decide=True,
    note='guards against residual confounding by true relatedness when E is a noisy proxy')
AG = P[(P.source == 'original_100') | (P.code1.isin(['Y', 'E']) == P.code2.isin(['Y', 'E']))]
add('secondary', 'S7 near ~ label | related, pairs whose two passes agree on related vs unrelated', AG[AG.related == 1], 'near', decide=True)
g_old = dict(note='old: v7 official H2 25/33 vs 6/50, GEE OR 22.0 [7.1, 68.0], p 3.9e-08 (83-pair blind sample; manuscript_checks_output.txt line 65); '
                  'frame-corrected 25/33 vs 6/46, OR 20.2 [6.56, 62.13] (yisheng_models_v7_checks.csv, blind sample frame)')
add('secondary', 'S8 H2 related (Y/E) ~ label | all coded pairs in the MC frame, X excluded, pass-1 codes', P, 'related', **g_old)
add('secondary', 'S8b H2 related (Y/E) ~ label | as S8 with pass-2 codes', P2, 'related')
add('secondary', 'S9 near ~ related + label: coefficient of related (meaning-first precondition), pass-1 codes', P, 'near', x='related', formula='near ~ related + label',
    note='group1 = related, group0 = unrelated (both groups pooled); old (v7, 79 in-frame pairs, ordinary logit): related OR 10.06 [2.17, 46.58]')
add('secondary', 'S9 near ~ related + label: coefficient of label, pass-1 codes', P, 'near', x='label', formula='near ~ related + label',
    note='old (v7, 79 in-frame pairs, ordinary logit): label OR 1.28 [0.29, 5.55]')
for grp, nm in [(1, 'labelled'), (0, 'ordinary')]:
    add('secondary', f'S9 near ~ related within {nm} pairs, pass-1 codes', P[P.label == grp], 'near', x='related',
        note='group1 = related, group0 = unrelated; old (v7): ' + ('14/25 vs 0/8' if grp else '2/6 vs 4/40'))

# ---------- 6b. 探索（编码完成、看过主结果之后加入，见 analysis_plan.md §7；不是预注册检验，不进判读） ----------
PE = frame('code1', related=('E',))
add('exploratory', 'X1 near ~ label | pairs coded E only, pass-1 codes (stand-in for S6, which is not estimable)', PE[PE.related == 1], 'near',
    note='added after the first run: S6 has only 4 ordinary pairs coded Y (0 near), so the strength-of-relatedness bias is checked within E instead')
PRY = PR.copy(); PRY['isY'] = (PRY.code1 == 'Y').astype(int)
add('exploratory', 'X2 near ~ label + Y: coefficient of label | related, pass-1 codes (adjusts for Y vs E)', PRY, 'near', formula='near ~ label + isY',
    note='added after the first run; group1 = labelled, group0 = ordinary')
CORE = frame('code1', sub=lambda x: x[(x.paronomastic_gloss != 'True') & ((x.label == 0) | (x.layer == 'both'))])
add('exploratory', 'X3 near ~ label | related, labels shared with Xiao Xu and no paronomastic gloss (v7 core; ordinary without paronomastic gloss)', CORE[CORE.related == 1], 'near',
    note='added after the first run; S2 and S3 combined, as in the v7 core (92 pairs, not conditioned on relatedness: GEE 1.59 [0.97, 2.61])')
add('exploratory', 'X4 near ~ label | related, the 677 newly coded items only, pass-1 codes', PR[PR.source == 'extended'], 'near',
    note='added after the reviewer check (v7_work/review/ext_coding_review.md §2); the 90 original items alone are row X4b')
add('exploratory', 'X4b near ~ label | related, the 90 original blind-coded items only (original blind codes)', PR[PR.source == 'original_100'], 'near',
    note='added with X4; old (v7): 14/25 vs 2/6, Fisher p 0.39')

# ---------- 7. 描述 ----------
ALLL = C[C.label == 1].copy(); ALLL['related'] = ALLL.code1.isin(['Y', 'E']).astype(int)
for nm, sub in [('all 212 labelled pairs', ALLL), ('labelled pairs without MC readings', ALLL[ALLL.cat4.isna()])]:
    s2 = sub[sub.code1 != 'X']
    res.append(dict(tier='descriptive', test=f'coded related (Y/E), X excluded | {nm}', n=len(s2), group1_hits=int(s2.related.sum()), group1_n=len(s2),
                    group1_rate=round(s2.related.mean(), 3) if len(s2) else '', note=f'X coded: {int((sub.code1 == "X").sum())}'))
for k in ['identical', 'alt_departing', 'alt_other', 'other']:
    for grp, nm in [(1, 'labelled'), (0, 'ordinary')]:
        s2 = PR[PR.label == grp]
        res.append(dict(tier='descriptive', test=f'MC category {k} | related {nm} pairs', n=len(s2), group1_hits=int((s2.cat4 == k).sum()), group1_n=len(s2),
                        group1_rate=round((s2.cat4 == k).mean(), 3) if len(s2) else ''))
for k in ['identical', 'alt_departing', 'alt_other', 'other']:
    s2 = P[P.cat4 == k]
    res.append(dict(tier='descriptive', test=f'coded related (Y/E) | MC category {k}, labelled and ordinary pooled', n=len(s2),
                    group1_hits=int(s2.related.sum()), group1_n=len(s2), group1_rate=round(s2.related.mean(), 3) if len(s2) else '',
                    note='old (v7): identical 10/13, alt_departing 6/7, alt_other 1/6, other 14/53'))

cols = ['tier', 'test', 'n', 'n_phonetics', 'group1_hits', 'group1_n', 'group1_rate', 'group0_hits', 'group0_n', 'group0_rate',
        'gee_OR', 'gee_CI95', 'gee_p_one_sided', 'gee_p_two_sided', 'gee_cov', 'mh_strata', 'mh_OR', 'mh_CI95', 'cmh_p_two_sided',
        'fisher_p_two_sided', 'verdict', 'note']
with open(os.path.join(OUT, 'yisheng_models_ext_coding.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for r in res: w.writerow({k: r.get(k, '') for k in cols})

# ---------- 8. κ ----------
def kappa(a, b):
    a, b = list(a), list(b); n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    cats = set(a) | set(b)
    pe = sum((a.count(k) / n) * (b.count(k) / n) for k in cats)
    return ((po - pe) / (1 - pe) if pe < 1 else float('nan')), po
lines = []
def rep(tag, a, b):
    k4, p4 = kappa(a, b); k2, p2 = kappa([x in 'YE' for x in a], [y in 'YE' for y in b]); kY, pY = kappa([x == 'Y' for x in a], [y == 'Y' for y in b])
    lines.append(f'{tag}: n={len(a)}  四类 κ={k4:.3f}（一致率 {p4:.1%}）  相关(Y/E)/不相关 κ={k2:.3f}（一致率 {p2:.1%}）  Y/非Y κ={kY:.3f}（一致率 {pY:.1%}）')
rep('新条目 第一次 vs 第二次', NEW.p1_code, NEW.p2_code)
for rel, nm in [('亦聲', '亦声组'), ('聲', '普通组')]:
    s2 = NEW[NEW.relation == rel]; rep(f'  其中{nm}', s2.p1_code, s2.p2_code)
AN = key[key.role == 'anchor']
rep('锚定 35 条 第一次 vs 原盲编', AN.p1_code, AN.orig_code)
rep('锚定 35 条 第二次 vs 原盲编', AN.p2_code, AN.orig_code)
rep('锚定 35 条 第一次 vs 第二次', AN.p1_code, AN.p2_code)
lines.append('')
lines.append('新条目两次编码的交叉表（行 = 第一次，列 = 第二次）：')
lines.append(pd.crosstab(NEW.p1_code, NEW.p2_code).to_string())
lines.append('')
for _, r in AN[AN.p1_code != AN.orig_code].iterrows():
    lines.append(f'锚定分歧（第一次）{r.phonetic}/{r.char}：原 {r.orig_code}，第一次 {r.p1_code}')
for _, r in AN[AN.p2_code != AN.orig_code].iterrows():
    lines.append(f'锚定分歧（第二次）{r.phonetic}/{r.char}：原 {r.orig_code}，第二次 {r.p2_code}')
# 附记（2026-09-30 编码开始后、正式运行前加入，见 analysis_plan.md §7）：同一代理实例多交的回答，不进任何分析
extra = [(p, b) for p in (1, 2) for b in range(1, N_BATCH + 1)
         if not DRY and os.path.exists(os.path.join(E, 'raw', f'pass{p}_b{b:02d}_second_answer_not_used.txt'))]
if extra:
    lines.append('')
    lines.append('附记（不进分析，见 analysis_plan.md §7）：同一代理实例多交的第二份回答与算数的第一份比较')
    for p, b in extra:
        n = int((key[f'p{p}_batch'].astype(int) == b).sum())
        g1 = parse(os.path.join(E, 'raw', f'pass{p}_b{b:02d}.txt'), n)
        g2 = parse(os.path.join(E, 'raw', f'pass{p}_b{b:02d}_second_answer_not_used.txt'), n)
        a1, a2 = [g1[i][0] for i in range(1, n + 1)], [g2[i][0] for i in range(1, n + 1)]
        k4, p4 = kappa(a1, a2)
        lines.append(f'  第{"一二"[p - 1]}次盲编第 {b} 批：n={n}，四类一致 {sum(x == y for x, y in zip(a1, a2))}/{n}，κ={k4:.3f}')
open(os.path.join(OUT, 'ext_kappa_output.txt'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')

# ---------- 9. 作者核验表：两次盲编的全部分歧 + 其余新条目中随机 50 条（不显示组别） ----------
dis = NEW[NEW.p1_code != NEW.p2_code]
agr = NEW[NEW.p1_code == NEW.p2_code].sort_values('sw_id', key=lambda s: s.astype(int))
rc = random.Random(SEED_CHECK)
pick = rc.sample(list(agr.sw_id), min(N_CHECK_RANDOM, len(agr)))
CH = pd.concat([dis.assign(why='两次不一致'), agr[agr.sw_id.isin(pick)].assign(why='随机抽查')])
order = list(CH.sw_id); rc.shuffle(order)
CH = CH.set_index('sw_id').loc[order].reset_index(); CH['check_id'] = range(1, len(CH) + 1)
wb = openpyxl.Workbook(); g = wb.active; g.title = '说明'
for line in ['作者核验表（扩大盲编，2026-09-30）',
             f'共 {len(CH)} 条：两次独立 LLM 盲编不一致的全部 {len(dis)} 条，加上两次一致的条目中随机抽的 {len(pick)} 条（随机种子 {SEED_CHECK}），顺序已打乱。表中不显示是否亦声。',
             '做法：请先只看 C–F 列（声符字、成员字和两者的《说文》释义），在 G 列填您的判断（Y/E/N/X），再看 H、I 两列的两次盲编；如有不同意见，在 J 列写一句理由。',
             'Y = 相同或近义（如 厓“山邊也” / 涯“水邊也”）；E = 经一步引申或推理才能连上（如 亡“逃也” / 忘“不識也”）；N = 看不出语义关系；X = 成员字是专名（地名、水名、姓氏、动植物名等）。',
             '只看本义，不看后起义和假借义；拿不准时，Y 与 E 之间取 E，E 与 N 之间取 N。请不要去查这个字在原书中是不是亦声。',
             '这是核验，不是主编码：分析用第一次盲编；您的判断会单独报告与盲编的一致率，改动了的条目另做一次敏感性分析。']:
    g.append([line])
g.column_dimensions['A'].width = 130
ws = wb.create_sheet('核验')
ws.append(['核验编号', '类型', '声符字', '声符字释义', '成员字', '成员字释义', '作者判断(Y/E/N/X)', '第一次盲编', '第二次盲编', '作者备注'])
for _, r in CH.iterrows():
    ws.append([int(r.check_id), r.why, r.phonetic, r.phonetic_gloss, r.char, r.member_gloss, '', r.p1_code, r.p2_code, ''])
dv = openpyxl.worksheet.datavalidation.DataValidation(type='list', formula1='"Y,E,N,X"', allow_blank=True)
ws.add_data_validation(dv); dv.add(f'G2:G{len(CH) + 1}')
for col, w in zip('ABCDEFGHIJ', [8, 10, 7, 40, 7, 40, 14, 10, 10, 30]): ws.column_dimensions[col].width = w
for c in ws[1]: c.font = Font(bold=True)
for row in ws.iter_rows(min_row=2):
    for c in row: c.alignment = Alignment(wrap_text=True, vertical='top')
ws.freeze_panes = 'A2'
wb.save(os.path.join(OUT, 'ext_check_sheet.xlsx'))
CH[['check_id', 'sw_id', 'phonetic', 'char', 'relation', 'why', 'p1_code', 'p2_code']].to_csv(os.path.join(OUT, 'ext_check_key.csv'), index=False, encoding='utf-8-sig')

for r in res:
    print(r['tier'], '|', r['test'], '|', f"{r.get('group1_hits', '')}/{r.get('group1_n', '')} vs {r.get('group0_hits', '')}/{r.get('group0_n', '')}",
          '| GEE', r.get('gee_OR', ''), r.get('gee_CI95', ''), 'p1', r.get('gee_p_one_sided', ''), '| MH', r.get('mh_OR', ''), r.get('mh_CI95', ''),
          '|', r.get('verdict', ''))
print('\n'.join(lines[:8]))
print('check sheet rows:', len(CH), '(disagreements', len(dis), ')')
