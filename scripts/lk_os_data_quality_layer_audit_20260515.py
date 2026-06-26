#!/usr/bin/env python3
"""LK OS Data Quality Layer audit.

Read-only/local audit for Lucas/Hermes Brain. It inspects the private LK OS SQLite
operational spine and emits sanitized aggregate JSON/MD reports. It never prints
PII rows and never touches external systems.
"""
from __future__ import annotations

import json
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = Path("/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite")
REPORT_JSON = ROOT / "reports" / "lk-os-data-quality-layer-audit-2026-05-15.json"
REPORT_MD = ROOT / "areas" / "lk" / "rotinas" / "lk-os-data-quality-layer-audit-2026-05-15.md"

REQUIRED_MODEL = {
    "canonical_product": {
        "status": "partial",
        "current_tables": ["lk_products", "lk_product_variants"],
        "missing": ["canonical style/model id", "normalized brand/model/colorway", "curation status"],
    },
    "variant_size": {
        "status": "partial",
        "current_tables": ["lk_product_variants"],
        "missing": ["normalized BR size", "US M/W/EU conversion fields", "size confidence", "variant commercial state"],
    },
    "shopify_tiny_sku_map": {
        "status": "partial",
        "current_tables": ["lk_product_variants", "tiny_anchor_stock"],
        "missing": ["dedicated alias table", "Tiny product id/variation id confidence", "manual review state"],
    },
    "tiny_stock_truth": {
        "status": "partial",
        "current_tables": ["tiny_anchor_stock"],
        "missing": ["full variant-level Tiny snapshot", "free vs reserved stock", "deposit id/name", "snapshot history"],
    },
    "commercial_state": {
        "status": "missing",
        "current_tables": [],
        "missing": ["disponivel", "reservado", "sob_encomenda_br", "sob_encomenda_us", "em_transito", "recebido_ja_vendido", "recebido_livre", "divergente"],
    },
    "price_current_and_history": {
        "status": "partial",
        "current_tables": ["lk_product_variants", "lk_order_items", "sourcing_price_comparisons"],
        "missing": ["price snapshot table", "compare_at snapshot", "approved price decision ledger", "external price evidence TTL"],
    },
    "sales_history": {
        "status": "partial",
        "current_tables": ["lk_orders", "lk_order_items"],
        "missing": ["variant/model/day rollup table", "120d demand materialization", "channel/source reconciliation confidence"],
    },
    "approvals_events": {
        "status": "partial",
        "current_tables": ["final_approval_groups", "lk_os_entity_dictionary"],
        "missing": ["canonical approval/event ledger table", "superseded/no-op states", "result/learning links"],
    },
    "data_quality_flags": {
        "status": "missing",
        "current_tables": [],
        "missing": ["per-variant dq status", "blocking reason", "source freshness", "last verified at"],
    },
}


def q(cur: sqlite3.Cursor, sql: str, params=()):
    cur.execute(sql, params)
    return cur.fetchone()[0]


def table_exists(cur: sqlite3.Cursor, name: str) -> bool:
    cur.execute("select 1 from sqlite_master where type='table' and name=?", (name,))
    return cur.fetchone() is not None


def columns(cur: sqlite3.Cursor, table: str):
    cur.execute(f"pragma table_info({table})")
    return [dict(cid=r[0], name=r[1], type=r[2], notnull=r[3], default=r[4], pk=r[5]) for r in cur.fetchall()]


def pct(num: int | float, den: int | float) -> float:
    if not den:
        return 0.0
    return round(float(num) * 100.0 / float(den), 2)


