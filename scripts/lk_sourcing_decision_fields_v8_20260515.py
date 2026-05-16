#!/usr/bin/env python3
from __future__ import annotations
import base64, json, os, pathlib, re, time, urllib.error, urllib.request
from datetime import datetime, timezone
from typing import Any

ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
DOPPLER_TOKEN_FILE=pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
V6=ROOT/'reports/lk-sourcing-current-lk-price-reference-v7-2026-05-15.json'
OUT_JSON=ROOT/'reports/lk-sourcing-decision-fields-v8-2026-05-15.json'
OUT_MD=ROOT/'reports/lk-sourcing-decision-fields-v8-2026-05-15.md'
MC_MD=ROOT/'areas/lk/rotinas/mission-control-sourcing-decision-fields-v8-2026-05-15.md'
NOTION_DB='2b127dc9-e033-805b-81b6-f62f5467ce77'
NOTION_VERSION='2022-06-28'
MARKER='LK OS sourcing v8 — campos decisivos Droper/StockX-GOAT/custo/preço site — 2026-05-15'

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

def shop_host(s: str)->str:
    s=(s or '').strip().replace('https://','').replace('http://','').rstrip('/')
    return s

def shopify_graphql(store: str, token: str, query: str, variables: dict[str,Any]):
    url=f'https://{shop_host(store)}/admin/api/2024-01/graphql.json'
    return http_json(url,{'X-Shopify-Access-Token':token},method='POST',payload={'query':query,'variables':variables})

def norm_sku(s: str|None)->str:
    return re.sub(r'[^A-Z0-9]', '', (s or '').upper())

