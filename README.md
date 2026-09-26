# 《说文》亦声与派生：训诂学 × 形态学研究论文

这个仓库存放 Qu 的 SSCI 论文项目的全部工作文件：论文稿、数据、脚本、文献综述和原书书页。内容原来放在 Claude 项目的共享文件夹（Library）里，2026-09-26 整体搬到这里，目录结构保持不变（都在 `youwen/` 下）。

- **研究问题**：许慎《说文解字》的"亦声"标注，是不是对派生关系的隐性标记？
- **论文题目**（暂定）：*What does 'also phonetic' mark? The Shuōwén's yìshēng label, homophony and derivation in Old Chinese*
- **目标期刊**：*Language and Linguistics*（中研院语言学研究所），备选 *Journal of Chinese Linguistics*。投稿前须在 mjl.clarivate.com 再核一次 SSCI 收录。
- **论文语言**：英文。

## 现在读哪个文件

| 要看什么 | 文件 |
|---|---|
| 论文当前稿（v6） | [`youwen/manuscript/yisheng_paper_v6.md`](youwen/manuscript/yisheng_paper_v6.md)，Word 版 [`yisheng_paper_v6.docx`](youwen/manuscript/yisheng_paper_v6.docx) |
| v6 大徐本引文核对与编码来源 | [`daxu_source_audit_v6.md`](youwen/manuscript/daxu_source_audit_v6.md)、[`coding_provenance_v6.md`](youwen/manuscript/coding_provenance_v6.md) |
| 文献综述（论文第 2 节的底稿） | [`youwen/literature_review.md`](youwen/literature_review.md) |
| 注释书目（编号 A1–F2，综述和论文都按这个编号引用） | [`youwen/bibliography.md`](youwen/bibliography.md) |
| 数据怎么来的、判定标准、各轮结果 | [`youwen/youwen_criteria.md`](youwen/youwen_criteria.md)（亦声部分在 §6b–§6e） |
| 王筠《说文释例》原文录文与书页 | [`youwen/shili_pages/README.md`](youwen/shili_pages/README.md) |
| Codex / Claude 共同变更日志 | [`PROJECT_LOG.md`](PROJECT_LOG.md)（两者修改项目前先读，修改后追加记录） |
| v5 参考文献 DOI 核对表 | [`youwen/doi_audit_v5.md`](youwen/doi_audit_v5.md) |

v1–v5 是旧稿，只留作对照。以后实质改稿请另存为 v7，不要覆盖 v6。

### 论文还缺什么

- 作者单位、基金和利益冲突等投稿声明仍需补全。
- v6 已写仓库数据链接与 AI 使用声明；投稿前按目标期刊当时的规则复核措辞。
- 两位作者已独立盲编 100 条并一致认同最终值，也复核了 196 个同音关系类型；个人原始工作记录未保存。历史 κ = 0.773 属于两次 LLM 编码，不能称为人工编码者信度。详见编码来源说明。
- 参考文献里标 † 的条目：卷期页码还没在出版社页面核实，投稿前要去掉 †
- v6 的关键例字说解与析形句已对照早稻田所藏陈昌治 1873 年刻本扫描，核对位置见记录；212 条分析集尚未全部逐页对校。1963 年中华书局本为此本缩印，但未直接翻检纸本。

## 主要结论（v6）

- 分析集：大徐本 227 条亦声字头，去掉 4 条"亦"本身作声符的误检和 11 条新附，得 212 条，分布在 172 个声符上；对照组是同声符的 953 个普通形声字。
- 亦声字与声符字更常同音（H1a，OR 2.38），更常是去声 \*-s 的关系（H1c，OR 2.44），语义上也更常相关（H2）；其他词缀（H1b）没有差别。
- 结论：亦声标的是"同一个词或只差 \*-s 的词换了新字形"，不是一般的词缀派生。
- 王筠《说文释例》卷三已说亦声有三种，第三种是"分別文之在本部者"。本文的贡献是第一次在全体亦声字上、控制语音后检验他的说法，不能说成王筠把亦声等同于分别文。
- 与小徐本对照：140 条两本都作亦声，62 条只有大徐作亦声，10 条无从判断。只用两本共有的 140 条，各项结果仍然成立。

## 目录说明

