#!/usr/bin/env python3
"""LK GMC P0 URL/checkout/landing review, read-only.

Opens the P0 package from the GMC correction preview into SKU-level evidence.
It queries Shopify Admin GraphQL with query operations only and checks public PDP URLs
with HTTP GET/HEAD. It does not change Merchant Center, Shopify, feed, checkout,
PDPs, theme, GSC, campaigns, or n8n.
"""
from __future__ import annotations

import base64
import csv
import json
import os
import pathlib
import re
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
MERCHANT = ROOT / 'reports/lk-merchant-center-feed-readonly-router-2026-05-11.json'
GMC_PREVIEW = ROOT / 'reports/lk-gmc-correction-preview-2026-05-12.json'
OUT_JSON = ROOT / 'reports/lk-gmc-p0-url-checkout-review-2026-05-12.json'
OUT_MD = ROOT / 'reports/lk-gmc-p0-url-checkout-review-2026-05-12.md'
OUT_CSV = ROOT / 'reports/lk-gmc-p0-url-checkout-review-2026-05-12.csv'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/gmc-p0-url-checkout-review-2026-05-12.md'
PUBLIC_HOST = 'https://lksneakers.com.br'

NOT_PERFORMED = [
    'merchant_center_write', 'supplemental_feed_update', 'product_insert_update_delete',
    'shopify_product_or_variant_write', 'shopify_theme_or_pdp_write', 'checkout_setting_change',
    'gsc_admin_or_indexing_submit', 'campaign_or_customer_send', 'supplier_contact',
    'purchase_or_po', 'external_marketplace_call', 'n8n_flow_creation',
]


def load_json(path: pathlib.Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding='utf-8'))


def load_doppler() -> dict[str, str]:
    token = os.environ.get('DOPPLER_TOKEN') or DOPPLER_TOKEN_FILE.read_text().strip()
    req = urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
    req.add_header('Authorization', 'Basic ' + base64.b64encode((token + ':').encode()).decode())
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def shopify_host(raw: str) -> str:
    raw = (raw or '').strip()
    raw = raw.removeprefix('https://').removeprefix('http://').rstrip('/')
    return raw


class Shopify:
    def __init__(self, secrets: dict[str, str]) -> None:
        host = shopify_host(secrets.get('SHOPIFY_STORE_URL') or secrets.get('SHOPIFY_SHOP') or '')
        token = secrets.get('SHOPIFY_ACCESS_TOKEN') or secrets.get('SHOPIFY_ADMIN_ACCESS_TOKEN')
        if not host or not token:
            raise RuntimeError('missing_shopify_readonly_credentials')
        self.url = f'https://{host}/admin/api/2024-01/graphql.json'
        self.token = token

    def gql(self, query: str, variables: dict[str, Any]) -> dict[str, Any]:
        if re.search(r'\bmutation\b', query, flags=re.I):
            raise RuntimeError('mutation_blocked_by_readonly_script')
        body = json.dumps({'query': query, 'variables': variables}).encode()
        req = urllib.request.Request(self.url, data=body, method='POST')
        req.add_header('Content-Type', 'application/json')
        req.add_header('X-Shopify-Access-Token', self.token)
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.loads(r.read().decode())
        if data.get('errors'):
            raise RuntimeError('shopify_graphql_error_' + json.dumps(data['errors'])[:300])
        return data['data']

    def search_variant(self, sku: str) -> list[dict[str, Any]]:
        q = '''query VariantBySku($query: String!) {
          productVariants(first: 10, query: $query) {
            nodes {
              id
              sku
              title
              selectedOptions { name value }
              product {
                id
                title
                handle
                status
                vendor
                productType
                onlineStoreUrl
                seo { title description }
                variants(first: 20) { nodes { id sku title availableForSale } }
              }
            }
          }
        }'''
        queries = [f'sku:"{sku}"', f'sku:{sku}']
        if '-' in sku:
            queries.append(f'sku:{sku.rsplit("-", 1)[0]}*')
        out: list[dict[str, Any]] = []
        seen: set[str] = set()
        for query in queries:
            data = self.gql(q, {'query': query})
            for node in data.get('productVariants', {}).get('nodes') or []:
                key = node.get('id') or node.get('sku') or json.dumps(node, sort_keys=True)
                if key not in seen:
                    seen.add(key)
                    out.append(node)
            if out:
                break
        return out


