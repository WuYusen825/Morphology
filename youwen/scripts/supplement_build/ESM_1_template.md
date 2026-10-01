# Online Resource 1 (ESM_1.pdf)

{{IDBLOCK}}

## 1 What the supplementary material contains

The article asks whether the *yìshēng* 亦聲 label ("also phonetic") of the *Shuōwén jiězì* marks derivation. It compares the 212 labelled entries of the Dà Xú recension with the 953 ordinary phonetic compounds on the same 172 phonetics, using Middle Chinese (MC) readings, Old Chinese (OC) reconstructions and a blind semantic coding of 767 pairs. The seven Online Resources hold the data, the codings, the analysis plan, the raw materials of the coding, the result tables and the code behind every number that the article computes. Section 7 explains how to regenerate the results. The tables of this guide are called "Guide table" to keep them apart from the tables of the article.

**Guide table 1** The Online Resources

| No. | File | What it holds | Used for in the article |
|---|---|---|---|
| 1 | `ESM_1.pdf` | This guide: every file, the data dictionaries, the coding instructions, who coded what, how to reproduce the results | Section 3.3 (coding protocol); reading guide |
| 2 | `ESM_2.xlsx` | Pair-level dataset (sheet `pairs`), the Dà Xú–Xiǎo Xú collation (`recension_collation`), the register of 104 checks against a print edition (`daxu_spotcheck`) | Tables 2, 4–6, 9–11 |
| 3 | `ESM_3.xlsx` | Semantic codings: first blind sample (`first_sample`), enlarged coding (`enlarged_coding`), authors' consolidated check (`author_check`), second answers (`second_answers`) | Tables 3, 5, 7, 8 |
| 4 | `ESM_4.pdf` | Analysis plan of the enlarged coding, committed before any batch was coded, with the log of later changes (English translation) | Sections 3.4, 3.5; H5 and its decision rule |
| 5 | `ESM_5.zip` | The 14 prompts, the raw answers returned by the coders (Claude instances), the two unused second answers, the blank check sheet, the collection log, the item key | Section 3.4; Table 8 note |
| 6 | `ESM_6.xlsx` | Result tables: every model output and count behind Tables 2 and 4–11 and Fig. 1, with the text reports of the scripts | Tables 4–8, 10, 11; Fig. 1; Section 5.2 |
| 7 | `ESM_7.zip` | Python scripts, input tables as CSV files, expected outputs, self-check | Every computed number |

**How to use the material.** To inspect the data, open Online Resources 2 and 3 and read Section 3 for the variables. To see exactly what the coders were told and what they answered, read Section 4.1 and open Online Resource 5. To trace a number of the article, look it up in Guide table 2, which names the result sheet and the script. To rerun everything, unpack Online Resource 7 and follow Section 7; its self-check compares about 190 numbers with the values printed in the article.

**Guide table 2** Where the tables and figure of the article come from

