# Morphology 投稿核对表（v10）

日期：2026-10-01。依据：Qu 2026-10-01 04:08 随消息发来的两份 PDF（Morphology 的 *Submission guidelines*，Springer Nature 的 *Submit faster on Snapp*）。对象：本目录下的投稿文件和 `youwen/manuscript/yisheng_paper_v10*.md`。

状态只有三种：**满足**（做了，且有检查依据）、**不适用**、**需 Qu**（只有 Qu 能给或能定）。机器核对的项目由 `youwen/scripts/yisheng_submission_audit.py` 执行，输出存在 [`audit_v10_output.txt`](audit_v10_output.txt)；括号里的名称是脚本里的检查项。Word 里的实际显示我这里无法看到（只用 LibreOffice 渲染逐页看过），见最后一节第 9 项。

## 1 要上传什么

| 要求（指南原文大意） | 状态 | 说明 |
|---|---|---|
| 稿件用 Word（.docx），正文、图、表放在同一个可编辑文件里（Source Files；Snapp：single editable file） | 满足 | `Manuscript_anonymised.docx`：12 个 Word 表格，图 1 嵌入，页码为自动页码，无域代码、尾注、批注和修订痕迹 |
| 图单独提供时，矢量用 EPS、半色调用 TIFF，文件名为 “Fig” + 编号（Fig1.eps） | 满足 | `Fig1.eps`（字体已嵌入）、`Fig1.tif`、`Fig1.png`；嵌入稿件的是 PNG |
| 双盲：作者信息和声明在系统界面里填，不放在稿件里或单独的题名页里 | 满足（需 Qu 在界面里填） | 匿名稿不含任何作者信息，也不含致谢、贡献、竞争利益、伦理、基金声明（第 4 节）；`Title_page.docx` 不上传，仅作为在界面里逐项填写的底稿，系统若要求题名页再传 |
| 先上传稿件，不要预先填字段；上传后核对系统自动抽取的标题、摘要和声明（Snapp） | 需 Qu | 上传后核对一次抽取结果 |
| 补充材料：见第 8 节 | 满足 | 七份文件 ESM_1–7（数据线程第二轮 2026-10-01 14:07 改完措辞）已核对并入库；许可和 Baxter–Sagart 列见第 11 节，待 Qu |
| cover letter | 满足 | `Cover_letter.docx`；署名 Yusen Wu、“再用过材料” 一条已按 Qu 的回答写好；日期投稿时补 |

## 2 正文（Title Page、Text）

| 要求 | 状态 | 说明 |
|---|---|---|
| 题名简明、有信息量 | 满足 | 15 个词 |
| 摘要 150–250 词，无未定义的缩写和未指明的引用 | 满足 | 246 词（把 亦聲 两个字各算一词为 247；按空格分词的 Word 口径）（abstract 150-250 words；no abbreviations in the abstract） |
| 4–6 个关键词 | 满足 | 6 个（4-6 keywords） |
| 十进制标题，不超过三级 | 满足 | 31 个标题，最深三级（decimal headings） |
| 缩写在首次出现时定义，之后一致使用 | 满足 | 人工逐个核过：MC、OC、OR、CI、GEE、MH 都在首次出现处定义；其余是代码字母（I、R、O、V、C；Y、E、N、X；L、F、C、U）和表内说明 |
| 脚注用脚注不用尾注；脚注不只含引文、不含书目信息、不含图表 | 满足 | 全文没有脚注（0 个），也没有尾注 |
| 正文用朴素字体（如 10 pt Times）；强调用斜体；自动页码；不用域功能；缩进不用空格；表格用表格功能；公式用公式编辑器 | 满足 | Times New Roman 11 pt、1.5 倍行距、A4、页边距 25 mm；汉字例证用宋体；没有公式 |
| 语言模型不得列为作者，使用须写在方法部分 | 满足 | §3.6 “Use of large language models”；Claude 与 Codex 都不在作者名单里；cover letter 里也写明 |
| 英文为主要呈现语言（Qu 04:08） | 满足 | 正文、表图标题、题名页、声明全是英文；汉字只作例证和数据，均有拼音或英文释义（含表格约 470 个汉字，对约 1.1 万个拉丁字母词；no paragraph that is mostly Chinese） |
| 字数 | 满足 | 正文 8,838 词，表格与注 2,044 词，37 条参考文献；Morphology 的指南没有字数上限，往期论文 1 万–2 万词（Qu 2026-09-30 13:58 已放开上限） |

