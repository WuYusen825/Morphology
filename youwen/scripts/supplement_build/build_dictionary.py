# Internal build step (not shipped): the data dictionary (kit/data_dictionary.csv), one row per column of every CSV in data/ and output/.
# Descriptions are written once here; shared model-result columns are described once and applied to every file that has them.
import csv, glob, json, os
import pandas as pd

KIT = '/tmp/claude-0/-home-user-Morphology/7d9f6fd5-d830-551f-9a43-e3ebcc390a52/scratchpad/esm/kit'
os.chdir(KIT)

# ---- shared descriptions -------------------------------------------------------------------------------------------
CP = 'Unicode code point(s) of the character, written U+XXXX (the Chinese character itself is in the column of the same name without "_codepoint")'
MODEL = {   # result tables of the ext_* scripts (group1 = labelled, group0 = ordinary)
    'tier': 'kind of analysis: primary (the one confirmatory test), secondary (robustness checks fixed in the plan), exploratory (added after the results were seen), descriptive (counts only); in the author-check and second-answer tables, which codes were used (see the file description)',
    'test': 'name of the test or comparison; the outcome is written before "~" and the subset after "|"',
    'n': 'number of pairs entering the model',
    'n_phonetics': 'number of distinct phonetics (clusters) among those pairs',
    'group1_hits': 'number of labelled pairs with the outcome',
    'group1_n': 'number of labelled pairs in the comparison',
    'group1_rate': 'group1_hits / group1_n',
    'group0_hits': 'number of ordinary pairs with the outcome',
    'group0_n': 'number of ordinary pairs in the comparison',
    'group0_rate': 'group0_hits / group0_n',
    'gee_OR': 'odds ratio, labelled against ordinary, from a logit GEE clustered by phonetic (exchangeable working correlation; independence if that fails)',
    'gee_CI95': '95% Wald confidence interval of gee_OR, written low-high',
    'gee_p_one_sided': 'one-sided p of the GEE odds ratio (direction fixed in advance), two significant digits',
    'gee_p_one_sided_exact': 'the same one-sided p with four significant digits',
    'gee_p_two_sided': 'two-sided p of the GEE odds ratio, two significant digits',
    'gee_cov': 'working correlation structure actually used for the GEE',
    'mh_strata': 'number of phonetics that contain both labelled and ordinary pairs (strata of the Mantel-Haenszel estimate)',
    'mh_OR': 'Mantel-Haenszel pooled odds ratio within phonetics',
    'mh_CI95': '95% confidence interval of mh_OR, written low-high',
    'cmh_p_two_sided': 'two-sided p of the Cochran-Mantel-Haenszel test',
    'fisher_p_two_sided': 'two-sided p of Fisher\'s exact test on the unstratified 2 x 2 table',
    'verdict': 'reading of the result under the decision rule of the analysis plan (excess significant at one-sided .05 and upper confidence limit at least 2 = supports C; upper limit below 2 = supports A; otherwise indeterminate)',
    'note': 'free-text note: what the row is, how it differs from the primary test, and where it was added after the results were seen',
}
COUNTS = {  # tables with labelled / ordinary columns (core, extra checks, sensitivity)
    'labelled_hits': 'number of labelled pairs (or entries) with the outcome',
    'labelled_n': 'number of labelled pairs (or entries) in the comparison',
    'labelled_rate': 'labelled_hits / labelled_n',
    'ordinary_hits': 'number of ordinary pairs with the outcome',
    'ordinary_n': 'number of ordinary pairs in the comparison',
    'ordinary_rate': 'ordinary_hits / ordinary_n',
    'gee_OR': 'odds ratio from a logit GEE clustered by phonetic (in a few descriptive rows the note says that the column holds another estimate)',
    'gee_CI95': '95% confidence interval of gee_OR, written low-high',
    'gee_p_two_sided': 'two-sided p of the GEE odds ratio',
    'gee_p_one_sided': 'one-sided p of the GEE odds ratio (direction fixed in advance)',
    'mh_strata': 'number of phonetics with both labelled and ordinary pairs (strata of the Mantel-Haenszel estimate)',
    'mh_labelled_n': 'number of labelled pairs in those strata',
    'mh_ordinary_n': 'number of ordinary pairs in those strata',
    'mh_OR': 'Mantel-Haenszel pooled odds ratio within phonetics',
    'mh_CI95': '95% confidence interval of mh_OR, written low-high',
    'cmh_p_two_sided': 'two-sided p of the Cochran-Mantel-Haenszel test',
    'fisher_p_two_sided': 'two-sided p of Fisher\'s exact test',
    'fisher_one_sided': 'one-sided p of Fisher\'s exact test (excess in the labelled group; for H4 the smaller of the two one-sided p)',
    'note': 'free-text note on the row',
    'n': 'number of pairs entering the model', 'n_phonetics': 'number of distinct phonetics (clusters)',
    'glmm_vb_OR': 'odds ratio from a mixed logit with a random intercept per phonetic, fitted by variational Bayes (a cross-check; can differ in the last digit between platforms)',
    'glmm_vb_CI95': '95% interval of glmm_vb_OR', 'glmm_vb_z': 'posterior mean divided by posterior standard deviation of the log odds ratio',
    'holm_p': 'Holm-corrected one-sided p within the main set or within the set without labels filed under their own phonetic',
    'hypothesis': 'hypothesis label of the paper (H1a, H1b, H1c, H2, H3, H4; "-sens", "-types", "-confound" mark side analyses)',
    'comparison': 'what is compared; "labelled columns" / "ordinary columns" in the text name the groups that fill those columns when a row reuses them',
    'outcome': 'outcome variable of the model', 'variant': 'data variant on which the model was fitted',
    'section': 'group of analyses (see the header of scripts/paper_checks.py)',
}

