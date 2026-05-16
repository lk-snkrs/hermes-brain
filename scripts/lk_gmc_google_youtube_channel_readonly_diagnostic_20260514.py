#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, json, pathlib, urllib.request, urllib.parse, urllib.error, time, re
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
ABC=ROOT/'scripts/lk_execute_approved_abc_20260514.py'
OUT=ROOT/'reports/lk-gmc-2026-05-14-google-youtube-channel-readonly-diagnostic.json'
MD=ROOT/'reports/lk-gmc-2026-05-14-google-youtube-channel-readonly-diagnostic.md'
BRAIN=ROOT/'areas/lk/rotinas/gmc-2026-05-14-google-youtube-channel-readonly-diagnostic.md'
API_DS='10636492695'
GOOGLE_PUB_NAME='Google & YouTube'
SAMPLE_SKUS=['01424-002-2','553558140-7','AQ9129-170-5','AQ9129-170-7','AQ9129-170-9','GW3773-39']
SAMPLE_PIDS=[f'online:pt:BR:{s}' for s in SAMPLE_SKUS]

def load_module(p,name):
    spec=importlib.util.spec_from_file_location(name,p); m=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(m); return m
abc=load_module(ABC,'abc')

def now(): return datetime.now(timezone.utc).isoformat()

def safe_keys(d): return sorted(d.keys()) if isinstance(d,dict) else []

def req_json(url, *, token=None, payload=None, headers=None, method=None, attempts=3):
    data=None if payload is None else json.dumps(payload,ensure_ascii=False).encode()
    if method is None: method='POST' if payload is not None else 'GET'
    last=None
    for i in range(1, attempts+1):
        req=urllib.request.Request(url,data=data,method=method)
        if token: req.add_header('Authorization','Bearer '+token)
        if payload is not None: req.add_header('Content-Type','application/json')
        for k,v in (headers or {}).items(): req.add_header(k,v)
        try:
            with urllib.request.urlopen(req,timeout=90) as r:
                raw=r.read().decode(errors='replace')
                return r.status, json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            raw=e.read().decode(errors='replace')
            try: body=json.loads(raw) if raw else {}
            except Exception: body={'raw':raw[:1000]}
            last=(e.code, body)
            if e.code not in {429,500,502,503,504}: return e.code, body
        except Exception as e:
            last=(0, {'error':str(e)[:500]})
        time.sleep(min(20,2**i))
    return last or (0, {'error':'request_failed'})

def shopify_context(secrets):
    store=(secrets.get('SHOPIFY_STORE_URL') or secrets.get('SHOPIFY_STORE') or secrets.get('SHOPIFY_SHOP_NAME') or '').replace('https://','').replace('http://','').strip('/')
    if store and not store.endswith('.myshopify.com') and '.' not in store: store+='.myshopify.com'
    token=secrets.get('SHOPIFY_ACCESS_TOKEN') or secrets.get('SHOPIFY_ADMIN_TOKEN') or secrets.get('SHOPIFY_API_TOKEN') or ''
    if not store or not token: raise RuntimeError('missing_shopify_credentials')
    return store, token

def gql(store, token, query, variables=None):
    code,body=req_json(f'https://{store}/admin/api/2025-01/graphql.json', payload={'query':query,'variables':variables or {}}, headers={'X-Shopify-Access-Token':token})
    return {'status_code':code,'body':body}

def rest(store, token, path):
    code,body=req_json(f'https://{store}/admin/api/2025-01/{path}', headers={'X-Shopify-Access-Token':token})
    return {'status_code':code,'body':body}

