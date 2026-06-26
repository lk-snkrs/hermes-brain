# Gate B2 P1 — correction packet — air-jordan-1-mid-se-space-jam

- title: `Tênis Nike Air Jordan 1 Mid SE Space Jam Preto ou`
- priority: `P1_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `9`
- prefixes: `DV1308004, DV1308004, DV1308004, DV1308004, DV1308004, DV1308004, DV1308004, DV1308004, DV1308004`

## Status counts
- matched_exact_sku_stock_resolved: `4`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `3`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `DV1308004` | shopify_duplicate_sku_blocked | Shopify SKU `DV1308004` | Tiny `` id ``
- `DV1308004-2` | shopify_variant_tiny_missing | Shopify SKU `DV1308004-2` | Tiny `` id ``
- `DV1308004-4` | shopify_variant_tiny_missing | Shopify SKU `DV1308004-4` | Tiny `` id ``
- `DV1308004-5` | shopify_variant_tiny_missing | Shopify SKU `DV1308004-5` | Tiny `` id ``
- `DV1308004-6` | matched_exact_sku_stock_resolved | Shopify SKU `DV1308004-6` | Tiny `DV1308004-6` id `921334778` | saldo LK CONTROLE: 1.0
- `DV1308004-7` | matched_exact_sku_stock_resolved | Shopify SKU `DV1308004-7` | Tiny `DV1308004-7` id `921334784` | saldo LK CONTROLE: 0.0
- `DV1308004-8` | matched_exact_sku_stock_resolved | Shopify SKU `DV1308004-8` | Tiny `DV1308004-8` id `921334789` | saldo LK CONTROLE: 0.0
- `DV1308004-9` | matched_exact_sku_stock_resolved | Shopify SKU `DV1308004-9` | Tiny `DV1308004-9` id `921334793` | saldo LK CONTROLE: 0.0
- `DV1308004-10` | tiny_duplicate_exact_code_blocked | Shopify SKU `DV1308004-10` | Tiny `DV1308004-10` id `921334724`

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
