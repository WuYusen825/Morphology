import json,csv,coding,math,sys,os
st=json.load(open('stats.json')); R=json.load(open('rows.json'))
for o in st:
    s=o['series']; core,src,alt,_=coding.CORE[s]; o['claimed_core']=core; o['alt_core']=alt
    codes=[coding.C[s][r['char']][1].replace('alt:','') for r in R if r['series']==s and coding.C[s][r['char']][0] not in('X','H')]
    o['alt_Y']=codes.count('Y') if alt else ''; o['alt_E']=codes.count('E') if alt else ''
F=['group','series','claimed_core','n_members','n_X_excluded','Y','E','N','strict_rate_Y','loose_rate_YE','keywords','kw_hits','kw_rate','baseline_rate','fisher_p_one_sided','alt_core','alt_Y','alt_E']
def lchoose(n,k): return math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1)
def fisher(a,b,c,d):
    n1=a+b;K=a+c;N=a+b+c+d
    return sum(math.exp(lchoose(K,x)+lchoose(N-K,n1-x)-lchoose(N,n1)) for x in range(a,min(n1,K)+1))
pool={}
for g in('youwen','control'):
    G=[o for o in st if o['group']==g]; n=sum(o['n_members'] for o in G); y=sum(o['Y'] for o in G); e=sum(o['E'] for o in G)
    pool[g]=(n,y,e)
(n1,y1,e1),(n0,y0,e0)=pool['youwen'],pool['control']
rows=[{k:o[k] for k in F} for o in st]
for g,(n,y,e) in pool.items():
    rows.append({'group':g,'series':'POOLED','n_members':n,'Y':y,'E':e,'N':n-y-e,'strict_rate_Y':round(y/n,3),'loose_rate_YE':round((y+e)/n,3)})
rows.append({'group':'youwen_vs_control','series':'FISHER_one_sided','strict_rate_Y':'%.2g'%fisher(y1,n1-y1,y0,n0-y0),'loose_rate_YE':'%.2g'%fisher(y1+e1,n1-y1-e1,y0+e0,n0-y0-e0)})
with open(os.path.join(sys.argv[1],'youwen_series_summary.csv'),'w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=F);w.writeheader();w.writerows(rows)
for r in rows[-3:]: print(r)
