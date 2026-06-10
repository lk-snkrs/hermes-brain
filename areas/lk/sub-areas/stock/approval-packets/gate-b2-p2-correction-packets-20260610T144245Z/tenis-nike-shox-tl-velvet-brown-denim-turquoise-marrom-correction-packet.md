# Gate B2 P2 — correction packet — tenis-nike-shox-tl-velvet-brown-denim-turquoise-marrom

- title: `Tênis Nike Shox TL Velvet Brown Denim Turquoise Marrom`
- priority: `P2_saneamento`
- lane: `TINY_DEPOSIT_PACKET`
- proposed_action: Verificar mapeamento do depósito LK | CONTROLE ESTOQUE e preparar proposta; NÃO executar write sem aprovação escopada.
- row_count: `7`
- prefixes: `IB4340, IB4340, IB4340, IB4340, IB4340, IB4340, IB4340`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `3`
- shopify_variant_tiny_missing: `3`

## Linhas principais
- `IB4340` | shopify_variant_tiny_missing | Shopify SKU `IB4340` | Tiny `` id ``
- `IB4340-200-37` | matched_exact_sku_stock_resolved | Shopify SKU `IB4340-200-37` | Tiny `IB4340-200-37` id `1070658885` | saldo LK CONTROLE: 0.0
- `IB4340-200-38` | matched_exact_sku_stock_resolved | Shopify SKU `IB4340-200-38` | Tiny `IB4340-200-38` id `1070658890` | saldo LK CONTROLE: 0.0
- `IB4340-200-39` | matched_exact_sku_stock_resolved | Shopify SKU `IB4340-200-39` | Tiny `IB4340-200-39` id `1070658895` | saldo LK CONTROLE: 0.0
- `IB4340-200-40` | matched_exact_sku_stock_missing_deposit | Shopify SKU `IB4340-200-40` | Tiny `IB4340-200-40` id `1070658900`
- `IB4340-200-41` | shopify_variant_tiny_missing | Shopify SKU `IB4340-200-41` | Tiny `` id ``
- `IB4340-200-42` | shopify_variant_tiny_missing | Shopify SKU `IB4340-200-42` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
