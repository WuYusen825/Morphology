# Paper outline v0.1: Xu Shen's *yìshēng* label and derivation

**Topic:** candidate question 2, chosen by Qu on 2026-09-24. Is Xu Shen's *yìshēng* 亦聲 label an implicit native diagnostic of derivation?
**Target journal:** *Language and Linguistics* (SSCI, diamond open access, English). Fallback: *Journal of Chinese Linguistics*. See `topic_and_journal.md` §7.
**Status:** first outline, 2026-09-24, written by the topic thread. This file owns the paper's section numbering; other files should follow it.
**Note for Qu:** please return the blind coding sheet before opening `outline_support/`, which names individual 亦聲 items.

**Where the parts live**
- **Background:** `literature_review.md` (v0.2), from the bibliography thread. It becomes §2 and already follows this outline's numbering and hypotheses.
- **Data and statistics:** owned by the pilot thread. Files: `yisheng_dataset.csv`, `yisheng_summary.csv`, `yisheng_daxu_xiaoxu.csv`, and `youwen_criteria.md` §6b–6c.
- **Exploratory numbers quoted here:** `outline_support/exploratory_checks.py`, with output in `outline_support/exploratory_checks_output.txt`.
  - They are machine-coded and have not been checked by a person.
  - They were used only to decide what the paper should test and how. None of them is a result yet.

---

## 0. The paper in five sentences

1. The Dà Xú recension marks 227 head entries as *yìshēng*, meaning "the meaningful component is also the phonetic". Of these, 212 are Xu Shen's own once false hits and Xu Xuan's additions are removed. The tradition has mostly debated where these characters belong among the six scripts. Wang Yun (1837) came closest to a claim about the words: one of his three kinds of *yìshēng* is the 分別文, a new graph for a word or for one sense of it. But he gave no counts, and no one has tested his claim against the sound relation between the two words.
2. We test whether the label covaries with independent phonological and semantic evidence of derivation. The comparison is between every labelled compound and the ordinary compounds built on the same phonetics.
3. **Expected finding**, from the exploratory counts:
   - labelled characters are far more often homophonous with their phonetic character (about 35% against 15% at the Middle Chinese level);
   - when the two differ only in tone, the labelled character is more often the departing-tone member, that is, the *-s derivative;
   - apart from that, labelled pairs are no more often related by regular affixes than ordinary pairs.
4. **Expected interpretation:** Wang Yun was right, and his claim can be made more precise. *yìshēng* marks the same word, or a minimally derived one, under a new graph: Wang's 累增字 and 分別文, conversion, and *-s derivatives. It does not mark affixal derivation in general.
5. **Contributions:**
   - the first population-level, phonologically controlled test of Wang Yun's claim that *yìshēng* includes differentiated graphs;
   - a three-way distinction (graphic differentiation, conversion, affixal derivation) that states Wang's category in morphological terms and separates it from derivation by affixes, which the morphology literature treats as the default;
   - an answer to the challenge to Arad's word-derived/root-derived diagnostic in Rasin, Preminger & Pesetsky 2024 [E12].

Sentences 3 and 4 state what we expect, not what we have shown. The paper's claims are fixed only after the confirmatory analysis in §3.6. §8 below says how the argument changes if the confirmatory results differ.

## Working title and abstract plan

- **Working title:** "What does 'also phonetic' mark? Xu Shen's *yìshēng* label, homophony and derivation in Old Chinese"
- **Alternative:** "Testing a native diagnostic of derivation: the *yìshēng* label of the *Shuōwén jiězì*"
- **Models for form and length:**
  - Sagart & Baxter 2012 [C8] and Mei 2012 [C7], both in *Language and Linguistics* 13(1);
  - Nohara 2023, *Language and Linguistics* 24(2): 325–344;
  - Schuessler 2024, *Language and Linguistics* 25(1): 80–122.
- **Planned length:** about 12,000 words including references. Check *Language and Linguistics*'s current author guidelines before drafting; its length limit has not been verified yet.

**Abstract (about 200 words), in seven moves:**
1. Native labels are a neglected source of evidence for Old Chinese morphology.
2. The question.
3. Data: every *yìshēng* entry against the ordinary compounds on the same phonetics, at both Middle Chinese (MC) and Old Chinese (OC) level.
4. Method: within-series comparison, mixed-effects models, and blind double coding of meaning.
5. Main numbers, filled in after the confirmatory analysis.
6. Interpretation: graphic differentiation plus *-s derivation.
7. Implications for *yòuwén* and for theories of roots and words.

