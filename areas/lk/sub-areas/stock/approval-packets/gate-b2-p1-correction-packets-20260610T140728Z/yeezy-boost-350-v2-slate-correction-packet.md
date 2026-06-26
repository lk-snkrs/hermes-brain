# Gate B2 P1 — correction packet — yeezy-boost-350-v2-slate

- title: `Tênis Yeezy Boost 350 V2 Slate Bege`
- priority: `P1_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `8`
- prefixes: `HP7870, HP7870, HP7870, HP7870, HP7870, HP7870, HP7870, HP7870`

## Status counts
- matched_exact_sku_stock_resolved: `6`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `1`

## Linhas principais
- `HP7870` | shopify_duplicate_sku_blocked | Shopify SKU `HP7870` | Tiny `` id ``
- `HP7870-6` | shopify_variant_tiny_missing | Shopify SKU `HP7870-6` | Tiny `` id ``
- `HP7870-1` | matched_exact_sku_stock_resolved | Shopify SKU `HP7870-1` | Tiny `HP7870-1` id `954139835` | saldo LK CONTROLE: 0.0
- `HP7870-2` | matched_exact_sku_stock_resolved | Shopify SKU `HP7870-2` | Tiny `HP7870-2` id `954139845` | saldo LK CONTROLE: 0.0
- `HP7870-3` | matched_exact_sku_stock_resolved | Shopify SKU `HP7870-3` | Tiny `HP7870-3` id `954139849` | saldo LK CONTROLE: 0.0
- `HP7870-5` | matched_exact_sku_stock_resolved | Shopify SKU `HP7870-5` | Tiny `HP7870-5` id `960671452` | saldo LK CONTROLE: 0.0
- `HP7870-4` | matched_exact_sku_stock_resolved | Shopify SKU `HP7870-4` | Tiny `HP7870-4` id `954139853` | saldo LK CONTROLE: 0.0
- `HP7870-7` | matched_exact_sku_stock_resolved | Shopify SKU `HP7870-7` | Tiny `HP7870-7` id `1069536796` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
