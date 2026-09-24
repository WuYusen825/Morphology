# 亦声 vs 普通形声（同声符）的比较统计，v2（2026-09-24）
# 分析集：in_analysis_set=True（大徐标注、剔除新附、只取 亦聲/聲）；普通组只保留在分析集中至少有一个亦声成员的声符（"all"），另报声符配对子集（"matched"）
# 输出 yisheng_summary.csv；--models 另拟合 outcome ~ label + (1|phonetic)（Bayes 变分近似）与 GEE（按声符聚类）作对照，Holm 校正
import json,math,csv,sys,os,collections
R=json.load(open('yisheng_rows.json'))
def lc(n,k): return math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1)
def fisher(a,b,c,d):
    n1=a+b;K=a+c;N=a+b+c+d
    return sum(math.exp(lc(K,x)+lc(N-K,n1-x)-lc(N,n1)) for x in range(a,min(n1,K)+1))
A=[r for r in R if r['in_analysis_set']=='True']
yph={r['phonetic'] for r in A if r['relation']=='亦聲'}
A=[r for r in A if r['phonetic'] in yph]
def matched(rows):
    k=collections.defaultdict(set)
    for r in rows: k[r['phonetic']].add(r['relation'])
    keep={p for p,v in k.items() if v=={'亦聲','聲'}}
    return [r for r in rows if r['phonetic'] in keep],len(keep)
out=[]
def row(h,label,rows,pred,note=''):
    L1=[r for r in rows if r['relation']=='亦聲']; L0=[r for r in rows if r['relation']=='聲']
    a=sum(map(pred,L1)); c=sum(map(pred,L0))
    out.append(dict(hypothesis=h,comparison=label,yisheng_hits=a,yisheng_n=len(L1),yisheng_rate=round(a/len(L1),3) if L1 else '',
        ordinary_hits=c,ordinary_n=len(L0),ordinary_rate=round(c/len(L0),3) if L0 else '',fisher_one_sided='%.2g'%fisher(a,len(L1)-a,c,len(L0)-c),note=note))
def both(h,label,rows,pred,note=''):
    row(h,label+', all phonetics',rows,pred,note); m,k=matched(rows); row(h,label+f', matched phonetics (n={k})',m,pred,note)
mc=[r for r in A if r['mc_relation']!='NA']
oc=[r for r in A if r['morph_relation_auto']!='NA']
both('H1a','MC identical syllable',mc,lambda r:r['mc_relation']=='identical')
both('H1a','OC (BS) identical',oc,lambda r:r['morph_relation_auto']=='I')
ni_oc=[r for r in oc if r['morph_relation_auto']!='I']; ni_mc=[r for r in mc if r['mc_relation']!='identical']
both('H1b','OC R (affix/alternation only) among non-identical',ni_oc,lambda r:r['morph_relation_auto']=='R')
for t in sorted({r['morph_affix_type'] for r in ni_oc if r['morph_affix_type']}):
    row('H1b',f'OC R subtype {t} among non-identical, all phonetics',ni_oc,lambda r,t=t:r['morph_affix_type']==t,'descriptive')
for cat in ('O','O2','V','C'):
    row('H1b',f'OC category {cat} among non-identical, all phonetics',ni_oc,lambda r,cat=cat:r['morph_relation_auto']==cat,'descriptive')
both('H1b','MC tone/voicing alternation among non-identical',ni_mc,lambda r:r['mc_relation']=='tone_voicing_alt')
alt=[r for r in mc if r['mc_relation']=='tone_voicing_alt']
both('H1c','member has departing tone, among tone/voicing alternations',alt,lambda r:r['mc_qusheng_direction']=='member')
row('H1c','head has departing tone, among tone/voicing alternations, all phonetics',alt,lambda r:r['mc_qusheng_direction']=='head','descriptive')
both('H1c','member-departing derivative, among all MC pairs',mc,lambda r:r['mc_qusheng_direction']=='member')
both('H2-confound','paronomastic gloss (definition contains the phonetic)',A,lambda r:r['paronomastic_gloss']=='True')
nopar=[r for r in mc if r['paronomastic_gloss']=='False']
row('H1a-sens','MC identical, paronomastic glosses removed, all phonetics',nopar,lambda r:r['mc_relation']=='identical')
# 同音字对的关系类型（描述）
idp=[r for r in A if r['mc_relation']=='identical']
for t in 'LFCUX':
    row('H1a-types',f'identical pairs of relation type {t}',idp,lambda r,t=t:r['identical_relation_type']==t,'descriptive; Claude first-pass, unblinded')
# 段注、小徐层（H3，探索性）
yi=[r for r in A if r['relation']=='亦聲']
def layer(name,rows):
    m=[r for r in rows if r['mc_relation']!='NA']; n=len(m)
    out.append(dict(hypothesis='H3',comparison=name+f' ({len(rows)} items)',yisheng_n=n,yisheng_hits=sum(r['mc_relation']=='identical' for r in m),
        yisheng_rate=round(sum(r['mc_relation']=='identical' for r in m)/n,3) if n else '',note='MC-identical among items with MC; semantic codes pending'))
