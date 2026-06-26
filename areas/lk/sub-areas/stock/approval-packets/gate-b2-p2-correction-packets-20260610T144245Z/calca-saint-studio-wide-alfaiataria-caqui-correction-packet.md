# Gate B2 P2 — correction packet — calca-saint-studio-wide-alfaiataria-caqui

- title: `Calça Saint Studio Wide Alfaiataria Caqui`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `4`
- prefixes: `ST11, ST11, ST11, ST11`

## Status counts
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `3`

## Linhas principais
- `ST11` | shopify_duplicate_sku_blocked | Shopify SKU `ST11` | Tiny `` id ``
- `ST11-1` | shopify_variant_tiny_missing | Shopify SKU `ST11-1` | Tiny `` id ``
- `ST11-2` | shopify_variant_tiny_missing | Shopify SKU `ST11-2` | Tiny `` id ``
- `ST11-3` | shopify_variant_tiny_missing | Shopify SKU `ST11-3` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
