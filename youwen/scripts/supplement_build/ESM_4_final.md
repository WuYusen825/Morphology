# Online Resource 4 (ESM_4.pdf)

**Article title:** What does 'also phonetic' mark? The Shuōwén's yìshēng label, homophony and derivation in Old Chinese  
**Journal:** Morphology  
**Authors:** Withheld for double-anonymous review  
**Corresponding author (affiliation, e-mail):** Withheld for double-anonymous review

**Caption:** Analysis plan for the enlarged coding, committed with a time-stamp before any batch was coded (English translation, with the log of later changes).

**Note on this translation.** The plan was written in Chinese and committed, together with the sampling script and the analysis script, before the first batch was coded; it is translated here in full (sections 1–6), followed by the record of deviations (section 7), which was kept up to date as changes were made. Numbers, rules and decisions are unchanged. Names of people and references to the internal workflow have been neutralised: "the authors" are the two authors, "the analysis assistant", "the drafting assistant" and "the coordinating assistant" are the AI assistants that took part (Claude), and "the independent review" is the internal review of the work; review documents that are not part of the supplementary material are marked as such. Chinese terms of the original are kept in parentheses where they matter. Labels such as v7, v8 and v9 are internal versions of the article draft and are kept because the plan and the log refer to them. File names refer to the working files of the project: the scripts named `ext_sample.py`, `ext_analysis.py`, `ext_author_check.py`, `ext_bias_sensitivity.py`, `ext_second_answer_sensitivity.py` and `ext_bias_reverse_scenario.py` are in Online Resource 7 (folder `scripts/`), and so is the computation of the earlier `yisheng_v7_checks.py` (in `core_models.py` and `paper_checks.py`); the prompts and the raw answers are in Online Resource 5, the codings in Online Resource 3 and the result tables in Online Resource 6. The sheet of the first sample, built by `blind_sheet_yisheng.py`, is the sheet `first_sample` of Online Resource 3.

---


# Enlarged blind coding: analysis plan (fixed before coding)

- **Date fixed**: 2026-09-30 (UTC), committed together with the sampling script and the analysis script before any coding batch was run. The time-stamp of the commit is the evidence that the plan was pre-specified; any change to this file after coding began may be written only in §7 "Record of deviations" (偏离记录) at the end.
- **Executed by**: the analysis assistant (Claude, an AI assistant working with the authors), following the authors' choice (enlarged blind coding, 扩大盲编) of 2026-09-30 06:23 on the decision card of the independent review.
- **Basis**: the independent review's proposal, `extended_coding_spec.md` (review document, not included), and the independent review's comments on drafts 2 and 3 (`draft2_review.md` §4 and `draft3_review.md` T1; review documents, not included).
- **Scripts**: sampling `ext_sample.py`, analysis `ext_analysis.py`. Both were committed in the same commit as this file; the analysis script was dry-run on random codes to confirm that it runs through (the dry-run output was not committed).

## 1 The question to be answered

Among pairs that are related in meaning, does the 亦聲 (yìshēng, "also phonetic") label still carry more homophony or \*-s (departing-tone alternation in Middle Chinese, MC)?

- (C) "same word or minimal derivation" (同词或最小派生): it will carry more, OR > 1.
- (A) "meaning-first" (意义先行): it will not carry more, OR ≈ 1.

The blind-coded sample of v7 had only 6 related ordinary pairs, so this comparison could not be made (v7 §5.2, §6).

## 2 Sampling frame and sample

### 2.1 Sampling frame (same as v7, corrected following T1 of the review of draft 3)

