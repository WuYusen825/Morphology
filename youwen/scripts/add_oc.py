# 并入上古音：BS 2014（digling/cddb 所收 BS 2014 字表 D_ocbs.tsv）与 Schuessler 2007（cddb Schuessler2007）
# 用法：python3 add_oc.py <cddb 目录>   —— 就地更新 rows.json
import csv,json,sys,collections
root=sys.argv[1]
BS=collections.defaultdict(list)
for r in csv.DictReader(open(f'{root}/datasets/Baxter2014/raw/D_ocbs.tsv',encoding='utf-8'),delimiter='\t'):
    BS[r['OurUnicodeZi']].append(r)
SC=collections.defaultdict(list)
for r in csv.DictReader(open(f'{root}/datasets/Schuessler2007/characters.tsv',encoding='utf-8'),delimiter='\t'):
    if r['DOCULECT']=='Old_Chinese' and r['READING'] not in [x['READING'] for x in SC[r['CHARACTER']]]:
        SC[r['CHARACTER']].append(r)
rows=json.load(open('rows.json'))
for r in rows:
    c=r['char']; b=BS.get(c,[])
    hit=[x for x in b if x['MCascii']==r['bs_mc']]
    if hit: pick,how=hit[0],'mc_match'
    elif len(b)==1: pick,how=b[0],'single_reading_mc_differs' if r['bs_mc'] else 'single_reading'
    elif b: pick,how=None,'multiple_readings_no_mc_match'
    else: pick,how=None,'not_in_bs_table'
    r['oc_bs2014']=pick['PubFull'] if pick else ''
    r['oc_bs_mc']=pick['MCascii'] if pick else ''
    r['oc_bs_gloss']=pick['OurGloss'] if pick else ''
    r['oc_bs_gsr']=pick['GSRindexStr'] if pick else ''
    r['oc_bs_match']=how
    r['_bs_raw']=pick
    r['oc_bs_all']=' | '.join(f"{x['PubFull']} ({x['MCascii']}; {x['OurGloss']})" for x in b)
    s=SC.get(c,[])
    r['oc_schuessler2007']=' | '.join(x['READING'] for x in s)
    r['schuessler_wordfamily']=' | '.join(sorted(set(x['VARIANT_CLASS'] for x in s if x['VARIANT_CLASS'])))
    r['schuessler_gloss']=' || '.join(sorted(set(x['GLOSS'] for x in s)))[:300]
from morph import compare
HEADS={r['series']:r for r in rows if r['relation']=='phonetic_head'}
for r in rows:
    h=HEADS.get(r['series'])
    cat,det=compare(r['_bs_raw'],h['_bs_raw'] if h else None) if r['relation']!='phonetic_head' else ('head','')
    r['morph_relation_to_head']=cat; r['morph_diff']=det
for r in rows: r.pop('_bs_raw',None)
json.dump(rows,open('rows.json','w'),ensure_ascii=False,indent=0)
print(collections.Counter(r['oc_bs_match'] for r in rows), sum(1 for r in rows if r['oc_schuessler2007']),len(rows))
