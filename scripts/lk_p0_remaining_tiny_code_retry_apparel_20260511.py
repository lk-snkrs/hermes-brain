#!/usr/bin/env python3
"""Retry the 3 apparel Tiny codigo writes using payload without grade to avoid Tiny normalizing S-P/L-G names to S/P/L/G."""
import base64,json,pathlib,time,urllib.parse,urllib.request
from copy import deepcopy
from datetime import datetime, timezone
ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/'reports/lk-p0-remaining-tiny-code-execution-retry-apparel-2026-05-11.json'
CANDIDATES=[
  {'id':'1069542767','title':'Moletom Alo Yoga Cropped Serenity Coverup Black Preto','size':'S/P','target':'ALO-8506462-S'},
  {'id':'1069544315','title':'Calça Saint Studio Alfaiataria Leve Prega Dupla Cinza','size':'L/G','target':'SST-4542302-L'},
  {'id':'1069930823','title':'Camiseta Pace Buero Washed Black Preto','size':'S/P','target':'PAC-1197278-S'},
]
dt=pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token').read_text().strip()
req=urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
req.add_header('Authorization','Basic '+base64.b64encode((dt+':').encode()).decode())
with urllib.request.urlopen(req,timeout=60) as resp: TOKEN=json.load(resp)['TINY_API_TOKEN']
def call(method, params):
    data=urllib.parse.urlencode({**params,'token':TOKEN,'formato':'json'}).encode()
    req=urllib.request.Request(f'https://api.tiny.com.br/api2/{method}.php',data=data,method='POST')
    with urllib.request.urlopen(req,timeout=90) as r: return json.load(r)
def obter(id):
    time.sleep(5)
    ret=call('produto.obter', {'id':id}).get('retorno',{})
    return ret.get('status'), ret.get('produto') or {}, ret
def alterar(payload):
    time.sleep(5)
    payload=deepcopy(payload); payload.setdefault('sequencia','1')
    body={'produtos':[{'produto':payload}]}
    return call('produto.alterar', {'produto':json.dumps(body, ensure_ascii=False)})
def snap(p):
    return {k:deepcopy(p.get(k)) for k in ['nome','codigo','preco','preco_promocional','unidade','origem','situacao','tipo','grade','idProdutoPai'] if k in p}
def changes(before, after):
    out=[]
    for k in before:
        if k=='codigo': continue
        if before.get(k)!=after.get(k): out.append({'field':k,'before':before.get(k),'after':after.get(k)})
    return out
def payload_from(p, codigo):
    # No grade field: avoids Tiny recalculating display name punctuation for apparel sizes.
    keep=['id','nome','unidade','preco','preco_promocional','origem','situacao','tipo']
    pl={k:deepcopy(p.get(k)) for k in keep if k in p}
    pl['id']=str(p.get('id')); pl['codigo']=codigo; pl['sequencia']='1'
    return pl
results=[]
for c in CANDIDATES:
    r={'tiny_child_id':c['id'],'product_title':c['title'],'size':c['size'],'target_codigo':c['target'],'success':False}
    status,before,raw=obter(c['id']); r['precheck_status']=status; r['before_snapshot']=snap(before); r['rollback_codigo']=before.get('codigo') or ''
    if (before.get('codigo') or '') == c['target']:
        r['write_attempted']=False; r['success']=True; r['after_snapshot']=snap(before); r['non_code_changes_detected']=[]; results.append(r); continue
    if before.get('codigo'):
        r['error']='refusing to overwrite non-empty codigo'; results.append(r); continue
    wr=alterar(payload_from(before, c['target'])); wret=wr.get('retorno',{})
    r['write_attempted']=True; r['write_status']=wret.get('status'); r['write_status_processamento']=wret.get('status_processamento'); r['write_errors']=wret.get('erros') or wret.get('erro')
    vstatus,after,vraw=obter(c['id']); r['verify_status']=vstatus; r['after_snapshot']=snap(after); ch=changes(snap(before), snap(after)); r['non_code_changes_detected']=ch
    r['success']=((after.get('codigo') or '')==c['target'] and not ch)
    if not r['success']:
        if (after.get('codigo') or '') != (before.get('codigo') or '') or ch:
            rb=alterar(payload_from(before, before.get('codigo') or ''))
            rbstatus,rbafter,_=obter(c['id'])
            r['rollback']={'rollback_api_return':rb.get('retorno',rb),'rollback_verify_status':rbstatus,'rollback_after_snapshot':snap(rbafter),'rollback_success':(rbafter.get('codigo') or '')==(before.get('codigo') or '') and not changes(snap(before), snap(rbafter))}
        else:
            r['rollback']={'not_needed':True}
    results.append(r)
report={'generated_at':datetime.now(timezone.utc).isoformat(),'scope':'Retry 3 apparel Tiny codigo writes without grade in payload to avoid name punctuation mutation','guardrails':['Tiny codigo only','no Shopify write','before/after non-code fields checked','rollback on any non-code mutation'], 'counts':{'candidates':len(results),'write_attempted':sum(1 for x in results if x.get('write_attempted')),'success':sum(1 for x in results if x.get('success')),'failed':sum(1 for x in results if not x.get('success'))}, 'results':results}
OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'report':str(OUT),'counts':report['counts'],'results':[{'id':x['tiny_child_id'],'success':x['success'],'after_codigo':(x.get('after_snapshot') or {}).get('codigo'),'changes':x.get('non_code_changes_detected')} for x in results]}, ensure_ascii=False, indent=2))
