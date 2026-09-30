# 扩大盲编：偏差敏感性（临界点）分析（2026-09-30，Claude 数据线程；探索性，不进判读）。
# 来源：独立评审对 v8 的意见（v7_work/review/v8_review.md “偏差敏感性分析”一节）经协调者转来。
# 问题：如果 (A)“意义先行”为真（标注只由真实相关决定，给定真实相关后标注与读音无关），
#       编码把真实不相关的字对错判为“相关”的比例要多大，才能在编为相关的字对里造出观察到的近音差别（P1：73/141 对 23/79）？
#       再与实际看到的编码分歧对照（两次盲编之间；第一次盲编与作者汇总判断之间）。
# 用法（在仓库根目录）：python3 youwen/ext_coding/ext_bias_sensitivity.py
# 读：ext_codes_long.csv、ext_check_sheet_author_filled.xlsx、ext_check_key.csv
# 写：ext_bias_sensitivity_output.txt、yisheng_bias_sensitivity_grid.csv
# 只用已有的编码，不做新的 LLM 编码；不改任何既有文件。
#
# 模型（都写在前面）：
#   R* = 真实相关（不可观测），R = 第一次盲编编为相关（Y/E），L = 是否亦声，N = 近音（中古同音或去声交替）。
#   (A)：L 只由 R* 决定，即给定 R*，N 与 L 无关；因此真实相关的字对里，亦声组与普通组的近音比例相同（真实 OR = 1）。
#   编码误差：给定 R* 与 L，R 与 N 无关（编码人看不到读音，误差与读音无关）；误差允许因组而异，
#     假阳率 fp_L、fp_O = 真实不相关而编为相关的比例（亦声组、普通组），灵敏度 se_L、se_O 任意。
#   在这些假设下，真实相关字对的近音比例可由观察到的 2×2×2 表反推：
#     A*_{l,n} = (a_{l,n} - fp_l * T_{l,n}) / (se_l - fp_l)，a = 编为相关的数，T = 该格总数；
#     真实相关中亦声与普通的近音优势比 OR* = (A*_{L,1}/A*_{L,0}) / (A*_{O,1}/A*_{O,0})，其中 se_l 在比值中约去，所以只取决于 fp_L 与 fp_O。
#   OR* 用合并的（未加权的）优势比，观察值是 2.61；GEE（按声符聚类、可交换）主检验是 2.35，两者只是加权不同。
#   区间：按声符整体重抽样（自助法，5000 次，种子 20260936），不含 fp 本身的不确定性，除非另有说明。
import os, csv
import numpy as np, pandas as pd, openpyxl
from scipy.stats import fisher_exact

E = os.path.join('youwen', 'ext_coding')
B, SEED = 5000, 20260936
YE = ('Y', 'E')
rng = np.random.default_rng(SEED)
lines = []
def out(s=''): lines.append(s)

# ---------- 数据：与 ext_analysis.py 的主检验样本相同（框内、有中古音、第一次盲编不是 X） ----------
C = pd.read_csv(os.path.join(E, 'ext_codes_long.csv'), encoding='utf-8-sig', dtype=str)
for c in ['label', 'near']: C[c] = C[c].astype(int)
C['cat4'] = C.cat4.replace('nan', np.nan)
P = C[C.cat4.notna() & (C.code1 != 'X')].copy()
assert len(P) == 634 and int(P.label.sum()) == 172
P['R1'] = P.code1.isin(YE).astype(int)
phon = sorted(P.phonetic.unique()); pix = {p: i for i, p in enumerate(phon)}
cnt = np.zeros((len(phon), 2, 2, 2), dtype=np.int64)          # [声符, 亦声, 近音, 编为相关]
for r in P.itertuples(): cnt[pix[r.phonetic], r.label, r.near, r.R1] += 1
tot = cnt.sum(0)
assert tot[1, 1, 1] == 73 and tot[1, 0, 1] == 68 and tot[0, 1, 1] == 23 and tot[0, 0, 1] == 56   # P1 的 73/141 对 23/79

