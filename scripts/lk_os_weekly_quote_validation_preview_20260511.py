#!/usr/bin/env python3
"""LK OS Weekly Quote Validation Preview, read-only.

Converts the Weekly Stock/SKU Action Plan into an internal supplier-validation
and quote brief. It computes sale-price signals, cost ceilings for target gross
margins, lead-time gates and family grouping. It does not contact suppliers,
create purchase orders, write Shopify/Tiny, change price/stock/campaign, send
externally or enable cron.
"""
from __future__ import annotations

import csv
import json
import pathlib
import re
from collections import defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE_JSON = ROOT / 'reports/lk-os-weekly-stock-sku-action-plan-2026-05-04_2026-05-10.json'
PUBLIC_JSON = ROOT / 'reports/lk-os-weekly-quote-validation-preview-2026-05-04_2026-05-10.json'
PUBLIC_CSV = ROOT / 'reports/lk-os-weekly-quote-validation-preview-2026-05-04_2026-05-10.csv'
PUBLIC_MD = ROOT / 'reports/lk-os-weekly-quote-validation-preview-2026-05-04_2026-05-10.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/weekly-quote-validation-preview-readonly-2026-05-11.md'
TARGET_MARGINS = [0.45, 0.50, 0.55]


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def brl(value: float | int | None) -> str:
    if value is None:
        return 'n/d'
    return 'R$ ' + f'{float(value):,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def stock_value(value: Any) -> str:
    return 'n/d' if value is None else str(value)


def avg_sale_price(item: dict[str, Any]) -> float | None:
    qty = int(item.get('sold_qty_fact_shopify') or 0)
    revenue = float(item.get('line_revenue_estimate_fact_shopify') or 0)
    if qty <= 0 or revenue <= 0:
        return None
    return round(revenue / qty, 2)


def cost_ceiling(avg_price: float | None, margin: float) -> float | None:
    if avg_price is None:
        return None
    return round(avg_price * (1 - margin), 2)


def family_key(title: str) -> str:
    title_clean = re.sub(r'\s+', ' ', title).strip()
    families = [
        ('Nike Moon Shoe SP Jacquemus', r'Nike Moon Shoe SP Jacquemus'),
        ('New Balance 9060', r'New Balance 9060'),
        ('New Balance 530', r'New Balance 530'),
        ('Nike Mind 002', r'Nike Mind 002'),
        ('Comme des Garçons PLAY Polo', r'Comme des Garçons.*Polo|Polo Comme des Garçons'),
        ('Onitsuka Tiger Mexico 66', r'Onitsuka Tiger Mexico 66'),
        ('Bearbrick Series 48', r'Bearbrick Series 48'),
    ]
    for label, pattern in families:
        if re.search(pattern, title_clean, flags=re.I):
            return label
    words = title_clean.split()
    return ' '.join(words[:4]) if words else 'Produto sem família'


def reference_quote_qty(item: dict[str, Any]) -> int:
    sold = int(item.get('sold_qty_fact_shopify') or 0)
    if item.get('priority') == 'P0':
        return max(1, min(3, sold + 1))
    if item.get('action_status') == 'sku_resolution_first':
        return 0
    return max(1, min(2, sold))


def lead_time_gate(item: dict[str, Any]) -> dict[str, str]:
    if item.get('action_status') == 'sku_resolution_first':
        return {
            'gate': 'blocked_until_sku_tiny_resolution',
            'ready_stock_or_0_7_days': 'not_applicable',
            '8_15_days': 'not_applicable',
            'over_15_days': 'not_applicable',
            'note': 'Resolver SKU/Tiny antes de cotar ou comprar.',
        }
    if item.get('priority') == 'P0':
        return {
            'gate': 'p0_lead_time_sensitive',
            'ready_stock_or_0_7_days': 'eligible_for_internal_quote_review',
            '8_15_days': 'requires_lucas_or_julio_decision',
            'over_15_days': 'not_recommended_without_presale_or_explicit_decision',
            'note': 'P0 só deve avançar se houver pronta entrega ou lead time curto, com margem validada.',
        }
    return {
        'gate': 'p1_optional_or_bundle',
        'ready_stock_or_0_7_days': 'optional_quote_if_margin_strong',
        '8_15_days': 'monitor_or_bundle_only',
        'over_15_days': 'not_recommended_now',
        'note': 'P1 não é autorização de compra; cotar só se fizer sentido comercial.',
    }