```
youwen/
├── manuscript/            论文稿 v1–v6（.md 为主，.docx 为 Word 版）、v6 来源记录和核数脚本
├── literature_review.md   英文文献综述
├── literature_review_access_log.md   哪些文献读了全文、哪些只读了摘要
├── bibliography.md        注释书目
├── topic_and_journal.md   选题比较和期刊比较（已定：问题二，首投 L&L）
├── outline.md             论文大纲 v0.1（已被论文稿取代，只作参考）
├── outline_support/       大纲里探索性数字的核对脚本和亦声字排除清单
├── youwen_criteria.md     数据说明、编码方案、判定标准和各轮结果
├── scripts/               数据抽取、编码和统计脚本（见下文"怎样重跑"）
├── shili_pages/           王筠《说文释例》卷三、卷八的书页图像和录文
├── sources/               《说文释例》卷八的国图扫描 PDF
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
| `yisheng_daxu_xiaoxu.csv` | 小徐本对照第一轮：按说解自动对齐（70 条可靠） |
| `yisheng_xiaoxu_round2_reads.tsv` | 第二轮：在四部丛刊本电子文本里逐条人工核读 |
| `yisheng_xiaoxu_round3_scan_reads.tsv` | 第三轮：电子本缺文的 56 条，在国图扫描的四部丛刊本上核读 |
| `yisheng_xiaoxu_collation_final.csv` | 小徐本对照最终结果（`layer` 列：both 140 / daxu_only 62 / unknown 10） |
| `yisheng_xiaoxu_gap_pages.csv` | 电子本缺文条目在四部丛刊本中的页码 |
| `blind_coding_sheet.xlsx` | 100 条语义关系盲编码表（不显示是否亦声） |
| `blind_coding_sheet_llm_coded.xlsx` | 历史 LLM 盲编码表；数值与两位作者后来独立盲编、复核后的最终一致编码完全相同，故 v6 沿用该文件，见编码来源说明 |
| `yisheng_claude_codes.csv` | 第一编码（Claude，编码时知道组别） |
| `blind_coding_llm_protocol.md`、`blind_coding_kappa_output.txt` | 第二编码的做法和 κ 结果 |
| `youwen_pilot.csv`、`youwen_series_summary.csv`、`youwen_layer2_later_chars.csv`、`blind_coding_sheet_youwen_old.xlsx` | 早期"右文"试点（15 个声符系列），只作背景 |

CSV 都是 UTF-8 带 BOM（`utf-8-sig`），用 Excel 直接打开不会乱码。

## 原书扫描

大文件没有放进仓库，放在本仓库的 [Releases](https://github.com/WuYusen825/Morphology/releases) 里：

| 位置 | 内容 | 能否使用 |
|---|---|---|
| Release `book1` | 王筠《说文释例》卷三，国家图书馆扫描（archive.org 条目 `02076570.cn`） | 可用 |
| `youwen/sources/shuowen_shili_juan08_NLC_02076575.cn.pdf` | 《说文释例》卷八，国家图书馆扫描（archive.org 条目 `02076575.cn`） | 可用 |
| Release `说文解字` | 四部丛刊本《說文繫傳通釋》，国家图书馆扫描；小徐本对照第三轮用的就是它 | 可用 |
| Release `book` | Z-Library 来源的《说文释例》PDF | **不要使用**，建议删除这个 Release |
| Release `book3` | 《说文解字繫传》现代影印本，PDF 元数据显示来自 Z-Library，且有版权页 | **不要使用**，建议删除这个 Release |
| Release `book2` | 《贞观政要》，传错了书 | 与本项目无关 |

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
```

注意：

- 脚本要在 `youwen/scripts/` 里运行，它们在当前目录读写中间文件（`sw.pkl`、`rows.json`、`yisheng_rows.json` 等），参数 `..` 是输出目录 `youwen/`。
- **不要运行 `blind_sheet.py` 和 `blind_sheet_yisheng.py` 并把输出目录设为 `..`**：两者都会覆盖 `blind_coding_sheet.xlsx`，而已完成的盲编码是按现在这张表做的。
- `youwen/manuscript/manuscript_checks.py` 和 `scripts/xiaoxu_gap_pages.py` 里写死了原共享文件夹的路径（`/mnt/project-files/youwen/…` 或 `/home/claude/Morphology/youwen/…`）。在本仓库运行前，把这些路径改成 `youwen/…`（从仓库根目录运行）。`manuscript_checks.py` 改路径后的输出与 `manuscript_checks_output.txt` 一致。
- 大纲的探索性数字：`python3 youwen/outline_support/exploratory_checks.py youwen/yisheng_dataset.csv youwen/scripts/shuowen/data`。
- 人工编码写在脚本里：右文试点在 `coding.py`，亦声 100 条在 `coding_yisheng.py`，同音字对的关系类型在 `relation_types.py`。改了这些要重跑后面的步骤。
- Word 版论文可以用 pandoc 从 Markdown 转出：`pandoc yisheng_paper_v6.md -o yisheng_paper_v6.docx`。

## 分支

目前的默认分支是 `claude/project-thread-lj0ffs`（最早建的数据分支）。论文分支（PR #1）和文献综述分支已经并进本次整理的分支，合并本次的 PR 后，默认分支上就有全部内容。

## 用 Codex 或其他 AI 助手

仓库根目录的 [`AGENTS.md`](AGENTS.md) 写了共同工作规则（改稿怎么存版本、哪些说法论文里不能写、哪些文件不能重新生成等）；[`CLAUDE.md`](CLAUDE.md) 是 Claude Code 的入口。两者修改项目内容前都应同步分支并读 [`PROJECT_LOG.md`](PROJECT_LOG.md) 的最近条目，修改后在同一次提交中追加记录。助手的私有记忆不能替代当前仓库文件。