def orstar(c, fpL, fpO):
    """c[..., 亦声, 近音, 编为相关]；返回校正后的真实相关字对中的近音优势比。假阳率过大使某格被“扣光”时按极限处理。"""
    gL, gO = fpL / (1 - fpL), fpO / (1 - fpO)
    aL1 = c[..., 1, 1, 1] - gL * c[..., 1, 1, 0]; aL0 = c[..., 1, 0, 1] - gL * c[..., 1, 0, 0]
    aO1 = c[..., 0, 1, 1] - gO * c[..., 0, 1, 0]; aO0 = c[..., 0, 0, 1] - gO * c[..., 0, 0, 0]
    with np.errstate(all='ignore'):
        res = (aL1 * aO0) / (aL0 * aO1)
    ok = (aL1 > 0) & (aL0 > 0) & (aO1 > 0) & (aO0 > 0)
    res = np.where(ok, res, np.nan)
    res = np.where((aL1 > 0) & (aL0 > 0) & (aO0 <= 0) & (aO1 > 0), 0.0, res)       # 普通组不近音的相关对被全部“扣光”：OR* 趋于 0
    res = np.where((aL1 > 0) & (aL0 > 0) & (aO1 <= 0) & (aO0 > 0), np.inf, res)    # 近音的相关对被扣光：OR* 趋于无穷
    return res
def fp_max(c=tot):   # 普通组不近音的相关对不被扣成负数的最大假阳率
    g = c[0, 0, 1] / c[0, 0, 0]; return g / (1 + g)
def solve(fn, target, hi):
    """fn 关于 fp_O 单调下降；求 fn(fp_O) = target 的 fp_O；fp_O = 0 时已不高于目标返回 0.0，到上限仍高于目标返回 None。"""
    if not fn(0.0) > target: return 0.0
    if fn(hi) > target: return None
    lo = 0.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if fn(mid) > target: lo = mid
        else: hi = mid
    return (lo + hi) / 2

# 自检：用已知真值的表检验校正公式（真实 OR 分别为 1 与 2，误差因组而异）
def _selftest(tL1, tL0):
    uL1, uL0, uO1, uO0, tO1, tO0 = 30., 70., 70., 310., 10., 10.
    fpL, fpO, seL, seO = 0.05, 0.11, 0.8, 0.9
    c = np.zeros((2, 2, 2))
    for l, n, tr, un, se, fp in [(1, 1, tL1, uL1, seL, fpL), (1, 0, tL0, uL0, seL, fpL), (0, 1, tO1, uO1, seO, fpO), (0, 0, tO0, uO0, seO, fpO)]:
        a = se * tr + fp * un; c[l, n, 1] = a; c[l, n, 0] = tr + un - a
    return float(orstar(c, fpL, fpO))
assert abs(_selftest(50., 50.) - 1.0) < 1e-9 and abs(_selftest(100., 50.) - 2.0) < 1e-9

# 自助法：按声符整体重抽样
ix = rng.integers(0, len(phon), (B, len(phon)))
boot = cnt[ix].sum(1)
def boot_q(fpL, fpO):
    v = orstar(boot, fpL, fpO); v = v[~np.isnan(v)]
    return np.percentile(v, 2.5), np.percentile(v, 97.5), len(v)
def boot_lo(fpL, fpO): return boot_q(fpL, fpO)[0]
def ci(v):
    v = np.asarray(v, dtype=float); v = v[~np.isnan(v)]
    return np.percentile(v, 2.5), np.percentile(v, 97.5)
def pct(x): return f'{x:.1%}'

# ---------- 1. 观察到的表 ----------
out('偏差敏感性（临界点）分析（探索性；用已有的第一次盲编，没有新的编码）')
out('模型与假设见 ext_bias_sensitivity.py 开头。要点：(A) 为真时真实 OR = 1；编码误差与读音无关，但可因亦声/普通而异。')
out('')
out('一、观察到的表（主检验样本：框内、有中古音、第一次盲编不是 X，634 对；与 P1 相同）')
out(f'  编为相关：亦声 近音 {tot[1,1,1]}、不近音 {tot[1,0,1]}；普通 近音 {tot[0,1,1]}、不近音 {tot[0,0,1]}')
out(f'  编为不相关：亦声 近音 {tot[1,1,0]}、不近音 {tot[1,0,0]}；普通 近音 {tot[0,1,0]}、不近音 {tot[0,0,0]}')
crude = (tot[1, 1, 1] / tot[1, 0, 1]) / (tot[0, 1, 1] / tot[0, 0, 1])
nU_O, nU_L, nR_O = int(tot[0, :, 0].sum()), int(tot[1, :, 0].sum()), int(tot[0, :, 1].sum())
out(f'  合并优势比 {crude:.2f}（GEE 主检验 2.35 [1.43, 3.86]，只是加权不同）')
out(f'  编为相关的字对里近音占：亦声 {tot[1,1,1]}/{tot[1,:,1].sum()} = {tot[1,1,1]/tot[1,:,1].sum():.0%}，普通 {tot[0,1,1]}/{nR_O} = {tot[0,1,1]/nR_O:.0%}。')
out(f'  编为不相关的字对：普通组 {nU_O} 对，亦声组只有 {nU_L} 对，前者是后者的 {nU_O/nU_L:.0f} 倍：能被错判成“相关”的真实不相关字对，普通组多得多。')
out('')

