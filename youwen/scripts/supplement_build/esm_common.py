"""Shared helpers for building the supplementary files (internal; not shipped)."""
import csv, re, datetime
from pathlib import Path
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

ESM = Path('/tmp/claude-0/-home-user-Morphology/7d9f6fd5-d830-551f-9a43-e3ebcc390a52/scratchpad/esm')
KIT = ESM / 'kit'
STAGE = ESM / 'stage'
STAGE.mkdir(exist_ok=True)

TITLE = "What does 'also phonetic' mark? The Shuōwén's yìshēng label, homophony and derivation in Old Chinese"
JOURNAL = 'Morphology'
WITHHELD = 'Withheld for double-anonymous review'
FIXED_DATE = datetime.datetime(2026, 10, 1, 0, 0, 0)   # neutral, fixed timestamp for file properties

CAPTIONS = {
    1: ('ESM_1.pdf', 'Guide to the electronic supplementary material: a description of every file, the data dictionaries, the coding instructions, a statement of who coded what, and instructions for reproducing the results.'),
    2: ('ESM_2.xlsx', 'Pair-level dataset: the 1,333 extracted pairs of a Shuōwén compound and its phonetic, of which 212 labelled and 953 ordinary pairs form the analysis set, with Middle and Old Chinese readings, sound-relation categories, gloss and recension flags and the relation types of homophonous pairs; the Dà Xú–Xiǎo Xú collation of the 227 labelled entries; and the register of the 104 entries checked against the print edition.'),
    3: ('ESM_3.xlsx', "Semantic codings: the first blind sample (100 pairs, the blind and the non-blind pass); the enlarged blind coding (767 pairs: the 677 new items, coded in two independent blind passes by separate Claude instances with confidence and notes, and the 90 first-sample items in the sampling frame); the authors' consolidated check of 126 pairs; and the second answers returned in two batches."),
    4: ('ESM_4.pdf', 'Analysis plan for the enlarged coding, committed with a time-stamp before any batch was coded (English translation, with the log of later changes).'),
    5: ('ESM_5.zip', "Materials of the enlarged coding: the 14 prompts (7 batches, 2 passes), the raw answers returned by the Claude instances, the two second answers that were not used, the blank sheet for the authors' check and the log of when each answer was collected."),
    6: ('ESM_6.xlsx', "Result tables: all model outputs and counts behind Tables 2 and 4–11 and Fig. 1 (main models, sensitivity analyses, tests on the enlarged coding, replacement by the authors' judgment, replacement by the second answers, sensitivity to coding bias, agreement statistics)."),
    7: ('ESM_7.zip', 'Analysis code: Python scripts that regenerate the result tables from the data tables, the input tables as CSV files, the expected outputs and a self-check script.'),
}

LICENCE = ("The authors' own contributions in this file (codings, annotations, tables, documentation) are released under the Creative Commons Attribution 4.0 "
           "International licence (CC BY 4.0); the analysis code (Online Resource 7) is released under the MIT licence. Columns derived from third-party resources keep "
           "the terms of their sources: the text of the Shuōwén and Duan Yucai's commentary (shuowenjiezi project, Apache-2.0), Middle Chinese positions "
           "(Qieyun data of the nk2028 project, CC0; tshet-uinh software, MIT) and the Old Chinese reconstruction of Baxter and Sagart (2014) as compiled in the cddb "
           "database (GPL-3.0). See Online Resource 1, Section 8.")

NUM_INT = re.compile(r'^-?(0|[1-9]\d*)$')
NUM_FLOAT = re.compile(r'^-?(0|[1-9]\d*)\.\d+$')
NUM_SCI = re.compile(r'^-?\d+(\.\d+)?[eE][-+]?\d+$')


def cp(s):
    """Unicode code points of a string, U+XXXX separated by spaces."""
    return ' '.join('U+%04X' % ord(c) for c in s)


def read_csv(path, **kw):
    """Read a CSV as strings, keeping empty cells as '' and the literal 'NA' as 'NA'."""
    return pd.read_csv(path, encoding='utf-8-sig', dtype=str, keep_default_na=False, **kw)


def convert(v):
    """Return (value, number_format) for a cell: integers and decimals become numbers (decimals keep their printed number of digits); the rest stays text."""
    if isinstance(v, (int, float)):
        return v, None
    if v is None:
        return None, None
    if v == '':
        return None, None
    if NUM_INT.match(v):
        return int(v), None
    if NUM_FLOAT.match(v):
        return float(v), '0.' + '0' * len(v.split('.')[1])
    if NUM_SCI.match(v):
        m = re.match(r'^-?\d+(?:\.(\d+))?[eE]', v)
        dec = len(m.group(1)) if m.group(1) else 0
        return float(v), ('0.' + '0' * dec if dec else '0') + 'E+00'
    assert not v.startswith('='), v
    return v, None


HEADER_FILL = PatternFill('solid', fgColor='D9E2F3')
ABOUT_FILL = PatternFill('solid', fgColor='F2F2F2')


