# v10 数字出处：相对 v9 的改动

日期：2026-10-01。对象：[`yisheng_paper_v10.md`](yisheng_paper_v10.md)（Word 版 [`.docx`](yisheng_paper_v10.docx)）及其匿名投稿版 [`yisheng_paper_v10_anonymised.md`](yisheng_paper_v10_anonymised.md)、题名页 [`yisheng_v10_title_page.md`](yisheng_v10_title_page.md) 和 cover letter [`yisheng_v10_cover_letter.md`](yisheng_v10_cover_letter.md)。

**v10 没有新的结果数字，也没有改动任何已有的数字。** 主检验、判读、表 1–12 和图 1 的数字都与 v9 相同，出处仍见 [`yisheng_paper_v9_numbers.md`](yisheng_paper_v9_numbers.md)（再往前是 [`v8`](yisheng_paper_v8_numbers.md)、[`v7`](yisheng_paper_v7_numbers.md)）。v10 是 v9 按 Morphology 的投稿要求（Springer 的 Submission guidelines 与 Snapp 说明页）排的版，另外顺手改了评审线程 `v9_review.md` 里的 S2、S5。Qu 2026-10-01 04:08 的指示是「这一版不必再优化」，所以评审的 S1（组内相关率）、S3（反方向偏差情景）没有做；S1 的数字和改法见评审线程的 `v7_work/review/v9_review.md` 与 `v9_review_extra.py`，投稿前如 Qu 要改再并入。

## 字数与篇幅（口径同 v9：以空格分隔、含拉丁字母或数字的词）

| 项目 | v10 | v9 | 说明 |
|---|---:|---:|---|
| 正文 §1–§7 | 8,838 词 | 8,614 词 | 多出的 224 词：§3.6（原在 Declarations 里的 “Use of AI tools” 一段，指南要求写进方法部分，约 120 词）和正文里新增的 “Online Resource n” 引用句（约 100 词） |
| 汉字（正文，不含表） | 342 个 | 342 个 | 按同一方法重数，v9 也是 342（v9 数字文件写的是 339，口径略有出入）；汉字只作例证，均有拼音或英文释义 |
| 摘要 | 246 词 | 249 词 | 把 亦聲 两个字各算一词时为 247；把小数点拆开的 \w+ 口径为 252；指南上限 250。为留余量改了两处措辞，意思不变 |
| 表格、表注和图注 | 2,044 词 + 图注 96 词 | 同 | 12 张表、1 幅图 |
| 参考文献 | 37 条 | 37 条 | 4 条补了 DOI，共 17 条有 DOI |
| 关键词 | 6 个 | 7 个 | 指南要求 4–6 个，删去 Metalinguistic evidence |

## 与 v9 的文字差别（全部）

| 位置 | 改动 | 原因 |
|---|---|---|
| 摘要 | “does not account for” 一句和末句各缩一处措辞 | 字数余量 |
| 关键词 | 删去 Metalinguistic evidence | 4–6 个 |
| §1 | “But he counted nothing and compared no sounds.” 改为 “But his test was a filing rule applied to chosen examples, with no baseline of ordinary compounds.”；“its first population-level…test” 前加 “to our knowledge” | 评审 S2：与 §2.2 对 Wang Yun 的说法矛盾 |
| §1、表 5 | 殯的释义统一为 “to lay out the dead in the coffin” | 评审 S5 |
| §4.2、§4.4、§4.6 | 5 处向后引用表 7、8、9、11 改成 “Section 4.3/4.4/4.6” | 指南：表须按数字顺序在正文里首次引用 |
| §3.1、§3.3、§3.4、§3.5、§3.6 | 新增或改写 “Online Resource n” 引用（首次引用顺序 1–7），去掉 “in the repository” | 指南：补充材料须在正文里以 “Online Resource n” 引用 |
| §3.6 | 新增小节 “Use of large language models”（内容即 v9 Declarations 里的 “Use of AI tools”，加两处交叉引用） | 指南：语言模型的使用须写在方法部分 |
| 图 1 | 图注改为 Springer 的形式（**Fig. 1**，数字后和末尾不加标点，写明线条和标记含义）；图重画为 119 mm 宽、8 pt Arial 兼容字体、黑白、EPS/TIFF/PNG | 指南的图件要求 |
| 文末 | 原 “Data availability”（仓库路径）、“Declarations”、“Use of AI tools” 改成 “Supplementary Information”（7 条 caption）与 “Statements and Declarations”：完整版含 Funding、Competing interests、Ethics approval and consent、Coding、Author contributions、Data availability；**匿名稿只留 Data availability**，其余按 Snapp 双盲页（稿件文件不含基金、竞争利益、伦理、贡献、致谢声明）移到题名页，在界面里填 | 指南的标题与内容要求；仓库地址不能出现在匿名稿里；Snapp 的双盲规定 |
| 参考文献 | Baxter & Sagart (1998, 2014)、Sagart (1999)、Schuessler (2007) 补了 DOI（Crossref 2026-10-01 核对） | 指南：有 DOI 一律写成完整链接 |
| 作者单位 | “Beijing Foreign Studies University, School of English and International Studies, Beijing, China” | 指南：机构、（院系）、城市、国家 |
| §3.3、§5.3、§5.4 | “judgement” 4 处统一为 “judgment”（全文其余 12 处已是 “judgment”）；“the released files” 改为 “the supplementary files” | 拼写一致；补充材料不叫 released |

## 补充材料说明里的数字（“Supplementary Information” 一节）

数据线程 2026-10-01 04:30 给出临时清单（ESM_1–7，经协调者转来）；下列数字已逐个对文件核过。

| caption 里的数字 | 出处 |
|---|---|
| 1,333 对 | `youwen/yisheng_dataset.csv` 的行数（223 亦聲 + 1,054 聲 + 39 會意/其他 + 17 省聲） |
| 212 亦声 + 953 普通 = 分析集 | 表 2 |
| 227 条小徐对勘 | `youwen/yisheng_xiaoxu_collation_final.csv` 的行数（212 + 11 新附 + 4 假命中 = 表 2 第一行） |
| 104 条核对登记 | `youwen/manuscript/daxu_spotcheck_v6.csv` 的行数；正文 §3.1 |
| 首批 100 对 | §3.3 |
| 767 对 = 677 新条目 + 90 框内首批条目 | 表 2、§3.4；v9 数字文件 |
| 126 条作者核验 | §3.4；v9 数字文件 |
| 14 条提示 = 7 批 × 2 遍 | `youwen/ext_coding/prompts/`：pass1_b01–b07、pass2_b01–b07 |
| 两份未用的第二次回答 | `youwen/ext_coding/raw/`：pass1_b03、pass1_b06 的 `_second_answer_not_used.txt`；正文 §3.4 |

## 图 1

数字同三个结果文件（`ext_coding/yisheng_models_ext_coding.csv`、`…_author_check.csv`、`…_second_answer.csv`），由 `youwen/scripts/yisheng_v10_figure.py` 读入；脚本断言正文引用的五个值：主检验 2.35 [1.43, 3.86]、作者判断替换 2.73 [1.61, 4.65]、声符内 MH 2.01 [0.75, 5.39]、第二次回答替换 2.39 [1.38, 4.14]、X3 1.80 [0.95, 3.42]。作图用 Python 3 + matplotlib（Liberation Sans，与 Arial 度量兼容）。
