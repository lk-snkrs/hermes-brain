#!/usr/bin/env python3
"""Materialize LK OS Data Quality Layer v0 in local SQLite.

Local/reversible only. Creates a private DB backup before writing derived tables.
No external calls and no PII export.
"""
from __future__ import annotations

import json
import os
import shutil
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = Path("/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite")
BACKUP_DIR = Path("/opt/data/hermes_bruno_ingest/local_sql/lk_os_backups")
REPORT_JSON = ROOT / "reports" / "lk-os-data-quality-layer-materialization-v0-2026-05-15.json"
REPORT_MD = ROOT / "areas" / "lk" / "rotinas" / "lk-os-data-quality-layer-materialization-v0-2026-05-15.md"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def q(cur: sqlite3.Cursor, sql: str, params=()):
    cur.execute(sql, params)
    return cur.fetchone()[0]


def main() -> int:
    if not DB_PATH.exists():
        raise SystemExit(f"DB not found: {DB_PATH}")

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(BACKUP_DIR, 0o700)
    backup_path = BACKUP_DIR / f"lk_os_phase5_before_data_quality_layer_v0_20260515.sqlite"
    if not backup_path.exists():
        shutil.copy2(DB_PATH, backup_path)
        os.chmod(backup_path, 0o600)

    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    generated_at = now_iso()

    cur.executescript(
        """
        drop table if exists lk_variant_quality_status;
        create table lk_variant_quality_status (
          variant_id text primary key,
          product_id text,
          source_variant_id text,
          source_product_id text,
          product_title text,
          variant_title text,
          sku text,
          normalized_size text,
          shopify_product_status text,
          shopify_is_active integer,
          has_sku integer,
          has_product_join integer,
          has_current_price integer,
          has_inventory_item_id integer,
          has_order_history integer,
          has_tiny_anchor_stock integer,
          sku_duplicate_group_size integer,
          dq_status text,
          blocking_reason text,
          source_labels text,
          last_verified_at text
        );

        drop table if exists lk_sku_alias_map;
        create table lk_sku_alias_map (
          alias_id text primary key,
          shopify_variant_id text,
          shopify_product_id text,
          source_variant_id text,
          shopify_sku text,
          product_title text,
          variant_title text,
          normalized_size text,
          tiny_anchor_sku text,
          tiny_anchor_status text,
          tiny_anchor_available_estimated_total real,
          tiny_anchor_match_count integer,
          match_confidence text,
          review_status text,
          notes text,
          last_verified_at text
        );
        """
    )

    # Materialize variant quality. This uses only existing local tables.
    cur.execute(
        """
        insert into lk_variant_quality_status (
          variant_id, product_id, source_variant_id, source_product_id, product_title, variant_title, sku,
          normalized_size, shopify_product_status, shopify_is_active, has_sku, has_product_join,
          has_current_price, has_inventory_item_id, has_order_history, has_tiny_anchor_stock,
          sku_duplicate_group_size, dq_status, blocking_reason, source_labels, last_verified_at
        )
        with sku_dupes as (
          select sku, count(*) as group_size
          from lk_product_variants
          where coalesce(trim(sku),'') <> ''
          group by sku
        ),
        order_hist as (
          select v.variant_id,
                 count(oi.item_id) as item_count
          from lk_product_variants v
          left join lk_order_items oi
            on (
              (coalesce(trim(oi.variant_id),'') <> '' and oi.variant_id = v.variant_id)
              or (coalesce(trim(oi.source_variant_id),'') <> '' and oi.source_variant_id = v.source_variant_id)
              or (coalesce(trim(oi.sku),'') <> '' and coalesce(trim(v.sku),'') <> '' and oi.sku = v.sku)
            )
          group by v.variant_id
        ),
        tiny as (
          select sku,
                 max(status) as status,
                 max(available_estimated_total) as available_estimated_total,
                 max(match_count) as match_count,
                 count(*) as anchor_rows
          from tiny_anchor_stock
          where coalesce(trim(sku),'') <> ''
          group by sku
        )
        select
          v.variant_id,
          v.product_id,
          v.source_variant_id,
          v.source_product_id,
          coalesce(v.product_title, p.title) as product_title,
          v.title as variant_title,
          v.sku,
          coalesce(nullif(trim(v.option1),''), nullif(trim(v.title),'')) as normalized_size,
          p.status as shopify_product_status,
          coalesce(v.is_active,0) as shopify_is_active,
          case when coalesce(trim(v.sku),'') <> '' then 1 else 0 end as has_sku,
          case when p.product_id is not null then 1 else 0 end as has_product_join,
          case when v.price is not null and v.price > 0 then 1 else 0 end as has_current_price,
          case when coalesce(trim(v.inventory_item_id),'') <> '' then 1 else 0 end as has_inventory_item_id,
          case when oh.item_count is not null and oh.item_count > 0 then 1 else 0 end as has_order_history,
          case when tiny.anchor_rows is not null and tiny.anchor_rows > 0 then 1 else 0 end as has_tiny_anchor_stock,
          coalesce(sd.group_size,0) as sku_duplicate_group_size,
          case
            when coalesce(trim(v.sku),'') = '' then 'blocked_missing_sku'
            when p.product_id is null then 'blocked_missing_product_join'
            when coalesce(sd.group_size,0) > 1 then 'needs_sku_alias_review'
            when v.price is null or v.price <= 0 then 'needs_current_price'
            when tiny.anchor_rows is null then 'needs_tiny_stock_truth'
            else 'ready_basic_variant_layer'
          end as dq_status,
          case
            when coalesce(trim(v.sku),'') = '' then 'Shopify variant has no SKU; cannot safely map Tiny/source/stock.'
            when p.product_id is null then 'Variant does not join to local product row.'
            when coalesce(sd.group_size,0) > 1 then 'SKU appears on multiple Shopify variants; needs alias/disambiguation.'
            when v.price is null or v.price <= 0 then 'Current Shopify variant price missing/zero in local spine.'
            when tiny.anchor_rows is null then 'No Tiny anchor stock row in current partial local stock table; full Tiny stock snapshot needed.'
            else 'Basic local layer ready; still needs full Tiny/free-reserved state before commercial action.'
          end as blocking_reason,
          'fact_shopify,derived_reconciliation' || case when tiny.anchor_rows is not null then ',fact_tiny_stock_partial' else '' end as source_labels,
          ? as last_verified_at
        from lk_product_variants v
        left join lk_products p on p.product_id = v.product_id
        left join sku_dupes sd on sd.sku = v.sku
        left join order_hist oh on oh.variant_id = v.variant_id
        left join tiny on tiny.sku = v.sku
        """,
        (generated_at,),
    )

    cur.execute(
        """
        insert into lk_sku_alias_map (
          alias_id, shopify_variant_id, shopify_product_id, source_variant_id, shopify_sku,
          product_title, variant_title, normalized_size, tiny_anchor_sku, tiny_anchor_status,
          tiny_anchor_available_estimated_total, tiny_anchor_match_count, match_confidence,
          review_status, notes, last_verified_at
        )
        with tiny as (
          select sku,
                 max(status) as status,
                 max(available_estimated_total) as available_estimated_total,
                 max(match_count) as match_count,
                 count(*) as anchor_rows
          from tiny_anchor_stock
          where coalesce(trim(sku),'') <> ''
          group by sku
        ),
        sku_dupes as (
          select sku, count(*) as group_size
          from lk_product_variants
          where coalesce(trim(sku),'') <> ''
          group by sku
        )
        select
          'shopify_variant:' || v.variant_id as alias_id,
          v.variant_id as shopify_variant_id,
          v.product_id as shopify_product_id,
          v.source_variant_id,
          v.sku as shopify_sku,
          coalesce(v.product_title, p.title) as product_title,
          v.title as variant_title,
          coalesce(nullif(trim(v.option1),''), nullif(trim(v.title),'')) as normalized_size,
          tiny.sku as tiny_anchor_sku,
          tiny.status as tiny_anchor_status,
          tiny.available_estimated_total as tiny_anchor_available_estimated_total,
          tiny.match_count as tiny_anchor_match_count,
          case
            when coalesce(trim(v.sku),'') = '' then 'none_missing_shopify_sku'
            when coalesce(sd.group_size,0) > 1 then 'low_duplicate_shopify_sku'
            when tiny.anchor_rows is not null then 'medium_tiny_anchor_exact_sku'
            else 'unknown_no_tiny_anchor_in_partial_table'
          end as match_confidence,
          case
            when coalesce(trim(v.sku),'') = '' then 'needs_shopify_sku_or_manual_mapping'
            when coalesce(sd.group_size,0) > 1 then 'needs_duplicate_sku_review'
            when tiny.anchor_rows is not null then 'anchor_mapped_partial_stock_only'
            else 'needs_full_tiny_lookup'
          end as review_status,
          case
            when coalesce(trim(v.sku),'') = '' then 'No SKU; do not source/price/stock-act from this variant.'
            when coalesce(sd.group_size,0) > 1 then 'Duplicate SKU group; use product/title/size/Tiny live evidence before action.'
            when tiny.anchor_rows is not null then 'Matched current partial Tiny anchor by exact SKU; still not full Tiny truth.'
            else 'No local Tiny anchor; next step is read-only full Tiny snapshot/lookup.'
          end as notes,
          ? as last_verified_at
        from lk_product_variants v
        left join lk_products p on p.product_id = v.product_id
        left join tiny on tiny.sku = v.sku
        left join sku_dupes sd on sd.sku = v.sku
        """,
        (generated_at,),
    )

    con.commit()

    status_counts = {}
    cur.execute("select dq_status, count(*) from lk_variant_quality_status group by dq_status order by count(*) desc")
    for status, count in cur.fetchall():
        status_counts[status] = count

    alias_counts = {}
    cur.execute("select review_status, count(*) from lk_sku_alias_map group by review_status order by count(*) desc")
    for status, count in cur.fetchall():
        alias_counts[status] = count

    source_label_counts = {}
    cur.execute("select source_labels, count(*) from lk_variant_quality_status group by source_labels order by count(*) desc")
    for labels, count in cur.fetchall():
        source_label_counts[labels] = count

    row_counts = {
        "lk_variant_quality_status": q(cur, "select count(*) from lk_variant_quality_status"),
        "lk_sku_alias_map": q(cur, "select count(*) from lk_sku_alias_map"),
    }

    con.close()

    report = {
        "generated_at": generated_at,
        "mode": "local_sql_materialization_only",
        "db_path": str(DB_PATH),
        "backup_path": str(backup_path),
        "backup_permissions_octal": oct(backup_path.stat().st_mode & 0o777),
        "tables_created_or_replaced": list(row_counts.keys()),
        "row_counts": row_counts,
        "dq_status_counts": status_counts,
        "sku_alias_review_status_counts": alias_counts,
        "source_label_counts": source_label_counts,
        "non_actions": [
            "No external API call",
            "No Shopify/Tiny/Merchant/Klaviyo/Notion/WhatsApp write",
            "No cron/UI/worker created",
            "No PII exported",
            "No purchase/contact/message/campaign",
        ],
        "rollback": "Restore the copied SQLite backup over the working DB if the derived-table write needs to be reverted.",
    }

    REPORT_JSON.parent.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    os.chmod(REPORT_JSON, 0o644)

    md = []
    md.append("# LK OS — Data Quality Layer v0 materializado")
    md.append("")
    md.append("Status: `local_materialization_complete`")
    md.append("Data: 2026-05-15")
    md.append("Modo: SQLite local/reversível. Nenhuma API externa ou write produtivo executado.")
    md.append("")
    md.append("## Veredito")
    md.append("")
    md.append("A primeira camada local do Data Quality Layer foi materializada com duas tabelas derivadas: `lk_variant_quality_status` e `lk_sku_alias_map`. Isso cria a base para o PRD voltar a operar por produto/variante/tamanho, sem ainda afirmar estoque livre ou estado comercial final.")
    md.append("")
    md.append("## Backup / rollback")
    md.append("")
    md.append(f"- Backup privado antes do write local: `{backup_path}`.")
    md.append(f"- Permissão do backup: `{oct(backup_path.stat().st_mode & 0o777)}`.")
    md.append("- Rollback: restaurar esse SQLite sobre o DB de trabalho se necessário.")
    md.append("")
    md.append("## Tabelas criadas")
    md.append("")
    for table, count in row_counts.items():
        md.append(f"- `{table}`: {count} linhas.")
    md.append("")
    md.append("## Status de qualidade por variante")
    md.append("")
    for status, count in status_counts.items():
        md.append(f"- `{status}`: {count} variants.")
    md.append("")
    md.append("## Status do mapa SKU/Alias")
    md.append("")
    for status, count in alias_counts.items():
        md.append(f"- `{status}`: {count} variants.")
    md.append("")
    md.append("## Leitura executiva")
    md.append("")
    md.append("- A maior lacuna prática continua sendo Tiny: a tabela atual `tiny_anchor_stock` é parcial, então a maior parte das variants fica em `needs_tiny_stock_truth` ou `needs_full_tiny_lookup`.")
    md.append("- Variants sem SKU ou com SKU duplicado já ficam bloqueadas/revisão antes de entrarem em sourcing, pricing, CRO ou conteúdo.")
    md.append("- A camada já permite que os próximos módulos não tratem Shopify inventory como verdade de estoque.")
    md.append("")
    md.append("## Próximo bloco seguro")
    md.append("")
    md.append("Criar o `lk_tiny_stock_snapshots` read-only completo por SKU/tamanho/depósito e depois recalcular `lk_variant_quality_status` para separar `ready_for_stock_decision`, `reserved_or_unclear`, `stockout_exact_ready`, `needs_manual_mapping` e `monitor`. Isso exige apenas consulta Tiny/Supabase/Shopify read-only; qualquer correção de SKU/estoque/preço continua approval-gated.")
    md.append("")
    md.append("## Não executado")
    md.append("")
    for action in report["non_actions"]:
        md.append(f"- {action}.")
    md.append("")

    REPORT_MD.parent.mkdir(parents=True, exist_ok=True)
    REPORT_MD.write_text("\n".join(md), encoding="utf-8")
    os.chmod(REPORT_MD, 0o644)

    print(json.dumps({
        "status": "ok",
        "json": str(REPORT_JSON),
        "md": str(REPORT_MD),
        "backup": str(backup_path),
        "row_counts": row_counts,
        "dq_status_counts": status_counts,
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
