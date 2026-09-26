# 给 AI 助手（Codex 等）的工作规则

项目简介、目录和重跑步骤见 [`README.md`](README.md)。下面是在这个仓库里工作时必须遵守的规则。

## 沟通

- 用中文和 Qu 交流。论文正文用英文写（目标期刊是英文刊），除非 Qu 另有要求。

## 改论文稿

- 当前稿是 `youwen/manuscript/yisheng_paper_v5.md`。有实质改动时另存为下一个版本号（`yisheng_paper_v6.md`），不要覆盖旧稿；需要 Word 版时用 pandoc 从 .md 转出同名 .docx。
- 正文 5,000–7,000 词（不含参考文献和表格）。
- 写作风格（Qu 的要求）：详略得当；各节、各段长短不要一样，按重要性分配；段落结构和句式要有变化。
- 论文里的数字必须来自 `youwen/` 下的结果文件（`yisheng_summary.csv`、`yisheng_models*.csv`、`yisheng_xiaoxu_collation_final.csv`、`blind_coding_kappa_output.txt`）或 `manuscript_checks_output.txt`，不要手算后直接写进稿子。

## 论文里不能写错的几点

- **王筠**：《说文释例》卷三说亦声"凡三種"，第三种是"分別文之在本部者"。不能写成王筠把亦声等同于分别文。本文的贡献是对他的说法做第一次全体、控制语音的检验。
- 王筠认为大徐误增的 9 条（貧 愾 恇 娶 婚 姻 婢 緉 坪）不能当作他认可的亦声例；卷三里他认可的是 禮 祏 胖 柵；卷八引 傾 𨻺 䫇 的亦声而未加反驳。原文与叶次见 `youwen/shili_pages/README.md`。
- **语义编码的一致度**（κ = 0.773）是两次 LLM 编码之间的一致度，不能称为人工编码者信度；论文要有 AI 使用声明。
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