layer('Da Xu + Duan both label',[r for r in yi if r['duan_label']=='亦聲'])
layer('Da Xu labels, Duan drops',[r for r in yi if r['duan_label']=='無'])
layer('Da Xu labels, Duan text missing in data',[r for r in yi if r['duan_label']=='缺段注'])
layer('Da Xu + Xiao Xu both label (aligned)',[r for r in yi if r['xiaoxu_label']=='亦聲'])
layer('Da Xu labels, Xiao Xu drops (aligned)',[r for r in yi if r['xiaoxu_label']=='無'])
ex=[r for r in R if r['label_source']!='daxu']
layer('Duan/Xiao Xu only (extra rows, 會意 in Da Xu)',ex)
layer('Da Xu 聲, Duan adds 亦聲',[r for r in A if r['relation']=='聲' and r['duan_label']=='亦聲'])

# H4（探索性）：归在以声符为部首之部的亦声字（普通形声字无一如此归部，所以只能在亦声字内部比较）
def h4(name,pred):
    rs=[r for r in yi if r['mc_relation']!='NA']; a=[r for r in rs if r['filed_under_phonetic']=='True']; b=[r for r in rs if r['filed_under_phonetic']=='False']
    x=sum(map(pred,a)); y=sum(map(pred,b))
    out.append(dict(hypothesis='H4',comparison=name+' (filed under phonetic vs other labels)',yisheng_hits=x,yisheng_n=len(a),yisheng_rate=round(x/len(a),3),
        ordinary_hits=y,ordinary_n=len(b),ordinary_rate=round(y/len(b),3),fisher_one_sided='%.2g'%min(fisher(x,len(a)-x,y,len(b)-y),fisher(y,len(b)-y,x,len(a)-x)),
        note=f"columns: filed-under-phonetic 亦聲 vs other 亦聲; two-sided-ish (min of one-sided); {sum(r['filed_under_phonetic']=='True' for r in yi)} of {len(yi)} labels filed under phonetic; no plain 聲 is"))
h4('MC identical',lambda r:r['mc_relation']=='identical')
h4('MC tone/voicing alternation',lambda r:r['mc_relation']=='tone_voicing_alt')

if '--models' in sys.argv:
    import pandas as pd, numpy as np, statsmodels.api as sm, statsmodels.formula.api as smf
    from statsmodels.genmod.bayes_mixed_glm import BinomialBayesMixedGLM
    from statsmodels.stats.multitest import multipletests
    tests=[('H1a','MC identical',mc,lambda r:r['mc_relation']=='identical'),
           ('H1b','MC tone/voicing alt | non-identical',ni_mc,lambda r:r['mc_relation']=='tone_voicing_alt'),
           ('H1b-OC','OC R | non-identical',ni_oc,lambda r:r['morph_relation_auto']=='R'),
           ('H1c','member departing | alternation',alt,lambda r:r['mc_qusheng_direction']=='member')]
    res=[]
    sub=lambda rows:[r for r in rows if r.get('filed_under_phonetic')!='True']
    tests+=[(h+' (excl. filed-under-phonetic)',n,sub(rows),p) for h,n,rows,p in tests]
    for h,name,rows,pred in tests:
        df=pd.DataFrame(dict(y=[int(pred(r)) for r in rows],label=[int(r['relation']=='亦聲') for r in rows],phon=[r['phonetic'] for r in rows]))
        g=smf.gee('y ~ label',groups='phon',data=df,family=sm.families.Binomial(),cov_struct=sm.cov_struct.Exchangeable()).fit()
        b,se=g.params['label'],g.bse['label']
        vb=BinomialBayesMixedGLM.from_formula('y ~ label',{'phon':'0 + C(phon)'},df).fit_vb()
        i=list(vb.model.exog_names).index('label'); bm,sd=vb.fe_mean[i],vb.fe_sd[i]
        p1=g.pvalues['label']/2 if b>0 else 1-g.pvalues['label']/2   # 单侧（方向已预先设定）
        res.append(dict(hypothesis=h,outcome=name,n=len(df),n_phonetics=df.phon.nunique(),
            gee_OR=round(math.exp(b),2),gee_CI95=f'{math.exp(b-1.96*se):.2f}-{math.exp(b+1.96*se):.2f}',gee_p_one_sided=p1,
            glmm_vb_OR=round(math.exp(bm),2),glmm_vb_CI95=f'{math.exp(bm-1.96*sd):.2f}-{math.exp(bm+1.96*sd):.2f}',
            glmm_vb_z=round(bm/sd,2)))
    k=len(res)//2   # Holm 分别在主分析和"剔除本部亦声"两组内部做
    adj=list(multipletests([x['gee_p_one_sided'] for x in res[:k]],method='holm')[1])+list(multipletests([x['gee_p_one_sided'] for x in res[k:]],method='holm')[1])
    for x,a in zip(res,adj): x['gee_p_one_sided']='%.2g'%x['gee_p_one_sided']; x['holm_p']='%.2g'%a
    with open(os.path.join(sys.argv[1],'yisheng_models.csv'),'w',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f,fieldnames=list(res[0]));w.writeheader();w.writerows(res)
    for x in res: print(x)

with open(os.path.join(sys.argv[1],'yisheng_summary.csv'),'w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
print('analysis set:',collections.Counter(r['relation'] for r in A),'phonetics',len(yph))
for o in out: print(o['hypothesis'],o['comparison'],f"{o['yisheng_hits']}/{o['yisheng_n']}",f"{o.get('ordinary_hits','')}/{o.get('ordinary_n','')}",o.get('fisher_one_sided',''))
