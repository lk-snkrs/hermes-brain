# Gate B2 P2 — correction packet — yeezy-boost-350-v2-zebra

- title: `Tênis Yeezy Boost 350 v2 Zebra Branco`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `7`
- prefixes: `CP9654, CP9654, CP9654, CP9654, CP9654, CP9654, CP9654`

## Status counts
- matched_exact_sku_stock_resolved: `1`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `5`

## Linhas principais
- `CP9654` | shopify_duplicate_sku_blocked | Shopify SKU `CP9654` | Tiny `` id ``
- `CP9654-5` | matched_exact_sku_stock_resolved | Shopify SKU `CP9654-5` | Tiny `CP9654-5` id `1069807743` | saldo LK CONTROLE: 0.0
- `CP9654-1` | shopify_variant_tiny_missing | Shopify SKU `CP9654-1` | Tiny `` id ``
- `CP9654-2` | shopify_variant_tiny_missing | Shopify SKU `CP9654-2` | Tiny `` id ``
- `CP9654-4` | shopify_variant_tiny_missing | Shopify SKU `CP9654-4` | Tiny `` id ``
- `CP9654-3` | shopify_variant_tiny_missing | Shopify SKU `CP9654-3` | Tiny `` id ``
- `CP9654-6` | shopify_variant_tiny_missing | Shopify SKU `CP9654-6` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