---

## 1. Introduction (about 1,200 words)

This section argues four things.

**1. The native evidence has a gap.** Historical phonology already accepts native evidence for Old Chinese morphology:
- tone-change readings in the commentaries (破讀; Jacques 2022 [C12]);
- the structure of phonetic series (Sagart & Baxter 2012 [C8]).

It has never tested Xu Shen's own structural labels in the same way.

**2. *yìshēng* is the natural test case.** It is the one place where Xu says explicitly that a component is both meaningful and phonetic. If Xu was sensitive to derivational relatedness, his labels should covary with regular sound relations between the two words. Wang Yun already proposed that one kind of *yìshēng* is the differentiated graph (分別文) [A11, quoted through B14]. The paper turns his proposal into predictions that can be tested.

**3. One label, three relations.** The section opens with three pairs that all carry the label:
- 政 "to govern" / 正 "correct" are identical (MC tsyengH), and Xu glosses 政 simply as 正也;
- 殯 "to lay out the encoffined dead" / 賓 "guest" differ only in tone (MC pjinH / pjin);
- 貧 "poor" / 分 "to divide" differ in the initial and in the rhyme (MC bin / pjun), although Xu's gloss 財分少也 ties the meanings closely.

This is the puzzle the paper sets out to solve.

**4. Design and payoff.**
- The design uses a population rather than examples: the comparison is made within phonetic series, at both MC and OC level.
- It gives the answer in brief and states one contribution for each of the three literatures.
- It ends with a road map.

## 2. Background (about 2,500 words): uses `literature_review.md` §2.1–2.5

The bibliography thread's draft becomes this section, keeping its numbering.

**The section must establish three gaps and one baseline:**
- **Gaps:**
  - *xùngǔ* treats *yìshēng* as a question of classification. Even Wang Yun's typology, which ties one kind of *yìshēng* to differentiated graphs, classifies characters without counts or phonological tests;
  - historical phonology uses native evidence but not Xu's labels;
  - morphological theory has a contrast between word-derived and root-derived formation, but its diagnostic is contested.
- **Baseline:** some sound–meaning systematicity is expected within any phonetic series even without derivation (Monaghan et al. 2014 [E7]; Dingemanse et al. 2015 [E8]; Meng, Wan & Kit 2025 [C16]). Effects must therefore be measured against the ordinary compounds on the same phonetics.

**Status of the review.** Version 0.2 of the review (2026-09-24) has made every change this outline asked for:
- Wang Yun's 分別文 and 累增字, and his three kinds of *yìshēng*, in §2.1, with Li Guoying, Jiang Zhiyuan, Xu Shushi [F1] and Li & Guo 2019 [B14];
- the path from 227 labelled entries to the 212 analysed;
- corrected example pairs in §2.2, all taken from outside the blind coding sheet;
- a descriptive §2.4, with the answer to Rasin et al. 2024 moved to §5.2 below;
- the hypotheses of §3.5 in §2.5.

Wang's "three kinds" passage is quoted second-hand, through Li & Guo 2019 [B14], until the 1837 text can be read. It must be checked against the original before submission.

## 3. Data and method (about 2,500 words)

### 3.1 Text and population

**Argues:** the population is the complete set of Xu Shen's own *yìshēng* entries, defined by explicit rules that can be reproduced.

**Text**
- The digital edition is shuowenjiezi/shuowen (Apache-2.0): 9,833 head entries, with Dà Xú fǎnqiè and Duan's emended text.
- Every example cited in the paper must be checked against two print editions:
  - the 1963 Zhonghua facsimile of Dà Xú;
  - the Shanghai guji edition of Duan.

**Count, step by step (provisional)**

| Step | Entries |
|---|---|
| Head entries whose gloss contains the formula (`youwen_criteria.md` §6b): 224 found automatically, 3 resolved by hand (從, 𠔁, 兩) | 227 |
| Minus four false hits: here 亦 is itself the phonetic (the formula reads 从X，亦聲) | 223 |
| Minus eleven further 新附 characters added by Xu Xuan (one of the four false hits is also 新附) | **212 entries, on 172 phonetics** |

The characters excluded at each step are listed in `outline_support/README.md`.

