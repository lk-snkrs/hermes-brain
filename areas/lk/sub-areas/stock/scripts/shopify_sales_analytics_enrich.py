#!/usr/bin/env python3
"""Enrich Shopify Sales OS SQLite for operational analytics.

Creates local read-only-derived dimensions/views for questions such as:
- category share (roupa/calçado/acessório) by channel;
- brand share;
- model/family ranking within a brand;
- paid/active sales filtering.

No Shopify/Tiny writes. This script only reads the local Sales OS DB and writes
local derived tables/views/reports.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "data" / "shopify_sales_os.db"
DEFAULT_REPORT = ROOT / "data/shopify_sales_analytics_readiness.json"
DEFAULT_OVERRIDES = ROOT / "data/shopify_sales_category_overrides.json"
HERMES_CLI_RUN = Path("/opt/data/home/.local/bin/hermes-cli-run")
API_VERSION = os.environ.get("SHOPIFY_API_VERSION", "2024-01")

CLOTHING_RE = re.compile(
    r"\b(camiseta|cal[cç]a|jaqueta|shorts?|top|vestido|saia|blusa|moletom|hoodie|regata|body|legging|bermuda|casaco|camisa|suti[aã]|cueca|pul[oô]ver|cropped|su[eé]ter|cardigan|polo|trouser|pants|jacket|shirt|tee|apparel)\b",
    re.I,
)
FOOTWEAR_RE = re.compile(
    r"\b(t[eê]nis|tenis|slide|crocs|sneaker|sapatilha|bota|sand[aá]lia|sapato|clog|loafer|mule|samba|vomero|9060|204l|530|550|shox|dunk|air force|air max|moon shoe|mind 00[12]|mexico 66|onitsuka|jordan|dockside|moc toe|tokyo mj|s[eé]zane x new balance)\b",
    re.I,
)
ACCESSORY_RE = re.compile(
    r"\b(acess[oó]rios?|lip|spray|kit|bolsa|case|[oó]culos|chaveiro|keychain|garrafa|limpeza|repel|blush|peptide|bon[eé]|meias?|meia|luvas?|espelho|pingente|colecion[aá]ve(?:l|is)|brinquedos?|figures?|toy|cleaning|cleaner|manuten[cç][aã]o|bag|cap|hat|socks|wallet|cinto)\b",
    re.I,
)
KIDS_RE = re.compile(r"\b(kids?|infantil|crian[cç]a|baby|toddler|gs|ps|td)\b", re.I)
SERVICE_RE = re.compile(r"\b(frete|cr[eé]dito|credito|shipping)\b", re.I)
COLLAB_RE = re.compile(r"\bx\b|jacquemus|travis scott|skims|loewe|versace|aim[eé] leon dore|aime leon dore|masp", re.I)

MODEL_PATTERNS: list[tuple[str, str]] = [
    ("Nike Moon Shoe", r"moon shoe"),
    ("Nike Mind", r"mind 00[12]|\bmind\b"),
    ("Nike Vomero", r"vomero"),
    ("Nike Dunk", r"\bdunk\b"),
    ("Nike Air Force", r"air force"),
    ("Nike Air Max", r"air max"),
    ("Nike Shox", r"\bshox\b"),
    ("New Balance 9060", r"\b9060\b|u9060|pc9060"),
    ("New Balance 204L", r"\b204l\b|u204l"),
    ("New Balance 530", r"\b530\b"),
    ("New Balance 550", r"\b550\b"),
    ("Onitsuka Mexico 66", r"mexic[oó] 66|mexico 66|m[ée]xico 66"),
    ("Adidas Samba", r"\bsamba\b"),
    ("Adidas SL 72", r"sl 72"),
    ("Jordan 1", r"jordan 1|air jordan 1|\baj1\b"),
    ("Lululemon Define", r"define"),
    ("Rhode Lip", r"lip|peptide"),
    ("Jason Markk", r"jason markk|repel|essential kit"),
]

BRAND_ALIASES = [
    ("Nike", r"\bnike\b|jacquemus x nike|nike x skims"),
    ("Jordan", r"\bjordan\b|air jordan|travis scott"),
    ("New Balance", r"new balance|\bnb-"),
    ("Onitsuka Tiger", r"onitsuka|mexico 66|m[ée]xico 66"),
    ("Adidas", r"\badidas\b|samba og|sl 72"),
    ("Alo Yoga", r"alo yoga"),
    ("Lululemon", r"lululemon"),
    ("Rhode", r"\brhode\b|peptide lip|pocket blush"),
    ("Jason Markk", r"jason markk"),
    ("Pace", r"\bpace\b"),
    ("Nude Project", r"nude project"),
    ("Saint Studio", r"saint studio"),
    ("Jacquemus", r"jacquemus"),
]

QUESTION_CAPABILITIES = [
    ("units_model_period", "Quantas unidades de um modelo venderam em X dias/meses?", "yes"),
    ("orders_model_period", "Quantos pedidos continham um modelo?", "yes"),
    ("revenue_model_period", "Qual faturamento de um modelo?", "yes"),
    ("avg_ticket_model", "Qual ticket médio dos pedidos com um modelo?", "yes"),
    ("size_mix_model", "Qual tamanho mais vendeu de um modelo?", "yes"),
    ("sku_rank_model", "Qual SKU mais vendido de um modelo?", "yes"),
    ("brand_rank_revenue", "Qual marca mais vendeu por faturamento?", "yes"),
    ("brand_rank_units", "Qual marca mais vendeu por unidades?", "yes"),
    ("top_products_revenue", "Qual ranking de produtos por faturamento?", "yes"),
    ("top_products_units", "Qual ranking de produtos por unidades?", "yes"),
    ("top_site_product", "Qual produto mais vendido no site?", "yes"),
    ("top_store_product", "Qual produto mais vendido na loja física?", "yes"),
    ("brand_site_store_share", "Qual share site vs loja por marca?", "yes"),
    ("model_site_store_share", "Qual share site vs loja por modelo?", "yes"),
    ("category_share_channel", "Quanto % de um canal foi roupa/calçado/acessório?", "yes_with_shopify_product_type_tags_fallback_heuristic"),
    ("nike_share", "Qual share de Nike no faturamento?", "yes_with_brand_rule"),
    ("nike_family_rank", "Dentro de Nike, qual família mais vendeu?", "yes_with_family_rule"),
    ("refunds_by_product", "Qual produto teve mais refund?", "yes"),
    ("expired_demand", "Qual demanda expirou por produto/marca?", "yes"),
    ("paid_vs_refunded", "Qual mix pago/reembolsado/expirado?", "yes"),
    ("weekly_best_day", "Qual dia/semana/mês vendeu mais?", "yes"),
    ("growth_decline", "Qual produto acelerou/caiu contra período anterior?", "yes"),
    ("cross_sell", "Quais produtos vendem juntos?", "yes"),
    ("multi_item_orders", "Quais marcas geram pedidos multi-item?", "yes"),
    ("price_realized", "Qual preço médio realizado por produto/SKU?", "yes"),
    ("audience_kids", "Quanto kids/infantil vendeu?", "heuristic"),
    ("collab_share", "Quanto collab vendeu?", "heuristic"),
    ("color_share", "Qual cor mais vendeu?", "partial_title_heuristic"),
    ("official_product_type", "Categoria oficial Shopify product_type/tags", "yes_read_only_product_enrichment"),
    ("gross_margin", "Margem por produto", "missing_cost_data"),
]



def shopify_store() -> str:
    store = (os.environ.get("SHOPIFY_STORE_URL") or os.environ.get("SHOPIFY_STORE") or os.environ.get("SHOPIFY_SHOP_NAME") or "").replace("https://", "").replace("http://", "").strip("/")
    if store and not store.endswith(".myshopify.com") and "." not in store:
        store += ".myshopify.com"
    return store


def shopify_token() -> str:
    return os.environ.get("SHOPIFY_ACCESS_TOKEN") or os.environ.get("SHOPIFY_ADMIN_TOKEN") or os.environ.get("SHOPIFY_API_TOKEN") or ""


def shopify_graphql(query: str, variables: dict[str, Any]) -> dict[str, Any]:
    store = shopify_store()
    token = shopify_token()
    if not store or not token:
        raise RuntimeError("missing_shopify_credentials")
    req = urllib.request.Request(
        f"https://{store}/admin/api/{API_VERSION}/graphql.json",
        data=json.dumps({"query": query, "variables": variables}).encode(),
        method="POST",
        headers={"X-Shopify-Access-Token": token, "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=90) as resp:
        payload = json.loads(resp.read().decode())
    if payload.get("errors"):
        raise RuntimeError("shopify_graphql_error:" + json.dumps(payload["errors"], ensure_ascii=False)[:1000])
    return payload.get("data") or {}


def chunked(values: list[str], size: int) -> list[list[str]]:
    return [values[i:i + size] for i in range(0, len(values), size)]


def parse_tags(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v).strip() for v in value if str(v).strip()]
    text = str(value).strip()
    if not text:
        return []
    try:
        parsed = json.loads(text)
        if isinstance(parsed, list):
            return [str(v).strip() for v in parsed if str(v).strip()]
    except Exception:
        pass
    return [v.strip() for v in text.split(",") if v.strip()]


def classify_category_from_official(product_type: str, tags: list[str]) -> tuple[str | None, str | None, float | None]:
    blob = f"{product_type} {' '.join(tags)}"
    if not blob.strip():
        return None, None, None
    if SERVICE_RE.search(blob):
        return "outros", "shopify_product_type_tags_v1_service", 0.99
    if FOOTWEAR_RE.search(blob):
        return "calcado", "shopify_product_type_tags_v1", 0.97
    if CLOTHING_RE.search(blob):
        return "roupa", "shopify_product_type_tags_v1", 0.95
    if ACCESSORY_RE.search(blob):
        return "acessorio", "shopify_product_type_tags_v1", 0.94
    return None, None, None


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def norm(text: Any) -> str:
    return str(text or "").strip()


def make_key(row: sqlite3.Row) -> str:
    product_id = norm(row["product_id"])
    variant_id = norm(row["variant_id"])
    sku = norm(row["sku"])
    title = norm(row["product_title"])
    if product_id or variant_id:
        return f"pid:{product_id}|vid:{variant_id}|sku:{sku}"
    # Keep original unicode casing here. SQLite lower() is ASCII-centric, so
    # using lower() in the view can break joins for titles like "TÊNIS".
    return f"title:{title}|sku:{sku}"


def brand_group(vendor: str, title: str, sku: str) -> str:
    blob = f"{vendor} {title} {sku}".lower()
    for brand, pattern in BRAND_ALIASES:
        if re.search(pattern, blob, re.I):
            return brand
    return vendor or "Unknown"


def model_family(vendor: str, title: str, sku: str) -> str:
    blob = f"{vendor} {title} {sku}".lower()
    for family, pattern in MODEL_PATTERNS:
        if re.search(pattern, blob, re.I):
            return family
    # fallback: brand + first meaningful token after brand when possible
    return brand_group(vendor, title, sku)


def classify_category(vendor: str, title: str, sku: str) -> tuple[str, str, float]:
    blob = f"{vendor} {title} {sku}"
    is_service = bool(SERVICE_RE.search(blob))
    is_clothing = bool(CLOTHING_RE.search(blob))
    is_footwear = bool(FOOTWEAR_RE.search(blob))
    is_accessory = bool(ACCESSORY_RE.search(blob))
    if is_service:
        return "outros", "service_non_product_v1", 0.99
    if is_footwear:
        return "calcado", "heuristic_title_sku_vendor_v1", 0.88
    if is_clothing and not is_accessory:
        return "roupa", "heuristic_title_sku_vendor_v1", 0.82
    if is_accessory and not is_clothing:
        return "acessorio", "heuristic_title_sku_vendor_v1", 0.80
    if is_clothing and is_accessory:
        return "roupa", "heuristic_title_sku_vendor_v1_ambiguous", 0.60
    return "outros", "heuristic_title_sku_vendor_v1_unknown", 0.35


def audience(title: str, sku: str) -> str:
    return "kids" if KIDS_RE.search(f"{title} {sku}") else "adult_or_unclassified"


def channel_group(source_name: str) -> str:
    s = (source_name or "").lower()
    if s == "pos":
        return "loja_fisica"
    if s == "web":
        return "site"
    if s == "shopify_draft_order":
        return "draft_order"
    if s.isdigit():
        return "app_numeric_source"
    return s or "unknown"


def init_schema(con: sqlite3.Connection) -> None:
    con.executescript(
        """
        CREATE TABLE IF NOT EXISTS shopify_sales_product_dimension (
          product_key TEXT PRIMARY KEY,
          product_id TEXT,
          variant_id TEXT,
          sku TEXT,
          product_title TEXT,
          variant_title TEXT,
          vendor TEXT,
          shopify_product_type TEXT,
          shopify_tags_json TEXT,
          shopify_product_title TEXT,
          shopify_product_vendor TEXT,
          shopify_product_updated_at TEXT,
          shopify_product_synced_at TEXT,
          brand_group TEXT,
          model_family TEXT,
          category TEXT,
          category_source TEXT,
          category_confidence REAL,
          audience TEXT,
          is_clothing INTEGER NOT NULL DEFAULT 0,
          is_footwear INTEGER NOT NULL DEFAULT 0,
          is_accessory INTEGER NOT NULL DEFAULT 0,
          is_collab INTEGER NOT NULL DEFAULT 0,
          first_seen_at TEXT,
          last_seen_at TEXT,
          updated_at TEXT NOT NULL
        );
        CREATE INDEX IF NOT EXISTS idx_sales_dim_brand ON shopify_sales_product_dimension(brand_group);
        CREATE INDEX IF NOT EXISTS idx_sales_dim_model ON shopify_sales_product_dimension(model_family);
        CREATE INDEX IF NOT EXISTS idx_sales_dim_category ON shopify_sales_product_dimension(category);
        CREATE TABLE IF NOT EXISTS shopify_sales_product_metadata (
          product_id TEXT PRIMARY KEY,
          title TEXT,
          vendor TEXT,
          product_type TEXT,
          tags_json TEXT,
          handle TEXT,
          status TEXT,
          updated_at TEXT,
          synced_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS shopify_sales_category_overrides (
          product_key TEXT PRIMARY KEY,
          match_title TEXT,
          match_sku TEXT,
          category TEXT NOT NULL,
          category_source TEXT NOT NULL,
          category_confidence REAL NOT NULL,
          brand_group TEXT,
          model_family TEXT,
          reason TEXT,
          approved_by TEXT,
          created_at TEXT,
          synced_at TEXT NOT NULL
        );
        CREATE INDEX IF NOT EXISTS idx_sales_product_metadata_type ON shopify_sales_product_metadata(product_type);
        """

    )
    # Backfill columns when upgrading an existing local DB.
    existing_cols = {r[1] for r in con.execute("PRAGMA table_info(shopify_sales_product_dimension)").fetchall()}
    for col, ddl in {
        "shopify_product_type": "ALTER TABLE shopify_sales_product_dimension ADD COLUMN shopify_product_type TEXT",
        "shopify_tags_json": "ALTER TABLE shopify_sales_product_dimension ADD COLUMN shopify_tags_json TEXT",
        "shopify_product_title": "ALTER TABLE shopify_sales_product_dimension ADD COLUMN shopify_product_title TEXT",
        "shopify_product_vendor": "ALTER TABLE shopify_sales_product_dimension ADD COLUMN shopify_product_vendor TEXT",
        "shopify_product_updated_at": "ALTER TABLE shopify_sales_product_dimension ADD COLUMN shopify_product_updated_at TEXT",
        "shopify_product_synced_at": "ALTER TABLE shopify_sales_product_dimension ADD COLUMN shopify_product_synced_at TEXT",
    }.items():
        if col not in existing_cols:
            con.execute(ddl)



def sync_shopify_product_metadata(con: sqlite3.Connection, *, only_missing: bool = False, batch_size: int = 50) -> dict[str, Any]:
    init_schema(con)
    if only_missing:
        rows = con.execute(
            """
            SELECT DISTINCT li.product_id
            FROM shopify_order_line_items li
            LEFT JOIN shopify_sales_product_metadata pm ON pm.product_id = CASE WHEN li.product_id LIKE 'gid://%' THEN li.product_id ELSE 'gid://shopify/Product/' || li.product_id END
            WHERE coalesce(li.product_id,'')<>'' AND pm.product_id IS NULL
            ORDER BY li.product_id
            """
        ).fetchall()
    else:
        rows = con.execute(
            "SELECT DISTINCT product_id FROM shopify_order_line_items WHERE coalesce(product_id,'')<>'' ORDER BY product_id"
        ).fetchall()
    product_ids = []
    for r in rows:
        raw = str(r[0] or "").strip()
        if not raw:
            continue
        product_ids.append(raw if raw.startswith("gid://") else f"gid://shopify/Product/{raw}")
    product_ids = sorted(set(product_ids))
    if not product_ids:
        return {"status": "ok", "requested_products": 0, "synced_products": 0, "missing_products": 0, "values_printed": False}
    query = """
    query ProductNodes($ids: [ID!]!) {
      nodes(ids: $ids) {
        ... on Product {
          id
          title
          vendor
          productType
          tags
          handle
          status
          updatedAt
        }
      }
    }
    """
    synced = 0
    missing = 0
    synced_at = now_iso()
    for batch in chunked(product_ids, batch_size):
        data = shopify_graphql(query, {"ids": batch})
        nodes = data.get("nodes") or []
        by_id = {n.get("id"): n for n in nodes if isinstance(n, dict) and n.get("id")}
        for pid in batch:
            node = by_id.get(pid)
            if not node:
                missing += 1
                continue
            tags = parse_tags(node.get("tags"))
            con.execute(
                """
                INSERT INTO shopify_sales_product_metadata(product_id, title, vendor, product_type, tags_json, handle, status, updated_at, synced_at)
                VALUES (?,?,?,?,?,?,?,?,?)
                ON CONFLICT(product_id) DO UPDATE SET
                  title=excluded.title, vendor=excluded.vendor, product_type=excluded.product_type,
                  tags_json=excluded.tags_json, handle=excluded.handle, status=excluded.status,
                  updated_at=excluded.updated_at, synced_at=excluded.synced_at
                """,
                (
                    pid,
                    norm(node.get("title")),
                    norm(node.get("vendor")),
                    norm(node.get("productType")),
                    json.dumps(tags, ensure_ascii=False),
                    norm(node.get("handle")),
                    norm(node.get("status")),
                    norm(node.get("updatedAt")),
                    synced_at,
                ),
            )
            synced += 1
        con.commit()
        time.sleep(0.15)
    return {"status": "ok", "requested_products": len(product_ids), "synced_products": synced, "missing_products": missing, "values_printed": False}



def sync_category_overrides(con: sqlite3.Connection, path: Path = DEFAULT_OVERRIDES) -> dict[str, Any]:
    """Load audited manual category overrides from JSON into SQLite.

    Overrides are intentionally narrow: use them only for legacy/no-metadata rows
    where the default classifier cannot produce an evidence-based source.
    """
    init_schema(con)
    con.execute("DELETE FROM shopify_sales_category_overrides")
    if not path.exists():
        con.commit()
        return {"status": "missing", "path": str(path), "overrides": 0, "values_printed": False}
    data = json.loads(path.read_text())
    overrides = data.get("overrides", [])
    now = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    for item in overrides:
        product_key = norm(item.get("product_key")) or product_key_for("", "", norm(item.get("match_title")), norm(item.get("match_sku")))
        category = norm(item.get("category"))
        source = norm(item.get("category_source")) or "manual_review_v1"
        confidence = float(item.get("category_confidence", 0.99))
        if not product_key or category not in {"calcado", "roupa", "acessorio", "outros"}:
            raise ValueError(f"invalid category override: {item!r}")
        con.execute(
            """
            INSERT INTO shopify_sales_category_overrides(
              product_key, match_title, match_sku, category, category_source, category_confidence,
              brand_group, model_family, reason, approved_by, created_at, synced_at
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                product_key,
                norm(item.get("match_title")),
                norm(item.get("match_sku")),
                category,
                source,
                confidence,
                norm(item.get("brand_group")),
                norm(item.get("model_family")),
                norm(item.get("reason")),
                norm(item.get("approved_by")),
                norm(item.get("created_at")),
                now,
            ),
        )
    con.commit()
    return {"status": "ok", "path": str(path), "overrides": len(overrides), "values_printed": False}

