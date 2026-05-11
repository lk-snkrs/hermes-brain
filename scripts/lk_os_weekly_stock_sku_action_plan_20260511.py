#!/usr/bin/env python3
"""LK OS Weekly Stock/SKU Action Plan, read-only.

Transforms the Weekly CEO Review stock risks into a sanitized operational queue.
No Shopify/Tiny writes, supplier contact, purchase order, price change, campaign,
cron or external send is performed.
"""
from __future__ import annotations

import csv
import json
import pathlib
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
WEEKLY_JSON = ROOT / 'reports/lk-os-weekly-ceo-review-2026-05-04_2026-05-10.json'
PUBLIC_JSON = ROOT / 'reports/lk-os-weekly-stock-sku-action-plan-2026-05-04_2026-05-10.json'
PUBLIC_CSV = ROOT / 'reports/lk-os-weekly-stock-sku-action-plan-2026-05-04_2026-05-10.csv'
PUBLIC_MD = ROOT / 'reports/lk-os-weekly-stock-sku-action-plan-2026-05-04_2026-05-10.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/weekly-stock-sku-action-plan-readonly-2026-05-11.md'
OFFICIAL_DEPOSIT = 'LK | CONTROLE ESTOQUE'


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def brl(value: float | int | None) -> str:
    if value is None:
        return 'n/d'
    return 'R$ ' + f'{float(value):,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def stock_value(value: float | int | None) -> str:
    if value is None:
        return 'n/d'
    return str(value)


def safe_float(value: Any) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except Exception:
        return None


def classify_priority(row: dict[str, Any]) -> tuple[str, str, str, int]:
    risk = row.get('stock_risk') or 'unknown'
    qty = int(safe_float(row.get('sold_qty_fact_shopify')) or 0)
    revenue = safe_float(row.get('line_revenue_estimate')) or 0.0
    quality = row.get('chosen_match_quality') or 'unknown'
    saldo = safe_float((row.get('official_deposit') or {}).get('saldo'))
    if risk == 'ruptura' and qty >= 2:
        return ('P0', 'ruptura com venda repetida', 'cotação/sourcing interno prioritário; validar fornecedor, lead time e margem antes de qualquer compra', 4000 + qty * 100 + int(revenue / 100))
    if risk == 'ruptura':
        return ('P1', 'ruptura com venda unitária', 'validar estoque Tiny atual e lead time; cotar se fizer sentido comercial', 3000 + qty * 100 + int(revenue / 100))
    if risk == 'baixo_estoque_vs_venda_da_semana':
        return ('P1', 'baixo estoque contra venda da semana', 'checar cobertura, reserva e reposição preventiva; sem compra sem aprovação', 2500 + qty * 100 + int(revenue / 100))
    if risk == 'unknown' or quality == 'no_safe_candidate' or saldo is None:
        return ('P1', 'estoque desconhecido ou SKU sem match seguro', 'resolver SKU/Tiny antes de sourcing; não comprar nem anunciar como disponível', 2300 + qty * 100 + int(revenue / 100))
    return ('P2', 'monitoramento', 'não agir agora; manter em observação semanal', 1000 + qty * 100 + int(revenue / 100))


def action_status(priority: str, reason: str) -> str:
    if 'SKU' in reason or 'desconhecido' in reason:
        return 'sku_resolution_first'
    if priority == 'P0':
        return 'quote_preview_candidate'
    if priority == 'P1':
        return 'validate_before_quote'
    return 'monitor_only'


def build_shopify_revenue_map(weekly: dict[str, Any]) -> dict[tuple[str, str, str], float]:
    products = (((weekly.get('sources') or {}).get('shopify') or {}).get('top_products') or [])
    out: dict[tuple[str, str, str], float] = {}
    for item in products:
        key = (
            item.get('product_title') or '',
            item.get('sku') or '',
            item.get('size_or_variant') or '',
        )
        out[key] = round(safe_float(item.get('line_revenue_estimate')) or 0.0, 2)
    return out


def build_queue(weekly: dict[str, Any]) -> list[dict[str, Any]]:
    checks = (((weekly.get('sources') or {}).get('tiny_stock') or {}).get('checks') or [])
    revenue_map = build_shopify_revenue_map(weekly)
    queue: list[dict[str, Any]] = []
    for row in checks:
        revenue = revenue_map.get((row.get('product_title') or '', row.get('sku') or '', row.get('size_or_variant') or ''), 0.0)
        row_for_priority = dict(row)
        row_for_priority['line_revenue_estimate'] = revenue
        priority, reason, recommended_action, score = classify_priority(row_for_priority)
        if priority not in {'P0', 'P1'}:
            continue
        deposit = row.get('official_deposit') or {}
        saldo = safe_float(deposit.get('saldo'))
        sold_qty = int(safe_float(row.get('sold_qty_fact_shopify')) or 0)
        item = {
            'priority': priority,
            'reason': reason,
            'action_status': action_status(priority, reason),
            'recommended_action_preview': recommended_action,
            'product_title': row.get('product_title') or 'Produto sem título',
            'sku': row.get('sku') or 'sem_sku',
            'size_or_variant': row.get('size_or_variant') or 'sem tamanho informado',
            'sold_qty_fact_shopify': sold_qty,
            'line_revenue_estimate_fact_shopify': revenue,
            'tiny_deposit': deposit.get('deposit') or OFFICIAL_DEPOSIT,
            'tiny_saldo_fact_tiny_stock': saldo,
            'stock_risk': row.get('stock_risk') or 'unknown',
            'match_quality': row.get('chosen_match_quality') or 'unknown',
            'source_labels': ['fact_shopify', 'fact_tiny_stock'],
            'confidence': 'high' if row.get('chosen_match_quality') == 'exact_norm_sku' and saldo is not None else 'needs_sku_or_stock_validation',
            'score': score,
            'not_authorized_actions': ['purchase_order', 'supplier_contact', 'shopify_write', 'tiny_write', 'price_change', 'campaign_or_external_send'],
        }
        queue.append(item)
    return sorted(queue, key=lambda x: (x['priority'], -x['score'], x['product_title']))