D = {}   # file -> {column: description}
D['data/pairs.csv'] = {
    'sw_id': 'row number of the head entry in the open Shuowen data; the key that links the tables',
    'char': 'the compound (the "member"): a character whose Shuowen analysis names the phonetic',
    'char_codepoint': CP, 'phonetic': 'the phonetic (series head) of the compound', 'phonetic_codepoint': CP,
    'group': 'labelled = analysis names the phonetic with yisheng; ordinary = plain sheng compound; abbreviated_phonetic = sheng with an abbreviated phonetic; source_other = extra row found only in Duan\'s text or the Xiao Xu (not analysed)',
    'relation': 'the same classification in the Shuowen\'s own terms: 亦聲 (yisheng), 聲 (sheng), 省聲 (abbreviated phonetic), 會意/其他 (extra rows)',
    'label_source': 'where the label is found: daxu (Da Xu text) / duan_only / xiaoxu_only / duan_only+xiaoxu_only',
    'in_analysis_set': 'True if the row is in the analysis set: label in the Da Xu text, not a xinfu (Xu Xuan\'s addition), relation yisheng or sheng',
    'in_comparison_frame': 'True if the row is in the analysis set and its phonetic has at least one labelled member (212 labelled and 953 ordinary rows)',
    'is_xinfu': 'True if the entry is a xinfu addition of Xu Xuan (not in the older text)',
    'head_in_shuowen': 'True if the phonetic is itself a head entry of the Shuowen',
    'head_gloss': 'Shuowen gloss of the phonetic', 'head_dx_fanqie': 'Da Xu fanqie of the phonetic',
    'shuowen_gloss': 'Shuowen gloss of the compound, including the structural analysis (from the open Shuowen data)', 'daxu_fanqie': 'Da Xu fanqie of the compound',
    'mc_bs2014': 'Middle Chinese reading of the compound in Baxter\'s transcription (final -X rising tone, -H departing tone), derived from the Guangyun position matched to the Da Xu fanqie',
    'guangyun_position': 'Guangyun phonological position of the matched reading (initial, openness, division, rhyme, tone)',
    'mc_confidence': 'how the Guangyun reading was matched to the fanqie: identical_fanqie / initial+rhyme+tone / rhyme+tone_only / initial_only / no_match_first_reading / none',
    'head_mc_bs2014': 'Middle Chinese reading of the phonetic', 'head_mc_confidence': 'match confidence for the phonetic (same values)',
    'mc_tone_member': 'MC tone of the compound: 平 level, 上 rising, 去 departing, 入 entering', 'mc_tone_head': 'MC tone of the phonetic (same values)',
    'mc_voicing_differs': 'True if the initials of the two readings differ in voicing only',
    'mc_relation': 'sound relation of compound and phonetic in MC: identical / tone_voicing_alt (same except tone or voicing) / other / NA (no reading at one end)',
    'mc_qusheng_direction': 'only for tone_voicing_alt pairs: member (the compound has the departing tone) / head (the phonetic has it) / none',
    'oc_bs2014': 'Old Chinese reconstruction of the compound (Baxter and Sagart 2014, from the cddb database; square brackets = uncertain segments)',
    'oc_bs_match': 'how the OC entry was found: mc_match (its MC reading equals the derived MC reading) / single_reading / multiple_readings / not_in_bs',
    'head_oc_bs2014': 'OC reconstruction of the phonetic', 'head_oc_bs_match': 'match status for the phonetic (same values)',
    'morph_relation_auto': 'OC relation of compound and phonetic: I identical; R differ only in prefix, suffix (including *-?, *-s), pharyngealisation or medial *r; O initial differs (same place); O2 initial differs (different place); V vowel differs; C coda differs; NA no reconstruction at one end',
    'morph_diff': 'what differs in the OC forms (components), with "uncertain" where brackets were removed before comparing',
    'morph_affix_detail': 'for R pairs, the affix change in detail', 'morph_affix_type': 'for R pairs, the affix type (for example suf_+ʔ, pre_-m-, phar_gained, multi)',
    'paronomastic_gloss': 'True if the definitional part of the gloss (before 从) contains the phonetic character itself',
    'duan_label': 'status of the label in Duan Yucai\'s edition: 亦聲 (kept) / 無 (dropped) / 缺段注 (no Duan text in the data); empty for rows without a label',
    'duan_phonetic': 'the phonetic named in Duan\'s text, if it differs from the Da Xu text', 'duan_phonetic_changed': 'True if Duan names a different phonetic',
    'xiaoxu_label': 'status in the Xiao Xu text for aligned entries: 亦聲 / 無 / 未对齐 (not aligned); the collation of record is data/recension_collation.csv',
    'identical_relation_type': 'for MC-identical pairs only, coded with the label visible (descriptive): L same word with an added determinative; F one sense given its own graph; C conversion; U unrelated homophone or loan; X proper name',
    'filed_under_phonetic': 'True if the compound is filed in the Shuowen section whose head is its own phonetic',
}
D['data/recension_collation.csv'] = {
    'sw_id': 'row number of the head entry (as in pairs.csv)', 'char': 'the labelled compound', 'char_codepoint': CP, 'phonetic': 'its phonetic', 'phonetic_codepoint': CP,
    'in_analysis_set': 'True / False; the 4 rows marked "False (亦 false hit)" are entries where 亦 is itself the phonetic',
    'daxu_gloss': 'the Da Xu analysis of the entry',
    'xiaoxu_reading': 'what the Xiao Xu (Sibu congkan text, checked on the scan) reads at that entry: 亦聲 (same label) / 聲 (plain phonetic) / 無聲 (no phonetic element) / 其他聲 (another phonetic) / 未找到 (entry not found) / 原书空白不清 (blank or illegible in the print) / 未見 (not seen)',
    'xiaoxu_reading_en': 'English rendering of xiaoxu_reading',
    'layer': 'result of the collation: both (label in both recensions) / daxu_only (Da Xu only) / unknown (cannot be decided)',
    'unknown_reason': 'why the layer is unknown: 新附 xinfu; juan 25 supplied from the Da Xu; blank; not seen in the scan', 'unknown_reason_en': 'English rendering of unknown_reason',
    'round': 'collation round in which the entry was read (round1, round2, round3_scan)',
    'xiaoxu_juan': 'juan (chapter) of the Xiao Xu edition in which the entry was looked up', 'xiaoxu_quote': 'the Xiao Xu wording quoted by the collator (Chinese data)',
    'note': 'collator\'s note (some in Chinese)', 'note_en': 'English rendering of the note',
}
D['data/first_sample_codes.csv'] = {
    'item': 'item number in the first blind sample (1-100)', 'sw_id': 'row number in pairs.csv (empty for the one pair not found there)',
    'phonetic': 'phonetic shown to the coder', 'phonetic_codepoint': CP, 'member': 'compound shown to the coder', 'member_codepoint': CP,
    'group': 'labelled / ordinary (never shown to the blind coder)', 'relation': 'group in the Shuowen\'s own terms (亦聲 / 聲) as recorded with the sample',
    'relation_in_pairs': 'the same according to pairs.csv', 'in_analysis_set': 'True / False / empty (pair not in pairs.csv)',
    'phonetic_gloss': 'Shuowen gloss of the phonetic as shown (structural analysis removed)', 'member_gloss': 'Shuowen gloss of the compound as shown (structural analysis removed)',
    'blind_code': 'blind semantic code, returned by a separate Claude instance that did not see the group: Y same or near-synonymous meaning; E connected by one step of extension or inference; N no visible relation; X proper name',
    'blind_confidence': 'coder\'s confidence 1 (low) to 3 (high)', 'blind_note': 'coder\'s note', 'nonblind_code': 'code of the non-blind pass (made by the Claude instance that built the dataset, knowing the group)',
    'oc_relation_auto': 'OC relation category (as morph_relation_auto in pairs.csv)',
}
D['data/author_check.csv'] = {
    'check_id': 'item number on the check sheet', 'check_type': 'passes_disagree (the two blind passes differ; all 76) / random_agreed (50 items drawn at random from the 601 on which the passes agree)',
    'phonetic': 'phonetic shown', 'phonetic_codepoint': CP, 'phonetic_gloss': 'gloss of the phonetic as shown', 'member': 'compound shown', 'member_codepoint': CP,
    'member_gloss': 'gloss of the compound as shown', 'author_code': 'the authors\' consolidated code (Y/E/N/X); each author checked separately and the judgments were consolidated into one code per item',
    'pass1_code': 'code of blind pass 1 shown on the sheet', 'pass2_code': 'code of blind pass 2 shown on the sheet',
}
D['data/ext_items_key.csv'] = {
    'sw_id': 'row number in pairs.csv', 'phonetic': 'phonetic', 'char': 'compound', 'relation': 'group in the Shuowen\'s terms: 亦聲 labelled / 聲 ordinary',
    'role': 'new (item coded for the first time) / anchor (first-sample item added to a batch as a calibration check: 5 per batch, 35 in all, each coded once in each pass)',
    'stratum': 'sampling stratum: labelled / ordinary_mc_oc (ordinary, with OC forms at both ends) / ordinary_mc_only',
    'has_mc': 'True if both ends have MC readings (False for 35 labelled entries)', 'has_oc': 'True if both ends have OC reconstructions',
    'orig_item': 'for anchors, the item number in the first sample', 'orig_code': 'for anchors, the first sample\'s blind code',
    'p1_batch': 'batch number in pass 1', 'p1_item': 'item number within the batch in pass 1', 'p2_batch': 'batch number in pass 2', 'p2_item': 'item number within the batch in pass 2',
    'phonetic_gloss': 'phonetic gloss as shown to the coders', 'member_gloss': 'compound gloss as shown to the coders',
}
D['data/duan_notes_precomputed.csv'] = {c: COUNTS[c] for c in ['section', 'comparison', 'labelled_hits', 'labelled_n', 'labelled_rate', 'ordinary_hits', 'ordinary_n', 'ordinary_rate', 'gee_OR', 'gee_CI95', 'gee_p_two_sided',
                                                              'mh_strata', 'mh_labelled_n', 'mh_ordinary_n', 'mh_OR', 'mh_CI95', 'cmh_p_two_sided', 'fisher_p_two_sided', 'note']}
