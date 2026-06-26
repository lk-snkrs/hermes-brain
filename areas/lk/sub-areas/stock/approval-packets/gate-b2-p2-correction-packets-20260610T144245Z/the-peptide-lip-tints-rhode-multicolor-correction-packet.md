# Gate B2 P2 — correction packet — the-peptide-lip-tints-rhode-multicolor

- title: `The Peptide Lip Tints Rhode Multicolor`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `16`
- prefixes: `LIP, LIP, LIP, LIP, LIP, LIP, LIP, LIP, LIP, LIP, LIP, LIP, LIP, LIP, LIP, LIP`

## Status counts
- matched_exact_sku_stock_resolved: `9`
- shopify_duplicate_sku_blocked: `3`
- shopify_variant_tiny_missing: `4`

## Linhas principais
- `LIP` | shopify_duplicate_sku_blocked | Shopify SKU `LIP` | Tiny `` id ``
- `LIP5` | shopify_duplicate_sku_blocked | Shopify SKU `LIP5` | Tiny `LIP5` id `1064344057` | saldo LK CONTROLE: 0.0
- `LIP6` | matched_exact_sku_stock_resolved | Shopify SKU `LIP6` | Tiny `LIP6` id `1064346849` | saldo LK CONTROLE: 0.0
- `LIP7-9` | matched_exact_sku_stock_resolved | Shopify SKU `LIP7-9` | Tiny `LIP7-9` id `1064347287` | saldo LK CONTROLE: 0.0
- `LIPCASE-1` | matched_exact_sku_stock_resolved | Shopify SKU `LIPCASE-1` | Tiny `LIPCASE-1` id `1061753908` | saldo LK CONTROLE: 0.0
- `LIPCASE-10` | matched_exact_sku_stock_resolved | Shopify SKU `LIPCASE-10` | Tiny `LIPCASE-10` id `1061753937` | saldo LK CONTROLE: 0.0
- `LIPCASE-11` | shopify_duplicate_sku_blocked | Shopify SKU `LIPCASE-11` | Tiny `LIPCASE-11` id `1061753940` | saldo LK CONTROLE: 0.0
- `LIPCASE-2` | matched_exact_sku_stock_resolved | Shopify SKU `LIPCASE-2` | Tiny `LIPCASE-2` id `1061753911` | saldo LK CONTROLE: 0.0
- `LIPCASE-3` | matched_exact_sku_stock_resolved | Shopify SKU `LIPCASE-3` | Tiny `LIPCASE-3` id `1061753914` | saldo LK CONTROLE: 0.0
- `LIPCASE-4` | matched_exact_sku_stock_resolved | Shopify SKU `LIPCASE-4` | Tiny `LIPCASE-4` id `1061753917` | saldo LK CONTROLE: 0.0
- `LIPCASE-5` | shopify_variant_tiny_missing | Shopify SKU `LIPCASE-5` | Tiny `` id ``
- `LIPCASE-6` | shopify_variant_tiny_missing | Shopify SKU `LIPCASE-6` | Tiny `` id ``
- `LIPCASE-7` | shopify_variant_tiny_missing | Shopify SKU `LIPCASE-7` | Tiny `` id ``
- `LIPCASE-8` | shopify_variant_tiny_missing | Shopify SKU `LIPCASE-8` | Tiny `` id ``
- `LIPCASE-9` | matched_exact_sku_stock_resolved | Shopify SKU `LIPCASE-9` | Tiny `LIPCASE-9` id `1061753934` | saldo LK CONTROLE: 0.0
- `LIPCASE2-1` | matched_exact_sku_stock_resolved | Shopify SKU `LIPCASE2-1` | Tiny `LIPCASE2-1` id `1061754065` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
