#!/usr/bin/env python3
from __future__ import annotations
import json,pathlib,re,sqlite3,urllib.parse
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
TRIAGE=ROOT/'reports/lk-gmc-2026-05-14-residual-triage-current.json'
LOCAL_DB=pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
OUT=ROOT/'reports/lk-gmc-2026-05-14-post-gtin-price-updated-preview.json'
MD=ROOT/'reports/lk-gmc-2026-05-14-post-gtin-price-updated-preview.md'
BRAIN=ROOT/'areas/lk/rotinas/gmc-2026-05-14-post-gtin-price-updated-preview.md'
PILOT_LIMIT=100

def now(): return datetime.now(timezone.utc).isoformat()
def dec(v):
    if v is None: return None
    try: return f'{float(str(v)):.2f}'
    except Exception: return None

def norm_title(s):
    import unicodedata
    s=str(s or '').lower(); s=unicodedata.normalize('NFKD',s); s=''.join(ch for ch in s if not unicodedata.combining(ch)); s=re.sub(r'\blk sneakers?\b',' ',s); s=re.sub(r'[^a-z0-9]+',' ',s).strip(); return s

def handle_from_link(link):
    if not link: return None
    path=urllib.parse.urlparse(link).path.strip('/'); parts=[p for p in path.split('/') if p]
    if 'products' in parts:
        i=parts.index('products')
        if i+1 < len(parts): return parts[i+1]
    return None

def load_sources():
    con=sqlite3.connect(str(LOCAL_DB)); con.row_factory=sqlite3.Row
    q="""select v.sku,v.source_variant_id,v.source_product_id,v.product_id,v.title variant_title,v.option1,v.option2,v.price,v.compare_at_price,p.title product_title,p.handle,p.status from lk_product_variants v left join lk_products p on p.product_id=v.product_id where v.price is not null and v.price > 0"""
    rows=[dict(r) for r in con.execute(q)]; con.close()
    by_handle={}; by_title={}; by_offer={}
    for r in rows:
        if r.get('handle'): by_handle.setdefault(str(r['handle']),[]).append(r)
        nt=norm_title(r.get('product_title'))
        if nt: by_title.setdefault(nt,[]).append(r)
        for k in ['sku','source_variant_id','source_product_id','product_id']:
            v=r.get(k)
            if v: by_offer.setdefault(str(v),[]).append(r)
    return by_handle,by_title,by_offer

def choose(row, by_handle, by_title, by_offer):
    pid=row['product_id']; offer=row.get('offerId') or pid.split(':')[-1]
    handle=handle_from_link(row.get('link'))
    attempts=[]
    # exact variant id in Merchant link is preferred when present
    variant=None
    if row.get('link'):
        qs=urllib.parse.parse_qs(urllib.parse.urlparse(row['link']).query)
        variant=(qs.get('variant') or [None])[0]
    keys=[]
    if variant: keys.append(('exact_shopify_variant_id_from_link', variant, by_offer.get(str(variant),[])))
    keys.append(('exact_offer_sku_or_variant_or_product_id', offer, by_offer.get(str(offer),[])))
    if handle: keys.append(('shopify_handle_from_merchant_link', handle, by_handle.get(handle,[])))
    nt=norm_title(row.get('title')); keys.append(('exact_normalized_title', nt, by_title.get(nt,[])))
    for src,key,cands in keys:
        attempts.append({'source':src,'key':key,'candidates':len(cands)})
        usable=[c for c in cands if c.get('price') is not None and float(c['price'])>0]
        if not usable: continue
        # For exact variant/offer, use that variant. For handle/title, use lowest positive product price.
        if src in {'exact_shopify_variant_id_from_link','exact_offer_sku_or_variant_or_product_id'}:
            c=usable[0]
            return c, src, key, attempts
        c=sorted(usable, key=lambda x: float(x['price']))[0]
        return c, src, key, attempts
    return None,'blocked_no_shopify_source','',attempts

