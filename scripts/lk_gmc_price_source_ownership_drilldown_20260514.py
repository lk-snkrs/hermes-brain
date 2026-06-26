#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, json, pathlib, urllib.parse, urllib.error, urllib.request, time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
ABC = ROOT / 'scripts/lk_execute_approved_abc_20260514.py'
DIAG = ROOT / 'reports/lk-gmc-2026-05-14-price-source-diagnostic.json'
PLAN = ROOT / 'reports/lk-gmc-2026-05-14-price-source-overwrite-plan.json'
OUT = ROOT / 'reports/lk-gmc-2026-05-14-price-source-ownership-drilldown.json'
MD = ROOT / 'reports/lk-gmc-2026-05-14-price-source-ownership-drilldown.md'
BRAIN = ROOT / 'areas/lk/rotinas/gmc-2026-05-14-price-source-ownership-drilldown.md'
API_DS = '10636492695'
AUTOFEED_DS = '10525577766'
SUPPLEMENTAL_DS = '10646853947'
LOCAL_DS = '10636384718'

def load(p, n):
    spec = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(m)
    return m

abc = load(ABC, 'abc')

def now():
    return datetime.now(timezone.utc).isoformat()

def amount(d: Any):
    if not isinstance(d, dict): return None
    if 'value' in d: return f"{float(d['value']):.2f}"
    if 'amountMicros' in d: return f"{int(d['amountMicros'])/1_000_000:.2f}"
    return None

def request_raw(url: str, token: str, method='GET', payload: dict[str,Any]|None=None, attempts=3) -> tuple[int, Any]:
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode('utf-8')
    last = None
    for i in range(1, attempts+1):
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header('Authorization', 'Bearer ' + token)
        if payload is not None:
            req.add_header('Content-Type', 'application/json; charset=utf-8')
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                raw = r.read().decode()
                return r.status, json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            raw = e.read().decode(errors='replace')
            try: body = json.loads(raw) if raw else {}
            except Exception: body = {'raw': raw[:1000]}
            last = (e.code, body)
            if e.code not in {429,500,502,503,504}: return e.code, body
        except Exception as e:
            last = (0, {'error': str(e)[:500]})
        time.sleep(min(20, 2**i))
    return last or (0, {'error':'request_failed'})

def content_account_get(mid: str, token: str):
    # Read-only account settings. Some fields may be omitted depending on access/API generation.
    url = f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/accounts/{mid}'
    return request_raw(url, token)

def content_account_status(mid: str, token: str):
    url = f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/accountstatuses/{mid}'
    return request_raw(url, token)

def merchant_datasource_get(mid: str, ds: str, token: str):
    name = f'accounts/{mid}/dataSources/{ds}'
    url = 'https://merchantapi.googleapis.com/datasources/v1/' + urllib.parse.quote(name, safe='/')
    return request_raw(url, token)

def product_input_get(mid: str, pid: str, ds: str, token: str):
    name, encoded, lang, label, offer = abc.product_input_name(mid, pid)
    qs = urllib.parse.urlencode({'dataSource': f'accounts/{mid}/dataSources/{ds}'})
    url = 'https://merchantapi.googleapis.com/products/v1/' + urllib.parse.quote(name, safe='/') + '?' + qs
    code, body = request_raw(url, token, attempts=2)
    return code, body, encoded

def product_get_v1(mid: str, encoded: str, token: str):
    name = f'accounts/{mid}/products/{encoded}'
    url = 'https://merchantapi.googleapis.com/products/v1/' + urllib.parse.quote(name, safe='/')
    return request_raw(url, token, attempts=2)

def content_status_get(mid: str, pid: str, token: str):
    url = f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/productstatuses/{urllib.parse.quote(pid, safe="")}'
    return request_raw(url, token, attempts=2)

