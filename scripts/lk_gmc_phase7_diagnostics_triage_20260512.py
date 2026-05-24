#!/usr/bin/env python3
"""LK GMC Phase 7 diagnostics triage, read-only.

Deepens the post-cleanup monitor into action buckets. It reads Merchant products
and productstatuses only, emits sanitized reports, and does not write to Merchant,
Shopify, Tiny, feeds, databases, POS/local settings, or external surfaces.
"""
from __future__ import annotations

import csv
import importlib.util
import json
import pathlib
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / 'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
PHASE7_BASELINE_JSON = ROOT / 'reports/lk-gmc-2026-05-12-phase7-post-cleanup-monitor.json'
RUN_STAMP = '2026-05-12-phase7-diagnostics-triage'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}-buckets.csv'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def import_audit():
    spec = importlib.util.spec_from_file_location('audit', AUDIT_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def load_json(path: pathlib.Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding='utf-8'))


def chan(pid: str) -> str:
    return (pid or '').split(':', 1)[0] if ':' in (pid or '') else 'unknown'


def issue_code(issue: dict[str, Any]) -> str:
    return str(issue.get('code') or issue.get('servability') or issue.get('attributeName') or 'unknown_issue')


def classify_issue(code: str, issue: dict[str, Any], channel: str) -> dict[str, str]:
    detail = (issue.get('detail') or '').lower()
    attr = str(issue.get('attributeName') or '')
    if code in {'item_missing_required_attribute', 'missing_item_attribute_for_product_type'}:
        return {
            'action_bucket': 'attribute_completion_preview',
            'risk': 'A2_write_required_if_applied',
            'safe_next': 'Build exact-ID supplemental/product attribute preview; no write until approval.',
            'owner_surface': 'Merchant feed/product attributes',
        }
    if code == 'checkout_url_invalid':
        return {
            'action_bucket': 'checkout_url_readonly_probe',
            'risk': 'A1_readonly_probe_then_A2_if_feed_fix_needed',
            'safe_next': 'Probe URLs with HEAD/GET read-only and classify redirect/404/variant issues before any feed/product write.',
            'owner_surface': 'Shopify URL / Merchant link attribute',
        }
    if code in {'price_updated', 'strikethrough_price_updated', 'condition_updated_from_detected'}:
        return {
            'action_bucket': 'merchant_auto_update_monitor',
            'risk': 'A0_no_action_default',
            'safe_next': 'Monitor only unless persistent disapproval appears; these are often Merchant normalization/update notices.',
            'owner_surface': 'Merchant automatic update/diagnostics',
        }
    if 'gtin' in code or attr.lower() == 'gtin':
        return {
            'action_bucket': 'gtin_policy_review',
            'risk': 'A1_readonly_then_manual_catalog_decision',
            'safe_next': 'Group by GTIN/product and inspect whether GTIN should be removed/replaced; no automatic GTIN edits.',
            'owner_surface': 'GTIN/catalog data quality',
        }
    if 'policy' in code or 'violation' in code or 'restricted' in code or 'sexual' in detail:
        return {
            'action_bucket': 'policy_manual_review',
            'risk': 'A3_sensitive_policy_review',
            'safe_next': 'Manual review samples before any product/feed/content change.',
            'owner_surface': 'Merchant policy/catalog content',
        }
    if code.startswith('image_'):
        return {
            'action_bucket': 'image_asset_review',
            'risk': 'A1_readonly_then_A2_asset_fix_if_needed',
            'safe_next': 'Read-only image URL probe and image dimension/background classification.',
            'owner_surface': 'Shopify/product image assets',
        }
    return {
        'action_bucket': 'misc_manual_review',
        'risk': 'A1_readonly',
        'safe_next': 'Sample and classify before proposing writes.',
        'owner_surface': 'unknown',
    }


