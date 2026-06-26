# Gate B2 P2 — correction packet — bolsa-minimal-saint-studio-cacto-off-white

- title: `Bolsa Minimal Saint Studio Cacto Off White`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `23`
- prefixes: `ST5, ST5, ST5, ST5, ST5, ST5, ST5, ST5, ST5, ST5, ST5, ST5, ST5, ST5, ST5, ST5, ST5, ST5, ST5, ST5, ST5, ST5, ST5`

## Status counts
- matched_exact_sku_stock_missing_deposit: `2`
- matched_exact_sku_stock_resolved: `10`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `10`

## Linhas principais
- `ST5` | matched_exact_sku_stock_resolved | Shopify SKU `ST5` | Tiny `ST5` id `1061015962` | saldo LK CONTROLE: 0.0
- `ST5-1` | shopify_duplicate_sku_blocked | Shopify SKU `ST5-1` | Tiny `ST5-1` id `1061030592` | saldo LK CONTROLE: 0.0
- `ST50` | matched_exact_sku_stock_resolved | Shopify SKU `ST50` | Tiny `ST50` id `1063680555` | saldo LK CONTROLE: 0.0
- `ST51-1` | matched_exact_sku_stock_resolved | Shopify SKU `ST51-1` | Tiny `ST51-1` id `1063684977` | saldo LK CONTROLE: 0.0
- `ST51-2` | matched_exact_sku_stock_missing_deposit | Shopify SKU `ST51-2` | Tiny `ST51-2` id `1063684980`
- `ST51-3` | shopify_variant_tiny_missing | Shopify SKU `ST51-3` | Tiny `` id ``
- `ST51-4` | shopify_variant_tiny_missing | Shopify SKU `ST51-4` | Tiny `` id ``
- `ST51-5` | shopify_variant_tiny_missing | Shopify SKU `ST51-5` | Tiny `` id ``
- `ST52` | shopify_variant_tiny_missing | Shopify SKU `ST52` | Tiny `` id ``
- `ST52-1` | shopify_variant_tiny_missing | Shopify SKU `ST52-1` | Tiny `` id ``
- `ST52-2` | matched_exact_sku_stock_resolved | Shopify SKU `ST52-2` | Tiny `ST52-2` id `1063685947` | saldo LK CONTROLE: 2.0
- `ST52-3` | matched_exact_sku_stock_resolved | Shopify SKU `ST52-3` | Tiny `ST52-3` id `1063685950` | saldo LK CONTROLE: 1.0
- `ST52-4` | matched_exact_sku_stock_resolved | Shopify SKU `ST52-4` | Tiny `ST52-4` id `1063685953` | saldo LK CONTROLE: 1.0
- `ST52-5` | matched_exact_sku_stock_resolved | Shopify SKU `ST52-5` | Tiny `ST52-5` id `1063685956` | saldo LK CONTROLE: -1.0
- `ST53` | matched_exact_sku_stock_resolved | Shopify SKU `ST53` | Tiny `ST53` id `1063797388` | saldo LK CONTROLE: 0.0
- `ST53-1` | matched_exact_sku_stock_missing_deposit | Shopify SKU `ST53-1` | Tiny `ST53-1` id `1063797391`
- `ST53-2` | shopify_variant_tiny_missing | Shopify SKU `ST53-2` | Tiny `` id ``
- `ST54` | shopify_variant_tiny_missing | Shopify SKU `ST54` | Tiny `` id ``
- `ST55` | shopify_variant_tiny_missing | Shopify SKU `ST55` | Tiny `` id ``
- `ST56` | shopify_variant_tiny_missing | Shopify SKU `ST56` | Tiny `` id ``
- `ST57` | shopify_variant_tiny_missing | Shopify SKU `ST57` | Tiny `` id ``
- `ST58` | matched_exact_sku_stock_resolved | Shopify SKU `ST58` | Tiny `ST58` id `1069931267` | saldo LK CONTROLE: 2.0
- `ST59` | matched_exact_sku_stock_resolved | Shopify SKU `ST59` | Tiny `ST59` id `1069931325` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