**Caveats on the count**
- **How 新附 were found.** The list is heuristic: entries at the end of a radical that have no Duan text. This rule finds 398 entries across the whole book, which is close to the roughly 400 新附 usually counted. It must still be checked on the facsimile, where the 新附 are printed separately.
- **Two special cases.** 否 is genuine: Duan keeps it under 不. 𠮱 under 亏 is a duplicate, which Xu Xuan himself notes.
- **Also excluded:** the two formulas found inside variant-graph entries (𠨮, 㾊) and the 省聲 entries.
- **Differences from earlier counts.** Hsu 2005 [F2] counts 267 across three versions. We read the difference as the union of the recensions (see H3).

**Wang Yun's third kind.** 40 of the 212 entries are filed in the section headed by their own phonetic, as 從 is filed under 从. On the review's reading (§2.1), these are Wang's 分別文之在本部者.
- For these 40 the label follows from Xu's filing system. The section head is by definition the meaningful component, so a character filed under its phonetic must be "X, and X is also the phonetic".
- No ordinary compound (聲) in the dataset is filed under its own phonetic.
- The main analyses are therefore run twice: on all 212, and on the 172 labels that are Xu's independent judgement. H4 compares the two groups.

### 3.2 Comparison group and matching

- **Comparison group:** every ordinary compound (X聲) on the same phonetics, after the same exclusions: 1,016 entries.
- **Two views:**
  - all phonetics;
  - matched phonetics only, meaning those with at least one analysable member of each kind: 121 at MC level, 42 at OC level.
- **Main model:** a mixed-effects logistic regression with a random intercept for each phonetic. It uses all the data but compares members within a series.
- **Why this baseline:** phonetic series are phonologically constrained. Homophony with the phonetic is more likely inside a series than between random pairs, so the right baseline is the unlabelled members of the same series.

### 3.3 Phonological variables

**Argues:** the primary test belongs at the Middle Chinese level.

**Middle Chinese (primary test)**
- **Source:** the Guangyun position of each character, matched to its Dà Xú fǎnqiè through tshet-uinh and written in BS 2014 MC notation.
- **Coverage:** 177 of 212 labelled entries and 917 of 1,016 unlabelled ones, about 89%.
- **Variables:**
  - identical syllable;
  - alternation in tone and/or in the voicing of the initial, and nothing else;
  - direction: which member carries the departing tone.
- **Why MC comes first:**
  - its coverage is more than three times that of the BS Old Chinese forms, which exist at both ends for only 320 of 1,228 pairs (26%);
  - MC readings do not depend on reconstructions built partly from phonetic-series evidence, which removes most of the circularity problem;
  - the two relations at issue, identity and the departing tone that reflects *-s, are both visible at MC level (Mei 2012 [C7]; Jacques 2016 [C11]; Zhang 2022 [C13]).

**Old Chinese (secondary test)**
- **Main system:** BS 2014 (cddb `D_ocbs.tsv`), used to type affixes.
  - Categories follow `scripts/morph.py`: I; R, split by affix; O; O2; V; C.
  - OC is needed for prefixes (*s-, *N-, *m-) and for the type A/B contrast, which MC does not show directly.
- **Robustness check:** Schuessler 2007 [C6].
- **Which OC relations count as regular:** 孟蓬生 2001 [B5], a check against the Chinese word-family literature.

### 3.4 Semantic variables

**Argues:** the semantic test cannot rest on Xu's glosses alone, because Xu wrote the gloss and assigned the label in the same act.

**The confound**
- The definition part of the gloss (before 从) contains the phonetic character itself in 58 of 212 labelled entries (27.4%), against 11 of 1,016 unlabelled ones (1.1%).
- Examples: 政 正也, 枰 平也, 劑 齊也.

**Measures**
1. **Blind double coding.** Two coders rate the semantic relation between each member and its phonetic:
   - **Y:** same meaning or near-synonym;
   - **E:** one step of extension;
   - **N:** no relation;
   - **X:** proper name.

   The coding uses the pilot thread's 100-item sheet (40 labelled, 60 unlabelled, with Xu's structural analysis removed). Agreement is reported as Cohen's κ.
