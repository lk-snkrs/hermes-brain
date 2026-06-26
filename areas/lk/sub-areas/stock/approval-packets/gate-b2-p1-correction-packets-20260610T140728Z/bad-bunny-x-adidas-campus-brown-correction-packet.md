# Gate B2 P1 — correction packet — bad-bunny-x-adidas-campus-brown

- title: `Tênis Bad Bunny x adidas Campus Brown Marrom`
- priority: `P1_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `8`
- prefixes: `ID2529, ID2529, ID2529, ID2529, ID2529, ID2529, ID2529, ID2529`

## Status counts
- matched_exact_sku_stock_resolved: `2`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `5`

## Linhas principais
- `ID2529` | shopify_duplicate_sku_blocked | Shopify SKU `ID2529` | Tiny `ID2529` id `981838150` | saldo LK CONTROLE: 0.0
- `ID2529-8` | matched_exact_sku_stock_resolved | Shopify SKU `ID2529-8` | Tiny `ID2529-8` id `1066747730` | saldo LK CONTROLE: 0.0
- `ID2529-1` | shopify_variant_tiny_missing | Shopify SKU `ID2529-1` | Tiny `` id ``
- `ID2529-2` | shopify_variant_tiny_missing | Shopify SKU `ID2529-2` | Tiny `` id ``
- `ID2529-3` | shopify_variant_tiny_missing | Shopify SKU `ID2529-3` | Tiny `` id ``
- `ID2529-7` | shopify_variant_tiny_missing | Shopify SKU `ID2529-7` | Tiny `` id ``
- `ID2529-4` | shopify_variant_tiny_missing | Shopify SKU `ID2529-4` | Tiny `` id ``
- `ID2529-5` | matched_exact_sku_stock_resolved | Shopify SKU `ID2529-5` | Tiny `ID2529-5` id `981838229` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
