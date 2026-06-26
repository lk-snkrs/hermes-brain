# Gate B2 P1 — correction packet — tenis-adidas-samba-og-maroon-cream-white-vinho

- title: `Tênis adidas Samba Og Maroon Cream White Vinho`
- priority: `P1_saneamento`
- lane: `TINY_DUPLICATE_PACKET`
- proposed_action: Preparar saneamento Tiny de código duplicado e rollback/readback; NÃO executar write sem aprovação escopada.
- row_count: `8`
- prefixes: `ID0477, ID0477, ID0477, ID0477, ID0477, ID0477, ID0477, ID0477`

## Status counts
- matched_exact_sku_stock_resolved: `6`
- shopify_variant_tiny_missing: `1`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `ID0477` | shopify_variant_tiny_missing | Shopify SKU `ID0477` | Tiny `` id ``
- `ID0477-3` | matched_exact_sku_stock_resolved | Shopify SKU `ID0477-3` | Tiny `ID0477-3` id `1056864417` | saldo LK CONTROLE: 1.0
- `ID0477-1` | matched_exact_sku_stock_resolved | Shopify SKU `ID0477-1` | Tiny `ID0477-1` id `1056829898` | saldo LK CONTROLE: 0.0
- `ID0477-2` | matched_exact_sku_stock_resolved | Shopify SKU `ID0477-2` | Tiny `ID0477-2` id `1056829901` | saldo LK CONTROLE: 5.0
- `ID0477-4` | matched_exact_sku_stock_resolved | Shopify SKU `ID0477-4` | Tiny `ID0477-4` id `1057376792` | saldo LK CONTROLE: 1.0
- `ID0477-5` | matched_exact_sku_stock_resolved | Shopify SKU `ID0477-5` | Tiny `ID0477-5` id `1063351087` | saldo LK CONTROLE: 3.0
- `ID0477-6` | matched_exact_sku_stock_resolved | Shopify SKU `ID0477-6` | Tiny `ID0477-6` id `1064652629` | saldo LK CONTROLE: 1.0
- `ID0477-7` | tiny_duplicate_exact_code_blocked | Shopify SKU `ID0477-7` | Tiny `ID0477-7` id `1056829895`

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