2. **Sensitivity check.** Every H2 test is run both with and without paronomastic glosses.
3. **External check.** Compare against the word-family field in Schuessler 2007, and check a sample against Wang Li 1982 [A8].
4. **Relation type for identical pairs.** Every pair that is identical at MC level gets one of four codes:
   - **Same word, new graph** (累增字);
   - **Sense specialization written with an added determinative** (分別文);
   - **Category change** (conversion);
   - **Unrelated homophone** (phonetic loan).

   This coding is the evidence for §5.1.

### 3.5 Hypotheses, and where they depart from the review

| Here | Hypothesis | Relation to review §2.5 |
|---|---|---|
| **H1a** Homophony | Labelled characters are homophonous with their phonetic character more often than unlabelled members of the same series. | New; split out of review H1 |
| **H1b** Affixal regularity | Among non-identical pairs, labelled characters differ from the phonetic by a regular affix or alternation (*s-, *N-, *m-, *-s, *-ʔ, voicing, A/B, *r) more often than unlabelled ones. | Review H1 without identity |
| **H1c** Direction | Among pairs that differ only in tone and/or voicing, the labelled character is the departing-tone member (*-s) more often than in unlabelled pairs. In other words, the label picks out the derivative, not the base. | New |
| **H2** Semantic inclusion | The meaning of a labelled character includes that of its phonetic (Y or E) more often than for unlabelled members, and the difference survives the removal of paronomastic glosses. | Review H2, with the controls of §3.4 |
| **H3** Label stability (exploratory) | Items on which Dà Xú, Xiǎo Xú and Duan disagree differ from stable items on H1a and H2. The prediction is two-sided. | Review H3, rescoped |
| **H4** Wang Yun's third kind (exploratory) | The 40 labelled characters filed under their own phonetic differ on H1a and H2 from the 172 labels that are Xu's independent judgement. The prediction is two-sided. | New; from Wang Yun, via review §2.1 |

**Why H1 is split and H3 rescoped** (adopted in review v0.2)

**1. Identity is not an affix.**
- Review H1 counts identical pairs and affixal pairs together.
- The exploratory data show that the two behave in opposite ways: identity is strongly favoured, affixes are not.
- Lumped together, they give only a modest effect: 55% against 38%, and only 57% against 46% within series.
- That modest figure hides both the main finding and its explanation.

**2. Direction is where derivation shows.**
- A derivational reading predicts more than a sound difference. It predicts which member carries *-s.
- Once the *-s-derivative cases are removed, the rest of the MC alternations are at baseline: 14.9% against 14.6%.

**3. H3 can only be partly tested.**
- **Xiǎo Xú coverage is limited.** So far only 70 of Xu's 227 items can be compared reliably with the Xiǎo Xú text (58 labelled in both, 12 in Dà Xú only). There are also 10 items that only Xiǎo Xú labels. Juan 25 of the 繫傳 was supplied from Dà Xú and must be excluded.
- **Duan's layer is complete but not independent.** Duan often follows Xiǎo Xú: 7 of the 10 items only Xiǎo Xú labels are among Duan's additions.
- **So H3 stays exploratory**, and the paper does not claim that the unstable items fall "between" the two groups, as the review expects.

**4. The review's §2.4 prediction should be refined.**
- The review predicts that *yìshēng* compounds are word-derived and *yòuwén* series root-derived.
- The data point to a finer contrast. What distinguishes *yìshēng* is the same word, or a zero-derived word, under a new graph. That is word-based, but mostly not affixal.

**Exploratory counts**

These are machine-coded and computed on all 212 labelled entries against 1,016 unlabelled ones. They are not results.

| Test | Labelled | Unlabelled | One-sided p |
|---|---|---|---|
| H1a: identical at MC, all series | 63/177 (35.6%) | 141/917 (15.4%) | 2.7e-9 |
| H1a: identical at MC, 121 matched series | 50/148 (33.8%) | 130/839 (15.5%) | 5.2e-7 |
| H1a: identical at OC (BS), all series | 15/60 (25.0%) | 14/260 (5.4%) | 2.4e-5 |
| H1b: OC affix-only difference, among non-identical pairs | 18/45 (40.0%) | 86/246 (35.0%) | 0.31 |
| H1b: the same, 31 matched series | 13/33 (39.4%) | 40/86 (46.5%) | 0.82 |
| H1b: MC tone/voicing alternation, among non-identical pairs | 33/114 (28.9%) | 157/776 (20.2%) | 0.025 |
| The same, with the *-s-derivative cases removed | 17/114 (14.9%) | 113/776 (14.6%) | 0.51 |
| H1c: labelled member has departing tone, among alternating pairs | 16/33 (48%) | 44/157 (28%) | 0.02 |
| H1c: departing-tone member, all series | 16/177 (9.0%) | 44/917 (4.8%) | 0.023 |
| H1c: the same, 121 matched series | 15/148 (10.1%) | 43/839 (5.1%) | 0.018 |
| Gloss contains the phonetic character (H2 confound) | 58/212 (27.4%) | 11/1,016 (1.1%) | n/a |
| H4: identical at MC, labels filed under their own phonetic vs other labels | 9/34 (26%) | 54/143 (38%) | not tested |

