#!/usr/bin/env python3
from __future__ import annotations
import base64, json, os, pathlib, time, urllib.error, urllib.request
from datetime import datetime, timezone

ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
DOPPLER_TOKEN_FILE=pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
NOTION_EXEC=ROOT/'reports/lk-compras-unified-sourcing-notion-execution-2026-05-14.json'
OUT=ROOT/'reports/lk-sourcing-ops-v2b-julio-no-manual-values-2026-05-15.json'
NOTION_DB='2b127dc9-e033-805b-81b6-f62f5467ce77'
NOTION_VERSION='2022-06-28'
MARKER='LK OS sourcing ops v2b — Hermes validates exact-size price; Júlio does not fill values — 2026-05-15'


def load_doppler():
    token=os.environ.get('DOPPLER_TOKEN') or DOPPLER_TOKEN_FILE.read_text().strip()
    req=urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
    req.add_header('Authorization','Basic '+base64.b64encode((token+':').encode()).decode())
    with urllib.request.urlopen(req,timeout=60) as r: return json.loads(r.read().decode())


def nh(tok): return {'Authorization':'Bearer '+tok,'Notion-Version':NOTION_VERSION}


def http_json(url, headers, method='GET', payload=None, attempts=4):
    data=None if payload is None else json.dumps(payload,ensure_ascii=False).encode()
    for i in range(attempts):
        req=urllib.request.Request(url,data=data,method=method)
        for k,v in headers.items(): req.add_header(k,v)
        if data is not None: req.add_header('Content-Type','application/json; charset=utf-8')
        try:
            with urllib.request.urlopen(req,timeout=90) as r:
                raw=r.read().decode(); return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            body=e.read().decode(errors='replace')
            if e.code not in {429,500,502,503,504} or i==attempts-1:
                return {'error':f'http_{e.code}','body':body[:1000]}
        except Exception as e:
            if i==attempts-1: return {'error':type(e).__name__,'body':str(e)[:1000]}
        time.sleep(min(20,2**(i+1)))
    return {'error':'request_failed'}


def paragraph(text):
    return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':text[:1900]}}]}}


def heading(text):
    return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':text[:1900]}}]}}


def existing_marker(tok,page_id):
    cursor=None
    while True:
        url=f'https://api.notion.com/v1/blocks/{page_id}/children?page_size=100'
        if cursor: url+='&start_cursor='+cursor
        d=http_json(url,nh(tok))
        for b in d.get('results',[]) if isinstance(d,dict) else []:
            typ=b.get('type')
            if typ and typ in b:
                rich=b[typ].get('rich_text') or b[typ].get('caption') or []
                text=''.join(x.get('plain_text') or (x.get('text') or {}).get('content') or '' for x in rich)
                if MARKER in text: return True
        if not d.get('has_more'): break
        cursor=d.get('next_cursor')
    return False


def main():
    sec=load_doppler(); tok=sec.get('NOTION_TOKEN_LK') or sec.get('NOTION_API_KEY')
    if not tok: raise SystemExit('missing notion token')
    # ensure option exists
    db=http_json(f'https://api.notion.com/v1/databases/{NOTION_DB}',nh(tok),method='PATCH',payload={'properties':{'Decisão Sourcing': {'select': {'options':[{'name':'Precisa validar tamanho','color':'yellow'},{'name':'Hermes validar preço/tamanho','color':'orange'},{'name':'Comprar nacional','color':'green'},{'name':'Importar','color':'blue'},{'name':'Pular','color':'red'},{'name':'Watchlist','color':'gray'}]}}}})
    rows=json.loads(NOTION_EXEC.read_text())['results']
    updated=0; appended=0; errors=[]
    for r in rows:
        page_id=r.get('page_id')
        if not page_id: continue
        props={'Fonte preço tam': {'rich_text':[{'text':{'content':'PENDENTE — Hermes precisa buscar/validar preço exato do tamanho correto em fonte confiável/autenticada. Júlio não preenche valor. Product-level é só sinal/foto, não custo.'}}]}, 'Preço exato tam USD': {'number': None}, 'Custo landed BRL': {'number': None}, 'Venda ideal BRL': {'number': None}}
        # Keep already viable national decisions; otherwise set Hermes validation state.
        if (r.get('properties') or {}).get('Decisão Sourcing') != 'Comprar nacional':
            props['Decisão Sourcing']={'select': {'name':'Hermes validar preço/tamanho'}}
        pr=http_json(f'https://api.notion.com/v1/pages/{page_id}',nh(tok),method='PATCH',payload={'properties':props})
        if pr.get('error'): errors.append({'page_id':page_id,'stage':'page_patch','error':pr.get('error')})
        else: updated+=1
        if not existing_marker(tok,page_id):
            blocks=[heading('Correção Lucas — Júlio não preenche valor'), paragraph(f'{MARKER}. Correção operacional: a validação do preço exato por tamanho é responsabilidade do Hermes/fonte integrada. Júlio não deve preencher preço USD manualmente.'), paragraph('Se Hermes não tiver preço exato do tamanho, manter importação bloqueada/pendente. Não usar KicksDev/StockX product-level como custo. Quando Hermes validar o preço correto, calcular: custo landed = (preço USD + custo trazer USD) × (dólar × 1,05); venda ideal = custo landed × 2.'), paragraph('Júlio continua responsável pela decisão/execução humana: comprar, pular, acompanhar, contato/pagamento quando aprovado e log operacional no Notion.')]
            ap=http_json(f'https://api.notion.com/v1/blocks/{page_id}/children',nh(tok),method='PATCH',payload={'children':blocks})
            if ap.get('error'): errors.append({'page_id':page_id,'stage':'append','error':ap.get('error')})
            else: appended+=1
        time.sleep(.25)
    summary={'status':'completed' if not errors else 'completed_with_errors','generated_at':datetime.now(timezone.utc).isoformat(),'db_error':db.get('error'),'pages_patched':updated,'correction_blocks_appended':appended,'errors':errors}
    OUT.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:summary[k] for k in ['status','pages_patched','correction_blocks_appended','db_error']},ensure_ascii=False))

if __name__=='__main__': main()
