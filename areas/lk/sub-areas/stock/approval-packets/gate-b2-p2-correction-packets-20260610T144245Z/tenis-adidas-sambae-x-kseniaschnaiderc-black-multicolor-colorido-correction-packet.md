# Gate B2 P2 — correction packet — tenis-adidas-sambae-x-kseniaschnaiderc-black-multicolor-colorido

- title: `Tênis adidas Sambae x KSENIASCHNAIDER Black Multicolor Colorido`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `2`
- prefixes: `ID0444, ID0444`

## Status counts
- matched_exact_sku_stock_resolved: `1`
- shopify_duplicate_sku_blocked: `1`

## Linhas principais
- `ID0444` | shopify_duplicate_sku_blocked | Shopify SKU `ID0444` | Tiny `ID0444` id `1057191297`
- `ID0444-1` | matched_exact_sku_stock_resolved | Shopify SKU `ID0444-1` | Tiny `ID0444-1` id `1057191299` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
