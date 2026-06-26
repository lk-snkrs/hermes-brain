# Gate B2 P1 — correction packet — nike-dunk-low-ocean-bliss

- title: `Tênis Nike Dunk Low Ocean Bliss Azul`
- priority: `P1_saneamento`
- lane: `TINY_DEPOSIT_PACKET`
- proposed_action: Verificar mapeamento do depósito LK | CONTROLE ESTOQUE e preparar proposta; NÃO executar write sem aprovação escopada.
- row_count: `9`
- prefixes: `DD1503123, DD1503123, DD1503123, DD1503123, DD1503123, DD1503123, DD1503123, DD1503123, DD1503123`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `4`
- shopify_variant_tiny_missing: `4`

## Linhas principais
- `DD1503123` | matched_exact_sku_stock_resolved | Shopify SKU `DD1503123` | Tiny `DD1503123` id `944722402` | saldo LK CONTROLE: 0.0
- `DD1503123-1` | matched_exact_sku_stock_resolved | Shopify SKU `DD1503123-1` | Tiny `DD1503123-1` id `944723449` | saldo LK CONTROLE: 0.0
- `DD1503123-2` | matched_exact_sku_stock_missing_deposit | Shopify SKU `DD1503123-2` | Tiny `DD1503123-2` id `944723469`
- `DD1503123-3` | shopify_variant_tiny_missing | Shopify SKU `DD1503123-3` | Tiny `` id ``
- `DD1503123-4` | shopify_variant_tiny_missing | Shopify SKU `DD1503123-4` | Tiny `` id ``
- `DD1503123-5` | shopify_variant_tiny_missing | Shopify SKU `DD1503123-5` | Tiny `` id ``
- `DD1503123-6` | shopify_variant_tiny_missing | Shopify SKU `DD1503123-6` | Tiny `` id ``
- `DD1503123-7` | matched_exact_sku_stock_resolved | Shopify SKU `DD1503123-7` | Tiny `DD1503123-7` id `944723536` | saldo LK CONTROLE: 0.0
- `DD1503123-8` | matched_exact_sku_stock_resolved | Shopify SKU `DD1503123-8` | Tiny `DD1503123-8` id `944723547` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