The 16 labelled departing-tone derivatives, among them 殯/賓, 琀/含 and 坪/平, are listed in `outline_support/README.md`.

Among pairs that differ only in tone or voicing, the reverse direction (the phonetic carries the departing tone) occurs 5 times for labelled pairs and 15 times for unlabelled ones.

### 3.6 Statistical analysis

**Confirmatory models (one for each hypothesis H1a–H2):**
- **Form:** logistic regression of the outcome on the label, with a random intercept for each phonetic.
- **Covariate for H1:** the semantic code.
- **Covariate for H2:** the phonological relation.
- **Correction:** Holm correction across these five tests.

**Descriptive statistics:** matched-series Fisher tests.

**Handling the exploratory look**
- The hypotheses were refined after an exploratory look at the same population. The paper says so.
- Because the population is finite and complete, no data can be held out. The mitigations are:
  1. the models are fixed in this outline before the human-verified coding exists, and that verified coding is new data;
  2. every test is reported, including the null results;
  3. the Duan and Xiǎo Xú layers are reported as partial replications.

**Effect sizes** are reported as odds ratios with 95% intervals, not only as p-values.

### 3.7 Reliability and textual checks

1. **Semantic coding.** Report κ for the blind semantic coding. Qu is the second coder.
2. **Hand check of machine categories.** Check by hand every machine-assigned MC and OC category for the labelled pairs, plus a random 20% of the unlabelled pairs.
3. **Facsimile check.** Check the 15 excluded entries and every cited example against the facsimiles.

## 4. Results (about 2,500 words; tables planned now, numbers filled in later)

**Argues:** the label tracks homophony and the direction of *-s, not affixal derivation in general, and it survives the controls. Wording will be adjusted to the confirmatory numbers.

| § | Content | Table or figure |
|---|---|---|
| 4.1 | Population, exclusions, coverage at MC and OC level | Table 1: the count path of §3.1, with coverage |
| 4.2 | H1a homophony | Table 2: MC and OC identity by label, all series and matched. Figure 1: rate of identity for each phonetic, labelled against unlabelled members |
| 4.3 | H1b affixes among non-identical pairs | Table 3: OC categories R (by affix), O, O2, V, C by label |
| 4.4 | H1c direction of *-s | Table 4: direction of tone difference by label, with the list of derivatives |
| 4.5 | H2 semantic inclusion, with and without paronomastic glosses; relation types among identical pairs | Table 5: semantic code by label. Figure 2: semantic relation crossed with phonological relation, by label |
| 4.6 | H3 label stability and H4 Wang's third kind (both exploratory) | Table 6: Dà Xú, Xiǎo Xú and Duan agreement, with MC relation. Table 7: labels filed under their own phonetic against other labels |
| 4.7 | Case studies | 殯/賓 and 琀/含 (*-s derivatives), 政/正 and 功/工 (identity), 貧/分 (labelled in Dà Xú but 分聲 in Xiǎo Xú), and one unlabelled affixal pair as contrast |

**A preliminary H3 observation for §4.6 (small numbers):**
- Duan removes the label from 42 of Xu's 212 entries and adds it to 42 others.
- The entries he removes are not less homophonous. Their rate of MC identity is 14/34 (41%), against 49/143 (34%) for entries labelled by both Xu and Duan.
- Duan's text gives 旄 as 毛聲 and 禬 as 會聲, yet his notes on both entries call them 形聲包會意.
- This suggests that his emendations follow his own theory, not the degree of relatedness. It must be verified by hand before it goes in the paper.

## 5. Discussion (about 2,500 words)

### 5.1 What *yìshēng* marks

**Argues:** the label picks out a new graph for the same or a minimally derived word. This confirms Wang Yun's observation and goes beyond it in two ways. The relation is the label's main business, not one kind among three. And part of it is derivational (*-s), which Wang's graphic categories do not distinguish.