def product_snapshot(prod: dict[str, Any]) -> dict[str, Any]:
    return {
        'id': prod.get('id'),
        'offerId': prod.get('offerId'),
        'channel': prod.get('channel'),
        'title': prod.get('title'),
        'link_present': bool(prod.get('link')),
        'imageLink_present': bool(prod.get('imageLink')),
        'price_present': bool(prod.get('price')),
        'salePrice_present': bool(prod.get('salePrice')),
        'gtin_present': bool(prod.get('gtin')),
        'brand': prod.get('brand'),
        'productTypes': prod.get('productTypes')[:3] if isinstance(prod.get('productTypes'), list) else prod.get('productTypes'),
        'googleProductCategory': prod.get('googleProductCategory'),
        'ageGroup': prod.get('ageGroup'),
        'gender': prod.get('gender'),
        'size': prod.get('sizes'),
        'color': prod.get('color'),
    }


def main() -> None:
    audit = import_audit()
    secrets = audit.load_doppler()
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    if not merchant_id:
        raise RuntimeError('missing_merchant_center_id')
    token = audit.google_access_token(audit.parse_service_account(secrets))
    products = audit.list_all('products', merchant_id, token)
    statuses = audit.list_all('productstatuses', merchant_id, token)
    product_by_id = {p.get('id'): p for p in products}
    baseline = load_json(PHASE7_BASELINE_JSON)
    baseline_summary = baseline.get('summary') or {}

    bucket_counts = Counter()
    issue_counts = Counter()
    bucket_issue_counts: dict[str, Counter] = defaultdict(Counter)
    bucket_channel_counts: dict[str, Counter] = defaultdict(Counter)
    affected_products_by_bucket: dict[str, set[str]] = defaultdict(set)
    samples: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for st in statuses:
        pid = st.get('productId') or ''
        ch = chan(pid)
        for issue in st.get('itemLevelIssues') or []:
            code = issue_code(issue)
            cls = classify_issue(code, issue, ch)
            bucket = cls['action_bucket']
            bucket_counts[bucket] += 1
            issue_counts[code] += 1
            bucket_issue_counts[bucket][code] += 1
            bucket_channel_counts[bucket][ch] += 1
            affected_products_by_bucket[bucket].add(pid)
            if len(samples[bucket]) < 12:
                prod = product_by_id.get(pid) or {}
                samples[bucket].append({
                    'product_id': pid,
                    'channel': ch,
                    'title': st.get('title') or prod.get('title'),
                    'issue_code': code,
                    'severity': issue.get('severity'),
                    'resolution': issue.get('resolution'),
                    'destination': issue.get('destination'),
                    'detail': str(issue.get('detail') or '')[:260],
                    'classification': cls,
                    'product_snapshot': product_snapshot(prod),
                })

    bucket_rows = []
    bucket_meta = {
        'attribute_completion_preview': ('P1', 'Build no-write exact-ID attribute completion packet from current diagnostics.'),
        'checkout_url_readonly_probe': ('P1', 'Probe affected URLs read-only; likely next approval packet if deterministic.'),
        'gtin_policy_review': ('P2', 'Manual catalog/policy review before edit; GTIN changes can be risky.'),
        'policy_manual_review': ('P2', 'Manual review; avoid automated content edits.'),
        'image_asset_review': ('P2', 'Read-only image probe first.'),
        'merchant_auto_update_monitor': ('P3', 'Monitor; usually not a direct remediation target.'),
        'misc_manual_review': ('P3', 'Sample first.'),
    }
    for bucket, instances in bucket_counts.most_common():
        priority, recommendation = bucket_meta.get(bucket, ('P3', 'Review manually.'))
        bucket_rows.append({
            'priority': priority,
            'bucket': bucket,
            'issue_instances': instances,
            'affected_product_ids': len(affected_products_by_bucket[bucket]),
            'channels': dict(bucket_channel_counts[bucket]),
            'top_issue_codes': [{'issue_code': k, 'count': v} for k, v in bucket_issue_counts[bucket].most_common(10)],
            'recommendation': recommendation,
        })

    current_summary = {
        'merchant_products_current': len(products),
        'merchant_productstatuses_current': len(statuses),
        'rows_with_item_issues': sum(1 for s in statuses if s.get('itemLevelIssues')),
        'item_issue_instances': sum(issue_counts.values()),
        'baseline_item_issue_instances': baseline_summary.get('item_issue_instances'),
        'delta_vs_phase7_baseline_instances': (sum(issue_counts.values()) - baseline_summary.get('item_issue_instances')) if isinstance(baseline_summary.get('item_issue_instances'), int) else None,
        'action_bucket_count': len(bucket_rows),
    }
    payload = {
        'generated_at': utc_now(),
        'status': 'gmc_phase7_diagnostics_triage_readonly_ready',
        'scope': 'Read-only action-bucket triage of current Merchant item diagnostics after GMC cleanup',
        'source_labels': ['fact_merchant_center', 'derived_reconciliation'],
        'summary': current_summary,
        'action_buckets': bucket_rows,
        'issue_counts_top': [{'issue_code': k, 'count': v} for k, v in issue_counts.most_common(30)],
        'samples_by_bucket': dict(samples),
        'interpretation': {
            'verdict': 'O próximo bloco com maior alavanca é P1 attribute_completion_preview, seguido por checkout_url_readonly_probe. Nenhum write foi executado; qualquer aplicação exigirá pacote exato e aprovação.',
            'recommended_next_safe_block': 'Build P1 attribute completion preview from exact current product IDs and issue attributes; output no-write approval packet only.',
        },
        'not_performed': ['merchant_product_delete','merchant_product_insert','merchant_product_update','content_api_custombatch','datafeed_fetchNow','feed_update','shopify_write','tiny_write','database_write','pos_or_local_inventory_setting_change','campaign_or_external_send'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        fields = ['priority','bucket','issue_instances','affected_product_ids','channels','top_issue_codes','recommendation']
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in bucket_rows:
            out = dict(r)
            out['channels'] = json.dumps(out['channels'], ensure_ascii=False)
            out['top_issue_codes'] = json.dumps(out['top_issue_codes'], ensure_ascii=False)
            w.writerow(out)
    lines = [
        '# LK GMC Phase 7 Diagnostics Triage, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Resumo executivo',
        f"- Merchant products/statuses atuais: {len(products)} / {len(statuses)}",
        f"- Linhas com item issues: {current_summary['rows_with_item_issues']}",
        f"- Instâncias de item issues: {current_summary['item_issue_instances']}",
        f"- Delta vs baseline Phase 7: {current_summary['delta_vs_phase7_baseline_instances']}", '',
        '## Buckets de ação',
    ]
    for r in bucket_rows:
        lines.append(f"- {r['priority']} `{r['bucket']}`: {r['issue_instances']} instâncias; produtos afetados={r['affected_product_ids']}; canais={r['channels']}; recomendação={r['recommendation']}")
    lines.extend(['', '## Veredito', f"- {payload['interpretation']['verdict']}", '', '## Próximo bloco seguro', f"- {payload['interpretation']['recommended_next_safe_block']}", '', '## Não executado'])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    lines.extend(['', '## Arquivos', f'- JSON: `{OUT_JSON}`', f'- CSV buckets: `{OUT_CSV}`'])
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')
    if CONTROL.exists():
        marker = '### 2026-05-12 — GMC Phase 7 diagnostics triage'
        text = CONTROL.read_text(encoding='utf-8')
        block = (
            f"\n{marker}\n\n"
            f"- Status: {payload['status']}.\n"
            f"- Item issues atuais: rows={current_summary['rows_with_item_issues']}; instances={current_summary['item_issue_instances']}; delta_vs_phase7={current_summary['delta_vs_phase7_baseline_instances']}.\n"
            f"- Buckets P1: attribute_completion_preview e checkout_url_readonly_probe.\n"
            f"- Nenhum write executado; próximo seguro: approval packet no-write de atributos obrigatórios por exact IDs.\n\n"
        )
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block, encoding='utf-8')
    if INDEX.exists():
        line = f'| LK GMC Phase 7 Diagnostics Triage 2026-05-12 | `areas/lk/rotinas/gmc-{RUN_STAMP}.md` | Triagem read-only dos diagnostics atuais em buckets de ação: atributos obrigatórios, checkout URL, GTIN/policy/image e monitoramento |'
        text = INDEX.read_text(encoding='utf-8')
        if line not in text:
            INDEX.write_text(text.rstrip() + '\n' + line + '\n', encoding='utf-8')
    print(json.dumps({'status': payload['status'], 'summary': current_summary, 'top_bucket': bucket_rows[0] if bucket_rows else None, 'public_report': str(OUT_MD)}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
