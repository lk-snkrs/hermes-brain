#!/usr/bin/env python3
"""Monitor LK GMC P2A finalization, then build LK OS stockout/recompra/sourcing validation queue.

Runs read-only/local. It does not send WhatsApp, contact suppliers, buy, write Notion,
write Shopify/Tiny/Merchant, or call Droper/StockX/GOAT. Step 2 uses existing local
LK OS SQLite + Brain artifacts only, labels evidence, and outputs an approval/validation
queue for the corrected flow.
"""
from __future__ import annotations

import json, sqlite3, time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/opt/data/hermes_bruno_ingest/hermes-brain')
REPORT = ROOT / 'reports/lk-gmc-2026-05-13-p2a-finalize-remaining-online.json'
PROGRESS_GLOB = '/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-13-p2a-finalize-remaining-online-progress-*.jsonl'
DB = Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
OUT_JSON = ROOT / 'reports/lk-os-stockout-recompra-sourcing-validation-queue-2026-05-13.json'
OUT_MD = ROOT / 'reports/lk-os-stockout-recompra-sourcing-validation-queue-2026-05-13.md'
POLL_SECONDS = 60
MAX_WAIT_SECONDS = 6 * 60 * 60
FINAL_STATUSES = {'apply_verified', 'apply_completed_needs_review', 'apply_stopped_on_patch_failure'}
NOT_PERFORMED = [
    'whatsapp_message_read', 'whatsapp_send', 'supplier_contact', 'purchase', 'reservation',
    'notion_write', 'shopify_write', 'tiny_write', 'merchant_write_beyond_existing_p2a_process',
    'droper_lookup', 'stockx_lookup', 'goat_lookup', 'klaviyo_send_or_schedule', 'customer_contact'
]


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def load_report():
    if not REPORT.exists():
        return None
    return json.loads(REPORT.read_text(encoding='utf-8'))


