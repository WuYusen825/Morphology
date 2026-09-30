# 《说文》亦声与派生：训诂学 × 形态学研究论文

这个仓库存放 Qu 的 SSCI 论文项目的全部工作文件：论文稿、数据、脚本、文献综述和原书书页。内容原来放在 Claude 项目的共享文件夹（Library）里，2026-09-26 整体搬到这里，目录结构保持不变（都在 `youwen/` 下）。

- **研究问题**：许慎《说文解字》的"亦声"标注，是不是对派生关系的隐性标记？
- **论文题目**（暂定）：*What does 'also phonetic' mark? The Shuōwén's yìshēng label, homophony and derivation in Old Chinese*
- **目标期刊**：*Morphology*（Springer）。2026-09-29 Qu 改定，Release `学习` 的 11 篇即发在该刊，作为写法和水平的参照。该刊的 SSCI 收录尚未核实（Springer 页面只列 ESCI），投稿前须在 mjl.clarivate.com 查。此前的首选是 *Language and Linguistics*，备选 *Journal of Chinese Linguistics*；v7 正文不写与收录有关的话，改投时结构不必大改。
- **论文语言**：英文。

## 现在读哪个文件

| 要看什么 | 文件 |
|---|---|
| 论文当前稿（v8，2026-09-30；v7 加上扩大盲编的结果） | [`youwen/manuscript/yisheng_paper_v8.md`](youwen/manuscript/yisheng_paper_v8.md)，Word 版 [`yisheng_paper_v8.docx`](youwen/manuscript/yisheng_paper_v8.docx) |
| v8 新增、改动和删去的数字的出处（没变的数字见 v7 的出处文件） | [`yisheng_paper_v8_numbers.md`](youwen/manuscript/yisheng_paper_v8_numbers.md)、[`yisheng_paper_v7_numbers.md`](youwen/manuscript/yisheng_paper_v7_numbers.md) |
| v8 评价：相对 v7 的变化、评审清单的落实、仍待 Qu 决定的事 | [`v8_evaluation.md`](youwen/manuscript/v8_evaluation.md) |
| 扩大盲编（767 对语义编码：编码前提交的分析计划、两次盲编、作者联合核验） | [`youwen/ext_coding/`](youwen/ext_coding/)：分析计划 [`analysis_plan.md`](youwen/ext_coding/analysis_plan.md)，结果摘要 [`ext_summary.md`](youwen/ext_coding/ext_summary.md)，结果 [`yisheng_models_ext_coding.csv`](youwen/ext_coding/yisheng_models_ext_coding.csv)、[`yisheng_models_ext_author_check.csv`](youwen/ext_coding/yisheng_models_ext_author_check.csv) |
| 上一稿（v7）及其评价、计划、评审报告 | [`yisheng_paper_v7.md`](youwen/manuscript/yisheng_paper_v7.md)、[`yisheng_paper_v7.docx`](youwen/manuscript/yisheng_paper_v7.docx)；[`v7_evaluation.md`](youwen/manuscript/v7_evaluation.md)、[`v7_plan.md`](youwen/manuscript/v7_plan.md)；评审线程的报告在 [`v7_review/`](youwen/manuscript/v7_review/)（含对扩大盲编的复核 `ext_coding_review.md`） |
| 更早的稿子（v6） | [`yisheng_paper_v6.md`](youwen/manuscript/yisheng_paper_v6.md)，Word 版 [`yisheng_paper_v6.docx`](youwen/manuscript/yisheng_paper_v6.docx) |
| Codex 的 v6 系统重构修改计划（2026-09-29 修订；v7 只作参考） | [`v6_系统重构修改计划.md`](youwen/manuscript/v6_系统重构修改计划.md)，附[关键例组核查](youwen/manuscript/lexical_examples_audit_v7.md)；按该计划写到一半的稿子改名为 [`yisheng_paper_v7_codex_partial.md`](youwen/manuscript/yisheng_paper_v7_codex_partial.md)，含占位符，留存备查 |
| v6 大徐本抽核与编码来源 | [`daxu_spotcheck_v6.csv`](youwen/manuscript/daxu_spotcheck_v6.csv)、[`daxu_source_audit_v6.md`](youwen/manuscript/daxu_source_audit_v6.md)、[`coding_provenance_v6.md`](youwen/manuscript/coding_provenance_v6.md) |
| 文献综述（v0.3 即 v7、v8 的第 2 节，附书目编号） | [`youwen/literature_review.md`](youwen/literature_review.md) |
| 注释书目（编号 A1–F2，综述和论文都按这个编号引用） | [`youwen/bibliography.md`](youwen/bibliography.md) |
| 数据怎么来的、判定标准、各轮结果 | [`youwen/youwen_criteria.md`](youwen/youwen_criteria.md)（亦声部分在 §6b–§6e，v7 补充检验与编码写法在 §9，扩大盲编在 §10，v8 的用法在 §11） |
| 王筠《说文释例》原文录文与书页 | [`youwen/shili_pages/README.md`](youwen/shili_pages/README.md) |
| Codex / Claude 共同变更日志 | [`PROJECT_LOG.md`](PROJECT_LOG.md)（两者修改项目前先读，修改后追加记录） |
| v5 参考文献 DOI 核对表 | [`youwen/doi_audit_v5.md`](youwen/doi_audit_v5.md) |
| 期刊 Discussion 写法学习（两轮精读的总结与对 v6 的建议；v7 据此改写） | [`youwen/Discussion精读总结.md`](youwen/Discussion精读总结.md)、[`Discussion宏观写作指导.md`](youwen/Discussion宏观写作指导.md)；逐篇笔记 [`discussion_close_reading.md`](youwen/discussion_close_reading.md)、[`discussion_close_reading_morphology2026.md`](youwen/discussion_close_reading_morphology2026.md)，阅读范围 [`discussion_reading_index.md`](youwen/discussion_reading_index.md) |

