#!/usr/bin/env python3
from __future__ import annotations
import base64, json, os, pathlib, time, urllib.error, urllib.request
from datetime import datetime, timezone
from typing import Any

ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
DOPPLER_TOKEN_FILE=pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
IN_JSON=ROOT/'reports/lk-sourcing-julio-decision-ranking-v9-2026-05-15.json'
OUT_JSON=ROOT/'reports/lk-sourcing-execution-control-v10-2026-05-15.json'
OUT_MD=ROOT/'reports/lk-sourcing-execution-control-v10-2026-05-15.md'
MC_MD=ROOT/'areas/lk/rotinas/mission-control-sourcing-execution-control-v10-2026-05-15.md'
NOTION_DB='2b127dc9-e033-805b-81b6-f62f5467ce77'
NOTION_VERSION='2022-06-28'
MARKER='LK OS sourcing v10 — fila de execução pendente Júlio — 2026-05-15'

def now(): return datetime.now(timezone.utc).isoformat()
def brl(v): return 'n/d' if v is None else f'R$ {float(v):,.2f}'.replace(',','X').replace('.',',').replace('X','.')
def usd(v): return 'n/d' if v is None else f'US$ {float(v):,.2f}'
def pct(v): return 'n/d' if v is None else f'{float(v)*100:.1f}%'

def load_doppler():
    token=os.environ.get('DOPPLER_TOKEN') or DOPPLER_TOKEN_FILE.read_text().strip()
    req=urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
    req.add_header('Authorization','Basic '+base64.b64encode((token+':').encode()).decode())
    with urllib.request.urlopen(req,timeout=60) as r: return json.loads(r.read().decode())

def nh(tok): return {'Authorization':'Bearer '+tok,'Notion-Version':NOTION_VERSION}

def http_json(url,headers,method='GET',payload=None,attempts=4):
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
            if e.code in {429,500,502,503,504} and i<attempts-1:
                time.sleep(3*(i+1)); continue
            return {'error':f'http_{e.code}','body':body[:1000]}
        except Exception as e:
            if i<attempts-1: time.sleep(2*(i+1)); continue
            return {'error':type(e).__name__,'body':str(e)[:1000]}
    return {'error':'request_failed'}

def paragraph(text): return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':text[:1900]}}]}}
def heading(text): return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':text[:1900]}}]}}

def page_has_marker(tok,page_id):
    d=http_json(f'https://api.notion.com/v1/blocks/{page_id}/children?page_size=100',nh(tok))
    for b in d.get('results',[]) if isinstance(d,dict) else []:
        typ=b.get('type')
        if typ and typ in b:
            rich=b[typ].get('rich_text') or b[typ].get('caption') or []
            text=''.join(x.get('plain_text') or (x.get('text') or {}).get('content') or '' for x in rich)
            if MARKER in text: return True
    return False

def execution_status(row:dict[str,Any])->str:
    pr=row.get('priority_v9','')
    if pr.startswith('P1'): return 'Pendente Júlio — P1'
    if pr.startswith('P2'): return 'Pendente Júlio — P2'
    if pr.startswith('P3'): return 'Pendente monitoramento'
    return 'Sem ação agora'

def blocker(row:dict[str,Any])->str:
    route=row.get('route_recommended_v9') or row.get('best_route') or 'n/d'
    if route == 'Importar':
        return 'Bloqueio humano: Júlio confirmar disponibilidade do marketplace/importador e decidir compra manualmente. Hermes não compra, não reserva e não paga.'
    if route == 'Comprar nacional':
        return 'Bloqueio humano: Júlio confirmar anúncio Droper, tamanho e disponibilidade antes de comprar manualmente. Hermes não compra e não contata vendedor.'
    if row.get('priority_v9','').startswith('P3'):
        return 'Monitorar preço. Só vira compra quando margem >=30% ou Lucas/Júlio aprovar exceção.'
    return 'Sem compra recomendada agora.'