def build_rows(source: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for item in source.get('queue') or []:
        if item.get('action_status') == 'monitor_only':
            continue
        avg = avg_sale_price(item)
        row = {
            'priority': item.get('priority'),
            'action_status': item.get('action_status'),
            'family': family_key(item.get('product_title') or ''),
            'product_title': item.get('product_title'),
            'sku': item.get('sku'),
            'size_or_variant': item.get('size_or_variant'),
            'sold_qty_fact_shopify': item.get('sold_qty_fact_shopify'),
            'revenue_fact_shopify': item.get('line_revenue_estimate_fact_shopify'),
            'avg_sale_price_fact_shopify': avg,
            'tiny_saldo_fact_tiny_stock': item.get('tiny_saldo_fact_tiny_stock'),
            'stock_risk': item.get('stock_risk'),
            'confidence': item.get('confidence'),
            'reference_quote_qty_not_purchase_qty': reference_quote_qty(item),
            'cost_ceiling_45_margin': cost_ceiling(avg, 0.45),
            'cost_ceiling_50_margin': cost_ceiling(avg, 0.50),
            'cost_ceiling_55_margin': cost_ceiling(avg, 0.55),
            'lead_time_gate': lead_time_gate(item),
            'source_labels': item.get('source_labels') or ['fact_shopify', 'fact_tiny_stock'],
            'supplier_cost_status': 'pending_supplier_quote',
            'supplier_availability_status': 'not_checked_no_supplier_contact',
            'recommended_internal_next_step': recommended_next_step(item),
            'not_authorized_actions': ['supplier_contact', 'purchase_order', 'purchase', 'shopify_write', 'tiny_write', 'price_or_stock_change', 'campaign_or_external_send'],
        }
        rows.append(row)
    return rows


def recommended_next_step(item: dict[str, Any]) -> str:
    if item.get('action_status') == 'sku_resolution_first':
        return 'Resolver SKU/Tiny antes de qualquer cotação externa.'
    if item.get('priority') == 'P0':
        return 'Montar cotação interna por família; avançar só com pronta entrega ou até 7 dias, custo dentro do teto e aprovação Lucas/Júlio.'
    return 'Validar estoque atual e custo apenas se fornecedor já tiver disponibilidade forte; caso contrário monitorar.'


def group_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[row['family']].append(row)
    groups = []
    for family, items in grouped.items():
        quote_qty = sum(int(i.get('reference_quote_qty_not_purchase_qty') or 0) for i in items)
        revenue = round(sum(float(i.get('revenue_fact_shopify') or 0) for i in items), 2)
        p0 = sum(1 for i in items if i.get('priority') == 'P0')
        p1 = sum(1 for i in items if i.get('priority') == 'P1')
        groups.append({
            'family': family,
            'items_count': len(items),
            'p0_count': p0,
            'p1_count': p1,
            'reference_quote_qty_not_purchase_qty': quote_qty,
            'revenue_signal_fact_shopify': revenue,
            'quote_brief_preview': build_quote_brief(family, items),
            'items': [{'sku': i['sku'], 'size_or_variant': i['size_or_variant'], 'priority': i['priority'], 'reference_quote_qty_not_purchase_qty': i['reference_quote_qty_not_purchase_qty']} for i in items],
        })
    return sorted(groups, key=lambda g: (g['p0_count'], g['revenue_signal_fact_shopify'], g['reference_quote_qty_not_purchase_qty']), reverse=True)


def build_quote_brief(family: str, items: list[dict[str, Any]]) -> str:
    lines = [f'Validar disponibilidade e custo para {family}. Quantidade é referência de cotação, não compra aprovada.']
    for i in items:
        lines.append(f"{i['sku']} tamanho {i['size_or_variant']}: ref {i['reference_quote_qty_not_purchase_qty']} un, teto custo 50% margem {brl(i['cost_ceiling_50_margin'])}, prioridade {i['priority']}.")
    lines.append('Responder custo unitário, disponibilidade imediata, lead time e condições; não enviar pedido sem aprovação Lucas/Júlio.')
    return ' '.join(lines)


def summary(rows: list[dict[str, Any]], groups: list[dict[str, Any]], source: dict[str, Any]) -> dict[str, Any]:
    return {
        'source_action_plan': str(SOURCE_JSON.relative_to(ROOT)),
        'week': ((source.get('summary') or {}).get('week') or {}),
        'rows': len(rows),
        'p0_count': sum(1 for r in rows if r.get('priority') == 'P0'),
        'p1_count': sum(1 for r in rows if r.get('priority') == 'P1'),
        'sku_resolution_first_count': sum(1 for r in rows if r.get('action_status') == 'sku_resolution_first'),
        'quote_groups_count': len(groups),
        'reference_quote_qty_not_purchase_qty': sum(int(r.get('reference_quote_qty_not_purchase_qty') or 0) for r in rows),
        'revenue_signal_fact_shopify': round(sum(float(r.get('revenue_fact_shopify') or 0) for r in rows), 2),
        'source_labels': ['fact_shopify', 'fact_tiny_stock', 'derived_reconciliation'],
    }


def write_csv(rows: list[dict[str, Any]]) -> None:
    fields = [
        'priority', 'action_status', 'family', 'product_title', 'sku', 'size_or_variant',
        'sold_qty_fact_shopify', 'revenue_fact_shopify', 'avg_sale_price_fact_shopify',
        'tiny_saldo_fact_tiny_stock', 'reference_quote_qty_not_purchase_qty',
        'cost_ceiling_45_margin', 'cost_ceiling_50_margin', 'cost_ceiling_55_margin',
        'supplier_cost_status', 'supplier_availability_status', 'recommended_internal_next_step'
    ]
    with PUBLIC_CSV.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)


