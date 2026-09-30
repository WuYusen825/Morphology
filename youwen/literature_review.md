# Literature Review (draft v0.3)

**Paper topic.** What does Xu Shen's label *yìshēng* 亦聲 ("also phonetic") record, and can a native analyst's classification serve as evidence of derivation where derivational morphology is covert? The paper compares all 212 labelled entries of the Dà Xú recension with the 953 ordinary phonetic compounds on the same 172 phonetics.

**Target journal:** *Morphology* (Springer; Qu, 2026-09-29). Its SSCI status is not yet confirmed.

**Status:** v0.3, 2026-09-30. The text below is Section 2 of the v7 paper ([`manuscript/yisheng_paper_v7.md`](manuscript/yisheng_paper_v7.md)), copied unchanged; if the two ever differ, the paper is authoritative. Sections 2.1–2.3 were rebuilt by the v7 literature thread from the OCR Markdown in Release `literature` (and, for Wang Yun, from the scans of the *Shìlì*), then integrated into the paper by the lead thread. What was read, and how, is in [`literature_review_access_log.md`](literature_review_access_log.md) §16. Bibliographic corrections are in [`bibliography.md`](bibliography.md) (entries marked "v7 核对（2026-09-30）"). In-text citations carry no page numbers (Qu, 2026-09-29).

