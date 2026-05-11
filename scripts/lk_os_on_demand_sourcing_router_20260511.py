#!/usr/bin/env python3
"""LK OS on-demand sourcing router, read-only.

Creates a decision-scoped sourcing router from the Approval Decision Log. This
is not a GOAT/Droper/StockX/KicksDev full-sync and it does not call external
marketplaces. It prepares the safe structure that can later be filled only for
approved quote/sourcing decisions.
"""
from __future__ import annotations

import csv
import json
import pathlib
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE_JSON = ROOT / 'reports/lk-os-approval-decision-log-router-2026-05-04_2026-05-10.json'
OUT_JSON = ROOT / 'reports/lk-os-on-demand-sourcing-router-2026-05-04_2026-05-10.json'
OUT_CSV = ROOT / 'reports/lk-os-on-demand-sourcing-router-2026-05-04_2026-05-10.csv'
OUT_MD = ROOT / 'reports/lk-os-on-demand-sourcing-router-2026-05-04_2026-05-10.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/on-demand-sourcing-router-readonly-2026-05-11.md'

EXTERNAL_SOURCES = ['GOAT', 'Droper', 'StockX', 'KicksDev']
SOURCE_LABELS = ['fact_shopify', 'fact_tiny_stock', 'derived_reconciliation', 'manual_approval_pending']


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def brl(value: float | int | None) -> str:
    if value is None:
        return 'n/d'
    return 'R$ ' + f'{float(value):,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def route_source_check(row: dict[str, Any]) -> dict[str, Any]:
    current_status = row.get('current_status')
    route = row.get('route')
    default_choice = row.get('default_safe_choice')

    if current_status == 'needs_data':
        return {
            'sourcing_router_status': 'blocked_needs_data',
            'eligible_for_external_lookup': False,
            'lookup_trigger_required': 'resolve_sku_tiny_data_first',
            'approval_gate': 'data_resolution_before_any_sourcing',
            'recommended_source_sequence': [],
            'reason': 'Linha precisa resolver dados antes de GOAT/Droper/StockX/KicksDev ou fornecedor.',
        }

    if route == 'hold_or_bundle_with_p0_decision':
        return {
            'sourcing_router_status': 'optional_hold_until_p0_bundle',
            'eligible_for_external_lookup': False,
            'lookup_trigger_required': 'lucas_julio_decide_bundle_with_p0',
            'approval_gate': 'manual_bundle_decision_required',
            'recommended_source_sequence': EXTERNAL_SOURCES,
            'reason': 'P1 opcional; só pesquisar mercado externo se for agrupado com uma cotação P0 aprovada.',
        }

    if default_choice == 'approve_quote_only':
        return {
            'sourcing_router_status': 'ready_for_manual_quote_approval_then_on_demand_lookup',
            'eligible_for_external_lookup': False,
            'lookup_trigger_required': 'approve_quote_only_or_explicit_sourcing_research',
            'approval_gate': 'Lucas/Júlio approval required before external lookup/contact',
            'recommended_source_sequence': EXTERNAL_SOURCES,
            'reason': 'P0 pronto para decisão; pesquisa externa só deve ocorrer no escopo desta decisão, não em sync permanente.',
        }

    return {
        'sourcing_router_status': 'hold_manual_review',
        'eligible_for_external_lookup': False,
        'lookup_trigger_required': 'manual_review',
        'approval_gate': 'manual_review_required',
        'recommended_source_sequence': [],
        'reason': 'Status não promove sourcing automático.',
    }


