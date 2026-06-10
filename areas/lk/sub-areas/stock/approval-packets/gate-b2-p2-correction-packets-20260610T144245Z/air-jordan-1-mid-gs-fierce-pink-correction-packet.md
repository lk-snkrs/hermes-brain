# Gate B2 P2 — correction packet — air-jordan-1-mid-gs-fierce-pink

- title: `Tênis Nike Air Jordan 1 Mid GS Fierce Pink Rosa`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `3`
- prefixes: `FD8780116, FD8780116, FD8780116`

## Status counts
- matched_exact_sku_stock_resolved: `1`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `1`

## Linhas principais
- `FD8780116` | shopify_duplicate_sku_blocked | Shopify SKU `FD8780116` | Tiny `` id ``
- `FD8780116-1` | shopify_variant_tiny_missing | Shopify SKU `FD8780116-1` | Tiny `` id ``
- `FD8780116-2` | matched_exact_sku_stock_resolved | Shopify SKU `FD8780116-2` | Tiny `FD8780116-2` id `1055963642` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
