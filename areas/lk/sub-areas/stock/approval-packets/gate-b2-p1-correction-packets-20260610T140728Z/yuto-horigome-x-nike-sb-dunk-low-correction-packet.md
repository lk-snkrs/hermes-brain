# Gate B2 P1 — correction packet — yuto-horigome-x-nike-sb-dunk-low

- title: `Tênis Yuto Horigome x Nike SB Dunk Low Azul`
- priority: `P1_saneamento`
- lane: `TINY_DUPLICATE_PACKET`
- proposed_action: Preparar saneamento Tiny de código duplicado e rollback/readback; NÃO executar write sem aprovação escopada.
- row_count: `9`
- prefixes: `FQ1180001, FQ1180001, FQ1180001, FQ1180001, FQ1180001, FQ1180001, FQ1180001, FQ1180001, FQ1180001`

## Status counts
- matched_exact_sku_stock_resolved: `6`
- shopify_variant_tiny_missing: `2`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `FQ1180001` | shopify_variant_tiny_missing | Shopify SKU `FQ1180001` | Tiny `` id ``
- `FQ1180001-1` | shopify_variant_tiny_missing | Shopify SKU `FQ1180001-1` | Tiny `` id ``
- `FQ1180001-2` | matched_exact_sku_stock_resolved | Shopify SKU `FQ1180001-2` | Tiny `FQ1180001-2` id `1009294900` | saldo LK CONTROLE: 0.0
- `FQ1180001-3` | matched_exact_sku_stock_resolved | Shopify SKU `FQ1180001-3` | Tiny `FQ1180001-3` id `1009294912` | saldo LK CONTROLE: 0.0
- `FQ1180001-4` | matched_exact_sku_stock_resolved | Shopify SKU `FQ1180001-4` | Tiny `FQ1180001-4` id `1009294933` | saldo LK CONTROLE: 0.0
- `FQ1180001-5` | matched_exact_sku_stock_resolved | Shopify SKU `FQ1180001-5` | Tiny `FQ1180001-5` id `1009294949` | saldo LK CONTROLE: 0.0
- `FQ1180001-6` | tiny_duplicate_exact_code_blocked | Shopify SKU `FQ1180001-6` | Tiny `FQ1180001-6` id `1009294889`
- `FQ1180001-10` | matched_exact_sku_stock_resolved | Shopify SKU `FQ1180001-10` | Tiny `FQ1180001-10` id `1066455538` | saldo LK CONTROLE: 1.0
- `FQ1180001-11` | matched_exact_sku_stock_resolved | Shopify SKU `FQ1180001-11` | Tiny `FQ1180001-11` id `1069767383` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