def safe_get_url(url: str) -> dict[str, Any]:
    if not url:
        return {'url': url, 'checked': False, 'error': 'empty_url'}
    ctx = ssl.create_default_context()
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; HermesBot/1.0; +read-only SEO audit)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    }
    result: dict[str, Any] = {'url': url, 'checked': True}
    try:
        req = urllib.request.Request(url, method='GET', headers=headers)
        with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
            raw = r.read(180000)
            text = raw.decode('utf-8', errors='ignore')
            result.update({
                'http_status': r.status,
                'final_url': r.geturl(),
                'content_type': r.headers.get('Content-Type'),
                'bytes_sampled': len(raw),
                'title': (re.search(r'<title[^>]*>(.*?)</title>', text, flags=re.I | re.S).group(1).strip() if re.search(r'<title[^>]*>(.*?)</title>', text, flags=re.I | re.S) else None),
                'has_add_to_cart_text': bool(re.search(r'adicionar|comprar|add to cart|adicionar ao carrinho', text, flags=re.I)),
                'has_unavailable_text': bool(re.search(r'esgotado|indispon[ií]vel|sold out|unavailable', text, flags=re.I)),
                'robots_noindex': bool(re.search(r'<meta[^>]+name=["\']robots["\'][^>]+noindex', text, flags=re.I)),
            })
    except urllib.error.HTTPError as e:
        result.update({'http_status': e.code, 'error': 'http_error', 'detail': str(e)[:180]})
    except Exception as e:
        result.update({'error': type(e).__name__, 'detail': str(e)[:180]})
    return result


def p0_rows() -> list[dict[str, Any]]:
    merchant = load_json(MERCHANT)
    out = []
    for row in merchant.get('queue') or []:
        codes = set(row.get('item_issue_codes') or [])
        if {'checkout_url_invalid', 'landing_page_error'} & codes:
            sku = (row.get('product_id') or '').split(':')[-1]
            out.append({
                'sku_or_offer_id': sku,
                'product_id': row.get('product_id'),
                'merchant_link': row.get('link') or '',
                'issue_codes': sorted(codes),
                'issue_details': row.get('item_issue_details') or [],
                'disapproved_destinations': row.get('disapproved_destinations') or [],
            })
    # stable dedupe by SKU
    seen = set(); dedup = []
    for row in out:
        key = row['sku_or_offer_id']
        if key not in seen:
            seen.add(key); dedup.append(row)
    return dedup


def classify(row: dict[str, Any], variants: list[dict[str, Any]], public_check: dict[str, Any]) -> tuple[str, str, str]:
    codes = set(row.get('issue_codes') or [])
    if not variants:
        return ('shopify_variant_not_found_for_offer_id', 'Offer ID/SKU in Merchant could not be matched to a live Shopify variant by read-only SKU query.', 'Review feed offer_id/SKU mapping or archived product source before any Merchant/feed change.')
    products = [v.get('product') or {} for v in variants]
    active = [p for p in products if p.get('status') == 'ACTIVE']
    if not active:
        return ('shopify_product_not_active', 'Shopify variant exists but product is not ACTIVE in Admin query.', 'Decide if product should remain in feed; preview exclusion or status/admin fix only after approval.')
    if public_check.get('http_status') and int(public_check['http_status']) >= 400:
        return ('public_pdp_http_error', 'Shopify variant exists, but public PDP URL returned HTTP error.', 'Verify handle/domain/theme routing and preview URL/feed correction before approval.')
    if public_check.get('error') and public_check.get('error') != 'empty_url':
        return ('public_pdp_fetch_error', 'Public PDP check failed or timed out from Hermes environment.', 'Retry with browser/GMC sample and compare with Shopify Admin URL before proposing write.')
    if public_check.get('robots_noindex'):
        return ('public_pdp_noindex', 'Public PDP appears to include robots noindex.', 'Inspect theme/PDP SEO settings; theme/admin changes require plan + approval.')
    if 'checkout_url_invalid' in codes and public_check.get('http_status') == 200:
        return ('pdp_ok_checkout_url_issue_likely_attribute_or_merchant_checkout', 'PDP is reachable; Merchant checkout URL issue likely comes from automatic checkout/merchant account setting or feed attribute context, not a dead PDP.', 'Prioritize Merchant diagnostics and required attributes; no Shopify PDP URL write indicated from this sample.')
    if 'landing_page_error' in codes and public_check.get('http_status') == 200:
        return ('landing_page_now_reachable_recheck_needed', 'PDP is reachable now; issue may be stale crawl/cache, variant URL mismatch, or intermittent landing error.', 'Request Merchant recheck only after other required attributes are prepared; no immediate public URL write.')
    return ('needs_manual_preview_review', 'Read-only checks did not isolate a single safe root cause.', 'Keep in preview and inspect Merchant sample/details before any write.')


