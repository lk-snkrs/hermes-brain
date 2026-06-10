# Gate B2 P1 — correction packet — tenis-new-balance-1000-x-aime-leon-dore-sea-salt-concrete-branco

- title: `Tênis New Balance 1000 x Aimé Leon Dore Sea Salt Concrete Branco`
- priority: `P1_saneamento`
- lane: `TINY_DUPLICATE_PACKET`
- proposed_action: Preparar saneamento Tiny de código duplicado e rollback/readback; NÃO executar write sem aprovação escopada.
- row_count: `13`
- prefixes: `M1000AC1, M1000AC1, M1000AC1, M1000AC1, M1000AC1, M1000AC1, M1000AC1, M1000AC1, M1000AC1, M1000AC1, M1000AC1, M1000AC1, M1000AC1`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `8`
- shopify_variant_tiny_missing: `3`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `M1000AC1` | shopify_variant_tiny_missing | Shopify SKU `M1000AC1` | Tiny `` id ``
- `M1000AC1-1` | matched_exact_sku_stock_resolved | Shopify SKU `M1000AC1-1` | Tiny `M1000AC1-1` id `1058670867` | saldo LK CONTROLE: 0.0
- `M1000AC1-2` | matched_exact_sku_stock_missing_deposit | Shopify SKU `M1000AC1-2` | Tiny `M1000AC1-2` id `1058670870`
- `M1000AC1-3` | shopify_variant_tiny_missing | Shopify SKU `M1000AC1-3` | Tiny `` id ``
- `M1000AC1-4` | shopify_variant_tiny_missing | Shopify SKU `M1000AC1-4` | Tiny `` id ``
- `M1000AC1-5` | matched_exact_sku_stock_resolved | Shopify SKU `M1000AC1-5` | Tiny `M1000AC1-5` id `1058670879` | saldo LK CONTROLE: 0.0
- `M1000AC1-6` | matched_exact_sku_stock_resolved | Shopify SKU `M1000AC1-6` | Tiny `M1000AC1-6` id `1058670882` | saldo LK CONTROLE: 1.0
- `M1000AC1-12` | tiny_duplicate_exact_code_blocked | Shopify SKU `M1000AC1-12` | Tiny `M1000AC1-12` id `1058670855`
- `M1000AC1-7` | matched_exact_sku_stock_resolved | Shopify SKU `M1000AC1-7` | Tiny `M1000AC1-7` id `1058670885` | saldo LK CONTROLE: 0.0
- `M1000AC1-8` | matched_exact_sku_stock_resolved | Shopify SKU `M1000AC1-8` | Tiny `M1000AC1-8` id `1058670888` | saldo LK CONTROLE: 0.0
- `M1000AC1-9` | matched_exact_sku_stock_resolved | Shopify SKU `M1000AC1-9` | Tiny `M1000AC1-9` id `1058670891` | saldo LK CONTROLE: 0.0
- `M1000AC1-10` | matched_exact_sku_stock_resolved | Shopify SKU `M1000AC1-10` | Tiny `M1000AC1-10` id `1058670894` | saldo LK CONTROLE: 0.0
- `M1000AC1-11` | matched_exact_sku_stock_resolved | Shopify SKU `M1000AC1-11` | Tiny `M1000AC1-11` id `1058670897` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
