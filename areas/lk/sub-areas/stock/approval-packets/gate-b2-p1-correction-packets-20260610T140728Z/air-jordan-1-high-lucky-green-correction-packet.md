# Gate B2 P1 — correction packet — air-jordan-1-high-lucky-green

- title: `Tênis Nike Air Jordan 1 High Lucky Green Verde`
- priority: `P1_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `6`
- prefixes: `DB4612300, DB4612300, DB4612300, DB4612300, DB4612300, DB4612300`

## Status counts
- matched_exact_sku_stock_resolved: `4`
- shopify_duplicate_sku_blocked: `1`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `DB4612300` | shopify_duplicate_sku_blocked | Shopify SKU `DB4612300` | Tiny `` id ``
- `DB4612300-36` | matched_exact_sku_stock_resolved | Shopify SKU `DB4612300-36` | Tiny `DB4612300-36` id `940000591` | saldo LK CONTROLE: 0.0
- `DB4612300-37` | matched_exact_sku_stock_resolved | Shopify SKU `DB4612300-37` | Tiny `DB4612300-37` id `940000600` | saldo LK CONTROLE: 0.0
- `DB4612300-3` | matched_exact_sku_stock_resolved | Shopify SKU `DB4612300-3` | Tiny `DB4612300-3` id `940000614` | saldo LK CONTROLE: 0.0
- `DB4612300-6` | matched_exact_sku_stock_resolved | Shopify SKU `DB4612300-6` | Tiny `DB4612300-6` id `1067135856` | saldo LK CONTROLE: 0.0
- `DB4612300-7` | tiny_duplicate_exact_code_blocked | Shopify SKU `DB4612300-7` | Tiny `DB4612300-7` id `939992163`

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
