# Gate B2 P1 — correction packet — nike-sb-dunk-low-what-the-p-rod

- title: `Tênis Nike SB Dunk Low What The P-Rod Colorido`
- priority: `P1_saneamento`
- lane: `TINY_DUPLICATE_PACKET`
- proposed_action: Preparar saneamento Tiny de código duplicado e rollback/readback; NÃO executar write sem aprovação escopada.
- row_count: `3`
- prefixes: `CZ2239600, CZ2239600, CZ2239600`

## Status counts
- matched_exact_sku_stock_resolved: `1`
- shopify_variant_tiny_missing: `1`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `CZ2239600` | shopify_variant_tiny_missing | Shopify SKU `CZ2239600` | Tiny `` id ``
- `CZ2239600-1` | matched_exact_sku_stock_resolved | Shopify SKU `CZ2239600-1` | Tiny `CZ2239600-1` id `1061506689` | saldo LK CONTROLE: 0.0
- `CZ2239600-3` | tiny_duplicate_exact_code_blocked | Shopify SKU `CZ2239600-3` | Tiny `CZ2239600-3` id `958544506`

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
