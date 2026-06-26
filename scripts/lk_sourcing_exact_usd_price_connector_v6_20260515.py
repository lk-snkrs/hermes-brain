#!/usr/bin/env python3
from __future__ import annotations
import base64, json, os, pathlib, re, time, urllib.error, urllib.parse, urllib.request
from datetime import datetime, timezone
from typing import Any

ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
DOPPLER_TOKEN_FILE=pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
V5=ROOT/'reports/lk-sourcing-br-to-us-size-conversion-v5-2026-05-15.json'
OUT_JSON=ROOT/'reports/lk-sourcing-exact-usd-price-connector-v6-2026-05-15.json'
OUT_MD=ROOT/'reports/lk-sourcing-exact-usd-price-connector-v6-2026-05-15.md'
MC_MD=ROOT/'areas/lk/rotinas/mission-control-sourcing-exact-usd-price-connector-v6-2026-05-15.md'
NOTION_DB='2b127dc9-e033-805b-81b6-f62f5467ce77'
NOTION_VERSION='2022-06-28'
USD_BRL=4.911381
FX_BUFFER=1.05
CUSTO_TRAZER_USD=100.0
MARKUP=2.0
TARGET_MARGIN=0.30
LOW_MARGIN=0.20
MARKER='LK OS sourcing v6 — exact StockX variant USD ask matched by Hermes — 2026-05-15'


def now(): return datetime.now(timezone.utc).isoformat()
def brl(v): return 'n/d' if v is None else f'R$ {float(v):,.2f}'.replace(',','X').replace('.',',').replace('X','.')
def usd(v): return 'n/d' if v is None else f'US$ {float(v):,.2f}'
def pct(v): return 'n/d' if v is None else f'{float(v)*100:.1f}%'
def factor(): return USD_BRL*FX_BUFFER

def norm_sku(s: str|None)->str: return re.sub(r'[^A-Z0-9]','',(s or '').upper())
def norm_size_label(s: str|None)->str:
    s=(s or '').lower().replace('—',' ').replace('/',' ').strip()
    s=re.sub(r'\s+',' ',s)
    m=re.search(r'us\s*([mw])\s*([0-9]+(?:\.5)?)',s)
    if not m: return ''
    return f'us {m.group(1)} {m.group(2)}'

def parse_target_labels(label: str)->list[str]:
    # Handles e.g. "US M 9.5 / US W 11 — conferir..."
    out=[]
    for m in re.finditer(r'US\s*([MW])\s*([0-9]+(?:\.5)?)', label or '', flags=re.I):
        out.append(f'us {m.group(1).lower()} {m.group(2)}')
    return out

def load_doppler():
    token=os.environ.get('DOPPLER_TOKEN') or DOPPLER_TOKEN_FILE.read_text().strip()
    req=urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
    req.add_header('Authorization','Basic '+base64.b64encode((token+':').encode()).decode())
    with urllib.request.urlopen(req,timeout=60) as r: return json.loads(r.read().decode())
def nh(tok): return {'Authorization':'Bearer '+tok,'Notion-Version':NOTION_VERSION}
def kh(key): return {'Authorization':'Bearer '+key,'User-Agent':'Hermes/1.0'}

def http_json(url,headers,method='GET',payload=None,attempts=5):
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
                time.sleep(min(45,4*(i+1)))
                continue
            return {'error':f'http_{e.code}','body':body[:1000]}
        except Exception as e:
            if i<attempts-1:
                time.sleep(min(45,3*(i+1)))
                continue
            return {'error':type(e).__name__,'body':str(e)[:1000]}
    return {'error':'request_failed'}

def stockx_products(key, style):
    params={'query':style,'limit':5,'display[variants]':'true','display[prices]':'true','display[statistics]':'true','display[traits]':'true'}
    url='https://api.kicks.dev/v3/stockx/products?'+urllib.parse.urlencode(params)
    d=http_json(url,kh(key))
    if d.get('error'): return d
    rows=d.get('data') or []
    exact=[x for x in rows if norm_sku(x.get('sku'))==norm_sku(style)]
    return {'data': exact or rows}

def find_variant(product: dict[str,Any], targets: list[str])->dict[str,Any]|None:
    for v in product.get('variants') or []:
        labels=[]
        if v.get('size') and v.get('size_type'):
            labels.append(norm_size_label(f"{v.get('size_type')} {v.get('size')}"))
        for sz in v.get('sizes') or []:
            labels.append(norm_size_label(sz.get('size') or (str(sz.get('type'))+' '+str(sz.get('size')))))
        labels={x for x in labels if x}
        if any(t in labels for t in targets):
            return v
    return None

