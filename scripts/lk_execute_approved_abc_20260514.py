#!/usr/bin/env python3
from __future__ import annotations
import base64, json, os, pathlib, re, subprocess, tempfile, time, urllib.error, urllib.parse, urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
NOTION_PREVIEW = ROOT/'reports/lk-compras-julio-notion-preview-droper-15-2026-05-14.json'
URL_PREVIEW = ROOT/'reports/lk-gmc-a-url-probe-landing-page-errors-2026-05-14.json'
ATTR_PREVIEW = ROOT/'reports/lk-gmc-b-color-age-gender-preview-2026-05-14.json'
OUT_JSON = ROOT/'reports/lk-approved-abc-execution-2026-05-14.json'
OUT_MD = ROOT/'reports/lk-approved-abc-execution-2026-05-14.md'
NOTION_DB_ENCOMENDA = '2b127dc9-e033-805b-81b6-f62f5467ce77'
DATA_SOURCE_ID = '10636492695'
CONTENT_SCOPE = 'https://www.googleapis.com/auth/content'
MERCHANT_API = 'https://merchantapi.googleapis.com/products/v1/'


def utc_now(): return datetime.now(timezone.utc).isoformat()

def load_doppler() -> dict[str,str]:
    token = os.environ.get('DOPPLER_TOKEN') or DOPPLER_TOKEN_FILE.read_text().strip()
    req = urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
    req.add_header('Authorization','Basic '+base64.b64encode((token+':').encode()).decode())
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())

def request_json(url: str, token: str|None=None, method='GET', payload: dict[str,Any]|None=None, headers: dict[str,str]|None=None, attempts=6, timeout=150) -> dict[str,Any]:
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode('utf-8')
    last = ''
    for i in range(1, attempts+1):
        req = urllib.request.Request(url, data=data, method=method)
        if token: req.add_header('Authorization','Bearer '+token)
        if payload is not None: req.add_header('Content-Type','application/json; charset=utf-8')
        for k,v in (headers or {}).items(): req.add_header(k,v)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                raw = r.read().decode()
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            raw = e.read().decode(errors='replace')
            last = f'http_{e.code}: {raw[:1200]}'
            if e.code not in {429,500,502,503,504} or i == attempts:
                raise RuntimeError(last) from e
        except Exception as e:
            last = str(e)[:1200]
            if i == attempts: raise RuntimeError(last) from e
        time.sleep(min(60, 2**i))
    raise RuntimeError(last or 'request_failed')

# Google/Merchant auth helpers

def b64url(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).decode().rstrip('=')

def parse_service_account(secrets: dict[str,str]) -> dict[str,Any]:
    raw = secrets.get('GOOGLE_SERVICE_ACCOUNT_JSON') or secrets.get('GA4_LK_N8N_ZIPPER_SERVICE_ACCOUNT') or secrets.get('GA4_LK_SERVICE_ACCOUNT')
    if not raw: raise RuntimeError('missing_google_service_account_secret')
    try: return json.loads(raw)
    except json.JSONDecodeError: return json.loads(base64.b64decode(raw).decode())

def google_access_token(sa: dict[str,Any]) -> str:
    now = int(time.time())
    claim = {'iss': sa['client_email'], 'scope': CONTENT_SCOPE, 'aud': sa.get('token_uri') or 'https://oauth2.googleapis.com/token', 'iat': now, 'exp': now + 3600}
    header = {'alg':'RS256','typ':'JWT'}
    signing_input = b64url(json.dumps(header,separators=(',',':')).encode())+'.'+b64url(json.dumps(claim,separators=(',',':')).encode())
    with tempfile.NamedTemporaryFile('w', delete=False) as f:
        f.write(sa['private_key']); key_path=f.name
    try:
        sig = subprocess.run(['openssl','dgst','-sha256','-sign',key_path], input=signing_input.encode(), capture_output=True, check=True).stdout
    finally:
        pathlib.Path(key_path).unlink(missing_ok=True)
    body = urllib.parse.urlencode({'grant_type':'urn:ietf:params:oauth:grant-type:jwt-bearer','assertion':signing_input+'.'+b64url(sig)}).encode()
    req = urllib.request.Request(sa.get('token_uri') or 'https://oauth2.googleapis.com/token', data=body, method='POST')
    req.add_header('Content-Type','application/x-www-form-urlencoded')
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())['access_token']

