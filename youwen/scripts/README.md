# 复现步骤
1. `git clone https://github.com/shuowenjiezi/shuowen` ；`git clone https://github.com/nk2028/tshet-uinh-examples && cd tshet-uinh-examples && npm install && npm run build`，把 `mc2.mjs` 放进该目录。
2. `python3 load.py` → `sw.pkl`
3. `python3 extract.py` → `rows.json`（抽取系列成员、段注、广韵音、BS 中古音）。
4. `python3 baseline.py` → `stats.json`；`python3 build_csv.py <outdir>`；`python3 summary.py <outdir>`；`python3 layer2.py <outdir>`（需 cjkvi-ids）；`python3 blind_sheet.py <outdir>`
6. 盲编码完成后：`python3 kappa.py blind_coding_sheet.xlsx youwen_pilot.csv`
5. 人工编码在 `coding.py` 中（C 字典），修改后重跑 4 即可。
7. 上古音：`git clone https://github.com/digling/cddb`，在 `python3 extract.py` 之后运行 `python3 add_oc.py cddb`，再重跑第 4 步
8. 问题二（亦声）：先要有 `<outdir>/yisheng_daxu_xiaoxu.csv`（第 9 步），然后 `python3 yisheng.py <outdir> cddb && python3 yisheng_stats.py <outdir> --models`（`--models` 需 `pip install statsmodels`）。同音字对关系类型在 `relation_types.py`。**不要重跑 `blind_sheet_yisheng.py`**：它读当前的 `yisheng_rows.json`，重跑会改变已发出的盲编码表。
9. 小徐本对照：`git clone https://github.com/kanripo/KR1j0019`；`python3 xiaoxu_align.py <outdir> KR1j0019`