v1–v7 是旧稿，只留作对照。以后实质改稿请另存为 v9，不要覆盖 v8。

v7 由 Claude 的三个线程分工完成（2026-09-29/30）：主稿线程按两份 Discussion 总结改写计划、写全文并负责提交；文献线程按 Release `literature` 的 Markdown 重写第 2 节和参考文献；评审线程对照 11 篇 *Morphology* 文章审了四轮，第四轮认为可以定稿。过程与评价见 `v7_evaluation.md`。

v8（2026-09-30）由主稿线程据扩大盲编的结果修订 v7：数据线程另在 `youwen/ext_coding/` 做编码和分析（PR #4，编码前先提交分析计划），评审线程独立复核数字并提出修订清单，作者核验由 Qu 交回。§2.1–§2.3 与参考文献没有变。v8 还待评审线程复核。过程见 `v8_evaluation.md`。

### 论文还缺什么

详见 [`v8_evaluation.md`](youwen/manuscript/v8_evaluation.md) 第 5 节，要点：

- **待 Qu 决定**：是否放宽 5,000–7,000 词的上限（v8 按拉丁字母词计为 6,987 词，正文另有汉字 263 个）；是否补充参考文献（现 37 条，11 篇 *Morphology* 文章的中位数约 80 条）；*Morphology* 的 SSCI 收录；数据存档用 Zenodo 还是 OSF。
- **已完成**：扩大盲编，用来区分“意义先行”与“同词或最小派生”两种解释（Qu 2026-09-30 决定做）。结果支持“同词或最小派生”，程度中等，已写进 v8 的 §3.3、§4.3、表 5、§5.2、§6 和摘要。**待评审线程复核 v8。**
- 作者单位、基金和利益冲突等投稿声明仍需补全。
- 编码的写法按 Qu 2026-09-30 的决定：以两份机器编码表为编码记录（盲编一轮用于分析，建库时的第一轮作对照），两位作者的独立编码与盲编逐项一致，作为核验；个人工作表未保存。κ = 0.773 是两次机器编码之间的一致度，不能称为人工编码者信度。
- 扩大盲编（`youwen/ext_coding/`）的 677 条新条目由两次独立盲编，κ = 0.817，同样是机器之间的一致度；主检验用第一次盲编（OR 2.35）。Qu 交回的核验表（126 条）是两位作者一起填的一份联合判断，表上看得到两次盲编的编码，只作核验和敏感性分析（改判后 OR 2.73），不是独立的人工编码，也不能据此算作者间信度。全文写“pre-specified”，不写“preregistered”（分析计划在编码前提交并有时间戳，但没有在外部平台登记）。
- 书目里仍标 † 的只剩 A11（王筠《说文释例》的版本）和论文没有引用的 E4–E6，投稿前核实。
- 分析集 212 条中的 104 条已对照早稻田所藏陈昌治 1873 年刻本扫描作定点抽核；抽核并非随机，余下 108 条未核，按 Qu 的决定已停止。䢈、𨻺 两处差异未解决。

