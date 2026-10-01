# 项目协作日志（Codex / Claude）

这是存放在 GitHub 项目分支上的**共享记录**，用于让不同助手看到彼此已完成的修改和会影响后续工作的决定。它不是论文正文，也不替代各数据文件、`youwen/youwen_criteria.md` 或 `youwen/literature_review_access_log.md`。

## 读写约定

1. **修改前**：同步当前工作分支；读 `AGENTS.md`、`CLAUDE.md`、`README.md` 和本日志最近条目；再核实要修改的权威文件。私有记忆只作为定位线索。
2. **修改后**：在同一次提交中按时间顺序向本文件末尾追加条目，记录日期、执行者、目的、变更文件、验证结果，以及当前论文版本或数据口径有无变化。未验证的事项明确标成待核实。
3. **发生冲突时**：以用户最新要求和已核实的当前文件为准；查 Git 提交记录确定变更来源，然后修正相应的共享说明与私有记忆。不要默默沿用旧条目。

## 2026-09-26 · Codex · 建立跨助手同步入口

- **基线**：在 PR [#2](https://github.com/WuYusen825/Morphology/pull/2) 的 `claude/library-to-github-8wdy00` 分支上核对项目；开始时的提交为 `390296764a4e6d35e0da7a77a7f8370371e741c1`。该分支汇集论文、文献综述、数据和原书页图；默认分支尚未包含全部项目材料。
- **项目内容**：研究《说文解字》的“亦声”标注是否对应上古汉语派生关系。当前英文正文为 `youwen/manuscript/yisheng_paper_v5.md`，目标期刊与目录见 `README.md`。v5 分析 212 个亦声字头及同声符的 953 个普通形声字；主要结果支持同音及去声 `*-s` 关系，也支持更高的语义相关性，但不支持把标注概括成一般词缀派生。大小徐本对照为 140 条共有、62 条仅大徐、10 条未定。上述口径应以现行正文和结果文件再次核实后用于改稿。
- **重要边界**：κ = 0.773 是两次 LLM 编码的一致度，不是人工编码者信度；王筠将亦声分为三种，不能说他把亦声直接等同于分别文。改稿与数据重跑规则见 `AGENTS.md`。旧稿 v1–v4 保留对照，后续实质改稿另存 v6。
- **本次变更**：新增本日志及 `CLAUDE.md`，在 `AGENTS.md` 和 `README.md` 加入修改前读取、修改后记录的入口；将先前核对的 v5 参考文献 DOI 清单复制到 `youwen/doi_audit_v5.md`，让两个助手可读。未修改正文、数据或统计脚本；当前权威正文仍为 v5。
- **验证**：以 PR #2 当前分支的 `README.md`、`AGENTS.md`、v5 正文、`youwen/youwen_criteria.md` 和文献目录核对了上述项目概况；本次提交前再次检查文件链接、日志入口和工作区差异。

## 2026-09-27 · Codex · v6 正文、作者编码与大徐本核对

- **当前权威版本**：新建 `youwen/manuscript/yisheng_paper_v6.md` 和同名 DOCX；v5 保留作历史稿，不作为后续改稿基底。同步更新 `AGENTS.md`、`README.md` 和 `youwen/youwen_criteria.md` 的版本入口与编码口径。没有修改 CSV、XLSX、统计脚本或模型结果。
- **作者编码事实**：两位作者各自在看不到“亦声／普通”标签的题单上独立编码 100 对本义关系，核对前 100 项一致，且与先前 LLM 值相同；两人还逐对复核 63＋133 个中古同音对的 L／F／C／U／X 类型。公开最终值沿用历史文件 `youwen/blind_coding_sheet_llm_coded.xlsx`，该文件名及说明页保留机器初编来源；两份作者独立原始表未留存，不把旧 κ = 0.773 当成人工编码信度。过程与文件边界见 `youwen/manuscript/coding_provenance_v6.md`。
- **正文改动**：§3 和结果部分直接写作者实际完成的盲编、核对与复核，删去把 LLM 当作最终编码者的叙述；§3.4 以声符聚类的 logistic GEE 为主要模型，子集使用 Fisher 精确检验；解释范围调整为同音、语义相关及部分去声 `*-s` 关系，保留其他词缀与交替不支持的结果。文末 AI 使用声明仍如实披露初期机器辅助的提取、大小徐校勘、脚本、探索性编码及写作。
- **大徐本核对**：逐页查看本地早稻田藏陈昌治刻本扫描，对正文逐字引用的核心说解、析形句及论证例字记下 PDF 卷号与页码，见 `youwen/manuscript/daxu_source_audit_v6.md`。这是直接检查该扫描，不是亲自翻检中华书局 1963 年纸本；尚未把分析集全部 212 字头逐页校勘。柵、恇、傾、𨻺、䫇的陈本对应页此轮尚未逐字定位；正文和记录均不得称这些条目已过印本核查。小徐本 140／62／10 的现有口径不变，扫描读法原仅抽查，不能冒称两位作者完整重核。
- **验证**：核查 v6 的正文词数、段落、表格与关键数字均沿用现有分析输出；DOCX 用 v5 版式生成，并在 Word 与 22 页渲染预览中检查，汉字显示正常。初次预览缺汉字的原因是预览器临时 HOME 未加载用户字体；补充字体配置后重渲染已恢复。提交前再做一次文件差异与远端状态核对。
- **给 Claude 的交接通知**：请从 v6 继续，不要把旧 LLM 编码 κ 写成两位作者的 κ，也不要将历史 `*_llm_coded.xlsx` 改名为人工原始表。若继续核对大徐本，先补完上述未定位例字和全部 212 字头的逐页记录，再修改正文的证据范围；若增补模型或数据，先核实数据和脚本，再同步正文、README 与本日志。`youwen/manuscript/yisheng_paper_v5.docx` 当前另有用户未提交的署名改动，本次提交不得包含。

## 2026-09-27 · Codex · v6 大徐补核与版本差异

- **补核结果**：在本地早稻田陈昌治刻本扫描中逐字找到柵（0004，17）、傾（0005，9）、䫇（0005，50）、恇（0006，51），已补入 `youwen/manuscript/daxu_source_audit_v6.md`。恇条刻本写“从心匡匡亦聲”，与电子文本的标点或析形断句须分开处理。
- **待核版本差异**：电子文本有 `𨻺`（U+28EFA）“仄也。从𨸏从頃，頃亦聲”，但陈本扫描 0008，27 的隓及其篆文之后直接接陊，在预期位置未见该条。此观察只针对已查的这一页；应与另一印本复核，不据此断言所有大徐版本都缺该字。v6 §6 与核对表已注明。212 条总体仍按既有电子文本定义，未作重算，也未宣称全体已过印本校勘。
- **给 Claude 的更新**：前一条日志列出的五个未定位字已解决四个；后续先查 `𨻺` 的版本依据，再继续全体 212 字头的印本校勘。当前正文仍为 v6；本次同步更新同名 DOCX，未碰用户在 v5 DOCX 中的未提交改动。

## 2026-09-27 · Codex · v6 按已完成的定点抽核收束

- **用户决定与当前权威**：用户明确要求停止继续核查大徐本，只依据已有记录，在正文按抽样检查表述，完成 v6 并上传 GitHub。上一条日志建议继续全体 212 条校勘的待办因此撤销；不要自行继续扫描。当前权威正文仍是 `youwen/manuscript/yisheng_paper_v6.md` 和同名 DOCX。
- **已完成的核查范围**：合并四份本轮已保存的目验记录，去重并与分析集编号核对后，共有 104／212 条。属于按进度与论证需要的定点抽核，并非随机抽样或全体逐字校勘。逐条编号、字头、陈本扫描 PDF 页码、已存片段和数字文本见 `youwen/manuscript/daxu_spotcheck_v6.csv`；关键例字见 `youwen/manuscript/daxu_source_audit_v6.md`。剩余 108 条本轮未核。
- **发现与正文处理**：䢈（陈本扫描 0003，80）首句见 `日月合宿爲辰`，电子文本作 `日月合宿从辰`，后续 `辰亦聲` 公式一致。此前发现的 𨻺 在陈本扫描预期位置未见，仍只作为这个印本的待解版本差异。v6 §3.1、§6 及数据可用性段落已限定抽核范围；现有统计、数据与脚本不变。
- **Word 字形处理**：DOCX 预览对个别扩展汉字显示方框，英文正文因此以 U+4888、U+28EFA、U+20501 码位指代；抽核 CSV 与中文记录仍保留原字头 䢈、𨻺、𠔁，方便按字检索。此处理不改条目身份或统计。
- **给 Claude 的约定位置通知**：请按用户最新指示使用本条范围口径，不沿用上条“继续核完 212 条”的待办；仅在用户另行要求时扩展版本校勘。不要把 104 条写成随机抽样、把 𨻺 推广为所有版本缺字，或把旧 LLM κ = 0.773 写成作者间信度。若未来实质改稿，依 `AGENTS.md` 另存 v7。用户在 v5 DOCX 的未提交改动不属于本次提交。

## 2026-09-28 · Claude · 缺失参考文献清单与 Karlgren 1934 扫描

- **起因**：Qu 要求把 v6 参考文献里还没有 PDF 的条目下载到本仓库。Qu 本地已有 17 篇（编号 01、02、06、09、12、13、15、16、21、22、23、24、28、30、36、39、41，按 v6 参考文献顺序编号）。
- **本次变更**：新增 `youwen/manuscript/missing_references.csv`，列出其余 24 条，分“期刊”（含报纸文章和硕士论文，给链接）和“书”（含书中章节和古籍，给书名）；新增 `youwen/sources/karlgren_word_families_BMFEA05_archive_Bulletin477728.pdf`；`README.md` 原书扫描表补一行。未修改正文、数据或脚本；当前权威正文仍为 v6。
- **Karlgren 1934 来源**：archive.org 条目 `Bulletin477728`，由远东古物博物馆（Statens museer för världskultur）自行上传，许可为 CC0 1.0。原 PDF 252 页，元数据 Producer 为 ilovepdf.com，修改日期 2017-04-02；截出书名页、目录和正文 PDF 第 11–122 页（原书第 9–120 页），共 114 页。目录确认 Karlgren 一文起于第 9 页、下一篇 Waley 起于第 121 页，与 v6 所列页码一致。**待核**：该卷书名页印“STOCKHOLM 1933”，v6 作 1934；只下载未读，阅读程度不变。
- **未能取得**：Karlgren 以外的期刊条目（JSTOR、知网等）要北外图书馆登录；本云端会话没有内置浏览器，无法让 Qu 登录。另外本仓库是公开仓库，出版社或数据库的受版权保护 PDF 不应提交进来，需 Qu 决定放在哪里。沈兼士 1933 所在论文集有台大图书馆扫描（Wikimedia Commons），本环境下载被限流。条目 37（四部丛刊本《系传》）已在 Release「说文解字」，清单已注明不缺。
- **验证**：CSV 共 24 行，编号与 v6 参考文献顺序核对无误；截出的 PDF 逐页抽查首、末页文字层，确认起止正确。

## 2026-09-28 · Codex · 参考文献 PDF／Markdown 整理与 Literature Release

- **目的与位置**：按用户要求整理仓库外的本地 `论文/参考文献PDF/` 与 `论文/参考文献MD/`，并上传到本仓库的 [Literature Release](https://github.com/WuYusen825/Morphology/releases/tag/literature)（tag `literature`）。这些参考文献文件及转换脚本留在本地，没有加入本 Git 分支；Release 的 [上传清单](https://github.com/WuYusen825/Morphology/releases/download/literature/literature-upload-manifest.json) 列出原相对路径、远端附件名、字节数和 SHA-256。
- **PDF 与 MD**：44 份原有 PDF 改为 `Author_Date_Title.pdf`，各部分内部用空格，并清理可选的 PDF Info／XMP 元数据；原名、新名及校验值留在本地 `论文/参考文献PDF/重命名与元数据清理清单.json`。这 44 份各有一份分页 Markdown；另有两组截图整理成的文章 Markdown（Pulleyblank 2000／1973）和一份转换说明，所以共 47 份 MD。《同源字典》和早稻田《说文解字》十册按用户要求未做 OCR，未转写的扫描页仅保留原 PDF 页链接；其余 OCR 文本尚未逐字校对。
- **两份截图 PDF**：将 `MORPHOLOGY IN OLD CHINESE` 的 26 张截图（包含后来补入的阅读器第 5 页）和 `Some New Hypothese` 的 15 张截图分别裁去浏览器界面、按页序合成图像 PDF，命名为 `Pulleyblank_2000_Morphology in Old Chinese.pdf` 和 `Pulleyblank_1973_Some New Hypotheses Concerning Word Families in Chinese.pdf`。原截图保留，生成脚本在本地 `论文/参考文献MD/make_screenshot_pdfs.py`；对应 Markdown 提供 OCR 文字，图像 PDF 本身没有文字层。
- **验证与给 Claude 的通知**：Release 现有 46 份 PDF、47 份 MD 和 1 份 JSON 清单，共 94 个附件；远端附件的名称、显示标签、字节数与 SHA-256 均与本地清单一致。两份新 PDF 均核对页数、元数据与全部页面缩略图；第 5 页顺序正确。使用任何文献作为论文依据前，仍须按 `AGENTS.md` 核实来源与原页；这次文件整理不等于已完成全文校对或来源审查。本次未更改仓库内论文、数据、文献阅读程度或统计口径，当前权威正文仍是 v6。工作区中用户未提交的 `youwen/manuscript/yisheng_paper_v5.docx` 改动不属于本次提交。


## 2026-09-28 · Codex · 期刊 Discussion 精读与理论推理比较

- **用户要求**：精读本地参考文献的讨论部分，以 Markdown 为主、必要时回查 PDF，重点学习期刊 research articles 如何从现象推进理论、划定严谨与推测边界、表达贡献。
- **已完成**：新增 `youwen/discussion_close_reading.md` 和 `youwen/discussion_reading_index.md`，以 14 篇期刊研究／论证文章为主体，另列 2 篇特殊体裁期刊文章和 3 篇对照材料。逐篇阅读范围与来源定位写入索引，同时在 `youwen/literature_review_access_log.md` 第 10 节追加实际阅读记录。研究文章、演讲修订、概述、综述、导论和会议论文没有混记；局部精读不记为整部通读。
- **内容**：比较功能重分类、历史多来源模型、派生方向的竞争解释、词族联合预测、结构诊断、音义相关到机制的推断、文字证据的形成层次；记录语言表达和可复用的讨论自检问题。对 v6 的应用为论证建议，不是已经验证或采用的新理论结论；不能将发表身份当作每个推论都正确或已知实际录用原因。
- **验证**：根据本地原文复核关键结论、具体比较及文献体裁；双栏错序处回查 Monaghan PDF 第 5–11 页及李宁、郭抒远第 1–2 页。检查了笔记的 19 处来源引用、21 个定义链接及本地目标文件，索引的 Release 链接来自现有上传清单。本轮没有重做远端参考文献附件审计，也没有逐字校对全部 OCR。
- **当前权威**：仍为 `youwen/manuscript/yisheng_paper_v6.md` 与同名 DOCX；未改正文、数据、编码、统计或原典抽核范围。用户已有的 `youwen/manuscript/yisheng_paper_v5.docx` 未提交改动继续保留，不纳入此次提交。后续若按笔记实质改稿，仍须另存 v7 并逐项核对其所需证据。

## 2026-09-28 · Codex · 单独保存 Discussion 精读总结

- 按用户“把以上总结出来的东西写进一个 md”的要求，新增 `youwen/Discussion精读总结.md`，整理上一轮六项主要认识、论文实例、对亦声研究的启发及写作自检问题，并链接完整精读笔记与原文索引。
- 本次仅整理既有阅读成果，没有新增阅读范围或修改论文、数据及统计。检查 Markdown 内容、相对链接和提交范围；现行权威稿仍为 v6，既有 v5 DOCX 改动保留。

## 2026-09-28 · Claude · 学习 Release：*Morphology* 2026 讨论精读，更新 Discussion 精读总结

- **用户要求**：在 Codex 精读 14 篇参考文献的基础上，继续精读 Release `学习` 中的 *Morphology* 论文，学习讨论怎样从数据推进到理论创新、严谨与推测的边界、语言、详略与创新类型；后又追加“怎样联系文献结论、呼应前人理论”；并说明怎样用于亦声稿，更新 `youwen/Discussion精读总结.md`。
- **合并**：先把 `claude/library-to-github-8wdy00`（Codex 当天三次提交：Literature Release 记录、讨论精读笔记与索引、单独的精读总结）合并进本分支。`PROJECT_LOG.md` 与 `youwen/literature_review_access_log.md` 两边都在末尾追加，按时间先后保留双方；访问日志中 Codex 的“第 10 节”改为第 11 节，Codex 上一条日志提到的“第 10 节”即现在的第 11 节。
- **资料**：Release `学习` 有 11 个 PDF（*Morphology* 36:11–36:21）。经 GitHub API 下载到会话临时目录，SHA-256 与 Release 所列一致；元数据确认为 Springer 正式出版 PDF；10 篇开放获取，Barbu Mititelu 等为订阅文章，只转述、短引。PDF 未提交进仓库。
- **变更文件**：新增 `youwen/discussion_close_reading_morphology2026.md`（逐篇笔记）；`youwen/Discussion精读总结.md` 改为第二版，整合两轮阅读，新增第 4 节（与文献对话的动作），第 8 节写对亦声稿的应用（期刊定位、v6 讨论诊断、v7 讨论布局与篇幅预算、逐段建议、前人主张计分表草稿、英文示范段落、严谨边界清单、未执行的可选新分析）；`youwen/discussion_reading_index.md` 增第二部分（第 20–30 条）；`youwen/literature_review_access_log.md` 增第 12 节；`README.md` 在文件表加一行，在 Release 表补 `literature`、`学习` 两行；`AGENTS.md` 的“资料来源”加一条下载与读 PDF 的做法。
- **验证**：逐篇阅读范围记入索引；总结与笔记中的英文引语逐条回到文字层核对；v6 的数字与引文取自 v6 正文，示范段落注明写入 v7 前须回到结果文件复核；新旧文件中 35 个相对链接全部存在。
- **从失败中得到的做法**：私有仓库的 `github.com/.../releases/download/...` 链接在云端会话返回 404，改用 API 附件端点（`Accept: application/octet-stream`）即可；环境无 `pdfinfo`，`pypdf` 因系统 `cryptography` 损坏报错，改用 `pip install pymupdf`。已写入 `AGENTS.md`。
- **更正**：GitHub API 显示本仓库为 private（2026-09-28 核对）；此前 Claude 条目称“本仓库是公开仓库”不准确。
- **未改动**：v6 正文与 DOCX、数据、脚本、编码、统计和大徐抽核范围均未改，当前权威稿仍为 v6。首投期刊记录仍是 *Language and Linguistics*；*Morphology* 的 SSCI 收录状态仍待 Qu 在 MJL 核实。总结第 8 节的改稿建议和可选新分析都未执行；若采用，须另存 v7，新分析须按 `AGENTS.md` 先写脚本和结果文件。

## 2026-09-29 · Codex · 整合本地与 Claude 第二版为宏观 Discussion 指导

- **用户要求**：读取 GitHub 上 Claude 精读11篇 Morphology 文献后更新的版本，以及本地原总结，生成一份新的宏观指导 Markdown。
- **版本核对**：当前本地分支 `claude/library-to-github-8wdy00` 起点为 `99be2c8`；其同名总结仍为第一版。通过 GitHub API 与定向 fetch 确认 Claude 更新在 `claude/yisheng-manuscript-an2sc4`，提交 `295732121850d594cdc720e0bd4f0ec75ae8f7a6`，包含第二版总结和 `discussion_close_reading_morphology2026.md`。完整读两版总结与新增笔记，读取另一分支的更新日志并核对规则差异。没有为了读取而合并分支或覆盖本地第一版。
- **产出**：新增 `youwen/Discussion宏观写作指导.md`，在通用写作层面整合中心问题、理论推进、诊断力、文献关系、推理边界、推测、章节篇幅、语言和贡献，附简短流程及亦声应用方向。来源采用固定提交链接。另在本地 `literature_review_access_log.md` 第11节记录本轮阅读层级；Claude 分支上的历史节号可能不同，不据数字合并覆盖记录。
- **校准**：区分叙述顺序与事前预测、零结果与反例、针对性稳健检查与排除全部伪影；不把11篇文章的共同倾向当作期刊硬性政策，不强制所有文章裁决具名理论或遵循固定篇幅、推测顺序。未把第二版的期刊收录、审稿周期、字数预算及未执行新分析转为通用要求。
- **验证和范围**：检查三份输入的版本、全部正文读取范围、新文档的来源引用和文件链接；本轮未重新审读11篇原文，不把笔记批评当作新的全文审计结论。当前论文仍为 v6，目标期刊及数据口径不变；原有 v5 DOCX 未提交改动不纳入此次提交。

## 2026-09-29 · Codex · v6 系统重构计划与关键例组复核

- **最新交付范围**：用户先要求基于两份 GitHub Discussion 精读系统重构全文，并允许在既有数据上作必要补充分析；随后明确“只需要给出修改 plan”，又允许已产出内容保留。因此本轮交付计划，不继续完成 v7，不制作新 Word 版。当前权威仍为 v6 MD／DOCX；已生成的 `yisheng_paper_v7.md` 含占位符且未经全文核数或引文／排版验证，已在文件顶部和 README 标为未完成工作稿。后续实施时继续完成 v7，不因这个文件存在而直接跳至 v8。
- **版本依据**：工作分支 `claude/library-to-github-8wdy00` 的 `bec212403026077c1334fcdb809ec353d8d5d29e`；另一份总结和11篇笔记来自 `claude/yisheng-manuscript-an2sc4` 的 `295732121850d594cdc720e0bd4f0ec75ae8f7a6`，没有合并其分支。目标期刊仍为 Language and Linguistics。
- **计划产出**：新增 `youwen/manuscript/v6_系统重构修改计划.md`，围绕“亦声所标示的词际联系如何跨越字形分化与词汇派生”提出六章方案、三节讨论、文献改写任务、旧稿迁移、必要分析与完成标准。重点是形成具体语言学解释，不把全文改成单独的证据方法论文章。
- **原文与例组**：新增 `lexical_examples_audit_v7.md`，保留原 L/F/C 编码，校准同词／分义与五个转换候选的解释力度；按段注修正儐的擯相与賓禮两义，不将后者直接接到“導也”。文献核查纠正 Qiu 仅作纯图形分析、Boltz 的加旁直接证明基词／派生方向、传统研究没有量化等过强概括；已读具体范围追加到 `youwen/literature_review_access_log.md` §12。鄒也靜2016只核官方摘要与元数据，不称阅读全文。
- **分析状态**：回查既有结果及去声两步分解；本轮无可交付的新 CMH 脚本／估计，计划中明确待执行。OC R 包含 `*-s`，旧 matched-series 合并检验不等于系列内控制；四分类表和真正的系列内比较是后续任务，不冒称已执行或全部通过。
- **文件与验证范围**：README 增加计划入口及版本状态；未改 v6、原始 CSV／XLSX、作者代码、模型输出、原综述正文或注释书目。保留已生成的 v7 部分草稿及核查记录，未完成 DOCX／PDF，因此没有相应渲染检查。检查计划链接、占位符状态、差异范围与既有数字来源。104／212 定点抽核范围不变；用户原有 v5 DOCX 未提交改动不纳入提交。
- **后续交接**：先读修改计划及例组核查，再决定是否实施正文改写。旧 README“主要结论（v6）”只是历史稿概括，相关同词、H1b、方向、传本论断应按计划修正，不能据它覆盖本轮新判断。没有新的作者编码、词源确证或历史传本定年。

## 2026-09-29 · Codex · 按用户批评重写计划：恢复解释与理论推进

- **用户纠正**：用户指出上一版重构计划不如原稿，防御性表述远多于所读论文。本轮据此修订计划的论证方向，交付仍为 plan，不继续写 v7 正文。
- **替代上一版**：重写同一 `youwen/manuscript/v6_系统重构修改计划.md`，替代 `225d6d9` 中的六章方案。保留 v6 七章框架和已有解释优势，四节讨论依次发展字形分化解释、词与词族的意义、王筠及传本实践、右文与新预期。将来源及推论核对集中至实施附表，避免把每节写成资料不能证明什么。
- **解释内容**：拟提出亦声将字形分化中保留的词汇联系写入构形分析，以同音／语义模式、傾／娶和賓系列展开其解释收益；随后形成两项后续预期。计划明确这是拟发展的解释，不新增实证结果。H1b 集合、儐义项等已核事实修正仍保留。
- **阅读与同步**：复读两份总结及相关案例笔记，重点落实第一份“严谨主要体现在连接处，而非不断使用保守措辞”和第二份从经验概括推进解释的要求；阅读日志追加 §13，未扩充原文阅读范围。README 更新计划入口与旧 v7 工作稿状态；后者是在上一版思路下生成的，后续依据当前计划从 v6 继续。
- **验证与范围**：核对计划内部章节、字数预算、来源链接、修改范围及远端分支状态。v6、未完成 v7 正文、原始数据、编码和分析输出均未改；用户既有 v5 DOCX 修改不纳入本次提交。当前权威仍为 v6。

## 2026-09-29 · Claude · 合并 PR #1 分支到 v7 工作分支

- **目的**：按 coordinator 选定的默认做法（GitHub 上传线程此前向 Qu 提出过同一方案），从默认分支 `claude/project-thread-lj0ffs`（`b3aec15`，已含 PR #2）新建 `claude/yisheng-paper-v7-ougcnb`，并把 PR #1 分支 `claude/yisheng-manuscript-an2sc4`（`2957321`）合并进来，使 v7 分支同时带有 `missing_references.csv`、Karlgren 1934 扫描、*Morphology* 2026 精读笔记与第二版 `Discussion精读总结.md`，以及 Codex 的 `Discussion宏观写作指导.md`。
- **冲突处理**：只在 `PROJECT_LOG.md` 与 `youwen/literature_review_access_log.md` 冲突，两边都是末尾追加。按日期保留双方：本日志中 Claude 2026-09-28 条目在前、Codex 2026-09-29 条目在后；访问日志中 Codex 2026-09-29 一节由“第 11 节”改为第 13 节（Codex 在上方日志条目里说的“第11节”即现在的第 13 节）。其余文件自动合并，未改内容。
- **再合并 Codex 计划**：随后又把 `claude/library-to-github-8wdy00`（`4f24f70`，PR #2 合并后 Codex 新增的两次提交：`v6_系统重构修改计划.md`、`lexical_examples_audit_v7.md` 和未完成的 `yisheng_paper_v7.md` 工作稿）合并进本分支。冲突仍只在两份日志末尾：本日志按时间把 Codex 两条 2026-09-29 条目排在本条之前；访问日志中 Codex 的“§12”“§13”依次改为第 14、15 节（上方 Codex 条目提到的“§12”即现第 14 节，“§13”即现第 15 节）。
- **未改动**：正文、数据、脚本、编码和统计口径不变；当前权威稿在本次合并时仍为 v6。

## 2026-09-30 · Claude · v7 定稿（主稿、文献、评审三线程分工）

- **用户要求**：Qu 2026-09-29 16:05 在“重写论文 v7”线程提出以下要求：
  - 依据两份最新的 Discussion 精读总结（`Discussion精读总结.md` 第二版、`Discussion宏观写作指导.md`）优化计划，写出新稿；Codex 的 `v6_系统重构修改计划.md` 只作参考。
  - 写完后，按总结和学术严谨性，与 *Morphology* 的论文比较水平，没达到就继续改。
  - 同步编码的写法。
  - 优先依据 Release `literature` 的 Markdown 更新文献综述，文中引用不写页码。
  - Qu 另说：“可以用多个thread分工”；目标期刊改为 *Morphology*，以 Release `学习` 的 11 篇为参照；编码“直接用LLM编码的两份原始表”（2026-09-30）。
- **分工**：
  - 主稿线程写计划、全文、编码段，负责全部提交。
  - 文献线程按 Markdown 重写 §2.1–2.3 与参考文献，并记录读取程度。
  - 评审线程对照 11 篇审了四轮：v6 与计划、初稿 1、2、3。第四轮认为初稿 3 可以定稿。
  - 另两个线程不推送；它们的产出由本次提交并入。
- **产出（`youwen/manuscript/`）**：
  - `yisheng_paper_v7.md` 与 `.docx`：初稿 3，加评审第四轮可选的 T1。正文按拉丁字母词计 6,998 词，另有汉字 269 个；摘要 240 词；表 7 张；参考文献 37 条。
  - `yisheng_paper_v7_numbers.md`：正文每个数字的出处。
  - `v7_evaluation.md`：对照两份总结与 11 篇的评价，以及待 Qu 决定的事。
  - `v7_plan.md`：计划。
  - `v7_review/`：评审线程的四份报告与复核脚本。
  - Codex 写到一半的 `yisheng_paper_v7.md` 改名为 `yisheng_paper_v7_codex_partial.md`，内容未动。
- **v7 相对 v6 的主要改动**：
  - 挂靠一般问题：没有显性形态时怎样诊断派生，本土分类能否作证据。
  - 表 1 列四种解释及其预测，其中意义先行一说依李國英公平构造。
  - H1c 分两步，方向改报条件 OR，并给基线（75% 对 61%）。
  - 表 7 做组合检验，写明梯度：读音效应主要由仅大徐的标注和声训条目承担；核心 92 对里语义对比仍大，同音对比变弱。
  - 结论改为：标注是词汇相关性的证据，这种相关在同音与 \*-s 中最密，不是有方向的派生标记；意义先行与同词解释现有样本分不开。
  - §5.3 写相关性、形式关系、方向三者分开诊断。
  - 示例改用两本共有的 琀、珥、憙；喪 一例写明只有大徐作亦声。
  - 编码段按 Qu 的决定改写（见 `youwen_criteria.md` §9）。
- **新增分析**：只写 `scripts/yisheng_v7_checks.py` → `yisheng_models_v7_checks.csv`，共 96 行，口径见 `youwen_criteria.md` §9。
  - 包括：四分剖面、声符内 MH、方向、组合检验、段注计数、相关对内的分组比较（12c）、H4 与段注删标的双侧 p（第 15 节）、盲编样本的抽样框（第 16 节）。
  - 第 16 节查出 50 个普通对中有 4 个不在 172 个声符的比较组内。正式的 H2 不变；v7 §3.3 加一句说明，§4.3 涉及读音的比较改用 79 对。
  - 没有改动任何既有数据文件、编码表或正式计数。
- **同步更新**：
  - `literature_review.md` 改为 v0.3，即 v7 的 §2，附书目编号。
  - `bibliography.md` 按文献线程核对逐条更正；仍带 † 的只剩 A11、E4–E6。
  - `literature_review_access_log.md` 增第 16 节。
  - `youwen_criteria.md` 增第 9 节。
  - README 更新当前稿、目标期刊、主要结论（v7）、结果文件表与重跑命令；AGENTS.md 更新当前稿、数字来源和编码写法。
- **验证**：
  - 评审线程四轮逐项核对正文数字，全部与结果文件一致；T1 的数字另由脚本第 16 节复算，与评审一致。
  - 改脚本后逐次对比 CSV，已有各行不变；只有第 12c 节插在中间，使其后各行顺延两行，出处表已按新行号改过。
  - 正文 37 条参考文献与文内引用互相对上。
  - 检索全文，没有违反 AGENTS.md 所列的写法边界。
  - DOCX 由 pandoc 3.9 按 v6 的样式生成，用 python-docx 核对：7 张表，25 个标题，𠔁、𨻺、䢈 都在。
- **从失败中得到的做法**：
  - 云端会话的 LibreOffice 连 .txt 都打不开，改用 python-docx 检查 DOCX。
  - 在检验脚本中间插新节会让已引用的行号顺延，以后新节一律加在末尾。
  - 书目批量替换的脚本先断言每处替换的次数、最后一次写盘，失败时文件不受影响。
- **权威版本**：当前稿由 v6 改为 v7；目标期刊记为 *Morphology*，SSCI 收录待 Qu 核实。
- **未改动**：
  - Qu 的 v5 DOCX 未提交改动；
  - 大徐定点抽核的范围（104/212，已按 Qu 的决定停止）；
  - 两份编码表与 κ 输出。

## 2026-09-30 · Claude · 记录扩大盲编的决定

- **决定**：Qu 2026-09-30 06:23 在评审线程的决定卡上选择投稿前扩大盲编，用来区分“意义先行”与“同词或最小派生”两种解释。
- **执行方式**：新的数据线程按评审写的方案执行：其余亦声对全部编码，普通对随机抽 500 个，两次独立盲编，编码前写定分析计划。编码表和结果文件走数据线程自己的分支和 PR，不进本分支。
- **本次变更**：`youwen/manuscript/v7_evaluation.md` 第 0、6 节和 README“论文还缺什么”改写为“已决定，进行中”。
- **后续**：结果回来后修订 v7 的 §3.3、§4.3、表 5、§5.2、§6 和摘要，另存或在本 PR 上修订前先读本日志，修订稿再交评审线程复核。
- **未改动**：论文正文、数据和统计口径都没有改。

## 2026-09-30 · Claude（扩大盲编数据线程）· 扩大盲编：编码前写定抽样与分析计划

- **用户决定**：Qu 在 v7 评审线程的决策卡上选“扩大盲编”（2026-09-30 06:23）。方案来自评审线程 `v7_work/review/extended_coding_spec.md`，由协调线程交给本线程。本线程在分支 `claude/youwen-extended-blind-coding-ynngrw` 上工作，不动 v7 分支和论文稿。
- **本次提交（编码前）**：新增 `youwen/ext_coding/`：
  - `analysis_plan.md`：分析计划，含抽样、编码流程、主检验与判读规则、次要检验、已知偏差；
  - `ext_sample.py` 与其输出 `ext_items_key.csv`、`prompts/`（14 批完整提示）；
  - `ext_analysis.py`：编码后运行的分析脚本，已用随机编码空跑，空跑输出未入库。
  - `youwen_criteria.md` 追加 §10。
- **核对**：
  - 框与 v7 相同（172 个声符，212 / 953）。框内已编亦声 35、普通 55，评审方案写的是 56；未编亦声 177（142 个有中古音），未编普通 898（803 个有中古音），评审方案写的是 897。
  - 普通组抽 500 个，但改为按有无上古构拟分层的等概率抽样，理由见计划 §2.3。
- **未改动**：`yisheng_dataset.csv`、`yisheng_models*.csv`、`blind_coding_sheet*.xlsx`、`yisheng_claude_codes.csv` 及论文各稿。权威论文版本不变（仍以 v7 分支 / PR #3 为准）。

## 2026-09-30 · Claude（扩大盲编数据线程）· 扩大盲编：两次盲编完成，分析结果

- **编码**：14 批全部收回，提示与 `prompts/` 逐字核对相同，回答全部可解析。原始回答和来源记录见 `youwen/ext_coding/raw/`。
  - 两个代理实例多交了一份回答（第一次盲编第 3、6 批），按计划 §7 只用第一份。
- **分析**：`ext_analysis.py` 正式运行，新增以下文件：
  - `blind_coding_extended_pass1.xlsx`、`blind_coding_extended_pass2.xlsx`（两次盲编表）；
  - `ext_codes_long.csv`；
  - `yisheng_models_ext_coding.csv`、`ext_kappa_output.txt`；
  - `ext_check_sheet.xlsx`、`ext_check_key.csv`（作者核验表，126 条）；
  - `ext_summary.md`（结果摘要）。
- **主要结果**：
  - 主检验 73/141 对 23/79，GEE OR 2.35 [1.43, 3.86]，单侧 p = 0.0004，按预定规则判为支持 (C)。
  - 声符内 MH OR 2.01 [0.75, 5.39]，不显著。
  - H2 重估为 OR 21.6 [13.3, 35.0]。
  - 两次盲编四类 κ 0.817。
- **看过结果后的改动**（计划 §7 已记）：
  - S6（只算 Y）完全分离，GEE 给出发散值。脚本加了保护，S6 改记为不可估，其余各行不变。
  - 补三个探索性检验 X1–X3，不进判读。
- **未改动**：`yisheng_dataset.csv`、`yisheng_models*.csv`、`manuscript_checks_output.txt`、`blind_coding_sheet*.xlsx`、`yisheng_claude_codes.csv` 及论文各稿。权威论文版本不变。
- **后续**：论文怎么改由主稿线程决定；作者核验回来后，另做敏感性分析。

## 2026-09-30 · Claude（扩大盲编数据线程）· 按评审复核补探索性检验 X4，改摘要措辞

- **评审结论**：评审线程复核了 PR #4（`v7_work/review/ext_coding_review.md`），结论是全部数字独立复现，三处偏离可以接受。
- **结果文件**：`ext_analysis.py` 加探索性检验 X4 与 X4b，新结果写入 `yisheng_models_ext_coding.csv`。
  - X4 只用新编 677 条：59/116 对 21/73，OR 2.42 [1.37, 4.25]，单侧 p = 0.001。
  - X4b 只用原 90 条：14/25 对 2/6，不显著。
  - 其余各行和核验表不变。
- **`ext_summary.md` 措辞**：
  - 声符内比较改为“点估计相近但不精确”，不再说“主要见于跨声符比较”；
  - “许慎本人的标注”改为“最可能出自许慎的标注”，并注明 X3 是探索性检验；
  - 写明结果排除的是什么。
- **计划**：§7 记下这次改动。
- **未改动**：原数据文件、既有模型结果和论文稿。

## 2026-09-30 · Claude（扩大盲编数据线程）· 作者核验回来：一致率与改判后的敏感性分析

- **来源**：Qu 交回填好的核验表，原样存为 `youwen/ext_coding/ext_check_sheet_author_filled.xlsx`（126 条，无备注，未注明是一人还是两人填写；后来 Qu 说明了，见文末“更正核验人”条）。
- **新增文件**：
  - `ext_author_check.py`（不改 `ext_analysis.py`）；
  - `ext_author_check_output.txt`；
  - `yisheng_models_ext_author_check.csv`；
  - `ext_summary.md` 加 §7。
- **一致率**：
  - 随机抽的 50 条，作者同意共同编码 45 条；
  - 不一致的 76 条，作者同第二次 50、同第一次 23、都不同 3；
  - 估计到 677 条（分层加权）：作者对第一次盲编四类 κ 0.735，对第二次 0.798。这是作者对 LLM 的一致度，不是作者间信度。
- **改判后**：
  - 用作者判断替换核验过的 126 条，其余新条目两次盲编相同；
  - 主检验 70/138 对 19/74，OR 2.73 [1.61, 4.65]，规则下仍支持 (C)，声符内 MH 2.26 [0.80, 6.33]；
  - 主检验仍以第一次盲编的 2.35 为准，改判后的结果作为敏感性分析。
- **计划**：§7 已记，含 §4.5 之外补的描述性项目。
- **未改动**：原数据文件、既有模型结果、论文稿，以及 `ext_analysis.py`。权威论文版本不变。

## 2026-09-30 · Claude（扩大盲编数据线程）· 补记核验人（已被文末“更正核验人”条覆盖）

- Qu 说明，上一条记的核验表是两位作者一起填的，即一份联合判断，不是两人各自独立的判断。
- `ext_summary.md` §7、`ext_author_check.py` 的输出头和 `ext_author_check_output.txt` 的第二行已改；计划 §7 和 `youwen_criteria.md` §10 已补记。
- 数字、检验和结论都不变（重跑后 `yisheng_models_ext_author_check.csv` 逐格相同）。这份联合判断不能用来算作者间一致度。
- 摘要 §7 加了一段英文可用的核验说明。

## 2026-09-30 · Claude（主稿线程）· v8：并入扩大盲编的结果

- **用户要求**：Qu 2026-09-29 16:05 的原要求仍有效（v7 的写法、与 *Morphology* 论文比较水平、编码写法）；2026-09-30 06:23 选了扩大盲编，13:24 说明核验表是两位作者“一起”填的。协调线程转来评审线程的复核（`ext_coding_review.md`）和作者核验回来的消息，要求据此修订 v7。
- **本次提交**：
  - 合并数据线程的分支 `claude/youwen-extended-blind-coding-ynngrw`（PR #4）：`youwen/ext_coding/` 全部文件，以及 `PROJECT_LOG.md`、`youwen_criteria.md` 末尾两边各自追加的条目（两边都保留，按日期先后排列）。
  - 新增 `youwen/manuscript/yisheng_paper_v8.md` 与 `.docx`：v7 加扩大盲编的结果。正文按拉丁字母词计 6,987 词（另有汉字 263 个），摘要 249 词；表 7 张；参考文献 37 条，与 v7 相同；§2.1–§2.3 逐字未改。
  - 新增 `yisheng_paper_v8_numbers.md`（新增、改动、删去的数字的出处）和 `v8_evaluation.md`（相对 v7 的评价、评审清单的落实、待 Qu 决定的事）。
  - `youwen/manuscript/v7_review/` 增评审线程对扩大盲编的复核 `ext_coding_review.md`、复核脚本与输出、`extended_coding_spec.md`（原在共享文件夹 `v7_work/review/`）。
  - README、AGENTS.md、`youwen_criteria.md`（§11）已更新：当前稿改为 v8，加 `ext_coding/` 的说明、重跑命令和写法的界线。
- **v8 相对 v7 的主要改动**：
  - 中心论点：标注追踪词汇相关性，并在相关字对里偏向同词或最小派生（同音与 \*-s），程度中等；仍不是有方向的派生标记。
  - 新增 H5（相关对里亦声对是否更常近音）及其判读规则；第一次盲编 73/141 对 23/79，OR 2.35 [1.43, 3.86]，单侧 p = 0.0004，规则判为支持 (C)。
  - H2 有 634 对的大样本：141/172 对 79/462，OR 21.6 [13.3, 35.0]。
  - §3.3 补写扩大编码（767 对、预先指定、κ 0.817、锚定条目）和作者联合核验（126 条，敏感性分析 2.73）。
  - §5.2 重写：(A) 只在“按释义编码的相关性系统低估了许慎的判断”时仍能成立；“基字假说”通过了一项预先写定的检验，另两项预测未检验。
  - 为保持正文不超过 7,000 词，删去若干次要比较和喪 一例（见 `yisheng_paper_v8_numbers.md` 末段）。
- **验证**：
  - 新数字逐项对照 `yisheng_models_ext_coding.csv`、`yisheng_models_ext_author_check.csv`、`ext_kappa_output.txt`、`ext_author_check_output.txt`，没有不符；评审线程独立复核了第一次盲编的全部主要数字。
  - v7 中有而 v8 中没有的数字，逐个列入 `yisheng_paper_v8_numbers.md`。
  - 37 条参考文献与文内引用互相对上；§2.1–§2.3 与参考文献同 v7 逐字相同。
  - 检索全文：没有 “preregistered”“confirmed” 等超出证据的词，κ 只写作机器之间的一致度，核验写作联合判断。
  - DOCX 由 pandoc 3.9 按 v6 的样式生成，用 python-docx 检查。
- **从失败中得到的做法**：
  - 初稿里作者核验一段被写了两遍，是靠某一节字数从 570 涨到 915 才发现的。用脚本替换或追加整段后，先看各节字数与段落数，再往下做。
  - 压缩篇幅时，先删整句和次要比较，再做逐词润色；逐词微调一次只省 3–8 词，效率很低。
  - 协调线程的说明沿用“an author check”，而数据线程的 6e694f8 已记下 Qu 13:24 的答复；以仓库里的记录为准，写作“联合核验”。
- **权威版本**：当前稿由 v7 改为 v8；v8 待评审线程复核。
- **未改动**：数据文件、编码表、模型结果、正式计数；§2.1–§2.3 与参考文献；Qu 的 v5 DOCX 未提交改动；大徐定点抽核的范围。

## 2026-09-30 · Claude（扩大盲编数据线程）· 偏差敏感性（临界点）分析

- **来源**：独立评审对 v8 的意见（经协调者转来）：如果 (A)“意义先行”为真，“相关”的误编要多大才能造出观察到的 OR 2.35（73/141 对 23/79）？
- **做法**：探索性，事后分析，只用已有的编码，没有新的编码。新脚本 `youwen/ext_coding/ext_bias_sensitivity.py`，输出 `ext_bias_sensitivity_output.txt` 和 `yisheng_bias_sensitivity_grid.csv`，摘要 `ext_summary.md` 新增 §8，计划 §7 和 `youwen_criteria.md` §10 已记。
- **临界点**（合并 OR 2.61；GEE 尺度相差不到 1 个百分点）：真实不相关的普通对里被编成相关的比例 11.5% 才能把 OR 降到 1（79 个编为相关的普通对里约 50 个是假阳），9.1% 降到 1.5，5.9% 降到 2；自助法 95% 下限到 1 需要 5.8%。亦声组的假阳率几乎不影响（0–30% 时 11.5%–11.9%），两组相同时 11.6% 就够：需要的是基数（编为不相关的字对，普通组 383、亦声组 31），不是两组误差不同。
- **对照**：两次盲编之间普通组假阳率 4.2% [2.1, 6.8]（19% 的第一次编为相关的普通对被第二次否定），按它校正 OR* 2.20 [1.18, 4.34]。作者汇总判断的抽查样本给 10.2% [2.5, 20.6]（47% [14, 89]），OR* 1.29 [0.00, 3.84]，区间太宽：随机层里第一次编为相关的普通对只有 5 个，53 个编为相关的普通对没有作者判断。
- **结论**：随机编码误差抹不掉这个差别；两次盲编共有的系统偏差（最可能是 E 的阈值）在现有核验样本下既不能肯定也不能排除。另一条路（按释义编码在普通近音对里漏判相关）要求灵敏度之比 0.38 [0.21, 0.65]，即意义联系要在同音的普通对里更常藏在释义之外、在亦声对里不然；作者核验这类字对只判了 6 个，数据不能排除。
- **未改动**：原数据文件、既有模型结果、论文稿，以及 `ext_analysis.py`、`ext_author_check.py`。主检验仍是第一次盲编的 OR 2.35，判读不变。是否写进论文由主稿线程决定。

## 2026-09-30 · Claude（扩大盲编数据线程）· 更正核验人（覆盖上面的“补记核验人”）

- **更正**：Qu 在评审线程 16:42 说（原话：「最后一个也是分开编的，然后给了汇总的，总而言之，后面与前面的流程是一致d」，经协调者 18:21 转来）：126 条核验由两位作者各自分开核对，再汇总成一张表，每条一个编码。13:24 的「一起」只是说两位作者都参与了，我读成了“一起填一张”，读错了；上一条“补记核验人”作废。
- **现在的说法**：作者汇总判断（each author checked separately; consolidated into one code per item）。在手的只有汇总表，所以 κ 是作者汇总判断对 LLM，不是作者间一致度；汇总时两人判断不同的条目怎么定，Qu 未说明。表上显示了抽查类型和两次盲编的编码（评审指出），核验不独立于它们。
- **待办**：评审已问 Qu 两位作者各自的原表是否还在；若上传，补算作者间一致度（按层加权：76 条不一致全数，加从 601 条一致中随机抽的 50 条）。目前没有收到。
- **已改**：`ext_summary.md` §7、§8（含给论文的两段英文），`ext_author_check.py` 的输出头和 `ext_author_check_output.txt` 第二行，`ext_bias_sensitivity.py` 及其输出的措辞，`youwen_criteria.md` §10，计划 §7，以及 PR #4 的说明。
- **不变**：数字、检验和结论（重跑后 `yisheng_models_ext_author_check.csv` 与 `yisheng_bias_sensitivity_grid.csv` 逐格相同）。论文稿是主稿线程的文件，由它改。

## 2026-09-30 · Claude（扩大盲编数据线程）· 第二次回答替换（X5，探索性）

- **缘起**：撰稿线程（v9）经协调者 18:29 请求，评审手算得 OR 2.39 [1.38, 4.14]：第一次盲编第 3、6 批各有一份按预定规则（每个代理实例第一份完整合格的回答算数）没有用的第二次回答，改用它们后主检验怎么变。
- **做法**：新脚本 `youwen/ext_coding/ext_second_answer_sensitivity.py`（不改既有脚本），把这两批 193 个新条目（锚定条目不动）的第一次回答换成第二次回答，重算主检验和相关检验；另跑只换第 3 批、只换第 6 批。先不替换，重现既有结果（逐格相同）；重跑两次输出逐字节相同。没有新编码，没有合成共识。
- **结果**：主检验 71/139 对 21/74，GEE OR 2.39 [1.38, 4.14]，单侧 p = 0.0009，与评审手算三个数都相同（对照 73/141 对 23/79，2.35 [1.43, 3.86]）；只换第 3 批 2.32 [1.42, 3.79]，只换第 6 批 2.40 [1.39, 4.14]。S1 2.28 [1.20, 4.32]、S2 2.10 [1.13, 3.89]、S3 1.82 [1.01, 3.29]，判读都是“支持 (C)”，没有变。X3（探索性核心口径）1.79 [0.90, 3.60]，单侧 p 0.0497，靠着 .05 的界；只换第 6 批时 p 0.063，判为不定。
- **读法**：结论不取决于“第一份回答算数”这条规则在这两批上的后果；这只测两批里两份回答的选择，不是编码者差异的全貌。第 3 批的第二份与第一份出自同一上下文，不独立；第 6 批的第二份是同一提示的独立重新运行。
- **命名**：撰稿线程和评审叫它“S6”，与分析计划 §4.3 的 S6（只算 Y）同名不同物，文件里记为 X5。
- **新文件**（`youwen/ext_coding/`）：`ext_second_answer_sensitivity.py`、`ext_second_answer_sensitivity_output.txt`、`yisheng_models_ext_second_answer.csv`、`ext_second_answer_items.csv`（两份回答逐条对照）；摘要 §9、计划 §7、`youwen/youwen_criteria.md` §10 已记。
- **未改动**：原数据文件、既有模型结果、既有脚本、论文稿。主检验仍是第一次盲编的 OR 2.35，判读不变；是否写进论文由主稿线程决定。

## 2026-09-30 · Claude（主稿线程）· v9：长版，并入评审意见和两项新分析

- **用户要求**：Qu 2026-09-30 13:58：篇幅“参考 Morphology 和往期论文投稿要求，重点是把事情说清楚”，参考文献先保持（37 条），无需核 *Morphology* 的 SSCI 收录，作者为 Yusen Wu 与 Weiyi Qu（School of English and International Studies, Beijing Foreign Studies University），无基金与利益冲突；另问 Zenodo 与 OSF 的区别（在给 Qu 的回复里答）。协调线程转来评审对 v8 的意见（M1、S1–S7、补回清单、篇幅分配），18:21 转来 Qu 16:42 的更正：126 条核验是两位作者各自核对、再汇总，不是一起填（13:24 的“一起”只说两位都参与）。
- **本次提交**：
  - 合并数据线程分支 `claude/youwen-extended-blind-coding-ynngrw` 的新提交：偏差临界点分析（18:32）、更正核验人（18:38）、第二次回答替换（X5，18:45）。`PROJECT_LOG.md` 与 `youwen_criteria.md` 两边各自追加的条目都保留（数据线程在 §10 末尾加的两条放在 §11 之前）。
  - 新增 `youwen/manuscript/yisheng_paper_v9.md/.docx`（完整版）、`yisheng_paper_v9_anonymised.md/.docx`（双盲投稿用）、`yisheng_v9_title_page.md/.docx`（题名页）、`yisheng_paper_v9_numbers.md`（新增、改动、恢复的数字的出处）、`v9_evaluation.md`（相对 v8 的变化、评审意见的落实、投稿形式、待 Qu 的事）、`figures/fig1_h5_forest.png` 与 `fig1_h5_forest_values.csv`。
  - 新增脚本 `youwen/scripts/yisheng_v9_counts.py`（重算正文里结果文件不直接给出的计数，带断言）、`yisheng_v9_figure.py`（图 1）、`yisheng_make_submission_files.py`（匿名版、题名页和三个 DOCX，断言匿名版没有作者信息）。
  - 更正记录里“联合核验”的说法：`AGENTS.md`、`README.md`、`youwen_criteria.md`（§11）；`yisheng_paper_v8_numbers.md` 与 `v8_evaluation.md` 文首加了更正说明，v8 正文保持原样留作历史。
  - README、AGENTS.md、`youwen_criteria.md`（新 §12）已更新：当前稿改为 v9，加双盲文件、三个脚本和数据线程两项新分析的说明；篇幅规则由“5,000–7,000 词”改为 Qu 13:58 的说法。
- **v9 相对 v8 的主要改动**：
  - 篇幅：正文 8,614 词（v8 为 6,987），连表约 10,600 词；表由 7 张增至 12 张，另加图 1；参考文献仍是 37 条。
  - 背景与方法：新 §2.1 小导引；§3.3 改为编码方案，加表 3（各码的例子）；新 §3.4 写扩大编码与作者核验；§3.5 加“OR 是什么”和最小关心效应取 2 的理由。
  - 结果：表 5 列出 16 个去声成员；v8 的表 5 拆成表 7（语义）与表 8（相关对里的读音，加一行第二次回答替换）；§4.3 加两次盲编分歧与核验的一段；表 9 同音字对的关系类型；补回 v8 为守字数删去的检验（上古 R 类 6/29 对 48/179，不归本部者 24/46 对 26/90，核心层 26% 对 46%，段注按语 4/21，小徐读法对王筠九条的检验）。
  - 讨论：表 12 把假设、结果与对四种解释的含义放在一起；§5.2 加偏差临界点（约 11% 的真不相关普通对被编成相关才能把 OR 降到 1，约 6% 降到 2；两次盲编之间 4%）；§5.4 补回喪、唐写本和王筠的一句；§6 写明作者只判了 79 个相关普通对中的 26 个。
  - 评审的 M1、S1–S7 全部落实；核验写作“两位作者各自核对 126 条，再汇总”，全文没有 joint、jointly。
- **验证**：
  - 重建链全部通过：`build_v9.py`（从 v8 改起的场外脚本，每处替换都断言旧文本恰好出现一次，并断言全文没有 joint、jointly）→ `yisheng_make_submission_files.py v9` → `yisheng_v9_counts.py` → `yisheng_v9_figure.py`。
  - 计数：摘要 249 词（Springer 常见上限 250），正文 8,614 词，连表、表注、图注约 10,600 词；12 张表、1 幅图、37 条参考文献。`yisheng_v9_counts.py` 用断言固定 767 对、634 对、150 个声符、76 处分歧（亦声 33、普通 43）、核验 126 条的各项数字、表 3 的例字、表 9 的同音对类型；全部与数据文件一致。
  - 新结果逐项对照数据线程的输出：表 8 的“第二次回答替换”一行与表注（193 条、第 3 批 2.32 [1.42, 3.79]、第 6 批 2.40 [1.39, 4.14]）对 `ext_second_answer_sensitivity_output.txt`；§5.2 的临界点（11.5%／GEE 尺度 11.0%、79 个里约 50 个、降到 2 需要 5.9%、两次盲编之间 4.2%、校正后 2.20 [1.18, 4.34]、作者核验 10.2% [2.5%, 20.6%]）对 `ext_bias_sensitivity_output.txt`；§4.4 新例字（傾／頃、珥／耳、窞／臽、胖／半、𠛎／句、繪／會、僎／巽、鬻／米）的码和读音类逐对对 `ext_codes_long.csv`。一致。
  - 文内的节、表、图引用逐条解析，表 1–12 与图 1 都有定义、都被引用；DOCX 用 python-docx 读回，表数、图数、𠔁 𨻺 䢈 三个扩展区字符都在。匿名版与匿名 DOCX（含全部 XML）没有作者姓名、单位、仓库属主名，作者属性为空。
  - 声明里“两位作者复核了同音对的关系类型”有记录可查：`coding_provenance_v6.md` 写两位作者逐对复核了 63 个亦声同音对和 133 个普通同音对；记录没说是各自还是一起，所以 v9 只写 both reviewed。
  - **没有做到的**：负责独立核数字的子任务被容器重启打断，没有出报告，所以 v9 的数字核对靠上面的脚本断言和逐项对照，没有第二位读者；LibreOffice 在本环境不可用，DOCX 没有渲染成页面看过，投稿前要在 Word 里看一遍表格、上标和 CJK 扩展区字体。数据线程的 `ext_bias_sensitivity_output.txt` 限制 7 仍写“预注册”，与本项目“pre-specified，不写 preregistered”的规则不一致（论文正文没有用那个词；文件归数据线程，本线程没有改，交付说明里提请协调线程转告）。
- **从失败中得到的做法**：
  - Qu 的“一起”被读成“一份联合判断”，v8 与三份记录文件据此写错，16:42 才更正。以后一句话的答复若有两种读法，正文先用中性措辞，向 Qu 提问时把将要写进论文的原句引出来，更正时一次改全所有记录。
  - 表 9 的普通对数先得 143，是数据集里按全部普通行数的；限于 172 个声符的框内是 133（v8 对）。类似的计数要限定在框内，并放进 `yisheng_v9_counts.py` 用断言固定。
  - pandoc 的参考样式文件带着作者姓名，匿名 DOCX 必须清空作者属性，并检查全部 XML 里没有作者信息；已写进 `yisheng_make_submission_files.py` 的断言。
  - 合并数据线程的分支时，`PROJECT_LOG.md` 与 `youwen_criteria.md` 必然在文末冲突：两边条目都留，数据线程加在 §10 末尾的条目放在主稿线程的 §11 之前。
  - 用带计数断言、可重跑的脚本改稿，再看各节字数；第三轮改动（数据线程的新结果）只要在脚本末尾再加一组断言替换，不必手改。
  - 容器重启会打断正在跑的后台子任务，且不留报告（这次是核数字的子任务）；场外的脚本和记忆文件不受影响。要核的数字先做成带断言的脚本，放进仓库，比只靠子任务稳；子任务只当第二读者，不当唯一的核对。
- **权威版本**：当前稿由 v8 改为 v9（完整版、匿名版、题名页）；待评审线程复核。
- **未改动**：数据文件、编码表、模型结果、正式计数；`ext_coding/` 里数据线程的文件（只合并，没有改）；参考文献（仍是 37 条）；Qu 的 v5 DOCX 未提交改动；大徐本定点抽核的范围。

## 2026-09-30 · Claude（扩大盲编数据线程）· 措辞更正：“预注册”改为“分析前已固定”

- **缘起**：撰稿线程发现 `ext_bias_sensitivity_output.txt` 局限第 7 条写了“预注册”，协调者 23:27 转来。本项目只写 pre-specified（分析前已固定）：分析计划在编码前提交（7b7c249），但 OSF 上什么也没注册。
- **已改**（只改措辞，数字、检验和结论不变）：`ext_bias_sensitivity.py` 里的这一句和重跑后的 `ext_bias_sensitivity_output.txt`（与上一版只差这一行，`yisheng_bias_sensitivity_grid.csv` 逐格相同）；计划 §7 里 18:31 条的一句（并在 §7 末尾记一条更正）；`ext_analysis.py` 里的一行注释；PR #4 说明里的“pre-registered rule”。
- **已搜**：`youwen/ext_coding/` 下所有文件、`youwen_criteria.md`、`PROJECT_LOG.md`、`ext_summary.md` 里没有其他“预注册 / preregistered / pre-registered”。`youwen/manuscript/yisheng_paper_v6.md` 里的 “were not preregistered” 是 Codex 的 v6，说的是没有预注册，与本规矩一致，未动。

## 2026-09-30 · Claude（扩大盲编数据线程）· 偏差敏感性的反方向情景（评审 S3，探索性）

- **缘起**：独立评审对 v9 的意见（协调者 23:46 转来）：摘要 §8 只看普通组假阳这一个方向；反方向是亦声组里第一次盲编编为无关的 31 对，若按标注本身算相关，并入相关组后近音差别还剩多少。评审手算约 2.17，要求用脚本算出区间。
- **做法**：新脚本 `youwen/ext_coding/ext_bias_reverse_scenario.py`（不改既有脚本，没有新编码，没有随机数）。先不并入，逐格重现 `yisheng_models_ext_coding.csv` 的 P1、S1；再把 31 对全部并入，另算最不利的取法（只并入其中不近音的 23 对）。这 31 对里近音 8、不近音 23；大小徐共有 25、大徐独有 5、未定 1。
- **结果**：全部并入后近音 81/172 对 23/79，GEE OR 2.00 [1.23, 3.26]，单侧 p = 0.0026，合并优势比 2.17（即评审的数，GEE 按声符聚类，点估计更低）；声符内 MH 2.18 [0.86, 5.48]；同音口径（S1）2.31 [1.22, 4.38]。最不利取法 73/164 对 23/79，1.76 [1.11, 2.80]。按规则都仍判为支持 (C)，区间下限都在 1 以上，但点估计降到了 2 上下，即最小关心效应的位置。
- **读法**：极端的压力测试，不是估计（它假定 31 对都真有意义联系）。反方向的误编抹不掉差别，也降不到 1；普通组假阳的方向才可能降到 1（见 §8）。论文里引用 GEE 的数，不要引 2.17。
- **新文件**（`youwen/ext_coding/`）：`ext_bias_reverse_scenario.py`、`ext_bias_reverse_scenario_output.txt`、`yisheng_bias_reverse_scenario.csv`；摘要 §8 末尾补了一句，计划 §7、`youwen/youwen_criteria.md` §10 已记。
- **未改动**：原数据文件、既有模型结果、既有脚本、论文稿。主检验仍是第一次盲编的 OR 2.35，判读不变；是否写进论文由主稿线程决定。

## 2026-10-01 · Claude（主稿线程）· v10：按 Morphology 投稿要求排版（不再优化）

- **用户要求**：Qu 2026-10-01 04:08（项目聊天，附两份 PDF：*Morphology* 的 Submission guidelines、Springer Nature 的 Submit faster on Snapp）：「这一版不必再优化，按morphology投稿要求排版，然后把补充材料安排好即可（包括命名和内部格式，注意英文为主要呈现语言）」；04:17 Qu：额度已重置，可以开始。04:04 Qu 对 126 条原表和汇总规则一问答「我和另一位作者做了编码的，和之前编的是一致的，可以忽略这个问题」：不再追问，v9 的措辞不变。
- **本次提交**：
  - 合并数据线程的新提交（`93fa1d4`：措辞更正“预注册”→“分析前已固定”、反方向偏差情景）；`PROJECT_LOG.md`、`youwen_criteria.md` 的冲突按“两边条目都留”处理。
  - 新增 `youwen/manuscript/yisheng_paper_v10.md/.docx`（完整版）、`yisheng_paper_v10_anonymised.md/.docx`（双盲投稿用）、`yisheng_v10_title_page.md/.docx`（题名页）、`yisheng_v10_cover_letter.md/.docx`（cover letter）、`yisheng_paper_v10_numbers.md`、`v10_evaluation.md`；按 Springer 和 Snapp 要求排好的上传文件和核对表在 `youwen/manuscript/submission/`（`Manuscript_anonymised.docx`、`Title_page.docx`、`Cover_letter.docx`、`Fig1.eps/.tif/.png`、`SUBMISSION_CHECKLIST.md`、`audit_v10_output.txt`）。
  - 新增脚本 `youwen/scripts/yisheng_v10_figure.py`（图 1，Springer 规格）、`yisheng_submission_audit.py`（对照指南的自查）；`yisheng_make_submission_files.py` 按 v10 的结构重写（A4、Times New Roman 11 pt、三线表、自动页码、匿名稿断言）。
  - README、AGENTS.md、`youwen_criteria.md`（新 §13）已更新：当前稿改为 v10，加上传文件、核对表和新脚本的说明；规则由“另存为 v10”改为“另存为 v11，不要覆盖 v10”。`v9_evaluation.md` 文首的更新说明改正：评审已复核 v9，S2、S5 在 v10 里改了，S1、S3 没做。
- **v10 相对 v9 的改动**（全部列在 `yisheng_paper_v10_numbers.md`）：没有新数字。S2（§1 对 Wang Yun 的说法与 §2.2 矛盾）和 S5（“encoffined/coffined”）；表按数字顺序首次引用（5 处向后引用改成章节引用）；关键词 7 个减为 6 个；摘要缩两处措辞（246 词）；§3.6 写明语言模型的使用；图 1 重画（119 mm 宽、8 pt、黑白）并改用 Springer 的图题写法；文末改成 Supplementary Information（7 条 caption）和 Statements and Declarations；仓库路径换成 Online Resource 1–7（数据线程 2026-10-01 04:30 的临时清单，经协调者转来），caption 里的数字逐个对文件核过；4 条参考文献补了 DOI。
- **验证**：
  - `yisheng_submission_audit.py v10`：摘要、关键词、标题层级、缩写、表和图的编号与引用顺序、表注字母、图题格式、图的像素与 dpi 与元数据、参考文献的排序与 DOI、Statements and Declarations、Online Resource 的引用顺序和 caption、匿名稿与 DOCX 全部 XML 无作者信息、无批注与修订、页码字段，共 97 项通过，0 项失败；占位符（通讯作者、邮箱、ORCID、贡献、再用材料、编委身份）以 INFO 报告。
  - DOCX 经 LibreOffice 渲染后逐页看过（匿名稿 28 页，题名页、cover letter 各 1 页）。
  - 汇总核对 caption 的数字：`yisheng_dataset.csv` 1,333 行，小徐对勘 227 行，`daxu_spotcheck_v6.csv` 104 行，`ext_coding/prompts/` 14 个提示，`ext_coding/raw/` 两份未用的第二次回答。
  - **没有做到的**：Word 里的实际显示没有看（只有 LibreOffice）；图宽按小开本取 119 mm，没有查到 *Morphology* 的开本；补充材料文件还在建，只核了 caption 的数字，没有打开文件；ESM_2 里再分发的中古音和上古音数据的许可条款仓库里没有记录（数据线程在 ESM_1 注明）。
- **从失败中得到的做法**：
  - LibreOffice 报 “source file could not be loaded”，原因是没装 `libreoffice-writer`（只有 `soffice` 启动器）：`apt-get update && apt-get install -y libreoffice-writer` 之后能转 DOCX→PDF，再用 pymupdf 转 PNG 看版面。已写进团队记忆的云端工具记录。
  - 自查脚本里 `[㐀-鿿\U00020000-\U0002fffff]` 多写了一位：`\U` 要恰好八位十六进制，`\U0002fffff` 被读成 `\U0002ffff` 加一个字面的 `f`，于是每个 f 都算汉字，摘要的 “把汉字各算一词” 字数被虚报成 250（实际 247）。字符区间写 `\U0002fa1f`，并拿独立方法对数一次。
  - pandoc 模板放在 Python f-string 里时，`::: {custom-style="…"}` 的花括号要双写，否则报 `f-string: expecting '}'`。
  - 上下文压缩后，协调者在压缩前转来的补充材料清单摘要里没有；先用 `fetch_thread`（新到旧）读自己线程的最近活动，里面有 “Received a message from the coordinator” 条目，从中补回遗漏的转达。
  - 排序检查把 “(100 CE)”“(10th century)” 当成无年份，误报字母序错；检查日期时要容许这两种写法。
- **权威版本**：当前稿由 v9 改为 v10（完整版、匿名稿、题名页、cover letter、上传文件）；v10 的数字与 v9 相同。
- **未改动**：数据文件、编码表、模型结果、正式计数；`ext_coding/` 里数据线程的文件；参考文献的条目和数量（37 条，仅补 DOI）；Qu 的 v5 DOCX 未提交改动。

## 2026-10-01 · Claude（主稿线程）· v10 小改：匿名稿按 Snapp 双盲页只留 Data availability

- **起因**：v10 交付后，我对照 Springer Nature 自己的 Snapp 双盲页（springernature.com/gp/snapp/submitting/how-to-submit/double-anonymous，2026-10-01 抓取原页）复核。该页写明稿件文件 “should not include: author acknowledgements or contribution statements; a competing interest statement; an ethics statement; funding information”，这些由 Snapp 询问，填入的内容进入发表版；没有提数据可用性声明，也没有提单独的题名页。*Morphology* 的指南 PDF 则一边说 “Statements and Declarations” 随论文发表（没有声明的稿件会被退回），一边在开头说换用 Snapp 后这类声明 “instead of including it in the manuscript” 在界面里填。两处不一致，我按 Snapp 页办（它是平台的现行说明，也是指南开头那句所指的做法），并在核对表第 4 节写明理由和退路。这是排版合规，不是内容改动：正文、表、图和数字都不变。
- **改了什么**：
  - `yisheng_make_submission_files.py`：匿名稿去掉 Funding、Competing interests、Ethics approval and consent、Coding、Author contributions 五段，只留 Data availability（“Coding” 一段含作者姓名，内容已见 §3.3–3.5）；题名页的说明改为 “不是匿名稿的一部分，是 Snapp 表单的英文底稿，系统要求题名页时再传”；cover letter 一条说明相应改写。
  - `yisheng_submission_audit.py`：匿名稿必须有 Data availability，不得有 Funding、Competing interests、Ethics、Author contributions、Acknowledgements/Acknowledgments；结果 100 项通过，0 项失败（原 97 项；声明部分的检查由 4 条变为 7 条）。
  - 重新生成匿名稿、题名页、cover letter 及其 DOCX，复制到 `submission/`；`SUBMISSION_CHECKLIST.md` 第 1、4 节、`v10_evaluation.md`（§3 第 7 项）、`yisheng_paper_v10_numbers.md`（“文末” 一行）、README、AGENTS.md、`youwen_criteria.md` 同步。完整版 `yisheng_paper_v10.md` 不变，仍含全部声明；如编辑部要求声明写进稿件，删去 Author contributions（含作者姓名缩写）后贴回即可。
- **从这件事得到的做法**：搜索摘要和抓取原页对同一页说得不一样（搜索摘要提到 “separate Title Page”，原页没有）；以抓取到的原页为准，并分别写明哪些是原页明文、哪些是推断。云端环境里 `WebSearch`/`WebFetch` 可以访问 springernature.com；投稿规则以平台页和期刊指南的原文为准，不以记忆或摘要为准。
- **未改动**：论文正文、表、图、数字、参考文献；数据文件和 `ext_coding/` 里数据线程的文件；补充材料（仍在数据线程手里）。

## 2026-10-01 · Claude（主稿线程）· 补充材料 ESM_1–7 到手：核对，数据可用性声明换成数据线程的版本，核对表重写，自查脚本加补充材料一节

- **起因**：数据线程 09:49 交付补充材料 ESM_1–7（共享文件夹 `v7_work/submission/supplement/`，约 1.8 MB；协调者转来，附一句话缩写）。我对着文件本身核，不对缩写：文件名、每份文件里自带的 caption、行数和数字、文档属性、有无作者信息、ESM_7 重跑、“谁做了什么”的措辞。本次提交只含正文侧、文档和自查脚本；七份文件和数据线程的重建脚本等它改完下面第 5 点的措辞、我复核后另提交（现在提交会在仓库里留下两份 1.8 MB 的二进制）。
- **核对结果**：
  1. 七份文件的完整 caption（PDF 第 1 页、xlsx 的 About 表、zip 里的 README）与匿名稿 Supplementary Information 一节的七条逐字相同（去掉斜体标记后比对）；文件名 ESM_n.ext 与清单一致。
  2. 行数与 caption 一致：`pairs` 1,333，`recension_collation` 227，`daxu_spotcheck` 104，`first_sample` 100，`enlarged_coding` 767，`author_check` 126，`second_answers` 203；ESM_5 共 34 个文件（14 个提示、14 份原始回答、2 份未用的第二次回答）；ESM_6 共 21 个 sheet；ESM_7 共 67 个文件。
  3. PDF 和 xlsx 的文档属性、zip 内 xlsx 的属性均无作者、最后修改者、公司；全部文本、单元格、批注、zip 成员名和额外字段里没有作者姓名、单位、邮箱、本地路径和会话号；仓库链接只有两个第三方来源（digling/cddb、shuowenjiezi/shuowen）。
  4. ESM_7 解压后在这里重跑 `python scripts/run_all.py`：249 项通过、0 项失败（25 个预期输出一致、189 个论文数字、20 项完整性），约 53 秒，与数据线程所报一致。
  5. 与来源记录有出入的两处措辞，已报协调者，由数据线程改 ESM_1、ESM_3、ESM_5、ESM_7：(a) 锚定条目写成 “每个批次都重复”，实际每批 5 个、共 35 个不同的首样本条目，每遍各编一次（ESM_1 第 6、7、9 页，ESM_3 数据字典，ESM_5 README 的 item_key 说明，ESM_7 数据字典 3 行）；(b) ESM_1 小徐对勘一行：Claude 线程抽查的是 像、瑁 两条（`youwen_criteria.md` 第 240 行附近），“no further human check” 容易让人以为抽查是人做的，应写成对勘由 Claude 实例完成、抽查由 Claude 实例做、没有人工核对。可选的第三处：第一次出现 “coders”“coder instances” 的地方加 “(Claude instances)”，与论文用词一致。论文 §3.6、Declarations 与 `coding_provenance_v6.md` 之间没有新增的 “谁做了什么” 的说法。
  6. 没有做到的：这里没有 Excel 和 Acrobat，xlsx 和 PDF 没有实际打开过（用 openpyxl 和 PyMuPDF 读了，渲染看了 ESM_1 第 1、11 页和 ESM_4 第 1 页）；各来源的许可原文没有核（相关仓库不在本环境可访问的范围内），ESM_1 §8 的条款是数据线程读原文后写的。
- **改了什么**：
  - `yisheng_paper_v10.md` 的 Data availability 一段换成数据线程的措辞，“coder instances” 改为 “Claude instances”（与 §3.4 一致）；匿名稿、题名页及其 DOCX 重新生成，复制到 `submission/`；自查仍为 100 项通过。
  - `SUBMISSION_CHECKLIST.md` 重写：状态为 满足／不适用／需 Qu／待数据线程／待入库；第 4 节说明匿名稿只留 Data availability 和退路；第 7 节第三方许可一行记为 “需 Qu 确认”；新增第 8 节（补充材料核对）和第 9 节（要 Qu 回答的事项：6 项必答、6 项选答）。`v10_evaluation.md`、`yisheng_paper_v10_numbers.md`、README 的 “待 Qu” 一条同步。
  - `yisheng_submission_audit.py`：`submission/supplement/` 里有文件时再查七份文件的名称、自带 caption 与匿名稿的逐字一致、行数和文件数、属性、全部文本里的姓名、单位、邮箱、本地路径和会话号；`--rerun-esm7` 解压 ESM_7 并重跑。用改坏的副本（加创作者属性、加邮箱、改 caption）验证过能报错。把七份文件临时放进 `submission/supplement/` 测试：132 项通过、0 失败（含重跑）；仓库里现在没有这个文件夹，所以保存的输出是 100 项通过加一行 “not in the repository yet”。
- **需 Qu**（核对表第 9 节）：(1) 通讯作者及邮箱、ORCID、作者贡献、是否以学位论文或会议稿发表过、是否有人是 *Morphology* 编委；(2) §3.1 “We visually checked … 104 of them” 对陈本扫描，是 Codex 读的还是作者也逐页看了（二选一，决定把句子改成什么）；(3) 补充材料的许可：作者自己的贡献 CC BY 4.0、代码 MIT，第三方列保留原条款（说文文本 Apache-2.0；上古音构拟字符串来自 Baxter–Sagart，经 cddb，GPL-3.0；中古音来自 nk2028，CC0／MIT）；是否在 CC BY 文件里保留 Baxter–Sagart 构拟串。这是数据线程的提议，**需 Qu 确认**。
- **留意**：`youwen/ext_coding/ext_check_sheet_author_filled.xlsx` 与 Qu 上传的作者核验原表逐字节相同，文件属性里有作者本名；以后做 OSF 或 Zenodo 的匿名数据副本时必须去掉或洗掉它（补充材料里的 `author_check` 是合并后重建的数据，没有这个问题）。S3 反向情景（GEE OR 2.00 [1.23, 3.26]）只在 ESM_6、ESM_7，正文不提。补充材料的自检脚本不扫描人名，论文、cover letter 和核对表里不要写 “自检会检查个人信息”。ESM_5 与 ESM_7/data/raw 都含原始回答，是有意重复。ESM_4 第 7 节的完整偏离记录（含 13:25 的 “together” 条目和 18:37 的更正）审稿人能读到，需 Qu 知悉。
- **从这件事得到的做法**：
  - 交付包对文件本身核，不对发送方的一句话缩写：“锚定条目每批重复” 要读 ESM_1 的批次说明和 ESM_3 的条目表才发现与 “每批 5 个” 不符。
  - 后台 Bash 任务里启动长时间运行的脚本，返回的 “completed (exit 0)” 只是外层 shell 的结束，不是脚本的结束；要另开一个后台 until 循环，等输出文件里出现 “exit 0”（ESM_7 的 run_all 约 53 秒）。
  - 内置安全检查会拦下 `rm -rf *` 一类的清理命令：不要绕，改用全新的目录，需要删的只删自己刚建的具体文件。
- **未改动**：论文正文（除数据可用性一段）、表、图、数字；参考文献；数据文件和 `ext_coding/` 里数据线程的文件；Qu 的 v5 DOCX 未提交改动。