# ---------- 2. 临界点 ----------
out('二、临界点：使校正后的真实 OR* 降到目标值所需的普通组假阳率 fp_O（假阳率 = 真实不相关而被编为相关的比例）；亦声组假阳率 fp_L 取下列各值')
hi_ = fp_max() * (1 - 1e-9)
out(f'  普通组假阳率的上限（再高，编为相关而不近音的 {tot[0,0,1]} 对都不够扣）：{pct(fp_max())}')
out('  目标 | fp_L | 需要的 fp_O | 其中被扣掉的普通相关对占编为相关的普通对 | 剩下的真实相关普通对')
rows_tip, xtip = [], {}
for target in [2.0, 1.5, 1.0, 'lower']:
    for fpL in [0.0, 0.05, 0.10, 0.20, 0.30]:
        if target == 'lower':
            fn = lambda x, fpL=fpL: boot_lo(fpL, x); tv, tag = 1.0, 'OR* 的自助法 95% 下限 = 1'
        else:
            fn = lambda x, fpL=fpL: orstar(tot, fpL, x); tv, tag = target, f'OR* = {target:g}'
        x = solve(fn, tv, hi_)
        if x is None:
            out(f'  {tag} | {fpL:.0%} | 不可能'); continue
        g = x / (1 - x); fpos = g * nU_O; xtip[(target, fpL)] = (x, fpos)
        out(f'  {tag} | {fpL:.0%} | {pct(x)} | {fpos:.0f}/{nR_O} = {fpos/nR_O:.0%} | {nR_O-fpos:.0f}')
        rows_tip.append(dict(kind='tipping', target=('lower95=1' if target == 'lower' else target), fp_L=fpL, fp_O_required=round(x, 4),
                             false_pos_share_of_coded_related_ordinary=round(fpos / nR_O, 3)))
# 不因组而异的假阳率
xnd = solve(lambda x: orstar(tot, x, x), 1.0, hi_)
xndl = solve(lambda x: boot_lo(x, x), 1.0, hi_)
gnd = xnd / (1 - xnd)
out(f'  两组假阳率相同（fp_L = fp_O）：OR* = 1 需要 {pct(xnd)}；自助法 95% 区间的下限降到 1 需要 {pct(xndl)}')
out(f'    此时亦声组只有约 {gnd*nU_L:.0f}/{tot[1,:,1].sum()} 对编为相关的是假阳（{gnd*nU_L/tot[1,:,1].sum():.0%}），普通组约 {gnd*nU_O:.0f}/{nR_O}（{gnd*nU_O/nR_O:.0%}）。')
xg = solve(lambda x: orstar(tot, 0.0, x), crude / 2.35, hi_)
xgn = solve(lambda x: orstar(tot, x, x), crude / 2.35, hi_)
out(f'  换成 GEE 的尺度（把合并值 2.61 对到 2.35，目标 OR* = 2.61/2.35 = {crude/2.35:.3f}）：fp_L = 0 时 fp_O = {pct(xg)}；fp_L = fp_O 时 {pct(xgn)}（与合并尺度的 {pct(solve(lambda x: orstar(tot, 0.0, x), 1.0, hi_))}、{pct(xnd)} 相差不到 1 个百分点）')
out('')
out(f'  读法：需要的不是“两组假阳率差多少”。两组假阳率相同（约 11.6%）就够了，原因是普通组里真实不相关的字对多（{nU_O} 对，亦声组 {nU_L} 对），')
out('  同样的假阳率下，普通组编为相关的字对里假阳占的比例（约 64%）远高于亦声组（约 3%）。换个说法：(A) 为真时，普通组真实相关的字对里近音的比例')
out(f'  应与亦声组相同（{tot[1,1,1]}/{tot[1,0,1]} = {tot[1,1,1]/tot[1,0,1]:.2f} 对 1），而观察到的是 {tot[0,1,1]}/{tot[0,0,1]} = {tot[0,1,1]/tot[0,0,1]:.2f}；要把 {tot[0,1,1]}/{tot[0,0,1]} 拉到 1.07，')
out(f'  就得认定 {nR_O} 个编为相关的普通对里约 50 个是假阳（假阳不挑读音，主要落在占多数的不近音对里）。')
out('  OR* 随 fp_O 下降，越往后越陡（fp_L = 0；fp_O → OR*）：' + '；'.join(f'{pct(x)} → {float(orstar(tot, 0.0, x)):.2f}' for x in [0.0, 0.025, 0.05, 0.075, 0.10, 0.115]))
out('')