def product_parts(pid: str):
    parts = pid.split(':',3)
    if len(parts)!=4: raise ValueError('bad product id '+pid)
    return parts

def product_input_name(mid: str, pid: str):
    channel, lang, label, offer = product_parts(pid)
    if channel != 'online': raise ValueError('only_online_supported '+pid)
    encoded = b64url(f'{lang}~{label}~{offer}'.encode())
    return f'accounts/{mid}/productInputs/{encoded}', encoded, lang, label, offer

def content_product_get(mid: str, token: str, pid: str) -> dict[str,Any]:
    url = f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products/{urllib.parse.quote(pid, safe="")}'
    return request_json(url, token=token)

def merchant_product_get(mid: str, token: str, encoded: str) -> dict[str,Any]:
    name = f'accounts/{mid}/products/{encoded}'
    return request_json(MERCHANT_API + urllib.parse.quote(name, safe='/'), token=token)

def patch_product_input_attrs(mid: str, token: str, pid: str, attrs: dict[str,Any]) -> dict[str,Any]:
    name, _encoded, lang, label, offer = product_input_name(mid, pid)
    body = {'name': name, 'offerId': offer, 'contentLanguage': lang, 'feedLabel': label, 'productAttributes': attrs}
    masks = ','.join('productAttributes.'+k for k in attrs.keys())
    qs = urllib.parse.urlencode({'dataSource': f'accounts/{mid}/dataSources/{DATA_SOURCE_ID}', 'updateMask': masks})
    return request_json(MERCHANT_API + urllib.parse.quote(name, safe='/') + '?' + qs, token=token, method='PATCH', payload=body)

# Notion helpers

def notion_title(page: dict[str,Any]) -> str:
    for p in (page.get('properties') or {}).values():
        if p.get('type') == 'title': return ''.join(t.get('plain_text','') for t in p.get('title',[]))
    return ''

def notion_headers(token: str) -> dict[str,str]:
    return {'Notion-Version':'2022-06-28'}

def notion_query_by_title(token: str, title: str) -> list[dict[str,Any]]:
    payload = {'page_size':5, 'filter': {'property':'Nome','title': {'equals': title}}}
    return request_json(f'https://api.notion.com/v1/databases/{NOTION_DB_ENCOMENDA}/query', token=token, method='POST', payload=payload, headers=notion_headers(token)).get('results',[])

def notion_create_card(token: str, card: dict[str,Any]) -> dict[str,Any]:
    name = f"Recompra Droper — {card['produto_lk']} — Tam {card['tamanho']} — {card['sku']}"
    props = {
        'Nome': {'title': [{'text': {'content': name}}]},
        'Status da Compra': {'status': {'name': 'Aguardando Aprovação'}},
        'Modelo': {'rich_text': [{'text': {'content': card['produto_lk'][:1800]}}]},
        'Tamanho': {'rich_text': [{'text': {'content': str(card.get('tamanho') or '')}}]},
        'Fornecedor': {'rich_text': [{'text': {'content': 'Droper'}}]},
        'Origem': {'select': {'name': 'Nacional'}},
        'Link': {'url': card.get('droper_link') or None},
        'Custo': {'number': parse_brl(card.get('droper_preco'))},
        'Pedido # ID': {'rich_text': [{'text': {'content': 'LK OS / stockout-recompra 120d'}}]},
        'Avisar Fornecedor': {'select': {'name': 'Não'}},
        'Programar Pagamento': {'select': {'name': 'Não'}},
    }
    props = {k:v for k,v in props.items() if not (k=='Link' and not v.get('url'))}
    children = [{'object':'block','type':'paragraph','paragraph':{'rich_text':[{'text':{'content': txt[:1800]}}]}} for txt in [
        f"Demanda 120d: {card.get('demanda_120d')}",
        f"Produto Droper: {card.get('droper_nome')} | Preço: {card.get('droper_preco')} | Match: {card.get('qualidade_match')}",
        "Ação humana: conferir disponibilidade, preço e logística; comprar/logar manualmente se fizer sentido.",
        "Guardrail Hermes: não comprou, não reservou, não contatou fornecedor/grupo e não alterou Shopify/Tiny/Merchant."
    ]]
    payload = {'parent': {'database_id': NOTION_DB_ENCOMENDA}, 'properties': props, 'children': children}
    return request_json('https://api.notion.com/v1/pages', token=token, method='POST', payload=payload, headers=notion_headers(token))

