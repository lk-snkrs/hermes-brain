#!/usr/bin/env python3
"""LK OS Supplier Quote Approval Packet, read-only.

Turns the weekly quote-validation preview into a Lucas/Júlio approval packet.
It prepares the exact approval choices and safe supplier-brief text, but does
not contact suppliers, buy, create POs, write Shopify/Tiny, change price/stock,
send externally, or enable cron.
"""
from __future__ import annotations

import csv
import json
import pathlib
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE_JSON = ROOT / 'reports/lk-os-weekly-quote-validation-preview-2026-05-04_2026-05-10.json'
PUBLIC_JSON = ROOT / 'reports/lk-os-supplier-quote-approval-packet-2026-05-04_2026-05-10.json'
PUBLIC_CSV = ROOT / 'reports/lk-os-supplier-quote-approval-packet-2026-05-04_2026-05-10.csv'
PUBLIC_MD = ROOT / 'reports/lk-os-supplier-quote-approval-packet-2026-05-04_2026-05-10.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/supplier-quote-approval-packet-readonly-2026-05-11.md'


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def brl(value: float | int | None) -> str:
    if value is None:
        return 'n/d'
    return 'R$ ' + f'{float(value):,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def approval_status(group: dict[str, Any]) -> str:
    if group.get('reference_quote_qty_not_purchase_qty', 0) <= 0:
        return 'needs_data'
    if group.get('p0_count', 0) > 0:
        return 'ready_for_approval_quote_only'
    return 'optional_quote_or_hold'


def approval_recommendation(group: dict[str, Any]) -> str:
    status = approval_status(group)
    if status == 'ready_for_approval_quote_only':
        return 'Aprovar envio de cotação apenas para disponibilidade, custo e lead time; compra separada depois.'
    if status == 'optional_quote_or_hold':
        return 'Opcional: cotar junto se fornecedor já responder P0; caso contrário manter em observação.'
    return 'Não enviar a fornecedor agora; resolver SKU/Tiny ou dados internos primeiro.'


def build_supplier_brief(group: dict[str, Any]) -> str:
    if approval_status(group) == 'needs_data':
        return 'Bloqueado para envio externo: resolver SKU/Tiny antes de cotar.'
    lines = [
        f"Olá, preciso validar disponibilidade e custo para {group['family']}.",
        'Isto é consulta de disponibilidade/preço, ainda não é pedido de compra.',
        'Itens para cotação:',
    ]
    for item in group.get('items') or []:
        qty = int(item.get('reference_quote_qty_not_purchase_qty') or 0)
        if qty <= 0:
            continue
        lines.append(f"- SKU {item.get('sku')} | tamanho {item.get('size_or_variant')} | referência cotação {qty} un | prioridade {item.get('priority')}")
    lines.extend([
        'Responder por favor: custo unitário, disponibilidade imediata, lead time, condição de pagamento e validade da cotação.',
        'Não separar, reservar ou faturar sem confirmação posterior.',
    ])
    return '\n'.join(lines)


def build_decisions(source: dict[str, Any]) -> list[dict[str, Any]]:
    decisions: list[dict[str, Any]] = []
    for idx, group in enumerate(source.get('quote_groups') or [], 1):
        status = approval_status(group)
        decisions.append({
            'decision_id': f'LK-QUOTE-20260504-20260510-{idx:02d}',
            'family': group.get('family'),
            'approval_status': status,
            'recommended_decision': approval_recommendation(group),
            'default_safe_choice': 'needs_data' if status == 'needs_data' else ('approve_quote_only' if status == 'ready_for_approval_quote_only' else 'hold_or_bundle_with_p0'),
            'allowed_approval_values': ['approve_quote_only', 'reject', 'needs_data', 'hold_or_bundle_with_p0'],
            'items_count': group.get('items_count'),
            'p0_count': group.get('p0_count'),
            'p1_count': group.get('p1_count'),
            'reference_quote_qty_not_purchase_qty': group.get('reference_quote_qty_not_purchase_qty'),
            'revenue_signal_fact_shopify': group.get('revenue_signal_fact_shopify'),
            'source_labels': ['fact_shopify', 'fact_tiny_stock', 'derived_reconciliation', 'manual_approval_pending'],
            'supplier_destination': 'pending_lucas_or_julio_selection',
            'supplier_brief_preview_not_sent': build_supplier_brief(group),
            'approval_required_before': ['supplier_contact', 'sending_quote_brief'],
            'separate_approval_required_after_quote': ['purchase', 'purchase_order', 'reservation', 'shopify_write', 'tiny_write', 'price_or_stock_change', 'campaign_or_external_send'],
        })
    return decisions


