# Gate B2 P2 — correction packet — nike-sb-dunk-low-pro-blue-raspberry

- title: `Tênis Nike SB Dunk Low Pro Blue Raspberry Azul`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `4`
- prefixes: `DM0807400, DM0807400, DM0807400, DM0807400`

## Status counts
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `3`

## Linhas principais
- `DM0807400` | shopify_duplicate_sku_blocked | Shopify SKU `DM0807400` | Tiny `` id ``
- `DM0807400-1` | shopify_variant_tiny_missing | Shopify SKU `DM0807400-1` | Tiny `` id ``
- `DM0807400-2` | shopify_variant_tiny_missing | Shopify SKU `DM0807400-2` | Tiny `` id ``
- `DM0807400-3` | shopify_variant_tiny_missing | Shopify SKU `DM0807400-3` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