## 主要结论（v8）

- 分析集：大徐本 227 条亦声字头，去掉 4 条"亦"本身作声符的误检和 11 条新附，得 212 条，分布在 172 个声符上；对照组是同声符的 953 个普通形声字。
- 亦声字与声符字更常同音（H1a，GEE OR 2.38，声符内 2.15），更常是去声 \*-s 交替（H1c 第一步 OR 2.42）；其他声调、清浊交替不富集，上古其他词缀（H1b）也没有证据。语义上远更常相关（H2：首批样本 25/33 对 6/50，OR 22.0；扩大编码 141/172 对 79/462，OR 21.6 [13.3, 35.0]）。
- 标注不带可检测的方向信息：涉及去声时，亦声字与普通字是去声一方的比例相近（76% 对 74%，条件 OR 1.11，区间宽）。形声字本身偏向去声一方（75%），但读音另有差异的字对也有 61%，所以字形只是偏向派生读法，不能确立方向。
- 梯度（v7 新做的组合检验）：读音效应主要由仅见于大徐本的标注和以声符释字的条目承担。在两本共有、释义不用声符的 92 对里，语义对比仍大（OR 16.1），同音对比变弱（GEE 1.59 [0.97, 2.61]，声符内 1.22）。v1–v6 报告的单项检验都仍成立。
- 结论：亦声是词汇相关性的证据，这种相关在同音与 \*-s 字对中最密；它不是有方向的派生标记。扩大盲编回答了“意义先行”与“同词或最小派生”哪个更合：在语义相关的字对里，亦声对仍比普通对更常同音或去声交替（H5：73/141 对 23/79，OR 2.35 [1.43, 3.86]，单侧 p = 0.0004；编码前写定的判读规则判为支持“同词或最小派生”）。程度中等：声符内 MH 2.01 [0.75, 5.39] 不精确，两本共有且无声训的核心层 1.80 [0.95, 3.42] 只是边缘可见（探索性）；作者核验后 2.73（敏感性分析）。这不等于“意义先行”被否定：只要按释义编码的相关性系统低估了许慎对同音字对的判断，它仍能成立。
- 王筠《说文释例》卷三已说亦声有三种，第三种是"分別文之在本部者"。本文的贡献是第一次在全体亦声字上、控制语音后检验他的说法，不能说成王筠把亦声等同于分别文。归本部者并不更常同音；他否定的九条，有七条落在与其余标注相同的读音关系上。
- 与小徐本对照：140 条两本都作亦声，62 条只有大徐作亦声（可能是大徐增，也可能是小徐脱），10 条无从判断。

## 目录说明

```
youwen/
├── manuscript/            论文稿 v1–v8（.md 为主，.docx 为 Word 版）、v6 来源记录和核数脚本、v7 与 v8 的数字出处、评价、计划与评审报告
├── ext_coding/            扩大盲编：分析计划（编码前提交）、抽样与分析脚本、14 批提示与原始回答、两次盲编表、结果、作者核验表
├── literature_review.md   英文文献综述
├── literature_review_access_log.md   哪些文献读了全文、哪些只读了摘要
├── bibliography.md        注释书目
├── topic_and_journal.md   选题比较和期刊比较（选题已定：问题二；期刊 2026-09-29 改为 Morphology，见本文件开头）
├── outline.md             论文大纲 v0.1（已被论文稿取代，只作参考）
├── outline_support/       大纲里探索性数字的核对脚本和亦声字排除清单
├── youwen_criteria.md     数据说明、编码方案、判定标准和各轮结果
├── scripts/               数据抽取、编码和统计脚本（见下文"怎样重跑"）
├── shili_pages/           王筠《说文释例》卷三、卷八的书页图像和录文
├── sources/               《说文释例》卷八的国图扫描 PDF、Karlgren《Word families in Chinese》扫描 PDF（BMFEA 5，1933）
└── *.csv / *.tsv / *.xlsx 数据和结果（见下表）
```

