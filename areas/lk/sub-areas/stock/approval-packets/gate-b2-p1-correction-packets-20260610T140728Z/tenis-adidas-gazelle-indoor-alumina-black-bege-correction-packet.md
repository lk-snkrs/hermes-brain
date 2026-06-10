# Gate B2 P1 — correction packet — tenis-adidas-gazelle-indoor-alumina-black-bege

- title: `Tênis adidas Gazelle Indoor Alumina Black Bege`
- priority: `P1_saneamento`
- lane: `TINY_DUPLICATE_PACKET`
- proposed_action: Preparar saneamento Tiny de código duplicado e rollback/readback; NÃO executar write sem aprovação escopada.
- row_count: `6`
- prefixes: `IH4769, IH4769, IH4769, IH4769, IH4769, IH4769`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- matched_exact_sku_stock_resolved: `2`
- shopify_variant_tiny_missing: `2`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `IH4769` | tiny_duplicate_exact_code_blocked | Shopify SKU `IH4769` | Tiny `IH4769` id `1059103250`
- `IH4769-1` | matched_exact_sku_stock_resolved | Shopify SKU `IH4769-1` | Tiny `IH4769-1` id `1059103256` | saldo LK CONTROLE: 0.0
- `IH4769-2` | matched_exact_sku_stock_resolved | Shopify SKU `IH4769-2` | Tiny `IH4769-2` id `1059103259` | saldo LK CONTROLE: 0.0
- `IH4769-3` | matched_exact_sku_stock_missing_deposit | Shopify SKU `IH4769-3` | Tiny `IH4769-3` id `1059103262`
- `IH4769-4` | shopify_variant_tiny_missing | Shopify SKU `IH4769-4` | Tiny `` id ``
- `IH4769-5` | shopify_variant_tiny_missing | Shopify SKU `IH4769-5` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
