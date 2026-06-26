# Gate B2 P1 — correction packet — chinelo-havaianas-x-dolce-gabanna-zebra-preto

- title: `Chinelo Havaianas x Dolce & Gabbana Zebra Preto`
- priority: `P1_saneamento`
- lane: `TINY_DUPLICATE_PACKET`
- proposed_action: Preparar saneamento Tiny de código duplicado e rollback/readback; NÃO executar write sem aprovação escopada.
- row_count: `5`
- prefixes: `41499220121, 41499220121, 41499220121, 41499220121, 41499220121`

## Status counts
- matched_exact_sku_stock_resolved: `3`
- shopify_variant_tiny_missing: `1`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `41499220121` | shopify_variant_tiny_missing | Shopify SKU `41499220121` | Tiny `` id ``
- `41499220121-1` | matched_exact_sku_stock_resolved | Shopify SKU `41499220121-1` | Tiny `41499220121-1` id `1060924309` | saldo LK CONTROLE: 0.0
- `41499220121-2` | matched_exact_sku_stock_resolved | Shopify SKU `41499220121-2` | Tiny `41499220121-2` id `1060924312` | saldo LK CONTROLE: 0.0
- `41499220121-3` | matched_exact_sku_stock_resolved | Shopify SKU `41499220121-3` | Tiny `41499220121-3` id `1060924315` | saldo LK CONTROLE: 0.0
- `41499220121-4` | tiny_duplicate_exact_code_blocked | Shopify SKU `41499220121-4` | Tiny `41499220121-4` id `1060924304`

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
