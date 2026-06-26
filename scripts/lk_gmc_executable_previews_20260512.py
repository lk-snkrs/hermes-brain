#!/usr/bin/env python3
"""Executable previews for LK GMC A/B/C/D packages.

Creates exact product-id action previews and private rollback snapshots for all
P0/P1 buckets. This script intentionally performs no Merchant/feed/Shopify/DB
writes and does not call delete/insert/update/custombatch/fetchNow.
"""
from __future__ import annotations

import csv
import importlib.util
import json
import os
import pathlib
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
RANKING_PATH = ROOT / 'scripts/lk_gmc_orphan_ranking_20260512.py'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
OUT_JSON = ROOT / 'reports/lk-gmc-executable-previews-2026-05-12.json'
OUT_CSV = ROOT / 'reports/lk-gmc-executable-previews-2026-05-12.csv'
OUT_MD = ROOT / 'reports/lk-gmc-executable-previews-2026-05-12.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/gmc-executable-previews-2026-05-12.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'

PACKAGE_ORDER = ['A_online_stale_triage', 'B_online_identifier_fix', 'D_local_stale_triage', 'C_local_identifier_fix']


def load_ranking_module():
    spec = importlib.util.spec_from_file_location('lk_gmc_orphan_ranking', RANKING_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def package_for(bucket: str) -> str:
    return {
        'online_unmatched_possible_stale': 'A_online_stale_triage',
        'online_identifier_mismatch': 'B_online_identifier_fix',
        'local_unmatched_after_normalization': 'D_local_stale_triage',
        'local_identifier_mismatch': 'C_local_identifier_fix',
    }.get(bucket, 'Z_manual_review')


def proposed_operation(bucket: str) -> str:
    return {
        'online_unmatched_possible_stale': 'merchant_cleanup_candidate_exact_product_id_after_final_sample_validation',
        'online_identifier_mismatch': 'identifier_mapping_fix_candidate_before_delete',
        'local_unmatched_after_normalization': 'local_cleanup_candidate_exact_product_id_after_pos_tiny_validation',
        'local_identifier_mismatch': 'local_identifier_mapping_fix_candidate_preserve_listing',
    }.get(bucket, 'manual_review_only')


def approval_gate(package: str) -> str:
    return {
        'A_online_stale_triage': 'Approval required to delete/suppress exact Merchant online product IDs or change source feed/app.',
        'B_online_identifier_fix': 'Approval required for exact identifier mapping write in Merchant/feed/Shopify/app.',
        'D_local_stale_triage': 'Approval required to delete/suppress exact local Merchant product IDs after POS/Tiny validation.',
        'C_local_identifier_fix': 'Approval required for local inventory/POS/Merchant mapping write; do not disable local channel.',
    }.get(package, 'Approval required for any write.')


def compact_public_product(p: dict[str, Any], status: dict[str, Any]) -> dict[str, Any]:
    return {
        'id': p.get('id'),
        'offerId': p.get('offerId'),
        'channel': p.get('channel'),
        'source': p.get('source'),
        'title': p.get('title'),
        'availability': p.get('availability'),
        'itemGroupId': p.get('itemGroupId'),
        'gtin_present': bool(p.get('gtin')),
        'mpn': p.get('mpn'),
        'price': p.get('price'),
        'status_destinations': [
            {'destination': d.get('destination'), 'channel': d.get('channel'), 'status': d.get('status')}
            for d in (status.get('destinationStatuses') or [])
        ],
        'item_issue_count': len(status.get('itemLevelIssues') or []),
        'creationDate': status.get('creationDate'),
        'lastUpdateDate': status.get('lastUpdateDate'),
    }


def main() -> None:
    rank = load_ranking_module()
    audit = rank.load_audit_module()
    sec = audit.load_doppler()
    mid = sec['MERCHANT_CENTER_ID_LK']
    token = audit.google_access_token(audit.parse_service_account(sec))
    products = audit.list_all('products', mid, token)
    statuses = audit.list_all('productstatuses', mid, token)
    product_by_id = {p.get('id'): p for p in products}
    status_by_pid = {s.get('productId'): s for s in statuses}
    idx = rank.load_shopify_index()
    norm_channels: dict[str, set[str]] = defaultdict(set)
    for p in products:
        norm_channels[rank.norm_offer(p.get('offerId') or '', p.get('channel') or '')].add(p.get('channel') or '')
    classified = [rank.classify(p, status_by_pid.get(p.get('id')) or {}, idx, norm_channels) for p in products]
    queue = [r for r in classified if r.get('priority') in {'P0', 'P1'}]
    queue.sort(key=lambda r: (PACKAGE_ORDER.index(package_for(r['bucket'])) if package_for(r['bucket']) in PACKAGE_ORDER else 99, r['priority'], r['reconciliation_offer_id']))

    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)

    package_rows: dict[str, list[dict[str, Any]]] = defaultdict(list)
    private_snapshot = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'Private rollback snapshot for LK GMC executable previews',
        'read_only': True,
        'records': [],
        'not_performed': ['delete', 'insert', 'update', 'custombatch', 'fetchNow', 'shopify_write', 'feed_write'],
    }

    for r in queue:
        pid = r['product_id']
        p = product_by_id.get(pid) or {}
        st = status_by_pid.get(pid) or {}
        package = package_for(r['bucket'])
        operation = proposed_operation(r['bucket'])
        public = {
            'package': package,
            'priority': r['priority'],
            'bucket': r['bucket'],
            'product_id': pid,
            'channel': r['channel'],
            'offer_id': r['offer_id'],
            'reconciliation_offer_id': r['reconciliation_offer_id'],
            'title': r['title'],
            'proposed_operation': operation,
            'approval_gate': approval_gate(package),
            'rollback_snapshot_ref': 'private_snapshot_records_by_product_id',
            'execution_status': 'not_executed_preview_only',
            'evidence': r.get('evidence') or [],
            'has_destination_problem': bool((r.get('merchant_status') or {}).get('has_disapproved')),
            'item_issue_count': (r.get('merchant_status') or {}).get('item_issue_count') or 0,
        }
        package_rows[package].append(public)
        private_snapshot['records'].append({
            'package': package,
            'classification': public,
            'merchant_product_resource': p,
            'merchant_product_status': st,
            'public_compact': compact_public_product(p, st),
        })

    private_path = PRIVATE_DIR / 'lk-gmc-executable-previews-rollback-2026-05-12.json'
    private_path.write_text(json.dumps(private_snapshot, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.chmod(private_path, 0o600)

    package_summaries = []
    for package in PACKAGE_ORDER:
        rows = package_rows.get(package, [])
        package_summaries.append({
            'package': package,
            'count': len(rows),
            'priority_counts': dict(Counter(r['priority'] for r in rows)),
            'channel_counts': dict(Counter(r['channel'] for r in rows)),
            'bucket_counts': dict(Counter(r['bucket'] for r in rows)),
            'approval_gate': approval_gate(package),
            'proposed_operations': dict(Counter(r['proposed_operation'] for r in rows)),
            'sample_product_ids': [r['product_id'] for r in rows[:20]],
        })

    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'LK GMC executable previews for all A/B/C/D packages',
        'status': 'gmc_executable_previews_ready_preview_only',
        'source_labels': ['fact_merchant_center', 'fact_shopify_local_snapshot', 'derived_reconciliation', 'manual_approval_required'],
        'summary': {
            'queue_total': len(queue),
            'priority_counts': dict(Counter(r['priority'] for r in queue)),
            'channel_counts': dict(Counter(r['channel'] for r in queue)),
            'package_counts': {p['package']: p['count'] for p in package_summaries},
            'private_rollback_snapshot_path': str(private_path),
            'private_rollback_records': len(private_snapshot['records']),
            'merchant_writes': 0,
            'shopify_writes': 0,
            'feed_writes': 0,
            'external_sends': 0,
        },
        'execution_contract': {
            'preview_only': True,
            'approval_required_before_any_write': True,
            'rollback_ready_for_preview': True,
            'rollback_snapshot_private_path': str(private_path),
            'recommended_order': PACKAGE_ORDER,
        },
        'packages': package_summaries,
        'not_performed': private_snapshot['not_performed'] + ['database_write', 'campaign_or_external_send', 'local_inventory_disable', 'gmb_update', 'pos_inventory_write'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    fields = ['package', 'priority', 'bucket', 'product_id', 'channel', 'offer_id', 'reconciliation_offer_id', 'title', 'proposed_operation', 'approval_gate', 'rollback_snapshot_ref', 'execution_status', 'evidence', 'has_destination_problem', 'item_issue_count']
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for package in PACKAGE_ORDER:
            for r in package_rows.get(package, []):
                row = {k: r.get(k) for k in fields}
                row['evidence'] = ';'.join(r.get('evidence') or [])
                w.writerow(row)

    lines = [
        '# LK GMC Executable Previews, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Resumo executivo',
        f"- Itens P0/P1 com preview executável: {len(queue)}",
        f"- Snapshot privado de rollback: `{private_path}`",
        f"- Registros no snapshot privado: {len(private_snapshot['records'])}",
        '- Escritas executadas: 0', '',
        '## Pacotes prontos para aprovação futura',
    ]
    for p in package_summaries:
        lines.extend([
            f"### {p['package']}",
            f"- Itens: {p['count']}",
            f"- Prioridades: {p['priority_counts']}",
            f"- Canais: {p['channel_counts']}",
            f"- Buckets: {p['bucket_counts']}",
            f"- Gate: {p['approval_gate']}",
            f"- Amostra product IDs: {p['sample_product_ids'][:10]}", '',
        ])
    lines.extend([
        '## Contrato de execução',
        '- Este artefato não autoriza execução sozinho.',
        '- Qualquer delete/update/feed/app/Shopify/local inventory ainda exige aprovação atual do Lucas por pacote.',
        '- O rollback privado guarda o recurso Merchant/status atual por product ID para restauração caso uma ação aprovada precise ser revertida.', '',
        '## Não executado',
    ])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')

    if CONTROL.exists():
        marker = '### 2026-05-12 — GMC executable previews A/B/C/D'
        text = CONTROL.read_text(encoding='utf-8')
        block = f"\n{marker}\n\n- Status: preview-only concluído.\n- Previews executáveis A/B/C/D gerados para {len(queue)} itens P0/P1, com CSV de product IDs e snapshot privado de rollback ({len(private_snapshot['records'])} registros).\n- Nenhum Merchant/feed/Shopify/local inventory write executado; execução exige aprovação atual por pacote.\n\n"
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block, encoding='utf-8')
    if INDEX.exists():
        text = INDEX.read_text(encoding='utf-8')
        line = '| LK GMC Executable Previews 2026-05-12 | `areas/lk/rotinas/gmc-executable-previews-2026-05-12.md` | Previews executáveis A/B/C/D para 4.671 P0/P1 com product IDs exatos e snapshot privado de rollback, sem writes |'
        if line not in text:
            anchor = '| LK GMC Action Package Preview 2026-05-12 | `areas/lk/rotinas/gmc-action-package-preview-2026-05-12.md` | Pacote completo preview-only para 4.671 P0/P1 do Merchant, com ordem de execução, rollback e aprovação por bucket, sem writes |'
            INDEX.write_text(text.replace(anchor, anchor + '\n' + line), encoding='utf-8')
    print(json.dumps({'status': payload['status'], 'summary': payload['summary']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