def build_queue(source: dict[str, Any]) -> list[dict[str, Any]]:
    queue: list[dict[str, Any]] = []
    for row in source.get('decision_log') or []:
        routing = route_source_check(row)
        queue.append({
            'sourcing_request_id': row.get('decision_id', '').replace('LK-QUOTE', 'LK-SOURCING'),
            'source_decision_id': row.get('decision_id'),
            'created_at': now_utc(),
            'business_area': 'LK Sneakers',
            'family': row.get('family'),
            'decision_type': 'on_demand_sourcing_research_preview',
            'current_approval_status': row.get('current_status'),
            'approval_route': row.get('route'),
            'sourcing_router_status': routing['sourcing_router_status'],
            'eligible_for_external_lookup_now': routing['eligible_for_external_lookup'],
            'lookup_trigger_required': routing['lookup_trigger_required'],
            'approval_gate': routing['approval_gate'],
            'recommended_source_sequence': routing['recommended_source_sequence'],
            'source_labels': SOURCE_LABELS,
            'reference_quote_qty_not_purchase_qty': row.get('reference_quote_qty_not_purchase_qty'),
            'revenue_signal_fact_shopify': row.get('revenue_signal_fact_shopify'),
            'size_normalization_required': 'StockX/GOAT listings must identify US Men vs US Women and normalize to LK/BR/EU before comparing.',
            'persist_only_decision_scoped_summary': True,
            'do_not_full_sync_external_prices': True,
            'future_result_fields_if_approved': {
                'source_checked': None,
                'query_timestamp': None,
                'product_sku_size_queried': None,
                'external_price_raw': None,
                'size_system_raw': None,
                'normalized_lk_size': None,
                'estimated_landed_cost_brl': None,
                'availability': None,
                'confidence': None,
                'cheapest_viable_source': None,
                'expires_at': None,
            },
            'not_authorized_by_this_row': [
                'external_marketplace_call',
                'supplier_contact',
                'purchase',
                'purchase_order',
                'reservation',
                'shopify_write',
                'tiny_write',
                'price_or_stock_change',
                'campaign_or_customer_send',
                'cron_or_full_sync',
            ],
            'reason': routing['reason'],
        })
    return queue


def summarize(queue: list[dict[str, Any]], source: dict[str, Any]) -> dict[str, Any]:
    counts: dict[str, int] = {}
    for row in queue:
        key = row['sourcing_router_status']
        counts[key] = counts.get(key, 0) + 1
    return {
        'source_decision_log': str(SOURCE_JSON.relative_to(ROOT)),
        'week': ((source.get('summary') or {}).get('week') or {}),
        'rows': len(queue),
        'status_counts': counts,
        'ready_after_manual_approval_count': counts.get('ready_for_manual_quote_approval_then_on_demand_lookup', 0),
        'optional_bundle_count': counts.get('optional_hold_until_p0_bundle', 0),
        'blocked_needs_data_count': counts.get('blocked_needs_data', 0),
        'reference_quote_qty_not_purchase_qty': sum(int(r.get('reference_quote_qty_not_purchase_qty') or 0) for r in queue),
        'revenue_signal_fact_shopify': round(sum(float(r.get('revenue_signal_fact_shopify') or 0) for r in queue), 2),
    }


def write_csv(queue: list[dict[str, Any]]) -> None:
    fields = [
        'sourcing_request_id', 'source_decision_id', 'family', 'current_approval_status',
        'approval_route', 'sourcing_router_status', 'eligible_for_external_lookup_now',
        'lookup_trigger_required', 'approval_gate', 'reference_quote_qty_not_purchase_qty',
        'revenue_signal_fact_shopify', 'do_not_full_sync_external_prices', 'reason'
    ]
    with OUT_CSV.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(queue)


