# 问题二语料：《说文》全部"亦声"字，及与其同声符的普通形声字（对照组），附中古音、BS 2014 上古音与自动形态关系分类
import pickle,re,json,subprocess,csv,sys,os,collections
from morph import compare
out=sys.argv[1]; cddb=sys.argv[2]
D=pickle.load(open('sw.pkl','rb'))
BS=collections.defaultdict(list)
for r in csv.DictReader(open(f'{cddb}/datasets/Baxter2014/raw/D_ocbs.tsv',encoding='utf-8'),delimiter='\t'): BS[r['OurUnicodeZi']].append(r)
HEAD={}
for d in D:
    for c in [d['wordhead']]+d['indexes']: HEAD.setdefault(c,d)
yi=re.compile(r'([^\s，。、；：“”《》从])亦聲')
phons=sorted({m.group(1) for d in D for m in [yi.search(d['explanation'])] if m})
rows=[]
for P in phons:
    pat=re.compile('从[^。]{0,5}?'+re.escape(P)+'(省)?(亦)?聲')
    h=HEAD.get(P)
    for d in D:
        if d['wordhead']==P: continue
        y=yi.search(d['explanation'])
        if y and y.group(1)==P: rel='亦聲'
        else:
            m=pat.search(d['explanation'])
            if not m: continue
            rel='亦聲' if m.group(2) else ('省聲' if m.group(1) else '聲')
        rows.append(dict(phonetic=P,head_in_shuowen=bool(h),head_gloss=h['explanation'] if h else '',head_dx_fanqie=h['pronunciation'] if h else '',
            char=d['wordhead'],sw_id=d['id'],relation=rel,shuowen_gloss=d['explanation'],daxu_fanqie=d['pronunciation']))
q=[{'char':r['char'],'fq':r['daxu_fanqie'].replace('切','')} for r in rows]+[{'char':P,'fq':(HEAD[P]['pronunciation'] if P in HEAD else '').replace('切','')} for P in phons]
json.dump(q,open('q3.json','w'),ensure_ascii=False)
mc=json.loads(subprocess.check_output(['node','mc2.mjs','../q3.json'],cwd='tshet-uinh-examples'))
MCm={(x['char'],i<len(rows)):x for i,x in enumerate(mc)}
def pick(c,mcv):
    b=BS.get(c,[]); hit=[x for x in b if x['MCascii']==mcv]
    if hit: return hit[0],'mc_match'
    if len(b)==1: return b[0],'single_reading'
    return (None,'multiple_readings' if b else 'not_in_bs')
for i,r in enumerate(rows):
    m=mc[i]; hm=[x for x in mc[len(rows):] if x['char']==r['phonetic']][0]
    r.update(mc_bs2014=m['bs_mc'],guangyun_position=m['gy_primary'],mc_confidence=m['mc_match'],head_mc_bs2014=hm['bs_mc'])
    a,ha=pick(r['char'],m['bs_mc']); b,hb=pick(r['phonetic'],hm['bs_mc'])
    r.update(oc_bs2014=a['PubFull'] if a else '',oc_bs_match=ha,head_oc_bs2014=b['PubFull'] if b else '',head_oc_bs_match=hb)
    cat,det=compare(a,b); r.update(morph_relation_auto=cat,morph_diff=det)
    r['src']='说文: shuowenjiezi/shuowen; 广韵: tshet-uinh 0.15.1; BS2014: digling/cddb Baxter2014/raw/D_ocbs.tsv'
# 只保留至少有一个普通形声对照字、或本身即亦声的系列（全部保留，统计时再筛）
rows.sort(key=lambda r:(r['phonetic'],r['relation']!='亦聲',r['sw_id']))
with open(os.path.join(out,'yisheng_dataset.csv'),'w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
json.dump(rows,open('yisheng_rows.json','w'),ensure_ascii=False)
C=collections.Counter((r['relation'],r['morph_relation_auto']) for r in rows)
print(len(phons),len(rows),collections.Counter(r['relation'] for r in rows)); [print(k,v) for k,v in sorted(C.items())]