def pick_sample(rows):
    stale = [r for r in rows if r.get('diagnosis') == 'merchant_stale_vs_shopify_and_public']
    regular, sale, clear = [], [], []
    for r in stale:
        shop = r.get('shopify_admin') or {}
        cp, cs, tp, ts = r.get('content_price'), r.get('content_salePrice'), shop.get('price'), shop.get('salePrice')
        if cp != tp and not cs and not ts and len(regular) < 6: regular.append(r)
        elif ts and cs != ts and len(sale) < 6: sale.append(r)
        elif cs and not ts and len(clear) < 3: clear.append(r)
    ordered = regular + sale + clear
    seen=set(); out=[]
    for r in ordered:
        if r['product_id'] not in seen:
            seen.add(r['product_id']); out.append(r)
        if len(out) >= 12: break
    return out

def summarize_input(body: Any):
    pa = body.get('productAttributes') if isinstance(body, dict) else None
    if not isinstance(pa, dict):
        return {'exists': False}
    return {
        'exists': True,
        'name': body.get('name'),
        'offerId': body.get('offerId'),
        'price': amount(pa.get('price')),
        'salePrice': amount(pa.get('salePrice')),
        'title_present': bool(pa.get('title')),
        'link_present': bool(pa.get('link')),
        'availability': pa.get('availability'),
        'raw_keys': sorted(pa.keys())[:50],
    }

