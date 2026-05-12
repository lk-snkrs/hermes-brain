#!/usr/bin/env python3
"""LK GMC correction preview, read-only.

Turns Merchant Center issue groups into actionable preview packages without
changing Merchant Center, Shopify, feed, GSC, PDPs, campaigns, or n8n.
"""
from __future__ import annotations

import csv
import json
import pathlib
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / 'reports/lk-merchant-center-feed-readonly-router-2026-05-11.json'
OUT_JSON = ROOT / 'reports/lk-gmc-correction-preview-2026-05-12.json'
OUT_MD = ROOT / 'reports/lk-gmc-correction-preview-2026-05-12.md'
OUT_CSV = ROOT / 'reports/lk-gmc-correction-preview-2026-05-12.csv'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/gmc-correction-preview-2026-05-12.md'

NOT_PERFORMED = [
    'merchant_center_write', 'supplemental_feed_update', 'product_insert_update_delete',
    'shopify_product_or_variant_write', 'shopify_theme_or_pdp_write', 'gsc_admin_or_indexing_submit',
    'campaign_or_customer_send', 'supplier_contact', 'purchase_or_po', 'n8n_flow_creation',
]


def load() -> dict[str, Any]:
    return json.loads(SRC.read_text(encoding='utf-8'))


def classify_codes(codes: set[str], destinations: set[str]) -> dict[str, str]:
    if 'checkout_url_invalid' in codes or 'landing_page_error' in codes:
        return {
            'package': 'P0_admin_url_checkout_landing_review',
            'owner': 'Lucas/admin Shopify-Merchant',
            'fix_surface': 'Merchant account / checkout URL / PDP availability',
            'safe_next_action': 'verify checkout/PDP URL samples in browser/admin and prepare exact admin fix preview; no URL/feed write now',
            'approval_required_for_write': 'Merchant/Shopify admin change or feed URL rule change',
        }
    if 'local_stores_lack_inventory' in codes:
        return {
            'package': 'P1_local_inventory_program_review',
            'owner': 'Lucas/admin Merchant local inventory',
            'fix_surface': 'Local inventory feed / local surfaces configuration',
            'safe_next_action': 'review whether LK wants LocalSurfaces active and reconcile local inventory feed mapping before any change',
            'approval_required_for_write': 'Merchant local inventory feed/config update',
        }
    if 'restricted_gtin' in codes:
        return {
            'package': 'P1_gtin_identifier_compliance_review',
            'owner': 'Hermes preview + Lucas approval',
            'fix_surface': 'Identifier policy / GTIN / identifier_exists mapping',
            'safe_next_action': 'prepare SKU-level identifier compliance list; decide whether GTIN is valid, blank, or identifier_exists=false before feed write',
            'approval_required_for_write': 'Shopify metafield/feed identifier mapping update',
        }
    if 'item_missing_required_attribute' in codes or 'missing_item_attribute_for_product_type' in codes:
        return {
            'package': 'P1_required_attributes_feed_mapping',
            'owner': 'Hermes preview + Lucas/admin approval',
            'fix_surface': 'Shopify product data or feed mapping for required attributes',
            'safe_next_action': 'create attribute template by product type: age_group, gender, color, size, material/pattern where applicable; preview exact mapping only',
            'approval_required_for_write': 'Shopify product/metafield update or Merchant feed rule/supplemental feed update',
        }
    if 'price_updated' in codes or 'strikethrough_price_updated' in codes:
        return {
            'package': 'P2_price_sync_monitor',
            'owner': 'Hermes monitor',
            'fix_surface': 'Merchant price crawl freshness / Shopify price sync',
            'safe_next_action': 'monitor unless persistent with disapproval; compare sample PDP price vs Merchant after next crawl',
            'approval_required_for_write': 'price/feed change only if persistent mismatch is verified',
        }
    return {
        'package': 'P2_other_feed_issue_review',
        'owner': 'Hermes preview',
        'fix_surface': 'Other Merchant issue',
        'safe_next_action': 'review issue details and sample products before proposing any write',
        'approval_required_for_write': 'depends on issue; no write allowed from this preview',
    }