def build_md(payload: dict[str, Any]) -> str:
    s = payload['summary']
    lines = [
        '# LK OS Weekly Quote Validation Preview, read-only',
        '',
        f"Generated at: `{payload['generated_at']}`",
        f"Week: `{s['week'].get('start_date')}` to `{s['week'].get('end_date')}`",
        '',
        '## Escopo',
        '',
        'Preview interno para transformar a fila Stock/SKU em validação de fornecedor, lead time e margem. Quantidade abaixo é referência para cotação, não autorização de compra.',
        '',
        '## Resumo',
        '',
        f"- Linhas avaliadas: {s['rows']}",
        f"- P0: {s['p0_count']}",
        f"- P1: {s['p1_count']}",
        f"- Bloqueadas até resolver SKU/Tiny: {s['sku_resolution_first_count']}",
        f"- Grupos de cotação: {s['quote_groups_count']}",
        f"- Quantidade referência para cotação, não compra: {s['reference_quote_qty_not_purchase_qty']}",
        f"- Sinal de receita Shopify: {brl(s['revenue_signal_fact_shopify'])}",
        '- Fonte de venda: `fact_shopify`',
        '- Fonte de estoque: `fact_tiny_stock`',
        '- Tetos de custo: `derived_reconciliation`, calculados a partir do preço médio vendido e margem alvo.',
        '',
        '## Grupos de cotação preview',
        '',
    ]
    for idx, group in enumerate(payload['quote_groups'], 1):
        lines.extend([
            f"### {idx}. {group['family']}",
            f"- Itens: {group['items_count']} | P0: {group['p0_count']} | P1: {group['p1_count']}",
            f"- Quantidade referência para cotação: {group['reference_quote_qty_not_purchase_qty']}",
            f"- Receita Shopify sinal: {brl(group['revenue_signal_fact_shopify'])}",
            f"- Brief interno: {group['quote_brief_preview']}",
            '',
        ])
    lines.append('## Top itens com teto de custo')
    lines.append('')
    for idx, row in enumerate(payload['rows'][:14], 1):
        lines.extend([
            f"### {idx}. {row['product_title']} | {row['size_or_variant']}",
            f"- Prioridade: {row['priority']} | status: `{row['action_status']}`",
            f"- SKU: `{row['sku']}` | família: {row['family']}",
            f"- Venda Shopify: {row['sold_qty_fact_shopify']} un, {brl(row['revenue_fact_shopify'])}, preço médio {brl(row['avg_sale_price_fact_shopify'])}",
            f"- Tiny saldo: `{stock_value(row['tiny_saldo_fact_tiny_stock'])}`",
            f"- Quantidade referência para cotação, não compra: {row['reference_quote_qty_not_purchase_qty']}",
            f"- Teto custo para margem 45/50/55%: {brl(row['cost_ceiling_45_margin'])} / {brl(row['cost_ceiling_50_margin'])} / {brl(row['cost_ceiling_55_margin'])}",
            f"- Gate lead time: {row['lead_time_gate']['gate']} | {row['lead_time_gate']['note']}",
            f"- Próximo passo interno: {row['recommended_internal_next_step']}",
            '',
        ])
    lines.extend([
        '## O que não foi feito',
        '',
        '- Nenhum fornecedor foi contatado.',
        '- Nenhuma compra, PO ou reserva foi feita.',
        '- Nenhum write em Shopify, Tiny, preço, estoque, campanha, cliente ou banco de produção.',
        '- Nenhum envio externo e nenhum cron ativado.',
        '',
        '## Aprovação necessária para avançar',
        '',
        'Para enviar qualquer brief a fornecedor, Lucas/Júlio precisam aprovar destino, escopo, itens e quantidade de cotação. Compra continua sendo uma aprovação separada depois de custo, lead time e margem reais.',
    ])
    return '\n'.join(lines) + '\n'


