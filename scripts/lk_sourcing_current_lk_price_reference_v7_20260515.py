#!/usr/bin/env python3
from __future__ import annotations
import base64, json, os, pathlib, re, time, urllib.error, urllib.request
from datetime import datetime, timezone
from typing import Any

ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
DOPPLER_TOKEN_FILE=pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
V6=ROOT/'reports/lk-sourcing-exact-usd-price-connector-v6-2026-05-15.json'
OUT_JSON=ROOT/'reports/lk-sourcing-current-lk-price-reference-v7-2026-05-15.json'
OUT_MD=ROOT/'reports/lk-sourcing-current-lk-price-reference-v7-2026-05-15.md'
MC_MD=ROOT/'areas/lk/rotinas/mission-control-sourcing-current-lk-price-reference-v7-2026-05-15.md'
NOTION_DB='2b127dc9-e033-805b-81b6-f62f5467ce77'
NOTION_VERSION='2022-06-28'
MARKER='LK OS sourcing v7 — preço atual LK/Shopify como referência — 2026-05-15'

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
    v6=json.loads(V6.read_text())
    previous_rows=[]
    if OUT_JSON.exists():
        try:
            previous_rows=(json.loads(OUT_JSON.read_text()).get('rows') or [])
        except Exception:
            previous_rows=[]
    previous_by_page={x.get('page_id'): x for x in previous_rows}
    db=http_json(f'https://api.notion.com/v1/databases/{NOTION_DB}',nh(notion_token),method='PATCH',payload={'properties':{'Preço LK atual BRL': {'number': {}}, 'Preço médio vendido BRL': {'number': {}}, 'Fonte preço LK': {'rich_text': {}}}})
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
        avg_sold=r.get('sale_price_brl')
        landed=r.get('exact_landed_cost_brl')
        margin_current=(current_price-landed)/current_price if current_price and landed is not None else None
        nat_margin=r.get('national_margin_pct_v3')
        if landed is not None and margin_current is not None and margin_current >= 0.30 and (nat_margin is None or margin_current > nat_margin):
            decision_v7='Importar'; status_v7='import_exact_size_viable_vs_lk_current_price'
        elif nat_margin is not None and nat_margin >= 0.30:
            decision_v7='Comprar nacional'; status_v7='national_exact_size_viable_or_better_vs_lk_current_price'
        elif landed is not None and margin_current is not None and margin_current >= 0.20:
            decision_v7='Watchlist'; status_v7='import_exact_size_borderline_vs_lk_current_price'
        elif nat_margin is not None and nat_margin >= 0.20:
            decision_v7='Watchlist'; status_v7='national_borderline_import_not_better_vs_lk_current_price'
        else:
            decision_v7='Pular'; status_v7='not_viable_vs_lk_current_price' if landed is not None else 'no_exact_usd_ask'
        if var is None: missing+=1
        source=(f'Preço LK atual/Shopify da variante SKU {sku}: {brl(current_price)}'
                f'{f" (compare-at {brl(compare_price)})" if compare_price else ""}. '
                f'Preço médio vendido 120d usado como histórico: {brl(avg_sold)}. '
                f'Importação: ask {usd(r.get("exact_size_price_usd"))}, landed {brl(landed)}, venda ideal {brl(r.get("ideal_sale_brl"))}, margem vs preço LK atual {pct(margin_current)}. '
                'Correção Lucas: o preço atual do nosso produto precisa aparecer como referência; sem compra/contato/pagamento.')
        props={'Preço LK atual BRL': {'number': current_price}, 'Preço médio vendido BRL': {'number': avg_sold}, 'Fonte preço LK': {'rich_text':[{'text':{'content':source[:1800]}}]}, 'Margem import atual %': {'number': margin_current}, 'Decisão Sourcing': {'select': {'name': decision_v7}}}
        pr=http_json(f'https://api.notion.com/v1/pages/{r["page_id"]}',nh(notion_token),method='PATCH',payload={'properties':props})
        if pr.get('error'): errors.append({'page_id':r['page_id'],'patch_error':pr})
        else: pages_updated+=1
        previous=previous_by_page.get(r['page_id']) or {}
        previously_missing=previous.get('lk_current_price_brl') is None
        if previously_missing or not page_has_marker(notion_token,r['page_id']):
            blocks=[heading('Correção — preço atual LK/Shopify como referência'), paragraph(f'{MARKER}. {source}'), paragraph('Leitura Shopify foi read-only por SKU da variante. O preço médio vendido 120d fica como histórico; a referência operacional do card passa a mostrar também o preço atual do produto na LK.')]
            ap=http_json(f'https://api.notion.com/v1/blocks/{r["page_id"]}/children',nh(notion_token),method='PATCH',payload={'children':blocks})
            if ap.get('error'): errors.append({'page_id':r['page_id'],'append_error':ap})
            else: blocks_appended+=1
        row={**r,'lk_current_price_brl':current_price,'lk_compare_at_price_brl':compare_price,'lk_current_price_source':'fact_shopify_variant_price_by_sku' if var else 'missing_shopify_variant_by_sku','lk_product_title':(var or {}).get('product',{}).get('title'),'lk_product_handle':(var or {}).get('product',{}).get('handle'),'import_margin_vs_lk_current_price_pct':margin_current,'decision_v7':decision_v7,'validation_status_v7':status_v7,'source_text_v7':source}
        rows.append(row)
    counts={}
    for r in rows:
        counts[r['decision_v7']]=counts.get(r['decision_v7'],0)+1
    summary={'status':'completed' if not errors else 'completed_with_errors','generated_at':now(),'cards':len(rows),'pages_updated':pages_updated,'blocks_appended':blocks_appended,'shopify_missing_sku_count':missing,'db_error':db.get('error'),'decision_counts':counts,'not_performed':['purchase','reservation','supplier_contact','whatsapp_send','payment_schedule','shopify_write','tiny_write','merchant_write'],'errors':errors,'rows':rows}
    OUT_JSON.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    lines=['# LK Sourcing v7 — preço atual LK/Shopify como referência','',f"Generated: `{summary['generated_at']}`",'',f"- Cards atualizados: {pages_updated}/{len(rows)}",f"- SKUs Shopify não encontrados: {missing}",'','## Correção aplicada','- Agora cada card tem `Preço LK atual BRL` lido do Shopify por SKU da variante.','- `Preço médio vendido BRL` continua como histórico de 120d, mas não substitui o preço atual do produto.','- Margem de importação foi recalculada contra o preço LK atual.','','## Cards']
    for r in rows:
        lines += [f"### {r['model']} — BR {r['br_size']} → {r['us_size_label']}",f"- SKU: `{r['sku_lk']}`",f"- Preço LK atual: {brl(r['lk_current_price_brl'])}",f"- Preço médio vendido 120d: {brl(r.get('sale_price_brl'))}",f"- Ask exato USD: {usd(r.get('exact_size_price_usd'))}",f"- Landed: {brl(r.get('exact_landed_cost_brl'))}",f"- Venda ideal: {brl(r.get('ideal_sale_brl'))}",f"- Margem import vs preço LK atual: {pct(r.get('import_margin_vs_lk_current_price_pct'))}",f"- Decisão: `{r['decision_v7']}` / `{r['validation_status_v7']}`",'']
    OUT_MD.write_text('\n'.join(lines)+'\n')
    MC_MD.write_text('\n'.join(lines)+'\n')
    print(json.dumps({k:summary[k] for k in ['status','cards','pages_updated','blocks_appended','shopify_missing_sku_count','db_error','decision_counts']},ensure_ascii=False))
if __name__=='__main__': main()
