# v7 词汇关系术语与关键例组核对

日期：2026-09-29。执行者：Codex（独立论证审查）。

本文件为[系统修改计划](v6_系统重构修改计划.md)及后续 v7 改稿提供可追溯的解释依据，不重编码、不修改数据，也不新增人工标注。用户已将本轮交付收束为 plan；下文的改稿建议尚未形成完成版论文。核对对象是 v6、既有 `relation_types.py` 和主数据、开放《说文》电子文本及段注、已存王筠转录、O（2015）相关全文页。未重做大徐扫描或扩大 v6 的 104 条定点抽核范围。本文的“支持”指现有材料可承担的命题，不表示本轮完成了各字的历史词源考证。

## 1. 来源与定位

- 当前基线：[v6](yisheng_paper_v6.md)，尤其 §3.3、§4.4、§4.6、§5.1、§5.3。
- 既有类别：[关系分类字典](../scripts/relation_types.py)，`REL[(char, phonetic)]`；[主数据](../yisheng_dataset.csv)，`sw_id`、`char`、`phonetic`、`identical_relation_type`、`head_gloss`、`shuowen_gloss`、`mc_bs2014`、`head_mc_bs2014`。这些记录保持原样。
- 电子原文：本地 `youwen/scripts/shuowen/data/<sw_id>.json` 的 `explanation` 与 `duan_notes`，来源为公开仓库 `shuowenjiezi/shuowen`。数据文件中的声符释义见 `head_gloss`。下文保留关键原句，以便未检出这个被忽略的外部源码目录时仍可追溯核查。
- 王筠：[已有转录与书页索引](../shili_pages/README.md)。本轮复读转录及已有定位，不将既有初校转录冒称本轮重新逐字目验。
- O, Je-jung（2015）：本地 `/Users/johnwoo/Documents/Morphology/论文/参考文献MD/O_2015_王筠의 古今字 이론 연구 分別文과 累增字를 위주로.md`，重点印刷页 468、472–473、479–480（PDF 第 8、12–13、19–20 页）。相关摘述按可辨认正文，不据提取中缺失的罕见字建立新例。
- 大徐既有来源核验：[台账](daxu_spotcheck_v6.csv)和[审计说明](daxu_source_audit_v6.md)。本文件不增加该台账的核验状态。

## 2. v7 术语表与使用规则

| 推荐术语 | 本文所指 | 不应自动推出的判断 |
|---|---|---|
| **graph / character form**（字形） | 文字形式或《说文》所分析的字形单位；讨论附加构件、归部、异体时使用 | 一个新字形必定表示一个新词；字形相承已经证明历史派生方向 |
| **member graph / phonetic graph**（字头字／声符字） | 数据配对两端的图形位置 | 默认把声符所表之词称为 base、字头所表之词称为 derivative |
| **lexical item / lexical relation**（词汇项／词际关系） | 两端用法、意义及声音之间的语言关系；在身份未定时使用中性措辞 | 一组音义相关词必定具有本研究已经确定的共时形态结构 |
| **lexeme identity**（词位同一） | 两种写法是否代表同一词位的问题 | 同音、相同短释义、共同词源中任一项单独足以确认同一词位 |
| **homophony / identity of the selected MC readings**（同音） | 数据所采用的中古读音相同 | 历代读音均相同、没有异读、或上古必无形式差别 |
| **semantic relatedness**（语义相关） | 盲编码 Y/E 所操作化的近义或一步引申；描述性例证另注明来源 | 同词、同源或派生已被各自确证 |
| **graphic augmentation (L)**（原编码累增类） | 保留原编码意图：增加构件而被分析为同词或近乎同义的字对 | 本轮独立验证了全部 L 项的词位同一性；不能重命名为纯机械的“释义相同”，因为既有 L 项并不都直接呈相同基本释义 |
| **sense differentiation (F)**（原编码分义类） | 保留原编码意图：另字承接声符字的一个义项或相关意义 | 每例都只是一个词的义项、从未构成新词位；也不等于王筠全部分别文 |
| **conversion candidate (C)**（原编码转类候选） | 原 C 类在非盲描述性分析中提出的词类转变候选；保留 5 例与原代码 | 已经证明 5 次历史零派生、已经确定其词类及方向 |
| **derivation with an overt phonological contrast**（带可观察音系差异的派生） | 在形式、意义及历史材料共同支持时使用 | 把 conversion 排除出“真正的派生”，或把任何去声差异都当作同一功能的后缀 |
| **departing-tone relation**（去声关系） | 本文限定的声调／清浊交替中涉及去声的形式关系 | 单凭此项决定派生功能、词类、方向，或把所有去声词都算作本次指标 |
| **fēnbiéwén / lěizēngzì in Wang Yun’s account** | 王筠关于附加偏旁、意义区别及文字使用的原典类别 | 直接等同于当前数据 F/L；把古代“字”一律翻译为现代 lexeme |