def variant_by_sku(store: str, token: str, sku: str, model: str|None=None, br_size: str|None=None)->dict[str,Any]|None:
    q='''query VariantBySku($query:String!){ productVariants(first:50, query:$query){ nodes{ id sku price compareAtPrice title product{ id title handle status onlineStoreUrl } } } }'''
    # Exact SKU query with quotes is supported by Shopify search; fallback to unquoted if needed.
    for qq in [f'sku:"{sku}"', f'sku:{sku}']:
        d=shopify_graphql(store,token,q,{'query':qq})
        nodes=(((d.get('data') or {}).get('productVariants') or {}).get('nodes') or []) if isinstance(d,dict) else []
        exact=[n for n in nodes if (n.get('sku') or '').strip().upper()==sku.strip().upper()]
        if exact: return exact[0]
    # Fallback for historical LK SKU punctuation/size suffix differences, e.g.
    # 1183C102.751 + BR 41.5 exists in Shopify as 1183C102 751-13 with variant title 41.5.
    base=re.sub(r'-\d+$', '', sku or '')
    base_queries=[]
    if base:
        base_queries += [base, base.replace('.', ' '), base.replace('.', ''), re.sub(r'[^A-Za-z0-9]', '', base)]
    if model:
        base_queries.append(model)
    seen=set()
    for qq in base_queries:
        if not qq or qq in seen: continue
        seen.add(qq)
        d=shopify_graphql(store,token,q,{'query':qq})
        nodes=(((d.get('data') or {}).get('productVariants') or {}).get('nodes') or []) if isinstance(d,dict) else []
        candidates=[]
        for n in nodes:
            same_model=True
            if model:
                same_model=(n.get('product') or {}).get('title') == model
            size_ok=(str(n.get('title') or '').strip() == str(br_size or '').strip()) if br_size else True
            sku_ok=norm_sku(base) and norm_sku(base) in norm_sku(n.get('sku'))
            if same_model and size_ok and sku_ok:
                candidates.append(n)
        if candidates:
            return candidates[0]
    return None

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
    shop_token=sec.get('SHOPIFY_ACCESS_TOKEN')
    store=sec.get('SHOPIFY_STORE_URL')
    if not notion_token: raise SystemExit('missing Notion token')
    if not shop_token or not store: raise SystemExit('missing Shopify secret(s)')
    v6_payload=json.loads(V6.read_text())
    v6={'rows': v6_payload.get('rows', []) if isinstance(v6_payload, dict) else v6_payload}
    previous_rows=[]
    previous_source=OUT_JSON if OUT_JSON.exists() else V6
    if previous_source.exists():
        try:
            previous_rows=(json.loads(previous_source.read_text()).get('rows') or [])
        except Exception:
            previous_rows=[]
    previous_by_page={x.get('page_id'): x for x in previous_rows}
    db=http_json(f'https://api.notion.com/v1/databases/{NOTION_DB}',nh(notion_token),method='PATCH',payload={'properties':{
        'Preço site LK BRL': {'number': {}},
        'Preço Droper BRL': {'number': {}},
        'Preço StockX/GOAT USD': {'number': {}},
        'Custo produto BRL': {'number': {}},
        'Margem melhor rota %': {'number': {}},
        'Fonte decisão sourcing': {'rich_text': {}},
        'Preço LK atual BRL': {'number': {}},
        'Fonte preço LK': {'rich_text': {}}
    }})
    rows=[]; errors=[]; pages_updated=0; blocks_appended=0; missing=0
    cache={}
    for r in v6['rows']:
        sku=r['sku_lk']
        if sku not in cache:
            cache[sku]=variant_by_sku(store,shop_token,sku,r.get('model'),r.get('br_size'))
            time.sleep(.25)
        var=cache[sku]
        current_price=float(var['price']) if var and var.get('price') is not None else None
        compare_price=float(var['compareAtPrice']) if var and var.get('compareAtPrice') not in (None,'') else None
        droper_price=r.get('national_cost_brl')
        market_usd=r.get('exact_size_price_usd')
        landed=r.get('exact_landed_cost_brl')
        import_margin=(current_price-landed)/current_price if current_price and landed is not None else None
        droper_margin=(current_price-droper_price)/current_price if current_price and droper_price is not None else None
        route_candidates=[]
        if landed is not None:
            route_candidates.append(('Importar', landed, import_margin, 'StockX/GOAT mais barato disponível hoje'))
        if droper_price is not None:
            route_candidates.append(('Comprar nacional', droper_price, droper_margin, 'Droper'))
        viable=[x for x in route_candidates if x[2] is not None]
        best=min(viable, key=lambda x: x[1]) if viable else None
        best_margin=best[2] if best else None
        product_cost=best[1] if best else None
        best_route=best[0] if best else None
        if best and best_margin is not None and best_margin >= 0.30:
            decision_v7=best_route; status_v7='best_route_viable_vs_lk_site_price'
        elif best and best_margin is not None and best_margin >= 0.20:
            decision_v7='Watchlist'; status_v7='best_route_borderline_vs_lk_site_price'
        else:
            decision_v7='Pular'; status_v7='not_viable_vs_lk_site_price' if best else 'no_droper_or_stockx_goat_cost'
        if var is None: missing+=1
        source=(f'Preço site LK/Shopify SKU {sku}: {brl(current_price)}'
                f'{f" (compare-at {brl(compare_price)})" if compare_price else ""}. '
                f'Preço Droper: {brl(droper_price)}. '
                f'Preço StockX/GOAT mais barato: {usd(market_usd)}; custo landed importação {brl(landed)}. '
                f'Custo do produto usado na decisão: {brl(product_cost)} via {best_route or "n/d"}; margem melhor rota {pct(best_margin)}. '
                'Correção Lucas: preço médio não é campo decisivo; sem compra/contato/pagamento.')
        props={'Preço site LK BRL': {'number': current_price}, 'Preço LK atual BRL': {'number': current_price}, 'Preço Droper BRL': {'number': droper_price}, 'Preço StockX/GOAT USD': {'number': market_usd}, 'Custo produto BRL': {'number': product_cost}, 'Margem melhor rota %': {'number': best_margin}, 'Fonte decisão sourcing': {'rich_text':[{'text':{'content':source[:1800]}}]}, 'Fonte preço LK': {'rich_text':[{'text':{'content':source[:1800]}}]}, 'Decisão Sourcing': {'select': {'name': decision_v7}}}
        pr=http_json(f'https://api.notion.com/v1/pages/{r["page_id"]}',nh(notion_token),method='PATCH',payload={'properties':props})
        if pr.get('error'): errors.append({'page_id':r['page_id'],'patch_error':pr})
        else: pages_updated+=1
        previous=previous_by_page.get(r['page_id']) or {}
        previously_missing=previous.get('lk_current_price_brl') is None
        if previously_missing or not page_has_marker(notion_token,r['page_id']):
            blocks=[heading('Correção — campos decisivos de sourcing'), paragraph(f'{MARKER}. {source}'), paragraph('Leitura Shopify foi read-only por SKU da variante. A decisão passa a destacar Preço Droper, Preço StockX/GOAT mais barato, Custo do produto e Preço no site LK. Preço médio fica fora da decisão.')]
            ap=http_json(f'https://api.notion.com/v1/blocks/{r["page_id"]}/children',nh(notion_token),method='PATCH',payload={'children':blocks})
            if ap.get('error'): errors.append({'page_id':r['page_id'],'append_error':ap})
            else: blocks_appended+=1
        row={**r,'lk_current_price_brl':current_price,'lk_site_price_brl':current_price,'lk_compare_at_price_brl':compare_price,'lk_current_price_source':'fact_shopify_variant_price_by_sku' if var else 'missing_shopify_variant_by_sku','lk_product_title':(var or {}).get('product',{}).get('title'),'lk_product_handle':(var or {}).get('product',{}).get('handle'),'droper_price_brl':droper_price,'stockx_goat_price_usd':market_usd,'product_cost_brl':product_cost,'best_route':best_route,'best_route_margin_pct':best_margin,'import_margin_vs_lk_current_price_pct':import_margin,'droper_margin_vs_lk_current_price_pct':droper_margin,'decision_v8':decision_v7,'decision_v7':decision_v7,'validation_status_v8':status_v7,'validation_status_v7':status_v7,'source_text_v8':source,'source_text_v7':source}
        rows.append(row)
    counts={}
    for r in rows:
        counts[r['decision_v7']]=counts.get(r['decision_v7'],0)+1
    summary={'status':'completed' if not errors else 'completed_with_errors','generated_at':now(),'cards':len(rows),'pages_updated':pages_updated,'blocks_appended':blocks_appended,'shopify_missing_sku_count':missing,'db_error':db.get('error'),'decision_counts':counts,'not_performed':['purchase','reservation','supplier_contact','whatsapp_send','payment_schedule','shopify_write','tiny_write','merchant_write'],'errors':errors,'rows':rows}
    OUT_JSON.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    lines=['# LK Sourcing v8 — campos decisivos Droper / StockX-GOAT / custo / preço site','',f"Generated: `{summary['generated_at']}`",'',f"- Cards atualizados: {pages_updated}/{len(rows)}",f"- SKUs Shopify não encontrados: {missing}",'','## Correção aplicada','- Preço médio vendido 120d saiu da leitura decisiva.','- Cada card passa a destacar: `Preço Droper BRL`, `Preço StockX/GOAT USD`, `Custo produto BRL` e `Preço site LK BRL`.','- Decisão e margem usam o menor custo viável entre Droper nacional e StockX/GOAT importado, comparado com o preço atual do site LK.','','## Cards']
    for r in rows:
        lines += [f"### {r['model']} — BR {r['br_size']} → {r['us_size_label']}",f"- SKU: `{r['sku_lk']}`",f"- Preço site LK: {brl(r['lk_site_price_brl'])}",f"- Preço Droper: {brl(r.get('droper_price_brl'))}",f"- Preço StockX/GOAT: {usd(r.get('stockx_goat_price_usd'))}",f"- Custo produto usado: {brl(r.get('product_cost_brl'))} via {r.get('best_route') or 'n/d'}",f"- Margem melhor rota vs site LK: {pct(r.get('best_route_margin_pct'))}",f"- Decisão: `{r['decision_v8']}` / `{r['validation_status_v8']}`",'']
    OUT_MD.write_text('\n'.join(lines)+'\n')
    MC_MD.write_text('\n'.join(lines)+'\n')
    print(json.dumps({k:summary[k] for k in ['status','cards','pages_updated','blocks_appended','shopify_missing_sku_count','db_error','decision_counts']},ensure_ascii=False))
if __name__=='__main__': main()