| Article | Data | Results | Script (Online Resource 7) |
|---|---|---|---|
| Table 2, population and subsets | ESM_2 `pairs`; ESM_3 `enlarged_coding` | ESM_6 `report_counts` | `paper_counts.py`, `ext_sample.py` |
| Table 3, coding scheme with examples | ESM_3 `enlarged_coding` (pairs on which both passes agreed with confidence 3) | ESM_6 `report_counts` | `paper_counts.py` |
| Section 4.1, numbers in the text | ESM_2 `pairs` | ESM_6 `summary_counts`, `core_models` | `core_models.py` |
| Table 4, sound relations | ESM_2 `pairs` | ESM_6 `extra_checks`, `summary_counts` | `paper_checks.py`, `core_models.py` |
| Table 5, 16 departing-tone members | ESM_2 `pairs`, `recension_collation`; ESM_3 `first_sample`, `enlarged_coding` | ESM_6 `table5_members` | `paper_counts.py` |
| Table 6, departing tone and other relations | ESM_2 `pairs` | ESM_6 `core_models`, `extra_checks`, `summary_counts` | `core_models.py`, `paper_checks.py` |
| Table 7, relatedness of meaning | ESM_3 `first_sample`, `enlarged_coding`, `author_check` | ESM_6 `ext_coding_models`, `ext_author_check_models`, `report_first_sample` | `ext_analysis.py`, `ext_author_check.py`, `first_sample_checks.py` |
| Table 8, sound among related pairs | ESM_3 `enlarged_coding`, `author_check`, `second_answers` | ESM_6 `ext_coding_models`, `ext_author_check_models`, `ext_second_answer_models` | `ext_analysis.py`, `ext_author_check.py`, `ext_second_answer_sensitivity.py` |
| Table 9, relation types of homophonous pairs | ESM_2 `pairs` (`identical_relation_type`) | ESM_6 `report_counts` | `paper_counts.py` |
| Table 10, recension layers | ESM_2 `pairs`, `recension_collation` | ESM_6 `extra_checks`, `xiaoxu_sensitivity` | `paper_checks.py`, `sensitivity_xiao_xu.py` |
| Sections 4.5 and 4.6, numbers in the text (how much of the label; recension layers, glosses, Duan's emendations, filing position) | ESM_2 `pairs`, `recension_collation` | ESM_6 `extra_checks`, `xiaoxu_sensitivity`, `summary_counts` | `paper_checks.py`, `sensitivity_xiao_xu.py`, `core_models.py` |
| Table 11, checks on the main results | ESM_2, ESM_3 | ESM_6 `extra_checks`, `wangyun_sensitivity`, `xiaoxu_sensitivity`, `report_first_sample` | `paper_checks.py`, `sensitivity_wang_yun.py`, `sensitivity_xiao_xu.py`, `first_sample_checks.py` |
| Fig. 1, forest plot for H5 | ESM_3 | ESM_6 `fig1_values` | `paper_figure.py` |
| Section 3.4 and 4.3, agreement statistics | ESM_3 | ESM_6 `report_kappa`, `report_author_check`, `report_first_sample` | `ext_analysis.py`, `ext_author_check.py`, `first_sample_checks.py` |
| Section 5.2, bias sensitivity | ESM_3 | ESM_6 `bias_sensitivity_grid`, `report_bias_sensitivity` | `ext_bias_sensitivity.py` |

Tables 1 and 12 of the article repeat numbers that are traced in the rows above. A further sensitivity analysis, a reverse-direction scenario of the coding bias (ESM_6 `bias_reverse_scenario`, `report_reverse_scenario`; script `ext_bias_reverse_scenario.py`), is provided but not discussed in the text of the article.

## 2 Conventions

* **Format.** Spreadsheets are Excel workbooks (`.xlsx`); the same tables are CSV files in Online Resource 7 (UTF-8 with a byte-order mark). The workbooks were generated from these CSV files and hold identical contents. Each workbook starts with a sheet `About` (identification, caption, sheet list, conventions) and ends with a sheet `data_dictionary`; every other sheet holds one table with a header row.
* **Language.** All headers, descriptions and documentation are in English. Chinese appears only as data: characters, *Shuōwén* glosses, quotations and labels (for example `亦聲`). Every column that holds characters has a companion column of Unicode code points, written `U+XXXX`.
* **Missing values.** `NA` means not available (for example, no reading at one end of a pair); an empty cell means not applicable or not recorded. `True` and `False` are written as text.
* **Coders.** "Coder", "coder instance" and "machine coder" mean a Claude instance (Anthropic's language model) that was given the coding instructions and returned its codes. The authors' own judgments are always called "the authors' judgments" (Section 5).
* **Keys and groups.** `sw_id` is the row number of the head entry in the open *Shuōwén* data and links the sheets and files; it is unique among the rows of the comparison frame (in the whole sheet `pairs` one head entry has two rows). `group` is `labelled` (the Dà Xú analysis of the compound names its phonetic with *yìshēng*) or `ordinary` (plain phonetic compound, 聲); `relation` gives the same in the *Shuōwén*'s own terms (`亦聲`, `聲`). Two further values mark rows that the article does not use: `abbreviated_phonetic` (省聲, 17 rows) and `source_other` (`會意/其他`, 39 extra rows found only in Duan Yucai's commentary or in the Xiǎo Xú). The tests of the article use the 212 labelled and 953 ordinary rows with `in_comparison_frame = True` (Table 2 of the article calls them the analysis set); the column `in_analysis_set` marks the wider set before the restriction to phonetics that have a labelled member (212 labelled and 1,019 ordinary rows; Section 4.5).
* **Numbers.** Result tables show estimates at the precision at which the scripts print them (odds ratios and p-values in the form of the article). Odds ratios (OR) are given with 95% confidence intervals; `hits` and `n` count the outcome and the pairs for the labelled group (`group1_`, `labelled_`) and the ordinary group (`group0_`, `ordinary_`).

**Guide table 3** Codes and abbreviations

| Term | Meaning |
|---|---|
| Y, E, N, X | Semantic codes: Y same or near-synonymous meaning; E connected only through one step of extension or inference; N no visible semantic relation; X the compound is a proper name. "Related" means Y or E |
| MC, OC | Middle Chinese (readings from the *Guǎngyùn* in Baxter's notation); Old Chinese (Baxter and Sagart 2014) |
| identical, alt_departing, alt_other, other | The four mutually exclusive MC categories of the pair (Section 4.2); "near" means identical or alt_departing |
| I, R, O, O2, V, C | Old Chinese relation categories of the pair (Section 4.3) |
| L, F, C, U, X | Relation types of homophonous pairs (Section 4.4) |
| H1a, H1b, H1c, H2, H3, H4, H5 | The hypotheses of the article: H1a homophony; H1b other regular relations among non-identical pairs; H1c departing tone among tone or voicing alternations; H2 relatedness of meaning; H3 recension layers; H4 filing under the compound's own phonetic; H5 sound among related pairs |
| P1, S1–S9, X1–X5 | Labels of the tests of the enlarged coding in the result sheets (Guide table 4) |
| GEE, MH | Logistic generalised estimating equations clustered by phonetic; Mantel–Haenszel estimate within phonetic series |

**Guide table 4** Labels of the tests of the enlarged coding in the result sheets (details in Online Resource 4, Section 4)

| Label | Test |
|---|---|
| P1 | Primary test of H5: near ~ label among pairs coded related (Y or E), pass-1 codes |
| S1 | Outcome identical readings only |
| S2 | Pairs with paronomastic glosses removed (both groups) |
| S3 | Only labels shared by both recensions (all ordinary pairs kept) |
| S5, S7 | Pass-2 codes for the new items; only pairs on which the passes agree on related or unrelated |
| S6 | Strict coding (only Y counts as related); not estimable because the ordinary group has no near pair among 4 |
| S8, S8b | H2: related ~ label on all coded pairs (pass 1; pass 2) |
| S9 | Premise of meaning-first: near ~ related + label |
| X1, X2, X3, X4 | Exploratory: pairs coded E only; adjusted for Y against E; core labels (shared and without paronomastic gloss); the 677 new items only (X4b: the 90 first-sample items) |
| X5 (sheet `ext_second_answer_models`) | The second answers of pass 1, batches 3 and 6 substituted (tiers `second_b3_b6`, `second_b3_only`, `second_b6_only`) |
| tier `author_adjudicated` | The authors' consolidated judgments substituted for the 126 checked items |
| `P1r`, `S1r` (sheet `bias_reverse_scenario`) | Reverse-direction scenario (tiers `fold_all`, `fold_far`) |

## 3 Data dictionaries

### 3.1 Online Resource 2 (`ESM_2.xlsx`)

**Sheet `pairs`** (1,333 rows). One row per pair of a *Shuōwén* compound (the "member") and its phonetic, extracted from the open Dà Xú text: 223 labelled rows, 1,054 ordinary rows, 17 rows with an abbreviated phonetic (省聲) and 39 extra rows found only in Duan Yucai's commentary or in the Xiǎo Xú (not analysed).

{{DICT:ESM_2:pairs}}

**Sheet `recension_collation`** (227 rows). The collation of the 227 raw *yìshēng* headwords of the Dà Xú text with the Xiǎo Xú recension: of the 212 analysis entries, 140 carry the label in both recensions, 62 in the Dà Xú only, 10 cannot be decided.

{{DICT:ESM_2:recension_collation}}

**Sheet `daxu_spotcheck`** (104 rows). The register of the 104 analysis-set entries that were checked against the scan of a print edition (Section 6).

{{DICT:ESM_2:daxu_spotcheck}}

### 3.2 Online Resource 3 (`ESM_3.xlsx`)

**Sheet `first_sample`** (100 rows). The first blind sample: 40 labelled and 60 ordinary pairs drawn from pairs with OC forms at both ends, coded blind and non-blind (Section 5).

{{DICT:ESM_3:first_sample}}

**Sheet `enlarged_coding`** (767 rows). The enlarged blind coding: the 677 new items (177 labelled, 500 ordinary) coded in two passes, and the 90 first-sample items that lie in the sampling frame (35 of them served as anchors: each batch added 5 of them, and each anchor was coded once in each pass).

{{DICT:ESM_3:enlarged_coding}}

**Sheet `author_check`** (126 rows). The authors' consolidated check: all 76 pairs on which the two passes disagree, and 50 pairs drawn at random from the 601 on which they agree.

{{DICT:ESM_3:author_check}}

**Sheet `second_answers`** (203 rows). The second answers of pass 1, batches 3 and 6 (193 new items and 10 anchors), beside the first answers that were used.

{{DICT:ESM_3:second_answers}}

### 3.3 Online Resources 5, 6 and 7

*Online Resource 5* contains plain-text files described in its `README.txt`: a prompt file holds the instructions followed by one item per line (tab-separated), an answer file one answer line per item. `item_key.csv` is documented in `README.txt` and, as `ext_items_key.csv`, in `data_dictionary.csv` of Online Resource 7; `collection_log.csv` in `README.txt`.

*Online Resource 6* has one sheet per result table or text report; the sheet `About` lists them with the script that wrote each and the place in the article that uses it, and the sheet `data_dictionary` describes every column (199 rows). The text reports (sheets starting `report_`) hold one line of the report per row.

*Online Resource 7* has `data_dictionary.csv` (file, column, description) for every CSV file in `data/` and `output/`; its `README.txt` describes the folders and scripts.

## 4 Coding instructions and definitions

### 4.1 Semantic coding (Y, E, N, X)

**What the coders saw.** For each pair: an item number, the phonetic with its *Shuōwén* gloss, and the compound with its gloss. In the glosses the structural analysis was removed: only the part of the gloss before 从 is shown, the formula 凡某之屬皆… is deleted, and a gloss that begins with 从 (only 貣 in the sampling frame) is cut at its first full stop, so that no "X聲" is visible. A script asserts that no gloss shown contains 亦聲 or "从某聲". Where the phonetic is not itself a head entry of the open *Shuōwén* data (`head_in_shuowen` = False; 8 phonetics and 10 pairs in the enlarged coding, 2 pairs in the first sample) the coders were shown the word `None` instead of a gloss; in the workbooks the cell is empty. The group (labelled or ordinary), the Dà Xú formula and the readings were never shown. The coders were told not to read files or to use the web, and the collection log (Online Resource 5) shows that the only tool call any instance reported was the hand-back of its answer.

**Enlarged coding: the complete prompt.** Each of the 14 prompts (2 passes × 7 batches; 101 or 102 items each, of which 96 or 97 new items and 5 anchors, labelled and ordinary pairs mixed, order and batching different in the two passes, a fresh coder instance for each batch) has this text; `{n}` is the number of items of the batch. The filled prompts are in Online Resource 5.

```
{{PROMPT}}
```

**First sample: the protocol as recorded.** The first blind sample (100 pairs) was coded under the same criteria. The protocol file kept with the project gives the instructions in the following form; […] marks two passages that the record does not reproduce:

> Code 100 character pairs from the Shuowen glosses given below. […] Use ONLY the glosses in this prompt and your own knowledge of classical Chinese and the Shuowen. Do NOT read, search or open any file on disk, and do NOT use any web or search tool. […] Do NOT try to recall or check whether Xu Shen analyses the member character as 某聲, 某亦聲 or 會意.
>
> For each item, compare the 本义 of the member character with the 本义 of the phonetic character. Pick one code: Y: the same or near-synonymous meaning (厓 山邊也 / 涯 水邊也). E: connected only through one step of extension or inference (亡 逃也 / 忘 不識也). N: no semantic relation is visible. X: the member character is a proper name (place, river, surname, named plant or animal).
>
> Judge by 本义 only, not later or loan meanings. Where a gloss is "None", judge from your knowledge of that character's Shuowen 本义, with confidence 1 unless sure. A pun-style gloss (e.g. 狗 "叩也") is not evidence of a real semantic relation by itself. Confidence 1–3; a note of ≤15 characters. When unsure between two codes, prefer E over Y and N over E.
>
> Output exactly 100 lines: item, code, confidence, note (tab-separated).

The prompt of the enlarged coding contains three sentences that are not in the recorded text: one says what each item shows and that the structural analysis has been removed from the glosses, one asks the coder to work alone and give the answer directly, and one heads the item table; none concerns the criteria. The 35 anchor items (each batch added 5 of them; each was coded once in each pass) measure the effect of such differences: both passes agree with the first sample's blind codes on the anchors (κ = 0.875 and 0.918).

**How the answers were read.** Each line of an answer is: item number, code (Y, E, N or X), confidence (1–3), note. The first complete and acceptable answer of each coder instance counts. In pass 1, batches 3 and 6, the environment returned a second answer; these two answers are kept (Online Resource 5) and enter only the sensitivity analysis X5. The analysis plan fixed that a batch with missing, duplicated or invalid lines, or one in which the instance had used a tool, would be re-coded as a whole; none was (all 14 answers had the expected number of readable lines). Pairs coded X (proper names) enter no test. "Related" means Y or E.

### 4.2 Middle Chinese readings and sound relations

The reading of each character is that *Guǎngyùn* reading that matches the Dà Xú *fǎnqiè*; the *Guǎngyùn* positions are those of tshet-uinh 0.15.1 (the Zecun-tang text as compiled by the nk2028 project and collated against Zhou Zumo's *Guǎngyùn jiàoběn*). Matching tries, in this order: identical *fǎnqiè*; same initial, rhyme and tone; same rhyme and tone only; same initial only; if nothing matches, the first reading is taken and flagged (column `mc_confidence`). Readings are written in Baxter's notation (`mc_bs2014`; final -X for the rising and -H for the departing tone; a syllable without either marker has the level tone, or the entering tone if it ends in -p, -t or -k).

The relation of compound and phonetic (`mc_relation`) is `identical` (the same reading), `tone_voicing_alt` (the rhyme part is the same and the readings differ only in tone or in the voicing of the initial; a voicing alternation is the pairing of a full-voiced initial with its full-voiceless counterpart: b/p, d/t, dr/tr, dz/ts, dzr/tsr, dzy/tsy, g/k, z/s, zr/sr, zy/sy, h/x; differences of aspiration or place of articulation make the pair `other`), `other`, or `NA` when one end has no reading. For `tone_voicing_alt` pairs, `mc_qusheng_direction` records whether the compound (`member`) or the phonetic (`head`) has the departing tone, or neither (`none`). The four categories of Table 4 of the article (variable `cat4` in the enlarged coding) are: `identical`; `alt_departing` (an alternation with a departing tone at one end); `alt_other` (any other tone or voicing alternation); `other`. "Near" means `identical` or `alt_departing`. Alternations between the departing and the entering tone are not counted as tone alternations, because their MC rhymes differ (a final stop against none).

### 4.3 Old Chinese reconstructions and relations

OC forms are those of Baxter and Sagart (2014) as compiled in the cddb database (file `D_ocbs.tsv`). A form is linked to a character through its MC reading where possible (`oc_bs_match`: `mc_match`, `single_reading`, `multiple_readings`, `not_in_bs`). The relation of compound and phonetic (`morph_relation_auto`) is classified automatically from the two reconstructions, after removing square-bracketed uncertain segments: `I` identical; `R` the forms differ only in a prefix, a suffix (including \*-ʔ and \*-s), pharyngealisation or medial \*r; `O` the initial differs (same place of articulation); `O2` the initial differs (different place); `V` the vowel differs; `C` the coda differs; `NA` no reconstruction at one end. For `R` pairs the affix change is recorded in `morph_affix_detail` and `morph_affix_type`. Table 6 of the article separates `R` pairs that involve \*-s from the others.

### 4.4 Relation types of homophonous pairs (L, F, C, U, X)

For the pairs whose MC readings are identical, `identical_relation_type` classifies the relation of compound and phonetic: **L** accumulated graph (累增字: the compound is the phonetic with a determinative added for the same word); **F** distinguishing graph (分別文: one sense or word of the phonetic is given its own graph); **C** conversion (转类: a change of word class with the sound unchanged, for example noun to verb); **U** unrelated homophone (a loan or a purely phonetic use); **X** proper name (not counted). The values were assigned by the instance that built the dataset with the label visible, and both authors reviewed each of the 196 pairs (63 labelled and 133 ordinary) and agreed with the values (the column also holds values for 19 rows outside the comparison frame, which no table uses). This coding is descriptive (Table 9 of the article) and is not a blind test.

### 4.5 Other annotation flags

* `is_xinfu`, `in_analysis_set`, `in_comparison_frame`: the 227 raw headwords contain four false hits (亦 is itself the phonetic) and eleven *xīnfù* 新附 entries added by Xu Xuan in 986, identified as section-final entries without Duan Yucai's commentary (`is_xinfu` marks every row whose compound is such an entry: 48 rows, 11 of them labelled); the 212 that remain form the analysis set, and the comparison frame is the analysis-set rows whose phonetic has at least one labelled member (212 labelled and 953 ordinary rows on 172 phonetics).
* `paronomastic_gloss`: True if the definitional part of the gloss (before 从) contains the phonetic character itself (58 of 212 labelled and 11 of 953 ordinary rows).
* `filed_under_phonetic`: True if the compound is filed in the *Shuōwén* section headed by its own phonetic (40 labelled, no ordinary row).
* `duan_label`, `duan_phonetic`, `duan_phonetic_changed`: whether Duan Yucai's text keeps the label (`亦聲`), drops it (`無`) or has no commentary in the data (`缺段注`), and which phonetic it names.
* `layer` (sheet `recension_collation`): `both` (label in both recensions), `daxu_only`, `unknown` (cannot be decided: seven entries lie in juan 25 of the Xiǎo Xú, which was lost and later supplied from the Dà Xú, two were probably supplied the same way, one is blank in the print). `round` records the round in which an entry was read: `round1` (70 headwords) and `round2` (100) in the digital text, `round3_scan` (57 headwords that the digital text lacks, 56 of them in the analysis set) on the scan (Section 5). The column `xiaoxu_label` of `pairs` is a preliminary alignment; the collation of record is `recension_collation`.

## 5 Who coded what

**Guide table 5** Provenance of the variables

| Variable or file | Made by | Blind to group? | Record |
|---|---|---|---|
| Extraction of the 227 headwords, the 212 labelled entries, the 953 ordinary compounds; flags such as `paronomastic_gloss`, `filed_under_phonetic`, `is_xinfu` | Scripts (pattern search and rules) written with the help of Claude (Anthropic); three headwords resolved by hand | not applicable | ESM_2 `pairs` |
| MC readings and categories; OC forms and categories | Scripts from the *Guǎngyùn* positions and the Baxter–Sagart forms; no coder | not applicable | ESM_2 `pairs` |
| Dà Xú–Xiǎo Xú collation (`layer`) | Aligned by script and read by Claude instances: 170 headwords in the digital Xiǎo Xú text (Kanseki Repository KR1j0019; rounds 1 and 2) were compared item by item, and the 57 that the digital text lacks were located and transcribed on the scan of the National Library of China (round 3), where the readings were spot-checked on two entries by the Claude instance that supervised the round; the files record no human check of the collation | not applicable | ESM_2 `recension_collation` |
| Semantic codes, first sample (100 pairs) | **Blind pass:** a separate Claude instance that saw only the instructions and the stripped glosses (no files, no web). **Non-blind pass:** the Claude instance that built the dataset, knowing the group. The two authors each coded the 100 pairs independently from the unlabelled sheet and agreed with the blind pass throughout; their working sheets were not kept, so the blind codes are the codes of record | blind pass yes; non-blind pass no | ESM_3 `first_sample`; Section 4.1 |
| Semantic codes, enlarged coding (677 new items) | Two independent blind passes by separate Claude instances, a fresh instance for each of 14 batches; analyses use pass 1, pass 2 is a check | yes | ESM_3 `enlarged_coding`; ESM_5 |
| Authors' check of 126 items | Each author checked the 126 items separately; the judgments were consolidated into one code per item. Only the consolidated sheet is on file | yes for the group; the sheet also showed the type of each item and the codes of the two passes (the instructions asked the authors to enter their own judgment first) | ESM_3 `author_check` |
| Relation types L, F, C, U, X of homophonous pairs | Assigned by the Claude instance that built the dataset; both authors reviewed each of the 196 pairs and agreed with the values | no (label visible); descriptive only | ESM_2 `pairs` |
| Register of 104 checks against a print edition | Headword, gloss and *yìshēng* formula read against the scan page by page, with the assistance of Codex (OpenAI) | not applicable | ESM_2 `daxu_spotcheck`; Section 6 |
| Analysis plan, sampling, analysis scripts | Written by Claude following the authors' decision to enlarge the blind coding; the plan, the sampling script (which generates the prompts) and the analysis script were committed with a time-stamp before any batch was coded; nothing was registered externally | not applicable | ESM_4; ESM_7 |

**Agreement.** First sample: the blind and the non-blind pass agree on 86 of 100 pairs (Cohen's κ = 0.773), with no Y–N disagreement; this is agreement between two codings by the same model family, not between human coders. Enlarged coding: the two passes agree on 88.8% of the 677 new items (κ = 0.817; 0.681 for labelled and 0.824 for ordinary pairs). The authors' consolidated judgments agree with pass 1 at κ = 0.735 [95% CI 0.603, 0.842] and with pass 2 at κ = 0.798 [0.666, 0.905] (stratified estimates for all 677 items from the 126 checked). The reports are in ESM_6 `report_kappa`, `report_author_check` and `report_first_sample`.

## 6 The register of print-edition checks

The sheet `daxu_spotcheck` of Online Resource 2 records 104 of the 212 analysis-set entries whose headword, gloss and *yìshēng* formula were read against the scan of a print edition: Chen Changzhi's 1873 print of the *Shuōwén* in the Waseda University Library (the scan comes as ten PDF files numbered `ho04_00029_0001.pdf` to `ho04_00029_0010.pdf`, of which the register uses 0001 to 0004 and 0007; the locator is the file and the page of the PDF counted from 1, not the leaf number of the print). Of the 104 checks, 73 recorded an excerpt that agrees with the electronic text, 30 were visual checks without a saved excerpt, and one (䢈) shows a variant: the electronic text reads 日月合宿从辰, the print clearly 日月合宿爲辰, while the formula agrees.

The entries were chosen as the checking proceeded and as the argument needed examples. **The register is not a random sample, and it cannot be used to estimate a transcription error rate for the other 108 entries.** The check covers headword, relevant gloss and formula, not a full collation of the entry, and it does not re-decide the readings of the Xiǎo Xú. One discrepancy beyond the register is unresolved: the electronic text has a head entry written with the character U+28EFA (glossed 仄也, formula 頃亦聲) that was not found in the Chen scan, where 陊 follows 隓 directly (scan file 0008, PDF page 27); this records the absence on that page only and does not show that other editions lack the entry.

## 7 Reproducing the results

Unpack `ESM_7.zip` and run `python scripts/run_all.py` in the folder that contains `README.txt` (Python 3.10 or later with numpy, pandas, scipy and statsmodels; matplotlib for Fig. 1). The run takes about a minute. It runs the 13 analysis scripts in dependency order and then `scripts/self_check.py`, which

1. compares every file in `expected/` with the file that the scripts have just written (counts exactly, decimals within one unit of the last printed digit, the 14 coder prompts by SHA-256 hash);
2. compares about 190 numbers and counts printed in the article (Tables 2 and 4–11, Fig. 1 and the text) with the values in `output/`; and
3. checks package integrity: UTF-8 text, English headers, every column described in `data_dictionary.csv`, scripts that compile, and no e-mail addresses, local file paths or unexpected repository links in any file.

All random numbers are seeded in the scripts; the scripts never call the coder model, whose answers are read from `data/raw/`. The two analyses that count phrases in Duan Yucai's commentary use counts stored in `data/duan_notes_precomputed.csv`; running with `--shuowen DIR` on a clone of the open *Shuōwén* data recomputes them and gives identical results. Variational-Bayes mixed models (columns `glmm_vb_*`) may differ in the last printed digit between runs or library versions; the self-check allows for this, and the article does not report these columns. The `README.txt` of Online Resource 7 lists every script, what it writes and where the article uses it.

**What the package does not reproduce.** The analyses start from the pair table and the coding tables. The scripts that built the pair table from the open sources (extraction of the formula, matching of the *fǎnqiè* to the *Guǎngyùn*, lookup of the Old Chinese forms) depend on external data and software and on the working environment of the project and are not part of the package; the rules they implement are described in Section 3 of the article and in Sections 4.2 to 4.5 above, and every value they produced is in the sheet `pairs`. The coders' answers cannot be regenerated, since they were returned by the model; they are given as received (Online Resource 5).

## 8 Sources and rights

**Guide table 6** Resources behind the dataset

| Resource | Used for | Terms |
|---|---|---|
| Digital *Shuōwén jiězì* of the shuowenjiezi project (github.com/shuowenjiezi/shuowen, commit 6553a35): Dà Xú text, *fǎnqiè*, Duan Yucai's commentary | Glosses, formulas, Dà Xú readings, Duan layer | Apache License 2.0 |
| *Guǎngyùn* positions from the Qieyun data of the nk2028 project, via tshet-uinh 0.15.1 and tshet-uinh-examples (Baxter's notation) | MC readings | Data CC0; software MIT |
| Baxter and Sagart (2014), as compiled in the cddb database (github.com/digling/cddb, commit 054fb4c, file `D_ocbs.tsv`) | OC forms | Repository GPL-3.0; please cite Baxter and Sagart (2014) |
| Xiǎo Xú *Shuōwén jiězì xìzhuàn*, Sibu congkan edition: digital text of the Kanseki Repository (KR1j0019), scan of the National Library of China | Recension layers | Consulted; not redistributed except the short quotations in `recension_collation` |
| Chen Changzhi 1873 print of the *Shuōwén* (Waseda University Library scan) | Register of print-edition checks | Consulted; not redistributed |

**Reuse.** The authors' own contributions in these files (codings, annotations, tables, documentation) are released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0), and the analysis code under the MIT licence. The columns derived from the resources above keep the terms of their sources. In particular, the *Shuōwén* text (the gloss columns `head_gloss`, `shuowen_gloss`, `electronic_text_gloss`, `daxu_gloss`, `phonetic_gloss` and `member_gloss`, and the columns derived from Duan Yucai's commentary) comes from a project distributed under the Apache License 2.0, whose notice is reproduced here: this material contains text from the shuowenjiezi project, Apache License 2.0, https://www.apache.org/licenses/LICENSE-2.0; and the OC strings (`oc_bs2014`, `head_oc_bs2014`) come from a GPL-3.0 repository and the work of Baxter and Sagart, to be cited when reused. Anyone who redistributes these columns should check the terms of the original source.

## 9 Limits of the record

* The two authors' own working sheets for the first sample were not kept. The values in `first_sample` are the blind codes of a Claude instance; the authors' independent coding, which agreed with them throughout, cannot be reproduced from the files, and no agreement between the authors is reported.
* For the 126-item check only the consolidated sheet is on file. The sheet displayed the type of each item and the codes of the two passes (the instructions asked the authors to enter their own judgment first), so the authors' judgments are not independent of the machine codes. The agreement figures are between the consolidated judgments and the machine codes.
* The Dà Xú–Xiǎo Xú collation was made by Claude instances: the entries of the digital text were compared item by item, the readings on the scan were spot-checked on two entries by the Claude instance that supervised the round, and the files record no human check of the collation. Ten labels cannot be decided.
* The relation types L, F, C, U, X were assigned with the label visible and are descriptive only.
* The register of print-edition checks covers 104 of 212 entries and is not a random sample (Section 6).
* The machine coders are instances of one model family, so their errors may be correlated; the enlarged coding was designed with anchor items and a second pass to measure this, and the article reports a bias sensitivity analysis (Section 5.2).
* The result sheets show numbers at the precision at which the scripts print them. Differences in the last digit of variational-Bayes estimates between runs do not affect any number printed in the article.
* The scripts that built the pair table from the open sources are not part of the package (Section 7).
* The reverse-direction scenario (ESM_6 `bias_reverse_scenario`) is provided for completeness and is not discussed in the text of the article.
