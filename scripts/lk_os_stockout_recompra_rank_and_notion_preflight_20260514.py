#!/usr/bin/env python3
"""LK OS stockout/recompra ranking + Notion/Júlio pattern preflight.

Local/read-only. Uses LK OS SQLite only. Does not consult Droper/StockX/GOAT,
read/send WhatsApp, contact suppliers, buy/reserve, write Notion, or mutate
Shopify/Tiny/Merchant.

Important data-quality rule: sales are aggregated BEFORE joining Tiny/variant rows so
shared model SKUs do not duplicate revenue/units across sizes.
"""
from __future__ import annotations

import json, sqlite3, math, re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/opt/data/hermes_bruno_ingest/hermes-brain')
DB = Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
OUT_JSON = ROOT / 'reports/lk-os-stockout-recompra-ranking-notion-preflight-2026-05-14.json'
OUT_MD = ROOT / 'reports/lk-os-stockout-recompra-ranking-notion-preflight-2026-05-14.md'
OUT_ROUTINE = ROOT / 'areas/lk/rotinas/lk-os-stockout-recompra-ranking-notion-preflight-2026-05-14.md'

NOT_PERFORMED = [
    'droper_lookup', 'stockx_lookup', 'goat_lookup', 'whatsapp_read', 'whatsapp_send',
    'supplier_contact', 'purchase', 'reservation', 'payment', 'notion_write',
    'shopify_write', 'tiny_write', 'merchant_write', 'campaign_or_customer_contact'
]

PATTERN = {
    'pattern_name': 'LK Compras / Notion/Júlio existing flow',
    'source': 'learned from LK Compras Signal Queue + Lucas correction',
    'flow': [
        'purchase_request',
        'supplier_responses',
        'choose_cheapest_viable_or_closer_to_sao_paulo_when_delta_is_small',
        'human_purchase_and_logistics',
        'notion_purchase_log'
    ],
    'important_correction': 'Do not invent a generic Notion task template. Mirror the existing LK Compras/Notion flow and vocabulary.',
}


def now(): return datetime.now(timezone.utc).isoformat()

def nfloat(x):
    try: return float(x or 0)
    except Exception: return 0.0

def nint(x):
    try: return int(x or 0)
    except Exception: return 0

def norm_size(x):
    s = (x or '').strip().upper().replace(',', '.')
    if not s: return ''
    # prefer BR/EU numeric sizes; accept 34, 34.5, 10.5, OS/UNICO labels
    m = re.search(r'(?<!\d)([1-4]\d(?:\.5)?|[5-9](?:\.5)?|1[0-5](?:\.5)?)(?!\d)', s)
    if m: return m.group(1).replace('.0','')
    if any(tok in s for tok in ['ÚNICO','UNICO','U','OS','ONE SIZE']): return 'UNICO'
    return s


def score_row(r):
    revenue = nfloat(r['recent_revenue_120d_fact_shopify'])
    units = nfloat(r['recent_units_120d_fact_shopify'])
    orders = nfloat(r['recent_orders_120d_fact_shopify'])
    tiny_zero = bool(r['tiny_confirmed_zero'])
    tiny_exact = bool(r['tiny_exact_size_zero'])
    sku_unique = bool(r['sku_unique_in_shopify_variants'])
    shopify_zero = bool(r['shopify_zero_signal'])
    active = (r['product_status'] or '').lower() == 'active'
    sku_clear = bool((r['sku'] or '').strip())
    size_clear = bool((r['variant_size_or_title'] or '').strip())
    score = 0
    score += min(40, math.log10(max(revenue, 1)) * 10)
    score += min(20, units * 2)
    score += min(10, orders * 2)
    score += 25 if tiny_zero else 0
    score += 15 if tiny_exact else 0
    score += 8 if shopify_zero else 0
    score += 5 if active else 0
    score += 3 if sku_unique else 0
    score += 2 if sku_clear else 0
    score += 2 if size_clear else 0
    return round(score, 2)


