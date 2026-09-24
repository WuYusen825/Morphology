import json,csv,coding,os,sys
R=json.load(open('rows.json'))
HEADRHYME={'戔':'十四部','侖':'十三部','農':'九部','句':'四部','皮':'十七部','兼':'七部','巠':'十一部','叚':'五部','冓':'四部','堯':'二部','喬':'二部','氐':'十五部','票':'二部','叕':'十五部','青':'十一部','方':'十部','古':'五部','可':'十七部','其':'一部','各':'五部'}
ORDER=list(coding.CORE)
R.sort(key=lambda r:(ORDER.index(r['series']), r['relation']!='phonetic_head', r['sw_id']))
out=[]
for i,r in enumerate(R,1):
    s=r['series']; code,alt,note=coding.C[s][r['char']]
    n=len(r['gy_all'].split(' | ')) if r['gy_all'] else 0
    m=r['mc_match']
    conf='none' if m=='none' else ('high' if m in('identical_fanqie','initial+rhyme+tone') else ('medium' if n==1 else 'low'))
    flags=[]
    if conf in('low','none'): flags.append('mc_'+conf)
    if not r['duan_rhyme_group']: flags.append('duan_rhyme_missing')
    elif r['duan_rhyme_group']!=HEADRHYME[s]: flags.append('rhyme_group_differs_from_head')
    if '存疑' in note: flags.append('coding_uncertain')
    if code=='X': flags.append('proper_name_excluded')
    if '反义' in note: flags.append('counterexample_opposite_meaning')
    if r['relation'] not in('聲','phonetic_head'): flags.append('relation_'+r['relation'])
    core,src,altcore,altsrc=coding.CORE[s]
    out.append({'row_id':i,'group':r['group'],'series':s,'char':r['char'],'relation_in_shuowen':r['relation'],
      'shuowen_gloss':r['sw_gloss'],'shuowen_id':r['sw_id'],'daxu_fanqie':r['dx_fanqie'],
      'guangyun_position':r['gy_primary'],'guangyun_fanqie':r['gy_fanqie'],'mc_bs2014':r['bs_mc'],
      'mc_match_method':m,'mc_confidence':conf,'guangyun_all_readings':r['gy_all'],
      'oc_bs2014':r['oc_bs2014'],'oc_bs_match':r['oc_bs_match'],'oc_bs_gloss':r['oc_bs_gloss'],'oc_bs_gsr':r['oc_bs_gsr'],'oc_bs_all_readings':r['oc_bs_all'],'morph_relation_to_head':r['morph_relation_to_head'],'morph_diff':r['morph_diff'],'oc_schuessler2007':r['oc_schuessler2007'],'schuessler_wordfamily':r['schuessler_wordfamily'],'schuessler_gloss':r['schuessler_gloss'],
      'duan_rhyme_group':r['duan_rhyme_group'],'series_head_rhyme_group':HEADRHYME[s],
      'duan_semantic_remarks':r['duan_youwen_remarks'],'duan_loan_extension_remarks':r['duan_loan_or_extension_remarks'],
      'claimed_core':core,'claimed_core_source':src,'code_core':code,
      'alt_core':altcore,'code_alt_core':alt.replace('alt:',''),'coder':'Claude (first pass, unverified)','coder_note':note,
      'flags':';'.join(flags),
      'src_gloss':'說文解字(大徐本) via shuowen.org data, github.com/shuowenjiezi/shuowen',
      'src_duan':'段玉裁《說文解字注》 via same dataset (duan_notes field)',
      'src_mc':'廣韻 via tshet-uinh 0.15.1 (nk2028); MC notation = Baxter-Sagart 2014 via tshet-uinh-examples baxter.js','src_oc':'BS2014: github.com/digling/cddb datasets/Baxter2014/raw/D_ocbs.tsv (commit 054fb4c); Schuessler 2007: same repo datasets/Schuessler2007',
      'duan_full_notes':r['duan_full']})
os.makedirs(sys.argv[1],exist_ok=True)
with open(os.path.join(sys.argv[1],'youwen_pilot.csv'),'w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
from collections import Counter
print(len(out),Counter(f for o in out for f in o['flags'].split(';') if f))
for o in out:
    if 'rhyme_group_differs_from_head' in o['flags']: print(o['series'],o['char'],o['duan_rhyme_group'])
