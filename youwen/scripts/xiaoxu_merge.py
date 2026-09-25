# 小徐本对照：合并第一轮（yisheng_daxu_xiaoxu.csv，70 条可靠对齐）与第二轮（yisheng_xiaoxu_round2_reads.tsv，157 条逐条人工核读，2026-09-25）
# 第二轮做法：锚点 + 候选定位后，由 4 个子代理在四部叢刊本電子文本（kanripo KR1j0019，已归一化）里逐条读许慎说解，引文逐字核对过
# 分层（layer）：both = 小徐也作"亦聲"；daxu_only = 小徐作"聲"、无"聲"字或他字"聲"；
#   unknown = 电子本缺文（未找到）、大徐新附（小徐本无）、卷二十五（今本据大徐补，不作证据）、反切作"切"疑据大徐补入（詔）
# 第三轮（2026-09-25 晚）：电子本缺文的条目，由 4 个子代理在国家图书馆扫描的四部叢刊本《說文繫傳通釋》（Qu 上传到 GitHub Release「说文解字」）上逐页核读，
#   结果见 yisheng_xiaoxu_round3_scan_reads.tsv（含 PDF 页码与叶次）。瑁 原书此处空白（许说到'從玉'后缺），列为 unknown；糶 反切作'他弔切'，与 詔 同样疑据大徐补入。
# 用法：python3 scripts/xiaoxu_merge.py  → yisheng_xiaoxu_collation_final.csv
import csv,collections,re
R1={r['sw_id']:r for r in csv.DictReader(open('yisheng_daxu_xiaoxu.csv',encoding='utf-8-sig')) if r['daxu_yisheng']=='True'}
R2={r['sw_id']:r for r in csv.DictReader(open('yisheng_xiaoxu_round2_reads.tsv',encoding='utf-8'),delimiter='\t')}
DS={r['sw_id']:r for r in csv.DictReader(open('yisheng_dataset.csv',encoding='utf-8-sig')) if r['relation']=='亦聲' and r['label_source']=='daxu'}
FIX={'5302':('亦聲','第一轮误判：小徐作"从衣从日亦日聲"，即亦聲，只是语序不同')}
SUSPECT={'1526':'反切作"之紹切"（小徐通例作"反"），疑此条据大徐补入','3850':'扫描本反切作"他弔切"（小徐通例作"反"），疑此条据大徐补入'}
R3={r['sw_id']:r for r in csv.DictReader(open('yisheng_xiaoxu_round3_scan_reads.tsv',encoding='utf-8'),delimiter='\t')}
rows=[]
for i,r in R1.items():
    d=DS.get(i,{})
    if r['agreement'] in('both','daxu_only'):
        read='亦聲' if r['agreement']=='both' else ('聲' if re.search('聲',r['xiaoxu_text'].split('臣鍇')[0]) else '無聲'); src='round1'; quote=r['xiaoxu_text']; note=''; ju=''
    else:
        t=R2[i]; read=t['reading']; src='round2'; quote=t['quote']; note=t['note']; ju=t['juan']
    if i in FIX: read,note=FIX[i]
    if read=='未找到' and i in R3:
        t=R3[i]; src='round3_scan'; quote=t['quote']; note=(t['note']+f" [扫描 {t['pdf']} p{t['pdf_page']} {t['half']} {t['leaf']}]").strip()
        read={'亦聲':'亦聲','聲':'聲','無聲':'無聲','其他聲':'其他聲','未見':'未見','不清':'原书空白不清'}[t['reading']]
    if read=='未找到' and d.get('is_xinfu')=='True': why='新附'
    elif ju=='25': why='卷二十五据大徐补'
    elif read=='未找到': why='电子本缺文'
    elif read=='原书空白不清': why='原书空白'
    elif read=='未見': why='扫描本未见'
    elif i in SUSPECT: why='疑据大徐补入'; note=SUSPECT[i]
    else: why=''
    layer='unknown' if why else ('both' if read=='亦聲' else 'daxu_only')
    rows.append(dict(sw_id=i,char=r['char'],phonetic=d.get('phonetic','亦'),in_analysis_set=d.get('in_analysis_set','False (亦 false hit)'),
        daxu_gloss=r['daxu_gloss'],xiaoxu_reading=read,unknown_reason=why,layer=layer,round=src,xiaoxu_juan=ju,xiaoxu_quote=quote,note=note))
rows.sort(key=lambda x:int(x['sw_id']))
with open('yisheng_xiaoxu_collation_final.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
A=[r for r in rows if r['in_analysis_set']=='True']
print('all',len(rows),collections.Counter(r['layer'] for r in rows))
print('analysis set',len(A),collections.Counter(r['layer'] for r in A),collections.Counter(r['unknown_reason'] for r in A))
print(collections.Counter(r['xiaoxu_reading'] for r in A))
