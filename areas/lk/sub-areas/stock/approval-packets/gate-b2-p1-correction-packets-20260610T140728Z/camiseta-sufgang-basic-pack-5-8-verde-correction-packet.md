# Gate B2 P1 — correction packet — camiseta-sufgang-basic-pack-5-8-verde

- title: `Camiseta Sufgang Basic Pack 5.8 Verde`
- priority: `P1_saneamento`
- lane: `TINY_DEPOSIT_PACKET`
- proposed_action: Verificar mapeamento do depósito LK | CONTROLE ESTOQUE e preparar proposta; NÃO executar write sem aprovação escopada.
- row_count: `6`
- prefixes: `SF2BSP5, SF2BSP5, SF2BSP5, SF2BSP5, SF2BSP5, SF2BSP5`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `2`
- shopify_variant_tiny_missing: `3`

## Linhas principais
- `SF2BSP5` | matched_exact_sku_stock_resolved | Shopify SKU `SF2BSP5` | Tiny `SF2BSP5` id `1057573376` | saldo LK CONTROLE: 0.0
- `SF2BSP5-1` | matched_exact_sku_stock_resolved | Shopify SKU `SF2BSP5-1` | Tiny `SF2BSP5-1` id `1057573455` | saldo LK CONTROLE: 0.0
- `SF2BSP5-2` | matched_exact_sku_stock_missing_deposit | Shopify SKU `SF2BSP5-2` | Tiny `SF2BSP5-2` id `1057573458`
- `SF2BSP5-3` | shopify_variant_tiny_missing | Shopify SKU `SF2BSP5-3` | Tiny `` id ``
- `SF2BSP5-4` | shopify_variant_tiny_missing | Shopify SKU `SF2BSP5-4` | Tiny `` id ``
- `SF2BSP5-5` | shopify_variant_tiny_missing | Shopify SKU `SF2BSP5-5` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