## 3 作者信息（在界面里填；底稿是 `Title_page.docx`）

| 要求 | 状态 | 说明 |
|---|---|---|
| 作者姓名、单位（机构、院系、城市、国家） | 满足 | Yusen Wu、Weiyi Qu；Beijing Foreign Studies University, School of English and International Studies, Beijing, China。姓名拼写和顺序一经接收不可改，请 Qu 最后确认一次 |
| 明确标出一位通讯作者及其可用邮箱（Snapp：一位 responsible corresponding author） | 满足 | Yusen Wu，wu_yusen825@icloud.com（Qu 2026-10-01 13:49、14:10）；Weiyi Qu 的邮箱 202520101018@bfsu.edu.cn |
| 两位作者的 ORCID（有则填） | 满足 | 两位都没有（N/A，Qu 13:49） |
| 致谢 | 满足 | “None.”（无基金、无致谢，Qu 2026-09-30 13:58） |
| 作者贡献声明（必须在界面里填，只有界面里的会进入发表版） | 满足 | 按 Qu 的原话（Qu 参与编码和文献综述，其余 Wu 完成，Wu 在前）并按 Qu 要求的 “更具体” 写成 CRediT 句，Qu 14:16 确认 “对”（第 9 节第 6 项） |
| 竞争利益声明（必须在界面里填）；编委成员须自行声明 | 满足 | “no competing interests”（Qu 2026-09-30 13:58、10-01 13:49）；两位都不是 *Morphology* 编委（Qu 14:10 “都不是”） |
| 基金信息（界面里填） | 满足 | 无基金：“The authors did not receive support from any organization for the submitted work.” |
| 试验注册号 | 不适用 | 非临床试验 |

## 4 Statements and Declarations（匿名稿里只留数据可用性声明，其余在界面里填）

**两处说明不一致，我按 Snapp 页办。** Morphology 的指南 PDF 说 “Statements and Declarations” 一节随论文发表，没有声明的稿件 “will be returned as incomplete”，但同一份指南开头又说，本刊换用 Snapp 后，作者贡献、竞争利益等 “instead of including it in the manuscript” 而在界面里填，并写明 “we are currently working on revising our submission guidelines”。Springer Nature 的 Snapp 双盲页（springernature.com/gp/snapp/submitting/how-to-submit/double-anonymous，2026-10-01 抓取原页核对）明确写：“Your manuscript file should not include: author acknowledgements or contribution statements; a competing interest statement; an ethics statement; funding information”，这些由 Snapp 询问，填入的内容会进入发表版；该页没有提到数据可用性声明，也没有提到单独的题名页。所以 v10 的匿名稿只保留 Data availability，其余声明的英文底稿在 `Title_page.docx`，在界面里填。

| 要求 | 状态 | 说明 |
|---|---|---|
| 稿件文件不含致谢、作者贡献、竞争利益、伦理、基金信息（Snapp 双盲页） | 满足 | 匿名稿的 “Statements and Declarations” 下只有 Data availability；Funding、Competing interests、Ethics approval and consent 三段移出，“Coding” 一段（谁编了什么，含作者姓名，内容已见 §3.3–3.5）也不再放在匿名稿里；脚本逐项检查（manuscript file has no … statement） |
| 这些声明各有英文底稿、在界面里填 | 满足 | `Title_page.docx`：Funding、Competing interests、Ethics approval and consent、Author contributions、Data availability；贡献和编委身份待 Qu（第 3、9 节）。全文版 `yisheng_paper_v10.md` 保留完整的 “Statements and Declarations”（含 Coding） |
| 伦理、同意、动物 | 不适用 | 界面里填 “Not applicable. The study analyses historical texts and involves no human participants or animals.” |
| 数据可用性声明：说清数据在哪里、怎么取；每个数据集写明标题、仓库名、持久标识符（如 DOI）；不公开的要解释 | 满足（可选增强见第 9 节） | 属于 Snapp 页列的第三种写法 “Included in the paper or Supplementary Information”：数据、编码、材料、结果表和代码都作为 Online Resource 1–7；源文本与数据库按 §3 引用。尚无 DOI。匿名稿里有，界面里再粘一次 |
| 代码可用性 | 满足 | 并入数据声明（Online Resource 7） |
| 万一编辑部回信要求把声明写进稿件 | 需 Qu 知悉 | 全文版里有现成的 “Statements and Declarations”：删去 Author contributions 一段（它会含作者姓名缩写）后即可贴回匿名稿；Morphology 指南那句 “returned as incomplete” 针对的是没有声明的稿件，在界面里填了应算有 |

