# 盲编码第二编码人：独立 LLM 子代理（2026-09-25）

2026-09-25 Qu 在线程中要求"你帮qu完成""用一个subagent"。所以第二编码人**不是人**，而是一个独立的 Claude 子代理（general-purpose 类型）。论文中应报告为"两次独立的 LLM 编码之间的一致性"，不能报告为人工编码人间信度。

## 子代理看到了什么，没看到什么
- **看到的**：下面的编码说明，加上 100 条条目的文本（条目号、声符字及其《说文》释义、成员字及其释义），即 `blind_coding_sheet.xlsx` 第 1 至 5 列的内容，直接写在提示里。释义已去掉"从某某声/亦声"的结构分析。
- **没看到的**：任何文件都没有给它，并明令禁止它读盘或上网。所以它没有看到亦声标签、`yisheng_dataset.csv`、`yisheng_claude_codes.csv`、`coding_yisheng.py`、outline.md 或其他线程的文件。它只调用了 1 次工具，就是返回答案。
- **与第一编码人的关系**：第一编码人（Claude 本线程）编码时知道组别，不是盲编的。子代理与第一编码人不共享任何上下文，但两者是同一个模型家族，所以错误可能相关，κ 可能偏高。
- **结果文件**：子代理的编码写入 `blind_coding_sheet_llm_coded.xlsx`（原空白表 `blind_coding_sheet.xlsx` 保持不变）。

## 给子代理的编码说明（原文，英文）
> Code 100 character pairs from the Shuowen glosses given below. […] Use ONLY the glosses in this prompt and your own knowledge of classical Chinese and the Shuowen. Do NOT read, search or open any file on disk, and do NOT use any web or search tool. […] Do NOT try to recall or check whether Xu Shen analyses the member character as 某聲, 某亦聲 or 會意.
>
> For each item, compare the 本义 of the member character with the 本义 of the phonetic character. Pick one code:
> Y: the same or near-synonymous meaning (厓 山邊也 / 涯 水邊也). E: connected only through one step of extension or inference (亡 逃也 / 忘 不識也). N: no semantic relation is visible. X: the member character is a proper name (place, river, surname, named plant or animal).
>
> Judge by 本义 only, not later or loan meanings. Where a gloss is "None", judge from your knowledge of that character's Shuowen 本义, with confidence 1 unless sure. A pun-style gloss (e.g. 狗 "叩也") is not evidence of a real semantic relation by itself. Confidence 1–3; a note of ≤15 characters. When unsure between two codes, prefer E over Y and N over E.
>
> Output exactly 100 lines: item, code, confidence, note (tab-separated).

说明中的两个例子（厓/涯、亡/忘）本身就是样本中的条目，因为它们原样来自表中的"说明"页，Qu 也会看到同样的例子。计算 κ 时两例都保留。

## 结果（`scripts/kappa.py blind_coding_sheet_llm_coded.xlsx yisheng_claude_codes.csv --exclude …`）
| 口径 | n | 四类 κ（一致率） | Y/非Y κ（一致率） |
|---|---|---|---|
| 全部 | 100 | 0.773（86.0%） | 0.684（93.0%） |
| 剔除 outline 初版中可能暴露的 3 条 | 97 | 0.760（85.6%） | 0.631（92.8%） |
| 剔除新附和误收 5 条 | 95 | 0.776 | — |

- 分歧共 14 条：Claude 记 Y、子代理记 E 的 6 条；Claude 记 N、子代理记 X 的 4 条；Claude 记 E、子代理记 N 的 3 条；Claude 记 Y、子代理记 X 的 1 条。没有 Y 与 N 直接对立的情况。子代理整体更保守，这符合它得到的"拿不准时取保守"的指示。
- 按组看，κ 在亦声组为 0.704（n = 40），普通组为 0.749（n = 60）。
- Y+E 占可判定条目的比例：子代理为亦声 28/38、普通 6/51；Claude 为亦声 30/40、普通 8/54。第一编码人非盲，但盲编的子代理得出的组间差异同样悬殊。
- 严口径（Y/非Y）的 κ 低于常用的 0.70 门槛。论文宜以四类 κ 为主，或者把 Y 与 E 合并为"有语义关系"来报告。