D['data/duan_notes_precomputed.csv']['note'] = 'note; the rows were computed from the open Shuowen data (see README) and are used by scripts/paper_checks.py when that data is not supplied'

D['output/ext_items_key.csv'] = dict(D['data/ext_items_key.csv'])
D['output/ext_items_with_answers.csv'] = dict(D['data/ext_items_key.csv'], **{
    'p1_code': 'code returned in pass 1', 'p1_conf': 'confidence in pass 1', 'p1_note': 'coder\'s note in pass 1',
    'p2_code': 'code returned in pass 2', 'p2_conf': 'confidence in pass 2', 'p2_note': 'coder\'s note in pass 2'})
D['output/ext_codes_long.csv'] = {
    'sw_id': 'row number in pairs.csv', 'source': 'extended (677 new items) / original_100 (the 90 first-sample items that lie in the comparison frame)',
    'code1': 'code analysed: pass 1 for the new items, the first sample\'s blind code for the old items', 'code2': 'second code: pass 2 for the new items, the same blind code for the old items',
    'conf1': 'confidence of code1 (1-3)', 'conf2': 'confidence of code2 (1-3)', 'phonetic': 'phonetic', 'char': 'compound', 'relation': 'group in the Shuowen\'s terms (亦聲 / 聲)',
    'cat4': 'MC category: identical / alt_departing (tone or voicing alternation involving the departing tone) / alt_other (other tone or voicing alternation) / other; empty without MC readings',
    'paronomastic_gloss': 'as in pairs.csv', 'layer': 'recension layer of a labelled pair (both / daxu_only / unknown); empty for ordinary pairs', 'mc_relation': 'as in pairs.csv; empty without MC readings',
    'label': '1 labelled, 0 ordinary', 'near': '1 if cat4 is identical or alt_departing ("near"), else 0', 'ident': '1 if cat4 is identical, else 0',
}
D['output/ext_check_key.csv'] = {'check_id': 'item number on the check sheet', 'sw_id': 'row number in pairs.csv', 'phonetic': 'phonetic', 'char': 'compound', 'relation': 'group in the Shuowen\'s terms',
                                 'why': 'passes_disagree / random_agreed (see data/author_check.csv)', 'p1_code': 'pass-1 code', 'p2_code': 'pass-2 code'}