## 5 参考文献

| 要求 | 状态 | 说明 |
|---|---|---|
| 正文用 “作者 年份” 括号引注；遵循 APA 第 7 版（作者最多列 20 人） | 满足 | 最多 5 位作者；二手引用只列实际读过的（Wang Li 1982 经 Zeng 2002） |
| 列表只含正文引过的、已发表或已接受的作品，按第一作者姓氏排序 | 满足 | 37 条（every dated reference is cited；reference list alphabetised） |
| 刊名、书名用斜体 | 满足 | （journal and book titles italicised） |
| 有 DOI 的一律写成完整 https://doi.org/ 链接 | 满足 | 17 条有 DOI，均经 Crossref 核对；20 条没有（古籍、中文论著、会议论文，Crossref 查无） |
| 引用数据：建议用 DataCite 格式把公开数据（含自己随文提供的和重用的二手数据）列入参考文献，带 DOI | 需 Qu | 可选。需要先有数据集的 DOI（见第 9 节） |

## 6 表和图

| 要求 | 状态 | 说明 |
|---|---|---|
| 表用阿拉伯数字编号，按数字顺序在正文里引用，每表有标题 | 满足 | 12 张表，首次引用顺序 1–12（tables cited in consecutive order；v9 里 5 处向后引用已改成章节引用） |
| 表注用上标小写字母，放在表体下面 | 满足 | 表 1、6、8 有字母注，字母与表注一一对应（footnote letters match） |
| 已发表材料须在表题末注明来源 | 不适用 | 所有表都是原创 |
| 图：用阿拉伯数字编号、按顺序引用；标题在正文里，不在图里；标题以粗体 “Fig. 1” 开头，编号后和标题末尾不加标点；说明图中所有元素 | 满足 | Fig. 1 标题写明实线、虚线、四种标记的含义和数字的含义 |
| 图的文字用 Helvetica 或 Arial，字号统一（8–12 pt），线宽至少 0.1 mm，不用阴影；图里不放标题 | 满足 | Liberation Sans（与 Arial 度量兼容）8 pt，线宽 0.6–1.0 pt |
| 线条与文字混合的图至少 600 dpi；RGB 8 位；指明作图程序 | 满足 | 600 dpi，RGB；作图用 Python 3 + matplotlib，写在 cover letter 和作图脚本头部 |
| 尺寸：小开本期刊的图宽 119 mm、高不超过 195 mm；Snapp：至少 1500 × 1200 像素，PNG、高质量 JPEG、SVG 或 EPS | 满足（开本为假设） | 119 × 105 mm，2811 × 2490 像素。我按 “小开本” 取 119 mm，没有查到 *Morphology* 的开本；排版时被缩放不影响审稿 |
| 无障碍：有描述性标题；不只靠颜色区分；文字对比度不低于 4.5:1；不引用颜色 | 满足 | 黑白，用标记形状和实心/空心区分；DOCX 里的图有替代文字（caption does not rely on colour words） |
| 已发表的图须有版权许可；生成式 AI 图像须符合政策 | 不适用 | 图 1 是我们自己用数据画的，没有用生成式 AI 图像 |

## 7 双盲与原创性

