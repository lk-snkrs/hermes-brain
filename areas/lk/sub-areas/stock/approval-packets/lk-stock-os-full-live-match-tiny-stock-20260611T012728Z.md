# Approval packet — LK Stock OS full live match + Tiny stock

- Run ID: `20260611T012728Z`
- Created at UTC: `2026-06-11T01:27:28.449571Z`
- Input DB: `areas/lk/sub-areas/stock/data/lk_stock_os_current_p1_identity_then_p0_preview_20260610TSEQBA.db`
- Output DB: `areas/lk/sub-areas/stock/data/lk_stock_os_current_full_live_match_tiny_stock_20260611T012728Z.db`
- Rows checked live: `903`
- Local consult resolved after live match: `251`
- Tiny stock rows populated: `635`
- Tiny stock > 0 rows: `55`
- Tiny stock = 0 rows: `580`

## Status counts

- `BLOCKED_SHOPIFY_DUPLICATE_LIVE_FULL`: 282
- `CONSULTABLE_LOCAL_RESOLVED_BY_FULL_LIVE_MATCH`: 251
- `UNRESOLVED_LIVE_FULL`: 241
- `BLOCKED_TINY_DUPLICATE_LIVE_FULL`: 100
- `BLOCKED_TINY_MISSING_LIVE_FULL`: 15
- `BLOCKED_SHOPIFY_MISSING_LIVE_FULL`: 14

## Guardrails

- Tiny write: 0
- Shopify write: 0
- Writes externos: 0
- Public availability/pronta entrega pública: 0
- Runtime/cron/webhook novo: 0

## Nota operacional

Esta rodada promove match e saldo Tiny no cache/read model local usando leitura live Shopify/Tiny. Ela não libera promessa pública de pronta entrega; para resposta ao cliente, usar Stock OS DB com freshness ou reconfirmar Tiny quando a DB não bastar.