def variant_ask(v: dict[str,Any]|None)->float|None:
    if not v: return None
    la=v.get('lowest_ask')
    if isinstance(la,(int,float)) and la>0: return float(la)
    prices=v.get('prices') or []
    standard=[p for p in prices if p.get('type')=='standard' and isinstance(p.get('price'),(int,float))]
    if standard: return float(min(p['price'] for p in standard))
    anyp=[p for p in prices if isinstance(p.get('price'),(int,float))]
    if anyp: return float(min(p['price'] for p in anyp))
    return None

def calc(ask):
    if ask is None: return None,None
    landed=(ask+CUSTO_TRAZER_USD)*factor()
    return landed, landed*MARKUP

def route_decision(row, landed):
    sale=row.get('sale_price_brl')
    nat_margin=row.get('national_margin_pct_v3')
    imp_margin=(sale-landed)/sale if sale and landed is not None else None
    if landed is not None and imp_margin is not None and imp_margin>=TARGET_MARGIN and (nat_margin is None or imp_margin>nat_margin):
        return 'Importar','import_exact_size_viable',imp_margin
    if nat_margin is not None and nat_margin>=TARGET_MARGIN:
        return 'Comprar nacional','national_exact_size_viable_or_better',imp_margin
    if landed is not None and imp_margin is not None and imp_margin>=LOW_MARGIN:
        return 'Watchlist','import_exact_size_borderline',imp_margin
    if nat_margin is not None and nat_margin>=LOW_MARGIN:
        return 'Watchlist','national_borderline_import_not_better',imp_margin
    return 'Pular','not_viable_with_exact_size_ask' if landed is not None else 'no_exact_usd_ask',imp_margin

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
    kicks_key=sec.get('KICKS_DEV_API_KEY') or sec.get('KICKS_API_KEY') or sec.get('KICKSDB_API_KEY')
    if not notion_token: raise SystemExit('missing Notion token')
    if not kicks_key: raise SystemExit('missing KicksDev key')
    rows=json.loads(V5.read_text())['rows']
    db=http_json(f'https://api.notion.com/v1/databases/{NOTION_DB}',nh(notion_token),method='PATCH',payload={'properties':{'Preço exato tam USD': {'number': {}}, 'Custo landed BRL': {'number': {}}, 'Venda ideal BRL': {'number': {}}, 'Margem import atual %': {'number': {}}, 'Decisão Sourcing': {'select': {'options':[{'name':'Hermes validar preço/tamanho','color':'orange'},{'name':'Comprar nacional','color':'green'},{'name':'Importar','color':'blue'},{'name':'Pular','color':'red'},{'name':'Watchlist','color':'gray'}]}}, 'Status preço import': {'select': {'options':[{'name':'US size mapeado; preço pendente','color':'yellow'},{'name':'Preço USD validado','color':'green'},{'name':'Fonte/API não retornou ask','color':'orange'}]}}}})
    product_cache={}; out=[]; errors=[]; pages_updated=0; blocks_appended=0
    for r in rows:
        style=r['style_sku']; targets=parse_target_labels(r.get('us_size_label') or '')
        if style not in product_cache:
            product_cache[style]=stockx_products(kicks_key,style)
            time.sleep(.7)
        pdata=product_cache[style]
        product=None; variant=None; exact_ask=None; product_error=None
        if pdata.get('error'):
            product_error=pdata
        else:
            products=pdata.get('data') or []
            product=products[0] if products else None
            if product: variant=find_variant(product,targets)
            exact_ask=variant_ask(variant)
        landed,ideal=calc(exact_ask)
        decision,status,imp_margin=route_decision(r,landed)
        price_status='Preço USD validado' if exact_ask is not None else 'Fonte/API não retornou ask'
        source_text=(f'Hermes match automático: {r.get("br_size")} → EU {r.get("eu_reference_size")} → {r.get("us_size_label")}. '
                     f'Fonte: KicksDev StockX variants/display[variants]+display[prices], style {style}. ')
        if exact_ask is not None:
            source_text += (f'Ask USD exato do tamanho: {usd(exact_ask)}; landed {brl(landed)}; venda ideal {brl(ideal)}; margem no preço atual {pct(imp_margin)}. ')
        else:
            source_text += 'A fonte não retornou ask USD exato para o tamanho convertido; importação segue pendente. '
        source_text += 'Sem compra/contato/pagamento; Júlio não preenche preço.'
        props={'Fonte preço tam': {'rich_text':[{'text':{'content':source_text[:1800]}}]}, 'Status preço import': {'select': {'name':price_status}}, 'Decisão Sourcing': {'select': {'name':decision}}, 'Preço exato tam USD': {'number': exact_ask}, 'Custo landed BRL': {'number': landed}, 'Venda ideal BRL': {'number': ideal}, 'Margem import atual %': {'number': imp_margin}}
        pr=http_json(f'https://api.notion.com/v1/pages/{r["page_id"]}',nh(notion_token),method='PATCH',payload={'properties':props})
        if pr.get('error'): errors.append({'page_id':r['page_id'],'patch_error':pr})
        else: pages_updated+=1
        if not page_has_marker(notion_token,r['page_id']):
            blocks=[heading('Preço USD exato por tamanho — StockX/KicksDev'), paragraph(f'{MARKER}. {source_text}'), paragraph('Fórmula: custo landed=(ask USD exato+custo trazer US$100)×(dólar 4,911381×1,05); venda ideal=landed×2. Product-level min/avg não foi usado como custo.'), paragraph('Não executado: compra, reserva, fornecedor, WhatsApp, pagamento, Shopify, Tiny ou Merchant.')]
            ap=http_json(f'https://api.notion.com/v1/blocks/{r["page_id"]}/children',nh(notion_token),method='PATCH',payload={'children':blocks})
            if ap.get('error'): errors.append({'page_id':r['page_id'],'append_error':ap})
            else: blocks_appended+=1
        out.append({**r,'stockx_product_id': product.get('id') if product else None,'stockx_slug': product.get('slug') if product else None,'target_size_labels':targets,'matched_variant_id': variant.get('id') if variant else None,'matched_variant_size': variant.get('size') if variant else None,'matched_variant_size_type': variant.get('size_type') if variant else None,'exact_size_price_usd':exact_ask,'exact_landed_cost_brl':landed,'ideal_sale_brl':ideal,'import_margin_pct':imp_margin,'decision_v6':decision,'validation_status_v6':status,'import_price_status_v6':price_status,'source_text_v6':source_text,'product_error':product_error})
        time.sleep(.35)
    counts={}
    for r in out: counts[r['validation_status_v6']]=counts.get(r['validation_status_v6'],0)+1
    summary={'status':'completed' if not errors else 'completed_with_errors','generated_at':now(),'cards':len(out),'pages_updated':pages_updated,'blocks_appended':blocks_appended,'db_error':db.get('error'),'counts':counts,'usd_brl':USD_BRL,'fx_buffer':FX_BUFFER,'custo_trazer_usd':CUSTO_TRAZER_USD,'markup':MARKUP,'source':'KicksDev StockX product variants with display[variants]/display[prices]; variant-level lowest_ask/prices only','not_performed':['purchase','reservation','supplier_contact','whatsapp_send','payment_schedule','shopify_write','tiny_write','merchant_write'],'errors':errors,'rows':out}
    OUT_JSON.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    lines=['# LK Sourcing v6 — ask USD exato por tamanho StockX/KicksDev','',f"Generated: `{summary['generated_at']}`",'','## Veredito']
    lines += [f'- {k}: {v}' for k,v in sorted(counts.items())]
    lines += ['','## Regras','- Usado apenas preço/ask de variante/tamanho (`variants.lowest_ask` ou `prices` por variante).','- Product-level `min_price/avg_price` não entra no custo.','- Fórmula: `landed=(ask_usd+100)×(4.911381×1.05)`; `venda_ideal=landed×2`.','- Nenhuma compra/contato/pagamento/write externo fora dos cards Notion.','','## Cards']
    for r in out:
        lines += [f"### {r['model']} — BR {r['br_size']} → {r['us_size_label']}",f"- SKU: `{r['sku_lk']}` / style `{r['style_sku']}`",f"- Ask exato USD: {usd(r['exact_size_price_usd'])}",f"- Landed: {brl(r['exact_landed_cost_brl'])}",f"- Venda ideal: {brl(r['ideal_sale_brl'])}",f"- Margem import no preço atual: {pct(r['import_margin_pct'])}",f"- Decisão v6: `{r['decision_v6']}` / `{r['validation_status_v6']}`",f"- Variante: `{r['matched_variant_size_type'] or 'n/d'} {r['matched_variant_size'] or ''}` `{r['matched_variant_id'] or 'n/d'}`",'']
    OUT_MD.write_text('\n'.join(lines)+'\n')
    MC_MD.write_text('\n'.join(lines)+'\n')
    print(json.dumps({k:summary[k] for k in ['status','cards','pages_updated','blocks_appended','counts','db_error']},ensure_ascii=False))

if __name__=='__main__': main()