- **What the label covers:**
  - Wang Yun's 累增字 (the same word, with a determinative added);
  - his 分別文 (one sense given its own graph);
  - conversion;
  - *-s derivatives such as 殯 and 琀, where the labelled character is the derived member.
- **What it does not cover:** it does not pick out the wider class of affixal relations that runs through the phonetic series as a whole.
- **Link to Boltz's account of writing:** this matches Boltz's account of determinative addition [D2]. A graph extended to write a related word is disambiguated by a signific, so the phonetic is the graph of the base word.
- **Xu's label as evidence:** the label shows that Xu recognized this configuration as distinct from the ordinary phonetic compound.
- **Wang's structural criterion (H4, if the exploratory pattern holds):** filing under the phonetic's own section does not pick out the homophonous pairs. In the exploratory counts these labels are, if anything, less often homophonous (26% against 38%). So Wang's third kind is a fact about Xu's filing system, while the relation Wang saw runs through the label as a whole.

### 5.2 Morphological theory

**Argues:** the Chinese case separates relatedness from affixation, and it answers the objection to Arad's diagnostic.

**1. Writing records conversion.**
- Old Chinese has no inflection that would expose zero derivation.
- The script records conversion and sense specialization that the phonology leaves unmarked.
- So graphic evidence can reveal a kind of derivation that is otherwise hard to see.

**2. Answer to Rasin et al. 2024 [E12].**
- **Their challenge:** Rasin, Preminger and Pesetsky show that Arad's correlation between unpredictable meaning and root-derived status does not hold in Hebrew.
- **How our design differs:** we never classify items by semantic predictability. The classification is Xu's label, which is external to the analysis. Entailment is only one outcome among several.
- **An independent diagnostic:** direction (H1c) gives a test that does not use meaning at all.
- **What the case shows:** relatedness to an existing word can be identified without Arad's semantic diagnostic, and it covaries with phonological identity and with *-s.

**3. Word-based morphology fits the results better.**
- The units that pattern are words and their graphic or derivational families. The findings are phrased in those terms (Aronoff 2007 [E1]; Hathout & Namer 2019 [E9]; Bonami & Strnadová 2019 [E10]).
- Abstract roots would be the alternative unit of description, but they are not what patterns here.
- Bobeck 2025 [E11] on Classical Arabic is a parallel case to consider.

### 5.3 Consequences for *yòuwén* and 聲符示源

**Argues:** the phonetic "carries meaning" in two different ways, and the *yòuwén* tradition runs them together.

- **Where the effect is strong:** when the phonetic writes the same word. This is where the labelled cases concentrate.
- **Where it is weak:** elsewhere in the series, sharing of meaning is at the level of phonaesthemes or systematicity, not derivation (Kwon & Round 2015 [E5]).
- **The consequence:** a statement like 凡从某聲皆有某義 mixes the two. This gives the "character standing for word" (以字代詞) critique (Chen 2021 [B1]) a quantitative basis.

### 5.4 Why the recensions and Duan disagree

This section depends on H3. Duan's emendations follow his theory of 形聲包會意 (Xu Shushi 2024 [F1]). Variation in the label is therefore partly editorial. This limits what any single recension can show, and it explains the count of 267 in Hsu 2005.

## 6. Limitations (about 600 words)

1. **Coverage of the OC data.** Only 26% of pairs have BS reconstructions at both ends, and Schuessler 2007 stands in for Zhengzhang. The MC-first design reduces both problems, but the affix typing in H1b rests on a small subset.
2. **Possible circularity.**
   - BS draws partly on phonetic-series evidence.
   - Comparing within series controls for this in part.
   - MC readings carry the main tests.
3. **The texts used.**
   - The digital Dà Xú and Duan texts: every example is checked on the facsimiles.
   - The Xiǎo Xú e-text has gaps.
   - 新附 entries were identified by a heuristic.
4. **The MC readings.**
   - They are Guangyun positions matched to Dà Xú fǎnqiè, so they are later than Xu Shen.
   - Tone-change readings are accepted as evidence of morphology (Jacques 2022 [C12]), but some may be later innovations.
5. **The semantic coding.** It is a judgement, which is why it is double-coded and reported with κ.
6. **Exploratory refinement** (see §3.6).

## 7. Conclusion (about 400 words)

