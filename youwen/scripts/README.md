# 复现步骤
1. `git clone https://github.com/shuowenjiezi/shuowen` ；`git clone https://github.com/nk2028/tshet-uinh-examples && cd tshet-uinh-examples && npm install && npm run build`，把 `mc2.mjs` 放进该目录。
2. `python3 load.py` → `sw.pkl`
3. `python3 extract.py` → `rows.json`（抽取系列成员、段注、广韵音、BS 中古音）。
4. `python3 baseline.py` → `stats.json`；`python3 build_csv.py <outdir>`；`python3 summary.py <outdir>`；`python3 layer2.py <outdir>`（需 cjkvi-ids）；`python3 blind_sheet.py <outdir>`
6. 盲编码完成后：`python3 kappa.py blind_coding_sheet.xlsx youwen_pilot.csv`
5. 人工编码在 `coding.py` 中（C 字典），修改后重跑 4 即可。
7. 上古音：`git clone https://github.com/digling/cddb`，在 `python3 extract.py` 之后运行 `python3 add_oc.py cddb`，再重跑第 4 步
8. 问题二（亦声）：`python3 yisheng.py <outdir> cddb && python3 yisheng_stats.py <outdir>`