# ---------- 3. 与实际看到的编码分歧对照 ----------
out('三、对照：实际看到的编码分歧（都是编码人之间的分歧，不是相对于许慎的判断；见文末限制）')
# (a) 第一次 vs 第二次：新条目里框内两次都不是 X 的字对
Nn = P[(P.source == 'extended') & (P.code2 != 'X')].copy(); Nn['R2'] = Nn.code2.isin(YE).astype(int)
def two_pass(df):
    d = np.zeros((len(phon), 2, 6), dtype=np.int64)
    for r in df.itertuples():
        i = pix[r.phonetic]
        d[i, r.label, 0] += (r.R2 == 0); d[i, r.label, 1] += (r.R1 == 1 and r.R2 == 0); d[i, r.label, 2] += (r.R1 == 1)
        d[i, r.label, 3] += (r.R1 == 0); d[i, r.label, 4] += (r.R2 == 1 and r.R1 == 0); d[i, r.label, 5] += (r.R2 == 1)
    return d
d2 = two_pass(Nn); d2t = d2.sum(0); d2b = d2[ix].sum(1)
two = {}
for l, nm in [(0, '普通'), (1, '亦声')]:
    nl = int((Nn.label == l).sum())
    fpv = d2t[l, 1] / d2t[l, 0]; sh = d2t[l, 1] / d2t[l, 2]
    fpr = d2t[l, 4] / d2t[l, 3]
    with np.errstate(all='ignore'):
        cfp = ci(d2b[:, l, 1] / d2b[:, l, 0]); csh = ci(d2b[:, l, 1] / d2b[:, l, 2]); cfpr = ci(d2b[:, l, 4] / d2b[:, l, 3])
    two[l] = dict(fp=fpv, fpr=fpr, sh=sh)
    out(f'  第一次 vs 第二次（{nm}对，新条目里框内两次都不是 X 的 {nl} 对）：')
    out(f'    以第二次为参照：第二次编为不相关的 {d2t[l,0]} 对里第一次编为相关的 {d2t[l,1]} 对，假阳率 {pct(fpv)} [{pct(cfp[0])}, {pct(cfp[1])}]；第一次编为相关的 {d2t[l,2]} 对里第二次不同意的占 {sh:.0%} [{csh[0]:.0%}, {csh[1]:.0%}]')
    out(f'    以第一次为参照：第一次编为不相关的 {d2t[l,3]} 对里第二次编为相关的 {d2t[l,4]} 对，假阳率 {pct(fpr)} [{pct(cfpr[0])}, {pct(cfpr[1])}]')
out('  （两次盲编之间的分歧大致是每次各自随机误差之和，所以单次的随机假阳率约是上面数字的一半；系统性误差——两次犯同样的错——看不出来。）')
# (b) 第一次盲编 vs 作者汇总判断：分层估计
ws = openpyxl.load_workbook(os.path.join(E, 'ext_check_sheet_author_filled.xlsx'))['核验']
Ad = pd.DataFrame(list(ws.iter_rows(min_row=2, values_only=True)), columns=['check_id', 'why', 'phon', 'pg', 'char', 'mg', 'author', 'p1s', 'p2s', 'note'])
Ad['check_id'] = Ad.check_id.astype(str)
K = pd.read_csv(os.path.join(E, 'ext_check_key.csv'), encoding='utf-8-sig', dtype=str)
M0 = Ad.merge(K, on='check_id', suffixes=('', '_k')); assert len(M0) == 126
M0['dis'] = (M0.why_k == '两次不一致')
fr = P.set_index('sw_id')
M = M0[M0.sw_id.isin(fr.index) & (M0.author != 'X')].copy()
M['label'] = fr.label.loc[M.sw_id].values; M['near'] = fr.near.loc[M.sw_id].values
M['R1'] = fr.R1.loc[M.sw_id].values; M['Ra'] = M.author.isin(YE).astype(int)
M['w'] = np.where(M.dis, 1.0, 601 / 50)
out(f'  作者汇总判断的核验条目中，框内且作者不判 X 的 {len(M)} 条（不一致层 {int(M.dis.sum())}，随机层 {int((~M.dis).sum())}，随机层每条代表 601/50 = 12.02 条）。')
for l, nm in [(0, '普通'), (1, '亦声')]:
    s = M[(M.label == l) & (M.R1 == 1)]
    out(f'    {nm}对里第一次编为相关的抽查条目：随机层 {int((~s.dis).sum())} 条（作者判为不相关 {int(((~s.dis) & (s.Ra == 0)).sum())} 条），不一致层 {int(s.dis.sum())} 条（作者判为不相关 {int((s.dis & (s.Ra == 0)).sum())} 条）')
