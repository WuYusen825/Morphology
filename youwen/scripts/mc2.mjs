import { 資料 } from 'tshet-uinh';
import * as X from './dist/index.js';
import fs from 'node:fs';
const bx = X.baxter({版本:'2014'});
const inp = JSON.parse(fs.readFileSync(process.argv[2],'utf8')); // [{char, fq}]
const norm = s => (s||'').replace(/[〈［｟〖〘].*?[〉］｠〗〙]/g,'');
const out = inp.map(({char,fq})=>{
  const rd = 資料.query字頭(char).map(r=>({d:r.音韻地位, 反切:r.反切??'', 釋義:(r.釋義||'').slice(0,30)}));
  let best=null, how='none';
  if (rd.length){
    const up=fq?[...fq][0]:null, lo=fq?[...fq][1]:null;
    const U=new Set(up?資料.query字頭(up).map(r=>r.音韻地位.母):[]);
    const L=new Set(lo?資料.query字頭(lo).map(r=>r.音韻地位.韻+r.音韻地位.聲):[]);
    const both=rd.filter(x=>U.has(x.d.母)&&L.has(x.d.韻+x.d.聲));
    const same=rd.filter(x=>x.反切.replace(/[〈〉]/g,'')===fq);
    if (same.length){best=same[0];how='identical_fanqie';}
    else if (both.length){best=both[0];how='initial+rhyme+tone';}
    else { const a=rd.filter(x=>L.has(x.d.韻+x.d.聲)); const b=rd.filter(x=>U.has(x.d.母));
      if(a.length){best=a[0];how='rhyme+tone_only';} else if(b.length){best=b[0];how='initial_only';} else {best=rd[0];how='no_match_first_reading';}}
  }
  return {char, gy_all: rd.map(x=>`${x.d.描述} ${x.反切}切 ${bx(x.d)}`).join(' | '),
    gy_primary: best?best.d.描述:'', gy_fanqie: best?best.反切:'', bs_mc: best?bx(best.d):'', mc_match: how};
});
console.log(JSON.stringify(out));
