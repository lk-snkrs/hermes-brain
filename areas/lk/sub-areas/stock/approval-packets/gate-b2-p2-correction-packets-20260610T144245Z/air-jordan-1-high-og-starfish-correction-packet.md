# Gate B2 P2 — correction packet — air-jordan-1-high-og-starfish

- title: `Tênis Nike Air Jordan 1 High OG Starfish Laranja`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `7`
- prefixes: `555088036, 555088036, 555088036, 555088036, 555088036, 555088036, 555088036`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `3`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `2`

## Linhas principais
- `555088036` | shopify_duplicate_sku_blocked | Shopify SKU `555088036` | Tiny `555088036` id `1069536568` | saldo LK CONTROLE: 0.0
- `555088036-38` | matched_exact_sku_stock_missing_deposit | Shopify SKU `555088036-38` | Tiny `555088036-38` id `937670696`
- `555088-036-2` | shopify_variant_tiny_missing | Shopify SKU `555088-036-2` | Tiny `` id ``
- `555088036-40` | shopify_variant_tiny_missing | Shopify SKU `555088036-40` | Tiny `` id ``
- `555088-036-4` | matched_exact_sku_stock_resolved | Shopify SKU `555088-036-4` | Tiny `555088-036-4` id `1056650105` | saldo LK CONTROLE: 0.0
- `555088-036-5` | matched_exact_sku_stock_resolved | Shopify SKU `555088-036-5` | Tiny `555088-036-5` id `1056650108` | saldo LK CONTROLE: 0.0
- `555088036-43` | matched_exact_sku_stock_resolved | Shopify SKU `555088036-43` | Tiny `555088036-43` id `937670708` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