ml, mn, m1, ma, mw = (M[c].values for c in ['label', 'near', 'R1', 'Ra', 'w'])
idd, idr = np.where(M.dis.values)[0], np.where(~M.dis.values)[0]
A_orig = np.zeros((2, 2))                                      # 原 100 条（作者本人编过）：框内第一次编码为相关的字对
for r in P[P.source == 'original_100'].itertuples():
    if r.R1 == 1: A_orig[r.label, r.near] += 1
def stats(ii):
    l, n, r1, ra, w = ml[ii], mn[ii], m1[ii], ma[ii], mw[ii]
    res = {}
    for g in (0, 1):
        s = l == g
        neg = w[s & (ra == 0)].sum(); pos = w[s & (r1 == 1)].sum(); fa = w[s & (r1 == 1) & (ra == 0)].sum()
        res[g] = (fa / neg if neg > 0 else np.nan, fa / pos if pos > 0 else np.nan)
    A = A_orig.copy()
    for g in (0, 1):
        for k in (0, 1): A[g, k] += w[(l == g) & (n == k) & (ra == 1)].sum()
    orw = (A[1, 1] * A[0, 0]) / (A[1, 0] * A[0, 1]) if min(A[1, 0], A[0, 1]) > 0 else np.nan
    return res, orw, A
ast, orw0, Aw = stats(np.arange(len(M)))
fpO_b, fsO_b, fsL_b, orw_b = [], [], [], []
for _ in range(B):
    ii = np.concatenate([idd[rng.integers(0, len(idd), len(idd))], idr[rng.integers(0, len(idr), len(idr))]])
    r, o, _A = stats(ii)
    fpO_b.append(r[0][0]); fsO_b.append(r[0][1]); fsL_b.append(r[1][1]); orw_b.append(o)
fpO_b = np.array(fpO_b)
cfpO, cfsO, cfsL, corw = ci(fpO_b), ci(fsO_b), ci(fsL_b), ci(orw_b)
out(f'  第一次盲编 vs 作者（普通对）：作者判为不相关的字对里第一次编为相关的占（假阳率）{pct(ast[0][0])} [{pct(cfpO[0])}, {pct(cfpO[1])}]；'
    f'第一次编为相关的字对里作者判为不相关的占 {ast[0][1]:.0%} [{cfsO[0]:.0%}, {cfsO[1]:.0%}]')
out(f'  第一次盲编 vs 作者（亦声对）：第一次编为相关的字对里作者判为不相关的占 {ast[1][1]:.0%} [{cfsL[0]:.0%}, {cfsL[1]:.0%}]；'
    f'亦声组的假阳率（{pct(ast[1][0])}）不可用：作者判为不相关的亦声对极少，几乎都落在第一次编为相关的里面，估计值超出模型可行范围（fp_L < 75%）。')
# 未核验的普通相关对
chk = set(M0.sw_id)
unc = P[(P.source == 'extended') & (P.label == 0) & (P.R1 == 1) & ~P.sw_id.isin(chk)]
n_o_o = int(((P.source == 'original_100') & (P.label == 0) & (P.R1 == 1)).sum())
n_o_e = int(((P.source == 'extended') & (P.label == 0) & (P.R1 == 1)).sum())
n_o_c = int(((P.source == 'extended') & (P.label == 0) & (P.R1 == 1) & P.sw_id.isin(chk)).sum())
out(f'  第一次编为相关的 {nR_O} 个普通对里：原 100 条的 {n_o_o} 个作者本人编过；新条目的 {n_o_e} 个里抽查过 {n_o_c} 个（含作者判为 X 的），还有 {len(unc)} 个没有作者判断。')
out('')
out('  各参照下普通组假阳的估计（对照第二节的临界点：OR* = 1 需要 fp_O 11.5%，即 50/79 = 63% 的普通相关对是假阳）：')
g4 = two[0]['fp'] / (1 - two[0]['fp']); ga = ast[0][0] / (1 - ast[0][0])
out(f'    两次盲编（第二次为参照）：fp_O {pct(two[0]["fp"])}，折合 {g4*nU_O:.0f}/{nR_O} = {g4*nU_O/nR_O:.0%} 的普通相关对是假阳')
out(f'    作者汇总判断：fp_O {pct(ast[0][0])}，折合 {ga*nU_O:.0f}/{nR_O} = {ga*nU_O/nR_O:.0%}；直接数：第一次编为相关的普通对里作者判为不相关的占 {ast[0][1]:.0%}（约 {int(round(ast[0][1]*nR_O))}/{nR_O}）')
out('')