def main() -> int:
    if not DB_PATH.exists():
        raise SystemExit(f"DB not found: {DB_PATH}")

    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    cur.execute("select name from sqlite_master where type='table' order by name")
    tables = [r[0] for r in cur.fetchall()]
    table_counts = {t: q(cur, f"select count(*) from {t}") for t in tables}
    schema = {t: columns(cur, t) for t in tables}

    metrics = {}
    if table_exists(cur, "lk_product_variants"):
        total = q(cur, "select count(*) from lk_product_variants")
        with_sku = q(cur, "select count(*) from lk_product_variants where coalesce(trim(sku),'') <> ''")
        with_price = q(cur, "select count(*) from lk_product_variants where price is not null and price > 0")
        with_inventory_item = q(cur, "select count(*) from lk_product_variants where coalesce(trim(inventory_item_id),'') <> ''")
        active = q(cur, "select count(*) from lk_product_variants where coalesce(is_active,0)=1")
        missing_product_join = q(cur, """
            select count(*)
            from lk_product_variants v
            left join lk_products p on p.product_id = v.product_id
            where p.product_id is null
        """)
        duplicate_skus = q(cur, """
            select count(*) from (
              select sku from lk_product_variants
              where coalesce(trim(sku),'') <> ''
              group by sku having count(*) > 1
            )
        """)
        metrics["variants"] = {
            "total": total,
            "active": active,
            "with_sku": with_sku,
            "with_sku_pct": pct(with_sku, total),
            "missing_sku": total - with_sku,
            "with_current_shopify_price": with_price,
            "with_current_shopify_price_pct": pct(with_price, total),
            "with_inventory_item_id": with_inventory_item,
            "missing_product_join": missing_product_join,
            "duplicate_sku_groups": duplicate_skus,
        }

    if table_exists(cur, "lk_order_items"):
        total_items = q(cur, "select count(*) from lk_order_items")
        with_sku_items = q(cur, "select count(*) from lk_order_items where coalesce(trim(sku),'') <> ''")
        with_variant_id = q(cur, "select count(*) from lk_order_items where coalesce(trim(variant_id),'') <> '' or coalesce(trim(source_variant_id),'') <> ''")
        missing_variant_join = q(cur, """
            select count(*)
            from lk_order_items oi
            left join lk_product_variants v
              on (v.variant_id = oi.variant_id or v.source_variant_id = oi.source_variant_id)
            where coalesce(oi.variant_id, oi.source_variant_id, '') <> ''
              and v.variant_id is null
        """)
        metrics["order_items"] = {
            "total": total_items,
            "with_sku": with_sku_items,
            "with_sku_pct": pct(with_sku_items, total_items),
            "with_variant_id_or_source_variant_id": with_variant_id,
            "with_variant_id_pct": pct(with_variant_id, total_items),
            "missing_variant_join_when_variant_id_present": missing_variant_join,
        }

    if table_exists(cur, "lk_orders"):
        total_orders = q(cur, "select count(*) from lk_orders")
        with_source = q(cur, "select count(*) from lk_orders where coalesce(trim(source_name),'') <> ''")
        with_tags = q(cur, "select count(*) from lk_orders where coalesce(trim(tags),'') <> ''")
        paid_like = q(cur, "select count(*) from lk_orders where lower(coalesce(financial_status,'')) in ('paid','partially_paid','partially_refunded')")
        metrics["orders"] = {
            "total": total_orders,
            "with_source_name": with_source,
            "with_source_name_pct": pct(with_source, total_orders),
            "with_tags": with_tags,
            "paid_like": paid_like,
        }

    if table_exists(cur, "tiny_anchor_stock"):
        total_tiny = q(cur, "select count(*) from tiny_anchor_stock")
        status_counts = {}
        cur.execute("select coalesce(status,'unknown') status, count(*) from tiny_anchor_stock group by 1 order by 2 desc")
        for status, count in cur.fetchall():
            status_counts[status] = count
        metrics["tiny_anchor_stock"] = {
            "total_anchor_rows": total_tiny,
            "status_counts": status_counts,
            "note": "Apenas anchor stock parcial; ainda não é snapshot full variant-level do Tiny.",
        }

    if table_exists(cur, "lk_os_sync_runs"):
        cur.execute("select source,status,started_at,finished_at,rows_customers,rows_orders,rows_order_items,rows_products,rows_variants,rows_rfm from lk_os_sync_runs order by started_at desc limit 5")
        metrics["sync_runs_recent"] = [
            {
                "source": r[0], "status": r[1], "started_at": r[2], "finished_at": r[3],
                "rows_customers": r[4], "rows_orders": r[5], "rows_order_items": r[6],
                "rows_products": r[7], "rows_variants": r[8], "rows_rfm": r[9],
            }
            for r in cur.fetchall()
        ]

    con.close()

    readiness = {
        "green": [
            "Shopify/Supabase operational spine exists locally with customers/orders/items/products/variants/RFM.",
            "Variant-level Shopify price/SKU/catalog fields are available for most variants.",
            "Reports can avoid PII and use aggregate counts from private SQLite.",
        ],
        "yellow": [
            "Tiny stock truth exists only as partial anchor stock, not full variant-level history.",
            "SKU mapping is present in variant rows but lacks a dedicated alias/confidence table.",
            "Sales history exists in order_items but demand rollups are not materialized as canonical tables.",
            "Approvals exist in scattered reports/groups, not one event ledger with result/learning links.",
        ],
        "red": [
            "Commercial state per variant is missing.",
            "Data quality flags per variant are missing.",
            "Price history/snapshots are missing; current Shopify price is available but not a history ledger.",
            "Reserved/free/encomenda/em_transito states are not represented as source-labeled facts.",
        ],
    }

    next_tables = [
        {
            "table": "lk_variant_quality_status",
            "purpose": "One row per Shopify variant/SKU/size with source-labeled readiness and blocking reasons.",
            "key_fields": ["variant_id", "source_variant_id", "sku", "normalized_size", "dq_status", "blocking_reason", "last_verified_at"],
            "mode": "local/materialized from read-only sources",
        },
        {
            "table": "lk_sku_alias_map",
            "purpose": "Canonical Shopify SKU to Tiny code/product/variation aliases with confidence and manual-review state.",
            "key_fields": ["shopify_variant_id", "shopify_sku", "tiny_product_id", "tiny_codigo", "match_confidence", "review_status"],
            "mode": "local/materialized + approval-gated correction queue",
        },
        {
            "table": "lk_tiny_stock_snapshots",
            "purpose": "Full Tiny stock truth by SKU/size/deposit, preserving free/reserved/physical counts over time.",
            "key_fields": ["snapshot_at", "deposit_name", "tiny_codigo", "sku", "size", "stock_free", "stock_reserved", "stock_physical"],
            "mode": "read-only sync; no Tiny writes",
        },
        {
            "table": "lk_variant_commercial_state",
            "purpose": "Business state per variant: available/reserved/encomenda/transit/sold/divergent with evidence.",
            "key_fields": ["variant_id", "sku", "commercial_state", "state_source", "confidence", "evidence_ref", "updated_at"],
            "mode": "derived preview first; human approval for uncertain states",
        },
        {
            "table": "lk_price_snapshots",
            "purpose": "Current and historical price/compare-at/cost/landed-price evidence separated by source.",
            "key_fields": ["captured_at", "variant_id", "sku", "source_label", "price_brl", "compare_at_brl", "cost_brl", "evidence_ref"],
            "mode": "read-only capture; price writes remain approval-gated",
        },
        {
            "table": "lk_variant_sales_rollups",
            "purpose": "Daily/weekly/120d demand by variant/model/size to feed Stock, CRO, Brand Mix and sourcing.",
            "key_fields": ["window", "variant_id", "sku", "units", "revenue", "orders", "last_sale_at", "source_label"],
            "mode": "derived from Shopify/Supabase order_items",
        },
        {
            "table": "lk_action_event_ledger",
            "purpose": "Unified Approval Manager / Learning Loop event table for recommendations, approvals, executions and lessons.",
            "key_fields": ["event_id", "area", "artifact", "status", "approval_text", "executed_at", "result", "learning_ref"],
            "mode": "local ledger; external writes need approval",
        },
    ]

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "read_only_local_sql_audit",
        "db_path": str(DB_PATH),
        "db_permissions_octal": oct(DB_PATH.stat().st_mode & 0o777),
        "table_counts": table_counts,
        "metrics": metrics,
        "required_model_audit": REQUIRED_MODEL,
        "readiness": readiness,
        "recommended_next_tables": next_tables,
        "non_actions": [
            "No external API call",
            "No Shopify/Tiny/Merchant/Klaviyo/Notion/WhatsApp write",
            "No cron/UI/worker created",
            "No PII exported in reports",
        ],
    }

    REPORT_JSON.parent.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    os.chmod(REPORT_JSON, 0o644)

    md = []
    md.append("# LK OS — Data Quality Layer / Modelo operacional por variante")
    md.append("")
    md.append("Status: `data_quality_layer_audit_ready`")
    md.append("Data: 2026-05-15")
    md.append("Modo: read-only/local SQL. Nenhuma API externa, write produtivo, cron, UI, worker, compra, contato ou envio executado.")
    md.append("")
    md.append("## Veredito")
    md.append("")
    md.append("A base local já cobre o esqueleto operacional Shopify/Supabase — clientes, pedidos, itens, produtos, variantes e RFM — mas ainda não atende completamente o PRD inicial porque falta transformar os dados em uma camada canônica por variante/tamanho com qualidade, estado comercial, estoque Tiny completo, histórico de preço e ledger único de ações/aprendizado.")
    md.append("")
    md.append("## Evidência atual sem PII")
    md.append("")
    md.append(f"- SQLite privado auditado: `{DB_PATH}` (`{oct(DB_PATH.stat().st_mode & 0o777)}`).")
    for t in ["lk_products", "lk_product_variants", "lk_orders", "lk_order_items", "lk_customers", "lk_customer_rfm", "tiny_anchor_stock"]:
        if t in table_counts:
            md.append(f"- `{t}`: {table_counts[t]} linhas.")
    v = metrics.get("variants", {})
    if v:
        md.append(f"- Variantes com SKU: {v['with_sku']}/{v['total']} ({v['with_sku_pct']}%).")
        md.append(f"- Variantes com preço Shopify atual: {v['with_current_shopify_price']}/{v['total']} ({v['with_current_shopify_price_pct']}%).")
        md.append(f"- Variantes sem join de produto: {v['missing_product_join']}.")
        md.append(f"- Grupos de SKU duplicado: {v['duplicate_sku_groups']}.")
    oi = metrics.get("order_items", {})
    if oi:
        md.append(f"- Itens de pedido com SKU: {oi['with_sku']}/{oi['total']} ({oi['with_sku_pct']}%).")
        md.append(f"- Itens de pedido com variant id/source_variant_id: {oi['with_variant_id_or_source_variant_id']}/{oi['total']} ({oi['with_variant_id_pct']}%).")
    tiny = metrics.get("tiny_anchor_stock", {})
    if tiny:
        md.append(f"- Tiny anchor stock parcial: {tiny['total_anchor_rows']} linhas; ainda não é snapshot completo por variante/tamanho/deposito.")
    md.append("")
    md.append("## Gap contra PRD inicial")
    md.append("")
    for name, spec in REQUIRED_MODEL.items():
        md.append(f"### {name}")
        md.append("")
        md.append(f"- Status: `{spec['status']}`")
        if spec["current_tables"]:
            md.append(f"- Tabelas atuais: {', '.join('`'+x+'`' for x in spec['current_tables'])}.")
        else:
            md.append("- Tabelas atuais: nenhuma tabela canônica dedicada.")
        md.append("- Falta:")
        for missing in spec["missing"]:
            md.append(f"  - {missing}.")
        md.append("")
    md.append("## Modelo canônico recomendado")
    md.append("")
    for tbl in next_tables:
        md.append(f"### `{tbl['table']}`")
        md.append("")
        md.append(f"- Função: {tbl['purpose']}")
        md.append(f"- Campos-chave: {', '.join('`'+x+'`' for x in tbl['key_fields'])}.")
        md.append(f"- Modo: {tbl['mode']}.")
        md.append("")
    md.append("## Sequência segura de implementação")
    md.append("")
    md.append("1. Criar somente tabelas/views locais derivadas em SQLite, sem tocar Shopify/Tiny/Notion/Merchant.")
    md.append("2. Materializar `lk_variant_quality_status` a partir das tabelas existentes.")
    md.append("3. Criar `lk_sku_alias_map` e marcar ambiguidades, sem corrigir SKUs automaticamente.")
    md.append("4. Planejar sync read-only completo Tiny para `lk_tiny_stock_snapshots` antes de qualquer decisão de estoque livre/reservado.")
    md.append("5. Só depois alimentar Pulso Comercial, CRO, Brand Mix, Content Engine e Pricing com essa camada.")
    md.append("")
    md.append("## Não executado")
    md.append("")
    for action in report["non_actions"]:
        md.append(f"- {action}.")
    md.append("")
    md.append("## Próximo bloco recomendado")
    md.append("")
    md.append("Implementar a primeira materialização local: `lk_variant_quality_status` + `lk_sku_alias_map` em modo SQLite/local, usando apenas dados já existentes, e gerar um relatório de quantos variants ficam `ready`, `needs_tiny_stock`, `needs_sku_alias`, `needs_price_history` ou `blocked_ambiguous`. Isso não autoriza writes externos.")
    md.append("")

    REPORT_MD.parent.mkdir(parents=True, exist_ok=True)
    REPORT_MD.write_text("\n".join(md), encoding="utf-8")
    os.chmod(REPORT_MD, 0o644)

    print(json.dumps({
        "status": "ok",
        "json": str(REPORT_JSON),
        "md": str(REPORT_MD),
        "tables": len(tables),
        "variants": metrics.get("variants", {}).get("total"),
        "missing_model_red": len(readiness["red"]),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