def refresh_dimension(con: sqlite3.Connection) -> dict[str, Any]:
    init_schema(con)
    override_payload = sync_category_overrides(con)
    # Derived table: rebuild deterministically each run so changes to product_key
    # logic/classifiers do not leave stale dimension rows behind.
    con.execute("DELETE FROM shopify_sales_product_dimension")
    rows = con.execute(
        """
        SELECT li.product_id, li.variant_id, li.sku, li.product_title, li.variant_title, li.vendor,
               pm.title AS shopify_product_title, pm.vendor AS shopify_product_vendor, pm.product_type AS shopify_product_type,
               pm.tags_json AS shopify_tags_json, pm.updated_at AS shopify_product_updated_at, pm.synced_at AS shopify_product_synced_at,
               min(li.created_at) first_seen_at, max(li.created_at) last_seen_at,
               count(*) row_count, coalesce(sum(li.quantity),0) units
        FROM shopify_order_line_items li
        LEFT JOIN shopify_sales_product_metadata pm ON pm.product_id = CASE WHEN li.product_id LIKE 'gid://%' THEN li.product_id ELSE 'gid://shopify/Product/' || li.product_id END
        GROUP BY li.product_id, li.variant_id, li.sku, li.product_title, li.variant_title, li.vendor,
                 pm.title, pm.vendor, pm.product_type, pm.tags_json, pm.updated_at, pm.synced_at
        """
    ).fetchall()
    updated = 0
    category_counts: dict[str, int] = {}
    for r in rows:
        title = norm(r["product_title"])
        sku = norm(r["sku"])
        vendor = norm(r["vendor"])
        product_type = norm(r["shopify_product_type"])
        tags = parse_tags(r["shopify_tags_json"])
        product_key = make_key(r)
        override = con.execute(
            "SELECT * FROM shopify_sales_category_overrides WHERE product_key=?",
            (product_key,),
        ).fetchone()
        if override:
            cat = override["category"]
            source = override["category_source"]
            confidence = float(override["category_confidence"])
        elif SERVICE_RE.search(f"{vendor} {title} {sku}"):
            cat, source, confidence = "outros", "service_non_product_v1", 0.99
        else:
            official_cat, official_source, official_confidence = classify_category_from_official(product_type, tags)
            if official_cat:
                cat, source, confidence = official_cat, official_source or "shopify_product_type_tags_v1", official_confidence or 0.95
            else:
                cat, source, confidence = classify_category(vendor, title, sku)
        bg = brand_group(norm(r["shopify_product_vendor"]) or vendor, norm(r["shopify_product_title"]) or title, sku)
        family = model_family(norm(r["shopify_product_vendor"]) or vendor, norm(r["shopify_product_title"]) or title, sku)
        aud = audience(title, sku)
        blob = f"{vendor} {title} {sku}"
        category_counts[cat] = category_counts.get(cat, 0) + 1
        con.execute(
            """
            INSERT INTO shopify_sales_product_dimension(
              product_key, product_id, variant_id, sku, product_title, variant_title, vendor,
              shopify_product_type, shopify_tags_json, shopify_product_title, shopify_product_vendor, shopify_product_updated_at, shopify_product_synced_at,
              brand_group, model_family, category, category_source, category_confidence, audience,
              is_clothing, is_footwear, is_accessory, is_collab, first_seen_at, last_seen_at, updated_at
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ON CONFLICT(product_key) DO UPDATE SET
              product_id=excluded.product_id, variant_id=excluded.variant_id, sku=excluded.sku,
              product_title=excluded.product_title, variant_title=excluded.variant_title, vendor=excluded.vendor,
              shopify_product_type=excluded.shopify_product_type, shopify_tags_json=excluded.shopify_tags_json,
              shopify_product_title=excluded.shopify_product_title, shopify_product_vendor=excluded.shopify_product_vendor,
              shopify_product_updated_at=excluded.shopify_product_updated_at, shopify_product_synced_at=excluded.shopify_product_synced_at,
              brand_group=excluded.brand_group, model_family=excluded.model_family, category=excluded.category,
              category_source=excluded.category_source, category_confidence=excluded.category_confidence,
              audience=excluded.audience, is_clothing=excluded.is_clothing, is_footwear=excluded.is_footwear,
              is_accessory=excluded.is_accessory, is_collab=excluded.is_collab,
              first_seen_at=excluded.first_seen_at, last_seen_at=excluded.last_seen_at, updated_at=excluded.updated_at
            """,
            (
                product_key,
                norm(r["product_id"]),
                norm(r["variant_id"]),
                sku,
                title,
                norm(r["variant_title"]),
                vendor,
                product_type,
                json.dumps(tags, ensure_ascii=False),
                norm(r["shopify_product_title"]),
                norm(r["shopify_product_vendor"]),
                norm(r["shopify_product_updated_at"]),
                norm(r["shopify_product_synced_at"]),
                bg,
                family,
                cat,
                source,
                confidence,
                aud,
                1 if cat == "roupa" else 0,
                1 if cat == "calcado" else 0,
                1 if cat == "acessorio" else 0,
                1 if COLLAB_RE.search(blob) else 0,
                norm(r["first_seen_at"]),
                norm(r["last_seen_at"]),
                now_iso(),
            ),
        )
        updated += 1
    con.executescript(
        """
        DROP VIEW IF EXISTS shopify_sales_line_items_enriched;
        CREATE VIEW shopify_sales_line_items_enriched AS
        SELECT
          li.*,
          o.order_name,
          o.order_number,
          o.financial_status,
          o.fulfillment_status,
          o.cancelled_at,
          o.total_price AS order_total_price,
          o.source_name AS order_source_name,
          CASE
            WHEN lower(coalesce(o.source_name,''))='pos' THEN 'loja_fisica'
            WHEN lower(coalesce(o.source_name,''))='web' THEN 'site'
            WHEN lower(coalesce(o.source_name,''))='shopify_draft_order' THEN 'draft_order'
            WHEN coalesce(o.source_name,'') GLOB '[0-9]*' THEN 'app_numeric_source'
            ELSE coalesce(o.source_name,'unknown')
          END AS channel_group,
          CASE WHEN coalesce(o.cancelled_at,'')='' THEN 1 ELSE 0 END AS is_active_order,
          CASE WHEN lower(coalesce(o.financial_status,''))='paid' THEN 1 ELSE 0 END AS is_paid_order,
          datetime(replace(replace(o.created_at,'T',' '),'Z','')) AS order_created_at_dt,
          d.product_key,
          d.shopify_product_type,
          d.shopify_tags_json,
          d.shopify_product_title,
          d.shopify_product_vendor,
          d.shopify_product_updated_at,
          d.shopify_product_synced_at,
          d.brand_group,
          d.model_family,
          d.category,
          d.category_source,
          d.category_confidence,
          d.audience,
          d.is_clothing,
          d.is_footwear,
          d.is_accessory,
          d.is_collab
        FROM shopify_order_line_items li
        JOIN shopify_orders o ON o.shopify_order_id = li.shopify_order_id
        LEFT JOIN shopify_sales_product_dimension d
          ON d.product_key = CASE
            WHEN coalesce(li.product_id,'')<>'' OR coalesce(li.variant_id,'')<>''
              THEN 'pid:' || coalesce(li.product_id,'') || '|vid:' || coalesce(li.variant_id,'') || '|sku:' || coalesce(li.sku,'')
            ELSE 'title:' || coalesce(li.product_title,'') || '|sku:' || coalesce(li.sku,'')
          END;
        DROP VIEW IF EXISTS shopify_sales_paid_line_items_enriched;
        CREATE VIEW shopify_sales_paid_line_items_enriched AS
        SELECT * FROM shopify_sales_line_items_enriched
        WHERE is_active_order=1 AND is_paid_order=1;
        DROP VIEW IF EXISTS shopify_sales_category_channel_summary;
        CREATE VIEW shopify_sales_category_channel_summary AS
        SELECT channel_group, category,
               count(distinct shopify_order_id) orders,
               coalesce(sum(quantity),0) units,
               round(coalesce(sum(line_revenue_estimate),0),2) revenue
        FROM shopify_sales_paid_line_items_enriched
        GROUP BY channel_group, category;
        DROP VIEW IF EXISTS shopify_sales_brand_model_summary;
        CREATE VIEW shopify_sales_brand_model_summary AS
        SELECT brand_group, model_family,
               count(distinct shopify_order_id) orders,
               coalesce(sum(quantity),0) units,
               round(coalesce(sum(line_revenue_estimate),0),2) revenue
        FROM shopify_sales_paid_line_items_enriched
        GROUP BY brand_group, model_family;
        """
    )
    con.commit()
    table_rows = con.execute("SELECT count(*) FROM shopify_sales_product_dimension").fetchone()[0]
    return {"dimension_rows_processed": updated, "dimension_table_rows": int(table_rows), "category_rows": category_counts, "category_overrides": override_payload}


