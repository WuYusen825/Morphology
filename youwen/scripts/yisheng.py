# 问题二语料：《说文》全部"亦声"字，及与其同声符的普通形声字（对照组），附中古音、BS 2014 上古音与自动形态关系分类
# v2（2026-09-24）：修正"从X亦聲"误收；标新附；中古音关系变量；声训标记；段注、小徐标签及仅见于段注/小徐的补充行
# 用法：python3 yisheng.py <outdir> <cddb>   （<outdir> 中需已有 yisheng_daxu_xiaoxu.csv）
import pickle,re,json,subprocess,csv,sys,os,collections
from morph import compare,affix_detail,affix_type
from relation_types import REL
out=sys.argv[1]; cddb=sys.argv[2]
D=pickle.load(open('sw.pkl','rb')); BYID={d['id']:d for d in D}
BS=collections.defaultdict(list)
for r in csv.DictReader(open(f'{cddb}/datasets/Baxter2014/raw/D_ocbs.tsv',encoding='utf-8'),delimiter='\t'): BS[r['OurUnicodeZi']].append(r)
HEAD={}
for d in D:
    for c in [d['wordhead']]+d['indexes']: HEAD.setdefault(c,d)
# "从巾亦聲"一类是"从巾，亦聲"，亦本身是声符，不是亦声标记（帟奕弈迹），故要求捕获字前不是"从"
yi=re.compile(r'(?<!从)([^\s，。、；：“”《》从])亦聲')
MANUAL={'從':'从','𠔁':'八','兩':'㒳'}

# 徐铉新附：每部末尾连续无段注的字头（段注本不收新附）。否 是例外（段氏归不部）。须据 1963 年中华影印本逐条核对
def has_duan(d): return any((n.get('explanation') or '').strip() or (n.get('note') or '').strip() for n in d['duan_notes'])
byrad=collections.defaultdict(list)
for d in sorted(D,key=lambda d:d['id']): byrad[d['radical']].append(d)
XINFU=set()
for ds in byrad.values():
    for d in reversed(ds):
        if has_duan(d): break
        XINFU.add(d['id'])
XINFU-={d['id'] for d in D if d['wordhead']=='否' and d['radical']=='不'}

# 段注本的亦声标注（段氏改定的说文正文 = duan_notes[].explanation）
def duan_text(d): return ''.join((n.get('explanation') or '') for n in d['duan_notes'])
import unicodedata
DUAN_MANUAL={'從':'从','頛':'耒','塋':'營','博':'尃'}   # 段注作"从亦聲""耒、頭傾、亦聲"等，正则取不到，手工指定
def duan_phon(d):
    if d['wordhead'] in DUAN_MANUAL and '亦聲' in duan_text(d): return DUAN_MANUAL[d['wordhead']]
    m=yi.search(unicodedata.normalize('NFKC',duan_text(d))); return m.group(1) if m else ''
WORDS={d['wordhead'] for d in D}
DUAN_FORM={'𩫖':'𩫏'}
def canon(c):  # 段注用字若不是大徐字头，按 indexes 映到大徐字头（仅用于补充行的声符）
    c=DUAN_FORM.get(c,c)
    if c in WORDS: return c
    h=HEAD.get(c); return h['wordhead'] if h else c
# 大徐标亦声、段注也标亦声但改换了声符的（逐条目验；其余"声符不同"均为段注用字异体，如豐/豊、丼/井、㒳/兩）
DUAN_PHON_CHANGED={'叛','咅','必','䢈','遌'}
# 段注的"亦聲"只针对古文/籀文重文，不针对字头，不作补充行
DUAN_CHONGWEN={'孚','仄','膌'}

# 小徐（繫傳）对齐结果
XX={}
xxf=os.path.join(out,'yisheng_daxu_xiaoxu.csv')
XX_PHON={'孝':'老','竦':'束','𧗁':'𦘔'}   # 小徐文本声符捕获有误的 3 条，据小徐原文"老省亦聲""束…亦聲""□□亦聲（大徐𦘔聲）"手改
for r in csv.DictReader(open(xxf,encoding='utf-8-sig')):
    XX[int(r['sw_id'])]=r

