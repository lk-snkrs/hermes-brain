#!/usr/bin/env python3
"""LK GMC required attributes correction preview, read-only.

Builds a local supplemental-feed-style preview for Merchant Center required
attributes (age_group, gender, size, color when detected). It queries Shopify
Admin GraphQL with query operations only. It does not write to Merchant Center,
Shopify, feed files, GSC, checkout, theme, campaigns, suppliers, customers, or
n8n.
"""
from __future__ import annotations

import base64
import csv
import json
import os
import pathlib
import re
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
MERCHANT = ROOT / 'reports/lk-merchant-center-feed-readonly-router-2026-05-11.json'
OUT_JSON = ROOT / 'reports/lk-gmc-required-attrs-preview-2026-05-12.json'
OUT_MD = ROOT / 'reports/lk-gmc-required-attrs-preview-2026-05-12.md'
OUT_CSV = ROOT / 'reports/lk-gmc-required-attrs-preview-2026-05-12.csv'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/gmc-required-attrs-preview-2026-05-12.md'

REQUIRED_ATTR_CODES = {'item_missing_required_attribute', 'missing_item_attribute_for_product_type'}
NOT_PERFORMED = [
    'merchant_center_write', 'supplemental_feed_upload', 'shopify_product_or_variant_write',
    'shopify_metafield_write', 'feed_file_replacement', 'gsc_admin_or_indexing_submit',
    'checkout_setting_change', 'theme_or_pdp_write', 'campaign_or_customer_send',
    'supplier_contact', 'purchase_or_po', 'external_marketplace_call', 'n8n_flow_creation',
]


def load_json(path: pathlib.Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding='utf-8'))


def load_doppler() -> dict[str, str]:
    token = os.environ.get('DOPPLER_TOKEN') or DOPPLER_TOKEN_FILE.read_text().strip()
    req = urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
    req.add_header('Authorization', 'Basic ' + base64.b64encode((token + ':').encode()).decode())
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read().decode())