def main():
    sec = abc.load_doppler()
    mid = sec['MERCHANT_CENTER_ID_LK']
    token = abc.google_access_token(abc.parse_service_account(sec))
    diag = json.loads(DIAG.read_text())
    rows = diag.get('rows', [])
    sample = pick_sample(rows)

    account_code, account_body = content_account_get(mid, token)
    status_code, status_body = content_account_status(mid, token)
    ds_results = {}
    for ds in [AUTOFEED_DS, API_DS, LOCAL_DS, SUPPLEMENTAL_DS]:
        c, b = merchant_datasource_get(mid, ds, token)
        ds_results[ds] = {'status_code': c, 'resource': b if c == 200 else {'error': b}}

    probes = []
    source_presence_counts = Counter()
    api_input_vs_output = Counter()
    ds_price_values = defaultdict(Counter)
    auto_update_issue_counts = Counter()
    fresh_output_vs_shopify = Counter()
    for r in sample:
        pid = r['product_id']
        fresh_content = {}
        try:
            cur = abc.content_product_get(mid, token, pid)
            fresh_content = {'price': amount(cur.get('price')), 'salePrice': amount(cur.get('salePrice')), 'source': cur.get('source')}
        except Exception as e:
            fresh_content = {'error': str(e)[:500]}
        probe = {'product_id': pid, 'prior_content_output': {'price': r.get('content_price'), 'salePrice': r.get('content_salePrice'), 'source': r.get('content_source')}, 'fresh_content_output': fresh_content, 'shopify_target': r.get('shopify_admin'), 'public_target': r.get('public_target'), 'data_source_inputs': {}}
        encoded = None
        for ds in [API_DS, AUTOFEED_DS, SUPPLEMENTAL_DS, LOCAL_DS]:
            code, body, encoded = product_input_get(mid, pid, ds, token)
            summ = summarize_input(body) if code == 200 else {'exists': False, 'status_code': code, 'error_status': (body.get('error', {}) if isinstance(body, dict) else body)}
            probe['data_source_inputs'][ds] = summ
            if summ.get('exists'):
                source_presence_counts[ds] += 1
                ds_price_values[ds][(summ.get('price'), summ.get('salePrice'))] += 1
        if encoded:
            c, b = product_get_v1(mid, encoded, token)
            pa = b.get('productAttributes', {}) if c == 200 and isinstance(b, dict) else {}
            probe['merchant_v1_output'] = {'status_code': c, 'price': amount(pa.get('price')), 'salePrice': amount(pa.get('salePrice')), 'raw_keys': sorted(pa.keys())[:50] if isinstance(pa, dict) else []}
        sc, sb = content_status_get(mid, pid, token)
        issues = []
        if sc == 200 and isinstance(sb, dict):
            for iss in sb.get('itemLevelIssues') or []:
                if iss.get('code') in {'price_updated','strikethrough_price_updated'}:
                    issues.append({k: iss.get(k) for k in ['code','attributeName','detail','description','resolution','servability']})
                    auto_update_issue_counts[iss.get('code')] += 1
        probe['fresh_productstatus_price_issues'] = issues
        st = probe.get('shopify_target') or {}
        final_price = (probe.get('merchant_v1_output') or {}).get('price') or fresh_content.get('price')
        final_sale = (probe.get('merchant_v1_output') or {}).get('salePrice') or fresh_content.get('salePrice')
        if final_price == st.get('price') and final_sale == st.get('salePrice'):
            fresh_output_vs_shopify['fresh_output_matches_shopify_target'] += 1
        else:
            fresh_output_vs_shopify['fresh_output_stale_vs_shopify_target'] += 1
        api_in = probe['data_source_inputs'][API_DS]
        out = probe.get('merchant_v1_output') or {}
        if api_in.get('exists'):
            api_input_vs_output['api_input_exists'] += 1
            if api_in.get('price') == out.get('price') and api_in.get('salePrice') == out.get('salePrice'):
                api_input_vs_output['api_input_matches_final_output'] += 1
            else:
                api_input_vs_output['api_input_differs_from_final_output'] += 1
        probes.append(probe)
        time.sleep(0.12)

    auto = account_body.get('automaticImprovements') if isinstance(account_body, dict) else None
    payload = {
        'generated_at': now(),
        'mode': 'read_only_price_source_ownership_drilldown',
        'sample_size': len(sample),
        'sample_product_ids': [r['product_id'] for r in sample],
        'account_settings_probe': {
            'content_accounts_get_status_code': account_code,
            'automaticImprovements': auto if auto is not None else 'not_returned_by_api_or_not_accessible',
            'returned_non_sensitive_keys': sorted(account_body.keys()) if isinstance(account_body, dict) else [],
        },
        'account_status_probe': {'status_code': status_code, 'returned_non_sensitive_keys': sorted(status_body.keys()) if isinstance(status_body, dict) else []},
        'data_sources_get': ds_results,
        'source_presence_counts_in_sample': dict(source_presence_counts),
        'api_input_vs_final_output_counts': dict(api_input_vs_output),
        'fresh_output_vs_shopify_counts': dict(fresh_output_vs_shopify),
        'fresh_productstatus_price_issue_counts_in_sample': dict(auto_update_issue_counts),
        'data_source_price_value_counts_in_sample': {ds: {str(k): v for k, v in cnt.items()} for ds, cnt in ds_price_values.items()},
        'probes': probes,
        'interpretation': [],
        'not_performed': ['Merchant write','Content API write','ProductInputs PATCH','data source update/delete','automatic item update settings change','feed fetch/upload','Shopify write','Tiny write','campaign/message/send'],
    }
    if auto is None:
        payload['interpretation'].append('Content API accounts.get did not expose automaticImprovements in this access/API view; UI or Merchant settings export may still be needed before changing auto-update settings.')
    else:
        item_updates = ((auto or {}).get('itemUpdates') or {})
        if item_updates.get('effectiveAllowPriceUpdates') is True:
            payload['interpretation'].append('Automatic item price updates are enabled/effective at account level; productstatuses confirm Google is auto-updating mismatched prices from the online store with servability unaffected.')
    if source_presence_counts.get(API_DS, 0) == len(sample):
        payload['interpretation'].append('API ProductInput exists for every sampled stale item; missing API input is not the immediate cause.')
    if not source_presence_counts:
        payload['interpretation'].append('ProductInputs GET returned 404 for all sampled source/dataSource combinations even though final products are readable; source ownership could not be proven at ProductInput-read level, so use final product + account auto-update + productstatus evidence.')
    elif source_presence_counts.get(AUTOFEED_DS, 0) == 0:
        payload['interpretation'].append('Autofeed ProductInput was not readable/found for sampled exact IDs through ProductInputs v1; final product still has source=api, so the visible output is API-owned even though price is stale.')
    if fresh_output_vs_shopify.get('fresh_output_matches_shopify_target'):
        payload['interpretation'].append('Some fresh Merchant/Content reads now match Shopify target while productstatuses still show auto-update notices; status clearance can lag final product readback.')
    if fresh_output_vs_shopify.get('fresh_output_stale_vs_shopify_target'):
        payload['interpretation'].append('Some fresh final outputs remain stale vs Shopify target; those need source/feed regeneration or a tightly verified price/salePrice pilot after the ownership path is fixed.')
    if api_input_vs_output.get('api_input_matches_final_output') == len(sample):
        payload['interpretation'].append('Final Merchant v1 output matches API ProductInput price in the sample. This points to the API input itself being stale/reverted, not a final-output merge where API input has the correct target but loses to crawl.')
    elif api_input_vs_output.get('api_input_differs_from_final_output'):
        payload['interpretation'].append('Some API ProductInputs differ from final Merchant output; this would support final-output merge/overwrite diagnostics.')

    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
    lines = [
        '# LK GMC price source ownership drilldown — 2026-05-14', '',
        f"Generated: `{payload['generated_at']}`", '',
        f"Sample stale products probed: `{len(sample)}`", '',
        '## Read-only findings',
        f"- Account settings probe: HTTP `{account_code}`; automaticImprovements: `{'returned' if auto is not None else 'not_returned_by_api_or_not_accessible'}`.",
        f"- ProductInputs source presence in sample: `{dict(source_presence_counts)}`.",
        f"- API input vs final Merchant output: `{dict(api_input_vs_output)}`.",
        f"- Fresh final output vs Shopify target: `{dict(fresh_output_vs_shopify)}`.",
        f"- Fresh Productstatus price issue details in sample: `{dict(auto_update_issue_counts)}`.",
        '',
        '## Interpretation',
    ]
    lines += [f'- {x}' for x in payload['interpretation']] or ['- No strong interpretation generated; inspect JSON probes.']
    lines += ['', '## Probe samples']
    for p in probes[:6]:
        api_in = p['data_source_inputs'].get(API_DS, {})
        auto_in = p['data_source_inputs'].get(AUTOFEED_DS, {})
        lines.append(f"- `{p['product_id']}`: final `{p.get('merchant_v1_output',{}).get('price')}`/`{p.get('merchant_v1_output',{}).get('salePrice')}`, fresh Content `{p.get('fresh_content_output',{}).get('price')}`/`{p.get('fresh_content_output',{}).get('salePrice')}`, API input `{api_in.get('price')}`/`{api_in.get('salePrice')}`, autofeed input exists `{auto_in.get('exists')}`; Shopify target `{(p.get('shopify_target') or {}).get('price')}`/`{(p.get('shopify_target') or {}).get('salePrice')}`; status issue codes `{[i.get('code') for i in p.get('fresh_productstatus_price_issues', [])]}`")
    lines += ['', '## Next safe remediation design',
              '- Do **not** bulk-retry price writes yet.',
              '- If API input is stale and matches final output, the next corrective route is likely source-of-truth regeneration/resync of the API feed/channel for exact rows, or a small ProductInputs v1 pilot with post-delay readback that verifies the API input itself changed and stayed changed.',
              '- If Merchant UI confirms automatic price updates are active and overriding API, prepare a separate settings-change packet with rollback/screenshot/export before any change.',
              '', '## Not performed']
    lines += [f'- {x}' for x in payload['not_performed']]
    MD.write_text('\n'.join(lines) + '\n')
    BRAIN.write_text(MD.read_text())
    print(json.dumps({'sample_size': len(sample), 'source_presence_counts_in_sample': dict(source_presence_counts), 'api_input_vs_final_output_counts': dict(api_input_vs_output), 'out': str(OUT)}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
