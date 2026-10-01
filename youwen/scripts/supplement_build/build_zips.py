"""Build ESM_5.zip and ESM_7.zip (internal; not shipped)."""
import sys, zipfile, io, hashlib
sys.path.insert(0, '/tmp/claude-0/-home-user-Morphology/7d9f6fd5-d830-551f-9a43-e3ebcc390a52/scratchpad/esm/work')
from esm_common import *
from openpyxl import load_workbook

ZIP_DATE = (2026, 10, 1, 0, 0, 0)
SRC_EXT = Path('/home/user/Morphology/youwen/ext_coding')


def add(z, arcname, data):
    zi = zipfile.ZipInfo(arcname, date_time=ZIP_DATE)
    zi.compress_type = zipfile.ZIP_DEFLATED
    zi.external_attr = 0o644 << 16
    zi.create_system = 3
    z.writestr(zi, data)


# ------------------------------------------------------------------------------------------------ ESM_5
CHECK_INSTR = [
    ("Authors' check sheet (enlarged blind coding, 30 September 2026)", '作者核验表（扩大盲编，2026-09-30）'),
    ('126 items in all: all 76 items on which the two independent blind passes disagree, plus 50 items drawn at random from those on which they agree (random seed 20260934); the order has been shuffled. The sheet does not show whether an item is marked yìshēng.',
     '共 126 条：两次独立 LLM 盲编不一致的全部 76 条，加上两次一致的条目中随机抽的 50 条（随机种子 20260934），顺序已打乱。表中不显示是否亦声。'),
    ('Procedure: please first look only at columns C-F (the phonetic, the compound and the Shuōwén glosses of both), enter your judgment (Y/E/N/X) in column G, and only then look at columns H and I (the two blind passes); if you disagree, write one sentence of reason in column J.',
     '做法：请先只看 C–F 列（声符字、成员字和两者的《说文》释义），在 G 列填您的判断（Y/E/N/X），再看 H、I 两列的两次盲编；如有不同意见，在 J 列写一句理由。'),
    ('Y = same or near-synonymous meaning (e.g. 厓 “山邊也” / 涯 “水邊也”); E = connected only through one step of extension or inference (e.g. 亡 “逃也” / 忘 “不識也”); N = no semantic relation visible; X = the compound is a proper name (place, river, surname, named plant or animal, etc.).',
     'Y = 相同或近义（如 厓“山邊也” / 涯“水邊也”）；E = 经一步引申或推理才能连上（如 亡“逃也” / 忘“不識也”）；N = 看不出语义关系；X = 成员字是专名（地名、水名、姓氏、动植物名等）。'),
    ('Judge by the original meaning only, not by later or loan meanings; when unsure between Y and E choose E, between E and N choose N. Please do not look up whether the character is marked yìshēng in the original work.',
     '只看本义，不看后起义和假借义；拿不准时，Y 与 E 之间取 E，E 与 N 之间取 N。请不要去查这个字在原书中是不是亦声。'),
    ('This is a check, not the primary coding: the analysis uses the first blind pass; your judgments will be reported separately as agreement with the blind coding, and items you changed will be analysed in a separate sensitivity analysis.',
     '这是核验，不是主编码：分析用第一次盲编；您的判断会单独报告与盲编的一致率，改动了的条目另做一次敏感性分析。'),
]
CHECK_COLS = [('A', 'check_id', 'item number', '核验编号'), ('B', 'check_type', 'passes_disagree (the two blind passes differ) or random_agreed (drawn at random from the items on which they agree)', '类型'),
              ('C', 'phonetic', 'the phonetic', '声符字'), ('D', 'phonetic_gloss', 'Shuōwén gloss of the phonetic, structural analysis removed', '声符字释义'),
              ('E', 'member', 'the compound', '成员字'), ('F', 'member_gloss', 'Shuōwén gloss of the compound, structural analysis removed', '成员字释义'),
              ('G', 'author_code', 'the authors enter their judgment here (Y/E/N/X) before looking at H and I', '作者判断(Y/E/N/X)'),
              ('H', 'pass1_code', 'code of blind pass 1', '第一次盲编'), ('I', 'pass2_code', 'code of blind pass 2', '第二次盲编'), ('J', 'author_note', 'free-text note', '作者备注')]


