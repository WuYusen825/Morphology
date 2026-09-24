# BS 2014 构拟成分比较：成员字 vs 声符字，自动归类语音差异类型
# I=完全相同；R=仅前缀/后缀/咽化(A/B型)/介音r 不同（BS 体系内的规则词缀或交替）；
# O=声干相同但声母不同（同部位）；O2=声母不同部位；V=主元音不同；C=韵尾不同；NA=缺构拟
import re
PLACE=[set('k kʰ g ŋ ŋ̊ q qʰ ɢ ʔ h ɦ x'.split()),set('t tʰ d n n̥ l l̥ r r̥ s z ts tsʰ dz'.split()),set('p pʰ b m m̥ w'.split()),set('j'.split())]
def norm(x): return re.sub(r'[\[\]()<>]','',x or '')
def parts(r):
    ini=norm(r['PubIni']); fin=norm(r['PubFin'])
    phar='ˤ' in ini; ini=ini.replace('ˤ','')
    glottal=fin.endswith('ʔ'); fin=fin.rstrip('ʔ')   # BS 把 *-ʔ 写在韵母栏，这里当作后缀处理
    m=re.match(r'^([aeiouəɨA]+)(.*)$',fin); v,coda=(m.group(1),m.group(2)) if m else (fin,'')
    suf=('ʔ' if glottal else '')+norm(r['PubSuf'])
    return dict(pre=norm(r['PubPre']),ini=ini,phar=phar,med=norm(r['PubMed']),v=v,coda=coda,suf=suf,
                uncertain=any(ch in (r['PubFull'] or '') for ch in '[]()'))
def place(i):
    i=i.split('.')[-1].replace('ʷ','')
    for n,s in enumerate(PLACE):
        if i in s: return n
    return None
def compare(a,b):
    if not a or not b: return 'NA',''
    A,B=parts(a),parts(b); diff=[k for k in ('pre','ini','phar','med','v','coda','suf') if A[k]!=B[k]]
    if not diff: cat='I'
    elif set(diff)<= {'pre','phar','med','suf'}: cat='R'
    elif 'coda' in diff: cat='C'
    elif 'v' in diff: cat='V'
    else: cat='O' if place(A['ini'])==place(B['ini']) and place(A['ini']) is not None else 'O2'
    return cat, ','.join(diff)+(';uncertain' if A['uncertain'] or B['uncertain'] else '')
def affix_detail(a,b):
    # R 类细分：列出成员字相对声符字在哪些成分上不同，写作"成分:声符值>成员值"，∅ 表示空
    if not a or not b: return ''
    A,B=parts(a),parts(b); out=[]
    for k in ('pre','phar','med','suf'):
        if A[k]!=B[k]:
            f=lambda x:('ˤ' if x else '∅') if k=='phar' else (x or '∅')
            out.append(f'{k}:{f(B[k])}>{f(A[k])}')
    return ';'.join(out)
def affix_type(a,b):
    # 单一差异时给出具体类型，便于按词缀拆分 R；多处差异记 multi
    d=affix_detail(a,b).split(';') if affix_detail(a,b) else []
    if len(d)!=1: return 'multi' if d else ''
    k,v=d[0].split(':'); src,tgt=v.split('>')
    if k=='suf': return 'suf_'+('+'+tgt if src=='∅' else ('-'+src if tgt=='∅' else src+'>'+tgt))
    if k=='pre': return 'pre_'+('+'+tgt if src=='∅' else ('-'+src if tgt=='∅' else src+'>'+tgt))
    if k=='phar': return 'phar_'+('lost' if src=='ˤ' else 'gained')
    return 'med_'+('+'+tgt if src=='∅' else ('-'+src if tgt=='∅' else src+'>'+tgt))