建议在方法中使用：

> The existing descriptive coding assigns homophonous pairs to graphic augmentation (L), sense differentiation (F), conversion candidates (C), unrelated homophony or borrowing (U), and proper names (X). The first two labels retain the intended distinctions of that coding, but do not independently establish whether the relevant uses instantiate one lexeme or two.

随后准确保留原操作定义及非盲、作者复核的来源说明。这里调整的是根据编码作出的推论强度，不是改动数据或重新划分类别。

## 3. 五个 C 例：保留编码，校准解释

全部五例在主数据中均为亦声、进入分析集、`mc_relation=identical`，`identical_relation_type=C`。读音为**本数据选定的 MC 读音**。下表不提出任何替代代码。

| 数据键与读音 | 电子原文及段注依据 | 现有材料支持什么 | v7 可以使用的表述 |
|---|---|---|---|
| `冒/瑁`；`sw_id=120`；*mawH* | 冒「冡而前也」。瑁「諸侯執圭朝天子，天子執玉以冒之……天子執瑁四寸」。段注引郑注「名玉曰冒者，言德能覆葢天下也」，并说「考工記以冒爲瑁」 | 冒的动作义与瑁的器物指称之间有明示联系；瑁/冒的用字替换也有段注记载。二者可作为动作—器物关联的转类候选，但同词异写和词类关联属于不同用法层次 | “冒–瑁 is a conversion candidate involving an action and a ritual object; Duan also records 冒 as a spelling of the object name.” 不写“字形改变但词完全没变” |
| `朿/刺`；`sw_id=2794`；*tshjeH* | 朿「木芒也……讀若刺」。刺「君殺大夫曰刺。刺，直傷也」。段注认为「刺、直傷也，當爲正義」，并列诸引申义；另记「又七迹切」 | 刺／伤的动作与树刺、尖锐部位的名物义构成可理解联系，名物—动作分析有较直接的释义基础；但两端相同去声读音不证明两端从未有其他形式或既存形态历史 | “The glosses of 朿 and 刺 support a noun–action relation under the selected homophonous readings.” 不将零派生方向当作本轮确证 |
| `耒/䒹`；`sw_id=568`；*lwojH* | 耒「手耕曲木也」。䒹「耕多艸」。段注「耒所以耕也。從耒艸會意」 | 耕具与耕作相关活动／状态存在联系；释义过短，不足独立确定䒹的词类、论元行为及构词方向 | “耒–䒹 links the name of a ploughing implement with a use associated with cultivation.” 可注明是 C 候选，不用它单独证明 productive denominal conversion |
| `臽/陷`；`sw_id=9595`；*heamH* | 臽「小阱也」。陷「高下也。一曰陊也」。段注「高下之形曰陷。故自高入於下亦曰陷。義之引申也」 | 坑阱与高下地形、落陷之间有意义联系，但段注特意先述形势，再述动作引申；基本释义不等于现代常用动词“fall into” | “臽–陷 is a conversion candidate in the existing coding, although Duan distinguishes a configuration of terrain from the extended event reading.” 不能直接用“小阱→落入”盖过原释义 |
| `芻/犓`；`sw_id=757`；*tsrhju* | 芻「刈艸也」。犓「以芻莖養牛也」。段注将后者校为「以芻莝養圈牛也」，并记「經傳犓豢字，今皆作芻豢」 | 本数据给芻的基本释义是刈草的动作，而犓也是喂养活动；若分析成“fodder名词→feed动词”，必须引入芻的名词义，不能声称只根据所呈两条基本释义便有名→动。段注另提供用字相替的联系 | “芻–犓 requires sense selection before a conversion analysis can be made: the stored gloss of 芻 is verbal, whereas a fodder-based analysis invokes a nominal use.” 不重编码，也不把它作为已确证转类例 |

