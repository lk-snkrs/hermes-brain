# Gate B2 P2 — correction packet — tenis-new-balance-530-stoneware-line-branco

- title: `Tênis New Balance 530 Stoneware Line Branco`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `4`
- prefixes: `MR530RD, MR530RD, MR530RD, MR530RD`

## Status counts
- matched_exact_sku_stock_resolved: `3`
- shopify_duplicate_sku_blocked: `1`

## Linhas principais
- `MR530RD` | shopify_duplicate_sku_blocked | Shopify SKU `MR530RD` | Tiny `MR530RD` id `1056864454` | saldo LK CONTROLE: 0.0
- `MR530RD-1` | matched_exact_sku_stock_resolved | Shopify SKU `MR530RD-1` | Tiny `MR530RD-1` id `1056864458` | saldo LK CONTROLE: 0.0
- `MR530RD-2` | matched_exact_sku_stock_resolved | Shopify SKU `MR530RD-2` | Tiny `MR530RD-2` id `1056864461` | saldo LK CONTROLE: 0.0
- `MR530RD-3` | matched_exact_sku_stock_resolved | Shopify SKU `MR530RD-3` | Tiny `MR530RD-3` id `1056864464` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
