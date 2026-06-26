#!/usr/bin/env python3
"""Final approval packet for LK GMC local C/D 63 residual old-LIA cleanup.

Builds a Lucas-reviewable packet from the read-only POS/source validation output.
Does not execute Merchant, Shopify, Tiny, POS, feed, DB, campaign or external
writes. The generated execution plan is a proposal only.
"""
from __future__ import annotations

import csv
import json
import os
import pathlib
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
RUN_STAMP = '2026-05-12-local-cd-final-approval-packet'
INPUT_CSV = ROOT / 'reports/lk-gmc-2026-05-12-local-cd-pos-source-validation.csv'
INPUT_JSON = ROOT / 'reports/lk-gmc-2026-05-12-local-cd-pos-source-validation.json'
SOURCE_ROLLBACK = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-12-local-cd-pos-source-validation-rollback-snapshot.json')
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_reconciliation')
PRIVATE_CSV = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}.csv'

APPROVAL_STATE = 'awaiting_lucas_explicit_execution_approval'
EXECUTOR_TO_BUILD_AFTER_APPROVAL = 'scripts/lk_gmc_execute_local_cd_63_old_lia_cleanup_20260512.py'


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_rows() -> list[dict[str, str]]:
    rows = list(csv.DictReader(INPUT_CSV.open(encoding='utf-8')))
    return [r for r in rows if r.get('decision_state') == 'old_lia_sku_replaced_by_active_shopify_product_with_replacement_local_present']


def candidate_row(r: dict[str, str]) -> dict[str, Any]:
    replacement_ids = [x for x in (r.get('replacement_local_product_ids_sample') or '').split(';') if x]
    current_skus = [x for x in (r.get('shopify_current_skus_sample') or '').split(';') if x]
    return {
        'approval_state': APPROVAL_STATE,
        'operation_type_if_approved': 'merchant_local_product_delete_exact_old_id_only',
        'old_product_id_to_delete_if_approved': r.get('product_id'),
        'old_offer_id': r.get('old_offer_id'),
        'old_normalized_sku': r.get('old_normalized_sku'),
        'merchant_title': r.get('merchant_title'),
        'package_origin': r.get('package'),
        'decision_state': r.get('decision_state'),
        'shopify_product_status': r.get('shopify_title_match_status'),
        'shopify_product_title': r.get('shopify_product_title'),
        'shopify_product_handle': r.get('shopify_product_handle'),
        'shopify_current_skus': current_skus,
        'replacement_local_product_ids_present': replacement_ids,
        'replacement_local_present_count': int(r.get('replacement_local_present_count') or 0),
        'shopify_total_inventory_quantity': r.get('shopify_total_inventory_quantity'),
        'merchant_destination_problem': r.get('merchant_destination_problem') == 'True',
        'merchant_item_issue_count': int(r.get('merchant_item_issue_count') or 0),
        'why_candidate': 'old LIA SKU absent from active Shopify product; replacement local row for current Shopify SKU is already present; Tiny exact codigo was absent in prior read-only probe',
        'hard_guards_required_before_execution': [
            'delete only exact old_product_id_to_delete_if_approved',
            'confirm product_id starts with local:pt:BR:LIA_',
            'confirm at least one replacement_local_product_id remains present before delete',
            'confirm old_product_id differs from every replacement_local_product_id',
            'do not delete replacement local rows',
            'do not disable local channel or POS provider',
            'use private rollback snapshot for restore if needed',
        ],
    }