def main():
    sec=load_doppler()
    notion_token=sec.get('NOTION_TOKEN_LK') or sec.get('NOTION_API_KEY')
    if not notion_token: raise SystemExit('missing Notion token')
    payload=json.loads(IN_JSON.read_text())
    rows=payload.get('rows') or []
    for r in rows:
        r['execution_status_v10']=execution_status(r)
        r['execution_blocker_v10']=blocker(r)
        r['execution_updated_at_v10']=now()
    db=http_json(f'https://api.notion.com/v1/databases/{NOTION_DB}',nh(notion_token),method='PATCH',payload={'properties':{
        'Status Execução Sourcing': {'select': {}},
        'Bloqueio Execução': {'rich_text': {}},
        'Atualizado Hermes': {'rich_text': {}}
    }})
    errors=[]; pages_updated=0; blocks_appended=0
    for r in rows:
        line=(f"{MARKER}. Status: {r['execution_status_v10']}. Ranking #{r.get('ranking_v9')} — {r.get('priority_v9')}. "
              f"Rota {r.get('route_recommended_v9')}; custo {brl(r.get('product_cost_brl'))}; site LK {brl(r.get('lk_site_price_brl') or r.get('lk_current_price_brl'))}; margem {pct(r.get('best_route_margin_pct'))}. "
              f"{r['execution_blocker_v10']}")
        props={
            'Status Execução Sourcing': {'select': {'name': r['execution_status_v10']}},
            'Bloqueio Execução': {'rich_text':[{'text':{'content':r['execution_blocker_v10'][:1800]}}]},
            'Atualizado Hermes': {'rich_text':[{'text':{'content':now()}}]}
        }
        pr=http_json(f'https://api.notion.com/v1/pages/{r["page_id"]}',nh(notion_token),method='PATCH',payload={'properties':props})
        if pr.get('error'): errors.append({'page_id':r['page_id'],'patch_error':pr})
        else: pages_updated+=1
        if not page_has_marker(notion_token,r['page_id']):
            ap=http_json(f'https://api.notion.com/v1/blocks/{r["page_id"]}/children',nh(notion_token),method='PATCH',payload={'children':[heading('Fila de execução pendente'), paragraph(line), paragraph('Estado intencional: pendente para Júlio/humano. Nenhuma compra, reserva, contato, pagamento ou mensagem foi executada pelo Hermes.')]})
            if ap.get('error'): errors.append({'page_id':r['page_id'],'append_error':ap})
            else: blocks_appended+=1
        time.sleep(.15)
    counts={}
    for r in rows: counts[r['execution_status_v10']]=counts.get(r['execution_status_v10'],0)+1
    out={'status':'completed' if not errors else 'completed_with_errors','generated_at':now(),'cards':len(rows),'pages_updated':pages_updated,'blocks_appended':blocks_appended,'db_error':db.get('error'),'execution_counts':counts,'not_performed':['purchase','reservation','supplier_contact','whatsapp_send','payment_schedule','shopify_write','tiny_write','merchant_write'],'errors':errors,'rows':rows}
    OUT_JSON.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    lines=['# LK Sourcing v10 — Fila de execução pendente Júlio','',f"Generated: `{out['generated_at']}`",'',f"- Cards atualizados: {pages_updated}/{len(rows)}",f"- Blocos adicionados: {blocks_appended}",'','## Status']
    for k,v in counts.items(): lines.append(f"- {k}: {v}")
    lines += ['','## Fila']
    for r in sorted(rows,key=lambda x:x.get('ranking_v9') or 999):
        lines += [f"### #{r.get('ranking_v9')} — {r.get('model')} — BR {r.get('br_size')}",f"- Status: `{r['execution_status_v10']}`",f"- Rota: {r.get('route_recommended_v9')}",f"- Custo: {brl(r.get('product_cost_brl'))}",f"- Site LK: {brl(r.get('lk_site_price_brl') or r.get('lk_current_price_brl'))}",f"- Margem: {pct(r.get('best_route_margin_pct'))}",f"- Bloqueio: {r['execution_blocker_v10']}",'']
    OUT_MD.write_text('\n'.join(lines)+'\n')
    MC_MD.write_text('\n'.join(lines)+'\n')
    print(json.dumps({k:out[k] for k in ['status','cards','pages_updated','blocks_appended','db_error','execution_counts']},ensure_ascii=False))
if __name__=='__main__': main()