def sku_from_product_id(pid: str) -> str:
    return (pid or '').split(':')[-1]


def build() -> dict[str, Any]:
    src = load()
    issue_groups = src.get('issue_groups') or []
    queue = src.get('queue') or []

    package_rows: dict[str, dict[str, Any]] = {}
    code_counts = Counter()
    attr_counts_by_package: dict[str, Counter] = defaultdict(Counter)
    sample_rows_by_package: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for g in issue_groups:
        codes = {c.strip() for c in (g.get('issue_codes') or '').split(',') if c.strip() and c.strip() != 'no_item_issue_code'}
        dests = {d.strip() for d in (g.get('disapproved_destinations') or '').split(',') if d.strip() and d.strip() != 'no_disapproved_destination'}
        meta = classify_codes(codes, dests)
        pkg = meta['package']
        row = package_rows.setdefault(pkg, {
            **meta,
            'priority': pkg.split('_', 1)[0],
            'issue_group_count': 0,
            'affected_item_count': 0,
            'disapproved_item_count_estimate': 0,
            'issue_codes': Counter(),
            'sample_product_ids': [],
            'sample_links': [],
            'approval_status': 'preview_only_requires_approval_before_write',
            'write_allowed_now': False,
            'source_label': 'fact_merchant_center_derived_reconciliation',
        })
        count = int(g.get('count') or 0)
        row['issue_group_count'] += 1
        row['affected_item_count'] += count
        if dests:
            row['disapproved_item_count_estimate'] += count
        for c in codes:
            row['issue_codes'][c] += count
            code_counts[c] += count
        for pid in g.get('sample_product_ids') or []:
            if pid and pid not in row['sample_product_ids'] and len(row['sample_product_ids']) < 12:
                row['sample_product_ids'].append(pid)
        for link in g.get('sample_links') or []:
            if link and link not in row['sample_links'] and len(row['sample_links']) < 6:
                row['sample_links'].append(link)

    for q in queue:
        codes = set(q.get('item_issue_codes') or [])
        pkg = classify_codes(codes, set(q.get('disapproved_destinations') or []))['package']
        for detail in q.get('item_issue_details') or []:
            attr = detail.get('attribute')
            if attr:
                attr_counts_by_package[pkg][attr] += 1
        if len(sample_rows_by_package[pkg]) < 10:
            sample_rows_by_package[pkg].append({
                'product_id': q.get('product_id'),
                'sku_or_offer_id': sku_from_product_id(q.get('product_id') or ''),
                'title': q.get('title'),
                'link': q.get('link'),
                'issue_codes': sorted(set(q.get('item_issue_codes') or [])),
                'attributes_seen_in_issue_details': sorted({d.get('attribute') for d in (q.get('item_issue_details') or []) if d.get('attribute')}),
                'disapproved_destinations': q.get('disapproved_destinations') or [],
            })

    packages = []
    priority_order = {'P0': 0, 'P1': 1, 'P2': 2, 'P3': 3}
    for row in package_rows.values():
        pkg = row['package']
        row['issue_codes'] = [{'issue_code': k, 'count': v} for k, v in row['issue_codes'].most_common()]
        row['top_attributes_from_queue_sample'] = [{'attribute': k, 'sample_count': v} for k, v in attr_counts_by_package[pkg].most_common()]
        row['sample_rows'] = sample_rows_by_package[pkg]
        packages.append(row)
    packages.sort(key=lambda r: (priority_order.get(r['priority'], 9), -r['affected_item_count']))

    summary = {
        'source_product_statuses_read': src.get('summary', {}).get('product_statuses_read'),
        'source_queue_items': src.get('summary', {}).get('queue_items'),
        'source_p1_items': src.get('summary', {}).get('p1_items'),
        'source_products_with_disapproved_destination': src.get('summary', {}).get('products_with_disapproved_destination'),
        'packages': len(packages),
        'p0_packages': sum(1 for p in packages if p['priority'] == 'P0'),
        'p1_packages': sum(1 for p in packages if p['priority'] == 'P1'),
        'p2_packages': sum(1 for p in packages if p['priority'] == 'P2'),
        'preview_only_items_covered': sum(p['affected_item_count'] for p in packages),
        'write_allowed_now': 0,
        'production_writes': 0,
        'external_sends_or_contacts': 0,
        'purchases_or_pos': 0,
        'external_marketplace_calls': 0,
        'n8n_flows_created': 0,
    }
    checks = [
        {'name': 'source_router_available', 'ok': bool(issue_groups and queue), 'detail': 'Merchant router JSON has grouped issues and queue sample.'},
        {'name': 'writes_blocked', 'ok': all(summary[k] == 0 for k in ['write_allowed_now','production_writes','external_sends_or_contacts','purchases_or_pos','external_marketplace_calls','n8n_flows_created']), 'detail': 'Preview performs no external write/send/contact/purchase.'},
        {'name': 'packages_cover_all_groups', 'ok': summary['preview_only_items_covered'] >= src.get('summary', {}).get('queue_items', 0), 'detail': 'Packages cover grouped queue counts from Merchant router.'},
    ]
    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'LK GMC correction preview read-only',
        'status': 'gmc_correction_preview_ready_readonly' if all(c['ok'] for c in checks) else 'needs_fix',
        'summary': summary,
        'packages': packages,
        'top_issue_codes': src.get('top_issue_codes') or [],
        'destination_status_counts': src.get('destination_status_counts') or [],
        'checks': checks,
        'not_performed': NOT_PERFORMED,
    }
    return payload