# ---------- 4. 在实际看到的假阳率下，校正后的 OR* ----------
out('四、在实际看到的假阳率下，校正后的 OR*（亦声组假阳率取 0，或与普通组相同；区间同时含声符重抽样与对照样本的重抽样）')
def corrected(fps, fpb, same):
    o = float(orstar(tot, fps if same else 0.0, fps))
    vals = np.array([float(orstar(boot[b], (fpb[b] if same else 0.0), fpb[b])) for b in range(B) if not np.isnan(fpb[b])])
    vals = vals[~np.isnan(vals)]
    return o, np.percentile(vals, 2.5), np.percentile(vals, 97.5)
fp2s = two[0]['fp']; fp2b = d2b[:, 0, 1] / d2b[:, 0, 0]
corr = {}
for key, nm, fps, fpb in [('two', '两次盲编（第二次为参照）', fp2s, fp2b), ('auth', '作者汇总判断', ast[0][0], fpO_b)]:
    for same, tag in [(False, '只校正普通组（fp_L = 0）'), (True, '两组假阳率相同')]:
        o, lo_, hi_b = corrected(fps, fpb, same); corr[(key, same)] = (o, lo_, hi_b)
        out(f'  {nm}，fp_O = {pct(fps)}，{tag}：OR* = {o:.2f}，95% 区间 [{lo_:.2f}, {hi_b:.2f}]')
out('  （区间下端为 0：该次重抽样的假阳率已超过上限 14.8% 左右，编为相关而不近音的普通对全被扣光，OR* 趋于 0。）')
out(f'  另一种不用假阳率模型的估计（直接改判）：把抽查条目按设计权重代表整个新条目框，原 100 条沿用原编码，以作者的判断计相关：合并 OR = {orw0:.2f}，95% 区间 [{corw[0]:.2f}, {corw[1]:.2f}]。')
out(f'    加权后作者判为相关的数：亦声 近音 {Aw[1,1]:.0f}、不近音 {Aw[1,0]:.0f}；普通 近音 {Aw[0,1]:.0f}、不近音 {Aw[0,0]:.0f}。普通组近音格只有 {Aw[0,1]:.0f} 个加权对，随机层里第一次编为相关的普通近音对只有 1 个（每个代表 12 个），所以这个估计极不稳定，方向与上面假阳率校正相反，两者都不能当证据。')
out('    未加权、只改核验条目的改判见 ext_summary §7：OR 2.73 [1.61, 4.65]。')
out('')

# ---------- 4b. 另一条路：按释义编码在近音的普通对里漏判相关（假阴，与读音有关） ----------
# 假阳路径之外，ext_summary §6 说 (A) 还有一条路：按释义编码的相关性低估了许慎对同音字对的判断。
# 模型：亦声组的灵敏度不随读音变；普通组近音与不近音的灵敏度之比 r = se_O1/se_O0。(A) 为真时观察到的 OR = 1/r，所以 r = 1/OR。
orb = (boot[:, 1, 1, 1] * boot[:, 0, 0, 1]) / (boot[:, 1, 0, 1] * boot[:, 0, 1, 1])
rlo, rhi = 1 / np.percentile(orb, 97.5), 1 / np.percentile(orb, 2.5)
need = tot[0, 0, 1] * tot[1, 1, 1] / tot[1, 0, 1]            # 普通组不近音的相关对不漏判时，近音的真实相关对要有这么多
miss = need - tot[0, 1, 1]
nU_near = int(tot[0, 1, 0])
Mn = M[(M.label == 0) & (M.near == 1) & (M.R1 == 0)]
chk_n = int(((P.source == 'extended') & (P.label == 0) & (P.near == 1) & (P.R1 == 0) & P.sw_id.isin(chk)).sum())
orig_n = int(((P.source == 'original_100') & (P.label == 0) & (P.near == 1) & (P.R1 == 0)).sum())
unc_n = int(((P.source == 'extended') & (P.label == 0) & (P.near == 1) & (P.R1 == 0) & ~P.sw_id.isin(chk)).sum())
out('四之二、另一条路：按释义编码在近音的普通对里漏判相关（假阴，且只在普通组）')
out(f'  (A) 为真且亦声组的灵敏度不随读音变时，观察到的 OR 等于普通组不近音对与近音对的灵敏度之比，所以普通组里真实相关的近音对被编为相关的机会，只有不近音对的 1/{crude:.2f} = {1/crude:.2f}（95% 区间 [{rlo:.2f}, {rhi:.2f}]，取自合并 OR 的自助法区间）。')
out(f'  换个说法：普通组不近音的相关对不漏判时，{nU_near} 个编为不相关的普通近音对里要有约 {miss:.0f} 个（{miss/nU_near:.0%}）其实相关；普通组不近音的 {tot[0,0,0]} 个编为不相关的对则几乎都不相关。编码人看不到读音；要成立，得是意义联系在同音的普通对里更常藏在释义之外、在亦声对里不然（ext_summary §6 说的那种低估）。')
out(f'  作者判断：这 {nU_near} 个普通近音对里，原 100 条的 {orig_n} 个作者编过；新条目里抽查过 {chk_n} 个，其中作者判为相关 {int((Mn.Ra == 1).sum())} 个（共 {len(Mn)} 个不判 X）；还有 {unc_n} 个没有作者判断。数太少，说不了多少。')
out('')

