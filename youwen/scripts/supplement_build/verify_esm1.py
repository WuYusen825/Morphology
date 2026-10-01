"""Check the numbers and statements of the guide (ESM_1) against the staged files (internal; not shipped)."""
import sys, io, re, zipfile
sys.path.insert(0, '/tmp/claude-0/-home-user-Morphology/7d9f6fd5-d830-551f-9a43-e3ebcc390a52/scratchpad/esm/work')
import pandas as pd
from esm_common import *

S = dict(dtype=str, keep_default_na=False)
x2 = pd.read_excel(STAGE / 'ESM_2.xlsx', sheet_name=None, **S)
x3 = pd.read_excel(STAGE / 'ESM_3.xlsx', sheet_name=None, **S)
x6 = pd.read_excel(STAGE / 'ESM_6.xlsx', sheet_name=None, **S)
P, R, D = x2['pairs'], x2['recension_collation'], x2['daxu_spotcheck']
FS, E, A, SA = x3['first_sample'], x3['enlarged_coding'], x3['author_check'], x3['second_answers']
n_ok = 0


def ok(cond, msg):
    global n_ok
    assert cond, 'FAILED: ' + msg
    n_ok += 1


def eq(a, b, msg): ok(a == b, f'{msg}: got {a!r}, expected {b!r}')


# Section 1
F = P[P.in_comparison_frame == 'True']
eq((int((F.group == 'labelled').sum()), int((F.group == 'ordinary').sum()), F.phonetic.nunique()), (212, 953, 172), 'frame 212/953/172')
eq(len(E), 767, 'enlarged coding 767 pairs')
# Section 2
eq(P.group.value_counts().to_dict(), {'ordinary': 1054, 'labelled': 223, 'source_other': 39, 'abbreviated_phonetic': 17}, 'groups of pairs')
eq(P.relation.value_counts().to_dict(), {'聲': 1054, '亦聲': 223, '會意/其他': 39, '省聲': 17}, 'relation values')
eq(int(P.sw_id.duplicated().sum()), 1, 'one duplicated sw_id')
eq(F.sw_id.is_unique, True, 'sw_id unique in the frame')
A_ = P[P.in_analysis_set == 'True']
eq((int((A_.group == 'labelled').sum()), int((A_.group == 'ordinary').sum())), (212, 1019), 'analysis set 212 / 1,019')
# Section 3
eq(len(P), 1333, 'pairs rows'); eq(len(R), 227, 'collation rows'); eq(len(D), 104, 'register rows'); eq(len(FS), 100, 'first sample rows')
eq(len(A), 126, 'author check rows'); eq(len(SA), 203, 'second answers rows'); eq(len(x6['data_dictionary']), 199, 'ESM_6 dictionary rows')
extra = P[P.group == 'source_other']
eq(set(extra.label_source), {'duan_only', 'duan_only+xiaoxu_only', 'xiaoxu_only'}, 'extra rows come from Duan or Xiao Xu only')
eq(R[R.in_analysis_set == 'True'].layer.value_counts().to_dict(), {'both': 140, 'daxu_only': 62, 'unknown': 10}, 'layers 140/62/10')
eq(FS.group.value_counts().to_dict(), {'ordinary': 60, 'labelled': 40}, 'first sample 40 / 60')
ok((FS.oc_relation_auto != 'NA').all() and (FS.oc_relation_auto != '').all(), 'all first-sample pairs have OC forms at both ends')
eq(E.source.value_counts().to_dict(), {'extended': 677, 'original_100': 90}, '677 new + 90 first-sample')
new = E[E.source == 'extended']
eq(new.group.value_counts().to_dict(), {'ordinary': 500, 'labelled': 177}, '677 = 177 + 500')
eq(int((E.role == 'anchor').sum()), 35, '35 anchors')
eq(A.check_type.value_counts().to_dict(), {'passes_disagree': 76, 'random_agreed': 50}, '126 = 76 + 50')
eq(677 - 76, 601, '601 agree')
eq(SA.role.value_counts().to_dict(), {'new': 193, 'anchor': 10}, '203 = 193 + 10'); eq(set(SA.batch), {'3', '6'}, 'second answers: batches 3 and 6')
# Section 4.1: prompts, None glosses, collection log
z5 = zipfile.ZipFile(STAGE / 'ESM_5.zip')
names = z5.namelist()
prompts = sorted(n for n in names if '/prompts/pass' in n)
eq(len(prompts), 14, '14 prompts')
sizes = []; anchors_per = []
K = pd.read_csv(io.BytesIO(z5.read('enlarged_coding_materials/item_key.csv')), encoding='utf-8-sig', **S)
nn = 0
for n in prompts:
    t = z5.read(n).decode('utf-8')
    lines = t.split('tab-separated):\n')[1].strip('\n').split('\n')
    sizes.append(len(lines))
    m = re.search(r'pass(\d)_b(\d\d)', n); ps, b = m.group(1), int(m.group(2))
    sub = K[K[f'p{ps}_batch'] == str(b)]
    eq(len(sub), len(lines), f'prompt {n} lines = key rows')
    anchors_per.append(int((sub.role == 'anchor').sum()))
    nn += sum(1 for l in lines if l.split('\t')[2] == 'None')
