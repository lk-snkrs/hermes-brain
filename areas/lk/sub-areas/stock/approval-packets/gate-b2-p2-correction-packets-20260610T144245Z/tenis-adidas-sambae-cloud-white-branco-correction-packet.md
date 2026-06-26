# Gate B2 P2 — correction packet — tenis-adidas-sambae-cloud-white-branco

- title: `Tênis adidas Sambae Cloud White Black Branco`
- priority: `P2_saneamento`
- lane: `TINY_DEPOSIT_PACKET`
- proposed_action: Verificar mapeamento do depósito LK | CONTROLE ESTOQUE e preparar proposta; NÃO executar write sem aprovação escopada.
- row_count: `7`
- prefixes: `IG5744, IG5744, IG5744, IG5744, IG5744, IG5744, IG5744`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `2`
- shopify_variant_tiny_missing: `4`

## Linhas principais
- `IG5744` | matched_exact_sku_stock_missing_deposit | Shopify SKU `IG5744` | Tiny `IG5744` id `1057111972`
- `IG5744-1` | shopify_variant_tiny_missing | Shopify SKU `IG5744-1` | Tiny `` id ``
- `IG5744-2` | shopify_variant_tiny_missing | Shopify SKU `IG5744-2` | Tiny `` id ``
- `IG5744-3` | shopify_variant_tiny_missing | Shopify SKU `IG5744-3` | Tiny `` id ``
- `IG5744-4` | shopify_variant_tiny_missing | Shopify SKU `IG5744-4` | Tiny `` id ``
- `IG5744-5` | matched_exact_sku_stock_resolved | Shopify SKU `IG5744-5` | Tiny `IG5744-5` id `1057111991` | saldo LK CONTROLE: 0.0
- `IG5744-6` | matched_exact_sku_stock_resolved | Shopify SKU `IG5744-6` | Tiny `IG5744-6` id `1057111994` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