# ---------- 5. 网格与输出 ----------
grid = []
for fpL in [0.0, 0.05, 0.10, 0.20, 0.30]:
    for fpO in [round(x, 3) for x in np.arange(0, 0.145, 0.005)]:
        v = float(orstar(tot, fpL, fpO))
        lo, hi, nv = boot_q(fpL, fpO)
        grid.append(dict(kind='grid', fp_L=fpL, fp_O=fpO, OR_star=round(v, 3) if not np.isnan(v) else '', OR_star_boot_lo=round(lo, 3), OR_star_boot_hi=round(hi, 3) if np.isfinite(hi) else ''))
out('限制：')
out('  1. 对照用的是编码人之间的分歧（两次盲编、作者汇总判断）。它们衡量编码的随机误差，以及作者与盲编之间的差别，不是相对于许慎本人判断的系统偏离；'
    '如果基于释义的“相关”与许慎所见的“相关”之间有所有编码人共有的系统差异，这里看不出来。作者汇总判断是两位作者各自核对后汇总成的一张表，在手的只有汇总表。表上显示了抽查类型和两次盲编的编码；如果作者因此更接近它们，这里估计的假阳率偏低（偏向 (C)）。')
pL = fisher_exact([[tot[1, 1, 0], tot[1, 1, 1]], [tot[1, 0, 0], tot[1, 0, 1]]])[1]
out('  2. 假设编码误差与读音无关（编码人看不到读音，这一点由流程保证）。但亦声组里编为不相关的字对集中在不近音一侧（近音 %d/%d，不近音 %d/%d，Fisher p = %.3f），'
    '说明基于释义的“相关”与读音本来就有联系（这也是 (C) 预测的，但 (A) 下真实相关与读音相近同样可以有联系）；校正按“误差与读音无关”处理，不能区分两者。' % (tot[1, 1, 0], tot[1, 1, :].sum(), tot[1, 0, 0], tot[1, 0, :].sum(), pL))
out('  3. “相关”只分有无，没有分强弱；强弱的作用另见 X1、X2。亦声组里作者判为不相关的字对很少，亦声组假阳率估不出来，所以只给 fp_L = 0 与 fp_L = fp_O 两种。')
out('  4. 作者抽查的随机层只有 %d 条，每条代表约 12 条；普通组“作者判为不相关”的比例（%.0f%%）主要由不一致层（两次盲编分歧的字对）决定，'
    '随机层的 %d 个普通相关对里只有 %d 个判为不相关，区间很宽。要收窄，可请作者把其余 %d 个没有判断的、编为相关的普通对补判完。'
    % (int((~M.dis).sum()), ast[0][1] * 100, int(((~M.dis) & (M.label == 0) & (M.R1 == 1)).sum()), int(((~M.dis) & (M.label == 0) & (M.R1 == 1) & (M.Ra == 0)).sum()), len(unc)))
out('  5. 观察到的合并优势比 2.61 与 GEE 的 2.35 加权不同，临界点在两种尺度下差别很小（见第二节）。')
out('  6. 最可能的“共有偏差”是 E（一步引申才连上）的阈值：编为相关的普通对几乎都是 E（75/79），作者的规则是 E 与 N 拿不准取 N。'
    '只算 E（X1：1.80 [1.00, 3.25]）和控制 Y/E（X2：2.13 [1.26, 3.63]）已在 ext_summary §3 报告，方向不变，但 Y/E 本身也是编出来的，不能代替对每个字对的核验。')