The frame consists of the 172 phonetics (声符) in the analysis set that still have labelled compounds (亦声字), and the 212 labelled compounds and 953 ordinary compounds (普通形声字) on them (`A` in `yisheng_v7_checks.py`). Only the phonetics (卒, 責, etc.) that have nothing but xīnfù (新附, Xu Xuan's additions) labelled compounds are not in the frame.

### 2.2 Check against the figures listed in the review proposal

| | Review proposal | Result of the check |
|---|---|---|
| Coded within the frame (original 100 items) | labelled 35, ordinary 56 | labelled 35, **ordinary 55**. Of the original 60 ordinary pairs, 1 is not in the analysis set (醒, itself a xīnfù character) and 4 are outside the frame (碎 淬 焠, 積) |
| Uncoded labelled pairs | about 177 | **177**, of which 142 pairs have MC readings for both members and 35 pairs lack MC readings |
| Uncoded ordinary pairs | 897 | **898**; of which **803** pairs have MC readings for both members |

The review proposal also states "both members must have MC readings". The outcome of the primary test is an MC relation, so:

- **Labelled group**: all of the remaining 177 pairs are coded (a complete census). The 35 pairs lacking MC readings do not enter the primary test and are used only to describe "how many of the 212 labelled compounds are semantically related to their phonetic".
- **Ordinary group**: sampled only from the 803 pairs in which both members have MC readings.

### 2.3 Sampling of the ordinary group: one change forced by the data

The default set by the coordinating assistant was "to draw 500 pairs at random, with a fixed seed, from the remaining ordinary pairs". The 500 pairs are kept here, but the draw is changed to **stratified equal-probability sampling** (分层等概率抽样), for the following reasons.

The original 100 blind-coded items were drawn from pairs "in which both members have a Baxter–Sagart Old Chinese (OC) reconstruction" (`blind_sheet_yisheng.py`). All 55 ordinary pairs originally in the frame belong to this stratum. If 500 pairs were drawn by simple random sampling from the remaining 803 pairs, then in the merged sample of the ordinary group a pair with an OC reconstruction would have a probability of being selected of about 0.65 and a pair without one of about 0.56, so the sample would no longer be equal-probability. [Note added in this translation: these two figures correspond to a draw of 500 from all 898 uncoded ordinary pairs; for a draw from the 803 pairs with MC readings they would be about 0.71 and 0.62. The argument and the design in the table below are not affected.]

The change: take the 858 ordinary pairs with MC readings as the population and a merged sample of 555 pairs (55 original + 500 new), stratified by "presence or absence of an OC reconstruction" and allocated proportionally:

| Stratum | Population | Originally coded | Newly drawn | Total | Inclusion probability |
|---|---|---|---|---|---|
| With MC, with OC reconstruction | 248 | 55 | 105 | 160 | 0.645 |
| With MC, without OC reconstruction | 610 | 0 | 395 | 395 | 0.648 |

The original 55 pairs are a simple random sample of the stratum to which they belong; adding a simple random draw from the remaining pairs of the same stratum still gives a simple random sample of that stratum. The merged ordinary group is therefore approximately self-weighting with respect to the 858 pairs, and no weighting is needed in the analysis.

- Random seeds: sampling 20260930, anchor items (锚定条目) 20260931, first batching 20260932, second batching 20260933, check sheet 20260934.
- Item list and batching: `ext_items_key.csv` (includes the group; not visible to the coding agent).

### 2.4 Expected size

- Related labelled pairs: 177 labelled pairs with MC readings × about 0.76 ≈ 134 pairs.
- Related ordinary pairs: 555 × about 0.12 ≈ 67 pairs.

Slightly more than the 60 pairs estimated in the review proposal. A rough power estimate is given in §6 of the review proposal; the interval actually obtained after coding is what counts.

## 3 Coding procedure

### 3.1 Coders

Independent LLM sub-agents (the general-purpose agent of Claude Code, of the same kind as the second coder of the original 100 items), a new instance for each batch, sharing no context with one another.

- No files are given; reading from disk and web access are forbidden; the agent only returns its answers.
- The agent cannot see the group, `yisheng_dataset.csv`, the original codes or any project file.

### 3.2 Two independent blind-coding passes

The 677 new items (177 labelled + 500 ordinary) are each coded twice:

- Pass 1 (第一次盲编) and pass 2 (第二次盲编) each re-batch and re-order the items with a different random seed. Each batch has 101–102 items: about 97 new items plus 5 anchor items, with labelled and ordinary pairs randomly mixed.
- Each pass has 7 batches, 14 batches in all. Each batch is coded by a new agent instance, so the two agents that code the same item cannot communicate with each other.
- To stay within the usage limit of the service, no more than 3 batches are run at the same time.

### 3.3 Anchor items

35 items are drawn at random from the 90 of the original 100 items that fall inside the frame, leaving out 亡/忘, which are used as examples in the instructions. Both passes use these 35 items, 5 per batch.

The anchor items are used to check whether the new coding agrees with the original blind coding. The analysis still uses their original blind-coded values (`blind_coding_sheet_llm_coded.xlsx`) and does not replace them with the new codes.

### 3.4 Prompts

- The complete prompts are stored batch by batch in `prompts/pass{1,2}_b{01..07}.txt`; these texts are exactly what was given to the agents, without any change.
- The coding instructions and the definitions of the four categories Y/E/N/X follow the original text recorded in `blind_coding_llm_protocol.md`, verbatim, including: the two examples; "original meaning only"; the handling of "None" glosses; paronomastic glosses (声训) not counting as evidence of semantic relatedness; confidence 1–3; taking the conservative choice when in doubt; and the prohibition on recalling or checking whether a compound is 亦聲.
- **One point needs to be explained**: the original protocol file recorded only the main sentences of the prompt, with two omissions marked "[…]" in the middle; the full text of the original prompt was not preserved. This time three linking sentences were written in; they do not concern the coding criteria:
  - an explanation of what is given for each item and that the structural analysis has been removed from the glosses;
  - "Work alone and give your answer directly.";
  - the header of the item table.

  The anchor items (§3.3) are there precisely to measure the effect of differences of this kind.
- **Handling of glosses**: the function `defn()` of `blind_sheet_yisheng.py` is retained, i.e. the part before the character 从 is taken and the formula 凡某之屬皆 ("all those of the class of so-and-so are ...") is removed. Only one change was made: when a gloss begins with 从 (within the frame there is only one such case, 貣 "从人求物也。从貝弋聲。"), the original function falls back to the first 40 characters of the full text, which exposes "弋聲"; this is changed to taking the text up to the first full stop.
- **Leakage check**: the sampling script asserts that none of the glosses given contains "亦聲" or "从某聲" ("X as phonetic").
- Where the phonetic is not a headword of the Shuōwén (8 phonetics, 14 pairs), the gloss is written as None, as in the original sheet.

### 3.5 Handling of the answers

- Each batch agent's answer is saved unchanged as `raw/pass{p}_b{bb}.txt`.
- Parsing rules: each line is "item, code, confidence, note"; the code is restricted to Y/E/N/X and the confidence to 1–3; item numbers must be complete and not duplicated.
- When the answer for a batch is unacceptable (missing items, duplicates, invalid codes), the whole batch is re-coded with a new agent instance and this is recorded in §7; no item-by-item repair is made.
- If the agent used any tool (reading from disk, web access), the batch is voided and re-coded, likewise recorded.

## 4 Analysis plan

### 4.1 Common specifications

- **Sample**: all coded pairs within the frame, namely the original 90 items with their original blind-coded values and the 677 new items with their pass 1 values. Pairs coded X (proper name, 专名) enter no test, as for H2 in v7.
- **Related**: coded Y or E.
- **MC categories**: the same as `cat4` in `yisheng_v7_checks.py`.
- **"Near" (近音; the outcome)**: homophonous, or a tonal or voicing alternation involving the departing tone (`identical` or `alt_departing`).
- All models are GEE (binomial, logit), clustered by phonetic, with an exchangeable working correlation structure.
  - If it does not converge or the standard error is invalid, an independence working correlation is used instead, still with robust standard errors clustered by phonetic, and this is noted in the `gee_cov` column of the results file.
  - Confidence intervals are Wald 95% intervals.

### 4.2 Primary test (the only confirmatory test)

- **Sample**: pairs coded as related (Y or E) in which both members have MC readings.
- **Model**: near ~ label, GEE clustered by phonetic.
- **Report**: the OR, its 95% confidence interval, and the p-value of the one-sided test of OR > 1.

**Decision rule** (判读), with the smallest effect of interest (SESOI, 最小关心效应) set at OR = 2 (the reasons are given in §6 of the review proposal):

| Result | Conclusion |
|---|---|
| One-sided p < 0.05, and upper confidence limit ≥ 2 | Supports (C) |
| One-sided p ≥ 0.05, and upper confidence limit < 2 | Supports (A) |
| One-sided p < 0.05, and upper confidence limit < 2 | Mixed: the excess of "near" pairs that comes with the label is statistically present but smaller than the smallest effect of interest. Write this as "a small phonetic component in addition to meaning-first", not as support for (C) |
| Otherwise (p ≥ 0.05, upper limit ≥ 2) | Still cannot be distinguished; report the interval as obtained |

### 4.3 Secondary tests (all reported, with no correction for multiple comparisons, used only for robustness and description)

- **S1**: the outcome is homophony only.
- **S2**: paronomastic-gloss items (`paronomastic_gloss`) are removed from both groups.
- **S3**: only labelled compounds common to the two editions, Dà Xú (大徐) and Xiǎo Xú (小徐), are used, with all ordinary compounds retained; the same basis as v7 Table 7.
- **S4**: within-phonetic Mantel–Haenszel pooled OR, using only phonetics that have both related labelled pairs and related ordinary pairs; the CMH p is reported.
- **S5**: the primary test is recomputed with the pass 2 values for the new items.
- **S6**: strict specification, counting only Y as related.
- **S7**: only the new items on which the two passes agree on "related or not", plus the original 90 items.
- **S8**: H2 is re-estimated on the full sample (related ~ label, GEE). It is computed once with pass 1 and once with pass 2, with the old values written alongside:
  - v7 official value: 25/33 vs 6/50, OR 22.0 [7.1, 68.0];
  - corrected for the frame: 25/33 vs 6/46, OR 20.2 [6.6, 62.1].
- **S9**: the premise of "meaning-first".
  - near ~ related + label (GEE), reporting both coefficients;
  - within the labelled group and within the ordinary group separately, compare the proportion of near pairs between related and unrelated pairs;
  - old values: v7's descriptive logit on 79 pairs, with OR 10.1 for related and OR 1.28 for the label; within groups, 14/25 vs 0/8 and 2/6 vs 4/40.
- **Description**:
  - the proportion of the 212 labelled pairs (and of the 35 of them lacking MC) coded as related;
  - the distribution of related pairs over the four MC categories;
  - the proportion coded as related in each category (corresponding to 10/13, 6/7, 1/6, 14/53 in v7).

### 4.4 Agreement

- New items, pass 1 against pass 2: κ for the four categories, κ for related/unrelated, κ for Y/non-Y, also reported separately by group, with the cross-tabulation.
- The 35 anchor items: pass 1 and pass 2 are each compared with the original blind coding, reporting the same κ values and the list of disagreements.

These κ values are all inter-LLM agreement and must not be presented as the reliability of human coders.

### 4.5 The authors' check

As decided by the authors on 2026-09-30, the authors' work is an item-by-item check (核验), not the primary coding.

- **Check sheet**: all new items on which the two passes disagree in the four-category code, plus 50 items drawn at random from the remaining new items (seed 20260934), in shuffled order, with the group not shown.
- The authors are asked to write down their own judgement first and only then look at the two passes.
- **The analysis does not wait for the result of the check**: all analyses are completed first with the blind coding.
- After the check comes back:
  - report the agreement rate and κ between the authors' judgement and pass 1;
  - if there are items on which the authors changed the judgement, carry out a further sensitivity analysis with the changed values substituted;
  - the primary test remains as in §4.2, unless the authors decide otherwise.

### 4.6 Known biases (stated up front; to be explained accordingly when the results are read)

- **The coder knows the pronunciations**: the agent is not shown pronunciations but is familiar with Classical Chinese. If it finds it easier to judge homophonous pairs as related, then "coded as related" is partly influenced by pronunciation. Conditioning on this makes "near" and the label negatively associated within the group, **which biases the OR of the primary test downward, towards (A)**.
- **"Related" is a noisy proxy for true relatedness**: (A) holds that the label is determined by true relatedness. If the coding has errors, labelled pairs coded as related are more likely than ordinary pairs to be "truly related", and truly related pairs are more often near, **which biases the OR upward, towards (C)**. S6 (counting only Y) and S7 (agreement of both passes) are used to check this.
- **Same model family**: the two passes and the original blind coding all come from the same model family, so their errors may be correlated and κ may be too high.

## 5 Outputs (all new files; no existing file is renamed or overwritten)

| File | Content |
|---|---|
| `ext_items_key.csv` | Items, group, stratum, batch and position; the original codes of the anchor items |
| `prompts/`, `raw/` | The complete prompt and the agent's raw answer for each batch |
| `blind_coding_extended_pass1.xlsx`, `blind_coding_extended_pass2.xlsx` | The two blind-coding sheets (group not shown) |
| `ext_codes_long.csv` | The two codes, the group and the MC category for the 767 coded pairs in the frame |
| `yisheng_models_ext_coding.csv` | Primary test, secondary tests and description; old values in the `note` column |
| `ext_kappa_output.txt` | κ and the anchor comparison |
| `ext_check_sheet.xlsx`, `ext_check_key.csv` | The authors' check sheet and its key |
| `ext_summary.md` | Summary of results (written after coding and analysis are complete) |

- The new values of the official counts (H2 etc.) are written only into these new files; `yisheng_models.csv`, `manuscript_checks_output.txt`, `blind_coding_sheet_llm_coded.xlsx` and others remain unchanged.
- Changes to the paper are the task of the drafting assistant.

## 6 Division of work

- The analysis assistant: sampling, coding, analysis, check sheet.
- The drafting assistant: revises v7 according to the results (§3.3, §4.3, Table 5, §5.2, §6, abstract).
- The independent review: re-checks the outputs.

## 7 Record of deviations

(Any deviation from this plan after coding began is recorded here item by item, with the time and the reason.)

- **2026-09-30 08:38 UTC, pass 1, batch 3: the same agent instance gave two answers.**
  - Course of events: the agent first returned a complete, acceptable answer of 102 lines as plain text, and then submitted a further answer using the hand-back tool. The four-category codes are identical for 76/102 items between the two answers.
  - Cause: the environment requires sub-agents to submit their results with the hand-back tool; after the first, plain-text answer the agent was prompted to use the hand-back tool, and so coded the batch again. The second answer was produced in the same context and is not independent of the first.
  - Handling rule (fixed before any analysis result was seen, and applying to all batches): **the first complete, acceptable answer of each agent instance counts.** Later answers are saved unchanged as `raw/pass{p}_b{bb}_second_answer_not_used.txt` and enter no analysis.
  - This rule requires no re-run; the "re-coding of the whole batch" in §3.5 is still used only when an answer is unacceptable.
- **2026-09-30 08:41 UTC, pass 1, batch 6: the same agent again returned a second answer (both through the hand-back tool).**
  - The agent's record shows that the environment ran the same agent a second time; the second run started afresh from the same prompt and did not see the first answer.
  - Under the rule of the previous entry, the first answer counts and the second is saved as `raw/pass1_b06_second_answer_not_used.txt`.
  - A "second independent run of the same prompt" of this kind incidentally shows how stable repeated coding by the same agent is, but it does not enter the main analysis. When the results are compiled, it appears only as a side note in `ext_kappa_output.txt`.
- **2026-09-30 08:49 UTC, a side-note passage is added to the analysis script (pass 2 batches 6 and 7 are still being coded; the official analysis has not yet been run).**
  - A few lines were added at the end of part 8 of `ext_analysis.py`: if `raw/` contains a `*_second_answer_not_used.txt`, it is compared with the first answer that counts, and the number of agreements on the four categories and κ are written into the side note of `ext_kappa_output.txt`.
  - This implements the "side note" mentioned in the previous entry; no test, sample or decision rule is changed.
- **Pass 2, batch 5: the agent added explanatory text before and after the coding lines** (for example, it coded 羌, 璥, 蜽 as X and explained that if X were limited to names of places, rivers, surnames, animals and plants, 羌 could be changed to E).
  - Under §3.5, only the acceptable coding lines are read; the explanatory text is saved unchanged in `raw/pass2_b05.txt`.
  - The codes are always taken as given by the agent and are not changed on the basis of the explanations; the difference in the scope of X is explained in the summary of results.
- **2026-09-30 08:51 UTC, two changes after the first official run (made after the results had been seen; recorded as they happened).**
  - **S6 not estimable**: when only Y is counted, only 4 pairs in the ordinary group are coded Y, none of them near; the GEE shows complete separation and gives a divergent OR of about 3×10¹³, yet the script, following the rule, judged it "supports (C)". A safeguard was therefore added to `gee()` in the script: an estimate with a coefficient of absolute value ≥ 10 or a standard error ≥ 10 is treated as not estimable. After re-running, only the S6 row changed (to "not estimable", with the Fisher p kept); all other rows and the check sheet remain identical cell for cell.
  - **Two exploratory tests added** (`tier = exploratory` in the results file; not part of the decision rule): S6 was meant to check the bias caused by the differing strength of the "related" codes (second item of §4.6); since it cannot be estimated, two other approaches are used instead: X1 uses only pairs coded E; X2 adds "whether coded Y" as a covariate among the related pairs. X3 is also added, combining S2 and S3, i.e. the core specification of v7 (common to Dà Xú and Xiǎo Xú, and free of paronomastic glosses), in order to compare with the statement in v7 that "the phonetic effect comes mainly from labels found only in Dà Xú and from paronomastic-gloss items".
- **2026-09-30 09:03 UTC, X4 and X4b added following the independent review (exploratory; not part of the decision rule).**
  - After checking the outputs, the independent review (`ext_coding_review.md` §2; review document, not included) proposed to see whether the primary test holds when only the 677 newly coded items are used: X4 is the new items alone, X4b the original 90 items alone.
  - After re-running, all other rows and the check sheet are unchanged.
- **2026-09-30 13:23 UTC, the authors' check came back; handled according to §4.5.**
  - An author returned the filled-in `ext_check_sheet_author_filled.xlsx` (saved unchanged); all 126 items are filled in, without notes, and the file does not state whether one or two authors filled it in (the author later explained this; see the correction entry of 2026-09-30 18:37 UTC at the end). The fixed columns are identical cell for cell to those of the original sheet.
  - A new script `ext_author_check.py` (`ext_analysis.py` is not changed):
    - reports, as in §4.5, the agreement rate and κ between the authors and pass 1 and pass 2, and redoes the tests after substituting the authors' judgements;
    - reproduces, with the unsubstituted data, the corresponding rows of `yisheng_models_ext_coding.csv`, identical cell for cell.
  - **Items added beyond §4.5** (added post hoc; descriptive; not part of the decision rule):
    - estimates, for all 677 items, the stratified agreement rate and κ (the disagreement stratum in full, the agreement stratum weighted by 601/50; stratified bootstrap with 2,000 replicates, seed 20260935);
    - the direction of the changes of judgement, by labelled/ordinary group;
    - which side the authors take among the items on which the two passes disagree (binomial test).
  - There is only one sensitivity analysis: all 76 disagreeing items are on the check sheet and the other new items were coded identically in the two passes, so substituting the authors' judgements for the 126 checked items gives the same result whether pass 1 or pass 2 is used as the base.
  - The primary test remains the pass 1 result of §4.2 and is unchanged.
- **2026-09-30 13:25 UTC, explanation of who did the check (superseded by the correction entry of 2026-09-30 18:37 UTC below).**
  - The previous entry noted that the sheet does not state whether one or two authors filled it in. An author replied that the check sheet had been filled in "together" by the two authors; this was recorded at the time as one joint judgment and not as the independent judgments of two persons. `ext_summary.md` §7 and the output header of `ext_author_check.py` were changed accordingly; the numbers, tests and conclusions are unchanged (after re-running, the results files are identical cell for cell; only one header line changed).
- **2026-09-30 18:31 UTC, bias sensitivity analysis (exploratory; not part of the decision rule).**
  - Source: the independent review's comments on v8 (section "Bias sensitivity analysis" of `v8_review.md`; review document, not included; relayed by the coordinating assistant): how large the miscoding of "related" would have to be, if (A) were true, to produce the observed difference in "near" pairs, set against the coding disagreements actually seen.
  - Method: a new script `ext_bias_sensitivity.py` (existing scripts unchanged), using only the existing pass 1 coding, the comparison of the two passes and the authors' consolidated judgement; there is no new coding. The model and assumptions are written at the beginning of the script: errors are independent of pronunciation, with false-positive rates fp_L and fp_O that may differ between labelled and ordinary pairs; the correction formula is self-checked on a table with known true values; bootstrap with 5000 resamples by phonetic, seed 20260936. Results: `ext_bias_sensitivity_output.txt`, `yisheng_bias_sensitivity_grid.csv`; summary §8.
  - This is a post hoc analysis made after P1 and the result of the authors' check had been seen; it is not a test fixed before the analysis. The primary test remains the pass 1 result of §4.2 and is unchanged.
  - Two items added post hoc: a weighted estimate from the authors' spot-check sample (stratified bootstrap, with the same 601/50 weights as in §4.5); and, for the other route (false negatives that depend on pronunciation), a ratio of sensitivities.
  - Two notes: under the authors' consolidated judgement the false-positive rate for the labelled group (95%) lies outside the feasible range of the model (fp_L < 75%) and is not used; for the labelled group only two cases are given, fp_L = 0 and fp_L = fp_O. The OR obtained without the false-positive model, by reclassifying directly with the design weights (7.32 [1.51, 30.98]), is extremely unstable (the ordinary near cell has only 4 weighted pairs) and runs in the opposite direction to the false-positive correction; both are given as description only.
- **2026-09-30 18:37 UTC, correction on who did the check (overrides the 13:25 entry).**
  - An author said (the author's words, translated from the Chinese: "The last one was also coded separately, then a consolidated one was handed over; in short, the later procedure is consistent with the earlier one"; relayed by the coordinating assistant at 18:21): the 126 items were checked separately by the two authors and then consolidated into one sheet. The "together" of 13:24 only meant that both authors took part; it had been recorded wrongly as "filled in one sheet together".
  - The check sheet is therefore the authors' consolidated judgment, not a joint judgment. Only the consolidated sheet is on file; each author's own sheet was not kept, and how items on which the two authors' judgments differed were settled in the consolidation is not documented. The κ is between the authors' consolidated judgment and the LLM, not agreement between the authors, and agreement between the authors cannot be computed.
  - The sheet displayed the spot-check type (column B) and the codes of the two passes (columns H and I), and the instruction page asked the authors to judge first from the glosses alone and only then look at the codes. The authors' judgment is thereby not independent of the codes; if the authors were as a result drawn closer to the codes, the false-positive rates estimated in §8 of the summary are too low.
  - Changed: `ext_summary.md` §7 and §8 (including the two English paragraphs for the paper), the output header of `ext_author_check.py` and line 2 of `ext_author_check_output.txt`, the wording of `ext_bias_sensitivity.py` and of its output, and the project records `youwen_criteria.md` §10 and `PROJECT_LOG.md` (project records, not included).
  - The numbers, tests and conclusions are unchanged: after re-running, `yisheng_models_ext_author_check.csv` and `yisheng_bias_sensitivity_grid.csv` are identical cell for cell, and the two output files differ only in wording. This is a correction of the record, not a change to the analysis; the primary test remains the pass 1 result of §4.2.
- **2026-09-30 18:45 UTC, sensitivity analysis X5 with substitution of the second answers (exploratory, post hoc; not part of the decision rule).**
  - Source: the drafting assistant (v9), relayed by the coordinating assistant at 18:29; the independent review had calculated by hand in `v8_review.md` an OR of 2.39 [1.38, 4.14] and asked for it to be reproduced with a script.
  - Method: a new script `ext_second_answer_sensitivity.py` (existing scripts unchanged). The first answers for the new items of pass 1 batches 3 and 6 (97 + 96 items; the anchor items are left unchanged) are replaced by the second answers in `raw/pass1_b03_second_answer_not_used.txt` and `raw/pass1_b06_second_answer_not_used.txt`, and P1, S1, S2, S3, S6, S8, S9, X1, X3, X4 are recomputed; two further versions replace only batch 3 and only batch 6. The two answers were not combined into a consensus, and there is no new coding.
  - Relation to the 08:38 entry above: that rule (the first complete, acceptable answer of each agent instance counts) is unchanged, and the primary test remains the result from the first answers in §4.2. The two answers that were to "enter no analysis" enter only this one exploratory analysis, separate from the main analysis. The second answer for batch 3 comes from the same context as the first and is not independent; the second answer for batch 6 is an independent re-run from the same prompt.
  - Self-check: the script first runs without substitution and reproduces the rows P1, S1, S2, S3, X3, S8, X4 of `yisheng_models_ext_coding.csv` (identical cell for cell), and checks that the first answers are identical item by item to `code1` in `ext_codes_long.csv`, before doing the substitution; two re-runs gave byte-identical output.
  - Results: primary test 71/139 vs 21/74, OR 2.39 [1.38, 4.14] (compare 73/141 vs 23/79, 2.35 [1.43, 3.86]), the same as the independent review's hand calculation; replacing only batch 3 gives 2.32 [1.42, 3.79], replacing only batch 6 gives 2.40 [1.39, 4.14]; the interpretation of S1, S2 and S3 is unchanged; X3 (exploratory) has a one-sided p of 0.0497, right at the .05 boundary. Results are in `ext_second_answer_sensitivity_output.txt`, `yisheng_models_ext_second_answer.csv`, `ext_second_answer_items.csv`; summary §9.
  - Naming: the drafting assistant and the independent review called it "S6", which is the same name but a different thing from S6 in §4.3 (only Y counted); it is recorded here as X5.
- **2026-09-30 23:29 UTC, wording correction (comment of the drafting assistant, relayed by the coordinating assistant).** In the 18:31 entry above, "not a test registered in advance" was changed to "not a test fixed before the analysis": the plan was committed before coding (7b7c249), but nothing was registered on OSF, and this project writes only "pre-specified". Only the wording was changed; the numbers, tests and conclusions are unchanged.
- **2026-09-30 23:51 UTC, reverse scenario for the bias sensitivity analysis (the independent review's S3; exploratory, post hoc; not part of the decision rule).**
  - Source: the independent review's comments on v9 (relayed by the coordinating assistant at 23:46): the tipping-point analysis in §8 considers only one direction, false positives in the ordinary group; the reverse direction asks how much of the near-pairs difference remains if the 31 labelled pairs coded as unrelated are counted as related on the strength of the label itself and merged into the related group. The independent review calculated by hand from the counts in Table 8 an OR of about 2.17.
  - Method: a new script `ext_bias_reverse_scenario.py` (existing scripts unchanged); no new coding. First, without merging, it reproduces P1 and S1 of `yisheng_models_ext_coding.csv` (identical cell for cell); then it merges all 31 pairs into the related group; it also computes a least favourable variant (merging only the 23 of them that are not near). There are no random numbers, and a re-run gives identical output. Results: `ext_bias_reverse_scenario_output.txt`, `yisheng_bias_reverse_scenario.csv`; one sentence at the end of summary §8.
  - Results: with all merged, near 81/172 vs 23/79, GEE OR 2.00 [1.23, 3.26], one-sided p 0.0026, pooled odds ratio 2.17 (the independent review's figure); least favourable variant 73/164 vs 23/79, 1.76 [1.11, 2.80]; by the rule both still support (C), with lower interval limits above 1, but the point estimate falls to about 2.
  - This is a post hoc analysis made after P1 and the result of the authors' check had been seen; it is not a test fixed before the analysis. The primary test remains the pass 1 result of §4.2 and is unchanged.