def summary(decisions: list[dict[str, Any]], source: dict[str, Any]) -> dict[str, Any]:
    counts: dict[str, int] = {}
    quote_qty = 0
    revenue = 0.0
    for d in decisions:
        counts[d['approval_status']] = counts.get(d['approval_status'], 0) + 1
        quote_qty += int(d.get('reference_quote_qty_not_purchase_qty') or 0)
        revenue += float(d.get('revenue_signal_fact_shopify') or 0)
    return {
        'source_quote_validation_preview': str(SOURCE_JSON.relative_to(ROOT)),
        'week': ((source.get('summary') or {}).get('week') or {}),
        'decision_rows': len(decisions),
        'approval_status_counts': counts,
        'reference_quote_qty_not_purchase_qty': quote_qty,
        'revenue_signal_fact_shopify': round(revenue, 2),
        'ready_for_quote_only_count': counts.get('ready_for_approval_quote_only', 0),
        'needs_data_count': counts.get('needs_data', 0),
        'optional_quote_or_hold_count': counts.get('optional_quote_or_hold', 0),
    }


def write_csv(decisions: list[dict[str, Any]]) -> None:
    fields = [
        'decision_id', 'family', 'approval_status', 'default_safe_choice', 'items_count',
        'p0_count', 'p1_count', 'reference_quote_qty_not_purchase_qty',
        'revenue_signal_fact_shopify', 'supplier_destination', 'recommended_decision'
    ]
    with PUBLIC_CSV.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(decisions)


def build_md(payload: dict[str, Any]) -> str:
    s = payload['summary']
    lines = [
        '# LK OS Supplier Quote Approval Packet, read-only',
        '',
        f"Generated at: `{payload['generated_at']}`",
        f"Week: `{s['week'].get('start_date')}` to `{s['week'].get('end_date')}`",
        '',
        '## Escopo',
        '',
        'Pacote de aprovação para Lucas/Júlio decidir se autoriza apenas o envio de cotação a fornecedores. Não é compra, PO, reserva ou contato executado.',
        '',
        '## Resumo',
        '',
        f"- Decisões: {s['decision_rows']}",
        f"- Prontas para aprovar cotação apenas: {s['ready_for_quote_only_count']}",
        f"- Opcionais ou segurar: {s['optional_quote_or_hold_count']}",
        f"- Precisam de dados antes: {s['needs_data_count']}",
        f"- Quantidade referência cotação, não compra: {s['reference_quote_qty_not_purchase_qty']}",
        f"- Sinal receita Shopify: {brl(s['revenue_signal_fact_shopify'])}",
        '',
        '## Como aprovar',
        '',
        'Valores aceitos por decisão: `approve_quote_only`, `reject`, `needs_data`, `hold_or_bundle_with_p0`.',
        'Mesmo se aprovado como `approve_quote_only`, qualquer compra, PO, reserva, alteração de preço/estoque ou campanha precisa de nova aprovação depois da resposta do fornecedor.',
        '',
        '## Decisões',
        '',
    ]
    for d in payload['decisions']:
        lines.extend([
            f"### {d['decision_id']} | {d['family']}",
            f"- Status: `{d['approval_status']}`",
            f"- Default seguro: `{d['default_safe_choice']}`",
            f"- Itens/P0/P1: {d['items_count']} / {d['p0_count']} / {d['p1_count']}",
            f"- Quantidade referência cotação: {d['reference_quote_qty_not_purchase_qty']}",
            f"- Receita Shopify sinal: {brl(d['revenue_signal_fact_shopify'])}",
            f"- Recomendação: {d['recommended_decision']}",
            '- Brief preview, não enviado:',
            '```text',
            d['supplier_brief_preview_not_sent'],
            '```',
            '',
        ])
    lines.extend([
        '## O que não foi feito',
        '',
        '- Nenhum fornecedor foi contatado.',
        '- Nenhuma mensagem externa foi enviada.',
        '- Nenhuma compra, PO, reserva ou pagamento foi feito.',
        '- Nenhum write em Shopify, Tiny, preço, estoque, campanha, cliente ou banco de produção.',
        '- Nenhum cron foi criado.',
    ])
    return '\n'.join(lines) + '\n'


def main() -> None:
    source = json.loads(SOURCE_JSON.read_text(encoding='utf-8'))
    decisions = build_decisions(source)
    payload = {
        'generated_at': now_utc(),
        'scope': 'LK OS approval packet for supplier quote sending, preview-only/read-only',
        'read_only': True,
        'summary': summary(decisions, source),
        'decisions': decisions,
        'approval_schema': {
            'status_values': ['approved', 'rejected', 'needs_data', 'needs_preview', 'executed'],
            'decision_values_for_this_packet': ['approve_quote_only', 'reject', 'needs_data', 'hold_or_bundle_with_p0'],
            'execution_blocked_until_manual_approval': True,
        },
        'not_performed': ['supplier_contact', 'external_send', 'purchase_order', 'purchase', 'reservation', 'shopify_write', 'tiny_write', 'price_or_stock_change', 'campaign_send', 'cron_creation'],
    }
    PUBLIC_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    write_csv(decisions)
    md = build_md(payload)
    PUBLIC_MD.write_text(md, encoding='utf-8')
    BRAIN_DOC.write_text(md.replace('# LK OS Supplier Quote Approval Packet, read-only', '# LK OS, Supplier Quote Approval Packet read-only, 2026-05-11'), encoding='utf-8')
    print(json.dumps({'ok': True, 'decisions': len(decisions), 'json': str(PUBLIC_JSON), 'md': str(PUBLIC_MD), 'csv': str(PUBLIC_CSV), 'brain_doc': str(BRAIN_DOC)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