out('  7. 这是探索性的敏感性分析，不改变预注册的主检验（P1 OR 2.35，按预先定的规则支持 C），也没有新的编码。')
x1, f1 = xtip[(1.0, 0.0)]; x2, f2 = xtip[(2.0, 0.0)]; x15, f15 = xtip[(1.5, 0.0)]; xlo, _f = xtip[('lower', 0.0)]
x1h = xtip[(1.0, 0.30)][0]
sm = ['要点（数字见下文各节；探索性，主检验不变）：',
      f'  1. 如果 (A) 为真（真实 OR = 1），要把合并 OR {crude:.2f} 拉到 1，真实不相关的普通对里要有 {pct(x1)} 被编成“相关”，即 {nR_O} 个编为相关的普通对里约 {f1:.0f} 个（{f1/nR_O:.0%}）是假阳；拉到 2 需要 {pct(x2)}（{f2/nR_O:.0%}），拉到 1.5 需要 {pct(x15)}（{f15/nR_O:.0%}）；自助法 95% 下限降到 1 需要 {pct(xlo)}。亦声组的假阳率几乎不影响这些数（fp_L 0–30% 时 OR* = 1 需要 {pct(x1)}–{pct(x1h)}）；两组相同时 {pct(xnd)} 就够。',
      f'  2. 所以需要的不是两组误差不同，而是基数：编为不相关的字对，普通组 {nU_O} 对，亦声组 {nU_L} 对。(A) 为真时“真实相关”是混杂因素，编码对它的测量误差在普通组里留下剩余混杂；普通组的假阳主要落在占多数的不近音对里，把编为相关的普通对的近音比例压低。',
      f'  3. 对照：两次盲编之间普通组假阳率 {pct(two[0]["fp"])}（第一次编为相关的 {d2t[0,2]} 个普通对里 {two[0]["sh"]:.0%} 第二次不同意），按它校正 OR* = {corr[("two", False)][0]:.2f} [{corr[("two", False)][1]:.2f}, {corr[("two", False)][2]:.2f}]；随机误差抹不掉这个差别。',
      f'  4. 作者汇总判断的抽查样本给出 {pct(ast[0][0])} [{pct(cfpO[0])}, {pct(cfpO[1])}]（第一次编为相关的普通对里作者判为不相关 {ast[0][1]:.0%} [{cfsO[0]:.0%}, {cfsO[1]:.0%}]，亦声对 {ast[1][1]:.0%} [{cfsL[0]:.0%}, {cfsL[1]:.0%}]），按它校正 OR* = {corr[("auth", False)][0]:.2f} [{corr[("auth", False)][1]:.2f}, {corr[("auth", False)][2]:.2f}]（{pct(ast[0][0])} 与临界值 {pct(x1)} 相近），但区间太宽，不能说明问题。原因是随机层里第一次编为相关的普通对只有 5 个（作者判为不相关 2 个），其余多来自两次盲编分歧的字对；还有 {len(unc)} 个编为相关的普通对没有作者判断。',
      f'  5. 结论：两次盲编之间的随机误差不足以抹掉这个差别；两次盲编共有的系统偏差（若有，最可能是 E 的阈值比作者宽）要多大才够：降到 2 或使下限到 1 约 {pct(x2)}，降到 1 约 {pct(x1)}；现有核验样本既不能肯定也不能排除。把其余 {len(unc)} 个没有作者判断的普通相关对补判完，可以把“假阳占多少”变成数出来的数。',
      f'  6. 另一条路（按释义编码在近音的普通对里漏判相关）：普通组里真实相关的近音对被编为相关的机会只有不近音对的 {1/crude:.2f}（[{rlo:.2f}, {rhi:.2f}]），即 {nU_near} 个编为不相关的普通近音对里约 {miss:.0f} 个其实相关，而不近音的几乎没有漏判；编码人看不到读音，要成立得是意义联系在同音的普通对里更常藏在释义之外、在亦声对里不然。作者核验里这类字对只抽查了 {len(Mn)} 个，其中判为相关 {int((Mn.Ra == 1).sum())} 个，数太少。',
      '']
lines[2:2] = sm
open(os.path.join(E, 'ext_bias_sensitivity_output.txt'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
with open(os.path.join(E, 'yisheng_bias_sensitivity_grid.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    cols = ['kind', 'target', 'fp_L', 'fp_O', 'fp_O_required', 'false_pos_share_of_coded_related_ordinary', 'OR_star', 'OR_star_boot_lo', 'OR_star_boot_hi']
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for r in rows_tip + grid: w.writerow({k: r.get(k, '') for k in cols})
print('\n'.join(lines))
