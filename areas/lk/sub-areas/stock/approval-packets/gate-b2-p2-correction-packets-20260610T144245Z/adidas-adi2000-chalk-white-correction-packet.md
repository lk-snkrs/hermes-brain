# Gate B2 P2 — correction packet — adidas-adi2000-chalk-white

- title: `Tênis adidas ADI2000 Chalk White Branco`
- priority: `P2_saneamento`
- lane: `TINY_DEPOSIT_PACKET`
- proposed_action: Verificar mapeamento do depósito LK | CONTROLE ESTOQUE e preparar proposta; NÃO executar write sem aprovação escopada.
- row_count: `8`
- prefixes: `GV9544, GV9544, GV9544, GV9544, GV9544, GV9544, GV9544, GV9544`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `5`
- shopify_variant_tiny_missing: `2`

## Linhas principais
- `GV9544` | shopify_variant_tiny_missing | Shopify SKU `GV9544` | Tiny `` id ``
- `GV9544-38` | matched_exact_sku_stock_resolved | Shopify SKU `GV9544-38` | Tiny `GV9544-38` id `937669177` | saldo LK CONTROLE: 0.0
- `GV9544-39` | matched_exact_sku_stock_resolved | Shopify SKU `GV9544-39` | Tiny `GV9544-39` id `937669183` | saldo LK CONTROLE: 0.0
- `GV9544-40` | matched_exact_sku_stock_resolved | Shopify SKU `GV9544-40` | Tiny `GV9544-40` id `937669189` | saldo LK CONTROLE: 0.0
- `GV9544-41` | matched_exact_sku_stock_resolved | Shopify SKU `GV9544-41` | Tiny `GV9544-41` id `937669203` | saldo LK CONTROLE: 0.0
- `GV9544-42` | matched_exact_sku_stock_resolved | Shopify SKU `GV9544-42` | Tiny `GV9544-42` id `937669216` | saldo LK CONTROLE: 0.0
- `GV9544-43` | matched_exact_sku_stock_missing_deposit | Shopify SKU `GV9544-43` | Tiny `GV9544-43` id `937669222`
- `GV9544-44` | shopify_variant_tiny_missing | Shopify SKU `GV9544-44` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
