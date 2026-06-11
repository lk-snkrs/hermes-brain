# Report — LK Stock OS full live match + Tiny stock

- Run ID: `20260611TDRYRUN2`
- Created at UTC: `2026-06-11T01:26:37.689268Z`
- Input DB: `areas/lk/sub-areas/stock/data/lk_stock_os_current_p1_identity_then_p0_preview_20260610TSEQBA.db`
- Output DB: `areas/lk/sub-areas/stock/data/lk_stock_os_current_full_live_match_tiny_stock_20260611TDRYRUN2.db`
- Rows checked live: `2`
- Local consult resolved after live match: `0`
- Tiny stock rows populated: `0`
- Tiny stock > 0 rows: `0`
- Tiny stock = 0 rows: `0`

## Status counts

- `UNRESOLVED_LIVE_FULL`: 2

## Guardrails

- Tiny write: 0
- Shopify write: 0
- Writes externos: 0
- Public availability/pronta entrega pública: 0
- Runtime/cron/webhook novo: 0

## Nota operacional

Esta rodada promove match e saldo Tiny no cache/read model local usando leitura live Shopify/Tiny. Ela não libera promessa pública de pronta entrega; para resposta ao cliente, usar Stock OS DB com freshness ou reconfirmar Tiny quando a DB não bastar.
