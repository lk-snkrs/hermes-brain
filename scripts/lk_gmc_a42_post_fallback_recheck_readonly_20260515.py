#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import pathlib
import time
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from typing import Any

ROOT = pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
ABC_PATH = ROOT / 'scripts/lk_execute_approved_abc_20260514.py'
PACKET_A = ROOT / 'reports/gmc_approval_packets_20260515/packet_a_price_only_42_preview.json'
PACKET_B = ROOT / 'reports/gmc_approval_packets_20260515/packet_b_draft404_20_preview.json'
APPLY = ROOT / 'reports/lk-gmc-2026-05-15-content-api-price-only-fallback-a42.json'
RUN = '2026-05-15-a42-post-fallback-readonly-recheck'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN}.json'
OUT_MD = ROOT / f'areas/lk/rotinas/gmc-{RUN}.md'


def load_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    return mod

abc = load_module(ABC_PATH, 'abc_a42_recheck')


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def money(v: Any) -> str | None:
    if v in (None, ''):
        return None
    try:
        return f"{Decimal(str(v)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}"
    except Exception:
        return str(v)


def amount(d: Any) -> str | None:
    if not isinstance(d, dict):
        return None
    if 'value' in d:
        return money(d.get('value'))
    if 'amountMicros' in d:
        return money(Decimal(int(d['amountMicros'])) / Decimal(1_000_000))
    return None


def content_url(mid: str, pid: str) -> str:
    return f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products/{urllib.parse.quote(pid, safe="")}'


def status_url(mid: str, pid: str) -> str:
    return f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/productstatuses/{urllib.parse.quote(pid, safe="")}'


def optional_get(url: str, token: str) -> dict[str, Any] | None:
    try:
        return abc.request_json(url, token=token)
    except Exception as e:
        if 'http_404' in str(e):
            return None
        raise


def merchant_v1(mid: str, token: str, pid: str) -> dict[str, Any] | None:
    try:
        _name, encoded, *_ = abc.product_input_name(mid, pid)
        return abc.merchant_product_get(mid, token, encoded)
    except Exception as e:
        return {'error': str(e)[:1000]}


