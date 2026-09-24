# 用法：python3 kappa.py <已填写的 blind_coding_sheet.xlsx> <yisheng_claude_codes.csv>
# （旧版右文表用 youwen_pilot.csv；两份 csv 都有 series/char/code_core 列）
#       可加 --exclude 字1字2…：另报剔除这些成员字后的 κ（敏感性分析，如编码前可能已见过的条目）
# 输出 Cohen's κ（四类 Y/E/N/X；以及严口径 Y vs 非Y）与分歧清单
import sys,csv
from collections import Counter
from openpyxl import load_workbook
EXC=sys.argv[sys.argv.index('--exclude')+1] if '--exclude' in sys.argv else ''
ws=load_workbook(sys.argv[1])['编码']
B={}
for r in ws.iter_rows(min_row=2,values_only=True):
    v=r[5] if len(r)<10 else r[7]   # 亦声表第 6 列、右文表第 8 列
    if v: B[(r[1],r[3])]=str(v).strip().upper()
A={(r['series'],r['char']):r['code_core'] for r in csv.DictReader(open(sys.argv[2],encoding='utf-8-sig'))}
pairs=[(A[k],b) for k,b in B.items() if k in A]
def kappa(p):
    n=len(p); po=sum(a==b for a,b in p)/n
    ca=Counter(a for a,_ in p); cb=Counter(b for _,b in p)
    pe=sum(ca[k]*cb[k] for k in set(ca)|set(cb))/n/n
    return (po-pe)/(1-pe), po
def report(tag,pairs):
    k4,po4=kappa(pairs); k2,po2=kappa([(a=='Y',b=='Y') for a,b in pairs])
    print(f'{tag} n={len(pairs)}  四类 κ={k4:.3f} (一致率 {po4:.1%})  Y/非Y κ={k2:.3f} (一致率 {po2:.1%})')
report('全部',pairs)
if EXC: report('剔除 --exclude 条目',[(A[k],b) for k,b in B.items() if k in A and k[1] not in EXC])
for k,b in B.items():
    if k in A and A[k]!=b: print('分歧',k,'Claude:',A[k],'你:',b)
