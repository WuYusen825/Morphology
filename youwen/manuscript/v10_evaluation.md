# v10 评价：按 Morphology 投稿要求排好版的 v9

日期：2026-10-01。对象：[`yisheng_paper_v10.md`](yisheng_paper_v10.md)（Word 版 [`.docx`](yisheng_paper_v10.docx)）、双盲投稿用的匿名版 [`yisheng_paper_v10_anonymised.md`](yisheng_paper_v10_anonymised.md)（[`.docx`](yisheng_paper_v10_anonymised.docx)）、题名页 [`yisheng_v10_title_page.md`](yisheng_v10_title_page.md) 和 cover letter [`yisheng_v10_cover_letter.md`](yisheng_v10_cover_letter.md)；按 Morphology 要求排好的上传文件在 [`submission/`](submission/)。数字出处见 [`yisheng_paper_v10_numbers.md`](yisheng_paper_v10_numbers.md)，对照指南的核对表见 [`submission/SUBMISSION_CHECKLIST.md`](submission/SUBMISSION_CHECKLIST.md)。

依据：Qu 2026-10-01 04:08 在项目聊天里发来两份 PDF（Morphology 的 *Submission guidelines*、Springer Nature 的 *Submit faster on Snapp*）和一句指示：「这一版不必再优化，按morphology投稿要求排版，然后把补充材料安排好即可（包括命名和内部格式，注意英文为主要呈现语言）」。所以 v10 不是新的改稿轮：**内容、数字、表和图的结论都是 v9 的**，v10 只做排版、合规和补充材料的对接。之前 v9 的评价（[`v9_evaluation.md`](v9_evaluation.md)）、评审对 v9 的复核（`v7_work/review/v9_review.md`：没有必须改的）继续有效。

## 0 结论

- **v10 可以交给 Qu 填完个人信息后投稿**，前提是数据线程的补充材料 ESM_1–7 交付并通过一次合规与数字核对（评审线程做）。
- 自查脚本 `youwen/scripts/yisheng_submission_audit.py` 对匿名稿、题名页、cover letter、图和补充材料清单共 100 项检查全部通过、0 项失败（输出在 [`submission/audit_v10_output.txt`](submission/audit_v10_output.txt)）；核对表里按 “满足／不适用／需 Qu／待补充材料” 逐条列了指南的要求。
- 还缺的都是只有 Qu 能给的：通讯作者及邮箱、ORCID、作者贡献、“再用过材料” 与 “编委身份” 的确认；以及补充材料成品。题名页和 cover letter 里以 `[TO BE SUPPLIED: …]` 占位，Word 里高亮显示。

## 1 做了什么

| 项目 | 做法 |
|---|---|
| 文件拆分 | 匿名稿 `Manuscript_anonymised.docx`（上传）；题名页 `Title_page.docx`（不上传，Snapp 的双盲流程要求作者信息和声明在界面里填，它是填写底稿）；`Cover_letter.docx`；图 `Fig1.eps/.tif/.png` |
| 版式 | A4，页边距 25 mm，Times New Roman 11 pt（汉字宋体），1.5 倍行距，标题 13/11/11 pt 粗体且不超过三级，表格 9 pt 三线表、表头加粗、表注用上标小写字母，图题 10 pt，参考文献 10 pt 悬挂缩进，只有自动页码一个域，无脚注、尾注、批注、修订 |
| 正文结构 | 十进制标题；§3.6 新增 “Use of large language models”；文末依次为 Supplementary Information（7 条 caption）、Statements and Declarations（匿名稿里只有 Data availability，见第 3 节第 7 项）、References |
| 图 1 | 重画为 119 mm 宽、8 pt 的 Arial 兼容字体、黑白（靠标记形状和空心/实心区分）、线宽至少 0.6 pt；EPS（字体嵌入）、TIFF、PNG 三份，PNG 为 2811 × 2490 像素、600 dpi；图题用 Springer 的写法 |
| 参考文献 | 按 APA 第 7 版的格式，4 条补了 DOI（Crossref 核对），共 17 条有 DOI；按第一作者姓氏排序（脚本检查） |
| 补充材料 | 正文引用 Online Resource 1–7（首次引用顺序 1–7），列出 7 条 caption，数据可用性声明改为 “Included in the paper or Supplementary Information”，不再出现仓库地址；caption 里的数字已对文件核过 |
| 双盲 | 匿名稿正文、DOCX 内部全部 XML 和属性、图片元数据里没有作者姓名、单位、仓库属主名（脚本逐项查） |
| 英文为主要呈现语言 | 正文、图表标题、题名页、声明、补充材料说明都是英文，汉字只作例证和数据，附拼音或英文释义 |

