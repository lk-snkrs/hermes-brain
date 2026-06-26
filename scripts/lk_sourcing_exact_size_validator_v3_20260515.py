#!/usr/bin/env python3
from __future__ import annotations
import base64, json, os, pathlib, time, urllib.error, urllib.request
from datetime import datetime, timezone
from typing import Any

ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
DOPPLER_TOKEN_FILE=pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
SOURCING=ROOT/'reports/lk-sourcing-ops-v2-markup2-exact-size-2026-05-15.json'
DROPER=ROOT/'reports/lk-os-droper-readonly-results-18-2026-05-14.json'
OUT_JSON=ROOT/'reports/lk-sourcing-exact-size-validator-v3-2026-05-15.json'
OUT_MD=ROOT/'reports/lk-sourcing-exact-size-validator-v3-2026-05-15.md'
MC_MD=ROOT/'areas/lk/rotinas/mission-control-sourcing-exact-size-validator-v3-2026-05-15.md'
NOTION_DB='2b127dc9-e033-805b-81b6-f62f5467ce77'
NOTION_VERSION='2022-06-28'
MARKER='LK OS sourcing exact-size validator v3 — Hermes validates price; Júlio does not fill values — 2026-05-15'
TARGET_MARGIN=0.30
LOW_MARGIN=0.20
USD_BRL=4.911381
FX_BUFFER=1.05
DEFAULT_CUSTO_TRAZER_USD=100.0
MARKUP=2.0


def now(): return datetime.now(timezone.utc).isoformat()
def brl(v): return 'n/d' if v is None else f'R$ {float(v):,.2f}'.replace(',','X').replace('.',',').replace('X','.')
def pct(v): return 'n/d' if v is None else f'{float(v)*100:.1f}%'

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

def paragraph(text): return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':text[:1900]}}]}}
def heading(text): return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':text[:1900]}}]}}

def existing_marker(tok,page_id):
    d=http_json(f'https://api.notion.com/v1/blocks/{page_id}/children?page_size=100',nh(tok))
    for b in d.get('results',[]) if isinstance(d,dict) else []:
        typ=b.get('type')
        if typ and typ in b:
            rich=b[typ].get('rich_text') or b[typ].get('caption') or []
            text=''.join(x.get('plain_text') or (x.get('text') or {}).get('content') or '' for x in rich)
            if MARKER in text: return True
    return False

def decide(sale_brl, droper_best):
    if not droper_best:
        return 'Hermes validar preço/tamanho','blocked_no_exact_size_source',None
    cost=float(droper_best['preco_num'])
    margin=(float(sale_brl)-cost)/float(sale_brl) if sale_brl else None
    if margin is not None and margin >= TARGET_MARGIN:
        return 'Comprar nacional','national_exact_size_viable',margin
    if margin is not None and margin >= LOW_MARGIN:
        return 'Watchlist','national_exact_size_borderline_import_compare_needed',margin
    return 'Pular','national_exact_size_low_margin_import_compare_needed',margin

