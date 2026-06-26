# Gate B2 P2 — correction packet — tenis-nike-dunk-low-indigo-haze-roxo

- title: `Tênis Nike Dunk Low Indigo Haze Roxo`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `4`
- prefixes: `DD1503500, DD1503500, DD1503500, DD1503500`

## Status counts
- matched_exact_sku_stock_missing_deposit: `1`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `2`

## Linhas principais
- `DD1503500` | shopify_duplicate_sku_blocked | Shopify SKU `DD1503500` | Tiny `DD1503500` id `959423879` | saldo LK CONTROLE: 0.0
- `DD1503500-1` | matched_exact_sku_stock_missing_deposit | Shopify SKU `DD1503500-1` | Tiny `DD1503500-1` id `959423956`
- `DD1503500-3` | shopify_variant_tiny_missing | Shopify SKU `DD1503500-3` | Tiny `` id ``
- `DD1503500-2` | shopify_variant_tiny_missing | Shopify SKU `DD1503500-2` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
