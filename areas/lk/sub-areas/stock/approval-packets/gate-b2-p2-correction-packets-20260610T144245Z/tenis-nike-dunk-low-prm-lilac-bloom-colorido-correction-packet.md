# Gate B2 P2 — correction packet — tenis-nike-dunk-low-prm-lilac-bloom-colorido

- title: `Tênis Nike Dunk Low PRM Lilac Bloom Colorido`
- priority: `P2_saneamento`
- lane: `TINY_DEPOSIT_PACKET`
- proposed_action: Verificar mapeamento do depósito LK | CONTROLE ESTOQUE e preparar proposta; NÃO executar write sem aprovação escopada.
- row_count: `7`
- prefixes: `FB7910, FB7910, FB7910, FB7910, FB7910, FB7910, FB7910`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `4`
- shopify_variant_tiny_missing: `2`

## Linhas principais
- `FB7910` | shopify_variant_tiny_missing | Shopify SKU `FB7910` | Tiny `` id ``
- `FB7910-500-1` | matched_exact_sku_stock_resolved | Shopify SKU `FB7910-500-1` | Tiny `FB7910-500-1` id `1057448285` | saldo LK CONTROLE: 0.0
- `FB7910-500-2` | matched_exact_sku_stock_resolved | Shopify SKU `FB7910-500-2` | Tiny `FB7910-500-2` id `1057448288` | saldo LK CONTROLE: 0.0
- `FB7910-500-3` | matched_exact_sku_stock_resolved | Shopify SKU `FB7910-500-3` | Tiny `FB7910-500-3` id `1057448291` | saldo LK CONTROLE: 0.0
- `FB7910-500-4` | matched_exact_sku_stock_resolved | Shopify SKU `FB7910-500-4` | Tiny `FB7910-500-4` id `1057448294` | saldo LK CONTROLE: 0.0
- `FB7910-500-5` | matched_exact_sku_stock_missing_deposit | Shopify SKU `FB7910-500-5` | Tiny `FB7910-500-5` id `1057448297`
- `FB7910-500-6` | shopify_variant_tiny_missing | Shopify SKU `FB7910-500-6` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
