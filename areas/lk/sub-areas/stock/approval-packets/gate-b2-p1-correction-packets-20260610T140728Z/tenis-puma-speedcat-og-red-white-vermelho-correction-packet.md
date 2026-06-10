# Gate B2 P1 — correction packet — tenis-puma-speedcat-og-red-white-vermelho

- title: `Tênis Puma Speedcat Og Red White Vermelho`
- priority: `P1_saneamento`
- lane: `TINY_DEPOSIT_PACKET`
- proposed_action: Verificar mapeamento do depósito LK | CONTROLE ESTOQUE e preparar proposta; NÃO executar write sem aprovação escopada.
- row_count: `7`
- prefixes: `39884602, 39884602, 39884602, 39884602, 39884602, 39884602, 39884602`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `3`
- shopify_variant_tiny_missing: `3`

## Linhas principais
- `39884602` | shopify_variant_tiny_missing | Shopify SKU `39884602` | Tiny `` id ``
- `39884602-1` | matched_exact_sku_stock_resolved | Shopify SKU `39884602-1` | Tiny `39884602-1` id `1060432337` | saldo LK CONTROLE: 0.0
- `39884602-2` | matched_exact_sku_stock_resolved | Shopify SKU `39884602-2` | Tiny `39884602-2` id `1060432340` | saldo LK CONTROLE: 0.0
- `39884602-3` | matched_exact_sku_stock_resolved | Shopify SKU `39884602-3` | Tiny `39884602-3` id `1060432343` | saldo LK CONTROLE: 0.0
- `39884602-4` | matched_exact_sku_stock_missing_deposit | Shopify SKU `39884602-4` | Tiny `39884602-4` id `1060432346`
- `39884602-5` | shopify_variant_tiny_missing | Shopify SKU `39884602-5` | Tiny `` id ``
- `39884602-6` | shopify_variant_tiny_missing | Shopify SKU `39884602-6` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
