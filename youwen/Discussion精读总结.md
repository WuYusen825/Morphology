# Discussion 精读总结：从数据到理论创新（第二版）

整理日期：2026-09-28。

**两轮阅读。** 第一版由 Codex 整理，依据参考文献中的 14 篇期刊研究文章和 5 篇对照材料，逐篇分析见[第一轮精读笔记](discussion_close_reading.md)。第二版由 Claude 补充 Release [`学习`](https://github.com/WuYusen825/Morphology/releases/tag/%E5%AD%A6%E4%B9%A0) 中的 11 篇 *Morphology* 2026 年研究文章，逐篇分析见[第二轮精读笔记](discussion_close_reading_morphology2026.md)，并按 Qu 的追加要求新增第 4 节“怎样联系前人结论、呼应前人理论”。两轮的阅读范围与原文入口见[阅读范围索引](discussion_reading_index.md)。

**口径。** “贡献”“增量”指从成文论文可以辨认的学术推进；没有审稿记录，不能断定实际录用原因，发表也不保证每一步推理都对。第 8 节对亦声稿的建议是写作与论证建议，不是已完成的改稿，也不是已执行的新分析。

---

## 一页结论

1. **理论创新来自改变一个具体的解释关系**，而不是来自数据量或新术语：重新分类现象、修订一条类型学标准、提出一条解释原则、把矛盾的文献化为条件或层次上的区分。第二轮再补一条：在 *Morphology* 上，这个关系必须是**一般形态学问题**（超丰富性、多重表达、透明度、范式与词族、能产性、转类、加工模型）。十一篇文章的单一语言材料，一律写成这些问题的证据。
2. **讨论的骨架**通常是：引言里先写出竞争理论及其预测 → 讨论逐项计分（证实、限定、挑战）→ 对最强的替代解释写出“它会预测什么、结果如何” → 把异常或零结果变成新的区分或原则 → 以可检验的后果和精确的限定收尾。
3. **严谨性集中在七个环节**：比较基准、测量与代理链、从关系到机制的桥（桥接假设）、替代解释、零结果、效应量、循环论证。**可以推测的**是机制、历史原因、编纂者或说话人的动机、跨领域类比——前提是标明身份、先给“乏味但可检验”的解释，并说明需要什么证据。
4. **与文献对话要精确到具名作者和具体命题**：一致之后说明增量；同样的结果争解释；按方法质量裁决冲突研究；用对手的数据再分析；替对手设想最强的辩护再检验；逐条套用既有类型学并提出修订；给含糊的“一致”降价。
5. **语言上限定的是命题，不是语气。** 用第一人称标记理论选择（I contend、we propose），用短句收束决定性的结果（“They did not.”），用一句整体限定代替逐句加 may。
6. **详略跟着理论分量走**：已知或预期的结果一两句带过，最大篇幅给异常、零结果或对既有理论的修订；结论短，但要回答引言的问题并给出后果。
7. **对亦声稿**：若投 *Morphology*，§5.3（词根、词与派生的诊断）要成为理论中心，而它现在只有约 240 词；核心概括应再推进一步，提出解释原则并推出数据以外的预测；稳健性检验可以在讨论里改写成“替代解释—预测—结果”；H1b、H4 的零结果需要重新定位；桥接假设要写明。另须先核实 *Morphology* 的 SSCI 收录状态（见第 8.1 节）。

---

## 1. 读了什么

**第一轮（Codex）**：Zhang 2022、Jacques 2016/2022、Mei 2012、Sagart & Baxter 2012、Bonami & Strnadová 2019、Arad 2003、Monaghan 等 2014、Meng 等 2025、Hill & List 2019、吳濟仲 2015、李宁与郭抒远 2019、Karlgren 1933、Pulleyblank 1973；另读 Aronoff 2007、Pulleyblank 2000 与三篇对照材料（Rasin 等 2024、Dingemanse 等 2015、Hathout & Namer 2019）。多为历史汉语形态学与形态理论的文章。

**第二轮（Claude）**：*Morphology* 第 36 卷（2026）的 11 篇研究文章，方法覆盖实验、语料、类型学、历史文献、计算模型：

| 简称 | 主题 | 讨论的理论问题 |
|---|---|---|
| Lõo 等 | 爱沙尼亚语自发语音的形态效应（听写实验） | 分解模型 vs 学习模型；范式效应 |
| Barbu Mititelu 等 | 英语派生后缀的透明度（WordNet + 分类器） | 零后缀是否更不透明；多功能性 |
| Saicová Římalová | 捷克语未完成体将来式（语料） | 超丰富性的典型性（Thornton 2019）；迂说式 |
| Sandström & Rosenberg | 瑞典语复合词掩蔽启动 | 语义盲的形—正字法分解 vs 词本位加工 |
| Huyghe 等 | 法语动转名词语义库 SONDE | 体保持假说（APH）；多功能性；派生范式 |
| Berg | 名词内部语素顺序（472 种语言） | 相关性原则、词库先于语法、人称前置 |
| Igartua | 巴斯克语多重表达的历时来源（文献） | Harris (2017) 类型学；ME 是否注定消亡 |
| Sandell | 吠陀梵语词重音与能产性（《梨俱吠陀》） | 频率对韵律规则化的抑制 |
| Ševčíková & Hledíková | 捷克语名转动词（转类 vs 前缀派生） | 转类的语义透明度 |
| Cohen 等 | 英语与西语中的词结构时长线索（眼动） | 形态句法一致性对语音线索使用的调节 |
| Nikolaev 等 | 判别词库模型学习芬兰语屈折类 | 屈折类是否需要作为抽象单位 |

与亦声稿最接近的是 Igartua（多时代的文献层次）、Sandell（古代单一经典语料 + 桥接假设）和 Ševčíková（转类与词典义判定相关性）；论证手法最值得学的是 Berg、Cohen、Huyghe 与 Sandström。

---

## 2. 从观察到理论：七条推进路径

两轮文章共同的推理链是：**精确的现象 → 改写为对某个具名理论命题的检验 → 排除平凡解释和替代解释 → 说明改变了什么（分类、单位、机制、条件、标准）→ 限定范围 → 推出后果或预测。** 具体有七条路径，一篇文章往往同时用几条。

### 2.1 先写出竞争理论的预测，讨论逐项计分

Lõo 等在引言里用一张表写出分解模型与学习模型对每个因变量的预测，讨论逐项回到这两类模型：这个结果“consistent with”分解模型，那个结果分解模型“less easily reconciled with”，整词频率则“in principle, compatible with both”。最后没有宣布胜者——“neither framework fully accounts for the complete pattern of effects”。Berg 为三条解释原则写出互相冲突的预测；Cohen 等为西语设计了两种相反预测（一致性使线索多余，或使线索可预测）。

要点在于：**计分表本身就是理论贡献**，前提是预测在看结果之前就写出来了；而且要说明哪些结果对竞争理论**没有诊断力**，不能把两种理论都能解释的结果算作支持自己一方。

### 2.2 设计一个对竞争理论有诊断力的对比

Sandström & Rosenberg 放进了伪复合词与正字法对照两组：分解模型预期前者强于后者，联结模型预期两者相同。讨论就围绕这个对比做裁决：“If segmentation were automatically triggered by surface structure alone, pseudo-compounds should have activated their embedded strings. They did not.” Nikolaev 等说明检验为什么有诊断力：单靠记忆不会让测试准确率随屈折类的能产性变化，而观察到了这种变化，说明学到的是可推广的映射。第一轮的 Bonami & Strnadová 用“最好的单一预测项”作基准，也属于这一类。

### 2.3 用新数据检验并修订既有理论或类型学

Saicová Římalová 逐条套用 Thornton (2019) 超丰富性的典型性标准，发现“受影响词位的数量”会把此现象误判为边缘，于是提出把“使用频率”增为一条标准。Igartua 以 Harris (2017) 的多重表达类型学组织全部巴斯克语材料，再提出两处修订：显性与隐性 ME 与形式—功能类型正交；以词为界的定义排除了短语屈折语言。Huyghe 等检验体保持假说，发现不保持体特征的情况与派生过程系统相关，因此不能只归于词汇化。第一轮的 Zhang (2022) 则改变了“什么才算完成体证据”的标准。

这是历史或描写性研究最常用、也最稳妥的理论贡献：**不必建立新理论，只要让既有理论的某一条标准、某一个边界因你的数据而改变。**

### 2.4 从经验概括走到解释原则，再推出数据以外的预测

Berg 在引言就区分经验概括与解释：Greenberg 的共性“do not explain typological patterns but are themselves in need of an explanation”。讨论中，领属标记的异常行为催生了一条新原则（人称前置）；让原则相互竞争，又推出“违反两条原则的顺序应接近零”，并在数据中验证（“This is exactly what we find”）；最后对未研究的范畴做预测，“A test of these predictions must await future work”。这是本批文章中理论推进最远、也最有章法的一篇。

### 2.5 把异常与零结果变成新的区分

Sandström & Rosenberg 把透明度的零结果重新定位为“语义关系是必要条件，程度不再起作用”（“Importantly, this null effect does not imply that semantics is irrelevant”）。Lõo 等给范式效应的零结果最多篇幅，三个候选解释各对应本研究与前作的一处具体差异。Berg 由领属的异常得出新原则。Cohen 等对英语水平的零结果只说“We have no evidence of this”，既不断言无效应，也不暗示有效应。

### 2.6 化解文献矛盾：按层次、阶段或条件区分

Sandström & Rosenberg 把掩蔽启动与语义启动、眼动结果的矛盾解释为不同加工阶段（“are not contradictory, but instead point to distinct temporal phases”）。Sandell 在引言提出“高频有时促进变化、有时抑制变化”的矛盾，讨论给出条件式答案：当变化需要覆盖词库信息时，高频起抑制作用。第一轮的 Monaghan 等把“任意性 vs 系统性”的二元争论改为有分布条件的问题。

### 2.7 资源或测量本身是贡献，但要用它检验具名命题

Huyghe 等与 Barbu Mititelu 等都以资源或测量为主，但都用它裁决了具体理论主张（体保持假说；零后缀是否更不透明）。第一轮的 Hill & List 改变了资料的表示方式，使拟音主张可以接受更具体的检查。只有资源而没有对具名命题的检验，理论贡献就难以辨认。

---

## 3. 严谨与推测的边界

### 3.1 必须严谨的七个环节

| 环节 | 要交代什么 | 做得好的例子 | 警示 |
|---|---|---|---|
| 比较基准 | 结果是否只是基准差异、类别不平衡或数学性质 | Bonami & Strnadová 比较最佳单一预测项；Huyghe 每个分类器都报多数类基线；Sandell 用 LNRE 外推后再比较 𝒫 | Barbu Mititelu 按原始准确率排后缀，而各后缀基线差别很大 |
| 测量与代理链 | 每一环测的是什么、假定了什么 | Barbu Mititelu 写出“if we take high polyfunctionality to correlate with reduced predictability”；Ševčíková 以共时词典义判定相关性，剔除只有词源联系的词 | 把代理当作所测之物本身 |
| 桥接假设 | 从已测的关系到机制、从后世材料到古代系统的假设 | Sandell：“I cautiously assume that this more robust representation extends to … lexical stress”；第一轮的 Sagart & Baxter 用借词中的前鼻音区分派生方向 | 第一轮 Mei 由现代亲属语言形式直接推派生方向 |
| 替代解释 | 最强的替代解释会预测什么，结果是否符合 | Cohen 等（别扭语境的解释预测多音节目标也有交互，没有）；Huyghe（替 APH 设想“词汇化”退路再堵住）；Nikolaev（嵌入是否是方法假象） | 只列局限，不检验替代解释 |
| 零结果 | 写成“没有证据”，候选原因对应具体设计 | Lõo、Cohen；Berg：“Critically, this does not imply that the principles make false predictions”；Saicová：语料未见不等于不存在 | Lõo 用零结果支持分解模型，只能到“more compatible” |
| 效应量 | 显著不等于重要，“显著但微弱”要直说 | Huyghe：“only marginally higher than the No Information Rate baseline … nevertheless statistically significant”；Lõo：频率效应“rather small” | 第一轮 Meng 等从小效应推到声音象征与应用 |
| 循环论证 | 分组标准与待解释的结果是否独立 | Berg 自己指出 Urgency 原则的循环风险 | Ševčíková 摘要把由前提定义出的“最透明”写成“与理论一致”；第一轮 Arad 的诊断受 Rasin 等质疑 |

第一轮总结列出的五个高危连接仍然适用：音义相关 → 同源；同源或交替 → 派生方向；后世或亲属语言形式 → 上古系统；文本标签的分布 → 编纂者意图；模型能解释数据 → 该模型优于其他模型。

### 3.2 可以合理推测，但要满足五个条件

1. 有具体的待解释现象。
2. 有独立知识、比较材料或既有模型作依据。
3. 相对于竞争解释有说得出的收益。
4. 能指出支持或削弱它的材料。
5. **标明身份，并先给“乏味但可检验”的解释。**

第五条是第二轮补充的。Cohen 等的写法最坦白：效应弱也许只是刺激设计所致，这“plausible and entirely testable in future work. But it is also a bit dull. We shall therefore indulge in some speculation regarding more interesting reasons.”其他标明身份的方式：Saicová 把最远的问题写成问句（“Why does motion play an important role in the data?”）；Igartua 给竞争的词源分级（“can hardly be deemed plausible”；“better grounded … although … not free of a considerable degree of speculation”），并直说远源推测“too remote and speculative to serve as minimally reliable evidence”；Berg 用“a case can be made for”；Nikolaev 把整个模型定位为“proof of concept”；第一轮的 Pulleyblank 用“If we suppose”展开远期模型。

检查办法（第一轮）：删去讨论中最远的机制猜想或应用展望，论文还剩什么独立成立的贡献？如果全部创新都依赖最后那次推测，就要回头把近处的增量写清楚。

### 3.3 已发表不等于每步都对

第二轮文章中可以不学的地方：

- **Ševčíková & Hledíková**：摘要写“In line with the Semantic Category Distribution Effect, the most transparent … verbs are …”，但“最透明”本来就是用该效应的前提定义的。
- **Barbu Mititelu 等**：按原始准确率比较后缀的透明度，忽略了各自的多数类基线。
- **Sandell**：由 6 个类别、p = .094 的相关得出“low productivity is a necessary precondition”，并用 6 个点的 Loess 推出能产性界线。
- **Berg**：人称前置原则是看到领属数据后提出的；“原则强弱因区而异”没有独立测量，存在他批评 Urgency 时指出的同类循环风险。
- **Sandström & Rosenberg**：伪复合词与对照“无差别”没有做等价检验；读音差异这个替代解释只用间接文献缓解；摘要比讨论说得更满。
- **Nikolaev 等**：多个指标与模型的相关未做多重比较校正；不显著时转而强调另一指标。
- **Saicová Římalová**：“运动义比定向性更重要”只靠一个动词。
- **Igartua**：存续的例子多，消失的例子篇幅少。

第一轮已指出 Meng 等（相关性到机制、教学应用的跨度）和 Arad（诊断是否独立于待解释的意义差异）的问题。

### 3.4 命题强度分层

| 命题类型 | 适合承担的任务 | 英文表达示范（改编，不是原文） | 要避免的跨越 |
|---|---|---|---|
| 描述 | 报告特定材料与比较中的模式 | The contrast is concentrated in X under the present classification. | 把样本直接推广到全部语言或时期 |
| 解释 | 说明为何与模式相容、能统一哪些现象 | This distribution follows if X, because it brings A and B under one account. | 把相容写成唯一 |
| 桥接假设 | 连接已测之物与所关心之物 | We assume that relations visible in X reflect relations in Y; the check in Section Z rules out A but not B. | 把假设写成观察 |
| 模型或原则 | 明确前提，推出可观察的后果 | We propose that …; if so, … should be rare, and it is. | 用新术语代替解释 |
| 理论后果 | 指出哪个既有命题须修改 | The result requires a distinction between A and B. / This criterion should be added to … | 只说“具有理论意义” |
| 界定边界 | 说明尚不能决定什么、需要什么证据 | These data cannot decide whether …; a comparison of A with B would. | 用“样本有限”等泛泛谦辞 |
| 推测 | 提出候选原因与研究方向 | A more speculative possibility is that …; it predicts … | 让推测承担核心结论 |

**真正的边界在命题之间，不在某个动词。** 最该避免的是同一句里悄悄换对象：从“字”换成“词”，从“意义相关”换成“同源”，从“同源”换成“能产派生”，从“与模型相容”换成“模型已获证明”。

---

## 4. 怎样联系前人结论、呼应前人理论

这是 Qu 追加的问题。两轮文章与文献的对话方式可以归为以下动作，按常用程度排列。

| 动作 | 做法 | 例子 |
|---|---|---|
| 一致 + 增量 | 先认同，再点出前人没做的那一维 | Lõo：“fits well with earlier studies by Ernestus et al. … However, they did not investigate …” |
| 文献主张 → 具名预期 → 逐条裁决 | 综述中每条主张挂具名出处，改写为预期，讨论逐条判定 | Barbu Mititelu（Plag、Valera、Kisselew）；Ševčíková：“do not appear to support Plag’s (1999, pp. 231–233) assumption … Instead, the findings align with Gottfurcht’s (2008, p. 272) observation” |
| 首尾呼应 | 引言立的理论，讨论逐一回收；引言提的矛盾，讨论给答案 | Lõo 的两类模型；Sandell 的频率矛盾 |
| 同果异解 | 与得到同样结果的前人争解释 | Sandström vs Gagné et al. (2018)：“激活后抑制”vs“激活不足” |
| 矛盾时指向具体设计差异 | 不笼统说“方法不同”，指出是哪一处 | Lõo（与自己前作的语料、任务差异）；Sandström（对方刺激有歧义切分）；Cohen（对方刺激一半匹配，学到的是“不可靠”而非“多余”） |
| 按方法质量裁决冲突研究 | 说明哪项研究的设计能支持哪个结论 | Sandell：Hotta 无多变量分析、Yang 未控制前缀，故不能推翻 Sondregger；“At present, I see no compelling reason to reject …” |
| 用对手的数据再分析 | 用同一把尺子量前人材料 | Sandell 在脚注中对 Probert 的古希腊语数据做 Wilcoxon 检验 |
| 替对手设想最强辩护再检验 | 先替被挑战的理论找退路，再堵住 | Huyghe 替 APH 设想“词汇化”退路 |
| 引对手原话 | 让反驳对象精确到一条原则 | Sandström 引“morpho-orthographic full decomposition”；Berg 逐字引出 Greenberg 共性并拆解 |
| 用理论自身的逻辑承诺排除它 | 找出理论必然推出的结果，看数据 | Berg：Urgency 若是范畴性的就不应有区域差异 |
| 逐条套用既有类型学并修订 | 以权威框架组织材料，在框架上提修订 | Saicová（Thornton）；Igartua（Harris）；Saicová 细化 Bonami (2015) 的分类 |
| 总体一致、局部分歧 | 明说在哪一点上分道 | Nikolaev：“fit well with … Bybee (1995), but diverge specifically with respect to …”；Sandell：“Exactly as Kiparsky (2016) contends …” |
| 与统一理论对话 | 用解释深度对普遍性 | Berg 回应 Hahn et al. (2021)：普遍性“is bought at the expense of a loss of explanatory depth” |
| 给含糊的一致降价 | 与泛泛之论一致不算发现 | Saicová：“those statements are so general that this conclusion has little value” |
| 借外部机制并标明未检验 | 引进他人的机制作解释候选 | Saicová 借 Bybee 的频率保护；Igartua 的遗传冗余类比 |
| 复制优先 | 在前作结果上推进之前先复制 | Cohen：“can we replicate Cohen (2024)’s findings?” |
| 把个案定位为一般理论的证据 | 说明本语言材料对一般理论补了什么 | Saicová：“Czech linguistic data may also contribute to …”；Berg 名词与动词适用同一组原则 |
| 说明本族分类的理论负载 | 早期语法的分类框架本身有预设 | Nikolaev：芬兰语第一部语法按拉丁语模型分出变格类 |

**三种要避免的写法**：只说“与前人一致”而不说哪个命题；只引支持自己的文献而不处理对立结果；把传统学者的说法改写成与现代理论等同（对亦声稿尤其要注意王筠）。

---

## 5. 语言表达

### 5.1 原则

1. **限定命题，不削弱语气。** 范围写进名词短语（in these data / among labelled pairs with MC readings），不必句句加 may。
2. **标明每句话的身份**：观察、解释、假设、推测、建议。第一人称常用来标记理论选择：I contend（Berg）、we propose（Sandström）、in our opinion（Lõo）、I cautiously assume（Sandell）。
3. **决定性的结果用短句收束**：“They did not.”“This is exactly what we find.”
4. **给乏味解释留位置**，再“indulge in”有意思的推测。
5. **整体限定代替逐句限定**：Igartua 的“if the analyses offered in the foregoing discussion are not flawed”；Ševčíková 结论前的“should be interpreted in light of these methodological specifics”。
6. **零结果的措辞**：no evidence for / we cannot conclude that / absent evidence from …, we have no reason to believe that …，不写成 there is no effect。

### 5.2 功能短语库（按用途，括号内为出处）

- **报告与定位**：The results … offer a straightforward yes in response to our first RQ（Cohen）/ These findings are unsurprising, as they straightforwardly replicate …（Cohen）/ Notably, the effect …, although present, is rather small（Lõo）
- **提出主张**：We interpret our results as supportive of …（Sandström）/ Our claim that … is based on the finding of …（Sandström）/ I contend that …（Berg）/ We may therefore re-interpret X as Y（Berg）
- **说明诊断力**：This correlation is theoretically informative: … alone would not require …, whereas …（Nikolaev）
- **桥接与条件**：I cautiously assume that …（Sandell）/ Granting the adequacy of …（Sandell）/ if we take X to correlate with Y（Barbu Mititelu）
- **处理替代解释**：It is worth briefly considering an alternative explanation … there are two counterarguments（Cohen）/ It would be an uphill battle then, to argue that … especially when it is so much simpler to argue that …（Cohen）/ it can be asked whether …, in which case they would not violate …（Huyghe）/ cannot be viewed simply as …（Huyghe）
- **承认方法局限**：We therefore cannot exclude the possibility that …（Nikolaev）/ this reduces—but does not eliminate—the possibility of …（Nikolaev）/ is unlikely to be solely an artefact of …（Nikolaev）/ we cannot be sure whether it is X or Y that …（Lõo）
- **零结果**：We have no evidence of this（Cohen）/ Importantly, this null effect does not imply that …（Sandström）/ Critically, this does not imply that the principles make false predictions（Berg）/ the fact that the forms were not found … does not mean that the forms do not exist（Saicová）
- **与文献**：fits well with … However, they did not investigate …（Lõo）/ do not appear to support … Instead, the findings align with …（Ševčíková）/ fit well with … but diverge specifically with respect to …（Nikolaev）/ Exactly as X contends, …（Sandell）/ the two factors are not incompatible（Sandell）/ At present, I see no compelling reason to reject …（Sandell）
- **修订理论**：This all supports the suggestion that … should be considered another criterion（Saicová）/ The result requires a distinction between A and B（第一轮自拟模板）/ is somewhat challenging for a typology … so far solely based on …（Igartua）
- **推测与分级**：We shall therefore indulge in some speculation（Cohen）/ a case can be made for …（Berg）/ can hardly be deemed plausible / appears to be better grounded … although …（Igartua）/ too remote and speculative to serve as minimally reliable evidence（Igartua）
- **限定与展望**：The bleak conclusion is that the available data are too scanty to provide robust evidence for or against …（Berg）/ A test of these predictions must await future work（Berg）/ A follow-up study that controls for … would be a useful way to distinguish between these possibilities（Cohen）/ … provides a proof of concept（Nikolaev）

这些短语是改写的模板，照抄会显得拼凑；关键是每句话承担的功能。

---

## 6. 详略与结构

### 6.1 篇幅的实际分布

按词数粗算（含例句与表格文字，只作比较），十一篇讨论与结论约占正文的 4%–39%，中位数约 24%。

- 占比很低的两篇（Huyghe 约 5%，Sandell 约 4%）不是讨论薄弱，而是解释已嵌在分析各节，Sandell 的理论对话在“前人研究”一节里就做完了。
- 占比最高的两篇（Ševčíková 约 39%，Cohen 约 27%）是结果与讨论合写，或各实验先各有讨论。
- 结论都短：Cohen 91 词，Sandell 的讨论与结论合计约 760 词，Berg 的结论最长（约 1,370 词），因为其中还有与动词的比较和对统一理论的回应。

v6 的 §5–§7 约占正文 26%，总量在正常范围内；问题在内部分配，见第 8.2 节。

### 6.2 三种讨论架构

1. **按理论主题的独立讨论**（Sandström、Berg、Lõo、Igartua）：适合一个中心论点加几条理论后果。
2. **按研究问题逐条作答**（Cohen 的“Four answers to four questions”、Nikolaev、Barbu Mititelu、Ševčíková）：适合有明确假设的文章，便于审稿人核对。
3. **解释嵌在分析中、结论很短**（Huyghe、Sandell）：适合资源型或以方法论证为主的文章。

以假设检验为骨架、又有较多理论后果的文章，可以把 2 与 1 结合：讨论开头用一小段逐条回答假设，再按主题展开。亦声稿适合这种结构。

### 6.3 分配原则

- **篇幅跟着理论分量走，不跟着结果顺序走。** Lõo 给意外的零结果约五段，预期内的结果每项一两段；Berg 的讨论几乎全给了“领属异常 → 新原则 → 原则竞争”这一条链；Saicová 最长的讨论段落是提出新标准的那一段。
- **最可能被审稿人攻击的地方要有篇幅。** Nikolaev 讨论中最长的是“同构是否为方法假象”；Cohen 给替代解释整整两段。
- **局限放在对应主张旁边，结论前再写一段总限定。** 这比全部推到文末的 Limitations 更有说服力（Ševčíková、Igartua）。
- **结论要回答引言的问题**，并给出一个后果或预测；可以以一句有记忆点的话结束（Cohen：“Listeners are resourceful creatures: they let no cue go unexploited.”）。

### 6.4 段内结构

较常见的段落顺序是：主张句 → 证据 → 替代解释或限定 → 后果。段落长短随内容变化：决定性的反驳可以只有两三句（Sandström 的否定后件式），机制讨论可以较长（Huyghe 的体保持一节）。

---

## 7. 什么样的创新让论文站得住

### 7.1 可辨认的增量类型

| 增量类型 | 第二轮例子 | 第一轮例子 |
|---|---|---|
| 新数据或新任务带来新的可观察量 | Lõo（自发语音 + 打字，三层准确率）；Cohen（西语扩展） | Jacques 2022（恢复异读的语法价值） |
| 检验并修订既有类型学或理论命题 | Saicová（Thornton）；Igartua（Harris）；Huyghe（APH） | Zhang 2022（完成体的举证标准） |
| 从经验概括到解释原则 | Berg（人称前置、原则竞争） | Arad 2003（局部性） |
| 诊断性对比裁决竞争模型 | Sandström（伪复合 vs 对照） | Bonami & Strnadová 2019 |
| 资源或测量 + 对具名命题的检验 | Huyghe；Barbu Mititelu | Hill & List 2019；Meng 等 2025 |
| 把已知效应推广到新语言，统计更严格 | Sandell（古希腊语、英语 → 吠陀梵语） | — |
| 复制后扩展 | Cohen | — |
| 为一个理论框架提供概念验证 | Nikolaev | — |
| 概念澄清、拆分分析层面 | Ševčíková（relatedness 与 compositionality） | 吳濟仲 2015（古今字 vs 分别文、累增字） |
| 用竞争证据约束派生方向或历史来源 | — | Sagart & Baxter 2012；Jacques 2016 |

### 7.2 十一篇的共同点

1. **摘要点名一般理论问题**，并说出本文对它的推进。
2. **相对于具名前人写明增量**，不笼统说“以往研究不足”。
3. **理论在引言里准备好**，讨论回收。
4. **替代解释主动处理**，不留给审稿人。
5. **至少 8 篇提供数据或脚本仓库、补充材料，或说明数据来自公开语料。**
6. **局限具体**，指出哪项结论受哪种证据限制，而不是泛泛谦辞。

### 7.3 可观察的审稿痕迹与周期

- 投稿到录用 9.7–17.4 个月，中位数 14.6 个月。
- Berg 感谢主编 Bonami “extraordinarily close engagement with my manuscript”；Igartua 把审稿人的替代分析写进脚注，并说明若采用它就没有 ME 阶段；Sandell 把审稿人提示的体裁优势写进脚注；Huyghe 感谢两位审稿人和 Bonami。
- 由此可见，审稿人会追问替代分析、相关文献和明确的限定。投稿前主动写进去，比在修改时补救更主动。

### 7.4 不可知之处

我们只能辨认文章提供了什么增量，无法知道编辑与审稿人实际看重哪一点；发表身份不能替代对每一步推理的判断（见 3.3 节）。

---

## 8. 应用到亦声稿：面向 *Morphology* 或同级 SSCI 期刊

### 8.1 期刊定位

- **先核实收录。** 项目记录 [`topic_and_journal.md`](topic_and_journal.md) 显示，*Morphology* 的 SSCI 收录状态尚未确认（Springer 页面只列 ESCI），当时的决定是确认前不作首选；README 记录的首投期刊仍是 *Language and Linguistics*。投稿前请在 mjl.clarivate.com 核实；改投哪一刊由 Qu 决定。下面的建议对 L&L、JCL、*Diachronica* 同样适用，只是 *Morphology* 对第 1 条要求最高。
- ***Morphology* 要的是一般形态学问题。** 十一篇都是用某种语言的材料回答一般问题。亦声稿可以挂靠的一般问题有三个：
  1. **没有显性形态时怎样诊断派生关系。** 上古汉语没有能显示零派生的屈折，若干派生词缀在中古音节中也不留直接痕迹；许慎的标注提供了一个独立于语音测试的本土分类。这与转类的诊断问题（Ševčíková & Hledíková；Barbu Mititelu 等；第一轮的 Jacques 2022）直接相关。
  2. **词本位 vs 词根本位派生**（Arad 2003；Rasin 等 2024；Aronoff 2007）以及**派生词族与范式**（Bonami & Strnadová 2019；Hathout & Namer 2019；Huyghe 等对词族结构的分析）。
  3. **本土元语言分析作为形态学证据的方法论**：与破读（Jacques 2022）、构字网络（Hill & List 2019）并列。

  若投 *Morphology*，摘要、引言末段和讨论都应点名其中一两个问题，并说明本文对它推进了什么。

### 8.2 v6 讨论的现状

按词数粗算（不含表格），v6 正文约 7,100 词，已在 `AGENTS.md` 规定的 5,000–7,000 词上限附近。各节：引言约 680 词（9.5%）、背景约 1,710（24%）、数据与方法约 1,390（20%）、结果约 1,490（21%）、§5.1 约 510、§5.2 约 350、§5.3 约 240、§5.4 约 150、§6 局限约 410、§7 结论约 200。

**已经做得好的地方**（与十一篇对照也不逊色）：
- 按声符聚类的模型和同声符对照组，基准意识强；
- 多项稳健性检验对应多种替代解释；
- §4.3 与 §5.1 关于派生方向的分解——“标注不必标方向，因为文字已经标了”——是全文最有理论含量的一步，也是对自己起始假设的修正；
- 零结果（H1b）照实报告，非计划的分解照实说明；
- 与王筠的关系处理得细，且没有把亦声等同于分别文。

**主要缺口**：
1. **理论中心太薄。** 面向 *Morphology* 读者最重要的 §5.3 只有约 240 词，末句“A root-based account would have to explain why …”在没有写出两种理论各自预测的情况下，容易被读成过度主张（第一轮总结已提醒）。
2. **核心结论停在经验概括**（“标注偏向标同一个词或最小派生”），还没有推进到解释原则和数据以外的预测。
3. **稳健性检验的逻辑散在方法、结果与局限中**，讨论里没有一段把“替代解释—预测—结果”串起来。
4. **H1b 与 H4 的零结果在讨论中没有得到重新定位**，读者可能读成“标注与词缀派生无关”或“王筠错了”。
5. **桥接假设没有写成假设**：中古音 → 汉代语音；许慎释义 → 汉代意义联系；大徐本标注 → 许慎的判断。
6. **§5.2（谁的标注）偏语文学细节**，面向形态学期刊可以压缩，细节移入结果或注释。

### 8.3 建议的 v7 讨论布局与篇幅预算（供 Qu 决定）

| 小节 | 内容 | 建议篇幅 | 学自 |
|---|---|---:|---|
| §5 开头 | 逐条回答 H1a–H4，各一句 | 约 100 词 | Cohen |
| §5.1 What the label marks | 重述核心概括；提出解释原则（明确标为假设）并推出可检验的后果 | 约 450 | Berg、Nikolaev |
| §5.2 Alternative explanations | 把稳健性检验改写成“替代解释—预测—结果—简约性” | 约 300 | Cohen、Huyghe |
| §5.3 Diagnosing derivation without overt morphology | 理论中心：转类与零派生的诊断；词本位 vs 词根本位（写出各自预测，不宣称词根理论被推翻）；声符系列作为派生词族 | 约 600 | Berg、Ševčíková、第一轮 Bonami & Strnadová、Arad–Rasin |
| §5.4 Whose label? | 压缩；王筠“总体一致、局部分歧”；版本层次的文本内证据 | 约 250 | Nikolaev、Igartua |
| §5.5 Yòuwén | 条件式化解“声符是否兼义”之争 | 约 150 | Sandell、Sandström |
| §6 Limitations | 去重；写明三条桥接假设；对释义依赖的精确让步 | 约 300 | Sandell、Nikolaev |
| §7 Conclusion | 回答引言问题；proof of concept；两三条数据以外的预测 | 约 250 | Berg、Nikolaev |

合计约 2,400 词，比现在多约 540 词。为守住 7,000 词上限，需要在别处压缩：例如背景 §2.1 对卷八的逐条引述可以减约 300–400 词（细节已在 `shili_pages/README.md`），结果中的部分稳健性叙述可以移进表注。

### 8.4 逐段改写建议

| v6 位置 | 现状 | 建议 | 学自 |
|---|---|---|---|
| 摘要 | 以《说文》与王筠为主线，末句提到形态理论 | 加一句点名一般问题（没有显性形态时的派生诊断），说明贡献 | 十一篇摘要的共同做法 |
| §1 末段或 §2.4 | 假设列表 | 为三种竞争解释写出对 H1a、H1b、H1c、H2 的预测，可做成小表：（a）纯字形分类（裘锡圭；段玉裁）；（b）一般派生的隐性标记（本文起点假设）；（c）同词或最小派生的标记（王筠分别文的延伸）；再加一条基线：（d）词库层面的弱音义系统性（Monaghan；Meng） | Lõo 的预测表；Berg |
| §5.1 | 经验概括 + 方向的分解 | 保留方向分解（它是全文最强的一步）；再提出解释原则，例如“许慎在认出声符字就是基词之字时才写‘从某，某亦声’”，说明它统一了同音、*-s、语义相关、方向不需标注、标注不穷尽（儐）五件事；明确标为假设，并给出可检验的后果（见 8.8 节） | Berg；Nikolaev 的“为什么有诊断力” |
| 新 §5.2 | 稳健性分散 | 一段写三到四个替代解释及其预测（示范见 8.6） | Cohen；Huyghe |
| §5.3 | 约 240 词 | 扩为理论中心；把“A root-based account would have to explain …”改写为：两种理论对标注分布各预测什么，本文数据能区分到哪一步，哪一步不能 | Berg；第一轮 Arad–Rasin |
| §5.2（现）→ §5.4 | 版本层次细节较多 | 压缩；用“fit well with … but diverge specifically with respect to …”概括与王筠的关系；若补做文本内一致性分析，可学 Igartua 用共存与频率裁决“扩标还是误增” | Nikolaev；Igartua |
| §5.4 → §5.5 | 右文说 | 写成条件式结论：强兼义集中在标注所标的最小关系，普通形声字只有弱的、样本限定的相关 | Sandell；Sandström |
| §6 | 三段局限 | 写明三条桥接假设；对“语义编码依赖许慎释义”写一段精确让步（示范见 8.6）；“未标注不等于无关系”（儐）作为方法论命题 | Sandell；Nikolaev；Saicová |
| §7 | 回答问题 + 推广到讀若、聲訓 | 首句回答问题后，把推广写成由原则推出的可检验预测；定位为 proof of concept | Berg；Nikolaev |
| 可选：讨论中加一张小表 | — | “前人主张计分表”（草稿见 8.5） | Barbu Mititelu；Saicová |

### 8.5 前人主张计分表（草稿，依据 v6 已报告的结果，需作者核定）

| 前人主张 | 出处 | v6 结果 | 判定 |
|---|---|---|---|
| 亦声是会意兼形声，是形声字的一个类别 | 段玉裁；裘锡圭 | 标注与同音、*-s、语义相关共变，而与其他词缀无关 | 作为字形分类不错，但不足以说明标注所记录的词际关系 |
| 亦声之第三种为“分別文之在本部者”，并有归部规则 | 王筠 1837 卷三 | 分化关系贯穿全部标注；归本部者不更常同音（9/34 vs 54/143） | 分别文说总体得到支持；归部判准不被支持 |
| 大徐多增标，以引申义并入声中 | 王筠 1837 | 仅大徐的 62 条更常同音（24/48 vs 35/122），同音者多为义项分化 | 大徐标得更宽且集中在引申义，得到支持；这些标注记录的是同一种关系，所以“误增”只是规范判断，不是统计结论 |
| 凡从某声皆有某义 | 右文说；段玉裁 | 普通形声字的抽样中，非专名者只有 6/50 相关（样本限定，不能外推） | 挑战：需要区分两种“兼义” |
| 派生词的声符往往就是基词之字 | Boltz 1994 | 去声 *-s 在形声字一方的比例，标注与否两组相同（约四分之三） | 一致，并解释了为什么标注不需要标方向 |
| 亦声是派生的隐性标记 | 本文起点假设 | 只对同词与 *-s 成立，一般词缀派生不成立 | 部分成立 |

写入正文时，第一、二行的措辞必须守住 `AGENTS.md` 的边界：王筠说亦声“凡三種”，第三种是“分別文之在本部者”，不能写成他把亦声等同于分别文。

### 8.6 示范段落（英文；数字取自 v6 正文，写入 v7 前按 `AGENTS.md` 回到结果文件复核）

**逐条回答假设（放在 §5 开头或 §7）**

> The hypotheses can be answered briefly. H1a: yes; labelled characters are homophonous with their phonetic more than twice as often as ordinary compounds on the same phonetics. H1b: no; other affixes and alternations do not set labelled pairs apart. H1c: yes, but not as we framed it; the label selects the \*-s relation, not its direction. H2: yes, and not merely because of paronomastic glosses. Of the exploratory comparisons, only the Xiǎo Xú collation separates the labels; Duan's changes and filing position do not.

**替代解释（新 §5.2）**

> Three other sources for the homophony effect can be named, and each predicts that it should vanish under a particular check. If it arose from Xu's habit of glossing a character by its own phonetic, it should disappear once such glosses are removed; it does not (31.7% against 15.4%). If it were an artefact of the Song editors of the Dà Xú, it should disappear on the 140 labels that the Xiǎo Xú shares; it does not (OR 1.94). If it reflected errors in matching Dà Xú fǎnqiè to *Guǎngyùn* readings, it should disappear when identity is coded directly from the fǎnqiè strings; it does not (OR 2.43). It is simpler to suppose that the label tracks identity of sound than that each check happens to preserve an artefact.

**说明检验为什么有诊断力（§5.1）**

> Had the label merely recorded Xu's belief that a phonetic may carry meaning, it would have no reason to covary with identity of sound or with the departing tone. That it covaries with these two relations, and not with the other affixes found in the same series, is what makes it informative about relations between words.

**桥接假设（§3.2 或 §6）**

> We assume that the sound relations visible in the Middle Chinese readings of member and phonetic, identity and a difference of tone alone, reflect relations between the words that Xu Shen analysed. The fǎnqiè check shows that the *Guǎngyùn* matching did not create these relations; it cannot exclude that some tone-change readings are later innovations, and the Old Chinese comparison, which covers only a quarter of the pairs, is the only partial check on this assumption.

**对释义依赖的精确让步（§6）**

> The semantic coding cannot be wholly independent of Xu Shen, since the glosses we coded were written in the same act as the label. Removing glosses that define a character by its own phonetic reduces this dependence but does not eliminate it: Xu may have glossed labelled characters in ways that bring out their relation to the phonetic even where the phonetic is not named. The sound results do not share this dependence, and they point the same way.

**与王筠：总体一致、局部分歧（§5.4）**

> The results fit Wang Yun's account, in which one of the three kinds of *yìshēng* is the differentiated graph filed in its own section, but diverge from it in two specific respects: differentiation is not concentrated where his filing rule places it, and the labels he rejected as Dà Xú additions fall mostly on the same minimal relations as the rest.

**概念验证（§7）**

> More generally, the study is a proof of concept: a native metalinguistic label can be tested like any other classification, against a comparison group and against sound and meaning evidence gathered independently of it.

### 8.7 严谨边界清单

**必须严谨（审稿人会逐项核对）**
- 标注与同音、*-s、语义相关的共变及其基准（同声符对照组、按声符聚类）；
- H1b 的零结果只说明“没有证据”，并写明上古音覆盖只有约 27%；
- “方向不能由标注诊断”——两组方向相同，这是可靠的推理；
- 版本口径：140 条两本共有 / 62 条仅大徐 / 10 条无从判断；227 条原始字头、212 条分析集（172 个声符）；
- 编码来源：κ = 0.773 是两次 LLM 编码的一致度，不能称为人工编码者信度；104 条大徐抽核是定点抽核，不是随机抽样；𨻺 只是这一印本的待解差异。

**可以推测，但要标明身份并给出检验办法**
- 许慎的认知或编纂动机（“认出声符是基词之字”）；
- 谁加了仅大徐的标注（徐铉、传抄者或更早）；
- 造字史的解释（Boltz）；
- 与词库层面音义系统性的关系；
- 对词根理论的含义——必须先写出两种理论各自的预测。

**不能写**
- “亦声是派生的隐性标记”（只部分成立）；
- “王筠把亦声等同于分别文”；
- “词根理论被推翻”；
- “仅大徐的 62 条是错误”（数据显示它们标的是同一种关系，只是更宽）；
- 把 196 对关系类型（在看得见标注时分类）当作支持王筠的独立证据。

### 8.8 数据以外的可检验预测与可选的新分析（均未执行）

下列各项若要进入论文，须先按 `AGENTS.md` 写脚本、生成结果文件、在 `youwen_criteria.md` 记录口径，并追加 `PROJECT_LOG.md`；未执行前只能作为展望。

1. **出土文献预测**（设计，Cohen 式）：若标注记录“声符字即基词之字”，被标注的字在早期写本中应更常直接写作声符字（同词异写），同音的普通形声字则不然。
2. **讀若、聲訓与段注“之言”**：若本文的原则成立，这些元语言手段与亦声重合的地方应集中在同音与 *-s 这两种最小关系上（v6 结论已提出推广，可改写成预测）。
3. **再分析前人材料**（Sandell 式）：用本文指标计算李宁、郭抒远 79 个“应标亦声”字，或王筠卷三讨论的 13 字的同音率与去声关系，看它们更像标注字还是普通形声字。
4. **文本内一致性**（Igartua 式）：在仅大徐标注所在的声符系列里，看大徐对同类成员是否时标时不标，以区分系统性的“扩标”与偶然的“误增”。

---

## 9. 写作自检清单

1. 这一段要解释的精确现象是什么？删去具体结果后，它会不会变成放在任何文章里都成立的空话？
2. 它回应哪个具名的前人命题？是证实、限定、挑战还是修订？
3. 这个检验为什么有诊断力？竞争解释会预测什么？
4. 比较基准是什么？结果会不会只是基准差异、类别不平衡或数学性质？
5. 从观察到解释的桥来自本研究、独立材料、既有理论，还是新增假设？写成假设了吗？
6. 最强的替代解释是什么？它的预测与结果对得上吗？
7. 零结果写成了“没有证据”还是“不存在”？候选原因是否对应到具体设计？
8. 哪些是推测？是否标明身份、先给了乏味但可检验的解释、说明了需要什么证据？
9. 命题强度与证据强度是否匹配？有没有把由前提推出的结论写成“与理论一致”？
10. 篇幅是否跟着理论分量走？最有分量的一环是不是最长？
11. 结论回答引言的问题了吗？有没有给出可检验的后果？
12. 删去最远的推测后，论文还剩什么独立成立的贡献？