def main() -> None:
    rows = read_rows()
    if not rows:
        raise RuntimeError('no_approval_candidates_found')
    candidates = [candidate_row(r) for r in rows]
    package_counts = Counter(c['package_origin'] for c in candidates)
    title_counts = Counter(c['merchant_title'] for c in candidates)
    replacement_presence = Counter('has_replacement' if c['replacement_local_present_count'] > 0 else 'missing_replacement' for c in candidates)
    guard_failures = []
    for c in candidates:
        old_pid = c['old_product_id_to_delete_if_approved'] or ''
        repl = set(c['replacement_local_product_ids_present'])
        if not old_pid.startswith('local:pt:BR:LIA_'):
            guard_failures.append({'product_id': old_pid, 'failure': 'old_product_id_not_local_lia'})
        if not repl:
            guard_failures.append({'product_id': old_pid, 'failure': 'no_replacement_local_present'})
        if old_pid in repl:
            guard_failures.append({'product_id': old_pid, 'failure': 'old_product_id_equals_replacement'})

    payload = {
        'generated_at': utc_now(),
        'status': 'gmc_local_cd_final_approval_packet_ready_no_execution',
        'scope': 'Final approval packet for 63 residual old local LIA rows, no execution',
        'source_labels': ['fact_merchant_center', 'fact_shopify', 'fact_tiny_stock', 'derived_reconciliation', 'manual_approval_required'],
        'summary': {
            'candidate_rows': len(candidates),
            'package_counts': dict(package_counts),
            'unique_merchant_titles': len(title_counts),
            'replacement_presence_counts': dict(replacement_presence),
            'guard_failures_count': len(guard_failures),
            'private_rollback_snapshot_path': str(SOURCE_ROLLBACK),
            'proposed_executor_path_after_approval': EXECUTOR_TO_BUILD_AFTER_APPROVAL,
            'merchant_writes': 0,
            'shopify_writes': 0,
            'tiny_writes': 0,
            'pos_or_local_inventory_writes': 0,
            'database_writes': 0,
            'external_sends': 0,
        },
        'approval_contract': {
            'current_state': APPROVAL_STATE,
            'what_lucas_would_approve_if_he_says_execute_this_packet': 'Delete only the 63 exact old Merchant local product IDs listed in candidates[].old_product_id_to_delete_if_approved, after rebuilding/validating an executor with the hard guards below and verifying replacement rows still exist.',
            'what_is_not_authorized_by_this_packet': [
                'delete online products',
                'delete replacement local rows',
                'disable local inventory/channel/POS',
                'modify Shopify/Tiny/feed/database',
                'touch campaigns or customer-facing surfaces',
                'expand scope beyond the 63 exact product IDs',
            ],
            'rollback_plan_if_approved_later': [
                'Use private rollback snapshot at the path in summary.private_rollback_snapshot_path.',
                'If any valid item is removed or count/regression appears, reinsert exact merchant_product_resource for affected old_product_id.',
                'Verify exact product ID presence/absence after Content API eventual consistency delay.',
                'Never restore/modify replacement local rows unless separate explicit approval exists.',
            ],
            'hard_guards_for_executor': [
                'load candidates from this JSON, not from a broad query',
                'abort if guard_failures_count is nonzero',
                'preflight list current Merchant products and confirm every replacement_local_product_id is present',
                'preflight confirm every old_product_id exists or is already gone/idempotent',
                'delete only exact old_product_id values; no prefix/wildcard deletes',
                'after delete, poll full list until each old ID is gone and each replacement ID remains present',
                'on any replacement missing/regression, stop and do not continue batch',
            ],
        },
        'guard_failures': guard_failures,
        'candidates': candidates,
        'not_performed': ['merchant_product_delete','merchant_product_update','content_api_custombatch','feed_update','shopify_write','tiny_write','database_write','local_inventory_disable','pos_inventory_write','campaign_or_external_send'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    fields = [
        'approval_state','operation_type_if_approved','old_product_id_to_delete_if_approved','old_offer_id','old_normalized_sku','merchant_title','package_origin','decision_state','shopify_product_status','shopify_product_title','shopify_product_handle','shopify_current_skus','replacement_local_product_ids_present','replacement_local_present_count','shopify_total_inventory_quantity','merchant_destination_problem','merchant_item_issue_count','why_candidate'
    ]
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True); os.chmod(PRIVATE_DIR, 0o700)
    for path in (OUT_CSV, PRIVATE_CSV):
        with path.open('w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            for c in candidates:
                row = {k: c.get(k) for k in fields}
                row['shopify_current_skus'] = ';'.join(c.get('shopify_current_skus') or [])
                row['replacement_local_product_ids_present'] = ';'.join(c.get('replacement_local_product_ids_present') or [])
                w.writerow(row)
    os.chmod(PRIVATE_CSV, 0o600)

    examples = candidates[:10]
    lines = [
        '# LK GMC Local C/D Final Approval Packet, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Resumo executivo',
        f"- Candidatos exatos: {len(candidates)}",
        f"- Pacotes origem: {dict(package_counts)}",
        f"- Títulos únicos: {len(title_counts)}",
        f"- Replacement local presente: {dict(replacement_presence)}",
        f"- Guard failures: {len(guard_failures)}",
        '- Merchant/Shopify/Tiny/POS/DB writes: 0', '',
        '## O que este pacote pediria se Lucas aprovar depois',
        '- Deletar somente os 63 IDs antigos `local:pt:BR:LIA_<old_sku>` listados no JSON/CSV.',
        '- Preservar todas as linhas replacement `local:pt:BR:LIA_<current_sku>`.',
        '- Não mexer em online, Shopify, Tiny, feed, POS, banco, campanha ou local channel.', '',
        '## Por que estes 63 entraram',
        '- Shopify live encontrou produto ativo pelo título exato.',
        '- O SKU antigo não está mais entre os SKUs atuais do produto.',
        '- Já existe linha local replacement para o SKU atual do Shopify.',
        '- Probe Tiny anterior não encontrou `codigo` exato para o SKU antigo.', '',
        '## Exemplos',
    ]
    for c in examples:
        lines.extend([
            f"- Old: `{c['old_product_id_to_delete_if_approved']}`",
            f"  - Produto: {c['merchant_title']}",
            f"  - Current SKUs Shopify: {', '.join(c['shopify_current_skus'][:5])}",
            f"  - Replacement local: {', '.join(c['replacement_local_product_ids_present'][:5])}",
        ])
    lines.extend([
        '', '## Rollback se aprovado/executado depois',
        f"- Snapshot privado: `{SOURCE_ROLLBACK}`",
        '- Restaurar recurso Merchant exato se algum item válido for removido ou houver regressão.',
        '- Verificar old gone + replacement present após delay de consistência da Content API.', '',
        '## Arquivos',
        f"- JSON público: `{OUT_JSON}`",
        f"- CSV público: `{OUT_CSV}`",
        f"- CSV privado/auditoria chmod 600: `{PRIVATE_CSV}`", '',
        '## Não executado',
    ])
    for item in payload['not_performed']:
        lines.append(f'- {item}')
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')

    if CONTROL.exists():
        marker = '### 2026-05-12 — GMC local C/D final approval packet'
        text = CONTROL.read_text(encoding='utf-8')
        block = (
            f"\n{marker}\n\n"
            f"- Status: approval packet final gerado sem execução.\n"
            f"- Escopo: {len(candidates)} old local LIA IDs; guard_failures={len(guard_failures)}.\n"
            f"- Snapshot privado rollback: `{SOURCE_ROLLBACK}`.\n"
            f"- Execução continua bloqueada até aprovação explícita Lucas para estes 63 IDs.\n"
        )
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block + '\n', encoding='utf-8')
    if INDEX.exists():
        text = INDEX.read_text(encoding='utf-8')
        line = '| LK GMC Local C/D Final Approval Packet 2026-05-12 | `areas/lk/rotinas/gmc-2026-05-12-local-cd-final-approval-packet.md` | Pacote final sem execução para 63 old LIA local IDs, com razões por item, replacement rows, rollback privado e guards de execução |'
        if line not in text:
            INDEX.write_text(text.rstrip() + '\n' + line + '\n', encoding='utf-8')

    print(json.dumps({'status': payload['status'], 'summary': payload['summary'], 'public_report': str(OUT_MD)}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
