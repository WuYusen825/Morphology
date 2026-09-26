# 给 AI 助手（Codex 等）的工作规则

项目简介、目录和重跑步骤见 [`README.md`](README.md)。下面是在这个仓库里工作时必须遵守的规则。

## 跨助手同步：每次修改前后

- 开始修改论文、书目、数据、脚本或项目规则前，先同步正在工作的 GitHub 分支，阅读本文件、`README.md`、[`PROJECT_LOG.md`](PROJECT_LOG.md) 的最近条目，并打开将要修改的现行权威文件。不要只凭 Codex 或 Claude 各自的私有记忆判断现状。
- 以用户当前要求和已核实的仓库文件为准；如果私有记忆与仓库记录不一致，先查 Git 历史和实际文件，再更新记忆。尤其要核实 README 指定的当前论文版本，不能从旧稿或旧日志推断。
- 每次修改上述项目内容或形成会影响后续工作的决定后，在同一次提交中向 `PROJECT_LOG.md` **追加**条目，写清日期、执行者、修改文件、原因、验证结果和权威版本是否变化。数据口径的细节仍须写入 `youwen/youwen_criteria.md`，文献阅读程度仍须写入 `youwen/literature_review_access_log.md`。
- Claude Code 的入口文件是 [`CLAUDE.md`](CLAUDE.md)；它指向同一套共享规则和日志。Codex 的本地 `.codex/project-memory/` 只是辅助索引，不能代替 GitHub 上的共享日志。

## 沟通

- 用中文和 Qu 交流。论文正文用英文写（目标期刊是英文刊），除非 Qu 另有要求。

## 改论文稿

- 当前稿是 `youwen/manuscript/yisheng_paper_v6.md`。有实质改动时另存为下一个版本号（`yisheng_paper_v7.md`），不要覆盖旧稿；需要 Word 版时用 pandoc 从 .md 转出同名 .docx。
- 正文 5,000–7,000 词（不含参考文献和表格）。
- 写作风格（Qu 的要求）：详略得当；各节、各段长短不要一样，按重要性分配；段落结构和句式要有变化。
- 论文里的数字必须来自 `youwen/` 下的结果文件（`yisheng_summary.csv`、`yisheng_models*.csv`、`yisheng_xiaoxu_collation_final.csv`、`blind_coding_kappa_output.txt`）或 `manuscript_checks_output.txt`，不要手算后直接写进稿子。

## 论文里不能写错的几点

- **王筠**：《说文释例》卷三说亦声"凡三種"，第三种是"分別文之在本部者"。不能写成王筠把亦声等同于分别文。本文的贡献是对他的说法做第一次全体、控制语音的检验。
- 王筠认为大徐误增的 9 条（貧 愾 恇 娶 婚 姻 婢 緉 坪）不能当作他认可的亦声例；卷三里他认可的是 禮 祏 胖 柵；卷八引 傾 𨻺 䫇 的亦声而未加反驳。原文与叶次见 `youwen/shili_pages/README.md`。
- **语义编码的一致度**（κ = 0.773）是历史两次 LLM 编码之间的一致度，不能称为人工编码者信度。2026-09-27 两位作者已确认独立盲编 100 条且结果一致，并复核 196 个同音关系类型；原始个人记录未保存，最终值沿用历史文件。详见 `youwen/manuscript/coding_provenance_v6.md`。论文仍须有 AI 使用声明。
- 小徐本对照以 `yisheng_xiaoxu_collation_final.csv` 为准（140 两本共有 / 62 仅大徐 / 10 无从判断）；更早的中间数字（100/48/64 等）已作废。
- 计数口径：227 条是大徐本亦声字头原始数，212 条（172 个声符）是分析集。

## 数据和脚本

- 不要手改 CSV/TSV/XLSX 数据文件。要改数据，改生成它的脚本或脚本里的编码字典（`coding.py`、`coding_yisheng.py`、`relation_types.py`），再按 README 的步骤重跑，并在 `youwen/youwen_criteria.md` 里记一笔改了什么、为什么。
- 不要把 `blind_sheet.py` 或 `blind_sheet_yisheng.py` 的输出目录设为 `youwen/`：两者都会覆盖已完成编码的 `blind_coding_sheet.xlsx`。
- 下载的外部仓库（shuowen、cddb、KR1j0019、tshet-uinh-examples、cjkvi-ids）和中间文件不要提交，`.gitignore` 已经排除。
- 改了分析脚本后，按 README 的"怎样重跑"跑一遍，再用 `git diff --stat` 看哪些结果文件变了，把变化告诉 Qu。

## 资料来源

- 只用合法公开的来源。不要使用、下载或提交影子图书馆（Z-Library、1lib 等）的文件；Release `book` 和 `book3` 就是这类文件，不要打开。
- 新的扫描 PDF 在使用前先查元数据（`pdfinfo` 的 Creator/Producer），确认书名和来源。
- 只读了摘要的文献，要在 `youwen/literature_review_access_log.md` 里注明。
