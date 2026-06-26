#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,json,pathlib,urllib.parse,urllib.request,time,os
from collections import Counter,defaultdict
from datetime import datetime,timezone
ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
ABC=ROOT/'scripts/lk_execute_approved_abc_20260514.py'
EXEC=ROOT/'scripts/lk_gmc_residual_approved_executor_20260514.py'
CONTENT_REPAIR=ROOT/'reports/lk-gmc-2026-05-14-price-source-api-content-repair.json'
OUT=ROOT/'reports/lk-gmc-2026-05-14-price-source-diagnostic.json'
MD=ROOT/'reports/lk-gmc-2026-05-14-price-source-diagnostic.md'
BRAIN=ROOT/'areas/lk/rotinas/gmc-2026-05-14-price-source-diagnostic.md'
def load(p,n):
    spec=importlib.util.spec_from_file_location(n,p); m=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(m); return m
abc=load(ABC,'abc'); ex=load(EXEC,'ex')
def now(): return datetime.now(timezone.utc).isoformat()
def money_from_cents(v):
    if v in (None,''): return None
    return f'{int(v)/100:.2f}'
def money(v):
    if v in (None,''): return None
    try: return f'{float(v):.2f}'
    except Exception: return str(v)
def amount(d):
    if not isinstance(d,dict): return None
    if 'value' in d: return money(d.get('value'))
    if 'amountMicros' in d: return f"{int(d['amountMicros'])/1_000_000:.2f}"
    return None
def public_variant(link, variant_id):
    handle=urllib.parse.urlparse(link or '').path.rstrip('/').split('/')[-1]
    if not handle: return {'error':'no_handle'}
    url=f'https://lksneakers.com.br/products/{handle}.js'
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 LKOS price diagnostic'})
        data=json.loads(urllib.request.urlopen(req,timeout=20).read().decode())
        var=next((v for v in data.get('variants',[]) if str(v.get('id'))==str(variant_id)),None)
        if not var: return {'handle':handle,'status':'variant_not_found','variant_count':len(data.get('variants',[]))}
        return {'handle':handle,'status':'ok','price':money_from_cents(var.get('price')),'compare_at_price':money_from_cents(var.get('compare_at_price')),'sku':var.get('sku'),'title':var.get('title'),'available':var.get('available')}
    except Exception as e:
        return {'handle':handle,'status':'error','error':str(e)[:400]}
def target_from_shopify_variant(v):
    sp=money(v.get('price')) if v else None; cap=money(v.get('compareAtPrice')) if v else None
    sale=bool(cap and sp and float(cap)>float(sp))
    return {'price':cap if sale else sp,'salePrice':sp if sale else None,'raw_price':sp,'raw_compareAtPrice':cap,'sale_mode':sale}
def target_from_public(var):
    sp=var.get('price'); cap=var.get('compare_at_price')
    sale=bool(cap and sp and float(cap)>float(sp))
    return {'price':cap if sale else sp,'salePrice':sp if sale else None,'raw_price':sp,'raw_compareAtPrice':cap,'sale_mode':sale}
def classify(actual_price, actual_sale, shop_target, pub_target):
    def matches(t): return actual_price==t.get('price') and actual_sale==t.get('salePrice')
    if matches(shop_target): return 'merchant_matches_shopify_admin'
    if pub_target.get('price') and matches(pub_target): return 'merchant_matches_public_shopify'
    if shop_target==pub_target and shop_target.get('price'): return 'merchant_stale_vs_shopify_and_public'
    if shop_target.get('price') and pub_target.get('price') and shop_target!=pub_target: return 'shopify_admin_public_diverge'
    return 'unknown_or_missing_public'
def main():
    sec=abc.load_doppler(); mid=sec['MERCHANT_CENTER_ID_LK']; token=abc.google_access_token(abc.parse_service_account(sec))
    repair=json.loads(CONTENT_REPAIR.read_text())
    # Diagnose all products that were either upserted or skipped as already matching from the price mismatch cohort.
    ids=[]
    for e in repair.get('executions',[]): ids.append(e['product_id'])
    for t in repair.get('triage',[]):
        if t.get('bucket')=='no_action_current_matches_shopify': ids.append(t['product_id'])
    ids=sorted(set(ids))
    rows=[]; cnt=Counter(); sample=defaultdict(list)
    for pid in ids:
        row={'product_id':pid}
        try:
            cp=abc.content_product_get(mid,token,pid)
            row.update({'content_source':cp.get('source'),'content_price':amount(cp.get('price')),'content_salePrice':amount(cp.get('salePrice')),'link':cp.get('link')})
            vid=ex.extract_variant_id(cp.get('link')) or (cp.get('offerId') if str(cp.get('offerId','')).isdigit() else None)
            row['legacy_variant']=vid
            v=ex.shopify_variant_by_legacy(abc,sec,vid) if vid else None
            st=target_from_shopify_variant(v)
            row['shopify_admin']={'sku':(v or {}).get('sku'),'variant_title':(v or {}).get('title'),**st}
            pv=public_variant(cp.get('link'),vid)
            row['public_product_js']=pv
            pt=target_from_public(pv) if pv.get('status')=='ok' else {'price':None,'salePrice':None}
            row['public_target']=pt
            row['diagnosis']=classify(row['content_price'],row['content_salePrice'],st,pt)
        except Exception as e:
            row['diagnosis']='error'; row['error']=str(e)[:800]
        cnt[row['diagnosis']]+=1
        if len(sample[row['diagnosis']])<8:
            sample[row['diagnosis']].append({k:row.get(k) for k in ['product_id','content_price','content_salePrice','legacy_variant','diagnosis']})
            if 'shopify_admin' in row: sample[row['diagnosis']][-1]['shopify_admin']=row['shopify_admin']
            if 'public_target' in row: sample[row['diagnosis']][-1]['public_target']=row['public_target']
        rows.append(row); time.sleep(.12)
    payload={'generated_at':now(),'mode':'read_only_diagnostic','input_products':len(ids),'diagnosis_counts':dict(cnt),'samples':{k:v for k,v in sample.items()},'rows':rows,'not_performed':['Merchant write','Content API write','Shopify write','Tiny write','feed fetch/upload','campaign/message/send']}
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    lines=['# LK GMC price source diagnostic — 2026-05-14','',f"Generated: `{payload['generated_at']}`",'',f"Input products: `{len(ids)}`",'', '## Diagnosis counts']
    for k,v in cnt.most_common(): lines.append(f'- {k}: `{v}`')
    lines += ['', '## Interpretação', '- `merchant_stale_vs_shopify_and_public`: Merchant/Content não acompanha Shopify Admin nem `/products/{handle}.js`; provável fonte/sobrescrita/cache do Merchant, não erro de preço Shopify.', '- `merchant_matches_shopify_admin`: sem ação de preço necessária no readback atual.', '- `shopify_admin_public_diverge`: precisa investigar Markets/publicação antes de escrever preço.', '', '## Não executado']+[f'- {x}' for x in payload['not_performed']]
    MD.write_text('\n'.join(lines)+'\n'); BRAIN.write_text(MD.read_text())
    print(json.dumps({'input_products':len(ids),'diagnosis_counts':dict(cnt),'out':str(OUT)},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
