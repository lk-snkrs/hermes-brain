# Gate B2 P1 — correction packet — tenis-new-balance-530-silver-white-branco

- title: `Tênis New Balance 530 Silver White Branco`
- priority: `P1_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `8`
- prefixes: `MR530EMA, MR530EMA, MR530EMA, MR530EMA, MR530EMA, MR530EMA, MR530EMA, MR530EMA`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `5`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `1`

## Linhas principais
- `MR530EMA` | shopify_duplicate_sku_blocked | Shopify SKU `MR530EMA` | Tiny `` id ``
- `MR530EMA-6` | matched_exact_sku_stock_resolved | Shopify SKU `MR530EMA-6` | Tiny `MR530EMA-6` id `1061510461` | saldo LK CONTROLE: 0.0
- `MR530EMA-3` | matched_exact_sku_stock_resolved | Shopify SKU `MR530EMA-3` | Tiny `MR530EMA-3` id `1061435623` | saldo LK CONTROLE: 1.0
- `MR530EMA-2` | matched_exact_sku_stock_resolved | Shopify SKU `MR530EMA-2` | Tiny `MR530EMA-2` id `1061435620` | saldo LK CONTROLE: 1.0
- `MR530EMA-1` | matched_exact_sku_stock_resolved | Shopify SKU `MR530EMA-1` | Tiny `MR530EMA-1` id `1061046859` | saldo LK CONTROLE: 0.0
- `MR530EMA-5` | matched_exact_sku_stock_resolved | Shopify SKU `MR530EMA-5` | Tiny `MR530EMA-5` id `1061435629` | saldo LK CONTROLE: 1.0
- `MR530EMA-7` | matched_exact_sku_stock_missing_deposit | Shopify SKU `MR530EMA-7` | Tiny `MR530EMA-7` id `1066423085`
- `MR530EMA-4` | shopify_variant_tiny_missing | Shopify SKU `MR530EMA-4` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
