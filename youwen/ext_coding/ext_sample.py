# 扩大盲编（2026-09-30，Claude 数据线程）：确定抽样框、抽样、分批，写出编码提示。不改任何既有文件。
# 用法（在仓库根目录）：python3 youwen/ext_coding/ext_sample.py
# 输出：youwen/ext_coding/ext_items_key.csv（条目与批次的对照表，含组别，编码代理看不到）
#       youwen/ext_coding/prompts/pass{1,2}_b{01..07}.txt（交给编码代理的完整提示）
# 抽样框与 v7 相同（yisheng_v7_checks.py）：分析集内仍有亦声字的 172 个声符，212 个亦声字、953 个普通字。
# 设计见 analysis_plan.md §2–§3。
import os, re, csv, random
import pandas as pd, openpyxl
Y = 'youwen'; OUT = os.path.join(Y, 'ext_coding')
SEED_SAMPLE, SEED_ANCHOR, SEED_P1, SEED_P2 = 20260930, 20260931, 20260932, 20260933
N_NEW_ORD, N_BATCH, N_ANCHOR_PER_BATCH = 500, 7, 5

d = pd.read_csv(os.path.join(Y, 'yisheng_dataset.csv'), encoding='utf-8-sig', dtype=str)
A = d[d.in_analysis_set == 'True']
yph = set(A[A.relation == '亦聲'].phonetic)
F = A[A.phonetic.isin(yph)].copy()
assert len(yph) == 172 and (F.relation == '亦聲').sum() == 212 and (F.relation == '聲').sum() == 953
assert not F.sw_id.duplicated().any()
F['has_mc'] = F.mc_relation.notna(); F['has_oc'] = F.morph_relation_auto.notna()

# 原 100 条盲编（blind_coding_sheet_llm_coded.xlsx）落在框内的条目
ws = openpyxl.load_workbook(os.path.join(Y, 'blind_coding_sheet_llm_coded.xlsx'))['编码']
S = pd.DataFrame(list(ws.iter_rows(min_row=2, values_only=True)), columns=['item', 'series', 'sgloss', 'char', 'cgloss', 'code', 'conf', 'note'])
CC = pd.read_csv(os.path.join(Y, 'yisheng_claude_codes.csv'), encoding='utf-8-sig', dtype=str)
S['item'] = S['item'].astype(str); S = S.merge(CC[['item', 'char', 'relation']], on='item', suffixes=('', '_c'))
assert (S.char == S.char_c).all()
S = S.merge(F[['phonetic', 'char', 'relation', 'sw_id']], left_on=['series', 'char', 'relation'], right_on=['phonetic', 'char', 'relation'], how='left')
O = S[S.sw_id.notna()].copy()
assert ((O.relation == '亦聲').sum(), (O.relation == '聲').sum()) == (35, 55), O.relation.value_counts()
coded = set(O.sw_id)
assert F[F.sw_id.isin(coded)].has_mc.all() and F[F.sw_id.isin(coded)].has_oc.all()  # 原样本只从两端都有 BS 构拟的字对中抽

# 新编条目：其余全部亦声字；普通字只取两端都有中古音者，按有无上古构拟分层，使合并后的普通字样本在 858 个有中古音的普通对中等概率
NL = F[(F.relation == '亦聲') & ~F.sw_id.isin(coded)]
PO = F[(F.relation == '聲') & F.has_mc & ~F.sw_id.isin(coded)]
N_MC_ORD = int(((F.relation == '聲') & F.has_mc).sum()); N_OC = int(((F.relation == '聲') & F.has_mc & F.has_oc).sum())
n_old = len(coded & set(F[F.relation == '聲'].sw_id))
target_oc = round((n_old + N_NEW_ORD) * N_OC / N_MC_ORD)
k_oc = target_oc - n_old; k_non = N_NEW_ORD - k_oc
rs = random.Random(SEED_SAMPLE)
pool_oc = sorted(PO[PO.has_oc].sw_id, key=int); pool_non = sorted(PO[~PO.has_oc].sw_id, key=int)
new_ord = rs.sample(pool_oc, k_oc) + rs.sample(pool_non, k_non)
new = list(sorted(NL.sw_id, key=int)) + new_ord
print(f'frame: 172 phonetics, 212 labelled (MC {int((F.relation == "亦聲").sum() - (~F[F.relation == "亦聲"].has_mc).sum())}), 953 ordinary (MC {N_MC_ORD}, MC+OC {N_OC})')
print(f'already coded in frame: 35 labelled, {n_old} ordinary; uncoded: labelled {len(NL)} (MC {int(NL.has_mc.sum())}), ordinary {int(((F.relation == "聲") & ~F.sw_id.isin(coded)).sum())} (MC {len(PO)})')
print(f'new ordinary: {k_oc} from the MC+OC stratum ({len(pool_oc)} uncoded), {k_non} from the MC-only stratum ({len(pool_non)} uncoded); '
      f'inclusion probability {target_oc}/{N_OC} = {target_oc / N_OC:.3f} vs {k_non}/{len(pool_non) + 0} of {N_MC_ORD - N_OC} = {k_non / (N_MC_ORD - N_OC):.3f}')