Changes from v0.2 (2026-09-24/25, about 5,900 words, organised by the outline's hypotheses; readable in Git history, e.g. commit `b055500`):
- v0.2 surveyed the literature hypothesis by hypothesis. v0.3 is the paper's argument in about 1,470 words: native analyses (2.1), what a derivation would leave in the sound (2.2), whether a label on a graph can bear on words, with Arad's diagnostics, Rasin et al.'s critique and paradigm-based relatedness (2.3), and four accounts with their predictions (2.4, Table 1).
- Citations were checked again against the Release `literature` Markdown or the scans. The exceptions are listed in access log §16.3: Hsu (2005) was read only in its abstract, Sagart (1999) only through its table of contents, and Wang Li (1982) is cited through Zeng (2002). In-text citations carry no page numbers.
- Duan Yucai's counts are now by head entry and come from a result file: 形聲包會意 in 128 head entries, 203 with the four related wordings (`yisheng_models_v7_checks.csv`). The v6 paper's "140 times" had no source and is dropped.
- Li Guoying's statement that a differentiated graph inherits its source's reading now grounds the meaning-first account (A).
- Works that v0.2 discussed but the paper does not cite (for example Meletis 2020, Wang Ning's theory of character configuration, Chen Xiaoqiang 2021, Huang et al. 2022) remain in `bibliography.md`.

Reference codes in square brackets after each entry point to `bibliography.md`.

---

## 2 Background

### 2.1 Native analyses: from Duan Yucai to Wang Yun

In the Dà Xú recension, 227 head entries carry the formula 从A从B，B亦聲; Section 3.1 explains why 212 are analysed. Duan Yucai (1815) read the label as marking a graph whose phonetic also contributes meaning: "whenever [Xu] says 'also phonetic', the character is a meaning-compound that is at the same time a phonetic compound" (凡言亦聲者，會意兼形聲也). He also thought Xu had used it too sparingly. 論 'discuss' "should read" 侖亦聲, and 128 characters are "phonetic compounds containing a meaning-compound" (形聲包會意), 203 with related wordings. The label was thus the visible edge of the *yòuwén* 右文 principle, recorded since Shen Kuo (ca. 1090/2016), that characters sharing a phonetic mostly, or in Duan's bolder formulas all, share its meaning (Xu Shushi, 2024; Zeng, 2002). Shen Jianshi (1935) separated this claim about whole series from the claim about a single pair (形聲兼會意).

Later work has asked which characters the label should cover. Wang Li (1982, as cited in Zeng, 2002) held all *yìshēng* characters to be cognate with their phonetic. Zeng (2002) objected that some are merely accumulated graphs of the same word. Li Guoying (1996/2020), whose school named the phonetic's "source-indicating function" (示源功能), argues that a graph differentiated from its source inherits the source's sound, whereas a derived word "need not be" homophonous with its base. Li Ning and Guo (2019) count 217 labels and claim that 79 more characters deserve one, but their criterion already includes derivation from the phonetic and Old Chinese homophony. Hsu (2005) collects 267 labelled characters from three versions of the text. A recent review faults the programme for "substituting the character for the word" (以字代詞; Chen Shuo, 2022).

Wang Yun's *Shuōwén shìlì* (1837) makes a different kind of claim, and it is the one tested here. The label "is said of three kinds: meaning-compounds that also give the sound; phonetic compounds that also give the meaning; and differentiated graphs filed in their own section" (言亦聲者凡三種：會意字而兼聲者，一也；形聲字而兼意者，二也；分別文之在本部者，三也; Wang Yun, 1837, juan 3). A differentiated graph (分別文) adds a component that changes the meaning of an existing graph; one that leaves the meaning unchanged is an accumulated graph (累增字; juan 8). A filing rule links the third kind to the label. Differentiated graphs filed in another section never state the base's meaning, while those in their own section make the principal component the sound as well (在異部者，概不言義；在本部者，概以主義兼聲也), as with 胖 'half a carcass', filed under 半 'half' rather than 肉 'meat'. Wang also pruned the transmitted labels. Of thirteen labelled characters, he accepts four (禮, 祏, 胖, 柵) and rejects nine (貧, 愾, 恇, 娶, 婚, 姻, 婢, 緉, 坪) as "mistaken additions in the Dà Xú" (大徐誤增). Yet in juan 8 he quotes three labelled graphs filed away from their base (傾 'lean', 𨻺 and 䫇) without objection. Wang thus tied one kind of *yìshēng*, not the label as a whole, to graph differentiation. Neither he nor later scholars asked how often the label coincides with a relation between words, against what baseline, or with which difference in sound.

### 2.2 Derivation in Old Chinese

Historical phonology says which differences in sound a derivation would leave. Karlgren (1933) grouped Old Chinese words into families linked by recurrent alternations, without analysing these as affixes; Pulleyblank (1973, 2000) did, and current reconstructions posit an explicit system of derivational affixes (Baxter & Sagart, 1998, 2014; Sagart, 1999; Schuessler, 2007). The best established is the suffix \*-s, the source of the Middle Chinese departing tone. It most often formed nouns from verbs and adjectives (Baxter & Sagart, 1998; Mei, 2012), but it also formed verbs, and it has been split into three suffixes (Baxter & Sagart, 2014), traced to several merged ones (Jacques, 2016; Zhang, 2022), or reduced to a marker of outward-directed derivation (Schuessler, 2007). All these accounts treat the departing-tone member as the derived one. Alternations of initial voicing, the second main type, are attributed to a prefix \*N- (Sagart & Baxter, 2012).

Native evidence enters in two ways. Jacques (2022) defends the tone-change readings (破讀) of Han to early Tang commentators, collected in the *Jīngdiǎn shìwén*, as evidence of inherited morphology; such readings are attested from Xu Shen's own time (Zhang, 2022). The script, too, often writes a derived word with its base's graph, as Warring States manuscripts write 義 'duty' as 宜 'proper' (Baxter & Sagart, 2014), or adds a semantic element to that graph, as in 授 'give' beside 受 'receive', already distinct on the oracle bones (Jacques, 2022). Character formation has been modelled as evidence for Old Chinese phonology (Hill & List, 2019), but the *Shuōwén*'s labels have not, to our knowledge, been tested as evidence of derivation.

### 2.3 Graphs, words and the diagnosis of derivation

Whether a label on a graph can say anything about words depends on how phonetic compounds arose. Boltz (1994) derives most of them from a graph borrowed for a homophonous, usually unrelated word and then given a semantic determinative, so that word families within a series are "an accidental feature"; yet he reads Xu's formula as giving the phonetic "a simultaneous phonetic and semantic function". Qiu (2000) traces such meaningful phonetics to graphs used in an extended sense and then given a semantic element, as in 娶 'take a wife' from 取 'take'. He finds them a small share of all compounds and rejects the claim that a phonetic's meaning is shared by all its compounds (see also Schuessler, 2007).

Morphological theory meets the same problem wherever derivation has no overt marker. Arad (2003) distinguishes words formed from roots from words formed from existing words, which keep their base's meaning, and diagnoses the latter by formal traces of the base and entailment of its meaning. Rasin et al. (2024) find that the two diagnostics come apart in her own Hebrew and English data, so formal and semantic evidence of derivation must be established independently. Lexeme-based work places lexical meaning in words rather than roots (Aronoff, 2007), and paradigm-based work defines relatedness as a content relation and a form relation that recur together across pairs, with no single base required (Bonami & Strnadová, 2019; Hathout & Namer, 2019). A *yìshēng* label is a third, native kind of evidence: a record of the pairs in which an ancient analyst saw the phonetic enter the meaning. Whether it also tracks form, beyond what meaning predicts, is an empirical question.

One baseline remains. Form and meaning are weakly associated even without morphology (Dingemanse et al., 2015; Monaghan et al., 2014), in Chinese rhyme books as elsewhere (Meng et al., 2025), although that study did not separate phonetic series from other homophones. Any effect of the label must therefore be measured within phonetic series, against their unlabelled members.

### 2.4 Four accounts and their predictions

Four accounts of the label make different predictions (Table 1).

(A) On a meaning-first account, the label records that the phonetic contributes meaning, as Duan read it, and carries no information about sound of its own. It still predicts a sound profile, through meaning. A graph differentiated from its source inherits the source's reading (Li Guoying, 1996/2020), so labelled pairs should share the sound profile of the semantically related pairs in their series, whatever that profile turns out to be.

(B) If the label is a general, implicit marker of derivation, the hypothesis this study started from, labelled pairs should be enriched in identity (conversion, sense specialisation), in \*-s and in the other affixal relations alike, and the label should single out the derived member.

(C) If the label marks a new graph for the same word or for a word minimally derived from it, an extension of Wang's differentiated graph, identity and \*-s should be enriched and other affixal relations not, and the label need say nothing about direction. Unlike (A), it predicts that among pairs related in meaning, labelled ones are more often identical or \*-s related.

(D) If the effect reflects lexicon-wide systematicity, labelled and ordinary members of the same series should differ little.

**Table 1** Predictions of four accounts of the label

| | (A) Meaning first | (B) General derivation | (C) Same word or minimal derivative | (D) Systematicity |
|---|---|---|---|---|
| Identity of sound (H1a) | +^a^ | + | + | small |
| Departing-tone alternation (H1c, step 1) | +^a^ | + | + | small |
| Other alternations (H1b without the departing tone) | 0^a^ | + | 0 | small |
| Relatedness of meaning (H2) | + | + | + | small |
| Direction of \*-s pairs | – | label picks the derived member | no difference | – |
| Sound among related pairs | no difference | + | + | – |

*Note.* + labelled pairs enriched; 0 no difference; – no prediction. ^a^ Predicted through meaning, to the extent that related members of a series are identical or \*-s related.

(A) and (C) part company only in the last row, and testing it needs pairs related in meaning on both sides of the label. The analysis is organised by four directional hypotheses and two exploratory comparisons:

- **H1a (homophony).** Labelled characters are homophonous with their phonetic more often than ordinary compounds on the same phonetics.
- **H1b (other regular relations).** Among non-homophonous pairs, labelled characters differ from their phonetic by a regular alternation or affix more often.
- **H1c (the departing tone).** Among pairs that differ only in tone or voicing, the labelled character is more often the departing-tone (\*-s) member.
- **H2 (meaning).** Labelled characters are related in meaning to their phonetic more often, even without glosses that define a character by its own phonetic.
- **H3 (recensions; exploratory).** Labels on which the Dà Xú, the Xiǎo Xú 小徐 and Duan's text disagree differ from stable labels on H1a.
- **H4 (Wang's filing criterion; exploratory).** Labelled characters filed under their own phonetic differ on H1a from other labelled characters.

The hypotheses were refined after an initial look at this population and were not preregistered; Table 1 gives the order of presentation, not a record of prior prediction. H1c as stated combines (B)'s claim about the derived member with (C)'s claim about \*-s, and Section 4.2 separates the two.

## References (cited in this section)

Arad, M. (2003). Locality constraints on the interpretation of roots: The case of Hebrew denominal verbs. *Natural Language & Linguistic Theory*, *21*(4), 737–778. https://doi.org/10.1023/A:1025533719905 [E3]

Aronoff, M. (2007). In the beginning was the word. *Language*, *83*(4), 803–830. https://doi.org/10.1353/lan.2008.0042 [E1]

Baxter, W. H., & Sagart, L. (1998). Word formation in Old Chinese. In J. L. Packard (Ed.), *New approaches to Chinese word formation: Morphology, phonology and the lexicon in modern and ancient Chinese* (pp. 35–76). Mouton de Gruyter. [C4]

Baxter, W. H., & Sagart, L. (2014). *Old Chinese: A new reconstruction*. Oxford University Press. [C9]

Boltz, W. G. (1994). *The origin and early development of the Chinese writing system* (American Oriental Series 78). American Oriental Society. [D2]

Bonami, O., & Strnadová, J. (2019). Paradigm structure and predictability in derivational morphology. *Morphology*, *29*(2), 167–197. https://doi.org/10.1007/s11525-018-9322-6 [E10]

Chen, S. [陳爍] (2022, August 31). 論"右文說"的局限與出路 [On the limits and prospects of the *yòuwén* theory]. *Zhōnghuá dúshū bào* 中華讀書報. [B16]

Dingemanse, M., Blasi, D. E., Lupyan, G., Christiansen, M. H., & Monaghan, P. (2015). Arbitrariness, iconicity, and systematicity in language. *Trends in Cognitive Sciences*, *19*(10), 603–615. https://doi.org/10.1016/j.tics.2015.07.013 [E8]

Duan, Y. [段玉裁] (1815). *說文解字注* [Annotated *Shuōwén jiězì*]. Cited from the digital text of the shuowenjiezi project (github.com/shuowenjiezi/shuowen, commit 6553a35). [A2]

Hathout, N., & Namer, F. (2019). Paradigms in word formation: What are we up to? *Morphology*, *29*(2), 153–165. https://doi.org/10.1007/s11525-019-09344-3 [E9]

Hill, N. W., & List, J.-M. (2019). Using Chinese character formation graphs to test proposals in Chinese historical phonology. *Bulletin of Chinese Linguistics*, *12*(2), 186–200. https://doi.org/10.1163/2405478X-01202008 [C15]

Hsu, Y. [許育龍] (2005). 《說文》亦聲字研究 [The *yìshēng* characters of the *Shuōwén jiězì*] [Master's thesis, Tamkang University]. [F2]

Jacques, G. (2016). How many \*-s suffixes in Old Chinese? *Bulletin of Chinese Linguistics*, *9*(2), 205–217. https://doi.org/10.1163/2405478X-00902014 [C11]

Jacques, G. (2022). On the nature of morphological alternations in Archaic Chinese and their relevance to morphosyntax. *Bulletin of the School of Oriental and African Studies*, *85*(3), 475–494. https://doi.org/10.1017/S0041977X22000854 [C12]

Karlgren, B. (1933). Word families in Chinese. *Bulletin of the Museum of Far Eastern Antiquities*, *5*, 9–120. [C1]

Li, G. [李國英] (2020). *小篆形聲字研究* [Phonetic compounds in the small-seal script] (Rev. ed.). Zhonghua shuju. (Original work published 1996) [B11]

Li, N. [李寧], & Guo, S. [郭抒遠] (2019). 《說文解字》亦聲字誤為形聲字例析 [Examples of *yìshēng* characters mistaken for phonetic compounds in the *Shuōwén jiězì*]. *Wénjiào zīliào* 文教資料, 2019(4), 3–4. [B14]

Mei, T.-L. (2012). The causative \*s- and nominalizing \*-s in Old Chinese and related matters in Proto-Sino-Tibetan. *Language and Linguistics*, *13*(1), 1–28. [C7]

Meng, Y., Wan, Y., & Kit, C. (2025). Sound symbolism is not "marginal" in Chinese: Evidence from diachronic rhyme books. *PLOS ONE*, *20*(5), Article e0322044. https://doi.org/10.1371/journal.pone.0322044 [C16]

Monaghan, P., Shillcock, R. C., Christiansen, M. H., & Kirby, S. (2014). How arbitrary is language? *Philosophical Transactions of the Royal Society B*, *369*(1651), Article 20130299. https://doi.org/10.1098/rstb.2013.0299 [E7]

Pulleyblank, E. G. (1973). Some new hypotheses concerning word families in Chinese. *Journal of Chinese Linguistics*, *1*(1), 111–125. [C2]

Pulleyblank, E. G. (2000). Morphology in Old Chinese. *Journal of Chinese Linguistics*, *28*(1), 26–51. [C3]

Qiu, X. (2000). *Chinese writing* (G. L. Mattos & J. Norman, Trans.; Early China Special Monograph Series 4). Society for the Study of Early China and Institute of East Asian Studies, University of California, Berkeley. [D1]

Rasin, E., Preminger, O., & Pesetsky, D. (2024). A re-evaluation of Arad's argument for roots. In R. Autry, G. de la Cruz Sanchez, L. A. Irizarry Figueroa, K. Mihajlovic, T. Ni, R. Smith, & H. Harley (Eds.), *Proceedings of the 39th West Coast Conference on Formal Linguistics* (pp. 382–392). Cascadilla Proceedings Project. [E12]

Sagart, L. (1999). *The roots of Old Chinese*. John Benjamins. [C5]

Sagart, L., & Baxter, W. H. (2012). Reconstructing the \*s- prefix in Old Chinese. *Language and Linguistics*, *13*(1), 29–59. [C8]

Schuessler, A. (2007). *ABC etymological dictionary of Old Chinese*. University of Hawai'i Press. [C6]

Shen, J. [沈兼士] (1935). 右文說在訓詁學上之沿革及其推闡 [The history and extension of the *yòuwén* theory in exegesis]. In *慶祝蔡元培先生六十五歲論文集* [Essays in honour of Cai Yuanpei's sixty-fifth birthday] (Vol. 2, pp. 777–854). Institute of History and Philology, Academia Sinica. [A6]

Shen, K. [沈括] (2016). *夢溪筆談* [Brush talks from Dream Brook] (Y. Zhu [諸雨辰], Ed. & Trans.). Zhonghua shuju. (Original work completed ca. 1090) [A1]

Wang, Y. [王筠] (1837). *說文釋例* [Examples of the conventions of the *Shuōwén*]. Cited by juan from the block-printed edition scanned by the National Library of China. [A11]

Xu, S. [Shushi] (2024). *An analysis of Duan Yucai's theory of shengyi tongyuan in his annotations to the Shuowen jiezi* [Doctoral thesis, University of Wales Trinity Saint David]. [F1]

Zeng, Z. [曾昭聰] (2002). *形聲字聲符示源功能述論* [On the source-indicating function of phonetic components]. Huangshan shushe. [B2]

Zhang, S. (2022). Rethinking the \*-s suffix in Old Chinese: With new evidence from Situ Rgyalrong. *Folia Linguistica*, *56*(s43-s1), 129–167. https://doi.org/10.1515/flin-2022-2014 [C13]
