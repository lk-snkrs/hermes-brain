# Gate B2 P1 — correction packet — polo-comme-des-garcons-play-preto

- title: `Polo Comme des Garçons PLAY Black Emblem Black Preto`
- priority: `P1_saneamento`
- lane: `TINY_DUPLICATE_PACKET`
- proposed_action: Preparar saneamento Tiny de código duplicado e rollback/readback; NÃO executar write sem aprovação escopada.
- row_count: `6`
- prefixes: `CDGP1, CDGP1, CDGP1, CDGP1, CDGP1, CDGP1`

## Status counts
- matched_exact_sku_stock_resolved: `1`
- shopify_variant_tiny_missing: `4`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `CDGP1` | shopify_variant_tiny_missing | Shopify SKU `CDGP1` | Tiny `` id ``
- `CDGP1-1` | shopify_variant_tiny_missing | Shopify SKU `CDGP1-1` | Tiny `` id ``
- `CDGP1-2` | shopify_variant_tiny_missing | Shopify SKU `CDGP1-2` | Tiny `` id ``
- `CDGP1-3` | shopify_variant_tiny_missing | Shopify SKU `CDGP1-3` | Tiny `` id ``
- `CDGP1-4` | matched_exact_sku_stock_resolved | Shopify SKU `CDGP1-4` | Tiny `CDGP1-4` id `1060890872` | saldo LK CONTROLE: 0.0
- `CDGP1-5` | tiny_duplicate_exact_code_blocked | Shopify SKU `CDGP1-5` | Tiny `CDGP1-5` id `1060890858`

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