def list_all(endpoint: str, mid: str, token: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    page = None
    while True:
        qs = {'maxResults': '250'}
        if page:
            qs['pageToken'] = page
        data = abc.request_json(f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/{endpoint}?' + urllib.parse.urlencode(qs), token=token)
        batch = data.get('resources') or []
        rows.extend(batch)
        page = data.get('nextPageToken')
        if not page or not batch:
            break
    return rows


def public_product_js(link: str) -> dict[str, Any]:
    parsed = urllib.parse.urlparse(link or '')
    parts = [p for p in parsed.path.split('/') if p]
    handle = None
    if 'products' in parts:
        i = parts.index('products')
        if i + 1 < len(parts):
            handle = parts[i + 1]
    variant = (urllib.parse.parse_qs(parsed.query).get('variant') or [None])[0]
    if not handle:
        return {'public_error': 'no_handle', 'public_status': None}
    url = f'https://lksneakers.com.br/products/{handle}.js'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 LKOS readonly A42 post fallback recheck'})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read().decode())
        variants = data.get('variants') or []
        chosen = None
        if variant:
            chosen = next((v for v in variants if str(v.get('id')) == str(variant)), None)
        if not chosen and variants:
            chosen = variants[0]
        cents = chosen.get('price') if chosen else None
        cmp_cents = chosen.get('compare_at_price') if chosen else None
        return {
            'handle': handle,
            'variant_id': variant,
            'public_status': 200,
            'public_variant_price_brl': money(Decimal(cents) / Decimal(100)) if cents is not None else None,
            'public_variant_compare_at_brl': money(Decimal(cmp_cents) / Decimal(100)) if cmp_cents is not None else None,
            'public_variant_title': chosen.get('title') if chosen else None,
        }
    except Exception as e:
        return {'handle': handle, 'variant_id': variant, 'public_error': str(e)[:800], 'public_status': None}


def extract_price_issues(status: dict[str, Any] | None) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    if not status:
        return out
    for issue in status.get('itemLevelIssues') or []:
        blob = json.dumps(issue, ensure_ascii=False).lower()
        if 'price' in blob or 'preço' in blob or 'mismatched' in blob or 'automatic item update' in blob:
            out.append({
                'code': issue.get('code'),
                'servability': issue.get('servability'),
                'resolution': issue.get('resolution'),
                'attributeName': issue.get('attributeName'),
                'description': issue.get('description'),
                'detail': issue.get('detail'),
            })
    return out


def classify(content_price: str | None, merchant_price: str | None, public_price: str | None, original_target: str | None) -> str:
    # Primary definition: the effective Merchant/Content product read must equal the live public variant.
    content_eq_public = bool(public_price) and content_price == public_price
    merchant_eq_public = (merchant_price is None) or (bool(public_price) and merchant_price == public_price)
    if content_eq_public and merchant_eq_public and public_price == original_target:
        return 'a_merchant_content_now_matches_public_target'
    if content_eq_public and merchant_eq_public and public_price != original_target:
        return 'b_merchant_content_equals_public_not_original_target_snapshot_likely_stale_no_rollback'
    return 'c_merchant_content_differs_from_live_public_needs_review'


def main() -> None:
    packet_a = json.loads(PACKET_A.read_text())
    packet_b = json.loads(PACKET_B.read_text())
    apply = json.loads(APPLY.read_text())
    apply_by_pid = {r['product_id']: r for r in apply.get('rows', [])}

    sec = abc.load_doppler()
    mid = sec['MERCHANT_CENTER_ID_LK']
    token = abc.google_access_token(abc.parse_service_account(sec))

    products = list_all('products', mid, token)
    statuses = list_all('productstatuses', mid, token)
    product_ids = {p.get('id') for p in products}
    status_by_pid = {s.get('productId'): s for s in statuses}
    status_ids = set(status_by_pid)

    rows = []
    for r in packet_a:
        pid = r['product_id']
        cur = optional_get(content_url(mid, pid), token)
        v1 = merchant_v1(mid, token, pid) or {}
        pa = v1.get('productAttributes') or {}
        pub = public_product_js(r.get('merchant_link') or '')
        status = status_by_pid.get(pid) or optional_get(status_url(mid, pid), token)
        content_price = amount((cur or {}).get('price'))
        content_sale_price = amount((cur or {}).get('salePrice'))
        merchant_price = amount(pa.get('price'))
        merchant_sale_price = amount(pa.get('salePrice'))
        public_price = pub.get('public_variant_price_brl')
        target = r.get('target_shopify_price_brl')
        cls = classify(content_price, merchant_price, public_price, target)
        issues = extract_price_issues(status)
        row = {
            'product_id': pid,
            'offerId': r.get('offerId'),
            'title': r.get('title'),
            'merchant_link': r.get('merchant_link'),
            'target_original_local_snapshot_brl': target,
            'fallback_immediate_verify_price_brl': (apply_by_pid.get(pid) or {}).get('actual_price_brl'),
            'content_current_price_brl': content_price,
            'content_current_sale_price_brl': content_sale_price,
            'content_source': (cur or {}).get('source'),
            'merchant_v1_current_price_brl': merchant_price,
            'merchant_v1_current_sale_price_brl': merchant_sale_price,
            'merchant_v1_error': v1.get('error'),
            **pub,
            'content_matches_public': content_price == public_price,
            'merchant_v1_matches_public': (merchant_price == public_price) if merchant_price is not None else None,
            'public_matches_original_target': public_price == target,
            'classification': cls,
            'price_issue_count': len(issues),
            'price_issues': issues,
        }
        rows.append(row)
        time.sleep(0.12)

    verify_b = []
    for r in packet_b:
        link = r.get('merchant_link') or ''
        pub = public_product_js(link)
        verify_b.append({
            'product_id': r['product_id'],
            'offerId': r.get('offerId'),
            'title': r.get('title'),
            'merchant_link': link,
            'expected_packet_shopify_status': r.get('shopify_status'),
            'absent_from_products_list': r['product_id'] not in product_ids,
            'absent_from_productstatuses_list': r['product_id'] not in status_ids,
            'public_js_status': pub.get('public_status'),
            'public_js_error': pub.get('public_error'),
            'handle': pub.get('handle'),
        })
        time.sleep(0.08)

    class_counts = Counter(r['classification'] for r in rows)
    issue_rows = [r for r in rows if r['price_issue_count']]
    summary = {
        'a42_rows': len(rows),
        'classification_counts': dict(class_counts),
        'content_matches_public': sum(1 for r in rows if r['content_matches_public']),
        'merchant_v1_matches_public': sum(1 for r in rows if r['merchant_v1_matches_public'] is True),
        'public_matches_original_target': sum(1 for r in rows if r['public_matches_original_target']),
        'price_issue_rows': len(issue_rows),
        'price_issue_codes': dict(Counter(i.get('code') for r in issue_rows for i in r.get('price_issues', []))),
        'public_errors': sum(1 for r in rows if r.get('public_error')),
        'b20_targets': len(verify_b),
        'b20_absent_products_list': sum(1 for r in verify_b if r['absent_from_products_list']),
        'b20_absent_productstatuses_list': sum(1 for r in verify_b if r['absent_from_productstatuses_list']),
        'b20_public_js_404_or_absent': sum(1 for r in verify_b if r.get('public_js_error') and ('HTTP Error 404' in r.get('public_js_error','') or '404' in r.get('public_js_error',''))),
        'merchant_products_list_count': len(products),
        'merchant_productstatuses_list_count': len(statuses),
    }
    payload = {
        'generated_at': now(),
        'status': 'readonly_post_fallback_recheck_complete',
        'merchant_id': mid,
        'summary': summary,
        'rows': rows,
        'verify_b20': verify_b,
        'not_performed': ['Merchant write', 'Content API write/upsert', 'Merchant ProductInputs PATCH', 'Shopify write', 'Tiny write', 'feed fetch/upload/fetchNow', 'salePrice/strikethrough update', 'campaign/message/contact'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')

    lines = [
        '# LK GMC — A42 post-fallback read-only recheck', '',
        f"Gerado em: `{payload['generated_at']}`", f"Status: `{payload['status']}`", '',
        '## Resumo',
        f"- A42 total: `{summary['a42_rows']}`",
        f"- (a) Merchant/Content agora igual ao público e ao target original: `{class_counts.get('a_merchant_content_now_matches_public_target', 0)}`",
        f"- (b) Merchant/Content igual ao público, mas diferente do target original: `{class_counts.get('b_merchant_content_equals_public_not_original_target_snapshot_likely_stale_no_rollback', 0)}`",
        f"- (c) Merchant/Content diferente do público: `{class_counts.get('c_merchant_content_differs_from_live_public_needs_review', 0)}`",
        f"- Content API product price == público: `{summary['content_matches_public']}/42`",
        f"- Merchant API v1 product price == público: `{summary['merchant_v1_matches_public']}/42`",
        f"- Público == target original snapshot: `{summary['public_matches_original_target']}/42`",
        f"- Linhas com issues de preço em productstatuses: `{summary['price_issue_rows']}`; códigos: `{summary['price_issue_codes']}`",
        f"- B20 DRAFT/404 ausentes products.list: `{summary['b20_absent_products_list']}/20`; productstatuses.list: `{summary['b20_absent_productstatuses_list']}/20`; public .js 404: `{summary['b20_public_js_404_or_absent']}/20`",
        '',
        '## Recomendação',
    ]
    if class_counts.get('c_merchant_content_differs_from_live_public_needs_review', 0):
        lines.append('- Não fazer rollback em lote. Tratar somente as linhas (c): ainda há divergência entre Merchant/Content e vitrine pública live.')
    else:
        lines.append('- Não fazer rollback. As linhas estão alinhadas com a vitrine pública live; diferenças contra snapshot original indicam snapshot local stale/wrong.')
    lines += ['', '## Classificação A42']
    for r in rows:
        short = {'a_merchant_content_now_matches_public_target':'a','b_merchant_content_equals_public_not_original_target_snapshot_likely_stale_no_rollback':'b','c_merchant_content_differs_from_live_public_needs_review':'c'}[r['classification']]
        issue = f" issues={r['price_issue_count']}" if r['price_issue_count'] else ''
        lines.append(f"- ({short}) `{r['product_id']}` — Content `{r['content_current_price_brl']}` / Merchant v1 `{r['merchant_v1_current_price_brl']}` / Público `{r['public_variant_price_brl']}` / Target orig `{r['target_original_local_snapshot_brl']}`{issue} — {r.get('title')}")
    lines += ['', '## B20 DRAFT/404 recheck']
    bad_b = [r for r in verify_b if not (r['absent_from_products_list'] and r['absent_from_productstatuses_list'] and r.get('public_js_error'))]
    if not bad_b:
        lines.append('- Todos os 20 seguem ausentes de products.list/productstatuses.list e continuam 404/ausentes no `.js` público.')
    else:
        for r in bad_b:
            lines.append(f"- Atenção `{r['product_id']}` — absent_products={r['absent_from_products_list']} absent_statuses={r['absent_from_productstatuses_list']} public_js_status={r.get('public_js_status')} error={r.get('public_js_error')}")
    lines += ['', '## Artefatos', f'- JSON: `{OUT_JSON}`', f'- Markdown: `{OUT_MD}`', '', '## Não executado'] + [f'- {x}' for x in payload['not_performed']]
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text('\n'.join(lines) + '\n')
    print(json.dumps({'summary': summary, 'json': str(OUT_JSON), 'markdown': str(OUT_MD)}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