| 要求 | 状态 | 说明 |
|---|---|---|
| 匿名稿的正文、DOCX 内部各部分（XML、属性）和图片元数据里没有作者姓名、单位、仓库属主名 | 满足 | 脚本逐项查了 Yusen、Weiyi、WuYusen、Beijing Foreign、BFSU、Foreign Studies、github.com/WuYusen825（正文和 DOCX 全部 XML 部件）；作者、最后修改者属性为空；EPS、TIFF、PNG 无作者或路径信息 |
| 稿件里不放可识别身份的自引 | 满足 | 参考文献里没有两位作者的作品；正文不含 Wu、Qu |
| 稿件原创、未曾发表、未同时投他处；如有再用（学位论文、会议稿）须在 cover letter 里说明 | 需 Qu | cover letter 写了 “原创、未发表、未一稿两投”，“再用的材料” 一条留作 Qu 确认 |
| 全体作者已批准稿件及其提交；所在机构（如需）已同意 | 需 Qu | cover letter 已写 “All authors have approved…”，请 Qu 确认属实 |
| 可推荐或回避审稿人（可选）；推荐须附机构邮箱或主页链接 | 需 Qu（可选） | 不填也可以 |
| 第三方数据与软件的使用许可 | 满足（Qu 14:16 同意） | ESM_1 §8 和各文件的 About／README 写明来源与条款：*Shuōwén* 文本 Apache-2.0；中古音（nk2028 的 Qieyun 数据 CC0，tshet-uinh 软件 MIT）；上古音构拟字符串来自 Baxter–Sagart，经 cddb 仓库（GPL-3.0），引用时请引 Baxter 和 Sagart（2014）。作者自己的贡献（编码、标注、表、文档）用 CC BY 4.0、代码用 MIT，是数据线程提议的，由 Qu 定。我没有核各来源的 LICENSE 原文（这些仓库不在本环境可访问的范围内），上述条款是数据线程读原文后写的。是否在 CC BY 4.0 的文件里再分发 GPL-3.0 仓库里的 Baxter–Sagart 构拟串，请 Qu 定：保留（现状，各列保留原条款，文件里已写明），或删去 `oc_bs2014`、`head_oc_bs2014` 两列只留派生类别（会影响 ESM_7 的自检，要数据线程重做） |

## 8 补充材料（Supplementary Information）

数据线程 2026-10-01 09:49 交付七份文件（共约 1.8 MB，在共享文件夹 `v7_work/submission/supplement/`；第二轮措辞修改后已复核并提交进仓库的 `youwen/manuscript/submission/supplement/`）。我对着文件本身核的，不是对着数据线程发来的缩写。

