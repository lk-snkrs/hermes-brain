# LK OS Tiny Stock Snapshot Full Read-only — 2026-05-15

Gerado em: `2026-05-15T20:22:28.299724+00:00`
Run ID: `tiny_stock_20260515T092206Z`
Status: `partial_api_rate_limited`

## Veredito

- Snapshot Tiny read-only iniciado/materializado parcialmente; execução pausada por rate limit/bloqueio Tiny para não pressionar a API.
- A camada derivada `lk_variant_commercial_state` foi recalculada a partir de Shopify + Tiny local.
- Nenhum write em Tiny, Shopify, Merchant, Notion, campanhas, estoque ou preço.

## Contagens

- tiny_products_listed: `17605`
- tiny_products_with_codigo: `15372`
- stock_products_checked: `897`
- deposit_rows: `2774`
- official_deposit_rows: `897`
- official_positive_rows: `40`

## Estado comercial derivado

- blocked_tiny_not_mapped: `10054`
- monitor_non_active_shopify_product: `1431`
- blocked_missing_shopify_sku: `1388`
- blocked_data_quality: `1032`
- ready_zero_stock_sourcing_candidate: `520`
- ready_available_tiny: `37`
- blocked_tiny_duplicate_code: `4`

## Status Tiny por variant Shopify

- not_mapped_in_tiny_snapshot: `12296`
- no_shopify_sku: `1388`
- zero_official_deposit: `736`
- available_official_deposit: `37`
- ambiguous_duplicate_tiny_code: `9`

## Limites / guardrails

- Snapshot Tiny v2 via produtos.pesquisa + produto.obter.estoque; rows still running/partial if status is not completed.
- Tiny stock resume/full modes now enforce delay >= 1.0s; lower values are bumped automatically to reduce API pressure after rate limits.
- Tiny remains operational stock truth; Shopify inventory was not used as stock truth.
- GMC availability policy remains separate: do not turn Tiny zero into Merchant out-of-stock automatically.

## O que não foi feito

- tiny_write
- shopify_write
- inventory_change
- price_change
- supplier_contact
- purchase
- campaign_or_external_send
- cron_creation