- **Answer to the question:** yes and no. *yìshēng* is a reliable native marker of the same word under a new graph, and of *-s derivatives. It is not a marker of affixal derivation in general.
- **Consequences:** it names the consequences for Old Chinese morphology, for *yòuwén*, and for word-based morphology.
- **Further work:** the same test applied to 讀若 and 聲訓 glosses, and to Duan's 之言 glosses, which were candidate question 3.

## 8. If the confirmatory results differ

- **If H1a holds but H1c does not:** the paper becomes a paper about graphic differentiation. The claim is then that *yìshēng* marks graphic differentiation of one word, and that Xu's label and Wang Yun's categories describe the same thing. The morphology section shrinks to the conversion argument.
- **If H1b turns out positive with verified affix typing:** the review's original framing (*yìshēng* as a diagnostic of affixal derivation) comes back, with identity reported alongside it.
- **If H1a fails after hand checking:** the paper reports a null result for a native diagnostic. This is still publishable in *Language and Linguistics* if the design is clean, but less attractive. JCL becomes the better target.

## 9. Reviewer objections to prepare for

1. **"The label is about graphs, not words."**
   - We test covariation with phonology built independently of the label (Guangyun; cddb).
   - The claim is limited to that covariation.
2. **Circularity of BS reconstructions.**
   - The main tests use MC.
   - The comparison is made within series.
   - BS is used only to type affixes.
3. **Circularity of the glosses.** Blind coding with the structural analysis removed, a check with and without paronomastic glosses, and an external source (Schuessler).
4. **Homophony by chance inside a series.** The unlabelled members of the same series are the baseline, and the models include a random effect for each phonetic.
5. **The text itself.** Checks against the facsimiles, the list of exclusions, and a comparison of the recensions.
6. **The tests were chosen after looking at the data.** We say so, fix the models before verification, report every test, and use Holm correction.
7. **"Identity is not derivation."** Agreed: the paper's claim is calibrated to exactly that point (§5.1–5.2).
8. **Why not a larger lexicon?** The population is complete. The limit is what Xu labelled, not a sample.
9. **"Wang Yun already said this."** He proposed it as one kind among three, without counts or phonology. We test it on the whole population, find that it is the label's main business, and show which part of it is derivational (*-s).

## 10. What the pilot thread is asked to add to the data

These requests go to the pilot thread through the coordinator. The topic thread does not edit the pilot's files.

1. **Remove four false hits.** Take the four entries listed in `outline_support/README.md` out of the 亦聲 group, because in each 亦 is the phonetic. Then add the three that are not 新附 to the 聲 group under the phonetic 亦.
2. **Flag the 新附 entries.** Flag Xu Xuan's 新附 across the dataset and exclude them from the main analysis. `outline_support/exploratory_checks.py` shows the heuristic used here, and the flags should then be checked on the facsimile.
3. **Add MC relation variables** as the primary phonological variables: identical, tone/voicing alternation, and direction.
4. **Stop merging I and R.** In `yisheng_stats.py`, report identity and affixal relations separately, and split R by affix.
5. **Flag paronomastic glosses.**
6. **Add the Duan and Xiǎo Xú layers.**
   - Add Duan's label as a column.
   - Add the items that only Duan or only Xiǎo Xú label as extra rows, with their phonetics. Most of them are missing now, because Xu analyses them as 會意.
7. **Code the identical pairs.** Give every MC-identical pair a relation type: 累增字, 分別文, conversion or loan. This should ideally be double-coded.
8. **Fit the models.** Run the mixed-effects models of §3.6 once the verified coding exists.
9. **Flag Wang Yun's third kind.** Mark the labelled entries filed in the section headed by their own phonetic (40 of 212; the Shuowen data's `radical` equals the phonetic).

## 11. Open checks

- **JCL contents.** The contents of *Journal of Chinese Linguistics* for 2022 and 2024–2026 were read through the CUHK Press page. There is no article on *yìshēng*, *yòuwén* or the *Shuowen*. The 2023 volume could not be read reliably.
- **A source to verify.** Baxter & Sagart, "Response to Ho Dah-an", JCL, January 2025 issue, is relevant to how robust BS 2014 is (§6). It appears in the CUHK Press contents listing, but its volume and pages have not been verified, so it is not cited yet.
- **The Korean recension study** (KCI ART002078031) is unreachable from here.