| 要求 | 状态 | 说明 |
|---|---|---|
| 文件按 ESM_n.ext 连号命名；文字用 PDF，表格用 xlsx/csv，多文件打成 zip；每份附一句简明 caption | 满足 | ESM_1.pdf（13 页）、ESM_2.xlsx、ESM_3.xlsx、ESM_4.pdf（9 页）、ESM_5.zip（34 个文件）、ESM_6.xlsx（21 个 sheet）、ESM_7.zip（69 个文件）；名称与 SI 一节一致 |
| 正文里写明引用，格式 “Online Resource n”；正文里放每份的 caption | 满足 | §3.1、§3.3–3.6 引用，首次引用顺序 1–7；“Supplementary Information” 一节列出 7 条 caption（Online Resources cited in order；each listed with file name and caption） |
| 每份文件自带的 caption 与正文里的一致 | 满足 | 脚本比对 7/7（PDF 首页、xlsx 的 About 表、zip 里的 README），字词逐字相同；撇号和引号的字形除外（Word 稿里是弯引号，ESM_3、ESM_5、ESM_6 里是直撇号，独立评审指出，不影响内容，不改） |
| 补充材料原样发布，不转换、不编辑 | 满足 | 数据线程第二轮（14:07）改完措辞后的文件就是要上传的文件；已入库 `submission/supplement/` |
| 每个文件里写明文章题目、刊名、作者姓名、通讯作者单位和邮箱 | 需 Qu 知悉 | 与双盲相冲突：每份文件开头有识别块——题名、刊名、caption，“Authors” 和 “Corresponding author” 都写 “Withheld for double-anonymous review”，录用后再补 |
| 提供数据给审稿人时，数据里的作者信息也应匿名（Research data and peer review） | 满足 | 文件属性全空（xlsx、PDF、zip 里的 xlsx）；我扫了七份文件的全部文本、单元格、属性、zip 成员名和额外字段，没有姓名、单位、邮箱、本地路径和会话号；仓库链接只有两个开源来源（digling/cddb、shuowenjiezi/shuowen） |
| 数据与论文数字一致 | 满足 | 行数与 caption 一致：1,333 对、212＋953、227 条对勘、104 条登记、100 对、767 对（677＋90）、126 条核验（76＋50）、203 条第二次回答（193＋10）；我在这里解压 ESM_7 跑 `python scripts/run_all.py`，249 项通过、0 失败（25 个预期输出一致、189 个论文数字、20 项完整性），约 50 秒 |
| 英文为主要呈现语言（Qu 04:08） | 满足 | 所有表头、说明、文档都是英文，汉字只作数据，每个汉字列带 U+ 码位列 |
| 文件版面 | 满足（有限） | 这里没有 Excel 和 Acrobat：用 openpyxl 和 PyMuPDF 读了结构，渲染看了 ESM_1 的第 1、11 页（CJK 字体已嵌入）；xlsx 没有在 Excel 里打开过 |
| “谁做了什么” 与论文、`coding_provenance_v6.md` 一致 | 满足 | ESM_1 §4.1、§4.4、§5、§9 逐句对过，没有新增的说法；两处措辞数据线程已改（第二轮，我重核：锚定条目 “每批加 5 个，共 35 个，每遍各编一次”；小徐对勘抽查 “by the Claude instance that supervised the round … no human check of the collation”；“coders (Claude instances)” 加了约定）。仍是正文没写、但有记录依据的两句：核验表上显示过抽查类型，关系类型由建数据集的 Claude 实例标注 |
| ESM_4 §7 “偏离记录” 是完整的原始记录 | 需 Qu 知悉 | 里面有 13:25 把核验表记成 “together” 的条目、18:37 的更正条目（附作者原话的译文）和提交号 7b7c249；与论文 “later changes are logged (Online Resource 4)” 一致，是真实记录，审稿人能读到那次更正的来龙去脉。要删减的话只能不改事实和数字 |
| 作者核验原表的作者信息 | 需 Qu 知悉 | 仓库里的 `youwen/ext_coding/ext_check_sheet_author_filled.xlsx`（Qu 上传的原表，逐字节原样保存）的 “最后修改者” 属性是作者本名；补充材料里用的是合并后重建的表，没有这个问题。以后做 OSF 或 Zenodo 的匿名数据副本时不要放它，或先洗掉属性；仓库若要公开，同样先处理 |
| 重建脚本 | 满足 | 已提交到 `youwen/scripts/supplement_build/`（内部，不上传；`README_REPO.md` 说明路径依赖）；其 README 写了重建顺序 |
| 自查脚本覆盖补充材料 | 满足 | `yisheng_submission_audit.py` 在 `submission/supplement/` 里有文件时再查：七个文件名与 SI 一节一致、每份自带的 caption 与正文逐字相同、行数和文件数、属性为空、全部文本里无姓名、单位、邮箱、本地路径、会话号；加 `--rerun-esm7` 会解压 ESM_7 重跑（约 1 分钟）。我用改坏的副本（加创作者属性、加邮箱、改 caption）验证过它会报错。注意：它不扫描措辞是否越过论文已有的 “谁做了什么”，那一项靠上面一行的人工对照 |

## 9 需要 Qu 回答或决定的事

Qu 2026-10-01 13:49 和 14:10 已答，已填入题名页和 cover letter（`yisheng_make_submission_files.py` 顶部）：

1. 通讯作者 Yusen Wu，邮箱 wu_yusen825@icloud.com；Weiyi Qu 的邮箱 202520101018@bfsu.edu.cn（Qu 答 “对”）。
2. ORCID：两位都没有（N/A）。
3. 竞争利益：无；两位都不是 *Morphology* 编委（Qu：“都不是”）；基金：无。
4. 再用：本稿内容未曾以学位论文、会议论文或预印本发表过（Qu：“否”），cover letter 已写 “re-uses no text, tables or figures …”。
5. 论文 §3.1 “We visually checked … 104 of them”：Qu 选 B，两位作者也逐页看了扫描，**保持原样**（不改成 Codex 协助）。
6. 作者贡献：Qu 原话「Qu参与编码，文献综述；其他都是Wu完成（先说Wu）」，又要求 “按文献主要做的具体工作分配稍微详细一些”。我按 CRediT 写成：“Yusen Wu: conceptualization, methodology, data curation, software, formal analysis, investigation, visualization, writing – original draft, writing – review and editing. Weiyi Qu: investigation (coding) and literature review.” Qu 14:16 确认 “对”。
7. 补充材料的许可：作者贡献用 CC BY 4.0、代码用 MIT，第三方各列保留原条款（第 7 节末行）是否同意；Baxter–Sagart 构拟串是保留还是删去：Qu 14:16：同意许可，Baxter–Sagart 两列保留。

