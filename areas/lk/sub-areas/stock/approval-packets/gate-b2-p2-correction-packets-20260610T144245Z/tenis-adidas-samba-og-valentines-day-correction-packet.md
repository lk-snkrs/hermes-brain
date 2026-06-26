# Gate B2 P2 — correction packet — tenis-adidas-samba-og-valentines-day

- title: `Tênis Adidas Samba OG Valentine's Day`
- priority: `P2_saneamento`
- lane: `TINY_DEPOSIT_PACKET`
- proposed_action: Verificar mapeamento do depósito LK | CONTROLE ESTOQUE e preparar proposta; NÃO executar write sem aprovação escopada.
- row_count: `7`
- prefixes: `ADI, ADI, ADI, ADI, ADI, ADI, ADI`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `3`
- shopify_variant_tiny_missing: `3`

## Linhas principais
- `ADI` | shopify_variant_tiny_missing | Shopify SKU `ADI` | Tiny `` id ``
- `ADI-9091550-34` | matched_exact_sku_stock_resolved | Shopify SKU `ADI-9091550-34` | Tiny `ADI-9091550-34` id `1069539322` | saldo LK CONTROLE: 0.0
- `ADI-9091550-35` | matched_exact_sku_stock_resolved | Shopify SKU `ADI-9091550-35` | Tiny `ADI-9091550-35` id `1068556772` | saldo LK CONTROLE: 0.0
- `ADI-9091550-36` | matched_exact_sku_stock_resolved | Shopify SKU `ADI-9091550-36` | Tiny `ADI-9091550-36` id `1069539329` | saldo LK CONTROLE: 0.0
- `ADI-9091550-37` | matched_exact_sku_stock_missing_deposit | Shopify SKU `ADI-9091550-37` | Tiny `ADI-9091550-37` id `1069539334`
- `ADI-9091550-38` | shopify_variant_tiny_missing | Shopify SKU `ADI-9091550-38` | Tiny `` id ``
- `ADI-9091550-39` | shopify_variant_tiny_missing | Shopify SKU `ADI-9091550-39` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
