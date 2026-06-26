# LK Stock OS — resolução local de identidade SKU/Tiny/Shopify — 20260610T172139Z

Escopo: resolver bloqueios de identidade somente em cache/local, usando evidência exata SKU+handle capturada em lotes live/read-only. Tiny e Shopify não foram alterados.

## Resultado
- linhas totais na DB: `903`
- novas linhas resolvidas localmente: `164`
- linhas identity_resolved_safe após overlay: `170`

## Resolvidas por status anterior
- BLOCKED_TINY_DEPOSIT_MISSING: `41`
- BLOCKED_TINY_MISSING: `123`

## Status após overlay
- BLOCKED_SHOPIFY_DUPLICATE: `287`
- BLOCKED_TINY_DEPOSIT_MISSING: `16`
- BLOCKED_TINY_DUPLICATE: `96`
- BLOCKED_TINY_MISSING: `334`
- CONSULTABLE_LOCAL_RESOLVED: `6`
- CONSULTABLE_LOCAL_RESOLVED_BY_LIVE_EXACT_MATCH: `164`

## Decisões
- KEEP_BLOCKED_SHOPIFY_DUPLICATE: `285`
- KEEP_BLOCKED_TINY_DEPOSIT_MISSING: `7`
- KEEP_BLOCKED_TINY_DUPLICATE: `73`
- KEEP_BLOCKED_TINY_MISSING: `265`
- LOCAL_IDENTITY_RESOLVED_EXACT_SKU_TINY_STOCK_EVIDENCE: `164`
- NO_SAFE_LOCAL_IDENTITY_CHANGE: `103`

## Artefatos
- SQLite: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_identity_resolved_20260610T172139Z.db`
- JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/reports/lk-stock-os-identity-resolution-20260610T172139Z.json`
- CSV: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/reports/lk-stock-os-identity-resolution-20260610T172139Z.csv`
- workers: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/reports/gate-b3-identity-resolution-workers-20260610T172139Z`

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/bot/runtime novo: `0`
- Disponibilidade pública/pronta entrega: `0`
- Mesmo linhas resolvidas localmente exigem Tiny/fonte viva no momento antes de atendimento.
