# Literature Review (draft v0.2)

**Paper topic (Qu's choice, candidate question 2):** Is Xu Shen's label *yìshēng* 亦聲 ("also phonetic") an implicit, native diagnostic of derivation? The question is whether characters glossed as "从 A 从 B，B 亦聲" stand in a regular relation to the word written by their phonetic (the same word, or the same root plus a known affix or alternation) more often than ordinary phonetic compounds do.

**Target journal:** *Language and Linguistics* (English).

**Status:** v0.2, 2026-09-24, with a small update on 2026-09-25 (last item in the list below). This draft becomes §2 of the paper. It follows the section numbering and the hypotheses of `outline.md`, which the topic thread owns. Changes from v0.1:
- §2.1 adds Wang Yun's *fēnbiéwén* and *lěizēngzì*, his three kinds of *yìshēng*, and recent work by Li Guoying, Jiang Zhiyuan, Xu Shushi, and Li and Guo. It also gives the path from the 227 labelled entries to the 212 that are analysed.
- §2.2 uses example pairs whose sound relation is stated correctly. (One v0.1 example, given as a tone-only pair, also differs in the initial.)
- §2.4 is now descriptive. The answer to Rasin et al. (2024) moves to §5.2.
- §2.5 states the outline's hypotheses H1a–H3.
- The example pairs were chosen from outside the 100-item blind coding sheet while the coding was under way.
- Update of 2026-09-25, after the coding had finished: §2.1 gives the juan 8 location of Wang Yun's definitions and discusses two of his own examples, 娶 and 傾, both known here only through O (2015). §2.5 adds the outline's H4.

Reference codes in square brackets (e.g., [C12]) point to `bibliography.md`. `literature_review_access_log.md` records which sources were read in full and which only from abstracts or through quotations in other works. Every claim that rests on such a source must be checked against the original before submission.

---

## 2. Background and previous research

### 2.1 From *yìshēng* to *yòuwén*: the traditional problem

The *Shuōwén jiězì* 說文解字 (100 CE) analyses the great majority of its head characters as phonetic compounds (*xíngshēng* 形聲): one component signals the semantic field (the "signific" or "semantic classifier") and another signals the pronunciation (the "phonetic"). In a smaller set of entries, however, Xu Shen does something different. He lists both components as meaningful (从 A 从 B) and then adds that one of them "is also the sound" (B 亦聲). Examples are 政 "to govern", glossed 正也 "to rectify" (从攴从正，正亦聲); 殯 "to lay out the encoffined dead before burial" (从歺从賓，賓亦聲); and 琀 "jade placed in the mouth of the dead" (从玉从含，含亦聲).

In the Dà Xú 大徐 recension, as represented in the open digital edition used for this study (shuowenjiezi/shuowen on GitHub, Apache-2.0), 227 head entries carry the formula. Of these, 224 are found automatically and three are resolved by hand (`youwen_criteria.md`). Not all of them are Xu Shen's own labels. In four, 亦 is itself the phonetic (the formula reads 从X，亦聲), which leaves 223. Eleven more are *xīnfù* 新附 characters, which Xu Xuan 徐鉉 added when he edited the text in 986. Removing them leaves 212 entries, on 172 phonetics, and these form the population analysed here (outline §3.1). Two further formulas occur in the glosses of variant graphs and are not counted. The digitised text has known typographical errors, so every count must be checked against the 1963 Zhonghua shuju facsimile of the Dà Xú edition, where the 新附 characters are printed separately.

The Dà Xú and Xiǎo Xú 小徐 recensions also differ in where they write *yìshēng*. A study in a Korean journal is devoted to exactly this question (二徐本《說文》亦聲字差異探討, KCI ART002078031; author and details still to be confirmed) [E13]. The Xiǎo Xú text is openly available in the *Sìbù cóngkān* edition digitised by the Kanseki Repository (KR1j0019), so the comparison can be made directly. §3.5 explains why it can be made only for part of the population.

The only monograph-length treatment of the label that we have identified is Hsu Yu-lung's 許育龍 master's thesis (2005) [F2]. According to its abstract, it collects 29 interpretations of *yìshēng* from the Southern Tang to the present, analyses 267 *yìshēng* characters across three textual versions of the *Shuōwén*, and sorts previous scholarship into four competing positions on how the label fits the six-script taxonomy. Its count is higher than ours, apparently because it pools the versions (outline §3.1). Article-length studies continue in the same vein. Li Ning 李寧 and Guo Shuyuan 郭抒遠 (2019), for example, identify 79 characters that Xu analyses as ordinary phonetic compounds but that in their view should carry the label [B14]. This literature confirms the gap identified below: the debate concerns which characters belong to the category, not the relation between the words written.

Duan Yucai 段玉裁 gave the formula its canonical interpretation. In a note in the first chapter of his commentary (卷一上) he states: "凡言亦聲者，會意兼形聲也" ("whenever [Xu] says 'also phonetic', the character is a meaning-compound that is at the same time a phonetic compound"). Duan also regarded the label as incompletely applied. For many characters that Xu analyses as ordinary phonetic compounds, he writes that the analysis "should read" otherwise. Under 論 "to discuss" and 議 "to deliberate", for instance, he writes "當云从言侖、侖亦聲" and "當云从言義、義亦聲". More importantly, Duan extended the idea far beyond the labelled cases. In the same digital edition, his commentary uses the phrase *xíngshēng bāo huìyì* 形聲包會意 ("a phonetic compound that contains a meaning-compound") 128 times and *xíngshēng zhōng yǒu huìyì* 形聲中有會意 29 times. For Duan, then, *yìshēng* is the explicit tip of a much broader pattern in which the phonetic also carries meaning. Xu Shushi (2024) analyses the sources, method and limits of this theory that sound and meaning share a source (*shēngyì tóngyuán* 聲義同源) [F1].

Wang Yun 王筠 (1784–1854) took a further step, and it is the one most directly relevant to this study. His *Shuōwén shìlì* 說文釋例 (1837) distinguishes two outcomes when a component is added to an existing graph [A11].
- If the added component changes the meaning, the new form is a "differentiated graph" (*fēnbiéwén* 分別文). This happens for one of two reasons. Either the graph's proper meaning had been taken over by a borrowed meaning, and the component was added to keep the two apart. Or the graph had many meanings, and the new form takes over only one of them.
- If the added component leaves the meaning unchanged, the new form is an "accumulated graph" (*lěizēngzì* 累增字). One case is when the old meaning was obscure and the component was added to make it explicit.

These definitions open juan 8 of the *Shìlì* (leaf 1 of the Zhonghua shuju facsimile, as quoted in O Je-jung 2015: 469) [B13]. Wang also classified the *yìshēng* label itself. As quoted by Li and Guo (2019) [B14], he writes: "言亦聲者凡三種：會意而兼聲者，一也；形聲字而兼意者，二也；分別文之在本部者，三也" ("*yìshēng* is said of three kinds: meaning-compounds that also indicate the sound; phonetic compounds that also indicate the meaning; and differentiated graphs placed in their own section"). On our reading, the third kind means differentiated graphs that Xu files in the section headed by their base graph. Wang therefore already tied the label, in part, to graphic differentiation, the case in which one word, or one meaning of a word, receives a graph of its own. The third example given above appears to be such a case: under 琀, Duan notes that the classics mostly write the word as 含 (經傳多用含). Yet 琀 is filed under 玉, not under 含. Wang's own examples in juan 8 likewise show that his differentiated graphs form a wider class than his third kind of *yìshēng*. Two of them carry the label in the Dà Xú text: 娶 "to take a wife", which he calls the differentiated graph of 取 "to take", and 傾 "to lean", from 頃 "head not upright" (O 2015: 471–473). Xu files these under 女 and 人, not under their base graphs, so on our reading Wang would count their labels among his first two kinds. His other examples, such as 恭 "reverent" beside 共, carry no label.

Wang, however, stated his three kinds as a classification of characters. He gave no counts, and he did not consider the sound relation between the two words. Recent work also warns against conflating his categories with the older exegetical notion of "ancient and modern graphs" (*gǔjīnzì* 古今字). Jiang Zhiyuan 蔣志遠 (2021) argues that the two belong to different theoretical levels, and that the conflation began with Xu Hao's 徐灝 later commentary on Duan, not with Wang himself [B12]. Ma Weicheng 馬偉成 (2012) studies how Wang treats phonetics that also carry meaning in his *Shuōwén jiězì jùdòu* 說文解字句讀 [B15]. The *Shìlì* itself has not yet been consulted for this draft, because the available scan cannot be read here. Wang's wording is therefore cited through O (2015) and Li and Guo (2019), and it must be checked against the original.

The *yìshēng* label belongs to a broader debate, the *yòuwén* 右文 ("right-side graph") hypothesis. The earliest record is Shen Kuo's 沈括 *Mèngxī bǐtán* 夢溪筆談, which attributes to Wang Shengmei 王聖美 the claim that the right-hand component of a character carries its meaning. His example is the series of 戔 (淺 "shallow", 錢 "coin", 殘 "damaged", 賤 "cheap"), all supposedly sharing the sense "small" [A1]. Qing philologists turned this intuition into a working method. Duan's formula "凡从某聲皆有某義" and Wang Niansun's 王念孫 principle of "seeking ancient meanings through ancient sounds, unconstrained by graphic form" (就古音以求古義，引伸觸類，不限形體) represent two different routes [A2, A3]. Duan tied meaning to the phonetic component. Wang Niansun tied it to the spoken word, whatever graph happened to write it. Zhang Taiyan 章太炎 and Huang Kan 黃侃 then systematised word-family research under two relations: *biànyì* 變易 (the same word written differently) and *zīrǔ* 孳乳 (a new word derived from an old one with a differentiated meaning) [A4, A5]. Recent work on Zhang's *Wénshǐ* 文始 stresses that what separates *zīrǔ* from *biànyì* is precisely whether the meaning has diverged (Zhu 2021) [B9]. In other words, *zīrǔ* is the tradition's closest analogue to derivation.

Shen Jianshi's 沈兼士 1933 survey remains the standard modern treatment of *yòuwén* [A6]. It distinguished cases where the phonetic genuinely signals meaning from cases where it is merely borrowed for its sound. Yang Shuda 楊樹達 applied the method to hundreds of individual characters [A7]. Wang Li 王力, by contrast, criticised *yòuwén* for organising etymology by graph rather than by word, even though his own *Tóngyuán zìdiǎn* 同源字典 relies heavily on phonetic series in practice [A8]. Zeng Zhaocong 曾昭聰 (2000) documents this tension in detail [A10].

Since the 1990s the discussion has moved to the "source-indicating function" (*shìyuán gōngnéng* 示源功能) of the phonetic. This line of work is associated with Wang Ning's 王寧 theory of character configuration [B8]. Li Guoying's 李國英 study of the phonetic compounds of the small-seal script (1996; revised edition 2020) discusses both the sound-indicating and the source-indicating functions of the phonetic [B11]. A notice of the revised edition presents it as keeping what is sound in *yòuwén* while correcting its one-sidedness. We have not yet been able to consult the book itself, including its treatment of *yìshēng*. The line was developed further in monographs by Zeng Zhaocong (2002) [B2] and, most recently, Chen Xiaoqiang (2021) [B1]. Chen proposes a "comparative cross-verification of phonetics" (聲符比較互證法). It examines characters built on *different* phonetics that are homophonous or near-homophonous, in order to escape *yòuwén*'s dependence on a single graph. A 2022 review singles out "substituting the character for the word" (以字代詞) as *yòuwén*'s central weakness (Chen Shuo 2022, reviewing [B1]). Parallel work models the semantics of word families more abstractly: as "etymological meaning" built from meaning components (Huang Yiqing 2007) [B4], or as a shared "core meaning" underlying polysemy and cognation (Wang & Wang 2014) [B7]. Zhang Bo (2003) supplies explicit procedures for verifying that two words belong to the same family [B3].

Three observations follow from this tradition. They define the gap the present study addresses.

1. **The tradition treats *yìshēng* mainly as a problem of character classification.** The standard question has been which of the "six scripts" (六書) a *yìshēng* character belongs to: meaning-compound, phonetic compound, or both. Duan's "會意兼形聲" answers that question. Wang Yun comes closest to a claim about words, since one of his three kinds of *yìshēng* is the differentiated graph. But his typology, too, is a classification of characters, stated without counts. Whether, and how often, the label picks out a particular relation between two words has not been tested.
2. **Traditional evidence for shared meaning is qualitative and selective.** Neither the *yòuwén* literature nor the *shìyuán* literature reports what proportion of a phonetic series, or of Xu's *yìshēng* set, actually shares the claimed meaning. Nor does it compare that proportion with a baseline.
3. **The phonological side is left implicit.** Traditional scholars required the two words to be "the same or similar in sound" (音同音近). They did not ask whether the particular sound difference between base and derivative is a *regular* one, of the kind a morphological process would produce.

### 2.2 Old Chinese word families as morphology

A separate tradition, largely in Western languages, reached the same materials from historical phonology. Karlgren (1934) argued that Chinese vocabulary is organised into word families rather than into thousands of isolated monosyllables [C1]. Sagart's encyclopaedia entry summarises this view as an argument for comparing word stems rather than individual words [C10]. Pulleyblank (1973, 2000) reinterpreted the phonological differences within word families as the traces of prefixes, suffixes and vowel alternations [C2, C3]. From that point on, the question became one of morphology.

The modern consensus rests on three bodies of evidence.

- **Xiéshēng series (phonetic series).** The pronunciations of characters that share a phonetic constrain the reconstruction of Old Chinese onsets and codas. Sagart and Baxter (2012) use exactly this evidence, together with word-family semantics, to reconstruct a causative/denominal prefix *s- [C8]. Mei (2012) makes a complementary argument for a causative *s- and a nominalising *-s [C7].
- **Readings in the commentarial tradition.** Jacques (2022) argues that sound glosses in early commentaries, which record "tone-change" or "voicing-change" readings (破讀), are reliable evidence for morphological alternations. He argues further that these alternations are directly relevant to syntactic analysis [C12]. Jacques (2016) and Zhang Shuya (2022) show that the departing tone (*qùshēng*, from *-s) is not a single suffix but several, including nominalisation, argument demotion and adverbialisation [C11, C13].
- **Reconstruction systems.** Baxter and Sagart (1998) survey the word-formation processes of Old Chinese [C4]. Sagart (1999) separates roots from affixes [C5]. Baxter and Sagart (2014) integrate both into a full reconstruction [C9]. Schuessler (2007) provides an etymological dictionary with explicit word-family judgements [C6].

Hill and List (2019) take an important methodological step [C15]. They model character formation as a directed graph in which each character points to its phonetic, and they use network analysis to test competing hypotheses in Old Chinese phonology. Some distinctions, such as the type A/B contrast, turn out to be encoded in the choice of phonetic, while others do not. The broader lesson is that the *Shuōwén*'s graphic analyses can be treated as data and tested systematically, rather than cited example by example.

This tradition, however, has a mirror-image gap to the one in §2.1. Historical phonologists have treated commentarial readings (Jacques 2022) and phonetic series (Sagart & Baxter 2012) as evidence for morphology. They have not asked whether Xu Shen's *own metalinguistic labels* carry such evidence. A *yìshēng* annotation is a native speaker-scholar's judgement that a character contains a meaningful and a phonetic component *at the same time*. Suppose Old Chinese derivation left regular phonological traces, and Xu Shen was sensitive to derivational relatedness. Then *yìshēng* characters should stand in regular sound relations to their base (identity, or a regular affixal difference) more often than ordinary phonetic compounds do.

A few *yìshēng* pairs suggest that the idea is worth testing. In the Dà Xú fǎnqiè readings, 殯 (必刃切, Middle Chinese pjinH) differs from 賓 (必鄰切, pjin) only in having the departing tone. 琀 (胡紺切, homH) differs from 含 (胡男切, hom) in the same way. Other labelled pairs are homophonous: 政 and 正 are both read 之盛切 (tsyengH). Still others differ in the voicing of the initial as well as in tone. The departing tone is the reflex of the *-s suffix(es) discussed above. These examples are illustrative only, and they were not sampled. §3 tests the pattern on the whole population. §3.5 separates homophony (H1a) from affixal differences (H1b) and from the direction of the tone difference (H1c).

### 2.3 Writing and language: why a graphic label can bear on morphology

An obvious objection is that *yìshēng* is a statement about a graph, not a word. The grapholinguistic literature makes this objection precise, and it also shows how it can be answered.

Qiu Xigui's standard account distinguishes components that function as semantic signs, phonetic signs and mere marks, and treats "meaning-compound-cum-phonetic" characters as a subtype of phonetic compounds [D1]. Boltz (1994) argues that the phonetic compound arose when a single graph was extended to write several related words and was then disambiguated by an added signific. On this view the phonetic of a derived word is often the graph of its base word [D2]. That account predicts exactly the configuration that *yìshēng* describes, and it amounts to a historical explanation of Wang Yun's differentiated graphs. Excavated manuscripts show, however, that early scribes varied their choice of phonetic considerably [D3]. The configuration preserved in the *Shuōwén* is therefore partly a Han-dynasty standardisation and not a direct record of how the words were derived.

General theories of writing supply the vocabulary needed to keep these levels apart. Meletis (2020) distinguishes graphematic units from the linguistic units they relate to, and the relations between them [D6]. Handel (2019) classifies Chinese-type scripts as morphosyllabic: each graph corresponds to a syllable that is typically a morpheme [D4]. Myers (2019) argues that the internal structure of Chinese characters has a grammar of its own, open to the same productivity-based analysis as morphology [D5]. Huang, Wang and Chen (2022) present corpus evidence that the character remains an indispensable unit in Chinese linguistic analysis alongside the word [D7]. Zhang Liulin (2023) argues that the character script contributed to making Old Chinese morphology invisible to later analysis [C14].

Taken together, this work suggests a clear condition. A graphic label such as *yìshēng* can count as evidence about morphology only if it can be shown to *covary* with independent linguistic evidence, namely regular phonological relations between the words written. The present study tests that condition directly. It uses Middle Chinese readings and Old Chinese reconstructions that were established independently of Xu Shen's labels.

### 2.4 Roots, words and derivational relatedness in morphological theory

Morphological theory offers two ways of describing relatedness between words, and a baseline for sound–meaning correspondences below the level of the morpheme.

**Root-based derivation.** In Distributed Morphology, roots are category-neutral and receive their interpretation from the first category-assigning head they combine with. Arad (2003) states the locality condition: "Roots are assigned an interpretation in the environment of the first category-assigning head with which they are merged," and "once the root has merged with a category head and formed a word, its interpretation is fixed" [E3]. Arad distinguishes *root-derived* formations from *word-derived* formations. Root-derived formations can take many unpredictable meanings from the same root. Word-derived formations inherit, and semantically entail, the meaning of an existing word. Harley (2014) goes further and argues that roots are individuated only by abstract indices, not by their sound or meaning [E4]. Rasin, Preminger and Pesetsky (2024), however, re-examine Arad's Hebrew data. They find that the claimed correlation between unpredictable meaning and root-derived status does not hold: some denominal verbs also have meanings that cannot be predicted from the noun [E12].

**Word-based derivation.** Aronoff (2007) defends the lexicalist position that lexemes, not morphemes, are the basic meaningful units, and he cites Hebrew verbal roots that have robust formal properties but no constant meaning [E1]. In a related paper, Aronoff (2013) treats the root as a purely morphological object [E2]. Work on derivational paradigms treats families of related words as structured sets whose members predict one another (Hathout & Namer 2019; Bonami & Strnadová 2019) [E9, E10]. From this perspective, the relevant unit is not a meaningful root but a *derivational family* whose members are linked by recurrent form–meaning relations.

The contrast between forms built on an existing word and forms built directly on a root is therefore well established. So is a semantic criterion for telling them apart: a word-derived form includes the meaning of its base. That criterion is the obvious one to apply to Xu Shen's glosses. After Rasin et al. (2024), however, it cannot be taken for granted. We return to this question in §5.2, where the results can bear on it.

A third body of work concerns sound–meaning systematicity below the level of the morpheme. Kwon and Round (2015) apply canonical typology to phonaesthemes such as English *gl-* or *sl-*. They find that what sets phonaesthemes apart from roots is that they are canonically "accompanied by non-recurrent residues" [E5]. Bergen (2004) shows that such units have psychological reality [E6]. Monaghan et al. (2014) and Dingemanse et al. (2015) show that form–meaning systematicity across a lexicon is weak but statistically robust, and they distinguish it from iconicity [E7, E8]. For Chinese specifically, Meng, Wan and Kit (2025) report robust sound-symbolic clustering across historical rhyme dictionaries [C16]. This literature supplies a baseline expectation. Some degree of meaning-sharing within a phonetic series is expected even without derivation, simply from lexical systematicity. Any claim that *yìshēng* marks derivation must therefore show an effect *above* that baseline.

### 2.5 Synthesis: the gap and the hypotheses

The three literatures meet at a point none of them has examined.

- Traditional philology has an explicit native category, *yìshēng*, which it has discussed almost entirely as a matter of character classification. Wang Yun linked part of it to graphic differentiation, but that link has never been tested (§2.1).
- Historical phonology has a well-developed inventory of derivational affixes and alternations, and it accepts native commentarial readings as evidence for them. It has not tested Xu Shen's structural labels in the same way (§2.2).
- Morphological theory provides a contrast between word-derived and root-derived formation, although its diagnostic is contested. It also provides a baseline expectation of sub-morphemic systematicity. Neither has been applied to Chinese graphic analysis (§2.4).

The present study asks whether *yìshēng* annotations *covary* with independent evidence of derivation. The hypotheses are stated in full in §3.5, with the tests in §3.6. In brief:

- **H1a (homophony).** Labelled characters are homophonous with their phonetic character more often than unlabelled members of the same series.
- **H1b (affixal regularity).** Among pairs that are not homophonous, labelled characters differ from the phonetic by a regular affix or alternation (*s-, *N-, *m-, *-s, *-ʔ, voicing, type A/B, *r) more often than unlabelled ones.
- **H1c (direction).** Among pairs that differ only in tone and/or voicing, the labelled character is the departing-tone (*-s) member more often than in unlabelled pairs. In other words, the label picks out the derivative, not the base.
- **H2 (semantic inclusion).** The meaning of a labelled character includes that of its phonetic character more often than for unlabelled members. The difference must survive the removal of paronomastic glosses, which define a character by its own phonetic (as 政 is glossed 正也).
- **H3 (label stability; exploratory, two-sided).** Items on which the Dà Xú text, the Xiǎo Xú text and Duan's emended text disagree differ from stable items on H1a and H2.
- **H4 (Wang Yun's third kind; exploratory, two-sided).** The 40 labelled characters filed in the section of their own phonetic differ on H1a and H2 from the other 172 labels, which reflect Xu's independent judgement.

H1 is split into three parts because identity and affixation are different relations. Identity is what Wang Yun's accumulated and differentiated graphs, and conversion, would produce. An affixal difference is what derivation proper would produce. If the label tracks identity and the direction of *-s but not affixal differences in general, *yìshēng* would mark a new graph for the same word, or for a minimally derived one, rather than affixal derivation as such. If it tracks none of them, the label is a graphic and exegetical category, and the result would support Wang Li's and Chen Xiaoqiang's warnings against "substituting the character for the word".

---

## References (cited in this section)

Codes in brackets refer to `bibliography.md`. † marks volume or page data not yet re-seen on the publisher's page.

- Arad, Maya. 2003. Locality constraints on the interpretation of roots: The case of Hebrew denominal verbs. *Natural Language & Linguistic Theory* 21(4): 737–778. † [E3]
- Aronoff, Mark. 2007. In the beginning was the word. *Language* 83(4): 803–830. [E1]
- Aronoff, Mark. 2013. The roots of language. In Silvio Cruschina, Martin Maiden & John Charles Smith (eds.), *The Boundaries of Pure Morphology*, 161–180. Oxford: Oxford University Press. [E2]
- Baxter, William H. & Laurent Sagart. 1998. Word formation in Old Chinese. In Jerome L. Packard (ed.), *New Approaches to Chinese Word Formation*, 35–76. Berlin: Mouton de Gruyter. [C4]
- Baxter, William H. & Laurent Sagart. 2014. *Old Chinese: A New Reconstruction*. New York: Oxford University Press. [C9]
- Bergen, Benjamin K. 2004. The psychological reality of phonaesthemes. *Language* 80(2): 290–311. † [E6]
- Bonami, Olivier & Jana Strnadová. 2019. Paradigm structure and predictability in derivational morphology. *Morphology* 29(2): 167–197. † [E10]
- Boltz, William G. 1994. *The Origin and Early Development of the Chinese Writing System*. New Haven: American Oriental Society. [D2]
- Chen, Shuo 陳爍. 2022. 論"右文說"的局限與出路 [On the limits and prospects of the *yòuwén* theory]. *Zhōnghuá dúshū bào* 中華讀書報, 31 August 2022, p. 8.
- Chen, Xiaoqiang 陳曉強. 2021. 形聲字聲符示源功能研究 [The source-indicating function of phonetic components]. Shanghai: Shanghai guji chubanshe. [B1]
- Dingemanse, Mark, Damián E. Blasi, Gary Lupyan, Morten H. Christiansen & Padraic Monaghan. 2015. Arbitrariness, iconicity, and systematicity in language. *Trends in Cognitive Sciences* 19(10): 603–615. † [E8]
- Duan, Yucai 段玉裁. 1815. 說文解字注. Jingyunlou edition; facsimile Shanghai guji chubanshe. [A2]
- Galambos, Imre. 2006. *Orthography of Early Chinese Writing: Evidence from Newly Excavated Manuscripts*. Budapest: Eötvös Loránd University. [D3]
- Handel, Zev. 2019. *Sinography: The Borrowing and Adaptation of the Chinese Script*. Leiden: Brill. [D4]
- Harley, Heidi. 2014. On the identity of roots. *Theoretical Linguistics* 40(3/4): 225–276. [E4]
- Hathout, Nabil & Fiammetta Namer. 2019. Paradigms in word formation: What are we up to? *Morphology* 29(2): 153–165. † [E9]
- Hill, Nathan W. & Johann-Mattis List. 2019. Using Chinese character formation graphs to test proposals in Chinese historical phonology. *Bulletin of Chinese Linguistics* 12(2): 186–200. [C15]
- Hsu, Yu-lung 許育龍. 2005. 《說文》亦聲字研究. MA thesis, Tamkang University. [F2]
- Huang, Chu-Ren, Hongjun Wang & I-Hsuan Chen. 2022. Characters as basic lexical units and monosyllabicity in Chinese. In C.-R. Huang et al. (eds.), *The Cambridge Handbook of Chinese Linguistics*, 74–96. Cambridge: Cambridge University Press. [D7]
- Huang, Kan 黃侃. 1983. 文字聲韻訓詁筆記, ed. Huang Zhuo 黃焯. Shanghai: Shanghai guji chubanshe. [A5]
- Huang, Yiqing 黃易青. 2007. 上古漢語同源詞意義系統研究. Beijing: Shangwu yinshuguan. [B4]
- Jacques, Guillaume. 2016. How many *-s suffixes in Old Chinese? *Bulletin of Chinese Linguistics* 9(2). [C11]
- Jacques, Guillaume. 2022. On the nature of morphological alternations in Archaic Chinese and their relevance to morphosyntax. *Bulletin of SOAS* 85(3): 475–494. [C12]
- Jiang, Zhiyuan 蔣志遠. 2021. 王筠"古今字"研究 [Wang Yun's *gǔjīnzì*]. Beijing: Shehui kexue wenxian chubanshe. [B12]
- Karlgren, Bernhard. 1934. Word families in Chinese. *Bulletin of the Museum of Far Eastern Antiquities* 5: 9–120. † [C1]
- Kwon, Nahyun & Erich R. Round. 2015. Phonaesthemes in morphological theory. *Morphology* 25(1): 1–27. [E5]
- Li, Guoying 李國英. 1996. 小篆形聲字研究 [Phonetic compounds in the small-seal script]. Beijing: Beijing shifan daxue chubanshe. Revised edition, Beijing: Zhonghua shuju, 2020. [B11]
- Li, Ning 李寧 & Guo Shuyuan 郭抒遠. 2019. 《說文解字》亦聲字誤為形聲字例析 [*Yìshēng* characters analysed as phonetic compounds in the *Shuōwén jiězì*]. 文教資料 2019(4). [B14]
- Ma, Weicheng 馬偉成. 2012. 王筠《說文解字句讀》「聲符兼義」探析 [Phonetics that also carry meaning in Wang Yun's *Shuōwén jiězì jùdòu*]. Hua Mulan wenhua chubanshe (中國語言文字研究輯刊). [B15]
- Mei, Tsu-lin. 2012. The causative *s- and nominalizing *-s in Old Chinese and related matters in Proto-Sino-Tibetan. *Language and Linguistics* 13(1): 1–28. † [C7]
- Meletis, Dimitrios. 2020. *The Nature of Writing: A Theory of Grapholinguistics*. Brest: Fluxus Editions. [D6]
- Meng, Yingying, Yuwei Wan & Chunyu Kit. 2025. Sound symbolism is not "marginal" in Chinese: Evidence from diachronic rhyme books. *PLOS ONE* 20(5): e0322044. [C16]
- Monaghan, Padraic, Richard C. Shillcock, Morten H. Christiansen & Simon Kirby. 2014. How arbitrary is language? *Philosophical Transactions of the Royal Society B* 369(1651): 20130299. [E7]
- Myers, James. 2019. *The Grammar of Chinese Characters*. London: Routledge. [D5]
- O, Je-jung 오제중. 2015. 王筠의 古今字 이론 연구: 分別文과 累增字를 위주로 [Wang Yun's theory of *gǔjīnzì*, with a focus on *fēnbiéwén* and *lěizēngzì*]. 비교문화연구 39: 462–483. † [B13]
- Pulleyblank, Edwin G. 1973. Some new hypotheses concerning word families in Chinese. *Journal of Chinese Linguistics* 1(1): 111–125. [C2]
- Pulleyblank, Edwin G. 2000. Morphology in Old Chinese. *Journal of Chinese Linguistics* 28(1): 26–51. [C3]
- Qiu, Xigui. 2000. *Chinese Writing*. Trans. Gilbert L. Mattos & Jerry Norman. Berkeley: Society for the Study of Early China. [D1]
- Rasin, Ezer, Omer Preminger & David Pesetsky. 2024. A re-evaluation of Arad's argument for roots. In Robert Autry et al. (eds.), *Proceedings of the 39th West Coast Conference on Formal Linguistics*, 382–392. Somerville, MA: Cascadilla Proceedings Project. [E12]
- Sagart, Laurent. 1999. *The Roots of Old Chinese*. Amsterdam: John Benjamins. [C5]
- Sagart, Laurent. 2015. Word families. In Rint Sybesma (ed.), *Encyclopedia of Chinese Language and Linguistics*. Leiden: Brill. [C10]
- Sagart, Laurent & William H. Baxter. 2012. Reconstructing the *s- prefix in Old Chinese. *Language and Linguistics* 13(1): 29–59. † [C8]
- Schuessler, Axel. 2007. *ABC Etymological Dictionary of Old Chinese*. Honolulu: University of Hawai'i Press. [C6]
- Shen, Jianshi 沈兼士. 1933. 右文說在訓詁學上之沿革及其推闡. In 慶祝蔡元培先生六十五歲論文集; reprinted in 沈兼士學術論文集, Beijing: Zhonghua shuju, 1986. [A6]
- Shen, Kuo 沈括. 夢溪筆談, juan 14. [A1]
- Wang, Li 王力. 1982. 同源字典. Beijing: Shangwu yinshuguan. [A8]
- Wang, Ning 王寧. 2015. 漢字構形學導論. Beijing: Shangwu yinshuguan. [B8]
- Wang, Niansun 王念孫. 1796. 廣雅疏證. [A3]
- Wang, Yun 王筠. 1837. 說文釋例. Facsimile reprint, Beijing: Zhonghua shuju (1988 as cited in O 2015; usually dated 1987, to be checked). Cited here through O 2015 and Li & Guo 2019. † [A11]
- Wang, Yunlu 王雲路 & Wang Cheng 王誠. 2014. 漢語詞彙核心義研究. Beijing: Shangwu yinshuguan. [B7]
- Xu, Shen 許慎. 100 CE. 說文解字. Dà Xú recension; facsimile Beijing: Zhonghua shuju, 1963. Digital text: shuowenjiezi/shuowen (GitHub, Apache-2.0).
- Xu, Shushi. 2024. An analysis of Duan Yucai's theory of *shengyi tongyuan* in his annotations to the *Shuowen jiezi*. PhD thesis, University of Wales Trinity Saint David. [F1]
- Yang, Shuda 楊樹達. 1983 [1937]. 積微居小學金石論叢 (enlarged edition). Beijing: Zhonghua shuju. [A7]
- Zeng, Zhaocong 曾昭聰. 2000. 王力先生有關形聲字聲符示源功能的研究述評. 中國語文通訊 55. [A10]
- Zeng, Zhaocong 曾昭聰. 2002. 形聲字聲符示源功能述論. Hefei: Huangshan shushe. [B2]
- Zhang, Bo 張博. 2003. 漢語同族詞的系統性與驗證方法. Beijing: Shangwu yinshuguan. [B3]
- Zhang, Liulin. 2023. Has Chinese always been an analytic language? Effects of writing on language evolution. *Language and Semiotic Studies* 9(4): 576–597. [C14]
- Zhang, Shuya. 2022. Rethinking the *-s suffix in Old Chinese: With new evidence from Situ Rgyalrong. *Folia Linguistica* 56: 129–167. [C13]
- Zhang, Taiyan 章太炎. 文始. In 章太炎全集. Shanghai: Shanghai renmin chubanshe. [A4]
- Zhu, Lechuan 朱樂川. 2021. 試論變易與孳乳中形音義的關係——以章太炎《文始》為例. 漢字漢語研究 2021(4). [B9]
- [Author to be confirmed]. 二徐本《說文》亦聲字差異探討. KCI-indexed Korean journal, article ART002078031. [E13; title only]
