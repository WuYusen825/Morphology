# Literature Review (draft v0.1)

**Paper topic (Qu's choice, candidate question 2):** Is Xu Shen's label *yìshēng* 亦聲 ("also phonetic") an implicit, native diagnostic of derivation? The question is whether characters glossed as "从 A 从 B，B 亦聲" stand in a regular morphological relation (same root plus a known affix or alternation) to the character written by their phonetic more often than ordinary phonetic compounds do.

**Target journal:** *Language and Linguistics* (English).
**Status:** first draft, written 2026-09-24 before the paper outline existed. Once the outline is in `/mnt/project-files/youwen/`, the section numbering here should follow it. Reference codes in square brackets (e.g., [C12]) point to `bibliography.md`. Which sources were read in full and which only from abstracts is recorded in `literature_review_access_log.md`. Every claim resting on an abstract-only source must be checked against the full text before submission.

---

## 2. Background and previous research

### 2.1 From *yìshēng* to *yòuwén*: the traditional problem

The *Shuōwén jiězì* 說文解字 (100 CE) analyses the great majority of its head characters as phonetic compounds (*xíngshēng* 形聲): one component signals the semantic field (the "signific" or "semantic classifier") and another signals the pronunciation (the "phonetic"). In a smaller set of entries, however, Xu Shen does something different. He lists both components as meaningful (从 A 从 B) and then adds that one of them "is also the sound" (B 亦聲). In the Dà Xú 大徐 recension, as represented in the open digital edition used for the pilot corpus (shuowenjiezi/shuowen on GitHub, Apache-2.0), 227 head entries carry the formula *yìshēng*. Typical examples are 娶 "to take a wife" (从女从取，取亦聲), 仲 "middle (brother)" (从人从中，中亦聲), 政 "to govern, rectify" (从攴从正，正亦聲), 坪 "level ground" (从土从平，平亦聲) and 吏 "official" (从一从史，史亦聲). This count comes from a digitised text that has known typographical errors, so it must be checked against the 1963 Zhonghua shuju facsimile of the Dà Xú edition. The Dà Xú and Xiǎo Xú recensions also differ in where they write *yìshēng*. A study in a Korean journal is devoted to exactly this question (二徐本《說文》亦聲字差異探討, KCI ART002078031; author and details still to be confirmed), and we return to the point in H3 below.

Duan Yucai 段玉裁 gave the formula its canonical interpretation. In his note under 吏 he states: "凡言亦聲者，會意兼形聲也" ("whenever [Xu] says 'also phonetic', the character is a meaning-compound that is at the same time a phonetic compound"). Duan also recognised that the label is applied inconsistently. Under 祫 "joint sacrifice" (从示、合) he remarks that Xu "does not say 合 is also phonetic only for brevity" (不云合亦聲者，省文). More importantly, Duan extended the idea far beyond the 227 labelled cases. In the same digital edition, his commentary uses the phrase *xíngshēng bāo huìyì* 形聲包會意 ("a phonetic compound that contains a meaning-compound") 128 times and *xíngshēng zhōng yǒu huìyì* 形聲中有會意 29 times, including under 娶 itself. For Duan, then, *yìshēng* is the explicit tip of a much broader pattern in which the phonetic also carries meaning.

That broader pattern is the *yòuwén* 右文 ("right-side graph") hypothesis. The earliest record is Shen Kuo's 沈括 *Mèngxī bǐtán* 夢溪筆談, which attributes to Wang Shengmei 王聖美 the claim that the right-hand component of a character carries its meaning. His example is the series of 戔 (淺 "shallow", 錢 "coin", 殘 "damaged", 賤 "cheap"), all supposedly sharing the sense "small" [A1]. Qing philologists turned this intuition into a working method. Duan's formula "凡从某聲皆有某義" and Wang Niansun's 王念孫 principle of "seeking ancient meanings through ancient sounds, unconstrained by graphic form" (就古音以求古義，引伸觸類，不限形體) represent two different routes [A2, A3]. Duan tied meaning to the phonetic component. Wang tied it to the spoken word, whatever graph happened to write it. Zhang Taiyan 章太炎 and Huang Kan 黃侃 then systematised word-family research under two relations: *biànyì* 變易 (the same word written differently) and *zīrǔ* 孳乳 (a new word derived from an old one with a differentiated meaning) [A4, A5]. Recent work on Zhang's *Wénshǐ* 文始 stresses that what separates *zīrǔ* from *biànyì* is precisely whether the meaning has diverged (Zhu 2021) [B9]. In other words, *zīrǔ* is the tradition's closest analogue to derivation.

Shen Jianshi's 沈兼士 1933 survey remains the standard modern treatment of *yòuwén* [A6]. It distinguished cases where the phonetic genuinely signals meaning from cases where it is merely borrowed for its sound. Yang Shuda 楊樹達 applied the method to hundreds of individual characters [A7]. Wang Li 王力, by contrast, criticised *yòuwén* for organising etymology by graph rather than by word, even though his own *Tóngyuán zìdiǎn* 同源字典 relies heavily on phonetic series in practice [A8]. Zeng Zhaocong 曾昭聰 (2000) documents this tension in detail [A10].

Since the 1990s the discussion has moved to the "source-indicating function" (*shìyuán gōngnéng* 示源功能) of the phonetic. This line of work is associated with Wang Ning's 王寧 theory of character configuration [B8] and was developed in monographs by Zeng Zhaocong (2002) [B2] and, most recently, Chen Xiaoqiang (2021) [B1]. Chen proposes a "comparative cross-verification of phonetics" (聲符比較互證法). It examines characters built on *different* phonetics that are homophonous or near-homophonous, in order to escape *yòuwén*'s dependence on a single graph. A 2022 review singles out "substituting the character for the word" (以字代詞) as *yòuwén*'s central weakness (Chen Shuo 2022, reviewing [B1]). Parallel work models the semantics of word families more abstractly: as "etymological meaning" built from meaning components (Huang Yiqing 2007) [B4], or as a shared "core meaning" underlying polysemy and cognation (Wang & Wang 2014) [B7]. Zhang Bo (2003) supplies explicit procedures for verifying that two words belong to the same family [B3].

Three observations follow from this tradition. They define the gap the present study addresses.

1. **The tradition treats *yìshēng* mainly as a problem of character classification.** The standard question has been which of the "six scripts" (六書) a *yìshēng* character belongs to: meaning-compound, phonetic compound, or both. Duan's "會意兼形聲" answers that question. What the answer implies about the *words* being written has not been examined as a separate issue.
2. **Traditional evidence for shared meaning is qualitative and selective.** Neither the *yòuwén* literature nor the *shìyuán* literature reports what proportion of a phonetic series, or of Xu's *yìshēng* set, actually shares the claimed meaning. Nor does it compare that proportion with a baseline.
3. **The phonological side is left implicit.** Traditional scholars required the two words to be "the same or similar in sound" (音同音近). They did not ask whether the particular sound difference between base and derivative is a *regular* one, of the kind a morphological process would produce.

### 2.2 Old Chinese word families as morphology

A separate tradition, largely in Western languages, reached the same materials from historical phonology. Karlgren (1934) argued that Chinese vocabulary is organised into word families rather than into thousands of isolated monosyllables [C1]. Sagart's encyclopaedia entry summarises this view as an argument for comparing word stems rather than individual words [C10]. Pulleyblank (1973, 2000) reinterpreted the phonological differences within word families as the traces of prefixes, suffixes and vowel alternations [C2, C3]. From that point on, the question became one of morphology.

The modern consensus rests on three bodies of evidence.

- **Xiéshēng series (phonetic series).** The pronunciations of characters that share a phonetic constrain the reconstruction of Old Chinese onsets and codas. Sagart and Baxter (2012) use exactly this evidence, together with word-family semantics, to reconstruct a causative/denominal prefix *s- [C8]. Mei (2012) makes a complementary argument for a causative *s- and a nominalising *-s [C7].
- **Readings in the commentarial tradition.** Jacques (2022) argues that sound glosses in early commentaries, which record "tone-change" or "voicing-change" readings (破讀), are reliable evidence for morphological alternations. He argues further that these alternations are directly relevant to syntactic analysis [C12]. Jacques (2016) and Zhang Shuya (2022) show that the departing tone (*qùshēng*, from *-s) is not a single suffix but several, including nominalisation, argument demotion and adverbialisation [C11, C13].
- **Reconstruction systems.** Baxter and Sagart (1998) survey the word-formation processes of Old Chinese [C4]. Sagart (1999) separates roots from affixes [C5]. Baxter and Sagart (2014) integrate both into a full reconstruction [C9]. Schuessler (2007) provides an etymological dictionary with explicit word-family judgements [C6].

Hill and List (2019) take an important methodological step [C15]. They model character formation as a directed graph in which each character points to its phonetic, and they use network analysis to test competing hypotheses in Old Chinese phonology. Some distinctions, such as the type A/B contrast, turn out to be encoded in the choice of phonetic, while others do not. The broader lesson is that the *Shuōwén*'s graphic analyses can be treated as data and tested systematically, rather than cited example by example.

This tradition, however, has a mirror-image gap to the one in §2.1. Historical phonologists have treated commentarial readings (Jacques 2022) and phonetic series (Sagart & Baxter 2012) as evidence for morphology. They have not asked whether Xu Shen's *own metalinguistic labels* carry such evidence. A *yìshēng* annotation is a native speaker-scholar's judgement that a character contains a meaningful and a phonetic component *at the same time*. If Old Chinese derivation left regular phonological traces, and if Xu Shen was sensitive to derivational relatedness, then *yìshēng* characters should differ from their base in precisely those regular ways more often than ordinary phonetic compounds do.

A handful of well-known *yìshēng* pairs suggests that the idea is worth testing. In the Dà Xú fǎnqiè readings, 娶 (七句切) differs from 取 (七庾切) only by departing versus rising tone. 仲 (直衆切) differs from 中 (陟弓切) by departing versus level tone, together with a voiced initial. 坪 (皮命切) is departing tone against level-tone 平 (符兵切). 吏 (力置切) is departing tone against rising-tone 史 (疏士切). The departing tone is exactly the reflex of the *-s suffix(es) discussed above. These examples are illustrative only. They were not sampled, and 婚 and 昏 (both 呼昆切) show that not every pair differs. They motivate a systematic test rather than replacing one.

### 2.3 Writing and language: why a graphic label can bear on morphology

An obvious objection is that *yìshēng* is a statement about a graph, not a word. The grapholinguistic literature makes this objection precise, and it also shows how it can be answered.

Qiu Xigui's standard account distinguishes components that function as semantic signs, phonetic signs and mere marks, and treats "meaning-compound-cum-phonetic" characters as a subtype of phonetic compounds [D1]. Boltz (1994) argues that the phonetic compound arose when a single graph was extended to write several related words and was then disambiguated by an added signific. On this view the phonetic of a derived word is often the graph of its base word [D2]. That account predicts exactly the configuration that *yìshēng* describes. Excavated manuscripts show, however, that early scribes varied their choice of phonetic considerably [D3]. The configuration preserved in the *Shuōwén* is therefore partly a Han-dynasty standardisation and not a direct record of how the words were derived.

General theories of writing supply the vocabulary needed to keep these levels apart. Meletis (2020) distinguishes graphematic units from the linguistic units they relate to, and the relations between them [D6]. Handel (2019) classifies Chinese-type scripts as morphosyllabic: each graph corresponds to a syllable that is typically a morpheme [D4]. Myers (2019) argues that the internal structure of Chinese characters has a grammar of its own, open to the same productivity-based analysis as morphology [D5]. Huang, Wang and Chen (2022) present corpus evidence that the character remains an indispensable unit in Chinese linguistic analysis alongside the word [D7]. Zhang Liulin (2023) argues that the character script contributed to making Old Chinese morphology invisible to later analysis [C14].

Taken together, this work suggests a clear condition. A graphic label such as *yìshēng* can count as evidence about morphology only if it can be shown to *covary* with independent linguistic evidence, namely regular phonological relations between the words written. The present study tests that condition directly, using reconstructions that were built independently of Xu Shen's labels.

### 2.4 Roots, words and derivational relatedness in morphological theory

Morphological theory offers two competing ways to state what *yìshēng* might encode. Each makes different predictions.

**Root-based derivation.** In Distributed Morphology, roots are category-neutral and receive their interpretation from the first category-assigning head they combine with. Arad (2003) states the locality condition: "Roots are assigned an interpretation in the environment of the first category-assigning head with which they are merged," and "once the root has merged with a category head and formed a word, its interpretation is fixed" [E3]. Arad distinguishes *root-derived* formations from *word-derived* formations. Root-derived formations can take many unpredictable meanings from the same root. Word-derived formations inherit, and semantically entail, the meaning of an existing word. Harley (2014) goes further and argues that roots are individuated only by abstract indices, not by their sound or meaning [E4]. Rasin, Preminger and Pesetsky (2024), however, re-examine Arad's Hebrew data. They find that the claimed correlation between unpredictable meaning and root-derived status does not hold: some denominal verbs also have meanings that cannot be predicted from the noun [E12].

**Word-based derivation.** Aronoff (2007) defends the lexicalist position that lexemes, not morphemes, are the basic meaningful units, and he cites Hebrew verbal roots that have robust formal properties but no constant meaning [E1]. In a related paper, Aronoff (2013) treats the root as a purely morphological object [E2]. Work on derivational paradigms treats families of related words as structured sets whose members predict one another (Hathout & Namer 2019; Bonami & Strnadová 2019) [E9, E10]. From this perspective, the relevant unit is not a meaningful root but a *derivational family* whose members are linked by recurrent form–meaning relations.

The distinction between root-derived and word-derived formations maps closely onto the traditional contrast between *yìshēng* compounds and ordinary phonetic series. A *yìshēng* character is, by Xu Shen's own description, built on a component that is *itself a word*, whose meaning the new character includes: 娶 "to take a wife" contains 取 "to take", and 仲 "middle brother" contains 中 "middle". This matches Arad's diagnostic for word-derived formation, in which the derivative entails the meaning of its base. A classic *yòuwén* series such as 戔 is different. Its members share, at most, an abstract and underspecified meaning ("small"). No member's meaning entails that of the phonetic character, and many members share nothing at all. That is the profile of root-derived formation, or of no morphological relation. The present study therefore predicts that *yìshēng* pairs should show (i) a higher rate of meaning entailment, and (ii) a higher rate of regular affixal sound differences, than ordinary phonetic compounds built on the same phonetics.

A third body of work concerns sound–meaning systematicity below the level of the morpheme. Kwon and Round (2015) apply canonical typology to phonaesthemes such as English *gl-* or *sl-*. They find that what sets phonaesthemes apart from roots is that they are canonically "accompanied by non-recurrent residues" [E5]. Bergen (2004) shows that such units have psychological reality [E6]. Monaghan et al. (2014) and Dingemanse et al. (2015) show that form–meaning systematicity across a lexicon is weak but statistically robust, and they distinguish it from iconicity [E7, E8]. For Chinese specifically, Meng, Wan and Kit (2025) report robust sound-symbolic clustering across historical rhyme dictionaries [C16]. This literature supplies a baseline expectation. Some degree of meaning-sharing within a phonetic series is expected even without derivation, simply from lexical systematicity. Any claim that *yìshēng* marks derivation must therefore show an effect *above* that baseline.

### 2.5 Synthesis: the gap and the hypotheses

The three literatures meet at a point none of them has examined.

- Traditional philology has an explicit native category, *yìshēng*, that it has discussed almost entirely as a matter of character classification (§2.1).
- Historical phonology has a well-developed inventory of derivational affixes and alternations, and it accepts native commentarial readings as evidence for them. It has not tested Xu Shen's structural labels in the same way (§2.2).
- Morphological theory provides an explicit contrast between word-derived and root-derived formation, and a baseline expectation of sub-morphemic systematicity. Neither has been applied to Chinese graphic analysis (§2.4).

The present study asks whether *yìshēng* annotations *covary* with independent evidence of derivation. Three hypotheses follow; the method is laid out in §3.

- **H1 (phonological regularity).** The sound difference between a *yìshēng* character and its phonetic character belongs to the class of attested Old Chinese affixes and alternations (e.g., *s-, *N-, *m-, *-s, *-ʔ, voicing, type A/B) more often than the sound difference between ordinary phonetic compounds and their phonetic characters, when both are drawn from the same phonetic series.
- **H2 (semantic entailment).** The *Shuōwén* gloss of a *yìshēng* character entails the meaning of its phonetic character more often than the glosses of ordinary phonetic compounds do. This is Arad's diagnostic of word-derived formation.
- **H3 (recension variance).** Where the Dà Xú and Xiǎo Xú 小徐 recensions disagree over whether a character is *yìshēng*, the disputed items should fall between the two groups on H1 and H2. If they do, the label reflects a graded judgement of derivational transparency, not an arbitrary transmission error.

If H1 and H2 hold, *yìshēng* would be the earliest explicit, systematic metalinguistic record of derivational relatedness in Chinese. It would also offer a principled answer to the *yòuwén* debate: the phonetic "carries meaning" when, and to the extent that, it writes the base of a word-derived formation. Otherwise it merely indexes sound, and any meaning shared across the series is the weaker, root-level or phonaesthemic systematicity described in §2.4. If H1 and H2 fail, the result is still informative. It would show that Xu Shen's *yìshēng* is a graphic and exegetical category that does not track morphology, which supports Wang Li's and Chen Xiaoqiang's warnings against "substituting the character for the word".

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
- Huang, Chu-Ren, Hongjun Wang & I-Hsuan Chen. 2022. Characters as basic lexical units and monosyllabicity in Chinese. In C.-R. Huang et al. (eds.), *The Cambridge Handbook of Chinese Linguistics*, 74–96. Cambridge: Cambridge University Press. [D7]
- Huang, Yiqing 黃易青. 2007. 上古漢語同源詞意義系統研究. Beijing: Shangwu yinshuguan. [B4]
- Jacques, Guillaume. 2016. How many *-s suffixes in Old Chinese? *Bulletin of Chinese Linguistics* 9(2). [C11]
- Jacques, Guillaume. 2022. On the nature of morphological alternations in Archaic Chinese and their relevance to morphosyntax. *Bulletin of SOAS* 85(3): 475–494. [C12]
- Karlgren, Bernhard. 1934. Word families in Chinese. *Bulletin of the Museum of Far Eastern Antiquities* 5: 9–120. † [C1]
- Kwon, Nahyun & Erich R. Round. 2015. Phonaesthemes in morphological theory. *Morphology* 25(1): 1–27. [E5]
- Mei, Tsu-lin. 2012. The causative *s- and nominalizing *-s in Old Chinese and related matters in Proto-Sino-Tibetan. *Language and Linguistics* 13(1): 1–28. † [C7]
- Meletis, Dimitrios. 2020. *The Nature of Writing: A Theory of Grapholinguistics*. Brest: Fluxus Editions. [D6]
- Meng, Yingying, Yuwei Wan & Chunyu Kit. 2025. Sound symbolism is not "marginal" in Chinese: Evidence from diachronic rhyme books. *PLOS ONE* 20(5): e0322044. [C16]
- Monaghan, Padraic, Richard C. Shillcock, Morten H. Christiansen & Simon Kirby. 2014. How arbitrary is language? *Philosophical Transactions of the Royal Society B* 369(1651): 20130299. [E7]
- Myers, James. 2019. *The Grammar of Chinese Characters*. London: Routledge. [D5]
- Pulleyblank, Edwin G. 1973. Some new hypotheses concerning word families in Chinese. *Journal of Chinese Linguistics* 1(1): 111–125. [C2]
- Pulleyblank, Edwin G. 2000. Morphology in Old Chinese. *Journal of Chinese Linguistics* 28(1): 26–51. [C3]
- Qiu, Xigui. 2000. *Chinese Writing*. Trans. Gilbert L. Mattos & Jerry Norman. Berkeley: Society for the Study of Early China. [D1]
- Rasin, Ezer, Omer Preminger & David Pesetsky. 2024. A re-evaluation of Arad's argument for roots. In Robert Autry et al. (eds.), *Proceedings of the 39th West Coast Conference on Formal Linguistics*, 382–392. Somerville, MA: Cascadilla Proceedings Project. [E12, new]
- Sagart, Laurent. 1999. *The Roots of Old Chinese*. Amsterdam: John Benjamins. [C5]
- Sagart, Laurent. 2015. Word families. In Rint Sybesma (ed.), *Encyclopedia of Chinese Language and Linguistics*. Leiden: Brill. [C10]
- Sagart, Laurent & William H. Baxter. 2012. Reconstructing the *s- prefix in Old Chinese. *Language and Linguistics* 13(1): 29–59. † [C8]
- Schuessler, Axel. 2007. *ABC Etymological Dictionary of Old Chinese*. Honolulu: University of Hawai'i Press. [C6]
- Shen, Jianshi 沈兼士. 1933. 右文說在訓詁學上之沿革及其推闡. In 慶祝蔡元培先生六十五歲論文集; reprinted in 沈兼士學術論文集, Beijing: Zhonghua shuju, 1986. [A6]
- Shen, Kuo 沈括. 夢溪筆談, juan 14. [A1]
- Wang, Li 王力. 1982. 同源字典. Beijing: Shangwu yinshuguan. [A8]
- Wang, Ning 王寧. 2015. 漢字構形學導論. Beijing: Shangwu yinshuguan. [B8]
- Wang, Niansun 王念孫. 1796. 廣雅疏證. [A3]
- Wang, Yunlu 王雲路 & Wang Cheng 王誠. 2014. 漢語詞彙核心義研究. Beijing: Shangwu yinshuguan. [B7]
- Xu, Shen 許慎. 100 CE. 說文解字. Dà Xú recension; facsimile Beijing: Zhonghua shuju, 1963. Digital text: shuowenjiezi/shuowen (GitHub, Apache-2.0).
- Yang, Shuda 楊樹達. 1983 [1937]. 積微居小學金石論叢 (enlarged edition). Beijing: Zhonghua shuju. [A7]
- Zeng, Zhaocong 曾昭聰. 2000. 王力先生有關形聲字聲符示源功能的研究述評. 中國語文通訊 55. [A10]
- Zeng, Zhaocong 曾昭聰. 2002. 形聲字聲符示源功能述論. Hefei: Huangshan shushe. [B2]
- Zhang, Bo 張博. 2003. 漢語同族詞的系統性與驗證方法. Beijing: Shangwu yinshuguan. [B3]
- Zhang, Liulin. 2023. Has Chinese always been an analytic language? Effects of writing on language evolution. *Language and Semiotic Studies* 9(4): 576–597. [C14]
- Zhang, Shuya. 2022. Rethinking the *-s suffix in Old Chinese: With new evidence from Situ Rgyalrong. *Folia Linguistica* 56: 129–167. [C13]
- Zhang, Taiyan 章太炎. 文始. In 章太炎全集. Shanghai: Shanghai renmin chubanshe. [A4]
- [Author to be confirmed]. 二徐本《說文》亦聲字差異探討. KCI-indexed Korean journal, article ART002078031. [E13; title only]
- Huang, Kan 黃侃. 1983. 文字聲韻訓詁筆記, ed. Huang Zhuo 黃焯. Shanghai: Shanghai guji chubanshe. [A5]
- Zhu, Lechuan 朱樂川. 2021. 試論變易與孳乳中形音義的關係——以章太炎《文始》為例. 漢字漢語研究 2021(4). [B9]
