# Gate B2 P2 — correction packet — tenis-adidas-tokyo-mary-jane-cream-white-red-gold-metallic-creme

- title: `Tênis Adidas Tokyo Mary Jane Cream White Red Gold Metallic Creme`
- priority: `P2_saneamento`
- lane: `TINY_DEPOSIT_PACKET`
- proposed_action: Verificar mapeamento do depósito LK | CONTROLE ESTOQUE e preparar proposta; NÃO executar write sem aprovação escopada.
- row_count: `8`
- prefixes: `IH3999, IH3999, IH3999, IH3999, IH3999, IH3999, IH3999, IH3999`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `2`
- shopify_variant_tiny_missing: `5`

## Linhas principais
- `IH3999` | shopify_variant_tiny_missing | Shopify SKU `IH3999` | Tiny `` id ``
- `IH3999-34` | matched_exact_sku_stock_resolved | Shopify SKU `IH3999-34` | Tiny `IH3999-34` id `1070120505` | saldo LK CONTROLE: 0.0
- `IH3999-35` | matched_exact_sku_stock_resolved | Shopify SKU `IH3999-35` | Tiny `IH3999-35` id `1070120510` | saldo LK CONTROLE: 0.0
- `IH3999-36` | matched_exact_sku_stock_missing_deposit | Shopify SKU `IH3999-36` | Tiny `IH3999-36` id `1070120515`
- `IH3999-37` | shopify_variant_tiny_missing | Shopify SKU `IH3999-37` | Tiny `` id ``
- `IH3999-38` | shopify_variant_tiny_missing | Shopify SKU `IH3999-38` | Tiny `` id ``
- `IH3999-39` | shopify_variant_tiny_missing | Shopify SKU `IH3999-39` | Tiny `` id ``
- `IH3999-40` | shopify_variant_tiny_missing | Shopify SKU `IH3999-40` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
