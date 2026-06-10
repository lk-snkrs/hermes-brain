# Gate B2 P2 — correction packet — dunk-low-light-ocean-bliss

- title: `Tênis Dunk Low Light Ocean Bliss`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `7`
- prefixes: `DV7210001, DV7210001, DV7210001, DV7210001, DV7210001, DV7210001, DV7210001`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `5`
- shopify_duplicate_sku_blocked: `1`

## Linhas principais
- `DV7210001` | shopify_duplicate_sku_blocked | Shopify SKU `DV7210001` | Tiny `DV7210001` id `1069537201` | saldo LK CONTROLE: 0.0
- `DV72100011` | matched_exact_sku_stock_resolved | Shopify SKU `DV72100011` | Tiny `DV72100011` id `1070196892` | saldo LK CONTROLE: 0.0
- `DV72100012` | matched_exact_sku_stock_resolved | Shopify SKU `DV72100012` | Tiny `DV72100012` id `1070196895` | saldo LK CONTROLE: 0.0
- `DV72100013` | matched_exact_sku_stock_resolved | Shopify SKU `DV72100013` | Tiny `DV72100013` id `1070196898` | saldo LK CONTROLE: 0.0
- `DV72100014` | matched_exact_sku_stock_resolved | Shopify SKU `DV72100014` | Tiny `DV72100014` id `1070196901` | saldo LK CONTROLE: 0.0
- `DV72100015` | matched_exact_sku_stock_resolved | Shopify SKU `DV72100015` | Tiny `DV72100015` id `1070196904` | saldo LK CONTROLE: 0.0
- `DV72100016` | matched_exact_sku_stock_missing_deposit | Shopify SKU `DV72100016` | Tiny `DV72100016` id `1070196907`

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
