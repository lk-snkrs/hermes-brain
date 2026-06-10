# Gate B2 P2 — correction packet — jaqueta-lululemon-define-nulu

- title: `Jaqueta Lululemon Define Nulu`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `16`
- prefixes: `11020158, 11020158, 11020158, 11020158, 11020158, 11020158, 11020158, 11020158, 11020158, 11020158, 11020158, 11020158, 11020158, 11020158, 11020158, 11020158`

## Status counts
- matched_exact_sku_stock_resolved: `9`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `6`

## Linhas principais
- `11020158` | shopify_duplicate_sku_blocked | Shopify SKU `11020158` | Tiny `11020158` id `1062417412`
- `11020158-1` | matched_exact_sku_stock_resolved | Shopify SKU `11020158-1` | Tiny `11020158-1` id `1062418316` | saldo LK CONTROLE: 0.0
- `11020158-11` | matched_exact_sku_stock_resolved | Shopify SKU `11020158-11` | Tiny `11020158-11` id `1062418384` | saldo LK CONTROLE: 1.0
- `11020158-12` | matched_exact_sku_stock_resolved | Shopify SKU `11020158-12` | Tiny `11020158-12` id `1062418400` | saldo LK CONTROLE: 0.0
- `11020158-13` | matched_exact_sku_stock_resolved | Shopify SKU `11020158-13` | Tiny `11020158-13` id `1062418324` | saldo LK CONTROLE: 0.0
- `11020158-14` | shopify_variant_tiny_missing | Shopify SKU `11020158-14` | Tiny `` id ``
- `11020158-15` | shopify_variant_tiny_missing | Shopify SKU `11020158-15` | Tiny `` id ``
- `11020158-17` | shopify_variant_tiny_missing | Shopify SKU `11020158-17` | Tiny `` id ``
- `11020158-18` | shopify_variant_tiny_missing | Shopify SKU `11020158-18` | Tiny `` id ``
- `11020158-2` | shopify_variant_tiny_missing | Shopify SKU `11020158-2` | Tiny `` id ``
- `11020158-3` | shopify_variant_tiny_missing | Shopify SKU `11020158-3` | Tiny `` id ``
- `11020158-5` | matched_exact_sku_stock_resolved | Shopify SKU `11020158-5` | Tiny `11020158-5` id `1062418380` | saldo LK CONTROLE: 0.0
- `11020158-6` | matched_exact_sku_stock_resolved | Shopify SKU `11020158-6` | Tiny `11020158-6` id `1062418396` | saldo LK CONTROLE: 0.0
- `11020158-7` | matched_exact_sku_stock_resolved | Shopify SKU `11020158-7` | Tiny `11020158-7` id `1062418320` | saldo LK CONTROLE: 0.0
- `11020158-8` | matched_exact_sku_stock_resolved | Shopify SKU `11020158-8` | Tiny `11020158-8` id `1062418336` | saldo LK CONTROLE: 0.0
- `11020158-9` | matched_exact_sku_stock_resolved | Shopify SKU `11020158-9` | Tiny `11020158-9` id `1062418352` | saldo LK CONTROLE: 1.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
