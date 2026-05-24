#!/usr/bin/env python3
from __future__ import annotations
import base64, json, os, pathlib, time, urllib.error, urllib.request
from datetime import datetime, timezone
from typing import Any

ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
DOPPLER_TOKEN_FILE=pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
IN_JSON=ROOT/'reports/lk-sourcing-decision-fields-v8-2026-05-15.json'
OUT_JSON=ROOT/'reports/lk-sourcing-julio-decision-ranking-v9-2026-05-15.json'
OUT_MD=ROOT/'reports/lk-sourcing-julio-decision-ranking-v9-2026-05-15.md'
MC_MD=ROOT/'areas/lk/rotinas/mission-control-sourcing-julio-decision-ranking-v9-2026-05-15.md'
NOTION_DB='2b127dc9-e033-805b-81b6-f62f5467ce77'
NOTION_VERSION='2022-06-28'
MARKER='LK OS sourcing v9 — Mesa de Decisão Júlio — 2026-05-15'

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

def priority(row: dict[str,Any]) -> str:
    decision=row.get('decision_v8') or row.get('decision_v7')
    margin=row.get('best_route_margin_pct')
    if decision == 'Importar' and margin is not None and margin >= 0.50: return 'P1 — Comprar primeiro'
    if decision in {'Importar','Comprar nacional'} and margin is not None and margin >= 0.30: return 'P2 — Comprar se orçamento permitir'
    if decision == 'Watchlist': return 'P3 — Monitorar preço'
    return 'P4 — Não comprar agora'

def action_text(row: dict[str,Any], rank: int) -> str:
    decision=row.get('decision_v8') or row.get('decision_v7')
    route=row.get('best_route') or 'n/d'
    if decision == 'Importar':
        return f'#{rank} — Importar via menor StockX/GOAT validado. Júlio confere disponibilidade operacional/importador e decide compra; não precisa preencher preço.'
    if decision == 'Comprar nacional':
        return f'#{rank} — Comprar nacional/Droper se o anúncio ainda estiver disponível e tamanho bater. Júlio decide compra; sem preencher preço.'
    if decision == 'Watchlist':
        return f'#{rank} — Monitorar. Só comprar se Droper ou StockX/GOAT cair e margem subir para >=30%.'
    return f'#{rank} — Não comprar agora. Margem insuficiente ou custo indisponível.'

def main():
    sec=load_doppler()
    notion_token=sec.get('NOTION_TOKEN_LK') or sec.get('NOTION_API_KEY')
    if not notion_token: raise SystemExit('missing Notion token')
    payload=json.loads(IN_JSON.read_text())
    rows=payload.get('rows') or []
    # Rank by actionability: P1/P2 first, then margin descending, then lower product cost.
    order={'P1 — Comprar primeiro':1,'P2 — Comprar se orçamento permitir':2,'P3 — Monitorar preço':3,'P4 — Não comprar agora':4}
    enriched=[]
    for r in rows:
        rr=dict(r)
        rr['priority_v9']=priority(rr)
        rr['route_recommended_v9']=rr.get('best_route') or 'n/d'
        enriched.append(rr)
    enriched.sort(key=lambda r:(order.get(r['priority_v9'],9), -(r.get('best_route_margin_pct') or -9), r.get('product_cost_brl') or 999999))
    for i,r in enumerate(enriched,1):
        r['ranking_v9']=i
        r['julio_next_action_v9']=action_text(r,i)

    db=http_json(f'https://api.notion.com/v1/databases/{NOTION_DB}',nh(notion_token),method='PATCH',payload={'properties':{
        'Ranking Sourcing': {'number': {}},
        'Prioridade Sourcing': {'select': {}},
        'Rota recomendada': {'select': {}},
        'Próxima ação Júlio': {'rich_text': {}}
    }})
    errors=[]; pages_updated=0; blocks_appended=0
    for r in enriched:
        summary=(f"{MARKER}. Ranking #{r['ranking_v9']} | {r['priority_v9']} | Rota: {r['route_recommended_v9']} | "
                 f"Preço site LK {brl(r.get('lk_site_price_brl') or r.get('lk_current_price_brl'))} | "
                 f"Droper {brl(r.get('droper_price_brl'))} | StockX/GOAT {usd(r.get('stockx_goat_price_usd'))} | "
                 f"Custo {brl(r.get('product_cost_brl'))} | Margem {pct(r.get('best_route_margin_pct'))}. "
                 f"{r['julio_next_action_v9']}")
        props={
            'Ranking Sourcing': {'number': r['ranking_v9']},
            'Prioridade Sourcing': {'select': {'name': r['priority_v9']}},
            'Rota recomendada': {'select': {'name': r['route_recommended_v9']}},
            'Próxima ação Júlio': {'rich_text':[{'text':{'content':r['julio_next_action_v9'][:1800]}}]}
        }
        pr=http_json(f'https://api.notion.com/v1/pages/{r["page_id"]}',nh(notion_token),method='PATCH',payload={'properties':props})
        if pr.get('error'): errors.append({'page_id':r['page_id'],'patch_error':pr})
        else: pages_updated+=1
        if not page_has_marker(notion_token,r['page_id']):
            ap=http_json(f'https://api.notion.com/v1/blocks/{r["page_id"]}/children',nh(notion_token),method='PATCH',payload={'children':[heading('Mesa de Decisão Júlio'), paragraph(summary), paragraph('Campos decisivos: Preço Droper, menor StockX/GOAT, custo do produto e preço atual no site LK. Preço médio não é usado para decidir compra.')]})
            if ap.get('error'): errors.append({'page_id':r['page_id'],'append_error':ap})
            else: blocks_appended+=1
        time.sleep(.15)
    counts={}
    for r in enriched: counts[r['priority_v9']]=counts.get(r['priority_v9'],0)+1
    out={'status':'completed' if not errors else 'completed_with_errors','generated_at':now(),'cards':len(enriched),'pages_updated':pages_updated,'blocks_appended':blocks_appended,'db_error':db.get('error'),'priority_counts':counts,'not_performed':['purchase','reservation','supplier_contact','whatsapp_send','payment_schedule','shopify_write','tiny_write','merchant_write'],'errors':errors,'rows':enriched}
    OUT_JSON.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    lines=['# LK Sourcing v9 — Mesa de Decisão Júlio','',f"Generated: `{out['generated_at']}`",'',f"- Cards atualizados: {pages_updated}/{len(enriched)}",f"- Blocos adicionados: {blocks_appended}",'','## Ordem de execução sugerida']
    for r in enriched:
        lines += [f"### #{r['ranking_v9']} — {r['model']} — BR {r['br_size']}",f"- Prioridade: `{r['priority_v9']}`",f"- Decisão: `{r.get('decision_v8') or r.get('decision_v7')}`",f"- Rota recomendada: {r['route_recommended_v9']}",f"- Preço site LK: {brl(r.get('lk_site_price_brl') or r.get('lk_current_price_brl'))}",f"- Preço Droper: {brl(r.get('droper_price_brl'))}",f"- Preço StockX/GOAT: {usd(r.get('stockx_goat_price_usd'))}",f"- Custo produto: {brl(r.get('product_cost_brl'))}",f"- Margem: {pct(r.get('best_route_margin_pct'))}",f"- Próxima ação Júlio: {r['julio_next_action_v9']}",'']
    OUT_MD.write_text('\n'.join(lines)+'\n')
    MC_MD.write_text('\n'.join(lines)+'\n')
    print(json.dumps({k:out[k] for k in ['status','cards','pages_updated','blocks_appended','db_error','priority_counts']},ensure_ascii=False))
if __name__=='__main__': main()