def parse_brl(text: str|None) -> float|None:
    if not text: return None
    m = re.search(r'([0-9\.]+,[0-9]{2})', text)
    if not m: return None
    return float(m.group(1).replace('.','').replace(',','.'))

def execute_notion(secrets: dict[str,str]) -> dict[str,Any]:
    token = secrets.get('NOTION_TOKEN_LK') or secrets.get('NOTION_API_KEY')
    cards = json.loads(NOTION_PREVIEW.read_text())['cards']
    results=[]
    if not token:
        return {'status':'blocked_missing_notion_token','created':0,'skipped':0,'results':[]}
    for card in cards:
        title = f"Recompra Droper — {card['produto_lk']} — Tam {card['tamanho']} — {card['sku']}"
        try:
            existing = notion_query_by_title(token, title)
            if existing:
                results.append({'title': title, 'status':'skipped_existing', 'page_id': existing[0].get('id')})
            else:
                page = notion_create_card(token, card)
                results.append({'title': title, 'status':'created', 'page_id': page.get('id'), 'url': page.get('url')})
            time.sleep(0.35)
        except Exception as e:
            results.append({'title': title, 'status':'error', 'error': str(e)[:500]})
            break
    return {'status':'completed' if all(r['status'] in {'created','skipped_existing'} for r in results) and len(results)==len(cards) else 'partial_or_error', 'created':sum(r['status']=='created' for r in results), 'skipped':sum(r['status']=='skipped_existing' for r in results), 'errors':sum(r['status']=='error' for r in results), 'database_id':NOTION_DB_ENCOMENDA, 'results':results}

# Shopify URL diff

def shopify_graphql(secrets: dict[str,str], query: str, variables: dict[str,Any]) -> dict[str,Any]:
    store = secrets.get('SHOPIFY_STORE_URL') or secrets.get('SHOPIFY_STORE') or secrets.get('SHOPIFY_SHOP_NAME')
    token = secrets.get('SHOPIFY_ACCESS_TOKEN') or secrets.get('SHOPIFY_ADMIN_TOKEN') or secrets.get('SHOPIFY_API_TOKEN')
    if not store or not token: raise RuntimeError('missing_shopify_credentials')
    store = store.replace('https://','').replace('http://','').strip('/')
    url = f'https://{store}/admin/api/2024-01/graphql.json'
    payload = {'query':query, 'variables':variables}
    return request_json(url, method='POST', payload=payload, headers={'X-Shopify-Access-Token': token})

def execute_shopify_diff(secrets: dict[str,str]) -> dict[str,Any]:
    rows = json.loads(URL_PREVIEW.read_text()).get('rows')
    if not rows:
        # fallback parse from md not needed; json currently has rows
        data = json.loads(URL_PREVIEW.read_text())
        rows = data.get('landing_page_errors') or []
    data = json.loads(URL_PREVIEW.read_text())
    rows = data.get('rows') or data.get('products') or data.get('landing_page_errors') or []
    if not rows:
        # reconstruct from known md is avoided; return blocked with file path
        return {'status':'blocked_no_machine_rows_in_url_preview_json', 'source':str(URL_PREVIEW)}
    q = '''query ProductByHandle($handle:String!){ productByHandle(handle:$handle){ id legacyResourceId title handle status onlineStoreUrl totalVariants variants(first:20){nodes{id legacyResourceId title sku availableForSale}} } }'''
    out=[]
    for r in rows:
        pid = r.get('productId') or r.get('product_id') or r.get('id')
        title = r.get('title') or r.get('product_title')
        link = r.get('link') or r.get('merchant_link') or r.get('url')
        handle = (urllib.parse.urlparse(link or '').path.rstrip('/').split('/')[-1] if link else '')
        item = {'product_id':pid,'merchant_title':title,'merchant_link':link,'handle':handle}
        try:
            resp = shopify_graphql(secrets, q, {'handle':handle})
            p = (resp.get('data') or {}).get('productByHandle')
            if p:
                item.update({'shopify_state':'handle_exists','shopify_product_id':p.get('legacyResourceId'),'shopify_title':p.get('title'),'shopify_status':p.get('status'),'onlineStoreUrl':p.get('onlineStoreUrl'),'variant_count':p.get('totalVariants')})
            else:
                item.update({'shopify_state':'handle_not_found','recommended_next':'find replacement handle or mark Merchant item stale; no Shopify write executed'})
        except Exception as e:
            item.update({'shopify_state':'error','error':str(e)[:500]})
        out.append(item); time.sleep(0.2)
    return {'status':'completed_readonly', 'checked':len(out), 'state_counts':dict(Counter(x['shopify_state'] for x in out)), 'rows':out, 'not_performed':['shopify_write','merchant_link_patch','redirect_creation','feed_upload']}