def progress_counts():
    files = sorted(Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots').glob('lk-gmc-2026-05-13-p2a-finalize-remaining-online-progress-*.jsonl'), key=lambda p: p.stat().st_mtime, reverse=True)
    if not files:
        return {}, None
    c = Counter()
    last = None
    for line in files[0].read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        try:
            item = json.loads(line)
            c[item.get('execution_status')] += 1
            last = item
        except Exception:
            c['parse_error'] += 1
    return dict(c), str(files[0])


def wait_for_gmc():
    start = time.time()
    last_print = 0
    while time.time() - start < MAX_WAIT_SECONDS:
        rep = load_report()
        status = rep.get('status') if rep else None
        counts, progress_path = progress_counts()
        if status in FINAL_STATUSES:
            return rep, counts, progress_path, 'final_report_status'
        # If process disappeared, accept latest report for consolidation even if not final.
        pid_exists = Path('/proc/16334').exists()
        if rep and not pid_exists:
            return rep, counts, progress_path, 'process_exited_with_latest_report'
        now = time.time()
        if now - last_print >= 600:
            print(json.dumps({'phase': 'waiting_gmc_p2a', 'status': status, 'progress_counts': counts, 'progress_path': progress_path, 'elapsed_seconds': int(now-start)}, ensure_ascii=False), flush=True)
            last_print = now
        time.sleep(POLL_SECONDS)
    rep = load_report() or {'status': 'timeout_waiting_for_gmc_report', 'summary': {}}
    counts, progress_path = progress_counts()
    return rep, counts, progress_path, 'monitor_timeout'


def build_queue(gmc_report, progress_counts_dict, progress_path, completion_reason):
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    # Recent paid order items with local Shopify inventory <= 0 and optional Tiny stock evidence.
    # This is a validation queue, not a purchase/contact queue.
    rows = cur.execute('''
        WITH recent AS (
          SELECT
            oi.title,
            oi.variant_title,
            oi.sku,
            oi.quantity,
            oi.line_total,
            oi.order_id,
            o.order_number,
            o.order_created_at,
            o.financial_status,
            o.cancelled_at,
            v.inventory_quantity AS shopify_inventory_quantity,
            p.handle,
            p.status AS product_status,
            COALESCE(t.available_estimated_total, NULL) AS tiny_available_estimated_total,
            t.status AS tiny_status,
            t.match_count AS tiny_match_count
          FROM lk_order_items oi
          JOIN lk_orders o ON o.order_id = oi.order_id
          LEFT JOIN lk_product_variants v ON v.source_variant_id = oi.source_variant_id OR (oi.sku IS NOT NULL AND oi.sku != '' AND v.sku = oi.sku)
          LEFT JOIN lk_products p ON p.product_id = v.product_id
          LEFT JOIN tiny_anchor_stock t ON t.sku = oi.sku
          WHERE o.cancelled_at IS NULL
            AND COALESCE(o.financial_status, '') NOT IN ('refunded','voided')
            AND oi.sku IS NOT NULL AND oi.sku != ''
            AND date(substr(o.order_created_at,1,10)) >= date('now', '-120 day')
        ), grouped AS (
          SELECT
            title, variant_title, sku, handle, product_status,
            MAX(order_created_at) AS last_order_at,
            COUNT(DISTINCT order_id) AS recent_orders,
            SUM(quantity) AS recent_units,
            ROUND(SUM(line_total), 2) AS recent_revenue_fact_shopify,
            MIN(COALESCE(shopify_inventory_quantity, 999999)) AS min_shopify_inventory_signal,
            MIN(COALESCE(tiny_available_estimated_total, 999999)) AS tiny_available_estimated_total,
            MAX(tiny_status) AS tiny_status,
            MAX(tiny_match_count) AS tiny_match_count
          FROM recent
          GROUP BY title, variant_title, sku, handle, product_status
        )
        SELECT * FROM grouped
        WHERE (min_shopify_inventory_signal <= 0 OR tiny_available_estimated_total <= 0)
        ORDER BY recent_revenue_fact_shopify DESC, recent_units DESC, last_order_at DESC
        LIMIT 25
    ''').fetchall()

    queue = []
    for r in rows:
        tiny_stock = r['tiny_available_estimated_total']
        tiny_confirmed_zero = tiny_stock is not None and tiny_stock != 999999 and float(tiny_stock) <= 0
        shopify_zero_signal = r['min_shopify_inventory_signal'] is not None and int(r['min_shopify_inventory_signal']) <= 0
        if tiny_confirmed_zero:
            validation_status = 'candidate_stockout_confirmed_by_local_tiny_anchor_snapshot'
            next_safe = 'prepare_droper_first_lookup_preview_only_if_lucas_approves_external_marketplace_lookup'
        elif shopify_zero_signal:
            validation_status = 'candidate_stockout_signal_shopify_inventory_needs_tiny_live_confirmation'
            next_safe = 'tiny_live_stock_confirmation_before_any_marketplace_or_supplier_step'
        else:
            validation_status = 'monitor_only'
            next_safe = 'no_action'
        queue.append({
            'product_title': r['title'],
            'variant_size_or_title': r['variant_title'],
            'sku': r['sku'],
            'handle': r['handle'],
            'last_order_at': r['last_order_at'],
            'recent_orders_120d_fact_shopify': r['recent_orders'],
            'recent_units_120d_fact_shopify': r['recent_units'],
            'recent_revenue_120d_fact_shopify': r['recent_revenue_fact_shopify'],
            'shopify_inventory_signal': r['min_shopify_inventory_signal'],
            'tiny_available_estimated_total_fact_tiny_stock_snapshot': None if tiny_stock == 999999 else tiny_stock,
            'validation_status': validation_status,
            'next_safe_action': next_safe,
            'blocked_without_inline_approval': ['droper_lookup','stockx_lookup','goat_lookup','supplier_contact','purchase','notion_write','shopify_write','tiny_write']
        })

    payload = {
        'generated_at': utc_now(),
        'status': 'step1_gmc_consolidated_step2_validation_queue_ready',
        'step1_gmc': {
            'completion_reason': completion_reason,
            'report_status': gmc_report.get('status'),
            'summary': gmc_report.get('summary') or {},
            'progress_counts': progress_counts_dict,
            'progress_path': progress_path,
            'report_path': str(REPORT),
        },
        'step2_queue': {
            'scope': 'stockout/recompra/sourcing validation queue from local Shopify order/items + local stock evidence; no external calls',
            'rows': len(queue),
            'source_labels': ['fact_shopify', 'fact_local_sql', 'fact_tiny_stock_snapshot_when_present', 'derived_reconciliation'],
            'items': queue,
        },
        'not_performed': NOT_PERFORMED,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    lines = [
        '# LK OS — Stockout/Recompra/Sourcing Validation Queue, 2026-05-13', '',
        f'Generated at: `{payload["generated_at"]}`', '',
        '## Step 1 — GMC P2A', '',
        f'- Status report: `{payload["step1_gmc"]["report_status"]}`',
        f'- Completion reason: `{completion_reason}`',
        f'- Progress counts: `{progress_counts_dict}`', '',
        '## Step 2 — Fila curta de validação', '',
        'Esta fila usa dados locais Shopify/Data Spine e snapshot Tiny quando existe. Não consulta Droper/StockX/GOAT e não cria tarefa Notion. É a fila segura para decidir o que validar/acionar depois.', '',
    ]
    for i, item in enumerate(queue[:10], 1):
        lines += [
            f'### {i}. {item["product_title"]} — {item["variant_size_or_title"]}',
            f'- SKU: `{item["sku"]}`',
            f'- Última venda/pedido: `{item["last_order_at"]}`',
            f'- 120d Shopify: {item["recent_units_120d_fact_shopify"]} un · R$ {item["recent_revenue_120d_fact_shopify"]}',
            f'- Sinal Shopify estoque: `{item["shopify_inventory_signal"]}`',
            f'- Tiny snapshot: `{item["tiny_available_estimated_total_fact_tiny_stock_snapshot"]}`',
            f'- Status: `{item["validation_status"]}`',
            f'- Próximo seguro: `{item["next_safe_action"]}`',
            ''
        ]
    lines += ['## Não executado', ''] + [f'- {x}' for x in NOT_PERFORMED]
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return payload


def main():
    gmc_report, counts, progress_path, reason = wait_for_gmc()
    payload = build_queue(gmc_report, counts, progress_path, reason)
    s = payload['step1_gmc'].get('summary') or {}
    print('LK OS — passos 1 e 2 concluídos/localizados')
    print(f"GMC P2A status: {payload['step1_gmc']['report_status']}")
    print(f"GMC patched/progress: {payload['step1_gmc']['progress_counts']}")
    print(f"Fila step2 gerada: {payload['step2_queue']['rows']} candidatos")
    for i, item in enumerate(payload['step2_queue']['items'][:5], 1):
        print(f"{i}. {item['product_title']} — {item['variant_size_or_title']} | SKU {item['sku']} | status {item['validation_status']} | próximo {item['next_safe_action']}")
    print('Não executado: WhatsApp read/send, fornecedor, compra, Notion, Shopify/Tiny/Merchant novo write, Droper/StockX/GOAT.')
    print(f'Relatórios: {OUT_MD} | {OUT_JSON}')

if __name__ == '__main__':
    main()
