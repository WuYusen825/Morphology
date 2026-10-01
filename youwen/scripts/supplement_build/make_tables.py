# Internal build step (not shipped): turn the project's working files into the released data tables.
# Reads from the repository checkout (my branch) and writes to esm/kit/data/.
import os, csv, shutil, re
import pandas as pd, openpyxl

REPO = '/home/user/Morphology/youwen'
KIT = '/tmp/claude-0/-home-user-Morphology/7d9f6fd5-d830-551f-9a43-e3ebcc390a52/scratchpad/esm/kit'
DATA = os.path.join(KIT, 'data')
os.makedirs(DATA, exist_ok=True)

def cp(s):
    return ' '.join(f'U+{ord(c):04X}' for c in s)

def write_csv(df, name):
    df.to_csv(os.path.join(DATA, name), index=False, encoding='utf-8-sig', lineterminator='\n')

# ---- 1. pairs.csv --------------------------------------------------------------------------
d = pd.read_csv(os.path.join(REPO, 'yisheng_dataset.csv'), encoding='utf-8-sig', dtype=str, keep_default_na=False)
assert d.shape == (1333, 38)
GROUP = {'亦聲': 'labelled', '聲': 'ordinary', '省聲': 'abbreviated_phonetic', '會意/其他': 'source_other'}
d['group'] = d.relation.map(GROUP)
assert d.group.notna().all()
d['char_codepoint'] = d.char.map(cp)
d['phonetic_codepoint'] = d.phonetic.map(cp)
A = d[d.in_analysis_set == 'True']
yph = set(A[A.relation == '亦聲'].phonetic)
d['in_comparison_frame'] = [str(a == 'True' and p in yph) for a, p in zip(d.in_analysis_set, d.phonetic)]
assert (d.in_comparison_frame == 'True').sum() == 212 + 953
first = ['sw_id', 'char', 'char_codepoint', 'phonetic', 'phonetic_codepoint', 'group', 'relation', 'label_source',
         'in_analysis_set', 'in_comparison_frame', 'is_xinfu']
rest = [c for c in d.columns if c not in first and c != 'src']
pairs = d[first + rest]
write_csv(pairs, 'pairs.csv')
print('pairs', pairs.shape)

# ---- 2. recension_collation.csv ------------------------------------------------------------
c = pd.read_csv(os.path.join(REPO, 'yisheng_xiaoxu_collation_final.csv'), encoding='utf-8-sig', dtype=str, keep_default_na=False)
READING_EN = {'亦聲': 'labelled yisheng', '聲': 'plain phonetic compound (shēng)', '無聲': 'no phonetic labelled (no shēng element)',
              '其他聲': 'a different phonetic', '未找到': 'entry not found', '原书空白不清': 'blank or illegible in the print', '未見': 'not seen'}
REASON_EN = {'': '', '新附': 'xinfu: added by Xu Xuan, not in the Xiǎo Xú',
             '卷二十五据大徐补': 'juan 25: lost from the Xiǎo Xú and supplied from the Dà Xú',
             '疑据大徐补入': 'probably supplied from the Dà Xú',
             '原书空白': 'blank in the print', '扫描本未见': 'not seen in the scan'}
assert set(c.xiaoxu_reading) <= set(READING_EN) and set(c.unknown_reason) <= set(REASON_EN)
c['char_codepoint'] = c.char.map(cp); c['phonetic_codepoint'] = c.phonetic.map(cp)
c['xiaoxu_reading_en'] = c.xiaoxu_reading.map(READING_EN); c['unknown_reason_en'] = c.unknown_reason.map(REASON_EN)
c.to_pickle(os.path.join(KIT, '..', 'work', 'collation_stage.pkl'))
print('collation', c.shape)

# ---- 3. first_sample_codes.csv -------------------------------------------------------------
ws = openpyxl.load_workbook(os.path.join(REPO, 'blind_coding_sheet_llm_coded.xlsx'))['编码']
s = pd.DataFrame(list(ws.iter_rows(min_row=2, values_only=True)),
                 columns=['item', 'phonetic', 'phonetic_gloss', 'member', 'member_gloss', 'blind_code', 'blind_confidence', 'blind_note'])