def main():
    sec=load_doppler(); tok=sec.get('NOTION_TOKEN_LK') or sec.get('NOTION_API_KEY')
    if not tok: raise SystemExit('missing notion token')
    db=http_json(f'https://api.notion.com/v1/databases/{NOTION_DB}',nh(tok),method='PATCH',payload={'properties':{'Decisão Sourcing': {'select': {'options':[{'name':'Precisa validar tamanho','color':'yellow'},{'name':'Hermes validar preço/tamanho','color':'orange'},{'name':'Comprar nacional','color':'green'},{'name':'Importar','color':'blue'},{'name':'Pular','color':'red'},{'name':'Watchlist','color':'gray'}]}}}})
    sourcing=json.loads(SOURCING.read_text())['rows']
    droper_by_sku={r['sku']:r for r in json.loads(DROPER.read_text())['results']}
    rows=[]; pages_updated=0; blocks_appended=0; errors=[]
    for r in sourcing:
        d=droper_by_sku.get(r['sku_lk'])
        best=(d or {}).get('best') if d else None
        decision, validation_status, margin=decide(r.get('sale_price_brl'), best)
        exact_size_source=None; exact_price_brl=None; exact_url=None; confidence=None
        if best:
            exact_price_brl=best.get('preco_num'); exact_url=best.get('product_url'); confidence=best.get('quality') or 'exact_size_match'; exact_size_source='Droper exact-size public search'
        if validation_status=='national_exact_size_viable':
            source_text=f'VALIDADO por Hermes: Droper match exato do tamanho {r["size_lk"]}, preço {brl(exact_price_brl)}, margem {pct(margin)}, fonte {exact_url}. Júlio não preenche valor; compra/contato/pagamento seguem humanos.'
        elif validation_status=='national_exact_size_borderline_import_compare_needed':
            source_text=f'VALIDADO por Hermes: Droper match exato do tamanho {r["size_lk"]}, preço {brl(exact_price_brl)}, margem {pct(margin)} abaixo do alvo 30%; comparar importação somente se Hermes obtiver preço USD exato por tamanho. Fonte {exact_url}.'
        elif validation_status=='national_exact_size_low_margin_import_compare_needed':
            source_text=f'VALIDADO por Hermes: Droper match exato do tamanho {r["size_lk"]}, mas margem {pct(margin)} baixa/negativa com preço {brl(exact_price_brl)}; não comprar nacional sem exceção. Importação segue bloqueada até Hermes obter preço USD exato por tamanho. Fonte {exact_url}.'
        else:
            source_text=f'BLOQUEADO: Hermes ainda não encontrou preço exato confiável para tamanho {r["size_lk"]}. Júlio não preenche valor. Product-level/KicksDev/StockX min não é custo; importação só após Hermes validar preço USD exato por tamanho.'
        props={'Fonte preço tam': {'rich_text':[{'text':{'content':source_text[:1800]}}]}, 'Decisão Sourcing': {'select': {'name':decision}}, 'Preço exato tam USD': {'number': None}, 'Custo landed BRL': {'number': None}, 'Venda ideal BRL': {'number': None}, 'Margem venda atual %': {'number': margin}}
        if exact_url: props['Link']={'url': exact_url}
        if exact_price_brl is not None: props['Custo']={'number': float(exact_price_brl)}
        pr=http_json(f'https://api.notion.com/v1/pages/{r["page_id"]}',nh(tok),method='PATCH',payload={'properties':props})
        if pr.get('error'): errors.append({'page_id':r['page_id'],'error':pr.get('error'),'body':pr.get('body')})
        else: pages_updated+=1
        if not existing_marker(tok,r['page_id']):
            blocks=[heading('Validação Hermes de preço por tamanho'), paragraph(f'{MARKER}. Resultado: {source_text}'), paragraph('Regra: preço nacional/Droper só vale se o tamanho exato está listado. Preço importado só será calculado com ask/preço USD do tamanho correto; product-level não entra em custo. Fórmula import: landed=(USD+custo trazer)×(FX×1,05); venda ideal=landed×2.'), paragraph('Não executado: compra, reserva, contato fornecedor, WhatsApp, pagamento, Shopify/Tiny/Merchant.')]
            ap=http_json(f'https://api.notion.com/v1/blocks/{r["page_id"]}/children',nh(tok),method='PATCH',payload={'children':blocks})
            if ap.get('error'): errors.append({'page_id':r['page_id'],'append_error':ap.get('error')})
            else: blocks_appended+=1
        rows.append({**r,'droper_status':(d or {}).get('status'),'exact_size_source':exact_size_source,'exact_size_price_brl':exact_price_brl,'exact_size_url':exact_url,'confidence':confidence,'validation_status':validation_status,'decision_v3':decision,'national_margin_pct_v3':margin,'source_text':source_text})
        time.sleep(.25)
    counts={}
    for r in rows: counts[r['validation_status']]=counts.get(r['validation_status'],0)+1
    summary={'status':'completed' if not errors else 'completed_with_errors','generated_at':now(),'cards':len(rows),'pages_updated':pages_updated,'blocks_appended':blocks_appended,'db_error':db.get('error'),'counts':counts,'formula_import':{'landed':'(exact_size_price_usd + custo_trazer_usd) × (usd_brl × 1.05)','ideal_sale':'landed × 2','usd_brl':USD_BRL,'fx_buffer':FX_BUFFER,'markup':MARKUP},'not_performed':['purchase','reservation','supplier_contact','whatsapp_send','payment_schedule','shopify_write','tiny_write','merchant_write'],'errors':errors,'rows':rows}
    OUT_JSON.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    lines=['# LK Sourcing — validador Hermes de preço por tamanho v3','',f"Generated: `{summary['generated_at']}`",'','## Veredito','','- Júlio **não preenche valor**. Hermes validou o que é possível por fonte integrada/read-only existente.','- Droper nacional: preço só aceito quando há match do **tamanho exato**.','- Importação: nenhum custo USD foi calculado porque KicksDev/StockX product-level continua sendo apenas sinal/foto; sem ask/preço USD exato por tamanho, importação fica bloqueada.','- Fórmula preservada para quando houver preço USD exato: `landed=(USD+custo trazer)×(FX×1,05)`; `venda ideal=landed×2`.','','## Contagem']
    for k,v in sorted(counts.items()): lines.append(f'- {k}: {v}')
    lines += ['','## Cards']
    for r in rows:
        lines += [f"### {r['model']} — Tam {r['size_lk']} — `{r['sku_lk']}`",f"- Decisão: `{r['decision_v3']}`",f"- Status: `{r['validation_status']}`",f"- Preço exato nacional: {brl(r['exact_size_price_brl'])} ({r['exact_size_source'] or 'n/d'})",f"- Margem nacional: {pct(r['national_margin_pct_v3'])}",f"- Link fonte: {r['exact_size_url'] or 'n/d'}",f"- Importação: bloqueada até Hermes obter preço USD exato por tamanho",'']
    OUT_MD.write_text('\n'.join(lines)+'\n')
    MC_MD.write_text('\n'.join(lines[:80])+'\n\nFonte completa: `reports/lk-sourcing-exact-size-validator-v3-2026-05-15.md`\n')
    print(json.dumps({k:summary[k] for k in ['status','cards','pages_updated','blocks_appended','counts','db_error']},ensure_ascii=False))

if __name__=='__main__': main()
