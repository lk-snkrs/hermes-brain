# Gate B2 P1 — correction packet — tenis-onitsuka-tiger-tokuten-cinza

- title: `Tênis Onitsuka Tiger Tokuten Cinza`
- priority: `P1_saneamento`
- lane: `TINY_DUPLICATE_PACKET`
- proposed_action: Preparar saneamento Tiny de código duplicado e rollback/readback; NÃO executar write sem aprovação escopada.
- row_count: `8`
- prefixes: `1183C431020, 1183C431020, 1183C431020, 1183C431020, 1183C431020, 1183C431020, 1183C431020, 1183C431020`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `4`
- shopify_variant_tiny_missing: `2`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `1183C431020` | tiny_duplicate_exact_code_blocked | Shopify SKU `1183C431020` | Tiny `1183C431020` id `1060368528`
- `1183C431020-1` | matched_exact_sku_stock_resolved | Shopify SKU `1183C431020-1` | Tiny `1183C431020-1` id `1060368536` | saldo LK CONTROLE: 0.0
- `1183C431020-2` | matched_exact_sku_stock_resolved | Shopify SKU `1183C431020-2` | Tiny `1183C431020-2` id `1060368539` | saldo LK CONTROLE: 0.0
- `1183C431020-3` | matched_exact_sku_stock_resolved | Shopify SKU `1183C431020-3` | Tiny `1183C431020-3` id `1060368542` | saldo LK CONTROLE: 0.0
- `1183C431020-4` | matched_exact_sku_stock_missing_deposit | Shopify SKU `1183C431020-4` | Tiny `1183C431020-4` id `1060368545`
- `1183C431020-5` | shopify_variant_tiny_missing | Shopify SKU `1183C431020-5` | Tiny `` id ``
- `1183C431020-6` | shopify_variant_tiny_missing | Shopify SKU `1183C431020-6` | Tiny `` id ``
- `1183C431020-7` | matched_exact_sku_stock_resolved | Shopify SKU `1183C431020-7` | Tiny `1183C431020-7` id `1060368554` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
