# Gate B2 P1 — correction packet — nike-dunk-sb-dunk-low-qs-bhm-rodeo-verde

- title: `Nike Dunk SB Dunk Low QS BHM Rodeo Verde`
- priority: `P1_saneamento`
- lane: `TINY_DEPOSIT_PACKET`
- proposed_action: Verificar mapeamento do depósito LK | CONTROLE ESTOQUE e preparar proposta; NÃO executar write sem aprovação escopada.
- row_count: `9`
- prefixes: `HF3058, HF3058, HF3058, HF3058, HF3058, HF3058, HF3058, HF3058, HF3058`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `3`
- shopify_variant_tiny_missing: `5`

## Linhas principais
- `HF3058` | shopify_variant_tiny_missing | Shopify SKU `HF3058` | Tiny `` id ``
- `HF3058-300-1` | matched_exact_sku_stock_resolved | Shopify SKU `HF3058-300-1` | Tiny `HF3058-300-1` id `1063617193` | saldo LK CONTROLE: 0.0
- `HF3058-300-2` | matched_exact_sku_stock_missing_deposit | Shopify SKU `HF3058-300-2` | Tiny `HF3058-300-2` id `1063617196`
- `HF3058-300-3` | shopify_variant_tiny_missing | Shopify SKU `HF3058-300-3` | Tiny `` id ``
- `HF3058-300-4` | shopify_variant_tiny_missing | Shopify SKU `HF3058-300-4` | Tiny `` id ``
- `HF3058-300-5` | shopify_variant_tiny_missing | Shopify SKU `HF3058-300-5` | Tiny `` id ``
- `HF3058-300` | shopify_variant_tiny_missing | Shopify SKU `HF3058-300` | Tiny `` id ``
- `HF3058-300-6` | matched_exact_sku_stock_resolved | Shopify SKU `HF3058-300-6` | Tiny `HF3058-300-6` id `1063617208` | saldo LK CONTROLE: 0.0
- `HF3058-300-7` | matched_exact_sku_stock_resolved | Shopify SKU `HF3058-300-7` | Tiny `HF3058-300-7` id `1063617211` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
