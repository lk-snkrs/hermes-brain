#!/usr/bin/env python3
from __future__ import annotations
import base64, json, os, pathlib, time, urllib.error, urllib.request
from datetime import datetime, timezone

ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
DOPPLER_TOKEN_FILE=pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
IN_JSON=ROOT/'reports/lk-sourcing-execution-control-v10-2026-05-15.json'
OUT_JSON=ROOT/'reports/lk-sourcing-p1-approval-packet-v11-2026-05-15.json'
OUT_MD=ROOT/'reports/lk-sourcing-p1-approval-packet-v11-2026-05-15.md'
MC_MD=ROOT/'areas/lk/rotinas/mission-control-sourcing-p1-approval-packet-v11-2026-05-15.md'
NOTION_DB='2b127dc9-e033-805b-81b6-f62f5467ce77'
NOTION_VERSION='2022-06-28'
MARKER='LK OS sourcing v11 — pacote P1 para aprovação de compra manual — 2026-05-15'

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

def main():
    sec=load_doppler()
    notion_token=sec.get('NOTION_TOKEN_LK') or sec.get('NOTION_API_KEY')
    if not notion_token: raise SystemExit('missing Notion token')
    rows=(json.loads(IN_JSON.read_text()).get('rows') or [])
    p1=[r for r in rows if str(r.get('priority_v9','')).startswith('P1')]
    p1.sort(key=lambda r:r.get('ranking_v9') or 999)
    total_cost=sum(float(r.get('product_cost_brl') or 0) for r in p1)
    expected_site=sum(float(r.get('lk_site_price_brl') or r.get('lk_current_price_brl') or 0) for r in p1)
    expected_gross=expected_site-total_cost
    blended_margin=(expected_gross/expected_site) if expected_site else None
    db=http_json(f'https://api.notion.com/v1/databases/{NOTION_DB}',nh(notion_token),method='PATCH',payload={'properties':{
        'Lote Compra': {'select': {}},
        'Aprovação Compra': {'select': {}},
        'Resumo Aprovação': {'rich_text': {}}
    }})
    errors=[]; pages_updated=0; blocks_appended=0
    for r in p1:
        approval=(f"P1 pronto para decisão manual. Ranking #{r.get('ranking_v9')}; rota {r.get('route_recommended_v9')}; "
                  f"SKU {r.get('sku_lk')}; BR {r.get('br_size')}; custo {brl(r.get('product_cost_brl'))}; "
                  f"site LK {brl(r.get('lk_site_price_brl') or r.get('lk_current_price_brl'))}; margem {pct(r.get('best_route_margin_pct'))}. "
                  "Aprovação aqui significa: Júlio pode conferir disponibilidade e comprar manualmente; Hermes não compra/contata/paga.")
        props={
            'Lote Compra': {'select': {'name': 'P1 — lote inicial'}},
            'Aprovação Compra': {'select': {'name': 'Aguardando decisão manual'}},
            'Resumo Aprovação': {'rich_text':[{'text':{'content':approval[:1800]}}]}
        }
        pr=http_json(f'https://api.notion.com/v1/pages/{r["page_id"]}',nh(notion_token),method='PATCH',payload={'properties':props})
        if pr.get('error'): errors.append({'page_id':r['page_id'],'patch_error':pr})
        else: pages_updated+=1
        if not page_has_marker(notion_token,r['page_id']):
            ap=http_json(f'https://api.notion.com/v1/blocks/{r["page_id"]}/children',nh(notion_token),method='PATCH',payload={'children':[heading('Pacote P1 — aprovação de compra manual'), paragraph(f'{MARKER}. {approval}'), paragraph('Este é um pacote de decisão, não uma execução. Antes de comprar, Júlio precisa confirmar disponibilidade/preço final no marketplace/importador.')]})
            if ap.get('error'): errors.append({'page_id':r['page_id'],'append_error':ap})
            else: blocks_appended+=1
        time.sleep(.15)
    out={'status':'completed' if not errors else 'completed_with_errors','generated_at':now(),'p1_count':len(p1),'pages_updated':pages_updated,'blocks_appended':blocks_appended,'db_error':db.get('error'),'total_estimated_cost_brl':total_cost,'total_site_value_brl':expected_site,'estimated_gross_brl':expected_gross,'blended_margin_pct':blended_margin,'not_performed':['purchase','reservation','supplier_contact','whatsapp_send','payment_schedule','shopify_write','tiny_write','merchant_write'],'errors':errors,'rows':p1}
    OUT_JSON.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    lines=['# LK Sourcing v11 — Pacote P1 para aprovação de compra manual','',f"Generated: `{out['generated_at']}`",'',f"- Itens P1: {len(p1)}",f"- Custo estimado total: {brl(total_cost)}",f"- Valor site LK: {brl(expected_site)}",f"- Lucro bruto estimado: {brl(expected_gross)}",f"- Margem combinada: {pct(blended_margin)}",'', '## Itens P1']
    for r in p1:
        lines += [f"### #{r.get('ranking_v9')} — {r.get('model')} — BR {r.get('br_size')}",f"- SKU: `{r.get('sku_lk')}`",f"- Rota: {r.get('route_recommended_v9')}",f"- Preço Droper: {brl(r.get('droper_price_brl'))}",f"- StockX/GOAT: {usd(r.get('stockx_goat_price_usd'))}",f"- Custo: {brl(r.get('product_cost_brl'))}",f"- Site LK: {brl(r.get('lk_site_price_brl') or r.get('lk_current_price_brl'))}",f"- Margem: {pct(r.get('best_route_margin_pct'))}",'- Estado: Aguardando decisão manual do Júlio/Lucas','']
    lines += ['## Texto de aprovação sugerido','Aprovo o lote P1 para o Júlio conferir disponibilidade e executar compra manual dos 4 itens, mantendo Hermes sem compra, contato, pagamento ou reserva automática.']
    OUT_MD.write_text('\n'.join(lines)+'\n')
    MC_MD.write_text('\n'.join(lines)+'\n')
    print(json.dumps({k:out[k] for k in ['status','p1_count','pages_updated','blocks_appended','db_error','total_estimated_cost_brl','total_site_value_brl','estimated_gross_brl','blended_margin_pct']},ensure_ascii=False))
if __name__=='__main__': main()
