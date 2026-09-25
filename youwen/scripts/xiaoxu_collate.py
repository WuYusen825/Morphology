# 小徐本对照第二轮（2026-09-25）：补齐第一轮（xiaoxu_align.py）没有可靠对齐的大徐亦声字
# 做法：只用第一轮的"唯一 8 字锚点 + 最长递增子序列"作为可靠定位，锚点之间的窗口通常只含几条；
# 在窗口内以说解的定义部分做模糊定位，读取许慎说解（到"臣鍇"为止），判定小徐作"亦聲"、"聲"还是其他。
# 卷二十五（今本据大徐补）单独标出，不作证据。
# 用法：python3 xiaoxu_collate.py <outdir> <KR1j0019 目录>   → <outdir>/yisheng_xiaoxu_collation.csv
import pickle,re,glob,csv,sys,os,bisect,collections
from difflib import SequenceMatcher
out,kr=sys.argv[1:3]
D=sorted(pickle.load(open('sw.pkl','rb')),key=lambda d:d['id'])
def norm(s):
    s=re.sub(r'<[^>]*>','',s); s=re.sub(r'&KR\d+;','□',s); s=re.sub(r'\[[^\]]*\]','□',s)
    s=s.replace('從','从').replace('声','聲').replace('�','□')
    return re.sub(r'[\s¶()（）/　，。、；：「」『』“”《》\[\]]','',s)
txt='';JU=[]   # JU: (起点, 卷号)
for f in sorted(glob.glob(f'{kr}/KR1j0019_0*.txt')):
    n=int(f[-7:-4])
    if 1<=n<=30:
        JU.append((len(txt),n)); txt+=norm(''.join(l for l in open(f,encoding='utf-8') if not l.startswith('#')))
def juan(p): return JU[bisect.bisect_right([a for a,_ in JU],p)-1][1]
def keys(e,L):
    e=norm(e); return [(i,e[i:i+L]) for i in range(0,max(0,len(e)-L)+1) if len(e[i:i+L])==L and '□' not in e[i:i+L]]
cand={}
for n,d in enumerate(D):
    for off,k in keys(d['explanation'],8):
        j=txt.find(k)
        if j>=0 and txt.find(k,j+1)<0: cand[n]=j-off; break
idxs=sorted(cand); P=[cand[i] for i in idxs]
tails=[];tidx=[];prev=[-1]*len(P)
for i,p in enumerate(P):
    k=bisect.bisect_left(tails,p)
    if k==len(tails): tails.append(p); tidx.append(i)
    else: tails[k]=p; tidx[k]=i
    prev[i]=tidx[k-1] if k>0 else -1
lis=[];i=tidx[-1]
while i>=0: lis.append(i); i=prev[i]
anc={idxs[i]:max(0,P[i]) for i in lis}
A=sorted(anc)
def window(n):
    k=bisect.bisect_left(A,n)
    if n in anc: return anc[n],anc[n]+len(norm(D[n]['explanation']))+60,0,0
    lo_n=A[k-1] if k>0 else None; hi_n=A[k] if k<len(A) else None
    lo=anc[lo_n] if lo_n is not None else 0; hi=anc[hi_n] if hi_n is not None else len(txt)
    return lo,hi,n-(lo_n if lo_n is not None else 0),(hi_n if hi_n is not None else len(D))-n
def core(e): return norm(e).split('臣鍇')[0]
def best(n,lo,hi):
    e=core(D[n]['explanation']); defn=re.split('从',e)[0] or e
    b=(0,None)
    for st in range(lo,max(lo+1,hi-3)):
        if txt[st] not in e: continue   # 起点须是说解中出现的字
        seg=txt[st:st+len(e)+8]
        r=SequenceMatcher(None,e.replace('亦聲','聲'),seg.split('臣鍇')[0].replace('亦聲','聲'),autojunk=False).ratio()
        if r>b[0]: b=(r,st)
    return b
import json
PH={}
for r in json.load(open('yisheng_rows.json')):
    if r['relation']=='亦聲' and r['label_source']=='daxu': PH[r['sw_id']]=r['phonetic']