**处理决定：** v7 保留原五项和原计数，称为 *conversion candidates in the descriptive coding*；逐例表置于补充材料或本审计中。正文无需逐项展开，也不以“5 对 0”为独立的零派生证明。可以明确说：若某例最终确证为转换派生，语音不变本身不取消其词位变化；这是一项概念区分，不是新增的五例实证结论。

## 4. L/F 边界及正文典型例组

### 4.1 反–返：同音且有意义联系，不自动等于一个词

- 数据键：`反/返`，`sw_id=1140`；原 F；数据 MC 两端 *pjonX*，OC 两端 `*Cə.panʔ`。
- 反「覆也」；返「還也」；段注在返下说「反覆也。覆復同」。反与返在数据中并非相同大徐反切串（府遠切／扶版切），本文的同音结论来自采用的 MC 匹配值；返匹配置信项为 `initial_only`。不另作读音重编码。
- 可支持：相关行动意义在另加构件的字形中得到区分；原 F 分类的解释对象是义项联系。
- 不可据此直接支持：“既然同音且相关，所以本来同一个词”；现代英译 *turn over / return* 本身也不能完成历史词位判定。
- 推荐正文：

> 反 and 返 have identical selected MC readings but different, connected glosses, 覆 “turn over” and 還 “return”. Their treatment as sense differentiation in the descriptive coding identifies a semantic connection; it does not itself decide whether the uses belong to one lexeme.

### 4.2 句–鉤：相同短释义与不同解释层次

- 数据键：`句/鉤`，`sw_id=1453`；原 L；MC 两端 *kuw*。
- 大徐两条均「曲也」。段注将鉤释义补作「曲鉤也」并说「曲物曰鉤。因之以鉤取物亦曰鉤」；再用吳鉤、釣鉤等说明金旁。
- O（2015）印刷页 468／PDF 第 8 页，讨论拘、笱、鉤为在句上加偏旁、保留“曲”义而发生意义区别的分别文。其解释不是本项目 L 编码。
- 可支持：短释义相同并未穷尽两字的全部词汇功能；同一例可在不同分析目标下归为“释义接近的增旁关系”或“分化关系”。
- 不可支持：把英文 *hook* 和 *bent* 当作无疑的同一个词；也不能据 O 的分析悄悄改 F。
- 推荐正文：

> 句 and 鉤 both receive the short gloss 曲也 in the Dà Xú text, which underlies their L assignment. Duan’s fuller account distinguishes the curved object and the act of hooking. Identical short glosses therefore do not by themselves settle lexeme identity.

### 4.3 頃–傾：原代码与王筠术语不一一对应的最清楚例子

- 数据键：`頃/傾`，`sw_id=5030`；原 L；本数据 MC 两端 *khjwieng*。
- 頃「頭不正也」；傾「仄也」。段注傾：「古多用頃爲之」；并提出仄当作夨、说明由倾头义引申的分析。
- 王筠卷八 6a/9–6b/2：先引頭不正、仄，后说「云不正，則凡不正者之統詞矣……知傾、𨻺皆頃之分別文」。这是现有转录明确的分别文判定。
- 可支持：段注记录同一倾斜用法的不同书写；王筠把字形承接与意义分别作为分类依据。因此原编码 L 与王筠分别文可落在同一对上，证明二者分类任务有别。
- 不可支持：所有 L 和 F 都等于同词异写；也不凭本例声调和字形推定造字先后。
- 推荐正文：

> Duan records 頃 as an earlier spelling for the use written 傾, whereas Wang calls 傾 a fēnbiéwén of 頃. The pair’s L assignment in our descriptive coding and Wang’s graphic classification consequently answer different questions.