def merchant_product(mid, token, pid):
    code,body=req_json(f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products/{urllib.parse.quote(pid,safe="")}', token=token, attempts=2)
    if code==200 and isinstance(body,dict):
        return {'status_code':code,'source':body.get('source'),'price':body.get('price'),'salePrice':body.get('salePrice'),'title':body.get('title'),'link':body.get('link'),'offerId':body.get('offerId'),'top_level_keys':safe_keys(body)}
    return {'status_code':code,'error_keys':safe_keys(body)}

def productstatus(mid, token, pid):
    code,body=req_json(f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/productstatuses/{urllib.parse.quote(pid,safe="")}', token=token, attempts=2)
    issues=[]; destinations=[]
    if code==200 and isinstance(body,dict):
        for iss in body.get('itemLevelIssues') or []:
            if iss.get('code') in {'price_updated','strikethrough_price_updated','landing_page_error','availability_updated'}:
                issues.append({k:iss.get(k) for k in ['code','attributeName','detail','description','servability','resolution']})
        destinations=body.get('destinationStatuses') or []
    return {'status_code':code,'target_issues':issues,'destinationStatuses':destinations[:10]}

def find_google_publication(publications):
    for p in publications:
        if p.get('name')==GOOGLE_PUB_NAME:
            return p
    return None

def main():
    secrets=abc.load_doppler()
    mid=secrets['MERCHANT_CENTER_ID_LK']
    google_token=abc.google_access_token(abc.parse_service_account(secrets))
    store, shop_token=shopify_context(secrets)

    pubs_q='''query Publications { publications(first:100) { nodes { id name supportsFuturePublishing catalog { id title status } } } }'''
    pubs_resp=gql(store, shop_token, pubs_q)
    pubs=(((pubs_resp['body'].get('data') or {}).get('publications') or {}).get('nodes') or []) if pubs_resp['status_code']==200 else []
    google_pub=find_google_publication(pubs)
    google_pub_id=google_pub.get('id') if google_pub else None

    # Introspect/query available fields relevant to channels/catalogs/apps to avoid guessing unsupported endpoints.
    introspection_q='''query Introspection { __schema { queryType { fields { name description args { name type { kind name ofType { kind name } } } type { kind name ofType { kind name } } } } } }'''
    intro_resp=gql(store, shop_token, introspection_q)
    fields=[]
    if intro_resp['status_code']==200:
        for f in ((((intro_resp['body'].get('data') or {}).get('__schema') or {}).get('queryType') or {}).get('fields') or []):
            if re.search(r'publication|catalog|channel|app|market|feed', f.get('name',''), re.I):
                fields.append({'name':f.get('name'),'args':[a.get('name') for a in f.get('args') or []]})

    # Product sample: publication status + resource publication record + merchant final + productstatus.
    sample=[]
    var_q='''query VariantBySku($q:String!,$pub:ID!){ productVariants(first:5, query:$q){ nodes { id legacyResourceId sku price compareAtPrice updatedAt inventoryQuantity product { id legacyResourceId title status handle updatedAt publishedOnPublication(publicationId:$pub) resourcePublicationsV2(first:30){ nodes { isPublished publishDate publication { id name } } } seo { title description } } } } }'''
    for sku,pid in zip(SAMPLE_SKUS,SAMPLE_PIDS):
        resp=gql(store, shop_token, var_q, {'q':'sku:'+sku,'pub':google_pub_id or ''})
        nodes=(((resp['body'].get('data') or {}).get('productVariants') or {}).get('nodes') or []) if resp['status_code']==200 else []
        node=nodes[0] if nodes else {}
        prod=node.get('product') or {}
        pubs_nodes=((prod.get('resourcePublicationsV2') or {}).get('nodes') or [])
        google_node=next((x for x in pubs_nodes if (x.get('publication') or {}).get('name')==GOOGLE_PUB_NAME), None)
        m=merchant_product(mid, google_token, pid)
        ps=productstatus(mid, google_token, pid)
        sample.append({
            'sku':sku,'product_id':pid,'shopify_found':bool(node),'shopify_variant': {
                'price': node.get('price'),'compareAtPrice': node.get('compareAtPrice'),'updatedAt': node.get('updatedAt'),'legacyResourceId': node.get('legacyResourceId')
            } if node else {},
            'shopify_product': {
                'title': prod.get('title'),'status': prod.get('status'),'handle': prod.get('handle'),'updatedAt': prod.get('updatedAt'),'publishedOnGoogleYoutube': prod.get('publishedOnPublication'),'googlePublicationRecord': {'isPublished': (google_node or {}).get('isPublished'), 'publishDate': (google_node or {}).get('publishDate')} if google_node else None,
                'published_publications': [((x.get('publication') or {}).get('name')) for x in pubs_nodes if x.get('isPublished')]
            } if prod else {},
            'merchant_content_api': m,
            'merchant_productstatus': ps,
            'classification': 'shopify_google_published_but_merchant_price_stale' if node and prod.get('publishedOnPublication') and ((m.get('price') or {}).get('value') not in {node.get('price'), None}) else 'review'
        })
        time.sleep(.12)

    # REST read-only endpoints that may expose sales-channel/publication context. No writes.
    rest_probes={}
    for path in ['publications.json?limit=250','product_listings.json?limit=5','products.json?limit=1&status=active','webhooks.json?limit=250']:
        r=rest(store, shop_token, path)
        body=r.get('body') if isinstance(r,dict) else {}
        rest_probes[path]={'status_code':r.get('status_code'),'top_level_keys':safe_keys(body),'count_hint': {k:len(v) for k,v in body.items() if isinstance(v,list)} if isinstance(body,dict) else None, 'error': body.get('errors') if isinstance(body,dict) else None}
        time.sleep(.1)

    # Merchant data source detailed info.
    code,ds=req_json('https://merchantapi.googleapis.com/datasources/v1/'+urllib.parse.quote(f'accounts/{mid}/dataSources/{API_DS}',safe='/'), token=google_token)
    report={
        'generated_at':now(),
        'mode':'approved_read_only_google_youtube_channel_diagnostic',
        'authorization':'Lucas chose option 1: Google & YouTube / Shopify channel read-only diagnostic.',
        'shopify_publications': {'status_code':pubs_resp['status_code'], 'count':len(pubs), 'publications':[{'name':p.get('name'),'id_suffix':(p.get('id') or '').rsplit('/',1)[-1], 'supportsFuturePublishing':p.get('supportsFuturePublishing'), 'catalog':p.get('catalog')} for p in pubs], 'google_youtube_publication': {'name': google_pub.get('name'), 'id_suffix': google_pub_id.rsplit('/',1)[-1]} if google_pub else None},
        'shopify_graphql_query_fields_relevant': fields,
        'shopify_rest_readonly_probes': rest_probes,
        'merchant_primary_api_datasource': {'status_code':code, 'resource': ds if code==200 else {'error_keys':safe_keys(ds)}},
        'sample_sku_diagnostics': sample,
        'counts': {
            'sample_count':len(sample),
            'shopify_found':sum(1 for x in sample if x.get('shopify_found')),
            'published_on_google_youtube':sum(1 for x in sample if (x.get('shopify_product') or {}).get('publishedOnGoogleYoutube')),
            'merchant_price_stale_vs_shopify_price':sum(1 for x in sample if x.get('shopify_variant',{}).get('price') and ((x.get('merchant_content_api',{}).get('price') or {}).get('value') != x.get('shopify_variant',{}).get('price'))),
            'merchant_price_issue_instances':sum(len(x.get('merchant_productstatus',{}).get('target_issues') or []) for x in sample),
        },
        'interpretation': [],
        'next_checklist_ui_readonly': [
            'Shopify Admin > Sales channels > Google & YouTube: abrir product sync/status/feed diagnostics.',
            'Filtrar pelos SKUs amostra e confirmar se o app mostra preço antigo, erro de sync, pending review ou last synced timestamp.',
            'Merchant Center > Products > Data sources: confirmar se DS 10636492695 aparece como Google & YouTube/Content API channel e se há regra/attribute source para price.',
            'Merchant Center > Automatic improvements > Item updates: manter ligado por enquanto; só alterar com packet separado.',
            'Se UI mostrar botão de resync/reprocess em Google & YouTube, preparar plano com screenshots + rollback/monitor antes de qualquer execução.'
        ],
        'not_performed':['Shopify write','Shopify app/channel config change','Google & YouTube resync button','Merchant write','ProductInputs PATCH','Content API write','data source update/delete','automatic item updates setting change','feed upload/fetchNow','Tiny write','campaign/send/contact']
    }
    if report['counts']['published_on_google_youtube']==len(sample):
        report['interpretation'].append('All sampled SKUs are active/found and published on Shopify Google & YouTube, so channel eligibility is not the blocker at publication level.')
    if report['counts']['merchant_price_stale_vs_shopify_price']:
        report['interpretation'].append('Merchant final Content API price remains stale vs Shopify current price for sampled SKUs; this points to Google & YouTube sync/output state or Merchant source merge, not Shopify catalog price itself.')
    if not any(f.get('name') in {'appInstallations','apps'} for f in fields):
        report['interpretation'].append('Current Shopify token/schema did not expose useful app-configuration internals; API can confirm publication status, but Google channel sync diagnostics likely require UI review or a channel-specific API not available here.')
    else:
        report['interpretation'].append('Shopify API exposes some app/query surfaces, but installation/config details were not enough to inspect Google channel sync settings safely.')
    OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

    lines=['# LK GMC Google & YouTube channel read-only diagnostic — 2026-05-14','',f"Generated: `{report['generated_at']}`",'', 'Status: `approved_read_only_diagnostic_complete`','', '## Escopo','- Diagnóstico read-only do canal Shopify `Google & YouTube` e da fonte Merchant API principal.','- Nenhum write, resync, fetchNow, settings change ou alteração Shopify/Merchant.', '', '## Achados', f"- Publicações Shopify encontradas: `{[p.get('name') for p in report['shopify_publications']['publications']]}`", f"- Google & YouTube publication ID suffix: `{(report['shopify_publications'].get('google_youtube_publication') or {}).get('id_suffix')}`", f"- Amostra: `{report['counts']['sample_count']}` SKUs; encontrados no Shopify `{report['counts']['shopify_found']}`; publicados no Google & YouTube `{report['counts']['published_on_google_youtube']}`.", f"- Stale price vs Shopify na amostra: `{report['counts']['merchant_price_stale_vs_shopify_price']}`.", '', '## Amostra']
    for x in sample:
        lines.append(f"- `{x['sku']}`: Shopify price `{x.get('shopify_variant',{}).get('price')}`, compare-at `{x.get('shopify_variant',{}).get('compareAtPrice')}`, Google & YouTube published `{x.get('shopify_product',{}).get('publishedOnGoogleYoutube')}`, Merchant price `{(x.get('merchant_content_api',{}).get('price') or {}).get('value')}`, issues `{[i.get('code') for i in x.get('merchant_productstatus',{}).get('target_issues',[])]}`.")
    lines += ['', '## Interpretação'] + [f'- {i}' for i in report['interpretation']]
    lines += ['', '## Próximo checklist read-only/UI'] + [f'- {i}' for i in report['next_checklist_ui_readonly']]
    lines += ['', '## Not performed'] + [f'- {i}' for i in report['not_performed']]
    MD.write_text('\n'.join(lines)+'\n')
    BRAIN.write_text(MD.read_text())
    print(json.dumps({'status':'complete','out':str(OUT),'counts':report['counts'],'md':str(MD),'brain':str(BRAIN)},ensure_ascii=False,indent=2))

if __name__=='__main__': main()