PH.update({d['id']:'亦' for d in D if d['wordhead'] in '帟奕弈迹' and '亦聲' in d['explanation']})   # 误收 4 字
rows=[]
for n,d in enumerate(D):
    if '亦聲' not in d['explanation']: continue
    lo,hi,dl,dh=window(n)
    sc,st=best(n,lo,hi)
    e=core(d['explanation'])
    seg=txt[st:st+len(e)+12].split('臣鍇')[0] if st is not None else ''
    m=re.search(r'(.)(省)?亦聲',seg); m2=re.search(r'(.)(省)?聲',seg)
    read='亦聲' if m else ('聲' if m2 else '其他')
    # 第二种判定：在锚点窗口内直接找"声符字+亦聲/聲"。窗口一般只有几条，声符字加"亦聲"几乎只会出自本条
    p=PH.get(d['id'],''); W=txt[lo:hi]; W=re.sub('臣鍇曰.*?(?=[^臣]{0,0})','',W)
    wy=len(re.findall(re.escape(p)+'(省)?亦聲',W)) if p else 0
    ws=len(re.findall(re.escape(p)+'(省)?聲',W))-wy if p else 0
    wread='亦聲' if wy else ('聲' if ws else '未见声符')
    rows.append(dict(sw_id=d['id'],char=d['wordhead'],daxu_gloss=d['explanation'],xiaoxu_text=seg,xiaoxu_reading=read,
        xiaoxu_phonetic=(m or m2).group(1) if (m or m2) else '',daxu_phonetic=p,window_reading=wread,window_yisheng_hits=wy,window_sheng_hits=ws,match_score=round(sc,2),window_chars=hi-lo,
        entries_from_anchor=f'{dl}/{dh}',juan=juan(st) if st is not None else '',
        window_text=txt[lo:hi][:400]))
with open(os.path.join(out,'yisheng_xiaoxu_collation.csv'),'w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print('anchors',len(A),'rows',len(rows))
print(collections.Counter(r['window_reading'] for r in rows))

# 第三种判定（主判定）：在预期卷次（锚点所在卷 ±1）内找出所有"声符字(省)(亦)聲"，
# 取其前 30 字与大徐说解（去掉结构分析）的相似度最高者为本条。异体字先归一。
VAR=str.maketrans({'賔':'賓','亾':'亡','㑹':'會','竒':'奇','徔':'从','従':'从','飬':'養','歳':'歲','齨':'齨','𥄕':'苜','属':'屬','髙':'高','扵':'於','䟽':'疏','艸':'艸'})
def vn(s): return s.translate(VAR)
T=vn(txt)
JS=[a for a,_ in JU]+[len(txt)]
def juan_range(n):
    k=bisect.bisect_left(A,n); ps=[anc[A[j]] for j in (k-1,k) if 0<=j<len(A)]
    js={juan(p) for p in ps}; lo=min(js)-1; hi=max(js)+1
    a=[s for s,j in JU if j>=lo]; b=[s for s,j in JU if j>hi]
    return (a[0] if a else 0),(b[0] if b else len(txt))
def cands(n,p):
    lo,hi=juan_range(n); e=vn(core(D[n]['explanation'])); pre=re.split('从',e)[0]
    out=[]
    for m in re.finditer(re.escape(vn(p))+'(省)?(亦)?聲',T[lo:hi]) if p else []:
        s=lo+m.start(); ctx=T[max(0,s-30):s]
        if '臣鍇' in ctx and '反' not in ctx.rsplit('臣鍇',1)[1]: continue   # 命中在徐鍇按语里（如 貧 下"當言分亦聲"），不是说解
        sm=SequenceMatcher(None,pre,ctx[-len(pre)-14:],autojunk=False); r=sum(b.size for b in sm.get_matching_blocks())/len(pre) if pre else 0   # 大徐定义部分有多少字按序出现在候选前文中
        out.append((round(r,2),s,'亦聲' if m.group(2) else ('省聲' if m.group(1) else '聲'),T[max(0,s-30):s+len(m.group(0))]))
    return sorted(out,reverse=True)
for r,(n,d) in zip(rows,[(n,d) for n,d in enumerate(D) if '亦聲' in d['explanation']]):
    c=cands(n,r['daxu_phonetic'])
    r['cand_best']=' | '.join(f'{x[0]} {x[2]} 卷{juan(x[1])} {x[3]}' for x in c[:3])
    r['cand_reading']=c[0][2] if c and c[0][0]>=0.6 else ''
    r['cand_score']=c[0][0] if c else 0
    r['cand_juan']=juan(c[0][1]) if c else ''
with open(os.path.join(out,'yisheng_xiaoxu_collation.csv'),'w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print(collections.Counter(r['cand_reading'] for r in rows))
