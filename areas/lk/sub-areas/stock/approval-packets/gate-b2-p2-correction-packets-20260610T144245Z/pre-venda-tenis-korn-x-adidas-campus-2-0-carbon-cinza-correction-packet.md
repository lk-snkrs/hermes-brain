# Gate B2 P2 — correction packet — pre-venda-tenis-korn-x-adidas-campus-2-0-carbon-cinza

- title: `Tênis Korn x adidas Campus 2.0 Carbon Cinza`
- priority: `P2_saneamento`
- lane: `TINY_DUPLICATE_PACKET`
- proposed_action: Preparar saneamento Tiny de código duplicado e rollback/readback; NÃO executar write sem aprovação escopada.
- row_count: `8`
- prefixes: `IF4282, IF4282, IF4282, IF4282, IF4282, IF4282, IF4282, IF4282`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- shopify_variant_tiny_missing: `6`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `IF4282` | shopify_variant_tiny_missing | Shopify SKU `IF4282` | Tiny `` id ``
- `IF4282-7` | tiny_duplicate_exact_code_blocked | Shopify SKU `IF4282-7` | Tiny `IF4282-7` id `1057646260`
- `IF4282-1` | matched_exact_sku_stock_missing_deposit | Shopify SKU `IF4282-1` | Tiny `IF4282-1` id `1057646267`
- `IF4282-2` | shopify_variant_tiny_missing | Shopify SKU `IF4282-2` | Tiny `` id ``
- `IF4282-3` | shopify_variant_tiny_missing | Shopify SKU `IF4282-3` | Tiny `` id ``
- `IF4282-4` | shopify_variant_tiny_missing | Shopify SKU `IF4282-4` | Tiny `` id ``
- `IF4282-5` | shopify_variant_tiny_missing | Shopify SKU `IF4282-5` | Tiny `` id ``
- `IF4282-6` | shopify_variant_tiny_missing | Shopify SKU `IF4282-6` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