### 数据和结果文件

| 文件 | 内容 |
|---|---|
| `yisheng_dataset.csv` | 主数据集：亦声字和同声符普通形声字，含中古音、上古音（Baxter–Sagart 2014）、语音关系、是否新附、是否进入分析集（`in_analysis_set`）等 |
| `yisheng_summary.csv` | 各假设的描述统计和 Fisher 检验 |
| `yisheng_models.csv` | 原分析输出含 GLMM（变分贝叶斯近似）与按声符聚类的 GEE；v6 正文主要报告 GEE，Holm 校正 |
| `yisheng_models_wangyun_sensitivity.csv` | 敏感性分析：去掉王筠认为是大徐误增的 9（或 10）条后重跑 |
| `yisheng_models_xiaoxu_sensitivity.csv` | 敏感性分析：只用大小徐两本共有的亦声字，以及 H3（仅大徐 vs 两本共有） |
| `ext_coding/yisheng_models_ext_coding.csv` | 扩大盲编的主检验（P1）、次要检验（S）、探索性检验（X）和描述；脚本 `ext_coding/ext_analysis.py`；旧值写在 note 列 |
| `ext_coding/yisheng_models_ext_author_check.csv` | 作者核验（126 条的联合判断）替换后重做的检验；脚本 `ext_coding/ext_author_check.py`。一致率与 κ 在 `ext_author_check_output.txt` |
| `ext_coding/` 的其他文件 | `analysis_plan.md`（编码前提交）、`ext_sample.py`、`prompts/` 与 `raw/`（每批的提示和编码代理的原始回答）、`blind_coding_extended_pass1.xlsx`/`pass2.xlsx`（两次盲编表，不显示组别）、`ext_check_sheet_author_filled.xlsx`（Qu 交回的核验表，原样保存）、`ext_kappa_output.txt`、`ext_summary.md` |
| `yisheng_models_v7_checks.csv` | v7 补充检验（`scripts/yisheng_v7_checks.py`）：中古四分剖面、声符内 MH、方向的条件 OR 与基线、组合检验、相关对内的比较、段注计数、盲编样本的抽样框等；口径见 `youwen_criteria.md` §9。不改任何既有数据或正式计数 |
| `yisheng_daxu_xiaoxu.csv` | 小徐本对照第一轮：按说解自动对齐（70 条可靠） |
| `yisheng_xiaoxu_round2_reads.tsv` | 第二轮：在四部丛刊本电子文本里逐条人工核读 |
| `yisheng_xiaoxu_round3_scan_reads.tsv` | 第三轮：电子本缺文的 56 条，在国图扫描的四部丛刊本上核读 |
| `yisheng_xiaoxu_collation_final.csv` | 小徐本对照最终结果（`layer` 列：both 140 / daxu_only 62 / unknown 10） |
| `yisheng_xiaoxu_gap_pages.csv` | 电子本缺文条目在四部丛刊本中的页码 |
| `blind_coding_sheet.xlsx` | 100 条语义关系盲编码表（不显示是否亦声） |
| `blind_coding_sheet_llm_coded.xlsx` | 盲编一轮（另一个 Claude 实例，看不到标注），v6、v7、v8 的语义分析都用它（v8 里它是首批 100 条的盲编）；两位作者后来独立编码，与它逐项一致，作为核验（Qu 2026-09-30 决定以两份机器编码表为编码记录），见编码来源说明 |
| `yisheng_claude_codes.csv` | 第一轮编码（建库的 Claude 实例，编码时知道组别），只作对照 |
| `blind_coding_llm_protocol.md`、`blind_coding_kappa_output.txt` | 第二编码的做法和 κ 结果 |
| `youwen_pilot.csv`、`youwen_series_summary.csv`、`youwen_layer2_later_chars.csv`、`blind_coding_sheet_youwen_old.xlsx` | 早期"右文"试点（15 个声符系列），只作背景 |