def fetch_summary(con: sqlite3.Connection) -> dict[str, Any]:
    totals = dict(
        con.execute(
            "select count(distinct shopify_order_id) orders, coalesce(sum(quantity),0) units, round(coalesce(sum(line_revenue_estimate),0),2) revenue from shopify_sales_paid_line_items_enriched"
        ).fetchone()
    )
    by_category = [dict(r) for r in con.execute("select category, sum(orders) orders, sum(units) units, round(sum(revenue),2) revenue from shopify_sales_category_channel_summary group by category order by revenue desc")]
    by_channel_category = [dict(r) for r in con.execute("select * from shopify_sales_category_channel_summary order by channel_group, revenue desc")]
    top_brands = [dict(r) for r in con.execute("select brand_group, count(distinct shopify_order_id) orders, sum(quantity) units, round(sum(line_revenue_estimate),2) revenue from shopify_sales_paid_line_items_enriched group by brand_group order by revenue desc limit 20")]
    nike_models = [dict(r) for r in con.execute("select model_family, orders, units, revenue from shopify_sales_brand_model_summary where brand_group in ('Nike','Jordan','Jacquemus') or model_family like 'Nike %' order by revenue desc limit 20")]
    metadata = dict(con.execute("""
        select count(distinct CASE WHEN li.product_id LIKE 'gid://%' THEN li.product_id ELSE 'gid://shopify/Product/' || li.product_id END) products_in_sales,
               count(distinct pm.product_id) products_with_shopify_metadata,
               sum(case when coalesce(pm.product_type,'')<>'' then 1 else 0 end) metadata_rows_with_product_type,
               max(pm.synced_at) latest_product_metadata_sync
        from (select distinct CASE WHEN product_id LIKE 'gid://%' THEN product_id ELSE 'gid://shopify/Product/' || product_id END AS product_id from shopify_order_line_items where coalesce(product_id,'')<>'') li
        left join shopify_sales_product_metadata pm on pm.product_id = li.product_id
    """).fetchone())
    category_source = [dict(r) for r in con.execute("select category_source, count(*) dimension_rows from shopify_sales_product_dimension group by category_source order by dimension_rows desc")]
    return {"paid_totals": totals, "product_metadata": metadata, "category_source": category_source, "by_category": by_category, "by_channel_category": by_channel_category, "top_brands": top_brands, "nike_models": nike_models}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=["refresh", "report", "sync-products"])
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--output", type=Path, default=DEFAULT_REPORT)
    ap.add_argument("--with-shopify-products", action="store_true", help="Read Shopify Admin product_type/tags into local metadata before refreshing analytics")
    ap.add_argument("--only-missing-products", action="store_true", help="When syncing Shopify products, fetch only product_ids not yet cached")
    args = ap.parse_args()
    con = sqlite3.connect(args.db)
    con.row_factory = sqlite3.Row
    product_sync = None
    if args.with_shopify_products or args.command == "sync-products":
        product_sync = sync_shopify_product_metadata(con, only_missing=args.only_missing_products)
    result = refresh_dimension(con)
    summary = fetch_summary(con)
    payload = {
        "status": "ok",
        "source": "shopify_sales_os_db_local_enrichment",
        "generated_at": now_iso(),
        "db": str(args.db),
        "refresh": result,
        "shopify_product_sync": product_sync,
        "summary": summary,
        "question_capabilities": [{"id": i, "question": q, "status": s} for i, q, s in QUESTION_CAPABILITIES],
        "classification_note": "category uses Shopify product_type/tags when available, then deterministic local title/vendor/SKU heuristics as fallback; model/audience/collab remain deterministic local signals.",
        "guardrails": {"shopify_write": 0, "tiny_write": 0, "external_write": 0, "public_availability_promise": 0, "auto_purchase": 0},
        "values_printed": False,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": "ok", "shopify_product_sync": product_sync, "dimension_rows_processed": result["dimension_rows_processed"], "dimension_table_rows": result["dimension_table_rows"], "output": str(args.output), "values_printed": False}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
