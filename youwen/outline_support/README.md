# outline_support/

**致 Qu：本文件夹逐字列出了亦声字，请在交回盲编码表之后再打开。**

This folder holds the topic thread's exploratory checks behind the numbers in `../outline.md`. The dataset and the confirmatory statistics belong to the pilot thread.

- `exploratory_checks.py`: reproduces every exploratory number in the outline.
  - Usage: `python3 exploratory_checks.py ../yisheng_dataset.csv <shuowenjiezi/shuowen>/data`
- `exploratory_checks_output.txt`: the output of the last run, 2026-09-24.

## Exclusions (outline §3.1)

**String false hits (4).** In these entries 亦 is itself the phonetic, as in 从巾，亦聲. They are ordinary compounds on the phonetic 亦, not *yìshēng* labels:
帟, 奕, 弈, 迹 (帟 is also 新附)

**Xu Xuan's 新附 (11 more):**
晬, 涯, 僦, 儈, 低, 魑, 腔, 赩, 債, 價, 謎

**How 新附 were found.** They are taken as the trailing run of entries without Duan text at the end of each radical. This rule finds 398 entries across the whole book, which is close to the roughly 400 新附 usually counted. Every flag must be checked against the 1963 Zhonghua facsimile.

**Not excluded:**
- 否 is genuine. It is last in 不部 and has no Duan text in the data, but Duan keeps it under 不. His note on the duplicate entry under 口 says 否字見不部。此誤增也.
- 𠮱 under 亏 is a duplicate that Xu Xuan himself notes (口部有𠮱，此重出). It stays in for now.

**Five of these excluded items are in the 100-item blind sample:** 債, 價, 涯, 魑, 弈. They still count for κ, but not for the main analysis.

## Labelled departing-tone derivatives (outline §3.5, H1c)

These are pairs that differ only in tone and/or initial voicing, where the 亦聲 character has the departing tone and its phonetic does not:

仲/中 從/从 緉/兩 娶/取 授/受 雊/句 琀/含 鄯/善 憙/喜 妊/壬 字/子 坪/平 腥/星 珥/耳 殯/賓 劑/齊

## Duan layer (outline §4.6)

These lists come from the output file; they are automated and not yet checked by hand.

**Xu only.** Duan's emended text has no 亦聲 for these (42 of 212):
㞣㵞䩡係像劑功否墨奸娣娶媄忘息愾拲整旄昦柵燓琥瓏眇瞑禬舒詔酣鈴阢陷陸黃𠔁𠭥𠮱𢔟𢿳𨻺𨿳

**Duan only (42):**
㔹㽥䏔也仄冥医博叛咢垒塋壹孚屔彤恩戌朻椁櫑漏碬糾絫綴耏膌莫萅葬葻諰閨頛馺鳧鼏𢖽𣦼𤲑𩡩

Seven of the ten items that only Xiǎo Xú labels (see `../yisheng_daxu_xiaoxu.csv`) are among Duan's additions: 莫, 葬, 咢, 彤, 朻, 櫑, 𤲑.