phons=sorted({m.group(1) for d in D for m in [yi.search(d['explanation'])] if m}|set(MANUAL.values())|{'亦'})
rows=[]
def base(P,d,rel,src):
    h=HEAD.get(P)
    return dict(phonetic=P,head_in_shuowen=bool(h),head_gloss=h['explanation'] if h else '',head_dx_fanqie=h['pronunciation'] if h else '',
        char=d['wordhead'],sw_id=d['id'],relation=rel,label_source=src,shuowen_gloss=d['explanation'],daxu_fanqie=d['pronunciation'])
for P in phons:
    pat=re.compile('从[^。]{0,5}?'+re.escape(P)+'(省)?(亦)?聲')
    for d in D:
        if d['wordhead']==P: continue
        y=yi.search(d['explanation'])
        if (y and y.group(1)==P) or MANUAL.get(d['wordhead'])==P: rel='亦聲'
        else:
            m=pat.search(d['explanation'])
            if not m: continue
            if m.group(0)=='从'+P+'亦聲': continue          # "从廾亦聲"：P 是形旁，亦是声符
            if P=='亦' and (y or m.group(1) is None and not re.search('从[^，。、从]亦聲',d['explanation'])): continue  # 亦系只收"从X亦聲""从X亦省聲"
            rel='亦聲' if m.group(2) else ('省聲' if m.group(1) else '聲')
        rows.append(base(P,d,rel,'daxu'))
have={(r['char'],r['phonetic']) for r in rows}; have_id={r['sw_id'] for r in rows if r['relation']=='亦聲'}
# 补充行：仅段注或仅小徐标亦声、而大徐未把该声符写成亦声者
extra={}
for d in D:
    if d['id'] in XINFU or d['id'] in have_id: continue
    p=duan_phon(d)
    if p and d['wordhead'] not in DUAN_CHONGWEN: extra.setdefault(d['id'],{})['duan']=canon(p)
for i,x in XX.items():
    if x['agreement']=='xiaoxu_only': extra.setdefault(i,{})['xiaoxu']=XX_PHON.get(x['char'],x['xiaoxu_phonetic'])
for i,e in sorted(extra.items()):
    d=BYID[i]; P=e.get('duan') or e.get('xiaoxu')
    src='+'.join(k+'_only' for k in ('duan','xiaoxu') if k in e)
    if (d['wordhead'],P) in have:   # 大徐已作"X聲"收入：不另立行，只在标签列体现
        continue
    rows.append(base(P,d,'會意/其他',src))
    if P not in phons: phons.append(P)

q=[{'char':r['char'],'fq':r['daxu_fanqie'].replace('切','')} for r in rows]+[{'char':P,'fq':(HEAD[P]['pronunciation'] if P in HEAD else '').replace('切','')} for P in phons]
json.dump(q,open('q3.json','w'),ensure_ascii=False)
mc=json.loads(subprocess.check_output(['node','mc2.mjs','../q3.json'],cwd='tshet-uinh-examples'))
HM={x['char']:x for x in mc[len(rows):]}
def pick(c,mcv):
    b=BS.get(c,[]); hit=[x for x in b if x['MCascii']==mcv]
    if hit: return hit[0],'mc_match'
    if len(b)==1: return b[0],'single_reading'
    return (None,'multiple_readings' if b else 'not_in_bs')

# 中古音关系：BS 中古音转写拆成声母/韵/调；清浊交替按全浊对全清归并
VOICE={'b':'p','d':'t','dr':'tr','dz':'ts','dzr':'tsr','dzy':'tsy','g':'k','z':'s','zr':'sr','zy':'sy','h':'x'}
INI=sorted(['p','ph','b','m','t','th','d','n','tr','trh','dr','nr','ts','tsh','dz','s','z','tsr','tsrh','dzr','sr','zr',
            'tsy','tsyh','dzy','ny','sy','zy','k','kh','g','ng',"'",'x','h','y','l'],key=len,reverse=True)
def split(s):
    tone={'X':'上','H':'去'}.get(s[-1:],'')
    body=s[:-1] if tone else s
    if not tone: tone='入' if body.endswith(('p','t','k')) else '平'
    ini=next((i for i in INI if body.startswith(i)),'')
    return ini,body[len(ini):],tone
