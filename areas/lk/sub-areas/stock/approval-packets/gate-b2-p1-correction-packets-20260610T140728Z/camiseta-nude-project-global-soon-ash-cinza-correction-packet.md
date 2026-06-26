# Gate B2 P1 — correction packet — camiseta-nude-project-global-soon-ash-cinza

- title: `Camiseta Nude Project Global Soon Ash Cinza`
- priority: `P1_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `6`
- prefixes: `NDP006, NDP006, NDP006, NDP006, NDP006, NDP006`

## Status counts
- matched_exact_sku_stock_resolved: `1`
- shopify_duplicate_sku_blocked: `5`

## Linhas principais
- `NDP006` | matched_exact_sku_stock_resolved | Shopify SKU `NDP006` | Tiny `NDP006` id `1064561653` | saldo LK CONTROLE: 0.0
- `NDP006-1` | shopify_duplicate_sku_blocked | Shopify SKU `NDP006-1` | Tiny `NDP006-1` id `1064561659` | saldo LK CONTROLE: 0.0
- `NDP006-2` | shopify_duplicate_sku_blocked | Shopify SKU `NDP006-2` | Tiny `NDP006-2` id `1064561662` | saldo LK CONTROLE: 2.0
- `NDP006-3` | shopify_duplicate_sku_blocked | Shopify SKU `NDP006-3` | Tiny `NDP006-3` id `1064561665` | saldo LK CONTROLE: 1.0
- `NDP006-4` | shopify_duplicate_sku_blocked | Shopify SKU `NDP006-4` | Tiny `NDP006-4` id `1064561668` | saldo LK CONTROLE: 1.0
- `NDP006-5` | shopify_duplicate_sku_blocked | Shopify SKU `NDP006-5` | Tiny `NDP006-5` id `1064561671` | saldo LK CONTROLE: 1.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