正文优先使用傾；不必把未在已查大徐位置寻得的𨻺继续作为平行实证重点。

### 4.4 取–娶：王筠一个图形类别可以包含另一种声音关系

- 数据键：`取/娶`，`sw_id=8086`；非同音，不在 L/F/C 的196对编码框内。MC *tshjuX / tshjuH*；现有 BS 形式 `*tsʰoʔ / *[ts]ʰoʔ-s`。
- 取「捕取也」；娶「取婦也」。段注「經典多叚取爲娶」；他采用小徐取聲而不保留亦声。
- 王筠卷八 7b/2–6 明称「娶爲取之分別文」，列典籍取／娶异文，却同时判大徐「從取，取亦聲」为「非例」。卷三 14a/3–6 同样反对其亦声，因「皆引伸之義，非本義也」。
- 可支持：同一个分别文类别跨越傾—頃的本数据同音关系与娶—取的声调差别；传统字形分类不直接规定某一种音系关系。取作为娶的异写，与广义“取”的词项在选定读音上存在去声对应，可同时成立。
- 不可支持：王筠认可娶为亦声；古籍用取书写娶就证明该用法必读取的上声；或所有分别文都没有派生。
- 推荐正文：

> Wang’s fēnbiéwén category includes both 傾–頃 and 娶–取, although the selected readings are identical in the first pair and differ in tone in the second. His category concerns graphic differentiation and therefore cuts across the phonological relations tested here. His rejection of 娶’s yìshēng label must be kept separate from his recognition of its differentiated graph.

### 4.5 关于 L/F 合计

原描述性计数 8 L + 42 F = 50／63 可以报告为“50 pairs assigned to L or F in the descriptive coding”。不建议再概括为“50确证同一个词或同一个词的一个义项”，因为后者需要词位身份判断，而本轮没有新增该项分析。亦不宜把原 L 整类改定义为“两个基本释义相同”：例如现代码中的不—否、象—像，其存储的声符基本释义与字头释义并不呈直接的同义对应。现编码及作者复核事实保持不变，论证不让它承担尚未操作化的词位诊断。

## 5. 賓系列：保留比较价值，修正儐的释义拼接

三对均采用字头 *pjinH* 与声符賓 *pjin*；主数据声符释义为「所敬也」，正文 *guest* 是约略释义。三例足以显示同一形式对立并不自行决定同一种语义联系。

| 字对及来源 | 核对的原句 | 可以承担的论证 |
|---|---|---|
| `賓/殯`，`sw_id=2533` | 大徐「死在棺，將遷葬柩，賓遇之……賓亦聲」。段注引檀弓「殯於客位」「賔之也」，同时反对该释义中「將遷葬柩」的文本次序／增改 | 标签、去声对应和传统解释中的宾客语义联系汇合，是一个有具体解释内容的派生候选；不能凭大徐释义的聲訓独自证明词源。现有数据库未给殯的 BS OC 形式，不宣称两端均有该数据库的独立重建 |
| `賓/儐`，`sw_id=5008` | 《说文》「導也。从人賓聲」，另有擯或体。段注先讨论「出接賓曰擯」，然后另论礼经儐的用法：「取賓禮相待之義。非擯相之義也」；又说「擯相字當从手，賓禮字當从人。許儐擯合而一，云導也，與二禮及鄭說不合」 | 普通聲字中也有可进一步考察的与賓有关用法；但 Duan 对“以宾礼相待”的分析修订并区分了《说文》合并的词义，不能把它无缝贴到 *to usher* 上。也不据同一字头读音自动判定这些被分出的用法同一词或同一读音层次 |
| `賓/鬢`，`sw_id=5701` | 大徐「頰髮也。从髟賓聲」。段注「鬢者，髮之濱也」 | 相同去声对应可伴随在这些释义中看不出宾客语义的词。段注提供的是另一条濱的解释线索，不是本轮已确认的替代词源 |

### v6 的具体问题

