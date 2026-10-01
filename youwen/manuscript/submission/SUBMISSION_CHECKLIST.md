# Morphology 投稿核对表（v10）

日期：2026-10-01。依据：Qu 2026-10-01 04:08 随消息发来的两份 PDF（Morphology 的 *Submission guidelines*，Springer Nature 的 *Submit faster on Snapp*）。对象：本目录下的投稿文件和 `youwen/manuscript/yisheng_paper_v10*.md`。

状态只有四种：**满足**（做了，且有检查依据）、**不适用**、**需 Qu**（只有 Qu 能给或能定）、**待补充材料**（等数据线程交付 ESM_1–7 后再核）。机器核对的项目由 `youwen/scripts/yisheng_submission_audit.py` 执行，输出存在 [`audit_v10_output.txt`](audit_v10_output.txt)；括号里的名称是脚本里的检查项。Word 里的实际显示我这里无法看到（只用 LibreOffice 渲染逐页看过），见最后一节第 7 项。

## 1 要上传什么

| 要求（指南原文大意） | 状态 | 说明 |
|---|---|---|
| 稿件用 Word（.docx），正文、图、表放在同一个可编辑文件里（Source Files；Snapp：single editable file） | 满足 | `Manuscript_anonymised.docx`：12 个 Word 表格，图 1 嵌入，页码为自动页码，无域代码、尾注、批注和修订痕迹 |
| 图单独提供时，矢量用 EPS、半色调用 TIFF，文件名为 “Fig” + 编号（Fig1.eps） | 满足 | `Fig1.eps`（字体已嵌入）、`Fig1.tif`、`Fig1.png`；嵌入稿件的是 PNG |
| 双盲：作者信息和声明在系统界面里填，不放在稿件里或单独的题名页里 | 满足（需 Qu 在界面里填） | 匿名稿不含任何作者信息；`Title_page.docx` 不上传，仅作为在界面里逐项填写的底稿 |
| 先上传稿件，不要预先填字段；上传后核对系统自动抽取的标题、摘要和声明（Snapp） | 需 Qu | 上传后核对一次抽取结果 |
| 补充材料：见第 8 节 | 待补充材料 | |
| cover letter | 满足（有占位） | `Cover_letter.docx`；日期、署名、“是否再用过材料”待 Qu |

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
| 明确标出一位通讯作者及其可用邮箱（Snapp：一位 responsible corresponding author） | 需 Qu | 已向 Qu 询问，未回；题名页留占位 |
| 两位作者的 ORCID（有则填） | 需 Qu | 可不填 |
| 致谢 | 满足 | “None.”（无基金、无致谢，Qu 2026-09-30 13:58） |
| 作者贡献声明（必须在界面里填，只有界面里的会进入发表版） | 需 Qu | 已向 Qu 询问，未回；格式可用自由文本或 CRediT |
| 竞争利益声明（必须在界面里填）；编委成员须自行声明 | 需 Qu 确认一句 | 内容为 “no competing interests”（Qu 2026-09-30 13:58）；还需 Qu 确认两位作者都不是 *Morphology* 编委 |
| 基金信息（界面里填） | 满足 | 无基金：“The authors did not receive support from any organization for the submitted work.” |
| 试验注册号 | 不适用 | 非临床试验 |

## 4 Statements and Declarations（匿名稿里有，标题与指南一致）

| 要求 | 状态 | 说明 |
|---|---|---|
| Funding、Competing interests、Ethics approval and consent、Data availability 各有声明 | 满足 | 稿件末尾 “Statements and Declarations”（statements in the manuscript）；另有 “Coding” 一段说明两位作者做了什么，措辞沿用 v9 |
| 伦理、同意、动物 | 不适用 | “Not applicable. The study analyses historical texts and involves no human participants or animals.” |
| 数据可用性声明：说清数据在哪里、怎么取；每个数据集写明标题、仓库名、持久标识符（如 DOI）；不公开的要解释 | 满足（可选增强见第 9 节） | 属于 Snapp 页列的第三种写法 “Included in the paper or Supplementary Information”：数据、编码、材料、结果表和代码都作为 Online Resource 1–7；源文本与数据库按 §3 引用。尚无 DOI |
| 代码可用性 | 满足 | 并入数据声明（Online Resource 7） |

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
| 第三方数据与软件的使用许可 | 待补充材料 | *Shuōwén* 数据（shuowenjiezi，Apache-2.0）已在正文写明；ESM_2 里再分发的中古音（tshet-uinh）和上古音（cddb/Baxter–Sagart）数据的许可条款，请数据线程在 ESM_1 里注明 |