# Merchant attrs

def execute_merchant_attrs(secrets: dict[str,str]) -> dict[str,Any]:
    mid = secrets.get('MERCHANT_CENTER_ID_LK')
    if not mid: return {'status':'blocked_missing_merchant_id'}
    token = google_access_token(parse_service_account(secrets))
    preview_rows = json.loads(ATTR_PREVIEW.read_text())['rows']
    grouped: dict[str,dict[str,Any]] = {}
    for r in preview_rows:
        pid = r['productId']
        g = grouped.setdefault(pid, {'product_id':pid,'title':r.get('title'),'suggested_attrs':{},'evidence':{},'source_rows':[]})
        attr = r['attribute']
        field = {'age group':'ageGroup','gender':'gender','color':'color'}[attr]
        g['suggested_attrs'][field] = r['suggested_value']
        g['evidence'][field] = r.get('evidence')
        g['source_rows'].append(r)
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True); os.chmod(PRIVATE_DIR,0o700)
    rollback_path = PRIVATE_DIR/f'lk-gmc-approved-c-attrs-rollback-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.json'
    rollback_records=[]; exec_results=[]; verify=[]
    for pid,g in grouped.items():
        name, encoded, *_ = product_input_name(mid, pid)
        current = content_product_get(mid, token, pid)
        current_subset = {k:current.get(k) for k in ['color','ageGroup','gender','sizes','title','offerId','id']}
        rollback_records.append({'product_id':pid, 'product_input_name':name, 'current_content_api_product_resource':current, 'current_subset':current_subset, 'target_attrs':g['suggested_attrs'], 'evidence':g['evidence']})
    rollback_path.write_text(json.dumps({'generated_at':utc_now(),'scope':'Approved C: Merchant API v1 ProductInputs PATCH color/ageGroup/gender only','dataSource':DATA_SOURCE_ID,'records':rollback_records}, ensure_ascii=False, indent=2)+'\n')
    os.chmod(rollback_path,0o600)
    for rec in rollback_records:
        pid = rec['product_id']; target = rec['target_attrs']
        cur = rec['current_subset']
        todo = {k:v for k,v in target.items() if str(cur.get(k) or '') != str(v or '')}
        if not todo:
            exec_results.append({'product_id':pid,'execution_status':'skipped_already_matching','patched_attrs':{}})
            continue
        try:
            patch_product_input_attrs(mid, token, pid, todo)
            exec_results.append({'product_id':pid,'execution_status':'patched','patched_attrs':todo})
        except Exception as e:
            exec_results.append({'product_id':pid,'execution_status':'error','patched_attrs':todo,'error':str(e)[:800]})
            break
        time.sleep(0.25)
    # initial exact readback
    time.sleep(8)
    for rec in rollback_records:
        pid=rec['product_id']; target=rec['target_attrs']
        try:
            fresh = content_product_get(mid, token, pid)
            actual = {k:fresh.get(k) for k in target}
            verify.append({'product_id':pid,'verify_status':'read','expected':target,'actual':actual,'match_expected':all(str(actual.get(k) or '') == str(v or '') for k,v in target.items())})
        except Exception as e:
            verify.append({'product_id':pid,'verify_status':'error','expected':target,'error':str(e)[:500],'match_expected':False})
    return {'status':'completed' if all(x.get('execution_status') in {'patched','skipped_already_matching'} for x in exec_results) else 'partial_or_error', 'preview_attribute_rows':len(preview_rows), 'unique_products':len(grouped), 'execution_counts':dict(Counter(x.get('execution_status') for x in exec_results)), 'verify_counts':dict(Counter(('match' if x.get('match_expected') else 'mismatch') for x in verify)), 'rollback_snapshot_path':str(rollback_path), 'execution_results':exec_results, 'verified_results':verify, 'not_performed':['price_update','availability_update','title_update','category_update','merchant_delete','shopify_write','tiny_write','feed_upload']}

