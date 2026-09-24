# 复现步骤
1. `git clone https://github.com/shuowenjiezi/shuowen` ；`git clone https://github.com/nk2028/tshet-uinh-examples && cd tshet-uinh-examples && npm install && npm run build`，把 `mc2.mjs` 放进该目录。
2. `python3 load.py` → `sw.pkl`
3. `python3 extract.py` → `rows.json`（抽取系列成员、段注、广韵音、BS 中古音）；然后过滤掉以声符为部首但另有他声的字（见 build 过程）。
4. `python3 baseline.py` → `stats.json`；`python3 build_csv.py <outdir>` → `youwen_pilot.csv`
5. 人工编码在 `coding.py` 中（C 字典），修改后重跑 4 即可。