## 2 对评审 v9 小建议的处理

| 建议 | v10 |
|---|---|
| S1 组内相关率，不用合并的 “55% 对 23%” | **没有做**（Qu 04:08：不再优化）。数字和改法见评审的 `v9_review.md`、`v9_review_extra.py`；Qu 如要，投稿前可并入 |
| S2 §1 说 Wang Yun “counted nothing and compared no sounds”，与 §2.2 矛盾 | 已改：“his test was a filing rule applied to chosen examples, with no baseline of ordinary compounds”；“first population-level test” 前加 “to our knowledge” |
| S3 反方向偏差情景 | **没有做**；数据线程在补充材料 ESM_6、ESM_7 里保留，标明正文没有讨论 |
| S4 DOCX 里的三线表和加粗表头 | 已做（版式） |
| S5 “encoffined/coffined” | 已改，两处统一为 “to lay out the dead in the coffin” |

## 3 我这里看不到、或做了假设的地方

1. **Word 里的实际显示。** 没有 Word，只用 LibreOffice 渲染逐页看过版面。三线表和图在 Word 里应当一样，但请 Qu 打开看一遍。
2. **图的宽度。** 指南按 “大开本 84/174 mm、小开本 119 mm” 分；我没有查到 *Morphology* 的开本，按小开本取 119 mm（高不超过 195 mm）。排版部门可以缩放，不影响审稿。
3. **字体。** 图里用的是 Liberation Sans（与 Arial 度量兼容），没有装 Arial。
4. **补充材料文件本身。** 数据线程仍在建；我只核了 caption 里的数字，没有打开文件。每个文件里写 “作者姓名、通讯作者邮箱” 的指南要求与双盲相冲突，核对表第 8 节建议送审版写 “withheld”，请 Qu 知悉。
5. **第三方数据的许可。** ESM_2 里再分发中古音（tshet-uinh）和上古音（cddb/Baxter–Sagart）数据，许可条款仓库里只记了 *Shuōwén* 数据的 Apache-2.0；请数据线程在 ESM_1 里注明。
6. **语言模型版本。** 方法部分只写了 “Claude (Anthropic)” 和 “Codex (OpenAI)”，没有版本号（各次编码用的模型版本在材料里能否查到，要看数据线程的 `provenance.tsv`）。
7. **声明放在稿件里还是界面里。** Morphology 的指南 PDF 一边说 “Statements and Declarations” 随论文发表，没有声明的稿件会被退回，一边说换用 Snapp 后作者贡献、竞争利益等在界面里填。Springer Nature 的 Snapp 双盲页（我 2026-10-01 抓取原页核对）明确写稿件文件不应含致谢、贡献、竞争利益、伦理和基金声明，也没有提题名页和数据可用性声明。我按 Snapp 页办：匿名稿只留 Data availability，Funding、Competing interests、Ethics 三段和 “Coding” 一段（后者含作者姓名，内容已见 §3.3–3.5）移到题名页，那是在界面里逐项填写的英文底稿。如编辑部要求声明写进稿件，全文版里有现成的，删去 Author contributions 后贴回即可（核对表第 4 节）。

## 4 重新生成

```
python3 youwen/scripts/yisheng_v10_figure.py                       # 图 1：Fig1.png/.eps/.tif
python3 youwen/scripts/yisheng_make_submission_files.py v10        # 匿名稿、题名页、cover letter 及其 DOCX（占位未填时加 --allow-todo）
python3 youwen/scripts/yisheng_submission_audit.py v10             # 对照指南的自查
```

个人信息到手后，在 `yisheng_make_submission_files.py` 顶部填 `CORRESPONDING`、`EMAILS`、`ORCIDS`、`CONTRIBUTIONS`，把 `PRIOR_PUBLICATION_CONFIRMED` 改为 `True`，再把 `yisheng_paper_v10.md` 里的 `⟦AUTHOR-CONTRIBUTIONS⟧` 换成贡献声明，重新生成即可；这些占位消失后自查脚本会报告 “title page and cover letter complete”。