## 8 补充材料（Supplementary Information）

数据线程建 `submission/supplement/`，临时清单是 ESM_1–7（2026-10-01 04:30 经协调者转来）；正文已按该清单引用，caption 的数字已对文件核过。

| 要求 | 状态 | 说明 |
|---|---|---|
| 文件按 ESM_n.ext 连号命名；文字用 PDF，表格用 xlsx/csv，多文件打成 zip；每份附一句简明 caption | 满足（清单）/ 待补充材料（文件） | ESM_1.pdf、ESM_2.xlsx、ESM_3.xlsx、ESM_4.pdf、ESM_5.zip、ESM_6.xlsx、ESM_7.zip |
| 正文里写明引用，格式 “Online Resource n”；正文里放每份的 caption | 满足 | §3.1、§3.3–3.6 引用，首次引用顺序 1–7；“Supplementary Information” 一节列出 7 条 caption（Online Resources cited in order；each listed with file name and caption） |
| 补充材料原样发布，不转换、不编辑 | 待补充材料 | 文件交付前须定稿 |
| 每个文件里写明文章题目、刊名、作者姓名、通讯作者单位和邮箱 | 需 Qu / 待补充材料 | 与双盲相冲突：送审版本的补充文件里只写题目和刊名，作者栏写 “withheld”，录用后再补作者信息。这一做法请 Qu 知悉 |
| 提供数据给审稿人时，数据里的作者信息也应匿名（Research data and peer review） | 待补充材料 | 数据线程已发现作者核验表的文件属性里有作者本名，包里改用重建的数据 |

## 9 需要 Qu 回答或决定的事

1. 通讯作者是谁，邮箱是什么（界面里要填，题名页和 cover letter 的占位都要换）。
2. 两位作者的 ORCID（有就给，没有可不填）。
3. 作者贡献：谁整理数据与分析、谁写初稿；或回 “两人共同完成”。
4. 这篇稿子的内容是否以学位论文、会议论文等形式发表过；两位是否都不是 *Morphology* 编委。
5. 补充材料之外，是否要把数据另存到 Zenodo 或 OSF 获得 DOI（指南 “strongly encouraged”，但不是必须；若要，在录用后补一句并加一条 DataCite 格式的参考文献）。
6. 是否推荐审稿人（可选，需机构邮箱或主页）。
7. 用 Word 打开 `Manuscript_anonymised.docx`，翻一遍表格和图 1（我只能用 LibreOffice 看，三线表在 Word 里应当一样，但没法保证）。
8. 补充材料文件里 “作者栏写 withheld” 的做法是否接受（第 8 节）。
9. 期刊的 SSCI 身份仍未核实、快审期刊的取舍仍由 Qu 定（见 `v7_work/journals/`），这不是排版问题，但决定投不投 *Morphology*。

没有做的事，按 Qu 04:08 的指示：评审 S1（组内相关率）和 S3（反方向偏差情景）没有并入正文，v10 的数字与 v9 相同。

## 10 在 Snapp 里的填写顺序（给 Qu）

1. 上传 `Manuscript_anonymised.docx`（一个文件，含全文、表和图）。不要预先填字段；上传后核对系统抽取的标题、摘要。
2. 在界面里填：作者与单位、通讯作者及邮箱、ORCID、作者贡献、竞争利益、基金（无）；数据可用性选 “Included in the paper or Supplementary Information”，粘贴稿件里的 Data availability 一段；伦理选 “不适用”。这些内容的英文底稿都在 `Title_page.docx`。
3. 上传补充材料 ESM_1–7（数据线程交付后）。
4. 图：嵌在稿件里即可；系统若要求，再上传 `Fig1.eps` 或 `Fig1.png`。
5. cover letter：用 `Cover_letter.docx` 的正文，补全日期和署名后上传或粘贴。
