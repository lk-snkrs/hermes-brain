# Gate B2 P1 — correction packet — tenis-adidas-gazelle-indoor-collegiate-green-verde

- title: `Tênis adidas Gazelle Indoor Collegiate Green Verde`
- priority: `P1_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `5`
- prefixes: `IG5929, IG5929, IG5929, IG5929, IG5929`

## Status counts
- shopify_duplicate_sku_blocked: `3`
- shopify_variant_tiny_missing: `1`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `IG5929` | shopify_variant_tiny_missing | Shopify SKU `IG5929` | Tiny `` id ``
- `IG5929-1` | shopify_duplicate_sku_blocked | Shopify SKU `IG5929-1` | Tiny `IG5929-1` id `1057191002`
- `IG5929-7` | tiny_duplicate_exact_code_blocked | Shopify SKU `IG5929-7` | Tiny `IG5929-7` id `1057190995`
- `IG5929-3` | shopify_duplicate_sku_blocked | Shopify SKU `IG5929-3` | Tiny `` id ``
- `IG5929-5` | shopify_duplicate_sku_blocked | Shopify SKU `IG5929-5` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