def build_check_sheet():
    from openpyxl.styles import Font, PatternFill, Alignment
    blank = read_csv(KIT / 'output/ext_check_sheet_blank.csv')
    # equality with the sheet that was sent
    orig = load_workbook(SRC_EXT / 'ext_check_sheet.xlsx')
    rows = list(orig['核验'].iter_rows(values_only=True))
    assert [str(x) for x in rows[0]] == [c[3] for c in CHECK_COLS]
    assert len(rows) - 1 == len(blank) == 126
    TYPEMAP = {'两次不一致': 'passes_disagree', '随机抽查': 'random_agreed'}
    for r, (_, b) in zip(rows[1:], blank.iterrows()):
        got = [('' if x is None else str(x)) for x in r]
        got[1] = TYPEMAP[got[1]]
        assert got == list(b), (got, list(b))
    wb = new_workbook('Authors check sheet (blank), English rendering')
    ws = wb.active; ws.title = 'Instructions'
    ws.append(['line', 'English rendering', 'Original text (Chinese, as shown to the authors)'])
    for c in ws[1]: c.font = Font(bold=True); c.fill = HEADER_FILL
    for i, (en, zh) in enumerate(CHECK_INSTR, 1):
        ws.append([i, en, zh])
    ws.append([])
    ws.append([None, 'Columns of the sheet "Check" (the original sheet had Chinese headers, given in the third column)', None]); ws.cell(ws.max_row, 2).font = Font(bold=True)
    for letter, name, desc, zh in CHECK_COLS:
        ws.append([letter, f'{name}: {desc}', zh])
    for r in ws.iter_rows(min_row=2):
        for c in r: c.alignment = Alignment(wrap_text=True, vertical='top')
    ws.column_dimensions['A'].width = 6; ws.column_dimensions['B'].width = 110; ws.column_dimensions['C'].width = 70
    add_table_sheet(wb, 'Check', blank, text_cols=tuple(blank.columns))
    # the check sheet is a form: keep every cell as text, as in the sheet that was sent
    buf = io.BytesIO(); wb.save(buf)
    return buf.getvalue()