def summarize(queue: list[dict[str, Any]], weekly: dict[str, Any]) -> dict[str, Any]:
    counts: dict[str, int] = {}
    statuses: dict[str, int] = {}
    for item in queue:
        counts[item['priority']] = counts.get(item['priority'], 0) + 1
        statuses[item['action_status']] = statuses.get(item['action_status'], 0) + 1
    revenue_at_risk = round(sum(float(item['line_revenue_estimate_fact_shopify'] or 0) for item in queue), 2)
    return {
        'queue_rows': len(queue),
        'priority_counts': counts,
        'action_status_counts': statuses,
        'revenue_signal_fact_shopify': revenue_at_risk,
        'week': weekly.get('week') or {},
        'source_weekly_review': str(WEEKLY_JSON.relative_to(ROOT)),
    }


def write_csv(queue: list[dict[str, Any]]) -> None:
    fields = [
        'priority', 'reason', 'action_status', 'product_title', 'sku', 'size_or_variant',
        'sold_qty_fact_shopify', 'line_revenue_estimate_fact_shopify', 'tiny_saldo_fact_tiny_stock',
        'stock_risk', 'match_quality', 'confidence', 'recommended_action_preview'
    ]
    with PUBLIC_CSV.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        for item in queue:
            writer.writerow(item)


def build_md(payload: dict[str, Any]) -> str:
    summary = payload['summary']
    queue = payload['queue']
    lines = [
        '# LK OS Weekly Stock/SKU Action Plan, read-only',
        '',
        f"Generated at: `{payload['generated_at']}`",
        f"Week: `{summary['week'].get('start_date')}` to `{summary['week'].get('end_date')}`",
        '',
        '## Escopo',
        '',
        'Fila operacional sanitizada que transforma riscos P0/P1 do Weekly CEO Review em próximas ações internas de estoque/SKU. É preview read-only.',
        '',
        '## Resumo',
        '',
        f"- Linhas na fila: {summary['queue_rows']}",
        f"- P0: {summary['priority_counts'].get('P0', 0)}",
        f"- P1: {summary['priority_counts'].get('P1', 0)}",
        f"- Sinal de receita Shopify nas linhas: {brl(summary['revenue_signal_fact_shopify'])}",
        '- Fonte de venda: `fact_shopify`',
        '- Fonte de estoque: `fact_tiny_stock`',
        '- Depósito Tiny: `LK | CONTROLE ESTOQUE`',
        '',
        '## Top fila operacional',
        '',
    ]
    for idx, item in enumerate(queue[:15], 1):
        lines.extend([
            f"### {idx}. {item['product_title']} | {item['size_or_variant']}",
            f"- Prioridade: {item['priority']} | {item['reason']}",
            f"- SKU: `{item['sku']}`",
            f"- Venda Shopify: {item['sold_qty_fact_shopify']} un, {brl(item['line_revenue_estimate_fact_shopify'])}",
            f"- Tiny `{item['tiny_deposit']}`: `{stock_value(item['tiny_saldo_fact_tiny_stock'])}`",
            f"- Risco: `{item['stock_risk']}` | match: `{item['match_quality']}` | confiança: `{item['confidence']}`",
            f"- Próxima ação preview: {item['recommended_action_preview']}",
            '',
        ])
    lines.extend([
        '## O que não foi feito',
        '',
        '- Nenhuma compra ou PO.',
        '- Nenhum contato com fornecedor.',
        '- Nenhum write em Shopify, Tiny, preço, estoque, campanha ou cliente.',
        '- Nenhum envio externo e nenhum cron ativado.',
        '',
        '## Próximo passo seguro',
        '',
        'Para P0, validar fornecedor, lead time e teto de custo/margem antes de cotação real. Para P1 desconhecido, resolver SKU/Tiny primeiro. Qualquer compra ou contato externo precisa de aprovação explícita.',
    ])
    return '\n'.join(lines) + '\n'


def main() -> None:
    weekly = json.loads(WEEKLY_JSON.read_text(encoding='utf-8'))
    queue = build_queue(weekly)
    payload = {
        'generated_at': now_utc(),
        'scope': 'LK OS Weekly Stock/SKU Action Plan read-only from Weekly CEO Review P0/P1 stock risks',
        'read_only': True,
        'source_labels': ['fact_shopify', 'fact_tiny_stock'],
        'summary': summarize(queue, weekly),
        'queue': queue,
        'not_performed': ['purchase_order', 'supplier_contact', 'shopify_write', 'tiny_write', 'price_or_stock_change', 'campaign_send', 'cron_creation'],
        'limitations': ['Uses Weekly CEO Review stock sample for sold/top SKUs only, not full catalog audit.', 'Unknown rows require SKU/Tiny validation before sourcing.'],
    }
    PUBLIC_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    write_csv(queue)
    md = build_md(payload)
    PUBLIC_MD.write_text(md, encoding='utf-8')
    BRAIN_DOC.write_text(md.replace('# LK OS Weekly Stock/SKU Action Plan, read-only', '# LK OS, Weekly Stock/SKU Action Plan read-only, 2026-05-11'), encoding='utf-8')
    print(json.dumps({'ok': True, 'queue_rows': len(queue), 'json': str(PUBLIC_JSON), 'md': str(PUBLIC_MD), 'csv': str(PUBLIC_CSV), 'brain_doc': str(BRAIN_DOC)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
