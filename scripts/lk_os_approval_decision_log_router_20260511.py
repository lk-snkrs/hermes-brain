#!/usr/bin/env python3
"""LK OS Approval Decision Log + Router, read-only.

Materializes supplier quote approval decisions into a stable decision log/router
so Lucas/Júlio approvals can be recorded later without guessing. This creates
no supplier contact, no external sends, no writes to Shopify/Tiny, no purchases,
no production DB writes and no cron.
"""
from __future__ import annotations

import csv
import json
import pathlib
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE_JSON = ROOT / 'reports/lk-os-supplier-quote-approval-packet-2026-05-04_2026-05-10.json'
PUBLIC_JSON = ROOT / 'reports/lk-os-approval-decision-log-router-2026-05-04_2026-05-10.json'
PUBLIC_CSV = ROOT / 'reports/lk-os-approval-decision-log-router-2026-05-04_2026-05-10.csv'
PUBLIC_MD = ROOT / 'reports/lk-os-approval-decision-log-router-2026-05-04_2026-05-10.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/approval-decision-log-router-readonly-2026-05-11.md'


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def brl(value: float | int | None) -> str:
    if value is None:
        return 'n/d'
    return 'R$ ' + f'{float(value):,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def route(decision: dict[str, Any]) -> dict[str, str]:
    status = decision.get('approval_status')
    if status == 'ready_for_approval_quote_only':
        return {
            'route': 'awaiting_lucas_or_julio_approval',
            'next_actor': 'Lucas/Júlio',
            'blocked_action': 'supplier_contact',
            'if_approved_next_step': 'prepare_supplier_send_preview_with_named_destination',
            'if_rejected_next_step': 'mark_rejected_keep_no_action',
        }
    if status == 'optional_quote_or_hold':
        return {
            'route': 'hold_or_bundle_with_p0_decision',
            'next_actor': 'Lucas/Júlio',
            'blocked_action': 'supplier_contact',
            'if_approved_next_step': 'bundle_in_existing_p0_quote_preview_only',
            'if_rejected_next_step': 'hold_monitor_weekly',
        }
    return {
        'route': 'needs_data_before_approval',
        'next_actor': 'Hermes/LK ops data cleanup',
        'blocked_action': 'supplier_contact_and_purchase',
        'if_approved_next_step': 'not_applicable_until_data_resolved',
        'if_rejected_next_step': 'keep_needs_data',
    }


def build_log(source: dict[str, Any]) -> list[dict[str, Any]]:
    log: list[dict[str, Any]] = []
    for d in source.get('decisions') or []:
        routing = route(d)
        log.append({
            'decision_id': d.get('decision_id'),
            'created_at': now_utc(),
            'business_area': 'LK Sneakers',
            'decision_type': 'supplier_quote_contact_only',
            'family': d.get('family'),
            'current_status': 'needs_approval' if d.get('approval_status') != 'needs_data' else 'needs_data',
            'approval_status_from_packet': d.get('approval_status'),
            'default_safe_choice': d.get('default_safe_choice'),
            'allowed_decisions': d.get('allowed_approval_values') or [],
            'recommended_decision': d.get('recommended_decision'),
            'route': routing['route'],
            'next_actor': routing['next_actor'],
            'blocked_action': routing['blocked_action'],
            'if_approved_next_step': routing['if_approved_next_step'],
            'if_rejected_next_step': routing['if_rejected_next_step'],
            'supplier_destination': d.get('supplier_destination'),
            'reference_quote_qty_not_purchase_qty': d.get('reference_quote_qty_not_purchase_qty'),
            'revenue_signal_fact_shopify': d.get('revenue_signal_fact_shopify'),
            'source_labels': d.get('source_labels') or [],
            'manual_decision_value': None,
            'manual_decision_by': None,
            'manual_decision_at': None,
            'execution_status': 'not_executed',
            'external_send_status': 'not_sent',
            'separate_approval_required_after_quote': d.get('separate_approval_required_after_quote') or [],
            'source_packet': str(SOURCE_JSON.relative_to(ROOT)),
        })
    return log


def summary(log: list[dict[str, Any]], source: dict[str, Any]) -> dict[str, Any]:
    status_counts: dict[str, int] = {}
    route_counts: dict[str, int] = {}
    for row in log:
        status_counts[row['current_status']] = status_counts.get(row['current_status'], 0) + 1
        route_counts[row['route']] = route_counts.get(row['route'], 0) + 1
    return {
        'source_packet': str(SOURCE_JSON.relative_to(ROOT)),
        'week': ((source.get('summary') or {}).get('week') or {}),
        'decision_log_rows': len(log),
        'status_counts': status_counts,
        'route_counts': route_counts,
        'quote_reference_qty_not_purchase_qty': sum(int(r.get('reference_quote_qty_not_purchase_qty') or 0) for r in log),
        'revenue_signal_fact_shopify': round(sum(float(r.get('revenue_signal_fact_shopify') or 0) for r in log), 2),
    }


