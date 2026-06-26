# Gate B2 P2 — correction packet — tenis-adidas-samba-x-wales-bonner-wonder-white-marrom

- title: `Tênis adidas Samba x Wales Bonner Wonder White Marrom`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `4`
- prefixes: `IH3261, IH3261, IH3261, IH3261`

## Status counts
- matched_exact_sku_stock_resolved: `1`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `2`

## Linhas principais
- `IH3261` | shopify_duplicate_sku_blocked | Shopify SKU `IH3261` | Tiny `` id ``
- `IH3261-1` | shopify_variant_tiny_missing | Shopify SKU `IH3261-1` | Tiny `` id ``
- `IH3261-2` | shopify_variant_tiny_missing | Shopify SKU `IH3261-2` | Tiny `` id ``
- `IH3261-3` | matched_exact_sku_stock_resolved | Shopify SKU `IH3261-3` | Tiny `IH3261-3` id `1061045199` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
