# Gate B2 P2 — correction packet — tenis-new-balance-9060-moonbeam-vintage-rose-lime-colorido

- title: `Tênis New Balance 9060 Moonbeam Vintage Rose Lime Colorido`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `5`
- prefixes: `U9060GCB, U9060GCB, U9060GCB, U9060GCB, U9060GCB`

## Status counts
- matched_exact_sku_stock_resolved: `1`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `3`

## Linhas principais
- `U9060GCB` | shopify_duplicate_sku_blocked | Shopify SKU `U9060GCB` | Tiny `U9060GCB` id `1056978997`
- `U9060GCB-1` | shopify_variant_tiny_missing | Shopify SKU `U9060GCB-1` | Tiny `` id ``
- `U9060GCB-2` | shopify_variant_tiny_missing | Shopify SKU `U9060GCB-2` | Tiny `` id ``
- `U9060GCB-4` | shopify_variant_tiny_missing | Shopify SKU `U9060GCB-4` | Tiny `` id ``
- `U9060GCB-6` | matched_exact_sku_stock_resolved | Shopify SKU `U9060GCB-6` | Tiny `U9060GCB-6` id `1066015861` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
