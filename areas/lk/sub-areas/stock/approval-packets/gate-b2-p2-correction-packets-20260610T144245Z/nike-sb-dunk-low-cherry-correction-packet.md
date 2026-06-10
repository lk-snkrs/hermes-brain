# Gate B2 P2 — correction packet — nike-sb-dunk-low-cherry

- title: `Tênis Nike SB Dunk Low Cherry Vermelho`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `4`
- prefixes: `DM0807600, DM0807600, DM0807600, DM0807600`

## Status counts
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `3`

## Linhas principais
- `DM0807600` | shopify_duplicate_sku_blocked | Shopify SKU `DM0807600` | Tiny `` id ``
- `DM0807600-1` | shopify_variant_tiny_missing | Shopify SKU `DM0807600-1` | Tiny `` id ``
- `DM0807600-2` | shopify_variant_tiny_missing | Shopify SKU `DM0807600-2` | Tiny `` id ``
- `DM0807600-3` | shopify_variant_tiny_missing | Shopify SKU `DM0807600-3` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
