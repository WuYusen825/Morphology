# Build sources of the Online Resources (internal; not part of the submission)

These scripts produced the seven files in `../submission/supplement/` (`ESM_1.pdf` to `ESM_7.zip`) on 2026-10-01. They are kept so that a later change (a different licence, camera-ready files with the authors' names, a corrected number) can be rebuilt instead of patched by hand. Do not upload this folder: `package_check.py` lists personal-name patterns for the anonymity scan, so keep it out of any public or anonymised copy.

## What each file does

| File | Role |
|---|---|
| `make_tables.py` | Turns the project's working files (repository checkout, `youwen/` and `youwen/ext_coding/`) into the released CSV tables in `kit/data/` |
| `build_dictionary.py` | Writes the data dictionary `kit/data_dictionary.csv` (one row per column of every CSV in `data/` and `output/`) and `work/dictionary.json` |
| `build_workbooks.py` | Builds `ESM_2.xlsx`, `ESM_3.xlsx`, `ESM_6.xlsx` from the kit's CSV tables (blank file properties, `About` and `data_dictionary` sheets) |
| `build_zips.py` | Builds `ESM_5.zip` and `ESM_7.zip` (neutral timestamps, single top folder, LF endings) |
| `build_esm1.py`, `ESM_1_template.md`, `prompt_template.txt` | Builds `ESM_1.pdf` (the guide); the dictionaries inside it are read from the staged workbooks |
| `build_esm4.py`, `ESM_4_final.md` | Builds `ESM_4.pdf` (English translation of the analysis plan, with the log of later changes) |
| `esm_common.py`, `pdf_common.py` | Shared constants (title, journal, the seven captions, licence sentence) and the HTML-to-PDF step (headless Chromium, footer "Online Resource n · page X of Y") |
| `verify_esm1.py` | 84 assertions: every number in the guide against the staged files |
| `diff_stage.py` | Compares a rebuilt `stage/` with a copy of the delivered files (cells of the workbooks, members of the zips, text of the PDFs), to see that a rebuild changed only what was meant to change |
| `package_check.py` | Package-level check: file names, sizes, file properties, anonymity scan (names, e-mail, paths), captions against the manuscript's Supplementary Information section |

The captions in `esm_common.py` (`CAPTIONS`) are the manuscript's own sentences (`submission/source/yisheng_paper_v10_anonymised.md`, section Supplementary Information); change them in both places.

## To rebuild

1. Copy this folder to a working folder `esm/work/` and set the folder in `esm_common.py` (`ESM = ...`), in the `sys.path.insert(...)` lines at the top of the build scripts, and in `KIT = ...` of `make_tables.py` and `build_dictionary.py`. The scripts expect `esm/kit/` (the unzipped `ESM_7.zip`, top folder renamed from `analysis_code` to `kit`) and write to `esm/stage/`.
2. Needs Python 3 with pandas, openpyxl, markdown (python-markdown), pymupdf and Pillow; for the PDFs the Chromium of the cloud image (`CHROME` in `pdf_common.py`) and the font WenQuanYi Zen Hei (it has no glyphs outside the Basic Multilingual Plane, so such characters are written as code points).
3. Order used on 2026-10-01: `make_tables.py` (repository working files to `kit/data/`), then the kit's `scripts/run_all.py` (writes `kit/output/`, which `expected/` mirrors), `build_dictionary.py`, `build_workbooks.py`, `build_zips.py`, `build_esm1.py`, `build_esm4.py`; then `verify_esm1.py` and `package_check.py [folder]`. Copy the seven files from `stage/` to `submission/supplement/` and run `package_check.py` on that folder again.

This order was reconstructed from the scripts after the fact; the working folder was never rebuilt from nothing in one go, so expect to adjust paths. Check the result with the package check and with the kit's own self-check (`python scripts/run_all.py`, 249 checks).

## Lessons from the build

- Never put author-identifying patterns (names, affiliation, student number) into a file that ships, not even assembled from pieces; scan for them in an internal checker (`package_check.py`).
- `csv.DictWriter` writes CRLF by default: pass `lineterminator='\n'`.
- A comment in the first two lines of a `.py` file that contains `coding:` or `coding=` (for example "# Blind coding: sampling") is read by Python as an encoding declaration and the script fails with an unknown-encoding error (PEP 263): word those header comments differently.
- openpyxl turns strings that start with `=` into formulas and reads `0.0` back as `0`; pandas reads the literal text `None` as missing: keep `NA` and `None` as text and read with the same settings the scripts use.
- Adding a column to a table can silently break a merge: merge on `sw_id`.
- A self-check is only believed after a mutation test: plant a wrong number or a name and see it fail.
- Numbers quoted in prose (for example "10 pairs with the gloss None") must come from the data, not from memory; `verify_esm1.py` does that for the guide.
- Statsmodels variational-Bayes columns (`glmm_vb_*`) can differ in the last digit between runs and library versions; the self-check allows for that.
- A statement about structure ("anchors repeated in every batch") is a claim about the data like a number: check it against the item key (the 35 anchors were 5 per batch, each coded once in each pass). Describe only what the files record; do not describe how differences between the authors were settled.
- The order of events on the authors' 126-item check (what the sheet showed; what the instructions asked) was told in one place as "the codes were shown after the authors had entered their judgment", which made the check look more independent than the other files and the paper say. Copy one source sentence into every file that tells it (the sheet showed the type and the codes of the two passes; the instructions asked the authors to enter their own judgment first) and grep the whole package for variants before delivering; `package_check.py` now does the grep.

## Second round: wording only (2026-10-01, after the lead's check)

Changed: ESM_1, ESM_3, ESM_5, ESM_6 and ESM_7; ESM_2 and ESM_4 are byte-identical to the first delivery. What changed: the anchor wording (ESM_1 three places, the `role` rows of the dictionaries in ESM_3 and ESM_7, the ESM_5 README); the collation spot-check attributed to the Claude instance that supervised the round, with "the files record no human check of the collation" (Guide table 5 and Section 9); the sentence about settling differences between the authors removed (Section 9); "(Claude instances)" at the first use of "coders" in ESM_1, the ESM_5 README and the ESM_7 README, plus a "Coders" convention in ESM_1 Section 2; the blind and non-blind codes of the first sample attributed to Claude instances in the dictionaries; the dictionary notes on `pass1_item`, `pass2_batch`, `pass2_item`, `conf2`, `note2` for first-sample items; "Figure 1" written "Fig. 1" in the ESM_6 dictionary and in the ESM_7 README, `requirements.txt` and script comments. No number, table value or script logic changed (kit self-check 249 passed / 0 failed, also with `--shuowen`).

Third step (14:20, the lead's go-ahead): `LICENSE-Apache-2.0.txt` (the LICENSE file of the shuowenjiezi project at commit 6553a35, copied byte for byte) and `NOTICE.txt` (the Work, its copyright line as the project's README states it, the nine files that hold Shuowen text, the changes made) were added to the kit root, so ESM_7 has 69 files; the README of the kit lists them (sections 4 and 8). `package_check.py` now checks that the licence file is the Apache text and that the NOTICE lists exactly the files that hold Shuowen glosses (probe strings from `pairs.csv`; mutation-tested). Only ESM_7 was rebuilt: run `import build_zips; build_zips.build_esm7()`, because `python build_zips.py` rebuilds ESM_5 as well (and its inner workbook gets a new time-stamp). If a file with Shuowen text is added to the kit, add it to the NOTICE list; the package check will say which one is missing.

Fourth step (14:35, the independent review's finding on the ESM_5 README): the README said that the authors' check sheet showed the codes of the two passes only "after the authors had entered their own judgment". The sheet always showed them (columns H and I); only the instructions asked the authors to enter their own judgment first, as ESM_1, ESM_4, ESM_6, ESM_7 and the paper say. The sentence in `build_esm5()` of `build_zips.py` now reads "The sheet showed the type of each item (...) and the codes of the two passes (columns H and I); the instructions asked the authors to enter their own judgment before looking at the codes." Only ESM_5.zip changed: 33 of its 34 members are byte-identical to the previous delivery (only `README.txt` differs, by that one sentence), because `build_esm5()` was called with `build_check_sheet` replaced by a function returning the delivered inner `author_check_sheet_blank.xlsx` (a rebuilt workbook would carry a new time-stamp). `package_check.py` now keeps the text of every file and fails if any file says "after the authors had entered/filled/written/judged/made", and it checks the ESM_5 README sentence and the two ESM_1 statements (72,044 checks, 0 failed; the previous ESM_5.zip fails two of them, so the check works).

How the round was done, for the next rebuild: the sources here are the new ones. `kit/data_dictionary.csv` inside ESM_7 is the source of truth for the dictionaries (it has hand edits that `build_dictionary.py` does not carry; the builder was updated only on the wording lines above, and it should not be re-run over the kit file). Rebuild order: `build_workbooks.py` (ESM_2/3/6), `build_zips.py` (ESM_5/7), `build_esm1.py`, `verify_esm1.py`, `package_check.py`, then the clean-unzip run of ESM_7. A rebuild writes a new creation time-stamp into every workbook, so an unchanged workbook differs in bytes while all cells are equal: keep the delivered file then (`diff_stage.py` shows it), and the inner `author_check_sheet_blank.xlsx` of ESM_5 was copied byte for byte from the delivered zip. Adding a sentence to the guide moves page breaks: Guide table 5 has column widths (class `t5` in `build_esm1.py`) so that it stays on one page, and Guide table 6 is kept whole (`table.keep`); look at the pages again after any edit.
