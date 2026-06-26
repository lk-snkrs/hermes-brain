# Gate B2 P2 — correction packet — tenis-adidas-campus-00s-crystal-white-branco

- title: `Tênis Adidas Campus 00s Crystal White Branco`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `4`
- prefixes: `GY0042, GY0042, GY0042, GY0042`

## Status counts
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `3`

## Linhas principais
- `GY0042` | shopify_duplicate_sku_blocked | Shopify SKU `GY0042` | Tiny `GY0042` id `1056109285`
- `GY0042-1` | shopify_variant_tiny_missing | Shopify SKU `GY0042-1` | Tiny `` id ``
- `GY0042-2` | shopify_variant_tiny_missing | Shopify SKU `GY0042-2` | Tiny `` id ``
- `GY0042-3` | shopify_variant_tiny_missing | Shopify SKU `GY0042-3` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
