#!/usr/bin/env python3
"""Preview-only action package for LK GMC orphan/identifier buckets.

Builds a complete action package with proposed remediation paths and rollback
requirements for all P0/P1 buckets from the GMC orphan ranking. It does not
execute Merchant, feed, Shopify, DB, campaign, local inventory, or external
writes.
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
RANKING_PATH = ROOT / 'scripts/lk_gmc_orphan_ranking_20260512.py'
OUT_JSON = ROOT / 'reports/lk-gmc-action-package-preview-2026-05-12.json'
OUT_CSV = ROOT / 'reports/lk-gmc-action-package-preview-2026-05-12.csv'
OUT_MD = ROOT / 'reports/lk-gmc-action-package-preview-2026-05-12.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/gmc-action-package-preview-2026-05-12.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'


def load_ranking_module():
    spec = importlib.util.spec_from_file_location('lk_gmc_orphan_ranking', RANKING_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def public_row(row: dict[str, Any]) -> dict[str, Any]:
    status = row.get('merchant_status') or {}
    return {
        'priority': row.get('priority'),
        'bucket': row.get('bucket'),
        'channel': row.get('channel'),
        'product_id': row.get('product_id'),
        'offer_id': row.get('offer_id'),
        'reconciliation_offer_id': row.get('reconciliation_offer_id'),
        'title': row.get('title'),
        'source': row.get('source'),
        'availability': row.get('availability'),
        'recommended_action': row.get('recommended_action'),
        'evidence': row.get('evidence') or [],
        'has_destination_problem': bool(status.get('has_disapproved')),
        'item_issue_count': status.get('item_issue_count') or 0,
    }


def action_for_bucket(bucket: str) -> dict[str, Any]:
    if bucket == 'online_unmatched_possible_stale':
        return {
            'package': 'A_online_stale_triage',
            'risk': 'high',
            'proposed_sequence': [
                'Verify a sample against live Shopify by offer_id, GTIN/barcode, product handle/title.',
                'If no current Shopify/Data Spine match exists, prepare Merchant cleanup/delete preview for exact product IDs only.',
                'Before execution, export product IDs, titles, URLs, status and current resource snapshot as rollback evidence.',
                'Execute only after Lucas approval; verify Merchant count/diagnostics after reprocessing lag.',
            ],
            'rollback_requirement': 'Reinsert or restore exact Merchant product resource/feed row from pre-action snapshot if a valid item is removed.',
            'approval_needed': 'Lucas approval for Merchant product delete/suppression or feed change.',
        }
    if bucket == 'online_identifier_mismatch':
        return {
            'package': 'B_online_identifier_fix',
            'risk': 'medium',
            'proposed_sequence': [
                'Confirm whether GTIN/product match maps to an active Shopify variant with different SKU/offer_id.',
                'Prefer fixing source identifiers/feed mapping over deleting the Merchant item.',
                'Generate exact before/after mapping preview for SKU/offer_id/product_id/GTIN.',
                'Execute only after approval for the specific source to change: Merchant/feed/Shopify/app.',
            ],
            'rollback_requirement': 'Keep old identifier mapping and feed/resource snapshot; rollback by restoring previous identifier/feed row.',
            'approval_needed': 'Lucas approval for any feed, Merchant, Shopify, or app identifier write.',
        }
    if bucket == 'local_identifier_mismatch':
        return {
            'package': 'C_local_identifier_fix',
            'risk': 'medium_high',
            'proposed_sequence': [
                'Preserve local listings by default because LK uses physical store/local inventory.',
                'Confirm Shopify POS/local inventory mapping for LIA_ offer_id and current SKU/GTIN/product.',
                'Prepare mapping correction preview; avoid local inventory deletion unless stale is proven.',
                'Execute only after approval because it can affect local free listings/local inventory visibility.',
            ],
            'rollback_requirement': 'Keep LIA product resource snapshot and POS/local mapping before any change; rollback by restoring mapping/resource.',
            'approval_needed': 'Lucas approval for any local inventory/POS/Merchant mapping write.',
        }
    if bucket == 'local_unmatched_after_normalization':
        return {
            'package': 'D_local_stale_triage',
            'risk': 'medium_high',
            'proposed_sequence': [
                'Sample against live Shopify POS/local inventory and Tiny before treating as stale.',
                'If no valid current source exists, prepare local-only cleanup preview by exact product ID.',
                'Do not disable the local channel globally; act only on proven stale product IDs.',
                'Execute only after approval and rollback snapshot.',
            ],
            'rollback_requirement': 'Keep exact local product resource snapshot; rollback by restoring/reinserting local product or source feed row.',
            'approval_needed': 'Lucas approval for local Merchant cleanup or local inventory feed/app change.',
        }
    return {
        'package': 'Z_manual_review',
        'risk': 'unknown',
        'proposed_sequence': ['Manual review required before any action.'],
        'rollback_requirement': 'Snapshot before action.',
        'approval_needed': 'Approval required for any write.',
    }


def main() -> None:
    rank = load_ranking_module()
    audit = rank.load_audit_module()
    sec = audit.load_doppler()
    mid = sec['MERCHANT_CENTER_ID_LK']
    token = audit.google_access_token(audit.parse_service_account(sec))
    products = audit.list_all('products', mid, token)
    statuses = audit.list_all('productstatuses', mid, token)
    status_by_pid = {s.get('productId'): s for s in statuses}
    idx = rank.load_shopify_index()
    norm_channels: dict[str, set[str]] = defaultdict(set)
    for p in products:
        norm_channels[rank.norm_offer(p.get('offerId') or '', p.get('channel') or '')].add(p.get('channel') or '')
    classified = [rank.classify(p, status_by_pid.get(p.get('id')) or {}, idx, norm_channels) for p in products]
    queue = [r for r in classified if r.get('priority') in {'P0', 'P1'}]
    queue.sort(key=lambda r: (r['priority'], r['bucket'], r['channel'], r['reconciliation_offer_id']))

    by_bucket = defaultdict(list)
    for r in queue:
        by_bucket[r['bucket']].append(r)
    bucket_packages = []
    for bucket, rows in sorted(by_bucket.items(), key=lambda x: (-len(x[1]), x[0])):
        action = action_for_bucket(bucket)
        bucket_packages.append({
            'bucket': bucket,
            'count': len(rows),
            'priority_counts': dict(Counter(r['priority'] for r in rows)),
            'channel_counts': dict(Counter(r['channel'] for r in rows)),
            'action_package': action,
            'sample_rows': [public_row(r) for r in rows[:25]],
        })

    package_rows = []
    for r in queue:
        action = action_for_bucket(r['bucket'])
        pr = public_row(r)
        pr.update({
            'action_package': action['package'],
            'risk': action['risk'],
            'approval_needed': action['approval_needed'],
            'rollback_requirement': action['rollback_requirement'],
            'execution_status': 'not_executed_preview_only',
        })
        package_rows.append(pr)

    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'LK GMC complete action package preview read-only',
        'status': 'gmc_action_package_preview_ready_readonly',
        'source_labels': ['fact_merchant_center', 'fact_shopify_local_snapshot', 'derived_reconciliation', 'manual_approval_required'],
        'summary': {
            'merchant_products_read': len(products),
            'queue_total_p0_p1': len(queue),
            'priority_counts': dict(Counter(r['priority'] for r in queue)),
            'channel_counts': dict(Counter(r['channel'] for r in queue)),
            'bucket_counts': dict(Counter(r['bucket'] for r in queue)),
            'package_counts': dict(Counter(action_for_bucket(r['bucket'])['package'] for r in queue)),
            'merchant_writes': 0,
            'shopify_writes': 0,
            'feed_writes': 0,
            'external_sends': 0,
        },
        'decision': {
            'recommended_execution_order': [
                'A_online_stale_triage',
                'B_online_identifier_fix',
                'D_local_stale_triage',
                'C_local_identifier_fix',
            ],
            'why': 'Start with online stale because it is largest and least likely to affect physical local inventory; keep local changes behind stricter approval.',
            'execution_requires_current_approval': True,
        },
        'bucket_packages': bucket_packages,
        'csv_rows_written': min(len(package_rows), 3000),
        'not_performed': [
            'merchant_product_delete', 'merchant_product_update', 'feed_update', 'shopify_write', 'database_write',
            'campaign_or_external_send', 'local_inventory_disable', 'gmb_update', 'pos_inventory_write'
        ],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    fields = ['priority', 'bucket', 'action_package', 'risk', 'channel', 'product_id', 'offer_id', 'reconciliation_offer_id', 'title', 'source', 'availability', 'recommended_action', 'evidence', 'has_destination_problem', 'item_issue_count', 'approval_needed', 'rollback_requirement', 'execution_status']
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in package_rows[:3000]:
            rr = {k: r.get(k) for k in fields}
            rr['evidence'] = ';'.join(r.get('evidence') or [])
            w.writerow(rr)

    lines = [
        '# LK GMC Action Package Preview, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Resumo executivo',
        f"- Fila P0/P1 total: {len(queue)}",
        f"- P0/P1 por prioridade: {payload['summary']['priority_counts']}",
        f"- Por canal: {payload['summary']['channel_counts']}",
        f"- Merchant/Shopify/feed writes: 0", '',
        '## Pacotes de ação',
    ]
    for pkg in bucket_packages:
        action = pkg['action_package']
        lines.extend([
            f"### {action['package']} — {pkg['bucket']}",
            f"- Itens: {pkg['count']}",
            f"- Risco: `{action['risk']}`",
            f"- Prioridades: {pkg['priority_counts']}",
            f"- Canais: {pkg['channel_counts']}",
            f"- Aprovação: {action['approval_needed']}",
            f"- Rollback: {action['rollback_requirement']}",
            '- Sequência proposta:',
        ])
        for step in action['proposed_sequence']:
            lines.append(f'  - {step}')
        lines.append('')
    lines.extend([
        '## Ordem recomendada',
        '1. A_online_stale_triage: maior volume e menor risco sobre inventário físico.',
        '2. B_online_identifier_fix: saneamento de ID antes de apagar.',
        '3. D_local_stale_triage: local sensível, só produto provado como stale.',
        '4. C_local_identifier_fix: preservar local listings e corrigir mapeamento com cuidado.', '',
        '## Não executado',
    ])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')

    if CONTROL.exists():
        marker = '### 2026-05-12 — GMC action package preview'
        text = CONTROL.read_text(encoding='utf-8')
        block = f"\n{marker}\n\n- Status: preview-only concluído.\n- Pacote completo gerado para {len(queue)} itens P0/P1: {payload['summary']['package_counts']}.\n- Ordem recomendada: online stale, online identifier fix, local stale, local identifier fix.\n- Nenhum Merchant/feed/Shopify/local inventory write executado; execução exige aprovação atual por pacote.\n\n"
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block, encoding='utf-8')
    if INDEX.exists():
        text = INDEX.read_text(encoding='utf-8')
        line = '| LK GMC Action Package Preview 2026-05-12 | `areas/lk/rotinas/gmc-action-package-preview-2026-05-12.md` | Pacote completo preview-only para 4.671 P0/P1 do Merchant, com ordem de execução, rollback e aprovação por bucket, sem writes |'
        if line not in text:
            anchor = '| LK GMC Orphan Ranking 2026-05-12 | `areas/lk/rotinas/gmc-orphan-ranking-2026-05-12.md` | Ranking read-only P0/P1 de locais e online órfãos após normalização `LIA_`, separando válidos, mismatch e possíveis stale, sem Merchant/Shopify writes |'
            INDEX.write_text(text.replace(anchor, anchor + '\n' + line), encoding='utf-8')
    print(json.dumps({'status': payload['status'], 'summary': payload['summary'], 'recommended_execution_order': payload['decision']['recommended_execution_order']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