CSV 都是 UTF-8 带 BOM（`utf-8-sig`），用 Excel 直接打开不会乱码。

## 原书扫描

大文件没有放进仓库，放在本仓库的 [Releases](https://github.com/WuYusen825/Morphology/releases) 里：

| 位置 | 内容 | 能否使用 |
|---|---|---|
| Release `book1` | 王筠《说文释例》卷三，国家图书馆扫描（archive.org 条目 `02076570.cn`） | 可用 |
| `youwen/sources/shuowen_shili_juan08_NLC_02076575.cn.pdf` | 《说文释例》卷八，国家图书馆扫描（archive.org 条目 `02076575.cn`） | 可用 |
| `youwen/sources/karlgren_word_families_BMFEA05_archive_Bulletin477728.pdf` | Karlgren, Word Families in Chinese（BMFEA 5，第 9–120 页，附书名页和目录），远东古物博物馆自传 archive.org 条目 `Bulletin477728`，CC0 | 可用 |
| Release `说文解字` | 四部丛刊本《說文繫傳通釋》，国家图书馆扫描；小徐本对照第三轮用的就是它 | 可用 |
| Release `book` | Z-Library 来源的《说文释例》PDF | **不要使用**，建议删除这个 Release |
| Release `book3` | 《说文解字繫传》现代影印本，PDF 元数据显示来自 Z-Library，且有版权页 | **不要使用**，建议删除这个 Release |
| Release `book2` | 《贞观政要》，传错了书 | 与本项目无关 |
| Release `literature` | 参考文献 PDF 与分页 Markdown（Codex 整理，见 `PROJECT_LOG.md` 2026-09-28 条目与上传清单） | 可用；使用前仍须核对原页 |
| Release `学习` | 11 篇 *Morphology* 2026 研究文章（10 篇开放获取，1 篇订阅文章），用于学习 Discussion 写法，也是 v7、v8 的水平参照 | 可用；其中 Barbu Mititelu 等、Ševčíková & Hledíková 两篇被 v7 引用（书目 E14、E15） |

## 外部数据来源

脚本从这些公开仓库读取原始数据（运行时临时下载，不放进本仓库）：

- [shuowenjiezi/shuowen](https://github.com/shuowenjiezi/shuowen)：大徐本《说文》说解和段注（JSON）
- [nk2028/tshet-uinh-examples](https://github.com/nk2028/tshet-uinh-examples)（依赖 `tshet-uinh`）：《广韵》中古音和 Baxter 中古音转写
- [digling/cddb](https://github.com/digling/cddb)：Baxter–Sagart 2014 上古音和 Schuessler 2007（GPL-3.0）
- [kanripo/KR1j0019](https://github.com/kanripo/KR1j0019)：四部丛刊本《说文解字繫传》电子文本（小徐本）
- [cjkvi/cjkvi-ids](https://github.com/cjkvi/cjkvi-ids)：只有 `layer2.py`（后起字层）需要

## 怎样重跑

需要 Python 3、Node.js 和 git。下面这组命令在 2026-09-26 从头跑过一遍，所有输出文件与仓库里的逐字节一致；跑完后 `git status` 应当看不到数据文件有改动（下载的仓库和中间文件已写进 `.gitignore`）。

```bash
pip install -r requirements.txt

cd youwen/scripts
git clone --depth 1 https://github.com/shuowenjiezi/shuowen
git clone --depth 1 https://github.com/digling/cddb
git clone --depth 1 https://github.com/kanripo/KR1j0019
git clone --depth 1 https://github.com/nk2028/tshet-uinh-examples
cp mc2.mjs tshet-uinh-examples/
(cd tshet-uinh-examples && npm install && npm run build)

python3 load.py                       # → sw.pkl（大徐本说文）
python3 extract.py                    # → rows.json（右文试点）
python3 add_oc.py cddb                # 给 rows.json 加上古音
python3 baseline.py                   # → stats.json
python3 build_csv.py ..               # → youwen_pilot.csv
python3 summary.py ..                 # → youwen_series_summary.csv
python3 xiaoxu_align.py .. KR1j0019   # → yisheng_daxu_xiaoxu.csv
python3 yisheng.py .. cddb            # → yisheng_dataset.csv 和 yisheng_rows.json
(cd .. && python3 scripts/xiaoxu_merge.py)   # → yisheng_xiaoxu_collation_final.csv
python3 yisheng_stats.py .. --models  # → yisheng_summary.csv、yisheng_models.csv
python3 wangyun_sensitivity.py .. ../blind_coding_sheet_llm_coded.xlsx ../yisheng_claude_codes.csv
python3 xiaoxu_sensitivity.py .. ../blind_coding_sheet_llm_coded.xlsx ../yisheng_claude_codes.csv ../yisheng_xiaoxu_collation_final.csv
python3 kappa.py ../blind_coding_sheet_llm_coded.xlsx ../yisheng_claude_codes.csv --exclude 娶婚仲
python3 yisheng_v7_checks.py .. shuowen/data   # → yisheng_models_v7_checks.csv（v7 补充检验）
```

扩大盲编的分析在仓库根目录运行（读 `youwen/ext_coding/raw/` 里的原始回答，重写结果文件；数据线程重跑时与已提交的文件逐格相同）：

```bash
python3 youwen/ext_coding/ext_analysis.py        # → 两次盲编表、ext_codes_long.csv、yisheng_models_ext_coding.csv、ext_kappa_output.txt、作者核验表
python3 youwen/ext_coding/ext_author_check.py    # → ext_author_check_output.txt、yisheng_models_ext_author_check.csv
```

注意：

- 脚本要在 `youwen/scripts/` 里运行，它们在当前目录读写中间文件（`sw.pkl`、`rows.json`、`yisheng_rows.json` 等），参数 `..` 是输出目录 `youwen/`。
- **不要运行 `blind_sheet.py` 和 `blind_sheet_yisheng.py` 并把输出目录设为 `..`**：两者都会覆盖 `blind_coding_sheet.xlsx`，而已完成的盲编码是按现在这张表做的。
- `youwen/manuscript/manuscript_checks.py` 和 `scripts/xiaoxu_gap_pages.py` 里写死了原共享文件夹的路径（`/mnt/project-files/youwen/…` 或 `/home/claude/Morphology/youwen/…`）。在本仓库运行前，把这些路径改成 `youwen/…`（从仓库根目录运行）。`manuscript_checks.py` 改路径后的输出与 `manuscript_checks_output.txt` 一致。
- **不要重跑 `ext_coding/ext_sample.py` 并提交它的输出**：条目表 `ext_items_key.csv` 和 14 批提示在编码时已经固定，编码是按它们做的。
- 大纲的探索性数字：`python3 youwen/outline_support/exploratory_checks.py youwen/yisheng_dataset.csv youwen/scripts/shuowen/data`。
- 人工编码写在脚本里：右文试点在 `coding.py`，亦声 100 条在 `coding_yisheng.py`，同音字对的关系类型在 `relation_types.py`。改了这些要重跑后面的步骤。
- Word 版论文用 pandoc 从 Markdown 转出，套用 v6 的 Word 样式：在 `youwen/manuscript/` 下运行 `pandoc yisheng_paper_v8.md -o yisheng_paper_v8.docx --reference-doc=yisheng_paper_v6.docx`。云端会话里 LibreOffice 转换会失败，可用 python-docx 检查表格数和 𠔁、𨻺、䢈 等扩展区汉字。

## 分支

目前的默认分支是 `claude/project-thread-lj0ffs`（最早建的数据分支）。论文分支（PR #1）和文献综述分支已经并进本次整理的分支，合并本次的 PR 后，默认分支上就有全部内容。

## 用 Codex 或其他 AI 助手

仓库根目录的 [`AGENTS.md`](AGENTS.md) 写了共同工作规则（改稿怎么存版本、哪些说法论文里不能写、哪些文件不能重新生成等）；[`CLAUDE.md`](CLAUDE.md) 是 Claude Code 的入口。两者修改项目内容前都应同步分支并读 [`PROJECT_LOG.md`](PROJECT_LOG.md) 的最近条目，修改后在同一次提交中追加记录。助手的私有记忆不能替代当前仓库文件。