def build_md(payload: dict[str, Any]) -> str:
    s = payload['summary']
    lines = [
        '# LK OS On-demand Sourcing Router, read-only',
        '',
        f"Generated at: `{payload['generated_at']}`",
        f"Week: `{s['week'].get('start_date')}` to `{s['week'].get('end_date')}`",
        '',
        '## Veredito operacional',
        '',
        'O próximo bloco seguro foi materializar o router de sourcing sob demanda. Isto prepara o caminho para GOAT/Droper/StockX/KicksDev apenas quando houver decisão comercial específica, sem criar full-sync de preços externos.',
        '',
        '## Resumo',
        '',
        f"- Linhas de sourcing roteadas: {s['rows']}",
        f"- Prontas somente depois de aprovação manual: {s['ready_after_manual_approval_count']}",
        f"- Opcionais para agrupar com P0: {s['optional_bundle_count']}",
        f"- Bloqueadas por dados: {s['blocked_needs_data_count']}",
        f"- Quantidade referência de cotação, não compra: {s['reference_quote_qty_not_purchase_qty']}",
        f"- Sinal de receita Shopify: {brl(s['revenue_signal_fact_shopify'])}",
        '',
        '## Regra principal',
        '',
        '- GOAT, Droper, StockX e KicksDev são ferramentas on-demand para compra/reposição/subida específica.',
        '- Não são tabelas permanentes de preço externo dentro do SQL local da LK.',
        '- Se algum resultado externo for persistido no futuro, deve ser resumo por decisão: item consultado, fonte, timestamp, custo estimado, confiança, cheapest viable source e validade.',
        '- Para StockX/GOAT, sempre identificar US Men vs US Women e normalizar para LK/BR/EU antes de comparar tamanho.',
        '',
        '## Fila roteada',
        '',
    ]
    for row in payload['sourcing_router']:
        lines.extend([
            f"### {row['sourcing_request_id']} | {row['family']}",
            f"- Status: `{row['sourcing_router_status']}`",
            f"- Lookup externo agora: `{row['eligible_for_external_lookup_now']}`",
            f"- Gatilho exigido: `{row['lookup_trigger_required']}`",
            f"- Gate de aprovação: {row['approval_gate']}",
            f"- Fontes futuras, se aprovado: {', '.join(row['recommended_source_sequence']) if row['recommended_source_sequence'] else 'n/d'}",
            f"- Receita Shopify sinal: {brl(row['revenue_signal_fact_shopify'])}",
            f"- Motivo: {row['reason']}",
            '',
        ])
    lines.extend([
        '## O que não foi feito',
        '',
        '- Nenhuma chamada a GOAT, Droper, StockX ou KicksDev.',
        '- Nenhum full-sync de preço externo.',
        '- Nenhum fornecedor foi contatado.',
        '- Nenhuma compra, PO, reserva ou pagamento.',
        '- Nenhum Shopify/Tiny write, alteração de preço/estoque/produto, campanha, cliente, banco de produção ou cron.',
        '',
        '## Próximo passo seguro',
        '',
        'Quando Lucas/Júlio aprovar uma família específica, preencher somente aquela decisão com pesquisa externa sob demanda e devolver cheapest viable option com custo estimado, lead time, margem e validade. Ainda assim, compra/PO continua sendo aprovação separada.',
    ])
    return '\n'.join(lines) + '\n'


def main() -> None:
    source = json.loads(SOURCE_JSON.read_text(encoding='utf-8'))
    queue = build_queue(source)
    payload = {
        'generated_at': now_utc(),
        'scope': 'LK OS on-demand sourcing router, read-only; no external marketplace calls and no price full-sync',
        'read_only': True,
        'summary': summarize(queue, source),
        'external_sources_defined_as_on_demand_only': EXTERNAL_SOURCES,
        'sourcing_router': queue,
        'not_performed': [
            'goat_lookup', 'droper_lookup', 'stockx_lookup', 'kicksdev_lookup',
            'external_price_full_sync', 'supplier_contact', 'purchase', 'purchase_order',
            'reservation', 'shopify_write', 'tiny_write', 'price_or_stock_change',
            'campaign_or_customer_send', 'production_db_write', 'cron_creation'
        ],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    write_csv(queue)
    md = build_md(payload)
    OUT_MD.write_text(md, encoding='utf-8')
    BRAIN_DOC.write_text(md.replace('# LK OS On-demand Sourcing Router, read-only', '# LK OS, On-demand Sourcing Router read-only, 2026-05-11'), encoding='utf-8')
    print(json.dumps({'ok': True, 'rows': len(queue), 'json': str(OUT_JSON), 'md': str(OUT_MD), 'csv': str(OUT_CSV), 'brain_doc': str(BRAIN_DOC)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