def main():
    triage=json.loads(TRIAGE.read_text())
    by_handle,by_title,by_offer=load_sources()
    rows=[]; counts=Counter(); pilot=[]
    for r in triage['rows']:
        if not str(r['product_id']).startswith('online:'): continue
        codes=[i['code'] for i in r.get('issues',[])]
        if 'price_updated' not in codes and 'strikethrough_price_updated' not in codes: continue
        shop,src,key,attempts=choose(r,by_handle,by_title,by_offer)
        merchant_price=dec((r.get('price') or {}).get('value'))
        merchant_sale=dec((r.get('salePrice') or {}).get('value'))
        shop_price=dec(shop.get('price')) if shop else None
        shop_compare=dec(shop.get('compare_at_price')) if shop else None
        issue_set=sorted(set(codes))
        if not shop:
            state='blocked_no_shopify_price_source'
        elif 'strikethrough_price_updated' in issue_set or merchant_sale or shop_compare:
            state='review_promotional_price_or_compare_at_price'
        elif merchant_price == shop_price:
            state='monitor_only_merchant_price_matches_shopify_current_price'
        else:
            state='candidate_price_only_patch_to_shopify_current_price'
        item={'product_id':r['product_id'],'offerId':r.get('offerId'),'title':r.get('title'),'merchant_link':r.get('link'),'issue_codes':issue_set,'merchant_price':merchant_price,'merchant_sale_price':merchant_sale,'shopify_price':shop_price,'shopify_compare_at_price':shop_compare,'shopify_source':src,'shopify_match_key':key,'shopify_variant_sku':shop.get('sku') if shop else None,'shopify_variant_id':shop.get('source_variant_id') if shop else None,'shopify_product_status':shop.get('status') if shop else None,'decision_state':state,'suggested_write':({'productAttributes.price':{'amountMicros':str(int(round(float(shop_price)*1000000))),'currencyCode':'BRL'},'updateMask':'productAttributes.price'} if state=='candidate_price_only_patch_to_shopify_current_price' else None),'evidence_attempts':attempts[:4]}
        counts[state]+=1
        if state=='candidate_price_only_patch_to_shopify_current_price' and len(pilot)<PILOT_LIMIT:
            item['selected_for_pilot_if_approved']=True; pilot.append(item['product_id'])
        else:
            item['selected_for_pilot_if_approved']=False
        rows.append(item)
    payload={'generated_at':now(),'read_only':True,'source_labels':['fact_merchant_center','fact_shopify_local_snapshot','derived_reconciliation'],'summary':{'triage_productstatuses_read':triage['summary']['productstatuses_read'],'price_or_strikethrough_products':len(rows),'decision_state_counts':dict(counts),'pilot_limit':PILOT_LIMIT,'selected_for_price_only_pilot':len(pilot),'target_issue_instances':triage['summary']['target_issue_instances']},'approval_packet':{'recommended_option':'price_only_pilot_100','scope':'Patch only online ProductInputs productAttributes.price to Shopify current variant price for selected candidate rows; no salePrice/strikethrough rows in pilot.','data_source':'accounts/*/dataSources/10636492695','route':'Merchant API ProductInputs v1 PATCH updateMask=productAttributes.price','requires_private_rollback':True,'requires_delayed_productstatuses_recheck':True},'rows':rows,'not_performed':['Merchant write','ProductInputs patch','Content API upsert/delete','Shopify write','Tiny write','feed fetch/upload','salePrice/strikethrough update','local/LIA change','campaign/message/send']}
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    lines=['# LK GMC post-GTIN price_updated preview — 2026-05-14','',f"Gerado em: `{payload['generated_at']}`",'', '## Summary']
    lines += [f"- Productstatuses lidos: `{payload['summary']['triage_productstatuses_read']}`", f"- Produtos online com price/strikethrough issue: `{len(rows)}`", f"- Decision states: `{dict(counts)}`", f"- Piloto recomendado: `{len(pilot)}` price-only rows"]
    lines += ['', '## Recomendação', '- Primeiro aplicar **somente preço atual** em 100 produtos sem `strikethrough_price_updated`/salePrice/compareAt; rota Merchant API ProductInputs v1 `productAttributes.price`.', '- Deixar `strikethrough_price_updated` para preview separado, porque envolve sale/compare-at e pode afetar preço riscado.', '', '## Amostras do piloto']
    for x in [r for r in rows if r.get('selected_for_pilot_if_approved')][:12]:
        lines.append(f"- `{x['product_id']}` — Merchant {x['merchant_price']} → Shopify {x['shopify_price']} — {x['title']}")
    lines += ['', '## Não executado'] + [f'- {x}' for x in payload['not_performed']]
    MD.write_text('\n'.join(lines)+'\n')
    BRAIN.write_text(MD.read_text())
    print(json.dumps({'summary':payload['summary'],'out':str(OUT),'md':str(MD)},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
