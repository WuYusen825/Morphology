# 小徐本《說文解字繫傳》（四部叢刊本，kanripo/KR1j0019）与大徐本字头逐条对齐，比较"亦聲"标注。
# 该电子本只录说解（小字），不录篆文字头，所以按说解文字顺序对齐：
#   两本条目次序基本一致，逐条在小徐文本中向后搜索该条说解的特征片段，找到即定位，条目区间 = 本条位置到下一条位置。
import pickle,re,glob,json,csv,sys,os,collections
out=sys.argv[1]; kr=sys.argv[2]
D=sorted(pickle.load(open('sw.pkl','rb')),key=lambda d:d['id'])
def norm(s):
    s=re.sub(r'<[^>]*>','',s); s=re.sub(r'&KR\d+;','□',s)
    s=s.replace('從','从').replace('声','聲')
    return re.sub(r'[\s¶()（）/　，。、；：「」『』“”《》\[\]]','',s)
txt=''
for f in sorted(glob.glob(f'{kr}/KR1j0019_0*.txt')):
    n=int(f[-7:-4])
    if 1<=n<=30:
        body=''.join(l for l in open(f,encoding='utf-8') if not l.startswith('#'))
        txt+=norm(body)
def keys(e,L,step):
    e=norm(e)
    return [(i,e[i:i+L]) for i in range(0,max(0,len(e)-L)+1,step) if len(e[i:i+L])==L and '□' not in e[i:i+L]]
# 第一步：取在全文中只出现一次的 8 字片段作锚点，再取位置单调递增的最长子序列，排除错配
import bisect
cand={}
for n,d in enumerate(D):
    for off,k in keys(d['explanation'],8,1):
        j=txt.find(k)
        if j>=0 and txt.find(k,j+1)<0: cand[n]=j-off; break
idxs=sorted(cand); P=[cand[i] for i in idxs]
# 最长递增子序列
tails=[];tidx=[];prev=[-1]*len(P)
for i,p in enumerate(P):
    k=bisect.bisect_left(tails,p)
    if k==len(tails): tails.append(p); tidx.append(i)
    else: tails[k]=p; tidx[k]=i
    prev[i]=tidx[k-1] if k>0 else -1
lis=[];i=tidx[-1]
while i>=0: lis.append(i); i=prev[i]
pos=[None]*len(D)
for i in lis: pos[idxs[i]]=max(0,P[i])
# 第二步：锚点之间的条目，用较短片段在相邻锚点区间内依次查找
anchors=[n for n in range(len(D)) if pos[n] is not None]
for ai in range(len(anchors)+1):
    lo_n=anchors[ai-1] if ai>0 else -1; hi_n=anchors[ai] if ai<len(anchors) else len(D)
    cur=pos[lo_n]+1 if lo_n>=0 else 0; hi=pos[hi_n] if hi_n<len(D) else len(txt)
    for n in range(lo_n+1,hi_n):
        for L in (6,5,4,3):
            hits=[txt.find(k,cur,hi)-off for off,k in keys(D[n]['explanation'],L,1)]
            hits=[h for h in hits if h>=cur-8]
            if hits: pos[n]=max(cur,min(hits)); cur=pos[n]+1; break
print('anchors',len(anchors))
found=[i for i,p in enumerate(pos) if p is not None]
from difflib import SequenceMatcher
def locate(n):
    """在对齐位置附近重新精确定位该条说解：候选起点为说解中任一 3 字片段的出现处，取与大徐说解最相似者。"""
    e=norm(D[n]['explanation']); e_core=e.split('臣鍇')[0]
    prv=next((pos[m] for m in range(n-1,-1,-1) if pos[m] is not None),0)
    nxt=next((pos[m] for m in range(n+1,len(D)) if pos[m] is not None),len(txt))
    lo=max(0,prv-2000); hi=min(len(txt),nxt+2000)
    best=(0,None)
    starts=set()
    for off,k in keys(e_core,3,1):
        j=txt.find(k,lo,hi)
        while j>=0 and len(starts)<400:
            starts.add(max(0,j-off)); j=txt.find(k,j+1,hi)
    for st in starts:
        seg=txt[st:st+len(e_core)+12].split('臣鍇')[0]
        r=SequenceMatcher(None,e_core.replace('亦聲','聲'),seg.replace('亦聲','聲')).ratio()
        if r>best[0]: best=(r,st)
    return best
rows=[]
for n,d in enumerate(D):
    dx='亦聲' in d['explanation']
    if not dx and pos[n] is None: continue
    # 先粗筛：只处理大徐亦声字，以及对齐区间内出现亦声的条目
    if not dx:
        nxt=next((pos[m] for m in range(n+1,len(D)) if pos[m] is not None),len(txt))
        if '亦聲' not in txt[pos[n]:nxt].split('臣鍇')[0]: continue
    score,st=locate(n)
    if st is None:
        rows.append(dict(sw_id=d['id'],char=d['wordhead'],daxu_gloss=d['explanation'],daxu_yisheng=dx,xiaoxu_yisheng='',xiaoxu_phonetic='',
            xiaoxu_text='',match_score=0,match_conf='none',agreement='not_aligned')); continue
    seg=txt[st:st+len(norm(d['explanation']))+12].split('臣鍇')[0]
    xx='亦聲' in seg; m=re.search(r'(.)亦聲',seg)
    if not dx and not xx: continue
    conf='high' if score>=0.8 else ('medium' if score>=0.65 else 'low')
    agr='not_aligned' if conf!='high' else ('both' if dx and xx else ('daxu_only' if dx else 'xiaoxu_only'))
    rows.append(dict(sw_id=d['id'],char=d['wordhead'],daxu_gloss=d['explanation'],daxu_yisheng=dx,xiaoxu_yisheng=xx if conf=='high' else '',
        xiaoxu_phonetic=m.group(1) if m and conf=='high' else '',xiaoxu_text=seg,match_score=round(score,2),match_conf=conf,agreement=agr))
# 同一段小徐文字可能被相邻两条同时认领：保留相似度高的一条
seen={}
for r in rows:
    if r['agreement']=='xiaoxu_only':
        k=r['xiaoxu_text'][:15]
        if k in seen and seen[k]['match_score']>=r['match_score']: r['agreement']='dup_drop'
        else:
            if k in seen: seen[k]['agreement']='dup_drop'
            seen[k]=r
rows=[r for r in rows if r['agreement']!='dup_drop']
rows.sort(key=lambda r:r['sw_id'])
with open(os.path.join(out,'yisheng_daxu_xiaoxu.csv'),'w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print('aligned entries',len(found),'/',len(D),'| xiaoxu 亦聲 in text total',txt.count('亦聲'))
print(collections.Counter(r['agreement'] for r in rows))