def add_table_sheet(wb, name, df, widths=None, number_cols=True, text_cols=()):
    ws = wb.create_sheet(name)
    ws.append(list(df.columns))
    for c in ws[1]:
        c.font = Font(bold=True); c.fill = HEADER_FILL; c.alignment = Alignment(vertical='top')
    for row in df.itertuples(index=False):
        out = []
        for col, v in zip(df.columns, row):
            if number_cols and col not in text_cols:
                val, fmt = convert(v)
            else:
                val, fmt = (None if v == '' else v), None
            out.append((val, fmt))
        ws.append([o[0] for o in out])
        r = ws.max_row
        for i, (val, fmt) in enumerate(out, 1):
            if fmt:
                ws.cell(r, i).number_format = fmt
    ws.freeze_panes = 'A2'
    ws.auto_filter.ref = f'A1:{get_column_letter(len(df.columns))}{len(df) + 1}'
    for i, col in enumerate(df.columns, 1):
        w = max([len(str(col))] + [len(str(x)) for x in df[col].head(300)]) + 2
        ws.column_dimensions[get_column_letter(i)].width = min(max(w, 8), 60)
    return ws


def add_text_sheet(wb, name, lines, header=('line_no', 'text')):
    ws = wb.create_sheet(name)
    ws.append(list(header))
    for c in ws[1]:
        c.font = Font(bold=True); c.fill = HEADER_FILL
    for i, l in enumerate(lines, 1):
        ws.append([i, l])
    ws.freeze_panes = 'A2'
    ws.column_dimensions['A'].width = 8
    ws.column_dimensions['B'].width = 150
    return ws


def add_about(wb, esm_no, intro_rows, sheet_rows, notes):
    """First sheet: identification block required by the publisher, the sheet list and the conventions.
    intro_rows: extra (label, value) rows after the identification block; sheet_rows: list of (sheet, rows, content, use); notes: list of strings."""
    fn, cap = CAPTIONS[esm_no]
    ws = wb.active; ws.title = 'About'
    rows = [('Online Resource', f'{esm_no} ({fn})'), ('Article title', TITLE), ('Journal', JOURNAL), ('Authors', WITHHELD), ('Corresponding author (affiliation, e-mail)', WITHHELD),
            ('Caption', cap)] + list(intro_rows)
    for lab, val in rows:
        ws.append([lab, val])
    for r in ws.iter_rows(min_row=1, max_row=ws.max_row):
        r[0].font = Font(bold=True); r[0].fill = ABOUT_FILL
        r[0].alignment = Alignment(vertical='top', wrap_text=True); r[1].alignment = Alignment(vertical='top', wrap_text=True)
    ws.append([])
    ws.append(['Sheets', None]); ws.cell(ws.max_row, 1).font = Font(bold=True)
    ws.append(['Sheet name', 'Content (rows × columns; where the paper uses it)'])
    for c in ws[ws.max_row]:
        c.font = Font(bold=True); c.fill = HEADER_FILL
    for sh, nrow, ncol, content in sheet_rows:
        ws.append([sh, f'{content} [{nrow} rows × {ncol} columns]' if nrow is not None else content])
        ws.cell(ws.max_row, 2).alignment = Alignment(wrap_text=True, vertical='top'); ws.cell(ws.max_row, 1).alignment = Alignment(vertical='top')
    ws.append([])
    ws.append(['Conventions', None]); ws.cell(ws.max_row, 1).font = Font(bold=True)
    for n in notes:
        ws.append([None, n]); ws.cell(ws.max_row, 2).alignment = Alignment(wrap_text=True, vertical='top')
    ws.append([])
    ws.append(['Licence', LICENCE]); ws.cell(ws.max_row, 1).font = Font(bold=True); ws.cell(ws.max_row, 1).alignment = Alignment(vertical='top')
    ws.cell(ws.max_row, 2).alignment = Alignment(wrap_text=True, vertical='top')
    ws.column_dimensions['A'].width = 34
    ws.column_dimensions['B'].width = 130
    return ws


def new_workbook(title_prop):
    wb = Workbook()
    p = wb.properties
    p.creator = ''; p.lastModifiedBy = ''; p.title = title_prop; p.subject = ''; p.description = ''; p.keywords = ''; p.category = ''
    p.created = FIXED_DATE; p.modified = FIXED_DATE
    return wb


COMMON_NOTES = [
    'Text encoding is Unicode (UTF-8 in the CSV files of Online Resource 7). Column headers are in English. Chinese appears only as data (characters, Shuōwén glosses, quotations, labels); for every character column there is a companion column of Unicode code points, written U+XXXX.',
    'NA means not available (for example, no reading at one end of a pair); an empty cell means not applicable or not recorded. True and False are written as text.',
    'Each sheet holds one table. The sheet "data_dictionary" describes every column of every data sheet in this file.',
    'The key sw_id (the row number of a head entry in the open Shuōwén data) links the pair table, the collation, the spot-check register and the codings across files.',
]