def write_csv(log: list[dict[str, Any]]) -> None:
    fields = [
        'decision_id', 'business_area', 'decision_type', 'family', 'current_status',
        'approval_status_from_packet', 'default_safe_choice', 'route', 'next_actor',
        'blocked_action', 'if_approved_next_step', 'if_rejected_next_step',
        'supplier_destination', 'reference_quote_qty_not_purchase_qty',
        'revenue_signal_fact_shopify', 'manual_decision_value', 'execution_status',
        'external_send_status'
    ]
    with PUBLIC_CSV.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(log)


def build_md(payload: dict[str, Any]) -> str:
    s = payload['summary']
    lines = [
        '# LK OS Approval Decision Log + Router, read-only',
        '',
        f"Generated at: `{payload['generated_at']}`",
        f"Week: `{s['week'].get('start_date')}` to `{s['week'].get('end_date')}`",
        '',
        '## Escopo',
        '',
        'Registro operacional das decisões pendentes. Serve para Lucas/Júlio aprovar, rejeitar ou pedir dados sem misturar isso com execução externa.',
        '',
        '## Resumo',
        '',
        f"- Decisões registradas: {s['decision_log_rows']}",
        f"- Needs approval: {s['status_counts'].get('needs_approval', 0)}",
        f"- Needs data: {s['status_counts'].get('needs_data', 0)}",
        f"- Quantidade referência cotação, não compra: {s['quote_reference_qty_not_purchase_qty']}",
        f"- Sinal receita Shopify: {brl(s['revenue_signal_fact_shopify'])}",
        '',
        '## Router',
        '',
    ]
    for row in payload['decision_log']:
        lines.extend([
            f"### {row['decision_id']} | {row['family']}",
            f"- Status atual: `{row['current_status']}`",
            f"- Rota: `{row['route']}`",
            f"- Próximo ator: {row['next_actor']}",
            f"- Default seguro: `{row['default_safe_choice']}`",
            f"- Ação bloqueada: `{row['blocked_action']}`",
            f"- Se aprovado: `{row['if_approved_next_step']}`",
            f"- Se rejeitado/segurar: `{row['if_rejected_next_step']}`",
            f"- Quantidade referência cotação: {row['reference_quote_qty_not_purchase_qty']}",
            f"- Receita Shopify sinal: {brl(row['revenue_signal_fact_shopify'])}",
            '',
        ])
    lines.extend([
        '## O que não foi feito',
        '',
        '- Nenhuma decisão foi marcada como aprovada pelo Lucas/Júlio.',
        '- Nenhum fornecedor foi contatado.',
        '- Nenhuma mensagem externa foi enviada.',
        '- Nenhuma compra, PO, reserva, pagamento, Shopify/Tiny write, preço, estoque, campanha, cliente, banco de produção ou cron foi executado.',
        '',
        '## Como usar depois',
        '',
        'Quando Lucas/Júlio aprovar uma linha, registrar `manual_decision_value` e só então preparar um preview de envio com fornecedor/destino explícito. Mesmo depois da cotação, compra e PO continuam exigindo nova aprovação.',
    ])
    return '\n'.join(lines) + '\n'


def main() -> None:
    source = json.loads(SOURCE_JSON.read_text(encoding='utf-8'))
    log = build_log(source)
    payload = {
        'generated_at': now_utc(),
        'scope': 'LK OS approval decision log/router for supplier quote approvals, read-only',
        'read_only': True,
        'summary': summary(log, source),
        'decision_log': log,
        'status_schema': {
            'current_status_values': ['needs_approval', 'needs_data', 'approved', 'rejected', 'executed'],
            'manual_decision_values': ['approve_quote_only', 'reject', 'needs_data', 'hold_or_bundle_with_p0'],
            'execution_requires_explicit_followup': True,
        },
        'not_performed': ['approval_marking', 'supplier_contact', 'external_send', 'purchase_order', 'purchase', 'reservation', 'shopify_write', 'tiny_write', 'price_or_stock_change', 'campaign_send', 'cron_creation'],
    }
    PUBLIC_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    write_csv(log)
    md = build_md(payload)
    PUBLIC_MD.write_text(md, encoding='utf-8')
    BRAIN_DOC.write_text(md.replace('# LK OS Approval Decision Log + Router, read-only', '# LK OS, Approval Decision Log + Router read-only, 2026-05-11'), encoding='utf-8')
    print(json.dumps({'ok': True, 'decision_log_rows': len(log), 'json': str(PUBLIC_JSON), 'md': str(PUBLIC_MD), 'csv': str(PUBLIC_CSV), 'brain_doc': str(BRAIN_DOC)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
