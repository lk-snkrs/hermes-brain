#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, json, pathlib, urllib.parse, urllib.request, urllib.error, time
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
ABC=ROOT/'scripts/lk_execute_approved_abc_20260514.py'
AUD=ROOT/'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
OUT=ROOT/'reports/lk-gmc-2026-05-14-landing-page-current-drilldown.json'
MD=ROOT/'reports/lk-gmc-2026-05-14-landing-page-current-drilldown.md'
BRAIN=ROOT/'areas/lk/rotinas/gmc-2026-05-14-landing-page-current-drilldown.md'

def load(p,n):
    spec=importlib.util.spec_from_file_location(n,p); m=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(m); return m
abc=load(ABC,'abc'); aud=load(AUD,'aud')

def now(): return datetime.now(timezone.utc).isoformat()

def request_url(url, method='GET'):
    req=urllib.request.Request(url, method=method, headers={'User-Agent':'Mozilla/5.0 (compatible; LKOS landing diagnostic; +https://lksneakers.com.br)'})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body=r.read(2048) if method!='HEAD' else b''
            return {'method':method,'status_code':r.status,'final_url':r.geturl(),'content_type':r.headers.get('content-type'),'body_prefix':body.decode(errors='replace')[:300]}
    except urllib.error.HTTPError as e:
        return {'method':method,'status_code':e.code,'final_url':getattr(e,'url',url),'error':str(e)}
    except Exception as e:
        return {'method':method,'status_code':None,'final_url':url,'error':str(e)[:500]}

def extract_handle(link):
    path=urllib.parse.urlparse(link or '').path.rstrip('/')
    return path.split('/')[-1] if path else None

def shopify_product_by_handle(secrets, handle):
    q='''query P($handle:String!){ productByHandle(handle:$handle){ id legacyResourceId title handle status onlineStoreUrl totalVariants variants(first:50){nodes{id legacyResourceId title sku availableForSale}} } }'''
    return ((abc.shopify_graphql(secrets,q,{'handle':handle}).get('data') or {}).get('productByHandle'))

def main():
    sec=abc.load_doppler(); mid=sec['MERCHANT_CENTER_ID_LK']; token=abc.google_access_token(abc.parse_service_account(sec))
    statuses=aud.list_all('productstatuses', mid, token)
    rows=[]
    for st in statuses:
        issues=[i for i in (st.get('itemLevelIssues') or []) if i.get('code')=='landing_page_error']
        if not issues: continue
        pid=st.get('productId')
        row={'product_id':pid,'status_title':st.get('title'),'issues':issues,'destinations':st.get('destinationStatuses') or []}
        try:
            prod=abc.content_product_get(mid, token, pid)
            row['merchant_product']={k:prod.get(k) for k in ['id','offerId','source','title','link','channel','contentLanguage','targetCountry','price','availability']}
            link=prod.get('link')
        except Exception as e:
            row['merchant_product_error']=str(e)[:800]; link=None
        handle=extract_handle(link)
        row['handle']=handle
        if link:
            row['public_head']=request_url(link,'HEAD')
            row['public_get']=request_url(link,'GET')
            # also Shopify .js, which bypasses theme but confirms public product endpoint/variant data when available.
            js_url=f'https://lksneakers.com.br/products/{handle}.js' if handle else None
            row['public_product_js']=request_url(js_url,'GET') if js_url else None
        try:
            p=shopify_product_by_handle(sec, handle) if handle else None
            row['shopify_admin']={'exists': bool(p), **({k:p.get(k) for k in ['legacyResourceId','title','handle','status','onlineStoreUrl','totalVariants']} if p else {})}
            if p:
                offer=str((row.get('merchant_product') or {}).get('offerId') or '')
                vars=(p.get('variants') or {}).get('nodes') or []
                row['shopify_admin']['matching_variants']=[v for v in vars if str(v.get('sku'))==offer or str(v.get('legacyResourceId'))==offer][:5]
        except Exception as e:
            row['shopify_admin']={'error':str(e)[:800]}
        rows.append(row); time.sleep(.12)
    def classify(r):
        prod=r.get('merchant_product') or {}; sh=r.get('shopify_admin') or {}; get=r.get('public_get') or {}; js=r.get('public_product_js') or {}
        if get.get('status_code')==200 and js.get('status_code')==200:
            return 'public_ok_status_lag_or_googlebot_specific'
        if sh.get('exists') and sh.get('status')=='ACTIVE' and (get.get('status_code')!=200):
            return 'shopify_active_but_public_unavailable_or_redirect_issue'
        if not sh.get('exists'):
            return 'shopify_handle_not_found_stale_merchant_link'
        if sh.get('status') in {'DRAFT','ARCHIVED'}:
            return 'shopify_not_public_stale_or_suppress_candidate'
        return 'needs_manual_review'
    for r in rows: r['classification']=classify(r)
    payload={'generated_at':now(),'mode':'read_only_landing_page_current_drilldown','landing_page_error_products':len(rows),'classification_counts':dict(Counter(r['classification'] for r in rows)),'rows':rows,'not_performed':['Merchant delete','Merchant link patch','Shopify publish/unpublish','redirect creation','feed fetch/upload','campaign/message/send']}
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    lines=['# LK GMC landing page current drilldown — 2026-05-14','',f"Generated: `{payload['generated_at']}`",'',f"Landing-page products: `{len(rows)}`",'', '## Classification counts']
    for k,v in payload['classification_counts'].items(): lines.append(f'- {k}: `{v}`')
    lines += ['', '## Rows']
    for r in rows:
        mp=r.get('merchant_product') or {}; sh=r.get('shopify_admin') or {}; get=r.get('public_get') or {}; js=r.get('public_product_js') or {}
        lines.append(f"- `{r['product_id']}` / offer `{mp.get('offerId')}` / `{mp.get('title') or r.get('status_title')}`: class `{r['classification']}`, public GET `{get.get('status_code')}`, .js `{js.get('status_code')}`, Shopify `{sh.get('status') if sh.get('exists') else sh.get('exists')}`")
    lines += ['', '## Next safe step', '- If public GET and `.js` are 200 but status remains, monitor/reprocess only; no delete/suppress.', '- If Shopify is DRAFT/ARCHIVED/not_found and public 404 persists, prepare exact-ID suppress/delete approval with rollback; do not publish Shopify automatically.', '', '## Not performed'] + [f'- {x}' for x in payload['not_performed']]
    MD.write_text('\n'.join(lines)+'\n'); BRAIN.write_text(MD.read_text())
    print(json.dumps({'landing_page_error_products':len(rows),'classification_counts':payload['classification_counts'],'out':str(OUT)},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
