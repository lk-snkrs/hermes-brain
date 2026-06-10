# Gate B2 P2 — correction packet — air-jordan-1-low-canyon-rust

- title: `Tênis Nike Air Jordan 1 Low Canyon Rust Colorido`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `2`
- prefixes: `DC0774042, DC0774042`

## Status counts
- matched_exact_sku_stock_resolved: `1`
- shopify_duplicate_sku_blocked: `1`

## Linhas principais
- `DC0774042` | shopify_duplicate_sku_blocked | Shopify SKU `DC0774042` | Tiny `DC0774042` id `969796133`
- `DC07740421` | matched_exact_sku_stock_resolved | Shopify SKU `DC07740421` | Tiny `DC07740421` id `973225959` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
