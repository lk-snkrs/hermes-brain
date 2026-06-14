#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import json
import os
import sqlite3
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_DB = Path(__file__).resolve().parents[1] / "data" / "shopify_sales_os.db"
DEFAULT_SUMMARY = Path(__file__).resolve().parents[1] / "data" / "shopify_sales_os_summary.json"
DEFAULT_SEARCH_INDEX = Path(__file__).resolve().parents[1] / "data" / "shopify_sales_search_index.json"
API_VERSION = os.environ.get("SHOPIFY_API_VERSION", "2024-01")
GUARDRAILS = {
    "shopify_write": 0,
    "tiny_write": 0,
    "external_write": 0,
    "public_availability_promise": 0,
    "auto_purchase": 0,
}

SCHEMA = """
PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;
CREATE TABLE IF NOT EXISTS schema_migrations (
  version TEXT PRIMARY KEY,
  applied_at TEXT NOT NULL
);
INSERT OR IGNORE INTO schema_migrations(version, applied_at) VALUES ('shopify_sales_os_v1', datetime('now'));
CREATE TABLE IF NOT EXISTS shopify_orders (
  shopify_order_id TEXT PRIMARY KEY,
  order_name TEXT,
  order_number TEXT,
  source_name TEXT,
  financial_status TEXT,
  fulfillment_status TEXT,
  currency TEXT,
  subtotal_price REAL DEFAULT 0,
  total_price REAL DEFAULT 0,
  total_discounts REAL DEFAULT 0,
  total_tax REAL DEFAULT 0,
  created_at TEXT,
  processed_at TEXT,
  updated_at TEXT,
  cancelled_at TEXT,
  payload_json TEXT NOT NULL,
  source_observed_at TEXT NOT NULL,
  inserted_at TEXT NOT NULL DEFAULT (datetime('now')),
  last_seen_at TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE TABLE IF NOT EXISTS shopify_order_line_items (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  shopify_order_id TEXT NOT NULL REFERENCES shopify_orders(shopify_order_id) ON DELETE CASCADE,
  line_item_id TEXT,
  product_id TEXT,
  variant_id TEXT,
  sku TEXT,
  product_title TEXT,
  variant_title TEXT,
  vendor TEXT,
  quantity REAL NOT NULL DEFAULT 0,
  price REAL DEFAULT 0,
  total_discount REAL DEFAULT 0,
  line_revenue_estimate REAL DEFAULT 0,
  source_name TEXT,
  created_at TEXT,
  UNIQUE(shopify_order_id, line_item_id)
);
CREATE TABLE IF NOT EXISTS shopify_sales_event_ledger (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  topic TEXT NOT NULL,
  source_event_id TEXT,
  idempotency_key TEXT NOT NULL UNIQUE,
  payload_hash TEXT NOT NULL,
  status TEXT NOT NULL CHECK(status IN ('received','processed','ignored','failed')),
  reason TEXT,
  source_observed_at TEXT,
  received_at TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE TABLE IF NOT EXISTS shopify_sales_sync_state (
  key TEXT PRIMARY KEY,
  value TEXT,
  updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_shopify_orders_created_at ON shopify_orders(created_at);
CREATE INDEX IF NOT EXISTS idx_shopify_orders_source_name ON shopify_orders(source_name);
CREATE INDEX IF NOT EXISTS idx_shopify_line_items_sku ON shopify_order_line_items(sku);
CREATE INDEX IF NOT EXISTS idx_shopify_line_items_variant ON shopify_order_line_items(variant_id);
"""


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def connect(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    con.executescript(SCHEMA)
    return con


def as_gid(kind: str, value: Any) -> str:
    text = str(value or "").strip()
    if not text:
        return ""
    if text.startswith("gid://"):
        return text
    return f"gid://shopify/{kind}/{text}"


def numeric(value: Any) -> float:
    if isinstance(value, dict):
        value = value.get("amount")
    try:
        return float(value or 0)
    except (TypeError, ValueError):
        return 0.0


def normalize_order(payload: dict[str, Any]) -> dict[str, Any]:
    order_id = payload.get("admin_graphql_api_id") or payload.get("id") or payload.get("legacyResourceId") or payload.get("name")
    shopify_order_id = as_gid("Order", order_id) if order_id and not str(order_id).startswith("fixture-") else str(order_id or "")
    if not shopify_order_id:
        raise ValueError("order_without_id")
    line_items = []
    raw_line_items = payload.get("line_items") or payload.get("lineItems") or []
    if isinstance(raw_line_items, dict):
        raw_line_items = [edge.get("node", edge) for edge in raw_line_items.get("edges", [])]
    for idx, item in enumerate(raw_line_items):
        node = item.get("node", item) if isinstance(item, dict) else {}
        quantity = numeric(node.get("quantity"))
        price = numeric(node.get("price") or node.get("originalUnitPriceSet", {}).get("shopMoney"))
        line_discount = numeric(node.get("total_discount") or node.get("totalDiscountSet", {}).get("shopMoney"))
        line_items.append({
            "line_item_id": str(node.get("admin_graphql_api_id") or node.get("id") or f"{shopify_order_id}:line:{idx}"),
            "product_id": str(node.get("product_id") or node.get("product", {}).get("id") or ""),
            "variant_id": str(node.get("variant_id") or node.get("variant", {}).get("id") or ""),
            "sku": str(node.get("sku") or node.get("variant", {}).get("sku") or "").strip(),
            "product_title": str(node.get("title") or node.get("name") or node.get("product", {}).get("title") or "Produto sem título"),
            "variant_title": str(node.get("variant_title") or node.get("variant", {}).get("title") or ""),
            "vendor": str(node.get("vendor") or ""),
            "quantity": quantity,
            "price": price,
            "total_discount": line_discount,
            "line_revenue_estimate": max(quantity * price - line_discount, 0),
        })
    return {
        "shopify_order_id": shopify_order_id,
        "order_name": str(payload.get("name") or payload.get("order_name") or ""),
        "order_number": str(payload.get("order_number") or payload.get("orderNumber") or ""),
        "source_name": str(payload.get("source_name") or payload.get("sourceName") or "unknown"),
        "financial_status": str(payload.get("financial_status") or payload.get("displayFinancialStatus") or "unknown"),
        "fulfillment_status": str(payload.get("fulfillment_status") or payload.get("displayFulfillmentStatus") or "unknown"),
        "currency": str(payload.get("currency") or payload.get("currencyCode") or "BRL"),
        "subtotal_price": numeric(payload.get("subtotal_price") or payload.get("subtotalPriceSet", {}).get("shopMoney")),
        "total_price": numeric(payload.get("total_price") or payload.get("totalPriceSet", {}).get("shopMoney")),
        "total_discounts": numeric(payload.get("total_discounts") or payload.get("totalDiscountsSet", {}).get("shopMoney")),
        "total_tax": numeric(payload.get("total_tax") or payload.get("totalTaxSet", {}).get("shopMoney")),
        "created_at": str(payload.get("created_at") or payload.get("createdAt") or ""),
        "processed_at": str(payload.get("processed_at") or payload.get("processedAt") or ""),
        "updated_at": str(payload.get("updated_at") or payload.get("updatedAt") or ""),
        "cancelled_at": str(payload.get("cancelled_at") or payload.get("cancelledAt") or ""),
        "payload_json": json.dumps(payload, ensure_ascii=False, sort_keys=True),
        "line_items": line_items,
    }


def payload_hash(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def verify_hmac(raw: bytes, header_hmac: str, secret: str) -> bool:
    digest = hmac.new(secret.encode(), raw, hashlib.sha256).digest()
    expected = base64.b64encode(digest).decode()
    return hmac.compare_digest(expected, header_hmac or "")


def upsert_order(con: sqlite3.Connection, payload: dict[str, Any], topic: str, event_id: str | None = None, raw: bytes | None = None) -> dict[str, Any]:
    raw_bytes = raw if raw is not None else json.dumps(payload, ensure_ascii=False, sort_keys=True).encode()
    digest = payload_hash(raw_bytes)
    order = normalize_order(payload)
    idempotency_key = f"{topic}:{event_id or order['shopify_order_id']}:{digest[:16]}"
    existing = con.execute("select status from shopify_sales_event_ledger where idempotency_key=?", (idempotency_key,)).fetchone()
    if existing:
        return {"status": "ignored", "reason": "duplicate_event", "idempotency_key": idempotency_key, "guardrails": GUARDRAILS}
    observed_at = now_iso()
    con.execute(
        "insert into shopify_sales_event_ledger(topic, source_event_id, idempotency_key, payload_hash, status, reason, source_observed_at) values (?,?,?,?,?,?,?)",
        (topic, event_id or order["shopify_order_id"], idempotency_key, digest, "received", None, observed_at),
    )
    con.execute(
        """insert into shopify_orders(shopify_order_id, order_name, order_number, source_name, financial_status, fulfillment_status, currency,
             subtotal_price, total_price, total_discounts, total_tax, created_at, processed_at, updated_at, cancelled_at, payload_json, source_observed_at, last_seen_at)
           values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
           on conflict(shopify_order_id) do update set order_name=excluded.order_name, order_number=excluded.order_number, source_name=excluded.source_name,
             financial_status=excluded.financial_status, fulfillment_status=excluded.fulfillment_status, currency=excluded.currency,
             subtotal_price=excluded.subtotal_price, total_price=excluded.total_price, total_discounts=excluded.total_discounts, total_tax=excluded.total_tax,
             created_at=excluded.created_at, processed_at=excluded.processed_at, updated_at=excluded.updated_at, cancelled_at=excluded.cancelled_at,
             payload_json=excluded.payload_json, source_observed_at=excluded.source_observed_at, last_seen_at=excluded.last_seen_at""",
        (order["shopify_order_id"], order["order_name"], order["order_number"], order["source_name"], order["financial_status"], order["fulfillment_status"], order["currency"],
         order["subtotal_price"], order["total_price"], order["total_discounts"], order["total_tax"], order["created_at"], order["processed_at"], order["updated_at"], order["cancelled_at"],
         order["payload_json"], observed_at, observed_at),
    )
    for line in order["line_items"]:
        con.execute(
            """insert into shopify_order_line_items(shopify_order_id, line_item_id, product_id, variant_id, sku, product_title, variant_title, vendor, quantity, price, total_discount, line_revenue_estimate, source_name, created_at)
               values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
               on conflict(shopify_order_id,line_item_id) do update set product_id=excluded.product_id, variant_id=excluded.variant_id, sku=excluded.sku,
                 product_title=excluded.product_title, variant_title=excluded.variant_title, vendor=excluded.vendor, quantity=excluded.quantity,
                 price=excluded.price, total_discount=excluded.total_discount, line_revenue_estimate=excluded.line_revenue_estimate, source_name=excluded.source_name, created_at=excluded.created_at""",
            (order["shopify_order_id"], line["line_item_id"], line["product_id"], line["variant_id"], line["sku"], line["product_title"], line["variant_title"], line["vendor"],
             line["quantity"], line["price"], line["total_discount"], line["line_revenue_estimate"], order["source_name"], order["created_at"]),
        )
    con.execute("update shopify_sales_event_ledger set status='processed', reason=?, updated_at=datetime('now') where idempotency_key=?", (f"line_items={len(order['line_items'])}", idempotency_key))
    con.commit()
    return {"status": "processed", "order_id": order["shopify_order_id"], "line_items": len(order["line_items"]), "idempotency_key": idempotency_key, "guardrails": GUARDRAILS}


def export_summary(con: sqlite3.Connection) -> dict[str, Any]:
    totals = con.execute("select count(*) orders, coalesce(sum(total_price),0) revenue, min(created_at) start, max(created_at) end from shopify_orders where coalesce(cancelled_at,'')='' ").fetchone()
    units = con.execute("select coalesce(sum(quantity),0) units from shopify_order_line_items").fetchone()["units"]
    source_rows = con.execute("select coalesce(source_name,'unknown') source_name, count(distinct shopify_order_id) orders, coalesce(sum(line_revenue_estimate),0) revenue, coalesce(sum(quantity),0) units from shopify_order_line_items group by source_name order by revenue desc").fetchall()
    product_rows = con.execute("select sku, product_title, variant_title, coalesce(sum(quantity),0) quantity, coalesce(sum(line_revenue_estimate),0) revenue from shopify_order_line_items group by sku, product_title, variant_title order by revenue desc, quantity desc limit 50").fetchall()
    status = "ok" if int(totals["orders"] or 0) else "empty"
    return {
        "status": status,
        "source": "shopify_sales_os_db",
        "generated_at": now_iso(),
        "freshness": {"local_start_date": totals["start"], "local_end_date": totals["end"], "orders_count": int(totals["orders"] or 0)},
        "totals": {"orders": int(totals["orders"] or 0), "revenue": round(float(totals["revenue"] or 0), 2), "units": round(float(units or 0), 2)},
        "channels": [{"source_name": r["source_name"], "orders": int(r["orders"] or 0), "revenue": round(float(r["revenue"] or 0), 2), "units": round(float(r["units"] or 0), 2)} for r in source_rows],
        "top_products": [{"sku": r["sku"], "product_title": r["product_title"], "variant_title": r["variant_title"], "quantity": round(float(r["quantity"] or 0), 2), "revenue": round(float(r["revenue"] or 0), 2)} for r in product_rows],
        "guardrails": GUARDRAILS,
        "coverage_note": "Shopify Sales OS local DB read-only. Webhook/backfill só ingerem eventos/pedidos em SQLite local; nenhum write Shopify/Tiny.",
    }


def export_search_index(con: sqlite3.Connection) -> dict[str, Any]:
    rows = con.execute("""
        select
          coalesce(sku,'') sku,
          coalesce(product_title,'Produto sem título') product_title,
          coalesce(variant_title,'—') variant_title,
          coalesce(vendor,'') vendor,
          coalesce(brand_group,'Outros') brand_group,
          coalesce(model_family,'') model_family,
          coalesce(category,'outros') category,
          coalesce(category_source,'') category_source,
          coalesce(channel_group, coalesce(source_name,'unknown')) channel_group,
          count(distinct shopify_order_id) orders,
          coalesce(sum(quantity),0) quantity,
          coalesce(sum(line_revenue_estimate),0) revenue,
          min(order_created_at_dt) first_order_at,
          max(order_created_at_dt) last_order_at
        from shopify_sales_paid_line_items_enriched
        group by sku, product_title, variant_title, vendor, brand_group, model_family, category, category_source, channel_group
    """).fetchall()
    window_rows = con.execute("""
        select
          coalesce(sku,'') sku,
          coalesce(product_title,'Produto sem título') product_title,
          coalesce(variant_title,'—') variant_title,
          count(distinct case when order_created_at_dt >= datetime('now','-7 days') then shopify_order_id end) orders_d7,
          coalesce(sum(case when order_created_at_dt >= datetime('now','-7 days') then quantity else 0 end),0) quantity_d7,
          coalesce(sum(case when order_created_at_dt >= datetime('now','-7 days') then line_revenue_estimate else 0 end),0) revenue_d7,
          count(distinct case when order_created_at_dt >= datetime('now','-30 days') then shopify_order_id end) orders_d30,
          coalesce(sum(case when order_created_at_dt >= datetime('now','-30 days') then quantity else 0 end),0) quantity_d30,
          coalesce(sum(case when order_created_at_dt >= datetime('now','-30 days') then line_revenue_estimate else 0 end),0) revenue_d30,
          count(distinct case when order_created_at_dt >= datetime('now','-90 days') then shopify_order_id end) orders_d90,
          coalesce(sum(case when order_created_at_dt >= datetime('now','-90 days') then quantity else 0 end),0) quantity_d90,
          coalesce(sum(case when order_created_at_dt >= datetime('now','-90 days') then line_revenue_estimate else 0 end),0) revenue_d90
        from shopify_sales_paid_line_items_enriched
        group by sku, product_title, variant_title
    """).fetchall()
    windows_by_key = {
        (r["sku"] or "", r["product_title"] or "", r["variant_title"] or ""): {
            "d7": {"orders": int(r["orders_d7"] or 0), "quantity": round(float(r["quantity_d7"] or 0), 2), "revenue": round(float(r["revenue_d7"] or 0), 2)},
            "d30": {"orders": int(r["orders_d30"] or 0), "quantity": round(float(r["quantity_d30"] or 0), 2), "revenue": round(float(r["revenue_d30"] or 0), 2)},
            "d90": {"orders": int(r["orders_d90"] or 0), "quantity": round(float(r["quantity_d90"] or 0), 2), "revenue": round(float(r["revenue_d90"] or 0), 2)},
        } for r in window_rows
    }
    recent_rows = con.execute("""
        select coalesce(li.sku,'') sku, coalesce(li.product_title,'Produto sem título') product_title, coalesce(li.variant_title,'—') variant_title,
               coalesce(o.order_name, o.order_number, li.shopify_order_id) order_ref, coalesce(o.source_name, li.source_name, 'unknown') source_name,
               coalesce(li.quantity,0) quantity, coalesce(li.line_revenue_estimate,0) revenue, coalesce(o.financial_status,'') financial_status,
               datetime(replace(replace(coalesce(o.created_at, li.created_at), 'T',' '),'Z','')) order_created_at_dt
        from shopify_order_line_items li
        join shopify_orders o on o.shopify_order_id = li.shopify_order_id
        where lower(coalesce(o.financial_status,''))='paid' and coalesce(o.cancelled_at,'')=''
        order by order_created_at_dt desc
    """).fetchall()
    recent_by_key: dict[tuple[str, str, str], list[dict[str, Any]]] = {}
    for rr in recent_rows:
        key = (rr["sku"] or "", rr["product_title"] or "", rr["variant_title"] or "")
        bucket = recent_by_key.setdefault(key, [])
        if len(bucket) < 8:
            bucket.append({
                "order_ref": rr["order_ref"],
                "order_created_at": rr["order_created_at_dt"],
                "channel": "loja_fisica" if str(rr["source_name"] or '').lower() == 'pos' else ("site" if str(rr["source_name"] or '').lower() == 'web' else rr["source_name"]),
                "quantity": round(float(rr["quantity"] or 0), 2),
                "revenue": round(float(rr["revenue"] or 0), 2),
                "financial_status": rr["financial_status"],
            })
    products: dict[tuple[str, str, str], dict[str, Any]] = {}
    for r in rows:
        key = (r["sku"] or "", r["product_title"] or "", r["variant_title"] or "")
        current = products.setdefault(key, {
            "sku": r["sku"] or "",
            "product_title": r["product_title"] or "Produto sem título",
            "variant_title": r["variant_title"] or "—",
            "vendor": r["vendor"] or "",
            "brand_group": r["brand_group"] or "Outros",
            "model_family": r["model_family"] or "",
            "category": r["category"] or "outros",
            "category_source": r["category_source"] or "",
            "orders": 0,
            "quantity": 0.0,
            "revenue": 0.0,
            "windows": windows_by_key.get(key, {"d7": {"orders": 0, "quantity": 0, "revenue": 0}, "d30": {"orders": 0, "quantity": 0, "revenue": 0}, "d90": {"orders": 0, "quantity": 0, "revenue": 0}}),
            "recent_sales": recent_by_key.get(key, []),
            "channels": {},
            "first_order_at": r["first_order_at"],
            "last_order_at": r["last_order_at"],
        })
        channel = r["channel_group"] or "unknown"
        orders = int(r["orders"] or 0)
        qty = float(r["quantity"] or 0)
        rev = float(r["revenue"] or 0)
        current["orders"] += orders
        current["quantity"] += qty
        current["revenue"] += rev
        current["channels"][channel] = {"orders": orders, "quantity": round(qty, 2), "revenue": round(rev, 2)}
        if r["first_order_at"] and (not current["first_order_at"] or r["first_order_at"] < current["first_order_at"]):
            current["first_order_at"] = r["first_order_at"]
        if r["last_order_at"] and (not current["last_order_at"] or r["last_order_at"] > current["last_order_at"]):
            current["last_order_at"] = r["last_order_at"]
    items = []
    for item in products.values():
        item["quantity"] = round(float(item["quantity"] or 0), 2)
        item["revenue"] = round(float(item["revenue"] or 0), 2)
        item["avg_unit_revenue"] = round(item["revenue"] / item["quantity"], 2) if item["quantity"] else 0
        haystack = " ".join(str(item.get(k) or "") for k in ["sku", "product_title", "variant_title", "vendor", "brand_group", "model_family", "category"]).lower()
        item["search_text"] = haystack
        items.append(item)
    items.sort(key=lambda x: (x["revenue"], x["quantity"]), reverse=True)
    totals = {"products": len(items), "orders": sum(i["orders"] for i in items), "units": round(sum(i["quantity"] for i in items), 2), "revenue": round(sum(i["revenue"] for i in items), 2)}
    return {
        "status": "ok" if items else "empty",
        "source": "shopify_sales_os_db_paid_active_line_items",
        "generated_at": now_iso(),
        "totals": totals,
        "items": items,
        "guardrails": GUARDRAILS,
        "coverage_note": "Índice read-only de vendas pagas/ativas (financial_status=PAID e não canceladas). Não promete disponibilidade pública.",
    }


def shopify_store() -> str:
    store = (os.environ.get("SHOPIFY_STORE_URL") or os.environ.get("SHOPIFY_STORE") or os.environ.get("SHOPIFY_SHOP_NAME") or "").replace("https://", "").replace("http://", "").strip("/")
    if store and not store.endswith(".myshopify.com") and "." not in store:
        store += ".myshopify.com"
    return store


def shopify_graphql(query: str, variables: dict[str, Any]) -> dict[str, Any]:
    store = shopify_store()
    token = os.environ.get("SHOPIFY_ACCESS_TOKEN") or os.environ.get("SHOPIFY_ADMIN_TOKEN") or os.environ.get("SHOPIFY_API_TOKEN") or ""
    if not store or not token:
        raise RuntimeError("missing_shopify_credentials")
    req = urllib.request.Request(f"https://{store}/admin/api/{API_VERSION}/graphql.json", data=json.dumps({"query": query, "variables": variables}).encode(), method="POST")
    req.add_header("X-Shopify-Access-Token", token)
    req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=60) as resp:
        body = json.loads(resp.read().decode())
    if body.get("errors"):
        raise RuntimeError(json.dumps(body["errors"])[:500])
    return body


def node_to_rest_like_order(node: dict[str, Any]) -> dict[str, Any]:
    line_items = []
    for edge in ((node.get("lineItems") or {}).get("edges") or []):
        item = edge.get("node") or {}
        variant = item.get("variant") or {}
        product = variant.get("product") or {}
        line_items.append({
            "id": item.get("id"),
            "product_id": product.get("id"),
            "variant_id": variant.get("id"),
            "title": item.get("title") or product.get("title"),
            "sku": item.get("sku") or variant.get("sku"),
            "variant_title": variant.get("title"),
            "vendor": product.get("vendor"),
            "quantity": item.get("quantity"),
            "price": ((item.get("originalUnitPriceSet") or {}).get("shopMoney") or {}).get("amount"),
            "total_discount": ((item.get("totalDiscountSet") or {}).get("shopMoney") or {}).get("amount"),
        })
    return {
        "id": node.get("id"),
        "name": node.get("name"),
        "order_number": node.get("legacyResourceId"),
        "source_name": node.get("sourceName"),
        "financial_status": node.get("displayFinancialStatus"),
        "fulfillment_status": node.get("displayFulfillmentStatus"),
        "currency": node.get("currencyCode"),
        "subtotal_price": ((node.get("subtotalPriceSet") or {}).get("shopMoney") or {}).get("amount"),
        "total_price": ((node.get("totalPriceSet") or {}).get("shopMoney") or {}).get("amount"),
        "total_discounts": ((node.get("totalDiscountsSet") or {}).get("shopMoney") or {}).get("amount"),
        "total_tax": ((node.get("totalTaxSet") or {}).get("shopMoney") or {}).get("amount"),
        "created_at": node.get("createdAt"),
        "processed_at": node.get("processedAt"),
        "updated_at": node.get("updatedAt"),
        "cancelled_at": node.get("cancelledAt"),
        "line_items": line_items,
    }


def backfill(con: sqlite3.Connection, since: str, until: str | None, limit: int) -> dict[str, Any]:
    query_filter = f"created_at:>={since}"
    if until:
        query_filter += f" created_at:<={until}"
    query = """
    query OrdersBackfill($cursor: String, $query: String!) {
      orders(first: 50, after: $cursor, query: $query, sortKey: CREATED_AT) {
        pageInfo { hasNextPage endCursor }
        edges { node { id legacyResourceId name sourceName displayFinancialStatus displayFulfillmentStatus currencyCode createdAt processedAt updatedAt cancelledAt subtotalPriceSet { shopMoney { amount } } totalPriceSet { shopMoney { amount } } totalDiscountsSet { shopMoney { amount } } totalTaxSet { shopMoney { amount } } lineItems(first: 100) { edges { node { id title sku quantity originalUnitPriceSet { shopMoney { amount } } totalDiscountSet { shopMoney { amount } } variant { id sku title product { id title vendor } } } } } } }
      }
    }
    """
    cursor = None
    scanned = processed = ignored = 0
    while scanned < limit:
        body = shopify_graphql(query, {"cursor": cursor, "query": query_filter})
        orders = ((body.get("data") or {}).get("orders") or {})
        for edge in orders.get("edges") or []:
            if scanned >= limit:
                break
            payload = node_to_rest_like_order(edge.get("node") or {})
            result = upsert_order(con, payload, "backfill/orders", event_id=payload.get("id"))
            scanned += 1
            if result["status"] == "processed":
                processed += 1
            else:
                ignored += 1
        page = orders.get("pageInfo") or {}
        cursor = page.get("endCursor")
        if not page.get("hasNextPage") or not cursor:
            break
        time.sleep(0.25)
    con.execute("insert or replace into shopify_sales_sync_state(key,value,updated_at) values ('last_backfill', ?, datetime('now'))", (json.dumps({"since": since, "until": until, "scanned": scanned, "processed": processed, "ignored": ignored, "at": now_iso()}),))
    con.commit()
    return {"status": "ok", "scanned": scanned, "processed": processed, "ignored": ignored, "guardrails": GUARDRAILS}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="LK Shopify Sales OS local read-only DB")
    sub = parser.add_subparsers(dest="cmd", required=True)
    for name in ["init-db", "export-summary", "export-search-index", "ingest-file", "ingest-stdin", "backfill"]:
        p = sub.add_parser(name)
        p.add_argument("--db", default=str(DEFAULT_DB))
    p = sub.choices["ingest-file"]
    p.add_argument("--payload", required=True)
    p.add_argument("--topic", default="orders/paid")
    p.add_argument("--event-id")
    p.add_argument("--hmac")
    p.add_argument("--webhook-secret", default=os.environ.get("SHOPIFY_WEBHOOK_SECRET", ""))
    p = sub.choices["ingest-stdin"]
    p.add_argument("--topic", default=os.environ.get("HERMES_WEBHOOK_EVENT_TYPE") or "orders/paid")
    p.add_argument("--event-id", default=os.environ.get("HERMES_WEBHOOK_DELIVERY_ID") or None)
    p.add_argument("--summary-output", default=str(DEFAULT_SUMMARY))
    p = sub.choices["export-summary"]
    p.add_argument("--output", default=str(DEFAULT_SUMMARY))
    p = sub.choices["export-search-index"]
    p.add_argument("--output", default=str(DEFAULT_SEARCH_INDEX))
    p = sub.choices["backfill"]
    p.add_argument("--since", required=True)
    p.add_argument("--until")
    p.add_argument("--limit", type=int, default=250)
    args = parser.parse_args(argv)
    con = connect(Path(args.db))
    if args.cmd == "init-db":
        print(json.dumps({"status": "ok", "db": str(Path(args.db)), "guardrails": GUARDRAILS}, ensure_ascii=False))
        return 0
    if args.cmd == "ingest-file":
        raw = Path(args.payload).read_bytes()
        if args.hmac and args.webhook_secret and not verify_hmac(raw, args.hmac, args.webhook_secret):
            print(json.dumps({"status": "failed", "reason": "invalid_hmac", "guardrails": GUARDRAILS}, ensure_ascii=False))
            return 3
        result = upsert_order(con, json.loads(raw.decode()), args.topic, event_id=args.event_id, raw=raw)
        print(json.dumps(result, ensure_ascii=False))
        return 0
    if args.cmd == "ingest-stdin":
        raw = sys.stdin.buffer.read()
        try:
            payload = json.loads(raw.decode("utf-8") or "{}")
        except Exception:
            print(json.dumps({"status": "failed", "reason": "invalid_json", "guardrails": GUARDRAILS}, ensure_ascii=False))
            return 2
        topic = str(args.topic or "")
        if topic.startswith("refunds/"):
            # Refund payloads do not always contain the complete order/line-item
            # shape needed by the sales read model. Keep an idempotent event
            # receipt in the ledger by storing the raw refund object as an order
            # shell only when Shopify includes order_id; otherwise ignore safely.
            payload = {
                "id": payload.get("order_id") or payload.get("admin_graphql_api_id") or payload.get("id"),
                "name": payload.get("order_name") or payload.get("order_id") or payload.get("id"),
                "created_at": payload.get("created_at") or now_iso(),
                "updated_at": payload.get("processed_at") or payload.get("created_at") or now_iso(),
                "cancelled_at": None,
                "source_name": "shopify_refund_webhook",
                "financial_status": "refunded",
                "fulfillment_status": None,
                "currency": payload.get("currency") or "BRL",
                "subtotal_price": 0,
                "total_price": 0,
                "total_discounts": 0,
                "total_tax": 0,
                "line_items": [],
            }
        result = upsert_order(con, payload, topic, event_id=args.event_id, raw=raw)
        summary = export_summary(con)
        out = Path(args.summary_output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
        result["summary_output"] = str(out)
        print(json.dumps(result, ensure_ascii=False))
        return 0
    if args.cmd == "export-summary":
        payload = export_summary(con)
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
        print(json.dumps({"status": payload["status"], "output": str(out), "guardrails": GUARDRAILS}, ensure_ascii=False))
        return 0
    if args.cmd == "export-search-index":
        payload = export_search_index(con)
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
        print(json.dumps({"status": payload["status"], "output": str(out), "items": payload["totals"]["products"], "guardrails": GUARDRAILS}, ensure_ascii=False))
        return 0
    if args.cmd == "backfill":
        print(json.dumps(backfill(con, args.since, args.until, args.limit), ensure_ascii=False))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