def build() -> dict[str, Any]:
    preview = load_json(GMC_PREVIEW)
    rows = p0_rows()
    secrets = load_doppler()
    shop = Shopify(secrets)
    results = []
    for i, row in enumerate(rows, 1):
        sku = row['sku_or_offer_id']
        try:
            variants = shop.search_variant(sku)
        except Exception as e:
            variants = [{'lookup_error': str(e)[:220]}]
        clean_variants = [v for v in variants if not v.get('lookup_error')]
        chosen_product = (clean_variants[0].get('product') if clean_variants else {}) or {}
        admin_url = chosen_product.get('onlineStoreUrl') or ''
        constructed_url = f"{PUBLIC_HOST}/products/{chosen_product.get('handle')}" if chosen_product.get('handle') else ''
        url_to_check = row.get('merchant_link') or admin_url or constructed_url
        public_check = safe_get_url(url_to_check)
        if i % 10 == 0:
            time.sleep(0.5)
        classification, evidence, next_action = classify(row, clean_variants, public_check)
        results.append({
            **row,
            'shopify_variant_match_count': len(clean_variants),
            'shopify_matches': [{
                'variant_id': v.get('id'),
                'variant_sku': v.get('sku'),
                'variant_title': v.get('title'),
                'product_id': (v.get('product') or {}).get('id'),
                'product_title': (v.get('product') or {}).get('title'),
                'handle': (v.get('product') or {}).get('handle'),
                'status': (v.get('product') or {}).get('status'),
                'vendor': (v.get('product') or {}).get('vendor'),
                'product_type': (v.get('product') or {}).get('productType'),
                'online_store_url': (v.get('product') or {}).get('onlineStoreUrl'),
            } for v in clean_variants[:5]],
            'url_checked': url_to_check,
            'public_check': public_check,
            'root_cause_classification': classification,
            'evidence_summary': evidence,
            'safe_next_action': next_action,
            'write_allowed_now': False,
            'approval_required_for_write': 'Merchant/feed/Shopify/checkout/theme/admin changes require Lucas approval with rollback plan.',
        })
    class_counts = Counter(r['root_cause_classification'] for r in results)
    http_counts = Counter(str((r.get('public_check') or {}).get('http_status') or (r.get('public_check') or {}).get('error') or 'unchecked') for r in results)
    summary = {
        'source_p0_package_items': next((p.get('affected_item_count') for p in (preview.get('packages') or []) if p.get('package') == 'P0_admin_url_checkout_landing_review'), None),
        'p0_rows_reviewed': len(results),
        'shopify_matched_rows': sum(1 for r in results if r['shopify_variant_match_count'] > 0),
        'public_url_http_200_rows': sum(1 for r in results if (r.get('public_check') or {}).get('http_status') == 200),
        'public_url_error_rows': sum(1 for r in results if (r.get('public_check') or {}).get('http_status') not in (200, None) or (r.get('public_check') or {}).get('error') not in (None, 'empty_url')),
        'classification_counts': dict(class_counts),
        'http_counts': dict(http_counts),
        'write_allowed_now': 0,
        'production_writes': 0,
        'external_sends_or_contacts': 0,
        'purchases_or_pos': 0,
        'external_marketplace_calls': 0,
        'n8n_flows_created': 0,
    }
    checks = [
        {'name': 'p0_rows_loaded', 'ok': len(results) > 0, 'detail': 'P0 checkout/landing rows loaded from Merchant read-only router.'},
        {'name': 'read_only_guardrails', 'ok': all(summary[k] == 0 for k in ['write_allowed_now','production_writes','external_sends_or_contacts','purchases_or_pos','external_marketplace_calls','n8n_flows_created']), 'detail': 'No writes/sends/contacts/purchases/marketplace/n8n.'},
        {'name': 'shopify_lookup_coverage', 'ok': summary['shopify_matched_rows'] >= max(1, len(results) // 2), 'detail': 'Most P0 Merchant offer IDs can be mapped to Shopify variants.'},
    ]
    return {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'LK GMC P0 URL/checkout/landing review read-only',
        'status': 'gmc_p0_url_review_ready_readonly' if all(c['ok'] for c in checks) else 'gmc_p0_url_review_needs_attention',
        'summary': summary,
        'results': results,
        'recommended_write_preview_plan': [
            '1. Do not change Merchant/Shopify yet: PDP reachability is a separate finding from Merchant checkout URL validity.',
            '2. For rows with PDP HTTP 200, prioritize Merchant automatic checkout/account diagnostics and missing required attributes before any URL rewrite.',
            '3. For rows with public PDP HTTP error or no Shopify variant match, prepare an exact feed exclusion/offer_id/handle preview with rollback before asking Lucas approval.',
            '4. Only after Lucas approval: apply the smallest write surface, then request Merchant recheck and log before/after issue counts.',
        ],
        'checks': checks,
        'not_performed': NOT_PERFORMED,
    }


def write_outputs(payload: dict[str, Any]) -> None:
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    fields = ['sku_or_offer_id','product_id','root_cause_classification','shopify_variant_match_count','url_checked','http_status','final_url','evidence_summary','safe_next_action','write_allowed_now']
    with OUT_CSV.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
        w.writeheader()
        for r in payload['results']:
            pc = r.get('public_check') or {}
            w.writerow({
                'sku_or_offer_id': r.get('sku_or_offer_id'),
                'product_id': r.get('product_id'),
                'root_cause_classification': r.get('root_cause_classification'),
                'shopify_variant_match_count': r.get('shopify_variant_match_count'),
                'url_checked': r.get('url_checked'),
                'http_status': pc.get('http_status') or pc.get('error'),
                'final_url': pc.get('final_url'),
                'evidence_summary': r.get('evidence_summary'),
                'safe_next_action': r.get('safe_next_action'),
                'write_allowed_now': r.get('write_allowed_now'),
            })
    s = payload['summary']
    lines = [
        '# LK GMC P0 URL/Checkout/Landing Review, 2026-05-12', '',
        f"Generated at: `{payload['generated_at']}`", '',
        '## Veredito', '',
        f"Status: `{payload['status']}`", '',
        'Pacote P0 aberto em evidências SKU/URL read-only. Não altera Merchant, Shopify, feed, checkout, PDP, tema, GSC, campanha ou n8n.', '',
        '## Resumo', '',
        f"- Itens P0 na origem: {s['source_p0_package_items']}",
        f"- Linhas P0 revisadas: {s['p0_rows_reviewed']}",
        f"- Linhas com match Shopify por SKU/offer_id: {s['shopify_matched_rows']}",
        f"- URLs públicas com HTTP 200: {s['public_url_http_200_rows']}",
        f"- URLs públicas com erro: {s['public_url_error_rows']}",
        f"- Writes/envios/contatos/compras/marketplace/n8n: {s['production_writes']}/{s['external_sends_or_contacts']}/{s['purchases_or_pos']}/{s['external_marketplace_calls']}/{s['n8n_flows_created']}", '',
        '## Classificações', '',
    ]
    for k, v in sorted(s['classification_counts'].items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f'- `{k}`: {v}')
    lines.extend(['', '## Amostras principais', ''])
    for r in payload['results'][:15]:
        pc = r.get('public_check') or {}
        match = (r.get('shopify_matches') or [{}])[0]
        lines.extend([
            f"### {r['sku_or_offer_id']}",
            f"- Produto Shopify: {match.get('product_title') or 'sem match'}",
            f"- Handle: {match.get('handle') or 'n/a'}",
            f"- URL checada: {r.get('url_checked') or 'n/a'}",
            f"- HTTP: {pc.get('http_status') or pc.get('error') or 'n/a'}",
            f"- Classificação: `{r['root_cause_classification']}`",
            f"- Evidência: {r['evidence_summary']}",
            f"- Próximo seguro: {r['safe_next_action']}",
            '',
        ])
    lines.extend(['## Plano de preview para write futuro', ''])
    for step in payload['recommended_write_preview_plan']:
        lines.append(f'- {step}')
    lines.extend(['', '## Checks', ''])
    for c in payload['checks']:
        lines.append(f"- {'OK' if c['ok'] else 'FAIL'}: `{c['name']}` — {c['detail']}")
    lines.extend(['', '## Não executado', ''])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    text = '\n'.join(lines) + '\n'
    OUT_MD.write_text(text, encoding='utf-8')
    BRAIN_DOC.write_text(text, encoding='utf-8')


def main() -> None:
    payload = build()
    write_outputs(payload)
    print(json.dumps({'ok': payload['status'].endswith('readonly'), 'status': payload['status'], 'summary': payload['summary']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