def build_esm5():
    top = 'enlarged_coding_materials/'
    readme = f"""MATERIALS OF THE ENLARGED CODING
Online Resource 5 (ESM_5.zip)

Article title:  {TITLE}
Journal:        {JOURNAL}
Authors:        {WITHHELD}
Corresponding author (affiliation, e-mail): {WITHHELD}

Caption: {CAPTIONS[5][1]}

CONTENTS

  prompts/pass{{1,2}}_b{{01..07}}.txt
      The complete prompt given to each of the 14 coders (Claude instances; 2 passes x 7 batches), exactly as sent. Each prompt holds the coding
      instructions and about 100 items; an item line reads: item number, phonetic, its gloss, compound, its gloss (tab-separated; the
      Shuowen structural analysis, such as 從某 or 某聲, is removed from the glosses). The group (yisheng or ordinary) is never shown.
  raw_answers/pass{{1,2}}_b{{01..07}}.txt
      The answer of each instance, saved unchanged. A line reads: item number, code, confidence, note (tab-separated). In pass 2,
      batch 5 the instance wrote explanatory text before and after the coding lines; it is kept as returned (only the coding lines are read).
  raw_answers/pass1_b03_second_answer_not_used.txt, raw_answers/pass1_b06_second_answer_not_used.txt
      In two batches of pass 1 the environment returned a second answer. A rule fixed before any analysis was run says that the first
      complete, acceptable answer of an instance counts; the second answers enter no main analysis and are used only in the sensitivity
      analysis X5 (Table 8 note; Online Resource 4, Section 7, and Online Resource 6).
  item_key.csv
      The key that links every prompt line to a pair: sw_id (the key of Online Resource 2), phonetic, compound, relation (亦聲 = labelled,
      聲 = ordinary), role (new = coded for the first time; anchor = first-sample item added to a batch as a calibration check: 5 per batch, 35 in all, each coded once in each pass),
      sampling stratum, whether Middle and Old Chinese forms exist, the batch and item position of the pair in pass 1 and pass 2,
      and the glosses shown. The group was never shown to the coders. Column definitions: data_dictionary.csv in Online Resource 7.
  author_check_sheet_blank.xlsx
      The sheet on which the authors checked 126 items, blank, as sent (English rendering of the instructions and headers; the original
      was in Chinese and is given beside the English). The sheet showed the type of each item (the passes disagree / drawn at random from
      those that agree) and the codes of the two passes (columns H and I); the instructions asked the authors to enter their own judgment
      before looking at the codes. The consolidated filled sheet is the sheet "author_check" of Online Resource 3.
  collection_log.csv
      When each answer was collected (UTC), whether the prompt that was sent was identical to the file in prompts/, the tool calls the
      instance reported (the only one is the hand-back of its answer; the first answer of pass 1, batch 3 came as plain text, with none),
      and the number of parsable lines against the number of items expected.

HOW THE FILES FIT TOGETHER

Reading a prompt and its answer: line i of prompts/passP_bBB.txt (after the instructions) and line i of raw_answers/passP_bBB.txt carry the
same item number; item_key.csv gives the pair behind it (columns pP_batch and pP_item). Online Resource 3 (sheet "enlarged_coding") lists
the codes, confidence and notes of both passes next to the pair; Online Resource 7 (scripts/ext_analysis.py) parses these raw answers and
runs the analyses. The prompts can be regenerated from the sampling script and are compared by hash in the self-check.

LICENCE

CC BY 4.0 for the authors' contributions (prompts, answers, key, log). The glosses in the key and the prompts are Shuowen text from the
shuowenjiezi project (Apache License 2.0, https://github.com/shuowenjiezi/shuowen).
"""
    out = STAGE / 'ESM_5.zip'
    with zipfile.ZipFile(out, 'w') as z:
        add(z, top + 'README.txt', readme.encode('utf-8'))
        for p in sorted((KIT / 'output/prompts').glob('pass*_b*.txt')):
            add(z, top + 'prompts/' + p.name, p.read_bytes())
        raws = sorted((KIT / 'data/raw').glob('pass*_b*.txt'))
        assert len(raws) == 16
        for p in raws:
            assert p.read_bytes() == (SRC_EXT / 'raw' / p.name).read_bytes(), p.name
            add(z, top + 'raw_answers/' + p.name, p.read_bytes())
        add(z, top + 'item_key.csv', (KIT / 'data/ext_items_key.csv').read_bytes())
        add(z, top + 'author_check_sheet_blank.xlsx', build_check_sheet())
        log = read_csv(SRC_EXT / 'raw/provenance.tsv', sep='\t')
        assert len(log) == 14 and list(log.columns) == ['pass', 'batch', 'collected_utc', 'prompt_identical_to_file', 'tool_uses_reported', 'parsable_lines', 'expected_lines']
        buf = io.StringIO(); log.to_csv(buf, index=False, lineterminator='\n')
        add(z, top + 'collection_log.csv', ('﻿' + buf.getvalue()).encode('utf-8'))
    print('saved', out, out.stat().st_size, 'bytes;', len(zipfile.ZipFile(out).namelist()), 'files')


# ------------------------------------------------------------------------------------------------ ESM_7
def build_esm7():
    top = 'analysis_code/'
    out = STAGE / 'ESM_7.zip'
    files = []
    for p in sorted(KIT.rglob('*')):
        if not p.is_file() or '__pycache__' in p.parts: continue
        rel = p.relative_to(KIT).as_posix()
        if rel.startswith('output/'): continue          # written by the scripts on the first run
        files.append((rel, p))
    with zipfile.ZipFile(out, 'w') as z:
        for rel, p in files:
            add(z, top + rel, p.read_bytes())
    print('saved', out, out.stat().st_size, 'bytes;', len(files), 'files')


if __name__ == '__main__':
    build_esm5(); build_esm7()