cc = pd.read_csv(os.path.join(REPO, 'yisheng_claude_codes.csv'), encoding='utf-8-sig', dtype=str, keep_default_na=False)
s['item'] = s['item'].astype(str)
assert (s.item.values == cc.item.values).all() and (s.member.values == cc.char.values).all() and (s.phonetic.values == cc.series.values).all()
s['blind_confidence'] = s['blind_confidence'].astype(str)
s['blind_note'] = s['blind_note'].fillna('')
s['phonetic_gloss'] = s['phonetic_gloss'].fillna(''); s['member_gloss'] = s['member_gloss'].fillna('')
s['relation'] = cc.relation.values
s['group'] = s.relation.map(GROUP)
s['oc_relation_auto'] = cc.morph_relation_auto.values
s['nonblind_code'] = cc.code_core.values
s['phonetic_codepoint'] = s.phonetic.map(cp); s['member_codepoint'] = s.member.map(cp)
# link each first-sample item to its row in pairs.csv (same merge and de-duplication rule as the original checking scripts)
dd = d[['phonetic', 'char', 'relation', 'in_analysis_set', 'sw_id']].rename(columns={'relation': 'relation_in_pairs', 'in_analysis_set': 'in_analysis_set_pairs', 'sw_id': 'sw_id_pairs'})
mm = s.merge(dd, left_on=['phonetic', 'member'], right_on=['phonetic', 'char'], how='left')
mm = mm[(mm.relation_in_pairs == mm.relation) | mm.relation_in_pairs.isna() | ~mm.item.duplicated(keep=False)]
assert len(mm) == 100 and mm.item.is_unique and (mm.item.values == s.item.values).all()
s['sw_id'] = mm.sw_id_pairs.fillna('').values
s['in_analysis_set'] = mm.in_analysis_set_pairs.fillna('').values
s['relation_in_pairs'] = mm.relation_in_pairs.fillna('').values
assert (s.in_analysis_set == 'True').sum() == 94 and (s.sw_id == '').sum() == 1
s = s[['item', 'sw_id', 'phonetic', 'phonetic_codepoint', 'member', 'member_codepoint', 'group', 'relation', 'relation_in_pairs', 'in_analysis_set',
       'phonetic_gloss', 'member_gloss', 'blind_code', 'blind_confidence', 'blind_note', 'nonblind_code', 'oc_relation_auto']]
write_csv(s, 'first_sample_codes.csv')
print('first_sample', s.shape, s.blind_code.value_counts().to_dict())

# ---- 4. author_check.csv -------------------------------------------------------------------
wb = openpyxl.load_workbook(os.path.join(REPO, 'ext_coding', 'ext_check_sheet_author_filled.xlsx'))
rows = list(wb['核验'].iter_rows(min_row=2, values_only=True))
a = pd.DataFrame(rows, columns=['check_id', 'check_type', 'phonetic', 'phonetic_gloss', 'member', 'member_gloss', 'author_code', 'pass1_code', 'pass2_code', 'author_note'])
assert a.author_note.isna().all() and len(a) == 126
TYPE = {'两次不一致': 'passes_disagree', '随机抽查': 'random_agreed'}
a['check_type'] = a.check_type.map(TYPE); assert a.check_type.notna().all()
a['check_id'] = a.check_id.astype(int).astype(str)
a['phonetic_codepoint'] = a.phonetic.map(cp); a['member_codepoint'] = a.member.map(cp)
a = a[['check_id', 'check_type', 'phonetic', 'phonetic_codepoint', 'phonetic_gloss', 'member', 'member_codepoint', 'member_gloss', 'author_code', 'pass1_code', 'pass2_code']]
write_csv(a, 'author_check.csv')
print('author_check', a.shape, a.author_code.value_counts().to_dict())

# ---- 5. ext_items_key.csv and raw answers --------------------------------------------------
shutil.copy(os.path.join(REPO, 'ext_coding', 'ext_items_key.csv'), os.path.join(DATA, 'ext_items_key.csv'))
os.makedirs(os.path.join(DATA, 'raw'), exist_ok=True)
for f in sorted(os.listdir(os.path.join(REPO, 'ext_coding', 'raw'))):
    if f.endswith('.txt'):
        shutil.copy(os.path.join(REPO, 'ext_coding', 'raw', f), os.path.join(DATA, 'raw', f))
print('raw files', len(os.listdir(os.path.join(DATA, 'raw'))))