def shopify_host(raw: str) -> str:
    return (raw or '').strip().removeprefix('https://').removeprefix('http://').rstrip('/')


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

    def variant_by_sku(self, sku: str) -> list[dict[str, Any]]:
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
                tags
                onlineStoreUrl
                seo { title description }
              }
            }
          }
        }'''
        queries = [f'sku:"{sku}"', f'sku:{sku}']
        if '-' in sku:
            queries.append(f'sku:{sku.rsplit("-", 1)[0]}*')
        seen = set(); out = []
        for query in queries:
            data = self.gql(q, {'query': query})
            for node in data.get('productVariants', {}).get('nodes') or []:
                key = node.get('id') or node.get('sku') or json.dumps(node, sort_keys=True)
                if key not in seen:
                    seen.add(key); out.append(node)
            if out:
                break
        return out


def merchant_required_rows() -> list[dict[str, Any]]:
    merchant = load_json(MERCHANT)
    rows = []
    for row in merchant.get('queue') or []:
        details = row.get('item_issue_details') or []
        attrs = sorted({(d.get('attribute') or '').strip().lower() for d in details if d.get('code') in REQUIRED_ATTR_CODES and d.get('attribute')})
        codes = set(row.get('item_issue_codes') or [])
        if attrs or REQUIRED_ATTR_CODES & codes:
            sku = (row.get('product_id') or '').split(':')[-1]
            rows.append({
                'offer_id': sku,
                'product_id': row.get('product_id'),
                'missing_attributes': attrs,
                'issue_codes': sorted(codes),
                'disapproved_destinations': row.get('disapproved_destinations') or [],
                'item_issue_count': row.get('item_issue_count'),
            })
    # stable de-dupe by offer_id
    seen = set(); out = []
    for r in rows:
        if r['offer_id'] not in seen:
            seen.add(r['offer_id']); out.append(r)
    return out


def norm_text(*parts: Any) -> str:
    return ' '.join(str(p or '') for p in parts).lower()


def infer_age_group(text: str) -> tuple[str, str]:
    if re.search(r'\b(kids|kid|junior|infantil|crian[cç]a|gs\b|ps\b|td\b|baby|toddler)\b', text):
        return 'kids', 'medium_keyword_kids'
    if re.search(r'\b(adulto|adult|men|women|masculino|feminino|wmns|unissex|unisex)\b', text):
        return 'adult', 'high_keyword_adult'
    return 'adult', 'medium_lk_default_adult_assortment'


def infer_gender(text: str) -> tuple[str, str]:
    if re.search(r'\b(wmns|women|womens|female|feminino|mulher)\b', text):
        return 'female', 'medium_keyword_female'
    if re.search(r'\b(men|mens|male|masculino|homem)\b', text):
        return 'male', 'medium_keyword_male'
    if re.search(r'\b(unisex|unissex)\b', text):
        return 'unisex', 'high_keyword_unisex'
    # LK sneakers/apparel are commonly sold without gender split; safer than inventing male/female.
    return 'unisex', 'medium_lk_default_unisex_needs_review'


def infer_size(offer_id: str, variant: dict[str, Any]) -> tuple[str, str]:
    opts = variant.get('selectedOptions') or []
    for opt in opts:
        if (opt.get('name') or '').lower() in {'size', 'tamanho'} and opt.get('value'):
            return str(opt['value']).strip(), 'high_shopify_selected_option'
    vt = str(variant.get('title') or '').strip()
    if vt and vt.lower() != 'default title':
        m = re.search(r'(\d{2}(?:\.5)?|[XSML]{1,3}(?:/[A-Z])?|OS|U)$', vt, flags=re.I)
        if m:
            return m.group(1).upper(), 'medium_variant_title_suffix'
    m = re.search(r'-(\d{1,2}(?:\.5)?|[XSML]{1,3}|OS|U)$', offer_id, flags=re.I)
    if m:
        return m.group(1).upper(), 'medium_offer_id_suffix'
    return '', 'low_no_size_detected'


def infer_color(text: str) -> tuple[str, str]:
    colors = [
        ('preto', 'black'), ('black', 'black'), ('branco', 'white'), ('white', 'white'),
        ('azul', 'blue'), ('blue', 'blue'), ('vermelho', 'red'), ('red', 'red'),
        ('verde', 'green'), ('green', 'green'), ('cinza', 'gray'), ('grey', 'gray'), ('gray', 'gray'),
        ('bege', 'beige'), ('cream', 'beige'), ('marrom', 'brown'), ('brown', 'brown'),
        ('rosa', 'pink'), ('pink', 'pink'), ('amarelo', 'yellow'), ('yellow', 'yellow'),
        ('roxo', 'purple'), ('purple', 'purple'), ('laranja', 'orange'), ('orange', 'orange'),
        ('prata', 'silver'), ('silver', 'silver'), ('dourado', 'gold'), ('gold', 'gold'),
    ]
    found = []
    for token, value in colors:
        if re.search(rf'\b{re.escape(token)}\b', text):
            found.append(value)
    if found:
        return '/'.join(dict.fromkeys(found)), 'medium_keyword_color'
    return '', 'low_no_color_detected'


def confidence(*signals: str) -> str:
    if any(s.startswith('low_') for s in signals):
        return 'low'
    if all(s.startswith('high_') for s in signals if s):
        return 'high'
    return 'medium'


def build() -> dict[str, Any]:
    rows = merchant_required_rows()
    shop = Shopify(load_doppler())
    results = []
    for r in rows:
        try:
            variants = shop.variant_by_sku(r['offer_id'])
            lookup_error = None
        except Exception as e:
            variants = []
            lookup_error = str(e)[:220]
        variant = variants[0] if variants else {}
        product = (variant.get('product') or {}) if variant else {}
        text = norm_text(product.get('title'), product.get('productType'), product.get('vendor'), product.get('tags'), variant.get('title'), r['offer_id'])
        age, age_sig = infer_age_group(text)
        gender, gender_sig = infer_gender(text)
        size, size_sig = infer_size(r['offer_id'], variant)
        color, color_sig = infer_color(text)
        missing = set(r['missing_attributes'])
        suggestions = {}
        sigs = []
        if not missing or 'age group' in missing:
            suggestions['age_group'] = age; sigs.append(age_sig)
        if not missing or 'gender' in missing:
            suggestions['gender'] = gender; sigs.append(gender_sig)
        if not missing or 'size' in missing:
            suggestions['size'] = size; sigs.append(size_sig)
        if 'color' in missing:
            suggestions['color'] = color; sigs.append(color_sig)
        conf = confidence(*sigs) if variants else 'low'
        surface = 'supplemental_feed_preview_preferred' if conf in {'high', 'medium'} else 'manual_review_before_write'
        if not size and 'size' in suggestions:
            surface = 'manual_review_before_write'
        results.append({
            **r,
            'shopify_variant_match_count': len(variants),
            'lookup_error': lookup_error,
            'product_title': product.get('title'),
            'product_handle': product.get('handle'),
            'product_status': product.get('status'),
            'vendor': product.get('vendor'),
            'product_type': product.get('productType'),
            'variant_sku': variant.get('sku'),
            'variant_title': variant.get('title'),
            'selected_options': variant.get('selectedOptions') or [],
            'suggested_attributes': suggestions,
            'evidence_signals': {'age_group': age_sig, 'gender': gender_sig, 'size': size_sig, 'color': color_sig if 'color' in missing else 'not_requested'},
            'confidence': conf,
            'recommended_surface': surface,
            'write_allowed_now': False,
            'approval_required_for_write': 'Lucas approval required before Merchant supplemental feed, Shopify metafield/product, feed rule, or account setting changes.',
        })
    summary = {
        'required_attr_rows_reviewed': len(results),
        'shopify_matched_rows': sum(1 for r in results if r['shopify_variant_match_count'] > 0),
        'supplemental_feed_preview_rows': sum(1 for r in results if r['recommended_surface'] == 'supplemental_feed_preview_preferred'),
        'manual_review_rows': sum(1 for r in results if r['recommended_surface'] == 'manual_review_before_write'),
        'confidence_counts': dict(Counter(r['confidence'] for r in results)),
        'missing_attribute_counts': dict(Counter(a for r in results for a in r['missing_attributes'])),
        'suggested_age_group_counts': dict(Counter((r['suggested_attributes'].get('age_group') or 'n/a') for r in results)),
        'suggested_gender_counts': dict(Counter((r['suggested_attributes'].get('gender') or 'n/a') for r in results)),
        'write_allowed_now': 0,
        'production_writes': 0,
        'external_sends_or_contacts': 0,
        'purchases_or_pos': 0,
        'external_marketplace_calls': 0,
        'n8n_flows_created': 0,
    }
    checks = [
        {'name': 'required_attr_rows_loaded', 'ok': len(results) > 0, 'detail': 'Merchant required-attribute rows loaded from read-only router.'},
        {'name': 'shopify_lookup_coverage', 'ok': summary['shopify_matched_rows'] >= max(1, len(results) // 2), 'detail': 'Most required-attribute offer IDs mapped to Shopify variants.'},
        {'name': 'read_only_guardrails', 'ok': all(summary[k] == 0 for k in ['write_allowed_now','production_writes','external_sends_or_contacts','purchases_or_pos','external_marketplace_calls','n8n_flows_created']), 'detail': 'No production writes/sends/contacts/purchases/marketplace/n8n.'},
    ]
    return {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'LK GMC required attributes preview read-only',
        'status': 'gmc_required_attrs_preview_ready_readonly' if all(c['ok'] for c in checks) else 'gmc_required_attrs_preview_needs_attention',
        'summary': summary,
        'results': results,
        'recommended_correction_plan': [
            'Use this CSV as a local preview, not as an uploaded supplemental feed.',
            'Prefer a Merchant supplemental feed/feed-rule preview for age_group/gender/size before touching Shopify product/metafields.',
            'For medium-confidence defaults (adult/unisex), Lucas should approve the rule because it applies merchandising assumptions.',
            'Rows without a reliable size or Shopify match must remain manual review before any write.',
            'After approval and write, request Merchant recheck and compare issue counts before/after.',
        ],
        'not_performed': NOT_PERFORMED,
        'checks': checks,
    }


def write_outputs(payload: dict[str, Any]) -> None:
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    fields = ['offer_id','product_id','product_title','product_handle','vendor','product_type','variant_sku','variant_title','missing_attributes','age_group','gender','size','color','confidence','recommended_surface','write_allowed_now']
    with OUT_CSV.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
        w.writeheader()
        for r in payload['results']:
            s = r['suggested_attributes']
            w.writerow({
                'offer_id': r.get('offer_id'), 'product_id': r.get('product_id'), 'product_title': r.get('product_title'),
                'product_handle': r.get('product_handle'), 'vendor': r.get('vendor'), 'product_type': r.get('product_type'),
                'variant_sku': r.get('variant_sku'), 'variant_title': r.get('variant_title'),
                'missing_attributes': ','.join(r.get('missing_attributes') or []),
                'age_group': s.get('age_group',''), 'gender': s.get('gender',''), 'size': s.get('size',''), 'color': s.get('color',''),
                'confidence': r.get('confidence'), 'recommended_surface': r.get('recommended_surface'), 'write_allowed_now': r.get('write_allowed_now'),
            })
    s = payload['summary']
    lines = [
        '# LK GMC Required Attributes Preview, 2026-05-12', '',
        f"Generated at: `{payload['generated_at']}`", '',
        '## Veredito', '',
        f"Status: `{payload['status']}`", '',
        'Preview local para corrigir atributos obrigatórios do Merchant. Não foi enviado para Merchant, não alterou Shopify e não substituiu feed.', '',
        '## Resumo', '',
        f"- Linhas required-attributes revisadas: {s['required_attr_rows_reviewed']}",
        f"- Matches Shopify: {s['shopify_matched_rows']}",
        f"- Linhas prontas para preview de supplemental feed: {s['supplemental_feed_preview_rows']}",
        f"- Linhas para revisão manual antes de write: {s['manual_review_rows']}",
        f"- Confiança: {s['confidence_counts']}",
        f"- Atributos faltantes: {s['missing_attribute_counts']}",
        f"- Sugestão age_group: {s['suggested_age_group_counts']}",
        f"- Sugestão gender: {s['suggested_gender_counts']}",
        f"- Writes/envios/contatos/compras/marketplace/n8n: {s['production_writes']}/{s['external_sends_or_contacts']}/{s['purchases_or_pos']}/{s['external_marketplace_calls']}/{s['n8n_flows_created']}", '',
        '## Amostras', '',
    ]
    for r in payload['results'][:20]:
        sug = r['suggested_attributes']
        lines.extend([
            f"### {r['offer_id']}",
            f"- Produto: {r.get('product_title') or 'sem match'}",
            f"- Variant: {r.get('variant_title') or 'n/a'} / `{r.get('variant_sku') or 'n/a'}`",
            f"- Missing: {', '.join(r.get('missing_attributes') or []) or 'n/a'}",
            f"- Sugestão: age_group=`{sug.get('age_group','')}`, gender=`{sug.get('gender','')}`, size=`{sug.get('size','')}`, color=`{sug.get('color','')}`",
            f"- Confiança: {r['confidence']} / superfície: {r['recommended_surface']}", '',
        ])
    lines.extend(['## Plano recomendado', ''])
    for step in payload['recommended_correction_plan']:
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
    if not payload['status'].endswith('readonly'):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
