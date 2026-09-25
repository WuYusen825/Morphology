# 电子本缺文条目在四部叢刊本中的页码（2026-09-25）：用 kanripo KR1j0019 的 SBCK 分支（带 <pb:> 页码），取缺文条目前后能定位的条目所在页，缺文就在这两页之间（含两端）。
# 已查明缺文原因：电子本整页或半页漏录（如 008-1b 页码重复三次，幺、𢆶、叀 三部全缺）。用法：在含 sbck/ 与 sw.pkl 的目录运行 → gap_pages.csv
import re,glob,pickle,bisect,csv,json
def norm(s):
    s=re.sub(r'<[^>]*>','',s); s=re.sub(r'&KR\d+;','□',s); s=re.sub(r'\[[^\]]*\]','□',s)
    s=s.replace('從','从').replace('声','聲').replace('�','□')
    return re.sub(r'[\s¶()（）/　，。、；：「」『』“”《》\[\]]','',s)
txt='';PG=[];allpages=[]
for f in sorted(glob.glob('sbck/KR1j0019_0*.txt')):
    n=int(f[-7:-4])
    if not 1<=n<=30: continue
    t=''.join(l for l in open(f,encoding='utf-8') if not l.startswith('#'))
    parts=re.split(r'<pb:KR1j0019_SBCK_(\d+-\d+[ab])>',t)
    for i in range(1,len(parts),2):
        b=norm(parts[i+1]); PG.append((len(txt),parts[i],len(b))); txt+=b
        if not allpages or allpages[-1]!=parts[i]: allpages.append(parts[i])
starts=[p for p,_,_ in PG]
def page(pos): return PG[bisect.bisect_right(starts,pos)-1][1]
D=sorted(pickle.load(open('sw.pkl','rb')),key=lambda d:d['id'])
cand={}
for n,d in enumerate(D):
    e=norm(d['explanation'])
    for i in range(0,max(1,len(e)-7)):
        k=e[i:i+8]
        if len(k)<8 or '□' in k: continue
        j=txt.find(k)
        if j>=0 and txt.find(k,j+1)<0: cand[n]=j-i; break
idxs=sorted(cand); P=[cand[i] for i in idxs]
tails=[];tidx=[];prev=[-1]*len(P)
for i,p in enumerate(P):
    k=bisect.bisect_left(tails,p)
    if k==len(tails): tails.append(p); tidx.append(i)
    else: tails[k]=p; tidx[k]=i
    prev[i]=tidx[k-1] if k>0 else -1
lis=[];i=tidx[-1]
while i>=0: lis.append(i); i=prev[i]
anc={idxs[i]:max(0,P[i]) for i in lis}; A=sorted(anc)
pos={d['id']:n for n,d in enumerate(D)}
# 页序：用 allpages 的顺序，并补出跳过的页号
def pkey(p): j,l=p.split('-'); return (int(j),int(l[:-1]),l[-1])
def between(a,b):
    ja,la,sa=pkey(a); jb,lb,sb=pkey(b); out=[]
    j,l,s=ja,la,sa
    while (j,l,s)<=(jb,lb,sb) and len(out)<40:
        out.append(f'{j:03d}-{l}{s}')
        if s=='a': s='b'
        else: s='a'; l+=1
        if (j,l)!=(jb,lb) and j<jb and l>60: j+=1; l=1
    return out
present={p:l for _,p,l in PG}
rows=[]
for r in csv.DictReader(open('/home/claude/Morphology/youwen/yisheng_xiaoxu_collation_final.csv',encoding='utf-8-sig')):
    if r['unknown_reason']!='电子本缺文': continue
    n=pos[int(r['sw_id'])]; k=bisect.bisect_left(A,n)
    lo=A[k-1]; hi=A[k] if k<len(A) else None
    pa=page(anc[lo]); pb=page(anc[hi]) if hi is not None else pa
    if pa.split('-')[0]!=pb.split('-')[0]: rng=[pa,pb]
    else: rng=between(pa,pb)
    miss=[p for p in rng if present.get(p,0)<5]
    rows.append(dict(sw_id=r['sw_id'],char=r['char'],phonetic=r['phonetic'],prev_found=D[lo]['wordhead'],prev_page=pa,next_found=D[hi]['wordhead'] if hi is not None else '',next_page=pb,pages_to_check=' '.join(rng),missing_in_etext=' '.join(miss)))
with open('gap_pages.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
for r in rows: print(r['char'],r['prev_found'],r['prev_page'],r['next_found'],r['next_page'],'|',r['missing_in_etext'])