# 锚定条目：原框内 90 条中随机 35 条（去掉说明里作例子的 亡/忘），两轮共用，每批 5 条
ra = random.Random(SEED_ANCHOR)
anc_pool = sorted(O[O.char != '忘'].sw_id, key=int)
anchors = ra.sample(anc_pool, N_BATCH * N_ANCHOR_PER_BATCH)

# 释义：沿用 blind_sheet_yisheng.py 的 defn；释义以“从”开头时取到第一个句号（只有 貣 一例），免得露出“某聲”
def defn(g):
    if not isinstance(g, str) or not g.strip(): return 'None'
    x = g.split('从')[0]; x = re.sub(r'凡.{1,3}之屬皆$', '', x).strip()
    if not x: x = g.split('。')[0] + '。'
    return x
F['mg'] = F.shuowen_gloss.map(defn); F['hg'] = F.head_gloss.map(defn)
for g in list(F.mg) + list(F.hg):
    assert '亦聲' not in g and not re.search(r'从.{1,3}聲', g), g
FI = F.set_index('sw_id')

PROMPT = '''Code {n} character pairs from the Shuowen glosses given below. Each item gives an item number, a phonetic character with its Shuowen gloss, and a member character (a character written with that phonetic) with its Shuowen gloss; the structural analysis (从某, 某聲 and the like) has been removed from the glosses. Use ONLY the glosses in this prompt and your own knowledge of classical Chinese and the Shuowen. Do NOT read, search or open any file on disk, and do NOT use any web or search tool. Work alone and give your answer directly. Do NOT try to recall or check whether Xu Shen analyses the member character as 某聲, 某亦聲 or 會意.

For each item, compare the 本义 of the member character with the 本义 of the phonetic character. Pick one code:
Y: the same or near-synonymous meaning (厓 山邊也 / 涯 水邊也). E: connected only through one step of extension or inference (亡 逃也 / 忘 不識也). N: no semantic relation is visible. X: the member character is a proper name (place, river, surname, named plant or animal).

Judge by 本义 only, not later or loan meanings. Where a gloss is "None", judge from your knowledge of that character's Shuowen 本义, with confidence 1 unless sure. A pun-style gloss (e.g. 狗 "叩也") is not evidence of a real semantic relation by itself. Confidence 1–3; a note of ≤15 characters. When unsure between two codes, prefer E over Y and N over E.

Output exactly {n} lines: item, code, confidence, note (tab-separated).

Items (item, phonetic character, its gloss, member character, its gloss; tab-separated):
{items}
'''

def batches(seed):
    r = random.Random(seed)
    items = new[:]; r.shuffle(items)
    anc = anchors[:]; r.shuffle(anc)
    sizes = [len(items) // N_BATCH + (1 if i < len(items) % N_BATCH else 0) for i in range(N_BATCH)]
    out, pos = [], 0
    for b in range(N_BATCH):
        chunk = items[pos:pos + sizes[b]] + anc[b * N_ANCHOR_PER_BATCH:(b + 1) * N_ANCHOR_PER_BATCH]; pos += sizes[b]
        r.shuffle(chunk); out.append(chunk)
    return out

os.makedirs(os.path.join(OUT, 'prompts'), exist_ok=True)
pos = {}
for p, seed in [(1, SEED_P1), (2, SEED_P2)]:
    for b, chunk in enumerate(batches(seed), 1):
        lines = []
        for i, sid in enumerate(chunk, 1):
            r = FI.loc[sid]
            lines.append(f'{i}\t{r.phonetic}\t{r.hg}\t{r.char}\t{r.mg}')
            pos[(p, sid)] = (b, i)
        with open(os.path.join(OUT, 'prompts', f'pass{p}_b{b:02d}.txt'), 'w', encoding='utf-8') as f:
            f.write(PROMPT.format(n=len(chunk), items='\n'.join(lines)))

OC_ = O.set_index('sw_id')
rows = []
for sid in new + anchors:
    r = FI.loc[sid]; is_anchor = sid in anchors
    rows.append(dict(sw_id=sid, phonetic=r.phonetic, char=r.char, relation=r.relation,
                     role='anchor' if is_anchor else 'new',
                     stratum=('labelled' if r.relation == '亦聲' else ('ordinary_mc_oc' if r.has_oc else 'ordinary_mc_only')),
                     has_mc=r.has_mc, has_oc=r.has_oc,
                     orig_item=OC_.loc[sid, 'item'] if is_anchor else '', orig_code=OC_.loc[sid, 'code'] if is_anchor else '',
                     p1_batch=pos[(1, sid)][0], p1_item=pos[(1, sid)][1], p2_batch=pos[(2, sid)][0], p2_item=pos[(2, sid)][1],
                     phonetic_gloss=r.hg, member_gloss=r.mg))
with open(os.path.join(OUT, 'ext_items_key.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(f'{len(new)} new items + {len(anchors)} anchors; batch sizes', [len(c) for c in batches(SEED_P1)], [len(c) for c in batches(SEED_P2)])