D['output/ext_check_sheet_blank.csv'] = {c: v for c, v in D['data/author_check.csv'].items() if c in ['check_id', 'check_type', 'phonetic', 'phonetic_gloss', 'member', 'member_gloss', 'author_code', 'pass1_code', 'pass2_code']}
D['output/ext_check_sheet_blank.csv']['author_code'] = 'blank: the cell the authors fill in'
D['output/ext_check_sheet_blank.csv']['author_note'] = 'blank: free-text note'
D['output/ext_second_answer_items.csv'] = {'batch': 'batch number (3 or 6)', 'item': 'item number within the batch', 'sw_id': 'row number in pairs.csv', 'role': 'new / anchor',
                                           'first': 'code of the first answer (the one that counted)', 'second': 'code of the second answer (not used in the main analysis)',
                                           'conf1': 'confidence of the first answer', 'conf2': 'confidence of the second answer'}
for f in ['ext_coding', 'ext_author_check', 'ext_second_answer', 'bias_reverse_scenario']:
    D[f'output/yisheng_models_{f}.csv' if f != 'bias_reverse_scenario' else 'output/yisheng_bias_reverse_scenario.csv'] = dict(MODEL)
D['output/yisheng_models_ext_author_check.csv']['tier'] = 'identity_pass1 (reference: no substitution, pass-1 codes) / author_adjudicated (the authors\' consolidated codes replace the machine codes of the 126 checked items)'
D['output/yisheng_models_ext_second_answer.csv']['tier'] = 'identity_pass1 (reference) / second_b3_b6 (second answers used in batches 3 and 6) / second_b3_only / second_b6_only'
D['output/yisheng_bias_reverse_scenario.csv']['tier'] = 'control (main test) / fold_all (all 31 labelled pairs coded unrelated counted as related) / fold_far (only the not-near ones among them)'
D['output/yisheng_bias_sensitivity_grid.csv'] = {
    'kind': 'tipping (false-positive rate in the ordinary group needed to reach a target odds ratio) / grid (corrected odds ratio at a given rate)',
    'target': 'target for the corrected odds ratio (2.0, 1.5, 1.0, or lower95=1: lower bootstrap limit 1); empty for grid rows',
    'fp_L': 'assumed false-positive rate among labelled pairs coded related', 'fp_O': 'assumed false-positive rate among ordinary pairs (grid rows)',
    'fp_O_required': 'false-positive rate among the truly unrelated ordinary pairs that brings the corrected odds ratio to the target (tipping rows)',
    'false_pos_share_of_coded_related_ordinary': 'share of the ordinary pairs coded related that would then be false positives',
    'OR_star': 'corrected odds ratio', 'OR_star_boot_lo': 'lower 95% bootstrap limit of OR_star', 'OR_star_boot_hi': 'upper 95% bootstrap limit of OR_star',
}
D['output/yisheng_summary.csv'] = {c: COUNTS[c] for c in ['hypothesis', 'comparison', 'labelled_hits', 'labelled_n', 'labelled_rate', 'ordinary_hits', 'ordinary_n', 'ordinary_rate', 'fisher_one_sided', 'note']}
D['output/yisheng_models.csv'] = {c: COUNTS[c] for c in ['hypothesis', 'outcome', 'n', 'n_phonetics', 'gee_OR', 'gee_CI95', 'gee_p_one_sided', 'glmm_vb_OR', 'glmm_vb_CI95', 'glmm_vb_z', 'holm_p']}
D['output/yisheng_models_extra_checks.csv'] = {c: COUNTS[c] for c in ['section', 'comparison', 'labelled_hits', 'labelled_n', 'labelled_rate', 'ordinary_hits', 'ordinary_n', 'ordinary_rate', 'gee_OR', 'gee_CI95', 'gee_p_two_sided',
                                                                      'mh_strata', 'mh_labelled_n', 'mh_ordinary_n', 'mh_OR', 'mh_CI95', 'cmh_p_two_sided', 'fisher_p_two_sided', 'note']}
