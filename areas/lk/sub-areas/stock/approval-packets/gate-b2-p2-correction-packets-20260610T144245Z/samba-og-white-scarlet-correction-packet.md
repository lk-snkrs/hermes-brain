# Gate B2 P2 — correction packet — samba-og-white-scarlet

- title: `Tênis Adidas Samba OG White Scarlet Branco`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `4`
- prefixes: `IG1025, IG1025, IG1025, IG1025`

## Status counts
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `3`

## Linhas principais
- `IG1025` | shopify_duplicate_sku_blocked | Shopify SKU `IG1025` | Tiny `` id ``
- `ig1025-2` | shopify_variant_tiny_missing | Shopify SKU `ig1025-2` | Tiny `` id ``
- `ig1025-4` | shopify_variant_tiny_missing | Shopify SKU `ig1025-4` | Tiny `` id ``
- `ig1025-5` | shopify_variant_tiny_missing | Shopify SKU `ig1025-5` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