ok(set(sizes) == {101, 102}, f'prompt sizes {set(sizes)}'); eq(set(anchors_per), {5}, '5 anchors per batch')
eq(sorted(set(sizes)), [101, 102], 'prompt sizes 101 or 102')
none_pairs = K[K.phonetic_gloss == 'None']
eq((len(none_pairs), none_pairs.phonetic.nunique()), (10, 8), 'None glosses: 10 pairs, 8 phonetics')
eq(int((E.phonetic_gloss == '').sum()), 10, 'enlarged_coding: empty phonetic_gloss cells = 10')
eq(int((FS.phonetic_gloss == '').sum()), 2, 'first sample: empty phonetic_gloss cells = 2')
eq(set(P[P.head_in_shuowen == 'False'].phonetic) >= set(none_pairs.phonetic), True, 'None glosses belong to phonetics that are not head entries')
log = pd.read_csv(io.BytesIO(z5.read('enlarged_coding_materials/collection_log.csv')), encoding='utf-8-sig', **S)
ok((log.parsable_lines == log.expected_lines).all() and len(log) == 14, 'collection log: all 14 answers parsable')
ok(log.tool_uses_reported.isin(['0', '1 (SubagentHandback)']).all(), 'collection log: only the hand-back reported')
# new items per batch 96/97
nb = K[K.role == 'new']
ok(set(nb.groupby('p1_batch').size()) == {96, 97}, 'new items per batch 96 or 97')
# Section 4.2
eq(sorted(set(P.mc_relation)), ['NA', 'identical', 'other', 'tone_voicing_alt'], 'mc_relation values')
eq(sorted(set(P.mc_qusheng_direction)), ['', 'head', 'member', 'none'], 'mc_qusheng_direction values')
eq(sorted(set(E.cat4) - {''}), ['alt_departing', 'alt_other', 'identical', 'other'], 'cat4 values')
eq(sorted(set(P.oc_bs_match)), ['mc_match', 'multiple_readings', 'not_in_bs', 'single_reading'], 'oc_bs_match values')
eq(sorted(set(P.morph_relation_auto)), ['C', 'I', 'NA', 'O', 'O2', 'R', 'V'], 'morph_relation_auto values')
eq(sorted(set(P.mc_confidence)), ['identical_fanqie', 'initial+rhyme+tone', 'initial_only', 'no_match_first_reading', 'none', 'rhyme+tone_only'], 'mc_confidence values')
# Section 4.4
ident = F[F.mc_relation == 'identical']
ct = pd.crosstab(ident.identical_relation_type, ident.group)
eq(int(ct['labelled'].sum()), 63, '63 labelled homophonous'); eq(int(ct['ordinary'].sum()), 133, '133 ordinary homophonous')
eq(int((P.identical_relation_type != '').sum()) - 196, 19, '19 rows with a relation type outside the frame')
eq(sorted(set(P.identical_relation_type) - {''}), ['C', 'F', 'L', 'U', 'X'], 'relation type values')
# Section 4.5
par = F[F.paronomastic_gloss == 'True']
eq((int((par.group == 'labelled').sum()), int((par.group == 'ordinary').sum())), (58, 11), 'paronomastic 58 / 11')
eq(F.groupby('group').filed_under_phonetic.apply(lambda s: int((s == 'True').sum())).to_dict(), {'labelled': 40, 'ordinary': 0}, 'filed under phonetic 40 / 0')
xin = P[P.is_xinfu == 'True']
eq((len(xin), int((xin.group == 'labelled').sum())), (48, 11), 'is_xinfu 48 rows, 11 labelled')
eq(set(P.duan_label), {'', '亦聲', '缺段注', '無'}, 'duan_label values')
eq(R['round'].value_counts().to_dict(), {'round2': 100, 'round1': 70, 'round3_scan': 57}, 'rounds 70 / 100 / 57')
eq(int(((R['round'] == 'round3_scan') & (R.in_analysis_set == 'True')).sum()), 56, 'round 3: 56 in the analysis set')
unk = R[(R.in_analysis_set == 'True') & (R.layer == 'unknown')]
print('unknown reasons:', unk.unknown_reason_en.value_counts().to_dict())
# Section 6
eq(D.check_status.value_counts().to_dict(), {'match': 73, 'visually_checked': 30, 'variant': 1}, 'register 73 / 30 / 1')
eq(sorted(set(D.scan_file)), [f'ho04_00029_{i:04d}.pdf' for i in (1, 2, 3, 4, 7)], 'register uses scan files 0001-0004 and 0007')
v = D[D.check_status == 'variant'].iloc[0]
eq(v.headword_codepoint, 'U+4888', 'variant is U+4888')
ok('日月合宿爲辰' in v.remark and '日月合宿从辰' in v.remark, 'variant wording')
# Section 5 agreement statistics are in the text reports of ESM_6
txt = {k: '\n'.join(v['text']) for k, v in x6.items() if k.startswith('report_')}
for needle in ['0.773', '0.817', '0.681', '0.824', '0.875', '0.918']:
    ok(any(needle in t for k, t in txt.items() if k in ('report_kappa', 'report_first_sample')), f'report text has {needle}')
for needle in ['0.735', '0.603', '0.842', '0.798', '0.666', '0.905']:
    ok(needle in txt['report_author_check'], f'author check report has {needle}')
ok('88.8%' in txt['report_kappa'] or '88.8' in txt['report_kappa'], 'pass agreement 88.8% in the kappa report')
ok('86' in txt['report_first_sample'], 'first sample agreement 86 in the report')
# Section 7: number of analysis scripts in run_all.py
z7 = zipfile.ZipFile(STAGE / 'ESM_7.zip')
ra = z7.read('analysis_code/scripts/run_all.py').decode('utf-8')
scripts = re.findall(r"\('([a-z_0-9]+\.py)'", ra)
print('scripts in run_all:', len(scripts), scripts)
print(f'{n_ok} checks passed')