可选或知悉（7–12）：

7. 补充材料之外，是否要把数据另存到 Zenodo 或 OSF 获得 DOI（指南 “strongly encouraged”，但不是必须；若要，在录用后补一句并加一条 DataCite 格式的参考文献；匿名副本里不放第 8 节说的那份原表）。
8. 是否推荐审稿人（可选，需机构邮箱或主页）。
9. 用 Word 打开 `Manuscript_anonymised.docx`，翻一遍表格和图 1（我只能用 LibreOffice 看，三线表在 Word 里应当一样，但没法保证）。
10. 补充材料文件里 “作者栏写 Withheld” 的做法（第 8 节）和 ESM_4 里的完整偏离记录（第 8 节）是否接受。
11. 匿名稿里不放 Funding、Competing interests、Ethics、Author contributions，只留 Data availability（第 4 节）：这是按 Snapp 双盲页办的，万一编辑部要求放回稿件，第 4 节末行有办法。
12. 期刊的 SSCI 身份仍未核实、快审期刊的取舍仍由 Qu 定（见 `v7_work/journals/`），这不是排版问题，但决定投不投 *Morphology*。

没有做的事，按 Qu 04:08 的指示：评审 S1（组内相关率）和 S3（反方向偏差情景）没有并入正文，v10 的数字与 v9 相同；S3 的反方向情景只在补充材料 ESM_6、ESM_7 里。

## 10 在 Snapp 里的填写顺序（给 Qu）

1. 上传 `Manuscript_anonymised.docx`（一个文件，含全文、表和图）。不要预先填字段；上传后核对系统抽取的标题、摘要。
2. 在界面里填：作者与单位、通讯作者及邮箱、ORCID、作者贡献、竞争利益、基金（无）；数据可用性选 “Included in the paper or Supplementary Information”，粘贴稿件里的 Data availability 一段；伦理选 “不适用”。这些内容的英文底稿都在 `Title_page.docx`。
3. 上传补充材料 ESM_1–7（`submission/supplement/`），不要改文件、不要重命名；每份在界面里按 “Online Resource n” 加 caption（caption 在匿名稿 “Supplementary Information” 一节，也在每份文件开头）。
4. 图：嵌在稿件里即可；系统若要求，再上传 `Fig1.eps` 或 `Fig1.png`。
5. cover letter：用 `Cover_letter.docx` 的正文，补全日期和署名后上传或粘贴。

## 11 补充材料里仍待定的两处（数据线程提出，2026-10-01 14:10）

- **Baxter–Sagart 构拟字符串**：ESM_2 `pairs` 和 ESM_7 `pairs.csv` 的 `oc_bs2014`、`head_oc_bs2014` 两列带有构拟字符串（cddb 仓库 GPL-3.0，数据本身和官方 PDF 扉页没写条款）。A 保留（引用 Baxter 和 Sagart 2014，写明来源）；B 删这两列、只留派生类别（要改 ESM_2、ESM_7、ESM_1，再核一轮）。我倾向 A：审稿人要核上古音读法，来源公开且已引用；Qu 14:16 定：保留（A）。
- **Apache-2.0 §4**：说文数据（Apache-2.0）要求随附许可证文本；数据线程建议 ESM_7 加 `LICENSE-Apache-2.0.txt` 和 `NOTICE.txt`（67 个文件变 69 个）。我同意；数据线程 14:22 已加（`LICENSE-Apache-2.0.txt` 是仓库原文逐字节复制，`NOTICE.txt` 写明来源、提交和改动），我已重核 ESM_7（69 个文件，249/0）并把审计脚本改为 69。ESM_5 的提示、ESM_2/3 的工作表同样含说文释义，只在 ESM_1 §8 和 ESM_5 README 写了项目名、许可和网址，没另附许可文本；不再另改（边际收益小），需要时可把两个许可文件也放进 ESM_5。
- ESM_4 第 7 节 09-30 18:37 条里有 “how items on which the two authors' judgments differed were settled … is not documented”：是原计划修订记录的译文，保持原样，不删（删了就不再是逐字翻译）。分析层级名 `author_adjudicated` 不改。
