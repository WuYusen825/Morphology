import pickle,json,re,math
D=pickle.load(open('sw.pkl','rb'))
import coding
KW={'戔':'小|少|淺|薄|微','侖':'理|倫|次|序|條','農':'厚|濃|多','句':'曲|句|鉤|拘','皮':'分|析|剝|破|離|裂|碎','兼':'并|幷|兼|兩|二','巠':'直|長|莖','叚':'赤|紅|丹','冓':'交|遇|會|合','堯':'高','喬':'高|長','氐':'下|底|根|至|抵','票':'輕|飛|浮|疾|末|風','叕':'連|聯|綴|續|合','青':'清|明|精|潔|純','方':'并|併|旁|兩','古':'久|故|舊|老','可':'可|肯|許','其':'箕|簸','各':'異|別|各|殊'}
def defn(e): return e.split('从')[0]
def lchoose(n,k): return math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1)
def fisher_greater(a,b,c,d):
    # P(X>=a) hypergeometric; a=series hits, b=series misses, c=other hits, d=other misses
    n1=a+b; K=a+c; N=a+b+c+d
    return sum(math.exp(lchoose(K,x)+lchoose(N-K,n1-x)-lchoose(N,n1)) for x in range(a,min(n1,K)+1))
R=json.load(open('rows.json'))
out=[]
for s,kw in KW.items():
    mem=[r for r in R if r['series']==s and r['relation']!='phonetic_head' and coding.C[s].get(r['char'],('?',))[0] not in ('X','H')]
    ids={r['sw_id'] for r in R if r['series']==s}
    pat=re.compile(kw)
    a=sum(1 for r in mem if pat.search(defn(r['sw_gloss']))); b=len(mem)-a
    others=[d for d in D if d['id'] not in ids]
    c=sum(1 for d in others if pat.search(defn(d['explanation']))); d_=len(others)-c
    codes=[coding.C[s][r['char']][0] for r in mem]
    out.append(dict(group=next(r['group'] for r in R if r['series']==s),series=s,keywords=kw,n_members=len(mem),kw_hits=a,kw_rate=round(a/len(mem),3),baseline_rate=round(c/len(others),3),
      fisher_p_one_sided=float('%.2g'%fisher_greater(a,b,c,d_)),Y=codes.count('Y'),E=codes.count('E'),N=codes.count('N'),
      strict_rate_Y=round(codes.count('Y')/len(mem),3),loose_rate_YE=round((codes.count('Y')+codes.count('E'))/len(mem),3),
      n_X_excluded=sum(1 for r in R if r['series']==s and coding.C[s].get(r['char'],('',))[0]=='X')))
json.dump(out,open('stats.json','w'),ensure_ascii=False)
for o in out: print(o)
