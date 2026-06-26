# Gate B2 P1 — correction packet — air-jordan-1-low-inside-out-black

- title: `Tênis Nike Air Jordan 1 Low Inside Out Black Preto`
- priority: `P1_saneamento`
- lane: `TINY_DUPLICATE_PACKET`
- proposed_action: Preparar saneamento Tiny de código duplicado e rollback/readback; NÃO executar write sem aprovação escopada.
- row_count: `7`
- prefixes: `DN1635001-38, DN1635001-38, DN1635001-38, DN1635001-38, DN1635001-38, DN1635001-38, DN1635001-38`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `1`
- shopify_variant_tiny_missing: `4`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `DN1635001-38` | matched_exact_sku_stock_missing_deposit | Shopify SKU `DN1635001-38` | Tiny `DN1635001-38` id `960622463`
- `DN1635001-38-1` | shopify_variant_tiny_missing | Shopify SKU `DN1635001-38-1` | Tiny `` id ``
- `DN1635001-38-6` | shopify_variant_tiny_missing | Shopify SKU `DN1635001-38-6` | Tiny `` id ``
- `DN1635001-38-5` | shopify_variant_tiny_missing | Shopify SKU `DN1635001-38-5` | Tiny `` id ``
- `DN1635001-38-2` | shopify_variant_tiny_missing | Shopify SKU `DN1635001-38-2` | Tiny `` id ``
- `DN1635001-38-3` | matched_exact_sku_stock_resolved | Shopify SKU `DN1635001-38-3` | Tiny `DN1635001-38-3` id `961173063` | saldo LK CONTROLE: 0.0
- `DN1635001-38-8` | tiny_duplicate_exact_code_blocked | Shopify SKU `DN1635001-38-8` | Tiny `DN1635001-38-8` id `961173068`

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