for f in ['wangyun', 'xiaoxu']:
    D[f'output/yisheng_models_{f}_sensitivity.csv'] = {c: COUNTS[c] for c in ['variant', 'hypothesis', 'outcome', 'n', 'n_phonetics', 'labelled_hits', 'labelled_n', 'ordinary_hits', 'ordinary_n', 'gee_OR', 'gee_CI95',
                                                                              'gee_p_one_sided', 'glmm_vb_OR', 'glmm_vb_CI95', 'gee_p_two_sided']}
D['output/table5_departing_tone_members.csv'] = {'sw_id': 'row number in pairs.csv', 'char': 'labelled compound', 'char_codepoint': CP, 'phonetic': 'its phonetic', 'phonetic_codepoint': CP,
                                                 'mc_bs2014': 'MC reading of the compound', 'head_mc_bs2014': 'MC reading of the phonetic', 'shuowen_gloss': 'Shuowen gloss of the compound',
                                                 'blind_code': 'blind semantic code analysed (see ext_codes_long.csv, code1)', 'paronomastic_gloss': 'as in pairs.csv', 'layer': 'recension layer (both / daxu_only / unknown)'}
D['output/fig1_h5_forest_values.csv'] = {'label': 'row label of Fig. 1', 'kind': 'pre (pre-specified) / expl (exploratory) / sens (authors\' judgment sensitivity) / mh (within-series estimate)',
                                         'OR': 'odds ratio plotted', 'lo': 'lower 95% limit', 'hi': 'upper 95% limit', 'hits1': 'labelled pairs identical or departing-tone alternant',
                                         'n1': 'labelled pairs coded related in the comparison', 'hits0': 'ordinary pairs identical or departing-tone alternant', 'n0': 'ordinary pairs coded related in the comparison'}

rows = []
missing = []
for f in sorted(glob.glob('data/*.csv') + glob.glob('output/*.csv')):
    cols = list(pd.read_csv(f, encoding='utf-8-sig', nrows=0).columns)
    dd = D.get(f)
    if dd is None:
        missing.append((f, 'file')); continue
    for c in cols:
        if c not in dd:
            missing.append((f, c)); continue
        rows.append(dict(file=f, column=c, description=dd[c]))
print('missing:', missing)
assert not missing, missing
with open('data_dictionary.csv', 'w', newline='', encoding='utf-8-sig') as fh:
    w = csv.DictWriter(fh, fieldnames=['file', 'column', 'description'], lineterminator='\n'); w.writeheader(); w.writerows(rows)
json.dump(rows, open('../work/dictionary.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(rows), 'rows')
