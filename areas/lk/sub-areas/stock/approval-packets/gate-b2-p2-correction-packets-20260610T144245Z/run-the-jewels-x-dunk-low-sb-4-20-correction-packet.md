# Gate B2 P2 — correction packet — run-the-jewels-x-dunk-low-sb-4-20

- title: `Tênis Run The Jewels x Dunk Low SB '4/20' Azul`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `5`
- prefixes: `DO9404400, DO9404400, DO9404400, DO9404400, DO9404400`

## Status counts
- matched_exact_sku_stock_resolved: `4`
- shopify_duplicate_sku_blocked: `1`

## Linhas principais
- `DO9404400` | shopify_duplicate_sku_blocked | Shopify SKU `DO9404400` | Tiny `DO9404400` id `1068503990` | saldo LK CONTROLE: 0.0
- `DO9404400-39` | matched_exact_sku_stock_resolved | Shopify SKU `DO9404400-39` | Tiny `DO9404400-39` id `937688004` | saldo LK CONTROLE: 0.0
- `DO9404400-40` | matched_exact_sku_stock_resolved | Shopify SKU `DO9404400-40` | Tiny `DO9404400-40` id `937688010` | saldo LK CONTROLE: 0.0
- `DO9404400-40.5` | matched_exact_sku_stock_resolved | Shopify SKU `DO9404400-40.5` | Tiny `DO9404400-40.5` id `937688016` | saldo LK CONTROLE: 0.0
- `DO9404400-42` | matched_exact_sku_stock_resolved | Shopify SKU `DO9404400-42` | Tiny `DO9404400-42` id `937688022` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
