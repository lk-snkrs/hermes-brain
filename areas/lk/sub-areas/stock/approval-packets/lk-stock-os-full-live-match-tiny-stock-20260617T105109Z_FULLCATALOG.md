# Approval packet — LK Stock OS full live match + Tiny stock

- Run ID: `20260617T105109Z_FULLCATALOG`
- Created at UTC: `2026-06-17T10:51:10.029612Z`
- Input DB: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_tiny_full_sync_20260617T082033Z.db`
- Output DB: `areas/lk/sub-areas/stock/data/lk_stock_os_current_full_live_match_tiny_stock_20260617T105109Z_FULLCATALOG.db`
- Rows checked live: `3773`
- Local consult resolved after live match: `3051`
- Tiny stock rows populated: `3488`
- Tiny stock > 0 rows: `315`
- Tiny stock = 0 rows: `3162`

## Status counts

- `CONSULTABLE_LOCAL_RESOLVED_BY_FULL_LIVE_MATCH`: 3051
- `BLOCKED_SHOPIFY_DUPLICATE_LIVE_FULL`: 282
- `UNRESOLVED_LIVE_FULL`: 243
- `BLOCKED_TINY_DUPLICATE_LIVE_FULL`: 99
- `BLOCKED_SHOPIFY_MISSING_LIVE_FULL`: 69
- `BLOCKED_TINY_MISSING_LIVE_FULL`: 23
- `BLOCKED_TINY_DEPOSIT_MISSING_LIVE_FULL`: 6

## Guardrails

- Tiny write: 0
- Shopify write: 0
- Writes externos: 0
- Public availability/pronta entrega pública: 0
- Runtime/cron/webhook novo: 0

## Nota operacional

Esta rodada promove match e saldo Tiny no cache/read model local usando leitura live Shopify/Tiny. Ela não libera promessa pública de pronta entrega; para resposta ao cliente, usar Stock OS DB com freshness ou reconfirmar Tiny quando a DB não bastar.
