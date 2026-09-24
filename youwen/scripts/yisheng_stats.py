import json,math,csv,sys,os,collections
R=json.load(open('yisheng_rows.json'))
def lc(n,k): return math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1)
def fisher(a,b,c,d):
    n1=a+b;K=a+c;N=a+b+c+d
    return sum(math.exp(lc(K,x)+lc(N-K,n1-x)-lc(N,n1)) for x in range(a,min(n1,K)+1))
out=[]
def row(label,L1,L0):
    a=sum(r['morph_relation_auto'] in ('I','R') for r in L1); c=sum(r['morph_relation_auto'] in ('I','R') for r in L0)
    out.append(dict(comparison=label,yisheng_n=len(L1),yisheng_regular=a,yisheng_rate=round(a/len(L1),3),ordinary_n=len(L0),ordinary_regular=c,ordinary_rate=round(c/len(L0),3),fisher_one_sided='%.2g'%fisher(a,len(L1)-a,c,len(L0)-c)))
ok=[r for r in R if r['morph_relation_auto']!='NA']
row('all phonetics',[r for r in ok if r['relation']=='亦聲'],[r for r in ok if r['relation']=='聲'])
ph={r['phonetic'] for r in ok if r['relation']=='亦聲'}&{r['phonetic'] for r in ok if r['relation']=='聲'}
row(f'matched phonetics (n={len(ph)})',[r for r in ok if r['relation']=='亦聲' and r['phonetic'] in ph],[r for r in ok if r['relation']=='聲' and r['phonetic'] in ph])
with open(os.path.join(sys.argv[1],'yisheng_summary.csv'),'w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
    f.write('\ncategory counts (relation,category,n)\n')
    for (a,b),n in sorted(collections.Counter((r['relation'],r['morph_relation_auto']) for r in R).items()): f.write(f'{a},{b},{n}\n')
for o in out: print(o)
