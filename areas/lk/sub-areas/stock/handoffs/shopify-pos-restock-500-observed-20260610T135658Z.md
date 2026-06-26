---
title: Handoff — Shopify test order arrived in orders ingest; POS restock route emitted 500
date_utc: 20260610T135658Z
area: lk/stock
source: lk-ops
status: open
---

# Handoff — Shopify test order arrived; POS restock route 500 observed

## Context

During validation of the LK Shopify webhook repair on 2026-06-10, a real POS test order arrived successfully through the `lk-shopify-orders-ingest` route.

## Evidence observed by lk-ops

- Shopify latest order: `#147742`, order id `7406970831070`, `source_name=pos`, `financial_status=paid`, created at `2026-06-10T10:52:05-03:00`.
- Local ledger `/opt/data/hermes_bruno_ingest/local_sql/lk_shopify_orders_ingest/orders_create_ledger.json` contains `#147742` with:
  - `last_event=orders/create`
  - `last_route=lk-shopify-orders-ingest`
  - `last_seen_at=2026-06-10T13:53:27Z`
  - `is_pos=true`
  - `automation_action=pos_postpurchase_route_filters_separately`
- Vercel logs for `lk-shopify-orders-ingest` around `13:52–13:53 UTC` show repeated `POST /webhooks/lk-shopify-orders-ingest` with `200`.

## Stock-specific observation

In the same Vercel log window, the separate route `POST /webhooks/lk-shopify-pos-restock` returned `500` at least at:

- `13:52:09 UTC`
- `13:52:16 UTC`
- `13:53:22 UTC`
- `13:55:27 UTC`

This is not the sales ingestion route, but it appears stock/restock-related and should be owned by `lk-stock` before any stock/pronta-entrega claim or correction.

## Request for lk-stock

Please inspect `lk-shopify-pos-restock` failures and decide whether any Tiny/stock reconciliation, retry, or route fix is needed. lk-ops did not calculate stock deltas and did not make Shopify/Tiny writes.