def main() -> None:
    source = json.loads(SOURCE_JSON.read_text(encoding='utf-8'))
    rows = build_rows(source)
    groups = group_rows(rows)
    payload = {
        'generated_at': now_utc(),
        'scope': 'LK OS Weekly Quote Validation Preview read-only from Weekly Stock/SKU Action Plan',
        'read_only': True,
        'summary': summary(rows, groups, source),
        'quote_groups': groups,
        'rows': rows,
        'margin_targets': TARGET_MARGINS,
        'not_performed': ['supplier_contact', 'purchase_order', 'purchase', 'shopify_write', 'tiny_write', 'price_or_stock_change', 'campaign_send', 'cron_creation'],
        'limitations': ['No supplier availability, real cost or real lead time was fetched or inferred.', 'Quote quantity is only a reference for availability/cost validation, not a purchase quantity.'],
    }
    PUBLIC_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    write_csv(rows)
    md = build_md(payload)
    PUBLIC_MD.write_text(md, encoding='utf-8')
    BRAIN_DOC.write_text(md.replace('# LK OS Weekly Quote Validation Preview, read-only', '# LK OS, Weekly Quote Validation Preview read-only, 2026-05-11'), encoding='utf-8')
    print(json.dumps({'ok': True, 'rows': len(rows), 'groups': len(groups), 'json': str(PUBLIC_JSON), 'md': str(PUBLIC_MD), 'csv': str(PUBLIC_CSV), 'brain_doc': str(BRAIN_DOC)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
