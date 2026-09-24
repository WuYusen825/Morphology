import pickle,re,json,subprocess
D=pickle.load(open('sw.pkl','rb'))
SERIES={'戔':'戔','侖':'侖','農':'農','句':'句','皮':'皮','兼':'兼','巠':'巠坙','叚':'叚','冓':'冓','堯':'堯','喬':'喬','氐':'氐','票':'票㶾𤐫','叕':'叕','青':'青靑'}
HEADID={'農':1779}
YW=re.compile(r'之言|凡.{0,6}聲|聲義|會意兼|兼形聲|形聲包會意|形聲兼會意|取.{1,6}之意|以.{1,3}會意|亦聲|皆有.{1,6}意|同意|音義(皆)?同')
OT=re.compile(r'假借|叚借|引伸|引申')
rows=[];seen=set()
for ph,forms in SERIES.items():
    pat=re.compile('(['+forms+'])(省)?(亦)?聲')
    cands=[(d,'phonetic_head') for d in D if d['wordhead'] in forms or d['id']==HEADID.get(ph)]
    for d in D:
        if d['wordhead'] in forms: continue
        m=pat.search(d['explanation'])
        if m: cands.append((d,'亦聲' if m.group(3) else ('省聲' if m.group(2) else '聲')))
        elif d['radical'] in forms: cands.append((d,'部屬會意(無聲)'))
    for d,rel in cands:
        if (ph,d['id']) in seen: continue
        seen.add((ph,d['id']))
        notes=' ‖ '.join(n['note'] for n in d['duan_notes'])
        bu=re.search(r'切。?(?:古音(?:在)?)?(?:第)?([一二三四五六七八九十]{1,3})部',notes) or re.search(r'古音(?:在)?(?:第)?([一二三四五六七八九十]{1,3})部',notes)
        sents=[s for n in d['duan_notes'] for s in n['note'].split('。')]
        rows.append(dict(series=ph,char=d['wordhead'],sw_id=d['id'],relation=rel,sw_gloss=d['explanation'],dx_fanqie=d['pronunciation'],
          duan_rhyme_group=(bu.group(1)+'部') if bu else '',
          duan_youwen_remarks=' / '.join(s for s in sents if YW.search(s))[:300],
          duan_loan_or_extension_remarks=' / '.join(s for s in sents if OT.search(s) and not YW.search(s))[:300],
          duan_full=notes))
json.dump([{'char':r['char'],'fq':r['dx_fanqie'].replace('切','')} for r in rows],open('q.json','w'),ensure_ascii=False)
mc=json.loads(subprocess.check_output(['node','mc2.mjs','../q.json'],cwd='tshet-uinh-examples'))
for r,m in zip(rows,mc):
    assert r['char']==m['char']; r.update({k:v for k,v in m.items() if k!='char'})
json.dump(rows,open('rows.json','w'),ensure_ascii=False,indent=0)
from collections import Counter
print(len(rows),Counter(r['mc_match'] for r in rows),Counter(r['relation'] for r in rows),sum(1 for r in rows if not r['duan_rhyme_group']))
# 过滤：以声符为部首但另有他声（或"闕"）的字不属该声符系列
rows=[r for r in rows if not (r['relation']=='部屬會意(無聲)' and ('聲' in r['sw_gloss'] or r['sw_gloss'].startswith('闕')))]
for r in rows:
    if r['relation']=='部屬會意(無聲)': r['relation']='會意（聲符作形旁，無聲）'
json.dump(rows,open('rows.json','w'),ensure_ascii=False,indent=0)