# ---- 2b. recension_collation.csv: English rendering of the collator's Chinese-only notes ------
XINFU_NOTE = 'A xīnfù character of the Dà Xú; absent in the Xiǎo Xú.'
J25 = 'Juan 25, supplied from the Dà Xú.'
NOTE_EN = {
    13: ('𠔁', 'Same as the Dà Xú; 八 is not repeated before 亦聲.'),
    20: ('喪', 'The text reads 云 (collation note: 云 is probably a corruption of 亾); no 亦 character.'),
    21: ('迹', '亦 is itself the phonetic; same wording as the Dà Xú.'),
    26: ('齨', 'Reads □聲, no 亦; the □ should be 臼.'),
    28: ('𤘌', '竒 is a variant of 奇.'),
    29: ('𤴙', 'No 疋亦聲 here; the next entry, 𤕟, has 疋亦聲.'),
    30: ('𤕟', 'Reads 从爻疋, without 从疋; the text continues into juan 5.'),
    37: ('詔', 'The fanqie is written 之紹切 (the Xiǎo Xú normally writes 反); probably supplied from the Dà Xú.'),
    41: ('謎', XINFU_NOTE),
    47: ('䢅', 'Same as the Dà Xú; 辰 is not repeated before 亦聲.'),
    57: ('𢿳', 'The □ is probably 𤔔; no 亦.'),
    58: ('鼓', 'The commentary (臣鍇) also says 故云亦聲 ("hence called yìshēng"); it takes the analysis as meaning-combining (會意).'),
    76: ('腔', 'The passage with 脧 and 腔 is not seen.'),
    86: ('可', 'The character 丂 is missing; the text reads 从口亦聲.'),
    89: ('愷', 'The 心 section of juan 20 has another entry, 康也 从心豈聲.'),
    102: ('糶', 'The fanqie in the scan is 他弔切 (the Xiǎo Xú normally writes 反); probably supplied from the Dà Xú.'),
    106: ('晬', XINFU_NOTE),
    109: ('𣐺', 'The □ stands for 𢎘; 聱 should read 聲.'),
    125: ('儈', 'This passage is not seen in the 人 section.'),
    126: ('低', 'A xīnfù character of the Dà Xú; the entry 儈 (債也) cannot be found.'),
    128: ('價', XINFU_NOTE),
    129: ('僦', 'This passage is not seen in the 人 section.'),
    130: ('化', '𠤎 is printed as 匕.'),
    132: ('衵', 'Misjudged in the first round: the Xiǎo Xú reads 从衣从日亦日聲, i.e. yìshēng, only in a different word order.'),
    136: ('𣣸', 'The character 𠧴 is missing (not shown as □); only 亦聲 remains.'),
    144: ('魑', 'A xīnfù character of the Dà Xú; the 鬼 section ends at 魋.'),
    152: ('赩', 'The 赤 section (eight characters) ends at 赫; there is no 赩.'),
    156: ('𥉁', 'Missing after the headword; no 亦聲.'),
    163: ('懬', 'Lacks 一曰寬也.'),
    171: ('泬', '宂 is probably 穴; no 聲 character.'),
    178: ('涯', XINFU_NOTE),
    187: ('婚', 'Reads 从女昏, with no 聲 character.'),
    196: ('緉', J25), 197: ('螟', J25), 198: ('蟘', J25), 200: ('䬍', J25), 201: ('鼀', J25),
    204: ('墨', 'Commentary (鍇): meaning-combining (會意).'),
    211: ('鈴', '今 is probably a corruption of 令; fanqie 連丁反; no 亦.'),
    216: ('陸', 'The □ stands for 𨸏.'),
    218: ('𨻺', 'The □ should be 𨸏.'),
    219: ('阢', '几 is probably a corruption of 兀; no 亦.'),
    220: ('隙', 'Reads □聲, no 亦; the □ should be 𡭴.'),
}
c = pd.read_pickle(os.path.join(KIT, '..', 'work', 'collation_stage.pkl'))
note_en = []
for i, r in c.iterrows():
    if i in NOTE_EN:
        assert r.char == NOTE_EN[i][0], (i, r.char)
        note_en.append(NOTE_EN[i][1])
    else:
        n = r.note.replace('[扫描 ', '[scan ')
        note_en.append(n)
c['note_en'] = note_en
# every note that is not translated must already be English (three or more Latin letters in a row) or empty
left = c[(c.note != '') & ~c.index.isin(NOTE_EN) & ~c.note.str.contains(r'[A-Za-z]{3,}')]
print('untranslated Chinese-only notes:', left[['char', 'note']].values.tolist())
c = c[['sw_id', 'char', 'char_codepoint', 'phonetic', 'phonetic_codepoint', 'in_analysis_set', 'daxu_gloss', 'xiaoxu_reading', 'xiaoxu_reading_en',
       'layer', 'unknown_reason', 'unknown_reason_en', 'round', 'xiaoxu_juan', 'xiaoxu_quote', 'note', 'note_en']]
write_csv(c, 'recension_collation.csv')
print('collation written', c.shape)
