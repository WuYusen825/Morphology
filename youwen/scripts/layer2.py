# 第二层：非《说文》字头、但《广韵》收录且 IDS 为"形旁+声符"结构的后起字。仅列出，不编码。
import pickle,json,re,subprocess,csv,sys,os
D=pickle.load(open('sw.pkl','rb'))
SW=set(c for d in D for c in [d['wordhead']]+d['indexes'])
FORMS={'戔':'戔','侖':'侖','農':'農','句':'句','皮':'皮','兼':'兼','巠':'巠坙','叚':'叚','冓':'冓','堯':'堯','喬':'喬','氐':'氐','票':'票㶾𤐫','叕':'叕','青':'青靑'}
IDS={}
for line in open('cjkvi-ids/ids.txt',encoding='utf-8'):
    if line.startswith(';'): continue
    p=line.rstrip('\n').split('\t')
    if len(p)>=3: IDS[p[1]]=[re.sub(r'\[.*?\]','',x) for x in p[2:]]
cand=[]
for ch,idss in IDS.items():
    if ch in SW or len(ch)!=1: continue
    for ph,forms in FORMS.items():
        if ch in forms: continue
        if any(len(x)==3 and x[0] in '⿰⿱⿸⿺⿹⿵⿴' and (x[2] in forms or (x[0]=='⿱' and x[1] in forms)) for x in idss):
            cand.append((ph,ch,idss[0]));break
json.dump([{'char':c,'fq':''} for _,c,_ in cand],open('q2.json','w'),ensure_ascii=False)
mc=json.loads(subprocess.check_output(['node','mc2.mjs','../q2.json'],cwd='tshet-uinh-examples'))
R=json.load(open('rows.json'))
RIME={}
for r in R:
    for rd in r['gy_all'].split(' | '):
        if rd: RIME.setdefault(r['series'],set()).add(rd.split()[0][-2])
out=[]
for (ph,ch,ids),m in zip(cand,mc):
    if not m['gy_all']: continue   # 只留《广韵》收录者
    # 语音过滤：至少一个读音的韵与该系列《说文》成员的韵相同，排除声符字作形旁者（如"皺"）
    if not any(rd.split()[0][-2] in RIME[ph] for rd in m['gy_all'].split(' | ')): continue
    out.append({'group':'layer2_later','series':ph,'char':ch,'ids':ids,'guangyun_all_readings':m['gy_all'],
                'code_core':'','note':'非《说文》字头；未编码','src':'IDS: cjkvi-ids; 广韵: tshet-uinh 0.15.1'})
out.sort(key=lambda r:(list(FORMS).index(r['series']),r['char']))
with open(os.path.join(sys.argv[1],'youwen_layer2_later_chars.csv'),'w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
from collections import Counter
print(len(out),Counter(r['series'] for r in out)); print(''.join(r['char'] for r in out))