def mc_vars(a,b):
    if not a or not b: return dict(mc_relation='NA',mc_tone_member='',mc_tone_head='',mc_voicing_differs='',mc_qusheng_direction='')
    A,B=split(a),split(b)
    v=dict(mc_tone_member=A[2],mc_tone_head=B[2],mc_voicing_differs=str(A[0]!=B[0] and VOICE.get(A[0],A[0])==VOICE.get(B[0],B[0])))
    if A==B: rel='identical'
    elif A[1]==B[1] and VOICE.get(A[0],A[0])==VOICE.get(B[0],B[0]): rel='tone_voicing_alt'
    else: rel='other'
    v['mc_relation']=rel
    v['mc_qusheng_direction']=('member' if A[2]=='去' and B[2]!='去' else 'head' if B[2]=='去' and A[2]!='去' else 'none') if rel=='tone_voicing_alt' else ''
    return v
def defn(g): return re.split('从|從',g)[0]
for i,r in enumerate(rows):
    m=mc[i]; hm=HM[r['phonetic']]; d=BYID[r['sw_id']]
    r.update(mc_bs2014=m['bs_mc'],guangyun_position=m['gy_primary'],mc_confidence=m['mc_match'],head_mc_bs2014=hm['bs_mc'],head_mc_confidence=hm['mc_match'])
    r.update(mc_vars(m['bs_mc'],hm['bs_mc']))
    a,ha=pick(r['char'],m['bs_mc']); b,hb=pick(r['phonetic'],hm['bs_mc'])
    r.update(oc_bs2014=a['PubFull'] if a else '',oc_bs_match=ha,head_oc_bs2014=b['PubFull'] if b else '',head_oc_bs_match=hb)
    cat,det=compare(a,b); r.update(morph_relation_auto=cat,morph_diff=det,
        morph_affix_detail=affix_detail(a,b) if cat=='R' else '',morph_affix_type=affix_type(a,b) if cat=='R' else '')
    # 声训：释义的定义部分（"从"之前）出现声符字本身
    r['paronomastic_gloss']=str(r['phonetic'] in defn(r['shuowen_gloss']))
    r['is_xinfu']=str(r['sw_id'] in XINFU)
    dp=duan_phon(d) if d['wordhead'] not in DUAN_CHONGWEN else ''
    r['duan_label']='' if r['is_xinfu']=='True' else ('缺段注' if not has_duan(d) else ('亦聲' if dp else '無'))
    r['duan_phonetic']=dp; r['duan_phonetic_changed']=str(bool(dp) and d['wordhead'] in DUAN_PHON_CHANGED and r['label_source']=='daxu')
    x=XX.get(r['sw_id'])
    r['xiaoxu_label']=('亦聲' if x['xiaoxu_yisheng']=='True' else '無') if x and x['agreement']!='not_aligned' else ('未对齐' if x else '')
    r['identical_relation_type']=REL.get((r['char'],r['phonetic']),'') if r['mc_relation']=='identical' else ''
    r['in_analysis_set']=str(r['label_source']=='daxu' and r['relation'] in ('亦聲','聲') and r['is_xinfu']=='False')
    r['src']='说文: shuowenjiezi/shuowen（大徐正文 explanation；段注 duan_notes）; 广韵: tshet-uinh 0.15.1; BS2014: digling/cddb Baxter2014/raw/D_ocbs.tsv; 小徐: kanripo/KR1j0019 via yisheng_daxu_xiaoxu.csv'
rows.sort(key=lambda r:(r['phonetic'],r['label_source']!='daxu',r['relation']!='亦聲',r['sw_id']))
with open(os.path.join(out,'yisheng_dataset.csv'),'w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
json.dump(rows,open('yisheng_rows.json','w'),ensure_ascii=False)
A=[r for r in rows if r['in_analysis_set']=='True']
print('rows',len(rows),collections.Counter((r['label_source'],r['relation']) for r in rows))
print('analysis set',collections.Counter(r['relation'] for r in A),'亦聲 phonetics',len({r['phonetic'] for r in A if r['relation']=='亦聲'}))
print('xinfu 亦聲',[r['char'] for r in rows if r['relation']=='亦聲' and r['is_xinfu']=='True'])
