# *Morphology* 2026 研究文章 Discussion 精读：从数据到理论创新

阅读日期：2026-09-28。执行：Claude。对象：本仓库 Release [`学习`](https://github.com/WuYusen825/Morphology/releases/tag/%E5%AD%A6%E4%B9%A0) 中的 11 篇 *Morphology*（Springer）第 36 卷（2026）研究文章。本文是逐篇阅读笔记；综合结论与对亦声稿的应用见 [Discussion 精读总结](Discussion精读总结.md)，阅读范围与原文入口见 [阅读范围索引](discussion_reading_index.md) 第二部分。

**怎么读的。** 每篇都完整读了摘要、引言（含研究问题与预测）、讨论与结论，以及讨论所依赖的结果段落；方法细节、例句串和附录表格按需略读，逐篇写明实际范围。重点看六件事：作者观察到什么；怎样从观察走到理论命题（桥在哪里）；哪些地方要求严谨、哪些地方允许推测；怎样联系前人的结论与理论；语言怎样标记命题的强度；篇幅怎样分配。每篇最后单列“对亦声稿的启发”。

**判断口径。** 文中“贡献”“增量”指从成文论文可以辨认的学术推进；没有审稿记录，不能断定编辑和审稿人实际因何录用。发表也不保证每一步推理都对，所以每篇都另写“我的评价”，指出可以不学的地方。

**版权。** 10 篇为开放获取（9 篇 CC BY 4.0，Lõo 等为 CC BY-NC-ND 4.0）；Barbu Mititelu 等一篇是订阅文章，笔记只转述并引用短语。PDF 均为出版社正式版（元数据 Creator = VTeX PDF Tools，Producer 含 “SPRINGER SBM; licensed version”），下载后与 Release 所列 SHA-256 逐一核对一致。

## 0. 十一篇一览

投稿到录用的间隔为 9.7–17.4 个月，中位数 14.6 个月。“讨论/结论占比”是讨论与结论章节词数占正文（不含参考文献与附录）的粗略比例，含例句与表格文字，只作比较参考。

| # | 文章（卷:号） | 类型与数据 | 讨论形式 | 讨论/结论占比 | 投稿→录用 |
|---|---|---|---|---:|---|
| P1 | Lõo, Tomaschek, Lippus & Tucker（36:11），爱沙尼亚语自发语音中的形态效应 | 在线听写实验，1000 个自发语音屈折名词，GAM | 合并的 Discussion & conclusion | 约 19% | 16.2 个月 |
| P2 | Barbu Mititelu, Iordăchioaia, Leseva & Stoyanova（36:12），英语派生后缀透明度 | WordNet 21,820 个词义对，朴素贝叶斯 vs 多数类基线 | Results and discussion（按 RQ）+ 结论 | 约 24% | 13.2 |
| P3 | Saicová Římalová（36:14），捷克语未完成体将来式的不对称超丰富性 | SYN2020 语料，20 个动词，频数与人工语义分析 | 结果内小讨论 + 总讨论 | 约 26% | 9.7 |
| P4 | Sandström & Rosenberg（36:13），瑞典语复合词与伪复合词的掩蔽启动 | 掩蔽启动词汇判断，128 个关键项 | Discussion + Concluding remarks | 约 25% | 13.5 |
| P5 | Huyghe 等 9 人（36:16），SONDE：法语动转名词语义库 | 5,272 个派生名词人工标注，分类器与潜在类别分析 | 解释嵌在结果各节，结论短 | 约 5% | 14.6 |
| P6 | Berg（36:15），名词内部语素顺序的类型学 | 472 种语言 773 例三语素名词，二项检验、卡方 | Theoretical discussion + Conclusion | 约 29% | 14.8 |
| P7 | Igartua（36:17），巴斯克语的多重表达及其历时来源 | 16 世纪以来文献与现代方言材料，Harris 类型学 | 历时、功能两节 + 结论 | 约 17% | 17.4 |
| P8 | Sandell（36:21），吠陀梵语的切分、能产性与词重音 | 《梨俱吠陀》语料，LNRE 能产性估计，贝叶斯逻辑回归 | 前人研究一节很长，讨论短 | 约 4% | 12.5 |
| P9 | Ševčíková & Hledíková（36:18），捷克语名转动词的语义透明度 | SYN2015，1,079 个转类动词与 229 个前缀派生动词 | Results and discussion（按 RQ）+ 结论 | 约 39% | 14.9 |
| P10 | Cohen, Carlson & Dussias（36:19），英语与西班牙语中的词结构时长线索 | 两个视觉情境眼动实验 | 各实验讨论 + 按 RQ 的总讨论 | 约 27% | 13.9 |
| P11 | Nikolaev, Chuang & Baayen（36:20），判别词库模型学习芬兰语屈折类 | 55,271 个词形的形式与语义嵌入，理解与产出模型 | 按 RQ 的总讨论 | 约 22% | 16.1 |

---

## P1 Lõo 等：点名自己排除不了的混淆，零结果占最多篇幅

**读的范围。** 第 1–24 页全读；§4 Discussion & conclusion 在第 20–24 页。

**设计与结果。** 132 名母语者听自发语料中截出的 1000 个屈折名词并打字；因变量分整词、词基、后缀三种准确率，另有反应时和打字时长。引言 §1.4 先写出两类加工模型（强制分解模型；学习模型）对每个因变量的预测，并列成 Table 1。结果：删音降低准确率；删音部位既影响对应部分，也跨部分影响另一部分；整词频率有小而稳定的效应；实现范式大小没有效应，与作者团队此前的视觉实验相反。

**从观察到理论。** 讨论逐项回到两类模型计分：部位内效应 “consistent with” 分解模型；跨部位效应 “less easily reconciled with” 分解模型，而学习模型预期它；整词频率 “in principle, compatible with both”，只是 “may be more naturally accommodated by” 学习模型；范式大小的零结果 “more compatible with” 分解模型。最后没有宣布胜者：“in our opinion, neither framework fully accounts for the complete pattern of effects”，并指出两类模型本来就不是为这种任务设计的。理论推进不大，但很干净：先写预测，再逐项计分，**明说哪些结果对竞争模型没有诊断力**。

**严谨与推测。** 最值得学的一步在部位效应之后：“we cannot be sure whether it is the morphemic structure or the relative location of the segment in the word that influences typing accuracy”。作者接着给出能区分二者的设计：双音节单语素词（kana）与带后缀的双音节词（maa-na）分别在第一、第二音节删音；也说明自发语料很难凑齐所需的删音位置。零结果部分先说 “surprising”，再给三个候选解释，每个都对应本研究与前作的一处具体差异：7000 万词广播语料 vs 1500 万词书面语料（社群层面 vs 个人经验）；词汇判断不必锁定具体形式 vs 打字必须锁定；自发语音变异可能掩盖小效应。随后还提出反方向的可能：语境也可能放大范式关系。

**我的评价。** 用零结果支持分解模型（absence of evidence）偏弱，好在措辞只到 “more compatible”。模型用逐步选择建立，讨论没有处理由此带来的探索性问题。结论写 “we found no evidence for paradigmatic influences”，没有写成“不存在”，这一点是对的。

**文献对话。** 常用句式是“一致 + 增量”：“This result fits well with earlier studies by Ernestus et al. … However, they did not investigate the internal morphological structure”。与自己的前作（Lõo et al. 2018a）矛盾时不回避，而是按设计差异调和。新颖性说成相对于文献的一句：“To our knowledge, paradigmatic effects in auditory comprehension have not previously been investigated using a written production task or spontaneous speech.”

**详略。** 预期内的结果每项一两段；意外的零结果约五段；结论一段。

**对亦声稿的启发。** 在讨论里点名本研究排除不了的混淆，并写出能区分它的具体设计；逐项说明哪些结果对哪种解释有诊断力（例如 v6 §4.3 的派生方向在两组相同，因而不能诊断标注）；H1b、H4 两个零结果应有篇幅，候选解释要对应具体的设计特点。

---

## P2 Barbu Mititelu 等：文献主张 → 明确预期 → 证实或挑战

**读的范围。** 第 1–29 页（§1–§8）全读，附录图表略看。订阅文章。

**设计与结果。** 用 WordNet 的 21,820 个派生词义对和 14 种形态语义关系；把“透明度”操作化为“用动词语义类、名词语义类和后缀三个特征预测关系的准确率”，以 ZeroR（总猜多数类）为基线。名词化后缀比动词化后缀可预测；ZeroV 比 ZeroN 难预测；-ate 与 ZeroV 相近；但零后缀并不比显性后缀更不透明，-ise 反而最难预测。

**从观察到理论。** 这是典型的“计分表”写法。§2 综述里每条主张都挂着具名来源，§3.1 把它们改写成可检验的预期（-ise 与 -ify 相近：Plag 1999、Valera 2023；ZeroV 比 ZeroN 难预测：Kisselew et al. 2016；零后缀最多功能：Plag 1999、Lieber 1981/2004），§7 逐条判定：“seems to be confirmed by our data”“the data confirm Valera’s (2023) observation”“these results certainly challenge the expectation …”。因为预期对应到具名作者和具体命题，挑战的对象就很精确。

**严谨与推测。** 作者意识到代理链：透明度 ← 可预测度 ← 语义类特征 + 简单分类器，并把关键假设写成条件句：“if we take high polyfunctionality to correlate with reduced predictability”；也声明做可靠分类器不在本文范围。小样本后缀（-en 只有十余对）不下结论；-ee 预测度低 “may also be due to its low frequency”。强措辞只用在有两重支持的地方，紧接着又写 “more data … are necessary to draw more reliable conclusions”。错误分析被用来检讨范畴体系本身：By-means-of 兼有“非生命致使”与“中介”两种用法，造成系统性误判，因此建议修订关系清单。

**我的评价。** 各后缀按原始准确率排序，但各自的多数类基线差别很大（-ise 从 29.75 提到 46.32，-ify 从 51.35 提到 59.03，-ise 相对基线的提升其实更大）。用原始准确率比较“透明度”，一部分比的是默认读法的占比，应比较相对基线的提升，或用机会校正指标。第一轮读到的 Bonami & Strnadová (2019) 讲的正是这种比较基准问题，这里是一个反例。

**语言。** seems to be confirmed … if we take … / which actually suggests that, at least in this dataset, … / it is surprising that … / these results certainly challenge … / may provide sufficient grounds for revising …

**对亦声稿的启发。** 讨论里可以做一张“前人主张计分表”：段玉裁（亦声即会意兼形声，另有大量“形声包会意”）、王筠（三种、归部规则、大徐误增）、右文说（凡从某声皆有某义）、Boltz（派生词的声符是基词之字）、裘锡圭（亦声是形声字的一类）——各自被证实、限定还是挑战。把残差当作检验范畴体系的材料（例如有标注却既不同音又不相关的 8 对）。比较子集（仅大徐 vs 两本共有）时，要说明各自的基线。

---

## P3 Saicová Římalová：逐条套用既有类型学，并提出修订

**读的范围。** 第 1–14 页全读；第 14–23 页的结果表与分析段落读过，例句串（约第 15–18、23–27 页）只略读；§4.1.3、§4.2.3、§4.3、§5 全读（第 20–21、27–32 页）。

**设计与结果。** 用 SYN2020 语料（约 1 亿词）考察 7 个核心定向动词与 13 个文献列为有 po- 将来式的其他未完成体动词；方法是频数加人工语义分析，没有推断统计。未完成体动词构成连续谱：只有分析式 → 两式并存 → 只有综合式（jít、jet）；两式并存时总是不对称；综合式偏向运动义，但不是互补分布。

**从观察到理论。** 讨论分两层。结果内的小讨论解释模式并提出原因：分析式歧义较少、更易识别为将来；高频不规则形式受频率保护（借 Bybee 1985/2006 的机制）；某些动词偏好综合式 “could be a remnant” of 历史上的定向与不定向对立。§5 则逐条套用 Thornton (2019) 超丰富性典型性类型学的四条标准。其中“受影响词位的数量”这条会把此现象判为边缘，按使用频率看却并不边缘，于是提出修订：“This all supports the suggestion that the frequency of the affected lexemes in usage should be considered another criterion when evaluating overabundance.” 这是全文的主要理论贡献，也占了讨论的最大篇幅。随后又用结果细化 Bonami (2015) 对迂说式的 split/nested 分类（“Using my results, I can specify that …”）。

**严谨与推测。** 反复声明语料未见不等于不存在（“the fact that the forms were not found in the corpus does not mean that the forms do not exist”）；反驳旧说时留余地，因为旧文献描述的可能是几代人以前的语言。借 Bermel & Knittl 的“语料比例与可接受度”关系作桥，同时说明名词屈折的结论能否推到动词将来式还需研究。原因推测都标明身份（One reason could be … / I believe that … / My interpretation of this finding is based on the argument that …）；最远的问题写成问句（Why does motion play an important role in the data? Do the data reflect …?）。

**我的评价。** 语义分布没有统计检验，语义分类由作者一人完成；13 个动词按“有运动义”等标准选出，本身偏向运动义；“运动义比定向性更重要”只靠 růst ‘生长’一个动词支撑，作者用两个 may 限定，但这仍是全文最弱的一环。“The research shows that semantics is important” 对描述性计数来说偏强。

**文献对话。** 用语料检验旧文献的直觉描述，并**给含糊的“一致”降价**：“corresponds to observations in the literature …, but those statements are so general that this conclusion has little value”。并列相互冲突的文献而不强行裁决（空间义起作用：Klavan 2020；未发现生命度、具体度的影响：Aigro & Vihman 2024）。最后把个案上升为对一般理论的贡献：“Czech linguistic data may also contribute to a deeper understanding of the diversity of the phenomena of overabundance and inflectional periphrasis.”

**对亦声稿的启发。** v6 实际上已在逐条检验王筠的类型学（三种、归部规则、大徐误增）。可以更明确地写：哪一条经受住了全体检验，哪一条（归部）会给出误导性判断，因而**建议怎样修订**：以词际关系而不是归部来界定第三种。v6 §4.6 “informative but non-exhaustive indicator” 与“语料未见 ≠ 不存在”同构，可以在讨论里写成一个方法论命题。

---

## P4 Sandström & Rosenberg：设计诊断性对比，用否定后件式驳竞争理论

**读的范围。** 第 1–24 页全读（引言、理论背景、方法、结果、§5 Discussion 第 19–23 页、§6 Concluding remarks 第 23–24 页）；附录模型表略看。

**设计与结果。** 掩蔽启动词汇判断（启动词呈现 50 ms），97 名被试在线完成；关键项分真复合词（透明到不透明）、伪复合词（matros = mat + ros）、正字法对照（krokus = krok + *us），目标都是第一个嵌入名词；透明度由 8 名语言学者评分。真复合词稳健启动（−28 ms）；伪复合词和正字法对照都无启动，两者没有差别；复合词内部透明度不调节启动量。

**从观察到理论。** 设计中有一个**对竞争理论有诊断力的对比**：分解模型预期伪复合词强于正字法对照，联结模型预期两者相同。讨论先交代主张的证据基础（“Our claim that … is based on the finding of …”），再用否定后件式驳竞争理论：“If segmentation were automatically triggered by surface structure alone, pseudo-compounds should have activated their embedded strings. They did not.” 最后一句只有三个词，力度很强。对透明度的零结果，作者用组间结果重新定位：“Importantly, this null effect does not imply that semantics is irrelevant”——语义关系是启动的必要条件，程度则不再起作用，至少在掩蔽条件下如此。再把相互矛盾的文献按加工阶段整理：掩蔽启动看不到透明度效应，语义启动、眼动这类晚期范式看得到，“are not contradictory, but instead point to distinct temporal phases of word recognition”。

**严谨与推测。** 限定范围的短语贯穿全文（at least not regarding words with a potential compound structure / at least under masked priming conditions）；探索性的分位数分析明确降级（should be interpreted cautiously. Nevertheless, …）；解释他人不同结果时指向具体刺激问题。

**我的评价。** 伪复合词与对照“无差别”不是等价性证明（没有做等价检验，伪复合词只有 31 项）；伪复合词读音与真复合词不同，这是一个真正的替代解释，作者只用间接文献缓解；摘要里 “challenge accounts positing a semantically blind … stage” 比讨论中的限定更强。

**文献对话。** 引对手原话来反驳（“morpho-orthographic full decomposition”，Beyersmann & Grainger 2023: 32），反驳对象精确到一条原则。同样的结果、不同的解释：Gagné et al. (2018) 也没发现伪复合词启动，但解释为“激活后被抑制”；本文说“激活不足”，并指出对方刺激有歧义切分（crowding 可切成 crowd-ing 或 crow-ding）——“This observation is relevant regardless of one’s theoretical perspective.” 承认对立证据（伪派生启动有人复现、有人没复现），再说明为何伪派生与伪复合表现不同。

**对亦声稿的启发。** 把竞争解释的预测写成可以被否定的形式，再用短句收束：若亦声只是字形分类（形声字的一类），它不应在同音、去声和语义相关上与同声符的普通形声字不同——它不同；若亦声标的是一般派生，H1b 应成立——它不成立。“存在 vs 程度”的重定位可以用于 H1b：标注追踪的是最小关系（同词、*-s），而不是有没有词缀关系。按层次化解文献矛盾：裘锡圭的字形分类与 Boltz 的造字史不必二选一，标注正处在二者的接口。

---

## P5 Huyghe 等：资源论文怎样检验具名理论命题

**读的范围。** 第 1–7 页（引言、取样）、第 14–16 页（标注程序与信度）、第 24–49 页（§3.2–§3.4 与 §4 结论）全读；第 7–14 页的语义描述体系和第 16–24 页的描述性分布略读。

**设计与结果。** 从 108 亿词网络语料中抽出 59,353 个候选对，人工筛得 5,272 个派生名词（42 个后缀与 4 种转类）；在义项层面标注语义类型、词汇体和论元语义角色。义项数的标注者一致性只有 ICC .54，作者因此改用词典义项清单，减少任意性；特征标注 κ 为 .67（PABAK .79）。全部标注约 2,200 小时。

**从观察到理论。** 本文没有独立的 Discussion，推理嵌在各小节里，有三个动作值得学。

- **先给直截了当的解释，再说明它为什么不够。** 多功能性的“经济性”解释（形式少、功能多）；作者用三条理由说明这种静态解释不充分：形式的数量会变；若按互补分配，平均每个过程只需 1.7 个功能，实际是 8.9 个；它也不解释意义的动态扩展。然后用条件概率的不对称找出功能间的扩展方向，构成网络，并用 2000 个同规模随机网络检验其中心化程度。
- **替对手设想退路，再把退路堵上。** 点名要检验的理论 Aspect Preservation Hypothesis（Fábregas et al. 2012），并引用其“最细致的表述”（Fábregas & Marín 2017: 157）。结果是 94–97% 的名词保持动词的体特征；作者随即替 APH 设想一条退路：“it can be asked whether aspectual differences … are idiosyncratic and reflect the effects of lexicalization rather than morphological derivation, in which case they would not violate the APH”。再用两条证据堵住：不保持体特征的情况与派生过程系统相关；没有经过词汇化的新造词也有 15% 不保持（引自己的前作）。结论是 “cannot be viewed simply as random opacification caused by lexicalization”。
- **对预测不好的部分诚实。** agent 名词是否带论元，模型只把准确率从 .750 提高到 .768，作者写 “poorly predicted”，并提出一个具体的补充假说（临时施事与职业施事之别）。

**严谨与推测。** 每个分类器都报基线；“显著但微弱”如实报告（“accuracy of .870, only marginally higher than the No Information Rate baseline of .859 … nevertheless statistically significant”；Cramér’s V “negligible to moderate”）。分析决定写成显式假设（“we postulated that a derivational semantic function can be identified when at least two nouns … instantiate the same combined semantic type”）。

**我的评价。** 有些结论措辞比证据强：分类器只比基线高一两个百分点的地方，结论仍写 “making it an inherent part of morphological processes”；中心化检验的零模型是同密度随机图，未必合适。

**文献对话。** 把前人的描述性发现（Balvet et al. 2011 报告 23% 不一致）推进为对理论命题的检验；指出句法学的名词化研究对词汇层面的作用 “uncertain and underexplored”；把派生中的同义双式与屈折中的超丰富性作跨域类比。

**对亦声稿的启发。** 学“替对手设想退路再堵住”。v6 的三条主要退路都已有证据，但散在方法、结果和局限里，讨论中应写成“一条退路—一项证据”的对应：同音效应只是许慎以声符释字的副产品（去掉声训后仍成立）；只是宋代大徐增标的产物（两本共有的 140 条上仍成立）；只是声符系列基线不同（按声符聚类的 GEE、匹配声符的比较）。学“先给直截了当的解释，再说明为什么不够”：亦声只是会意兼形声的字形分类——这个解释预测不出与同声符普通形声字在同音、*-s 和语义上的差别。

---

## P6 Berg：从经验概括走到解释原则，并推出数据以外的预测

**读的范围。** 第 1–12 页全读；第 12–24 页的数据分析读各小节结论、两处 interim summary 和 §4.4 镜像假说；§5 Theoretical discussion 与 §6 Conclusion 全读（第 24–31 页）。致谢中感谢主编 Bonami “extraordinarily close engagement with my manuscript”。

**设计与结果。** 搜检 2800 种语言的语法书，收集由一个词干与两个黏着语素构成的名词；每个语属（genus）取一种语言，得 472 种语言 773 例；只用二项检验和卡方，按大区分列。词干-后缀-后缀最常见（63%），前缀-词干-后缀 33%，前缀-前缀-词干 3.8%；领属标记偏向词首，但只见于约一半大区；镜像假说因数据太少无法检验。

**引言里先把理论准备好。** 逐字引出 Greenberg 共性 28、39，拆成两部分，指出前缀域的镜像部分从未检验；强调这些共性是经验概括，“do not explain typological patterns but are themselves in need of an explanation”。为好的解释原则立三条标准（普遍、无需先行分析即可应用、能处理同一范畴有的语言作前缀有的作后缀），据此排除 Baker 的 Mirror Principle（依赖各语言的句法推导，给不出一般预测），也排除只管词缀序列的可解析性解释——对后者他写道：“Such accounts have nothing to say about why the grammatical categories were prefixed or suffixed to the stem. Nor should they be expected to.”选定三条候选原则并写出互相冲突的预测；还预先写出 Urgency Principle 的证伪条件：若它有明显的区域效应，“we would be forced to argue that that which is regarded as urgent varies from one linguistic community to another. This would be an uncomfortable position to be in.”

**从观察到理论。** 讨论按一条链推进：
1. 原则预测的序列比数据能分辨的更细，“Critically, this does not imply that the principles make false predictions”——区分“未证实”与“被证伪”。
2. 领属标记的行为两条主原则解释不了；用预先写好的证伪条件排除 Urgency：“Nobody would want to argue that possession is less ‘urgent’ in Eurasia than in South America.”
3. 重新描述待解释现象：领属前置即“人称前置”，把自己动词研究中的原则推广到名词并改名为 Person-First（“I contend that …”）。
4. 让原则相互竞争，推出新预测：违反两条原则的顺序应接近零——“This is exactly what we find”；并立即限定：“this explanation does not predict that the three non-occurring orders are impossible. It rather predicts that they are highly unlikely.”
5. 用理论对数据之外的范畴做预测（附加标记应在词外缘；增大词应与指小词同位），“A test of these predictions must await future work.”
6. 回应一个统一理论（Hahn et al. 2021 的加工效率）：经验上，人称标记对后续词项预测力低却偏向词首，统一原则解释不了；元理论上，最大普遍性 “is bought at the expense of a loss of explanatory depth”，而具体原则反过来为一般原则提供内容。

**我的评价。** Person-First 是看到领属数据后提出的，靠动词研究和少数拆分语言支撑；“原则强弱因区而异”没有独立测量，与他批评 Urgency 的循环风险是同一类；“Nobody would want to argue” 是修辞而不是检验。

**语言。** I contend that / We may therefore re-interpret … as … / Critically, this does not imply that … / This is exactly what we find / a case can be made for / The bleak conclusion is that … / The answer appears to be in the negative / The bottom line is that …

**详略。** 讨论集中在“领属的异常 → 新原则 → 原则竞争”这条链上；已证实的部分一两句带过；局限嵌在各处结论里。

**对亦声稿的启发。** v6 的核心结论（亦声标的是同一个词或最小派生的新字形）仍是经验概括。讨论可以再走一步，提出一个解释原则，说明为什么标注集中在最小关系上，并推出数据以外的可检验预测。预先写出证伪条件：若亦声只是大徐的编辑产物，两本共有的 140 条上效应应当消失；若王筠的归部规则抓住了这种关系，归本部的字应更常同音。区分“未证实”与“被证伪”：H1b 不成立不等于标注与派生无关，H4 不成立不等于王筠的第三种不存在。

---

## P7 Igartua：长时段文献检验理论的历时推论（与亦声稿最接近）

**读的范围。** 第 1–11 页（引言、§2 理论与语言多样性、§3 分类）全读；§4、§5 的现代与历史材料略读，§4.5、§5.3.1–5.3.2、§5.6 全读（第 27–39 页）；§6–§8 全读（第 39–46 页）。致谢主编 Bonami 与匿名审稿人；脚注 37 直接写入审稿人提出的替代分析。

**设计与论点。** 以 Harris (2017) 的多重表达（multiple exponence, ME）四类型学为框架，整理现代巴斯克语与 16 世纪以来文献（Dechepare 1545、Leiçarraga 1571、Lazarraga 手稿、Refranes y sentencias 1596 等）中的 ME。核心论点：巴斯克语的 ME 四类俱全，并长期存续，不是注定很快消失的残迹；另对 Harris 类型学提出两点修订。

**从观察到理论。** 引言先精确引用 Harris 的定义，指出它把 ME 限于词内——这正是后文要挑战的边界。再梳理否认或贬低 ME 的理论阵营，并指出这些立场的**历时推论**：若在历史上看到 ME，就会把它看成 “weird and highly unstable, that is, doomed to die out quickly”。这样历时材料就有了明确的检验对象。讨论归纳产生 ME 的途径（屈折外化、再加缀、聚合类推、音变，以及“rather speculatively”的语法化）和消失途径（重新切分；外化过程中的简化），再用冗余的功能证据（噪声下的词识别、儿童学习）解释为何 ME “dies hard”（Stolz 2010 语）。

**语文学证据怎样支撑理论。**
- 同一文本中单标与双标形式并存，说明双标是活跃的 ME，而不是冻结残迹。
- **用文本内的频率裁决两种解释。** 有人把 -reanik 看成单标 -rean 衰落的证据；但在已出现 -reanik 的 Lazarraga 手稿中，-rean 仍占绝对优势（-reanik 只出现 6 次），所以更可能是强化而不是替换——虽然它最终确实取代了单标形式。
- **分级评价竞争的词源假说。** 一种 “can hardly be deemed plausible”；另一种 “appears to be better grounded … although it is still, inevitably, not free of a considerable degree of speculation”。对远源推测直说不能当证据：“too remote and speculative to serve as minimally reliable evidence.”

**严谨与推测。** 结论用一句整体限定（“if the analyses offered in the foregoing discussion are not flawed”），而不是逐句加 may；历时途径按可靠程度分级；功能解释借外部实验证据；与遗传冗余的类比只作 “rather close parallel”。

**我的评价。** 没有系统的频率统计，结论依赖精选例证；存续的例子多，消失的例子篇幅少，有选择性风险。

**文献对话。** 以一部权威类型学为骨架组织全部材料，再在骨架上提修订；找出对立理论的历时推论，让历时材料去检验它；与 Crow、Rarámuri、阿尔巴尼亚语、Maay 的平行研究对照。

**对亦声稿的启发。** 大徐、小徐、段注三层文本与 Igartua 的多时代文献同构。可以学他用文本内部的共存与频率来裁决解释：例如仅大徐有的 62 条是“扩标”还是“误增”，除同音率外，还可以看大徐在同一部首、同一声符系列的同类字上是否时标时不标（这是需要另行执行的新分析）。学他分级评价竞争解释的措辞，用于王筠、段玉裁与现代学者的不同说法。学他先找出对立理论的历时推论：若亦声只是后人附加的字形术语，它不应在两本共有的层次上就与同音、*-s 和语义相关——而它在 140 条共有标注上就有这种关联。

---

## P8 Sandell：显式写出桥接假设，并用方法质量裁决前人研究

**读的范围。** §1 引言（第 1–5 页）全读；§2 吠陀重音分析只读小节首尾（第 5–15 页略读）；§3 前人研究、§4 语料与统计、§5 讨论与结论全读（第 15–40 页）。属于 Cohen 与 Dabouis 主编的专题。

**设计与结果。** 以《梨俱吠陀》全文（164,766 个词例）为语料，比较三个重音一致的后缀（-vant-、-ín-、-tvá-）与三个重音不定的后缀（-ti-、-tu-、-is.-）。用 Baayen 的 𝒫 衡量能产性，并用 LNRE 模型外推到同一样本量以便比较。能产类重音一致、非能产类重音不定（六个类别的相关 r = −0.738，p = 0.094，只写作 “suggests”）；低频词更常是起首的默认重音（Wilcoxon r = .391；贝叶斯逻辑回归中对数频率系数的可信区间不含 0）。

**把心理语言学接到历时演变的桥。** 综述形态加工的双路径模型与 Hay & Baayen 的“能产性—可切分性”之后，作者明写桥接假设：“I cautiously assume that this more robust representation extends to all arbitrary phonological aspects of the whole word or lemma — including lexical stress.” 两条可检验的假说由此推出。这是本批论文中显式桥接假设最清楚的例子。

**文献对话（§3 是范本）。**
- 对 Probert (2006a) 的古希腊语研究：肯定其经验基础，但指出只有描述统计和频率分箱，“a reanalysis thereof is needed”；并在脚注里**用对方的数据做了一个快速再分析**，得到 “a significant, if weak, difference … small effect size”。
- 英语名动重音对的争论：Sondregger (2010) 给出稳健统计；Kiparsky (2016) 淡化频率——“the two factors are not incompatible”；Hotta (2013) 与 Yang (2016) 并未推翻 Sondregger，因为前者没有多变量分析，后者未控制前缀——**按方法质量裁决冲突研究**；结论是 “At present, I see no compelling reason to reject Sondregger’s finding.”
- 讨论中与对手在一点上会合：“Exactly as Kiparsky (2016) contends … stress shift … follows from the application of default phonological preferences when lexical preferences are too weakly encoded.”
- **回到引言里的矛盾，给出条件式调和**：高频在音系变化需要覆盖词库信息时起抑制作用（引言中 Gahl 2008 与 Hay et al. 2015 的矛盾由此化解）。

**数据透明。** 选《梨俱吠陀》的理由（最古、资源最全）和缺点（非历时均质、体裁单一、散文多无重音标注）都写出；审稿人提示的一个优点（单一体裁可排除语域造成的重音变体）也写进脚注；排除项逐一说明；同一词两种重音记为两个词条，“other approaches are conceivable, none … obviously superior”；尝试过但做不了的变量写进脚注并说明原因。

**讨论本身很短。** §5 约 760 词，只做三件事：带条件地归纳（“Granting the adequacy of the sketch of the principles of stress assignment in Vedic Sanskrit presented in Sect. 2.2, …”）、对齐前人、回答引言的矛盾。前面的章节已经完成了理论对话和统计解释。

**我的评价。** 讨论中写 “indicate unambiguously” 和 “low productivity is a necessary precondition”，对六个数据点、p = .094 的相关、贝叶斯因子只有 2.07 的类别能产性而言偏强；用六个点拟合 Loess 推出“界线在 𝒫 ≈ 0.01”是明显外推。

**对亦声稿的启发。** v6 用《广韵》中古音近似许慎时代的语音关系，应像 Sandell 一样写一句明确的桥接假设，并说明支撑与风险（反切串同一的复核只排除了匹配误差，不排除时代差）。可考虑用本文指标再分析前人数据，例如李宁、郭抒远的 79 个“应标亦声”字的同音率（需另行执行，结果写入结果文件后才能进正文）。对段玉裁、王筠、李宁与郭抒远等前人，说明各自的方法能证明什么、不能证明什么。回到引言中右文说“声符是否兼义”的争论，给出条件式答案。

---

## P9 Ševčíková & Hledíková：转类没有显性材料时怎样谈透明度

**读的范围。** 第 1–17 页（引言、§2 背景与研究问题、§3.1–3.2 取样与相关性判定）全读；§3.3 语义类别体系略读；§4 Results and discussion 与 §5 Conclusion 全读（第 21–38 页）。

**设计与结果。** 在 SYN2015 中找出 1,079 个名转动词（conversion）和 229 个“前缀加转类一步完成”的动词（parasynthesis，以语料中有无无前缀形式判定），按名词在动词义中的角色分 10 类；以 Gottfurcht (2008) 的 Semantic Category Distribution Effect 为前提：某过程中某语义类越常见，该类词越透明。ACTION、STATE 只见于转类，SOURCE 只见于前缀派生；两过程的熵相近，但偏好不同。

**概念处理。** 捷克语动词必带词尾，英语式“形式完全同一”的转类定义不成立；作者采用放宽的跨语言定义，并用三条理由说明词干后缀加不定式词尾是屈折而非派生后缀，同时交代本国传统的各种叫法（Dokulil 的 transflexion 等）。透明度拆成 relatedness（相关性）与 compositionality（组合性），前者是后者的必要非充分条件。**相关性以共时词典义判定，只有词源联系的词被剔除**（dvořit se、pochlebovat）。

**讨论要点。** 由分布推透明度时给出意义上的理由（转类本质是名词到动词的类转换，动作义名词最契合动词的主要功能）。明确范围：“We did not conduct dedicated experiments … Nevertheless, potential competition … can be briefly assessed on the basis of the available data.” 与前人对表：“The Czech data thus do not appear to support Plag’s (1999, pp. 231–233) assumption … Instead, the findings align with Gottfurcht’s (2008, p. 272) observation …”。结论之前专写一段方法限定：“the conclusions presented below should be interpreted in light of these methodological specifics.”

**我的评价（一个值得警惕的循环）。** 正文明说透明度推断依赖前提，但摘要写 “In line with the Semantic Category Distribution Effect, the most transparent converted verbs are those …”——“最透明”本来就是用该效应的前提定义出来的，不能算对该效应的独立支持。另外分布差异没有统计检验；两个样本量差别很大（1,196 与 229）的熵直接比较，以及与英语研究的跨研究熵比较，都有风险，作者只写 “may suggest”。

**对亦声稿的启发。** 避免把由假设推出的结论写成“与理论一致”：v6 的 196 对同音关系类型是在看得见标注时分的，讨论里引用 L、F、C 的比例时只能作描述，不能作为支持王筠分别文说的独立证据。点明 v6 的语义编码测的是《说文》释义所见的汉代意义联系，与现代同源词研究不是同一对象。说明为什么把“分别文、累增字”对应到 sense specialisation 与 added determinative，为什么把“转类”用于没有屈折标记可显示零派生的汉代汉语。

---

## P10 Cohen 等：替代解释 → 它的预测 → 结果 → 简约性

**读的范围。** §1 引言与预测（第 1–11 页）全读；实验方法略读；两个实验的结果与讨论（第 21–25、29–34 页）、§4 General discussion 与 §5 Conclusion 全读（第 34–39 页）。

**设计与结果。** 视觉情境眼动：目标为单数名词，竞争项为复数（cart/carts；coco/cocos）或多音节载体词（cart/carton）；操纵词干时长的匹配与否，语境为一致性限定词或元语言提及。英语复制了作者前作；西班牙语的音段压缩效应约为英语的三倍（0.44 与 0.14 empirical logits）；英语水平没有效应。

**引言中的文献推理。** 研究问题 1 就是复制前作（“can we replicate Cohen (2024)’s findings?”），理由是先确认结果稳健才能在其上推进。对相互矛盾的西班牙语产出研究，指出可能只是方言没控制。从文献推出两种相反的预测（一致性使线索多余而被忽略，或使线索可预测而更被利用），并重读对立文献：Clayards et al. (2021) 的刺激一半匹配一半不匹配，被试学到的可能是“不可靠”而不是“多余”。

**讨论的推理。**
- **替代解释的处理是全文最好的一段。** 替代解释：无限定词的语境句子别扭，占用工作记忆，才造成交互作用。两条反驳：若如此，多音节目标也应出现同样交互（他们做了分析，没有）；前作的刺激没有这种别扭结构，却得到同样的交互。收束：“It would be an uphill battle then, to argue that the metalinguistic mention structure was not responsible for that interaction in the two English experiments, but nevertheless was responsible for producing that identical interaction in Spanish – especially when it is so much simpler to argue that the same effect is present in all three experiments because the same mechanism is at work.”
- **“Four answers to four questions”。** 每个研究问题原文重述，先答 Yes 或 We have no evidence of this，再限定。
- **推测标明身份，并保留“乏味解释”。** 效应弱可能只是刺激设计造成的，“plausible and entirely testable in future work. But it is also a bit dull. We shall therefore indulge in some speculation regarding more interesting reasons.”
- **削弱自己的候选解释。** 对三个可能原因之一，作者说明它需要什么产出证据、现有证据互相矛盾，“Without that evidence from production, it is less convincing to argue …”。
- **零结果。** “We cannot, therefore, conclude that there is any effect … Possibly that lack of significance reflects a simple lack of statistical power … However, absent evidence from a larger-scale, higher-powered study, we have no reason to believe that …”
- **把混淆变成设计。** 直接语音线索与附属形态语音线索来自不同过程，无法比较；作者设计同一过程的对比（badge/badger vs badge/badges；lap/lapse vs lap/laps），并推出两条预测。
- 结论一段，以一句有记忆点的话结束：“Listeners are resourceful creatures: they let no cue go unexploited.”

**我的评价。** 语言、被试的多语背景与刺激结构（英语多种词尾，西语只能用开音节）完全混淆，三种解释都无法区分；作者承认这一点，但结论中“especially so in Spanish, whose richer morphosyntax reinforces …”仍略强于证据。

**对亦声稿的启发。** v6 的稳健性检验可以在讨论中改写成 Cohen 式论证：若效应来自许慎以声符释字的习惯，去掉声训后应当消失；若来自大徐增标，两本共有的 140 条上应当消失；若来自《广韵》匹配误差，改用反切串同一后应当消失——都没有消失；说每一项检验都各自碰巧保留了效应，远不如说标注本身追踪同音关系来得简单。可在讨论开头或结论首段逐条回答 H1a–H4。推测性解释之前先写“乏味但可检验”的解释。

---

## P11 Nikolaev 等：说明检验为什么有诊断力，精确承认方法假象

**读的范围。** §1 引言与四个研究问题（第 1–9 页）全读；§2 芬兰语屈折类（含历史背景）与 §3.1–3.2 模型和材料略读；§3.3–3.4 结果与 §4 General discussion 全读（第 20–34 页）。

**设计与结果。** 判别词库模型只用形式嵌入（字母 3-gram 或 4-gram）与语义嵌入，不给词干、词缀、屈折特征或屈折类信息；比较类型学习与频率学习；按频率分层留出低频词作测试。训练集接近满分；测试准确率与屈折类的能产性相关；4-gram 明显优于 3-gram；频率学习使低频词难学。

**引言。** 把模型的理论承诺写成三个 what-if 问题，公开写成前提，而不是暗中假定；并说明检验为什么有诊断力：“This correlation is theoretically informative: successful memorization alone would not require held-out accuracy to vary with independently established class productivity, whereas such a relationship would show that the learned form–meaning mapping reflects the graded potential for generalization across classes.” 历史背景一节说明芬兰语第一部语法（Petræus 1649）按拉丁语模型分类，后来的语法学家发现差别在词干而不在词尾，才放弃这种分类——本族早期语法的分类本身带有理论预设。

**讨论。** 按四个研究问题展开，最大篇幅给“形式与意义空间的同构从何而来、是否是方法假象”——这正是审稿人最可能攻击的地方。处理方式：先承认 fastText 部分由字符子串构造，形式相似可能进入“语义”向量（“We therefore cannot exclude the possibility that form similarity contributes …”）；再给三点考虑，其中一点用数据检验（两字母词尾串有 43% 的出现并不是该词尾，五字母为 0%，而 fastText 只用 5 字母以上的子串）；精确限定：“this reduces—but does not eliminate—the possibility of a direct confound”；结论是 “unlikely to be solely an artefact”，再引用 word2vec 得到同类结果的研究作独立支持。与 Bybee (1995)：“fit well with the general approach … but diverge specifically with respect to the role of higher-frequency words”。最后降低整体主张的地位：“the DLM provides a proof of concept …”。

**我的评价。** 5 个能产性指标乘 4 个模型的相关没有做多重比较校正；产出系统的准确率与能产性相关不显著，作者转而强调语义接近度的相关，有选择性强调之嫌。

**对亦声稿的启发。** 写出检验为什么有诊断力：若亦声只反映许慎“声符兼义”的信念，它不必与读音是否同一相关；它恰恰与同音和 *-s 相关，而与其他词缀关系无关。对最可能的方法质疑（语义编码依赖许慎释义，而释义与标注出自同一人）写一段 Nikolaev 式回应：承认 → 已做的缓解（去除声训后仍为 69% 对 12%；盲编不显示标注）→ 精确限定（减少但未消除）→ 结论（效应不太可能完全来自释义）→ 独立支持（同音与 *-s 的结果不依赖释义）。与王筠的关系可以写成总体一致、局部分歧。把“本土元语言标注可以用对照组和独立证据检验”定位为 proof of concept。

---

## 12. 横向观察（细节见总结）

- **理论问题一律点名。** 十一篇的摘要都点出所检验或修订的一般理论命题（超丰富性的典型性、多重表达类型学、体保持假说、分解 vs 词本位加工、Bybee 的频率效应等）。单一语言的材料一律写成这些问题的证据。
- **理论在引言里准备好，在讨论里回收。** 讨论能做深，是因为引言已经写出了竞争理论和各自的预测（Lõo、Berg、Sandström、Cohen、Barbu Mititelu），或写出了要检验的理论命题及其推论（Huyghe 的 APH、Igartua 的“ME 应当消亡”、Sandell 的两条假说）。
- **讨论的长短取决于前面做了多少。** Huyghe 与 Sandell 的讨论/结论只占约 4–5%，因为解释已嵌在分析各节，理论对话已在前人研究一节完成；Ševčíková 与 Cohen 的讨论占比高，因为结果与讨论合写或按研究问题逐条作答。
- **篇幅跟着理论分量走。** 最长的段落给异常、零结果或对既有理论的修订，已知或预期的结果一两句带过。
- **可观察的审稿痕迹。** Berg、Igartua、Huyghe 致谢主编 Bonami；Igartua 把审稿人的替代分析写进脚注；Sandell 把审稿人提示的“体裁单一的好处”写进脚注。审稿人看重替代分析、相关文献和明确的限定，最好在投稿前主动写进去。
- **至少 8 篇提供了数据或脚本仓库、补充材料，或说明数据来自公开语料**（OSF：Lõo、Sandström、Huyghe、Sandell、Ševčíková、Cohen；Berg 附补充数据；Saicová 用公开语料库）。