原句把儐称为 *to usher [guests]*，紧接着说 Duan 将它联系到 *treating someone by the rites due to a guest*。但段注恰好说后者“非擯相之義”，并批评《说文》“儐擯合而一”。若省去这个分歧，便将一项释义修订写成对原释义的直接认同。

### v7 可用段落

> The 賓 series makes the contribution of the label concrete. 殯, with the departing-tone reading *pjinH* beside 賓 *pjin*, bears the label and is explained through treating the dead as a guest. 儐 and 鬢 have the same selected departing-tone reading but ordinary 聲 analyses. Their meanings diverge. The gloss 頰髮 “hair on the cheeks” for 鬢 supplies no guest-related connection. For 儐, the relation requires closer lexical analysis: the Shuōwén gives 導 “to lead”, whereas Duan distinguishes ushering from treating someone with the rites due to a guest and connects the latter use explicitly to 賓. The unlabelled entry therefore contains a further candidate for lexical investigation, without making the selected tone contrast or the absence of the label decisive on its own.

如篇幅允许，可接一句：

> Duan’s distinction also shows why the meaning attached to a graphic entry cannot always be treated as a single, already identified lexeme.

这使例组同时承担两个正面任务：说明形式对立需要语义分析；说明文字标签有选择性但不穷尽相关候选。它不承担三条完整词源均已重建的任务。

## 6. 王筠原典在 v7 中各承担什么命题

| 已有定位与原句 | 可以直接使用的认识 | 避免的扩大 |
|---|---|---|
| 卷三 10a/7–8：「言亦聲者凡三種……分別文之在本部者，三也」 | 分别文归本部是三种亦声之一 | “亦声就是分别文” |
| 卷三 10a/9–10b/2：「在異部者，概不言義；在本部者，概以主義兼聲也」 | 王筠提出归部与说解方式的规范 | 将本文同音率的经验预期直接说成王筠自己的统计预测 |
| 卷八 1a/4–8：「其加偏旁而義遂異者……正義爲借義所奪……本字義多……義仍不異者……累增字」 | 分类以加旁及意义分担／保留为核心，并包括借义排挤等情形 | 将两类等同现代词位、派生、或单一音系规则；“借义”也不能统统说成同词内部引申 |
| 卷八 1b/4–5，援：「乃變例以著其爲一字也」 | 王筠用“一字”表达其对援／爰关系的判断 | 不作说明便译为已被现代标准验证的 *one lexeme*；可保留引号 *one zì* 并解释上下文 |
| 卷三 1a：「亦聲必兼意；省聲及但言聲者，亦多兼意」 | 他承认未标亦声也可有意义联系，适合引入程度比较 | 让王筠预测普通形声字一律无语义关系 |
| 卷三 13a/5–6：「凡引申假借之義，皆併入聲中……」；14a/3–6，娶婚姻 | 本义／引申／借义和释义中已显现的意义影响其标注判断 | 只用传本一致性解释他的所有拒收；婢两本共有他仍拒收 |
| 卷八 6a/9–6b/2（傾）、7b/2–6（娶） | 同为分别文而声音关系不同，且娶被拒绝亦声 | 把“图形分类”与“认可标签”混成一次判断 |

O（2015）印刷页 479–480／PDF 第19–20页将古今字的载籍用字问题与分别文／累增字的造字相承问题分开。v7 可据此建立分析层面，不将其论述改写成“凡分别文都不是同词异写”；两类现象在实际对象上可以相交。

## 7. 本轮可落实的修改边界

1. 删除“同音的前两类都是词不变的 graphic events”“only affixed forms are derivation proper”等句。
2. 将五 C 称为既有描述性编码中的候选，保留原值，放补充表；不据它们新增转换派生比例的确证性推论。
3. 用傾／娶说明传统图形范畴跨越不同声音关系；用鉤／句说明相同短释义不解决词位身份；返／反只表述为同音及可解释的意义联系。
4. 賓系列保留；显式呈现段注对儐／擯的意义区分，避免嫁接两义。
5. 若以后要确证零派生，需要逐义项的句法用例、词类诊断及读音来源；这属于另行分析，本轮未执行，不能在改稿中伪装已经完成。
