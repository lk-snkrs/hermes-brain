# Gate B2 P2 — correction packet — yeezy-boost-350-v2-citrin

- title: `Tênis Yeezy Boost 350 v2 Citrin Bege`
- priority: `P2_saneamento`
- lane: `TINY_DEPOSIT_PACKET`
- proposed_action: Verificar mapeamento do depósito LK | CONTROLE ESTOQUE e preparar proposta; NÃO executar write sem aprovação escopada.
- row_count: `6`
- prefixes: `FW3042, FW3042, FW3042, FW3042, FW3042, FW3042`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `3`
- shopify_variant_tiny_missing: `2`

## Linhas principais
- `FW3042` | shopify_variant_tiny_missing | Shopify SKU `FW3042` | Tiny `` id ``
- `FW3042-36` | matched_exact_sku_stock_resolved | Shopify SKU `FW3042-36` | Tiny `FW3042-36` id `937691897` | saldo LK CONTROLE: 0.0
- `FW3042-38` | matched_exact_sku_stock_resolved | Shopify SKU `FW3042-38` | Tiny `FW3042-38` id `937691903` | saldo LK CONTROLE: 0.0
- `FW3042-40` | matched_exact_sku_stock_resolved | Shopify SKU `FW3042-40` | Tiny `FW3042-40` id `937691910` | saldo LK CONTROLE: 0.0
- `FW3042-41` | matched_exact_sku_stock_missing_deposit | Shopify SKU `FW3042-41` | Tiny `FW3042-41` id `937691916`
- `FW3042-42` | shopify_variant_tiny_missing | Shopify SKU `FW3042-42` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