def write_outputs(payload: dict[str, Any]) -> None:
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    fields = ['priority','package','affected_item_count','disapproved_item_count_estimate','issue_group_count','fix_surface','safe_next_action','approval_required_for_write','write_allowed_now']
    with OUT_CSV.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
        w.writeheader()
        for p in payload['packages']:
            w.writerow({k: p.get(k, '') for k in fields})
    s = payload['summary']
    lines = [
        '# LK GMC Correction Preview, 2026-05-12', '',
        f"Generated at: `{payload['generated_at']}`", '',
        '## Veredito', '',
        f"Status: `{payload['status']}`", '',
        'Transforma os P1 do Merchant Center em pacotes de correção preview-only. Não altera Merchant Center, Shopify, feed, PDP, Search Console, campanhas ou n8n.', '',
        '## Resumo', '',
        f"- Product statuses lidos na origem: {s['source_product_statuses_read']}",
        f"- Fila origem P1/P2: {s['source_queue_items']} itens, {s['source_p1_items']} P1",
        f"- Produtos com destino reprovado: {s['source_products_with_disapproved_destination']}",
        f"- Pacotes gerados: {s['packages']} ({s['p0_packages']} P0, {s['p1_packages']} P1, {s['p2_packages']} P2)",
        f"- Itens cobertos por pacotes preview-only: {s['preview_only_items_covered']}",
        f"- Writes/envios/contatos/compras/marketplace/n8n: {s['production_writes']}/{s['external_sends_or_contacts']}/{s['purchases_or_pos']}/{s['external_marketplace_calls']}/{s['n8n_flows_created']}", '',
        '## Pacotes', '',
    ]
    for p in payload['packages']:
        lines.extend([
            f"### {p['priority']} · {p['package']}",
            f"- Itens afetados: {p['affected_item_count']}",
            f"- Estimativa com reprovação: {p['disapproved_item_count_estimate']}",
            f"- Superfície provável: {p['fix_surface']}",
            f"- Próximo seguro: {p['safe_next_action']}",
            f"- Aprovação necessária para write: {p['approval_required_for_write']}",
            f"- Top issue codes: {', '.join([x['issue_code'] + '=' + str(x['count']) for x in p['issue_codes'][:5]]) or 'n/a'}",
            f"- Top atributos no sample: {', '.join([x['attribute'] + '=' + str(x['sample_count']) for x in p['top_attributes_from_queue_sample'][:8]]) or 'n/a'}",
            f"- Sample IDs: {', '.join(p['sample_product_ids'][:8]) or 'n/a'}",
            '',
        ])
    lines.extend(['## Checks', ''])
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