def main():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    tables = {r[0] for r in cur.execute("select name from sqlite_master where type='table'")}
    missing = sorted(set(['lk_orders','lk_order_items','lk_product_variants','lk_products']) - tables)
    if missing: raise SystemExit(f'Missing required tables: {missing}')
    tiny_exists = 'tiny_anchor_stock' in tables

    # Aggregate sales first: no Tiny/variant joins here, avoiding duplication from shared SKUs.
    sales_rows = cur.execute('''
        SELECT
          oi.title AS product_title,
          oi.variant_title AS variant_size_or_title,
          oi.sku,
          oi.source_variant_id,
          MAX(o.order_created_at) AS last_order_at,
          COUNT(DISTINCT oi.order_id) AS recent_orders_120d_fact_shopify,
          SUM(oi.quantity) AS recent_units_120d_fact_shopify,
          ROUND(SUM(oi.line_total), 2) AS recent_revenue_120d_fact_shopify
        FROM lk_order_items oi
        JOIN lk_orders o ON o.order_id = oi.order_id
        WHERE o.cancelled_at IS NULL
          AND COALESCE(o.financial_status, '') NOT IN ('refunded','voided')
          AND oi.sku IS NOT NULL AND oi.sku != ''
          AND date(substr(o.order_created_at,1,10)) >= date('now', '-120 day')
        GROUP BY oi.title, oi.variant_title, oi.sku, oi.source_variant_id
    ''').fetchall()

    # Preload variant/product and Tiny indexes.
    variants_by_source = {}
    variants_by_sku = {}
    for v in cur.execute('SELECT * FROM lk_product_variants').fetchall():
        if v['source_variant_id']: variants_by_source.setdefault(str(v['source_variant_id']), []).append(v)
        if v['sku']: variants_by_sku.setdefault(str(v['sku']), []).append(v)
    products_by_id = {str(p['product_id']): p for p in cur.execute('SELECT * FROM lk_products').fetchall()}

    tiny_by_sku = {}
    if tiny_exists:
        for t in cur.execute('SELECT * FROM tiny_anchor_stock').fetchall():
            if t['sku']: tiny_by_sku.setdefault(str(t['sku']), []).append(t)

    items = []
    sanity_counts = {
        'sales_groups_120d_with_sku': len(sales_rows),
        'candidate_rows': 0,
        'tiny_confirmed_zero_any_size': 0,
        'tiny_exact_size_zero': 0,
        'tiny_zero_but_size_ambiguous_or_mismatch': 0,
        'shopify_zero_needs_tiny_confirmation': 0,
        'shared_sku_across_multiple_shopify_variants': 0,
        'active_products': 0,
    }

    for r in sales_rows:
        sku = str(r['sku'])
        variant_size_norm = norm_size(r['variant_size_or_title'])
        v_matches = variants_by_source.get(str(r['source_variant_id']), []) if r['source_variant_id'] else []
        if not v_matches:
            v_matches = variants_by_sku.get(sku, [])
        sku_variant_count = len(variants_by_sku.get(sku, []))
        invs = [nint(v['inventory_quantity']) for v in v_matches if v['inventory_quantity'] is not None]
        shopify_inventory = min(invs) if invs else None
        shopify_zero = shopify_inventory is not None and shopify_inventory <= 0
        product = None
        if v_matches:
            product = products_by_id.get(str(v_matches[0]['product_id']))
        product_status = product['status'] if product else None
        handle = product['handle'] if product else None
        vendor = product['vendor'] if product else None
        product_type = product['product_type'] if product else None

        tiny_matches = tiny_by_sku.get(sku, [])
        tiny_zero_matches = [t for t in tiny_matches if nfloat(t['available_estimated_total']) <= 0]
        exact_size_zero = [t for t in tiny_zero_matches if norm_size(t['size']) == variant_size_norm and variant_size_norm]
        tiny_any_zero = bool(tiny_zero_matches)
        tiny_exact_zero = bool(exact_size_zero)
        chosen_tiny = exact_size_zero[0] if exact_size_zero else (tiny_zero_matches[0] if tiny_zero_matches else (tiny_matches[0] if tiny_matches else None))
        tiny_available = chosen_tiny['available_estimated_total'] if chosen_tiny else None
        tiny_match_count = len(tiny_matches) if tiny_matches else None
        tiny_size = chosen_tiny['size'] if chosen_tiny else None
        tiny_status = chosen_tiny['status'] if chosen_tiny else None
        tiny_anchor_product = chosen_tiny['anchor_product'] if chosen_tiny else None

        if not (shopify_zero or tiny_any_zero):
            continue
        if tiny_exact_zero:
            status = 'tiny_zero_exact_size_ready_for_droper_preview_after_gmc'
        elif tiny_any_zero:
            status = 'tiny_zero_but_size_ambiguous_or_mismatch_needs_manual_sanity_before_droper'
        else:
            status = 'shopify_zero_needs_tiny_live_confirmation_after_gmc'

        item = {
            'rank': None,
            'product_title': r['product_title'],
            'variant_size_or_title': r['variant_size_or_title'],
            'variant_size_normalized': variant_size_norm,
            'sku': sku,
            'handle': handle,
            'vendor': vendor,
            'product_type': product_type,
            'product_status': product_status,
            'last_order_at': r['last_order_at'],
            'recent_orders_120d_fact_shopify': r['recent_orders_120d_fact_shopify'],
            'recent_units_120d_fact_shopify': r['recent_units_120d_fact_shopify'],
            'recent_revenue_120d_fact_shopify': r['recent_revenue_120d_fact_shopify'],
            'shopify_inventory_signal': shopify_inventory,
            'sku_variant_count_shopify': sku_variant_count,
            'sku_unique_in_shopify_variants': sku_variant_count == 1,
            'tiny_available_estimated_total_fact_tiny_stock_snapshot': tiny_available,
            'tiny_match_count_for_sku': tiny_match_count,
            'tiny_status': tiny_status,
            'tiny_anchor_product': tiny_anchor_product,
            'tiny_size': tiny_size,
            'tiny_size_normalized': norm_size(tiny_size),
            'tiny_confirmed_zero': tiny_any_zero,
            'tiny_exact_size_zero': tiny_exact_zero,
            'shopify_zero_signal': shopify_zero,
            'sanity_status': status,
            'notion_julio_preview_fields_pattern_matched': {
                'tipo': 'pedido_de_recompra_por_stockout',
                'origem': 'fact_shopify + fact_tiny_stock_snapshot/local_sql',
                'produto': r['product_title'],
                'tamanho': r['variant_size_or_title'],
                'sku': sku,
                'demanda_4_meses': f"{r['recent_units_120d_fact_shopify']} un / R$ {r['recent_revenue_120d_fact_shopify']}",
                'evidencia_stockout': 'Tiny zero no mesmo tamanho' if tiny_exact_zero else ('Tiny zero no SKU, mas tamanho ambíguo/mismatch' if tiny_any_zero else 'Sinal Shopify zero; confirmar Tiny'),
                'fluxo_compra': 'Droper primeiro; se não houver, StockX/GOAT; escolher menor preço viável ou fonte mais perto de SP quando delta pequeno; compra humana; log Notion',
                'campos_a_preencher_apos_lookup_aprovado': ['fonte', 'link', 'preco_produto', 'frete', 'prazo', 'proximidade_sp', 'caveat_tamanho', 'decisao_humana'],
            },
            'approval_required_before': ['droper_lookup','stockx_lookup','goat_lookup','supplier_contact','purchase','notion_write','whatsapp_send'],
        }
        item['ranking_score'] = score_row(item)
        items.append(item)
        sanity_counts['candidate_rows'] += 1
        sanity_counts['tiny_confirmed_zero_any_size'] += int(tiny_any_zero)
        sanity_counts['tiny_exact_size_zero'] += int(tiny_exact_zero)
        sanity_counts['tiny_zero_but_size_ambiguous_or_mismatch'] += int(tiny_any_zero and not tiny_exact_zero)
        sanity_counts['shopify_zero_needs_tiny_confirmation'] += int((not tiny_any_zero) and shopify_zero)
        sanity_counts['shared_sku_across_multiple_shopify_variants'] += int(sku_variant_count > 1)
        sanity_counts['active_products'] += int((product_status or '').lower() == 'active')

    items.sort(key=lambda x: (x['ranking_score'], x['recent_revenue_120d_fact_shopify'] or 0, x['recent_units_120d_fact_shopify'] or 0), reverse=True)
    for i, item in enumerate(items, 1): item['rank'] = i

    payload = {
        'generated_at': now(),
        'status': 'ranking_and_notion_pattern_preflight_ready_v2_deduped',
        'window': 'last_120_days_approx_4_months',
        'source_labels': ['fact_shopify','fact_local_sql','fact_tiny_stock_snapshot_when_present','derived_reconciliation','manual_pattern_lucas_correction'],
        'pattern_fidelity': PATTERN,
        'sanity_counts': sanity_counts,
        'ranking_heuristic': {
            'sales_aggregated_before_tiny_join_to_avoid_duplicate_revenue': True,
            'demand_value_log_revenue_max_40': True,
            'units_max_20': True,
            'orders_max_10': True,
            'tiny_zero_any_size_bonus_25': True,
            'tiny_exact_size_bonus_15': True,
            'shopify_zero_bonus_8': True,
            'active_product_bonus_5': True,
            'unique_sku_bonus_3': True,
            'sku_and_size_clarity_bonus_4': True,
        },
        'items': items,
        'top_18_candidates': items[:18],
        'not_performed': NOT_PERFORMED,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    lines = [
        '# LK OS — Ranking stockout/recompra + preflight Notion/Júlio', '',
        f'Generated at: `{payload["generated_at"]}`',
        'Status: `ranking_and_notion_pattern_preflight_ready_v2_deduped`', '',
        '## Veredito', '',
        'Preflight paralelo concluído em modo local/read-only. A janela usada é 120 dias (~4 meses), como Lucas aprovou. O item 2 foi ajustado para espelhar o padrão existente LK Compras → Júlio/Notion, sem inventar fluxo novo.', '',
        'Correção de qualidade aplicada: vendas foram agregadas antes de cruzar com Tiny/variants para não duplicar receita/unidades quando um SKU de modelo aparece em múltiplos tamanhos.', '',
        '## Padrão aprendido para item 2', '',
        '- Pedido de compra / recompra nasce de demanda concreta e stockout.',
        '- Coleta respostas/disponibilidade/preço/logística.',
        '- Decisão humana escolhe menor preço viável ou fonte mais perto de São Paulo quando a diferença for pequena.',
        '- Compra/logística continuam humanas.',
        '- Notion é log/registro da compra depois; Hermes não escreve sem aprovação.', '',
        '## Sanity check Tiny/local', '',
    ]
    for k,v in sanity_counts.items(): lines.append(f'- {k}: {v}')
    lines += ['', '## Top candidatos — preview sem PII', '']
    for item in items[:18]:
        lines += [
            f'### {item["rank"]}. {item["product_title"]} — {item["variant_size_or_title"]}',
            f'- SKU: `{item["sku"]}` · sku_variant_count: `{item["sku_variant_count_shopify"]}`',
            f'- Score: `{item["ranking_score"]}`',
            f'- Última venda: `{item["last_order_at"]}`',
            f'- Demanda 4 meses Shopify: {item["recent_units_120d_fact_shopify"]} un · R$ {item["recent_revenue_120d_fact_shopify"]}',
            f'- Estoque Shopify sinal: `{item["shopify_inventory_signal"]}`',
            f'- Tiny snapshot: `{item["tiny_available_estimated_total_fact_tiny_stock_snapshot"]}` · tiny_size `{item["tiny_size"]}` · tiny_match_count_sku `{item["tiny_match_count_for_sku"]}` · status `{item["tiny_status"]}`',
            f'- Sanity: `{item["sanity_status"]}`',
            '- Preview Júlio/Notion padrão: `pedido_de_recompra_por_stockout` → Droper primeiro → StockX/GOAT fallback → decisão humana preço/logística → log Notion.',
            ''
        ]
    lines += ['## Não executado', ''] + [f'- {x}' for x in NOT_PERFORMED]
    text='\n'.join(lines)+'\n'
    OUT_MD.write_text(text, encoding='utf-8')
    OUT_ROUTINE.write_text(text, encoding='utf-8')
    print(json.dumps({'wrote_json':str(OUT_JSON),'wrote_md':str(OUT_MD),'wrote_routine':str(OUT_ROUTINE),'sanity_counts':sanity_counts,'top_count':len(items[:18])}, ensure_ascii=False))

if __name__ == '__main__':
    main()