def write_md(payload: dict[str,Any]):
    lines=['# LK Approved A/B/C Execution — 2026-05-14','',f"Gerado em: `{payload['generated_at']}`",'', '## Resultado rápido',
           f"- Pacote A Notion/Júlio: `{payload['a_notion']['status']}` — criados {payload['a_notion'].get('created',0)}, existentes {payload['a_notion'].get('skipped',0)}, erros {payload['a_notion'].get('errors',0)}.",
           f"- Pacote B Shopify diff: `{payload['b_shopify_diff']['status']}` — {payload['b_shopify_diff'].get('checked',0)} URLs checadas; estados {payload['b_shopify_diff'].get('state_counts',{})}.",
           f"- Pacote C Merchant attrs: `{payload['c_merchant_attrs']['status']}` — {payload['c_merchant_attrs'].get('preview_attribute_rows',0)} linhas / {payload['c_merchant_attrs'].get('unique_products',0)} produtos; writes {payload['c_merchant_attrs'].get('execution_counts',{})}; readback {payload['c_merchant_attrs'].get('verify_counts',{})}.",
           '', '## Pacote B — Shopify read-only diff']
    for r in payload['b_shopify_diff'].get('rows',[]):
        lines += [f"- `{r.get('product_id')}` — handle `{r.get('handle')}` — `{r.get('shopify_state')}` — Shopify status `{r.get('shopify_status','')}` — {r.get('shopify_title') or r.get('merchant_title')}"]
    lines += ['', '## Pacote C — readback mismatches / atenção']
    mism=[v for v in payload['c_merchant_attrs'].get('verified_results',[]) if not v.get('match_expected')]
    if not mism: lines.append('- Nenhum mismatch no readback inicial.')
    else:
        for v in mism[:50]: lines.append(f"- `{v.get('product_id')}` expected={v.get('expected')} actual={v.get('actual')} status={v.get('verify_status')}")
    lines += ['', '## Snapshots / auditoria', f"- Rollback C privado: `{payload['c_merchant_attrs'].get('rollback_snapshot_path')}`", '- Arquivo JSON público: `reports/lk-approved-abc-execution-2026-05-14.json`', '', '## Não executado', '- Compra/reserva/pagamento/WhatsApp/fornecedor.', '- Shopify write/redirect/feed upload.', '- Preço, availability, title, categoria, Tiny, campanhas.']
    OUT_MD.write_text('\n'.join(lines)+'\n', encoding='utf-8')

def main():
    secrets = load_doppler()
    payload={'generated_at':utc_now(), 'approval':'Lucas approved A B C in Telegram', 'a_notion':None, 'b_shopify_diff':None, 'c_merchant_attrs':None}
    payload['a_notion']=execute_notion(secrets)
    payload['b_shopify_diff']=execute_shopify_diff(secrets)
    payload['c_merchant_attrs']=execute_merchant_attrs(secrets)
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    write_md(payload)
    print(json.dumps({'status':'done','out_json':str(OUT_JSON),'out_md':str(OUT_MD),'a':payload['a_notion']['status'],'b':payload['b_shopify_diff']['status'],'c':payload['c_merchant_attrs']['status'],'c_verify':payload['c_merchant_attrs'].get('verify_counts')}, ensure_ascii=False))

if __name__ == '__main__': main()
