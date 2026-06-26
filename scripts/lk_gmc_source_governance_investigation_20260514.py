#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, json, pathlib, urllib.parse, urllib.request, urllib.error, time, re, os
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
ABC = ROOT / 'scripts/lk_execute_approved_abc_20260514.py'
OUT = ROOT / 'reports/lk-gmc-2026-05-14-source-governance-investigation.json'
MD = ROOT / 'reports/lk-gmc-2026-05-14-source-governance-investigation.md'
BRAIN = ROOT / 'areas/lk/rotinas/gmc-2026-05-14-source-governance-investigation.md'
API_DS='10636492695'
AUTOFEED_DS='10525577766'
LOCAL_DS='10636384718'
SUPP_DS='10646853947'
KNOWN_DS=[AUTOFEED_DS, API_DS, LOCAL_DS, SUPP_DS]


def load_module(p: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(m)
    return m

abc = load_module(ABC, 'abc')

def now(): return datetime.now(timezone.utc).isoformat()

def request_raw(url: str, token: str|None=None, method='GET', payload: dict[str,Any]|None=None, headers: dict[str,str]|None=None, attempts=3) -> tuple[int, Any]:
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode('utf-8')
    last=None
    for i in range(1, attempts+1):
        req = urllib.request.Request(url, data=data, method=method)
        if token: req.add_header('Authorization', 'Bearer '+token)
        if payload is not None: req.add_header('Content-Type', 'application/json; charset=utf-8')
        for k,v in (headers or {}).items(): req.add_header(k,v)
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                raw=r.read().decode(errors='replace')
                return r.status, json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            raw=e.read().decode(errors='replace')
            try: body=json.loads(raw) if raw else {}
            except Exception: body={'raw': raw[:1000]}
            last=(e.code, body)
            if e.code not in {429,500,502,503,504}: return e.code, body
        except Exception as e:
            last=(0, {'error': str(e)[:500]})
        time.sleep(min(20, 2**i))
    return last or (0, {'error':'request_failed'})

def safe_keys(d: Any):
    return sorted(d.keys()) if isinstance(d, dict) else []

def datasource_list(mid: str, token: str):
    url=f'https://merchantapi.googleapis.com/datasources/v1/accounts/{mid}/dataSources?pageSize=100'
    return request_raw(url, token)

def datasource_get(mid: str, ds: str, token: str):
    name=f'accounts/{mid}/dataSources/{ds}'
    url='https://merchantapi.googleapis.com/datasources/v1/'+urllib.parse.quote(name, safe='/')
    return request_raw(url, token)

def content_datafeeds_list(mid: str, token: str):
    return request_raw(f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/datafeeds', token)

def content_account_get(mid: str, token: str):
    return request_raw(f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/accounts/{mid}', token)

def content_product_sample(mid: str, token: str, pids: list[str]):
    rows=[]
    for pid in pids:
        code, body = request_raw(f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products/{urllib.parse.quote(pid, safe="")}', token, attempts=2)
        if code == 200 and isinstance(body, dict):
            rows.append({
                'product_id': pid,
                'status_code': code,
                'source': body.get('source'),
                'channel': body.get('channel'),
                'offerId': body.get('offerId'),
                'contentLanguage': body.get('contentLanguage'),
                'targetCountry': body.get('targetCountry'),
                'feedLabel': body.get('feedLabel'),
                'price': body.get('price'),
                'salePrice': body.get('salePrice'),
                'customAttributeNames': sorted([x.get('name') for x in body.get('customAttributes') or [] if x.get('name')])[:50],
                'top_level_keys': safe_keys(body),
            })
        else:
            rows.append({'product_id': pid, 'status_code': code, 'error_keys': safe_keys(body)})
        time.sleep(0.08)
    return rows

def merchant_product_sample(mid: str, token: str, pids: list[str]):
    rows=[]
    for pid in pids:
        try:
            _name, encoded, *_ = abc.product_input_name(mid, pid)
        except Exception as e:
            rows.append({'product_id': pid, 'encoding_error': str(e)[:200]}); continue
        code, body = request_raw('https://merchantapi.googleapis.com/products/v1/'+urllib.parse.quote(f'accounts/{mid}/products/{encoded}', safe='/'), token, attempts=2)
        if code == 200 and isinstance(body, dict):
            pa=body.get('productAttributes') or {}
            rows.append({'product_id': pid, 'status_code': code, 'name': body.get('name'), 'offerId': body.get('offerId'), 'productAttributes_keys': safe_keys(pa), 'price': pa.get('price'), 'salePrice': pa.get('salePrice'), 'top_level_keys': safe_keys(body)})
        else:
            rows.append({'product_id': pid, 'status_code': code, 'error_keys': safe_keys(body)})
        time.sleep(0.08)
    return rows

def shopify_graphql(secrets: dict[str,str], query: str, variables: dict[str,Any]|None=None):
    store = (secrets.get('SHOPIFY_STORE_URL') or secrets.get('SHOPIFY_STORE') or secrets.get('SHOPIFY_SHOP_NAME') or '').replace('https://','').replace('http://','').strip('/')
    if store and not store.endswith('.myshopify.com') and '.' not in store: store += '.myshopify.com'
    token = secrets.get('SHOPIFY_ACCESS_TOKEN') or secrets.get('SHOPIFY_ADMIN_TOKEN') or secrets.get('SHOPIFY_API_TOKEN') or ''
    if not store or not token:
        return {'ok': False, 'status':'missing_shopify_credentials'}
    url=f'https://{store}/admin/api/2025-01/graphql.json'
    code, body = request_raw(url, method='POST', payload={'query': query, 'variables': variables or {}}, headers={'X-Shopify-Access-Token': token})
    # Redact no secrets in response; errors okay.
    return {'ok': code == 200, 'status_code': code, 'body': body if code == 200 else {'error_keys': safe_keys(body), 'errors': body.get('errors') if isinstance(body,dict) else None}}

def shopify_rest(secrets: dict[str,str], path: str):
    store = (secrets.get('SHOPIFY_STORE_URL') or secrets.get('SHOPIFY_STORE') or secrets.get('SHOPIFY_SHOP_NAME') or '').replace('https://','').replace('http://','').strip('/')
    if store and not store.endswith('.myshopify.com') and '.' not in store: store += '.myshopify.com'
    token = secrets.get('SHOPIFY_ACCESS_TOKEN') or secrets.get('SHOPIFY_ADMIN_TOKEN') or secrets.get('SHOPIFY_API_TOKEN') or ''
    if not store or not token:
        return {'ok': False, 'status':'missing_shopify_credentials'}
    code, body = request_raw(f'https://{store}/admin/api/2025-01/{path}', headers={'X-Shopify-Access-Token': token})
    return {'ok': code == 200, 'status_code': code, 'body': body if code == 200 else {'error_keys': safe_keys(body), 'errors': body.get('errors') if isinstance(body,dict) else None}}

def codebase_refs():
    pats=[API_DS, 'merchantapi.googleapis.com', 'shoppingcontent.googleapis.com', 'Google & YouTube', 'google channel', 'Content API']
    hits=[]
    for base in [ROOT/'scripts', ROOT/'areas', ROOT/'reports']:
        if not base.exists(): continue
        for p in base.rglob('*'):
            if p.is_dir() or p.suffix.lower() not in {'.py','.md','.json','.yaml','.yml','.txt'}: continue
            try:
                s=p.read_text(errors='ignore')
            except Exception: continue
            found=[pat for pat in pats if pat.lower() in s.lower()]
            if found:
                hits.append({'path': str(p.relative_to(ROOT)), 'patterns': found[:5]})
            if len(hits) >= 120: break
    counts=Counter()
    for h in hits:
        for pat in h['patterns']: counts[pat]+=1
    return {'pattern_counts': dict(counts), 'sample_hits': hits[:60], 'total_hit_files_capped': len(hits)}

def summarize_shopify_apps(app_resp: dict[str,Any]):
    out={'available': False}
    body=app_resp.get('body') if isinstance(app_resp, dict) else None
    if app_resp.get('ok') and isinstance(body, dict):
        data=body.get('data') or {}
        nodes=(((data.get('appInstallations') or {}).get('nodes')) or [])
        out={'available': True, 'count': len(nodes), 'apps': []}
        for n in nodes:
            app=n.get('app') or {}
            title=app.get('title') or app.get('handle') or ''
            out['apps'].append({'title': title, 'handle': app.get('handle'), 'id_suffix': (app.get('id') or '')[-12:]})
        out['google_like_apps']=[x for x in out['apps'] if re.search(r'google|youtube|merchant|feed|shopping|simprosys|flexify|datafeed|channel', (x.get('title') or '')+' '+(x.get('handle') or ''), re.I)]
    else:
        out={'available': False, 'status_code': app_resp.get('status_code'), 'errors': (body or {}).get('errors') if isinstance(body,dict) else None}
    return out

def summarize_publications(pub_resp: dict[str,Any]):
    body=pub_resp.get('body') if isinstance(pub_resp, dict) else None
    if pub_resp.get('ok') and isinstance(body, dict):
        nodes=((((body.get('data') or {}).get('publications') or {}).get('nodes')) or [])
        return {'available': True, 'count': len(nodes), 'publications':[{'name': n.get('name'), 'id_suffix': (n.get('id') or '')[-12:]} for n in nodes]}
    return {'available': False, 'status_code': pub_resp.get('status_code'), 'errors': (body or {}).get('errors') if isinstance(body,dict) else None}

def main():
    secrets=abc.load_doppler()
    mid=secrets['MERCHANT_CENTER_ID_LK']
    token=abc.google_access_token(abc.parse_service_account(secrets))
    pids=['online:pt:BR:01424-002-2','online:pt:BR:553558140-7','online:pt:BR:AQ9129-170-5','online:pt:BR:GW3773-39']

    ds_list_code, ds_list_body = datasource_list(mid, token)
    ds_get={}
    for ds in KNOWN_DS:
        c,b=datasource_get(mid, ds, token)
        ds_get[ds]={'status_code': c, 'resource': b if c==200 else {'error_keys': safe_keys(b)}}
    datafeeds_code, datafeeds_body=content_datafeeds_list(mid, token)
    acct_code, acct_body=content_account_get(mid, token)

    app_query='''query Apps { appInstallations(first: 100) { nodes { app { id title handle } launchUrl activeSubscriptions { status } } } }'''
    pub_query='''query Pubs { publications(first: 100) { nodes { id name } } }'''
    shop_query='''query ShopInfo { shop { name myshopifyDomain primaryDomain { url host } plan { displayName } } }'''
    shop_apps=shopify_graphql(secrets, app_query)
    shop_pubs=shopify_graphql(secrets, pub_query)
    shop_info=shopify_graphql(secrets, shop_query)
    shop_webhooks=shopify_rest(secrets, 'webhooks.json?limit=250')

    report={
      'generated_at': now(),
      'mode':'approved_read_only_source_governance_investigation',
      'authorization':'Lucas chose option 1: governance investigation without writes/settings changes.',
      'merchant_sources': {
        'dataSources_list_status_code': ds_list_code,
        'dataSources_list_count': len((ds_list_body or {}).get('dataSources') or []) if isinstance(ds_list_body, dict) else None,
        'dataSources_list_resources': (ds_list_body or {}).get('dataSources') if ds_list_code==200 and isinstance(ds_list_body,dict) else {'error_keys': safe_keys(ds_list_body)},
        'known_dataSources_get': ds_get,
        'content_datafeeds_list_status_code': datafeeds_code,
        'content_datafeeds': datafeeds_body if datafeeds_code==200 else {'error_keys': safe_keys(datafeeds_body)},
        'account_settings_status_code': acct_code,
        'account_settings_non_sensitive_keys': safe_keys(acct_body),
        'automaticImprovements': acct_body.get('automaticImprovements') if isinstance(acct_body, dict) else None,
      },
      'sample_readback': {
        'content_api_products': content_product_sample(mid, token, pids),
        'merchant_products_v1': merchant_product_sample(mid, token, pids),
      },
      'shopify_channel_evidence': {
        'shop_info': {'available': shop_info.get('ok'), 'body': shop_info.get('body') if shop_info.get('ok') else {'status_code': shop_info.get('status_code'), 'errors': (shop_info.get('body') or {}).get('errors') if isinstance(shop_info.get('body'),dict) else None}},
        'app_installations_summary': summarize_shopify_apps(shop_apps),
        'publications_summary': summarize_publications(shop_pubs),
        'webhooks_probe': {'available': shop_webhooks.get('ok'), 'status_code': shop_webhooks.get('status_code'), 'count': len((shop_webhooks.get('body') or {}).get('webhooks') or []) if shop_webhooks.get('ok') else None, 'topics_sample': sorted(set([w.get('topic') for w in ((shop_webhooks.get('body') or {}).get('webhooks') or []) if w.get('topic')]))[:50] if shop_webhooks.get('ok') else None},
      },
      'local_codebase_evidence': codebase_refs(),
      'interpretation': [],
      'not_performed':['Merchant/ProductInputs/Content API write','data source update/delete','automatic item update setting change','feed upload/fetchNow','Shopify write/app config change','Tiny write','campaign/send/contact']
    }
    # Interpret
    ds_resources=report['merchant_sources']['known_dataSources_get']
    api_res=(ds_resources.get(API_DS) or {}).get('resource') or {}
    auto_res=(ds_resources.get(AUTOFEED_DS) or {}).get('resource') or {}
    supp_res=(ds_resources.get(SUPP_DS) or {}).get('resource') or {}
    local_res=(ds_resources.get(LOCAL_DS) or {}).get('resource') or {}
    report['interpretation'].append('Primary online DS 10636492695 is the intended API ProductInputs owner, but final product readbacks remain stale after price PATCH; investigate the upstream app/job/channel that writes this data source, not the PATCH endpoint alone.')
    auto = ((report['merchant_sources'].get('automaticImprovements') or {}).get('itemUpdates') or {})
    if auto.get('effectiveAllowPriceUpdates') is True:
        report['interpretation'].append('Automatic price updates are effective and should remain enabled until upstream ownership is fixed; they are a safety net, not the primary source of truth.')
    google_like = report['shopify_channel_evidence']['app_installations_summary'].get('google_like_apps') if isinstance(report['shopify_channel_evidence']['app_installations_summary'], dict) else None
    if google_like:
        report['interpretation'].append('Shopify app installation evidence includes Google/feed-like apps; these are candidates for the upstream channel that may regenerate Merchant API input. Exact app config still requires UI review, not API mutation.')
    else:
        report['interpretation'].append('Shopify app installation query did not expose a confirmed Google/feed app with the current token/scope; Merchant UI / Shopify apps UI remains needed for final ownership confirmation.')

    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    lines=['# LK GMC source governance investigation — 2026-05-14','',f"Generated: `{report['generated_at']}`",'', 'Status: `approved_read_only_investigation_complete`','', '## Escopo aprovado','- Opção 1 escolhida por Lucas: investigar governança de fontes sem write/settings change.','- Nenhuma alteração em Merchant, Shopify, Tiny, feed, campanhas ou mensagens.','', '## Achados principais']
    lines += [f"- DataSources list status: `{ds_list_code}`; count: `{report['merchant_sources']['dataSources_list_count']}`.", f"- Content API datafeeds list status: `{datafeeds_code}`.", f"- Automatic price updates effective: `{auto.get('effectiveAllowPriceUpdates')}`."]
    apps=report['shopify_channel_evidence']['app_installations_summary']
    if apps.get('available'):
        lines.append(f"- Shopify app installations exposed by token: `{apps.get('count')}`; Google/feed-like candidates: `{apps.get('google_like_apps')}`.")
    else:
        lines.append(f"- Shopify app installations not fully available with current token/scope: `{apps.get('errors') or apps.get('status_code')}`.")
    pubs=report['shopify_channel_evidence']['publications_summary']
    if pubs.get('available'):
        lines.append(f"- Shopify publications exposed: `{[p.get('name') for p in pubs.get('publications', [])]}`.")
    lines += ['', '## Interpretação'] + [f'- {x}' for x in report['interpretation']]
    lines += ['', '## Próximo gate recomendado', '- Preparar **packet de UI/source ownership**: screenshots/export read-only no Merchant Center e Shopify Apps/Google channel para confirmar quem regenera DS `10636492695`.', '- Depois disso, escolher: (A) corrigir/upstream resync da fonte API; (B) limitar/autofeed com rollback; (C) experimento temporário de settings em coorte minúscula. Nenhuma opção executada agora.', '', '## Not performed']
    lines += [f'- {x}' for x in report['not_performed']]
    MD.write_text('\n'.join(lines)+'\n')
    BRAIN.write_text(MD.read_text())
    print(json.dumps({'status':'complete','out':str(OUT),'md':str(MD),'brain':str(BRAIN),'google_like_apps': apps.get('google_like_apps') if isinstance(apps,dict) else None, 'publications': pubs.get('publications') if isinstance(pubs,dict) else None}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
