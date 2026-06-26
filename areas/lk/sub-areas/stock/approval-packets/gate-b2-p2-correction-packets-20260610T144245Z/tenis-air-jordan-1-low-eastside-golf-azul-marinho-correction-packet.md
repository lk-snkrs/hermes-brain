# Gate B2 P2 — correction packet — tenis-air-jordan-1-low-eastside-golf-azul-marinho

- title: `Tênis Nike Air Jordan 1 Low "Eastside Golf" Azul Marinho`
- priority: `P2_saneamento`
- lane: `TINY_DUPLICATE_PACKET`
- proposed_action: Preparar saneamento Tiny de código duplicado e rollback/readback; NÃO executar write sem aprovação escopada.
- row_count: `4`
- prefixes: `DV1759-448, DV1759-448, DV1759-448, DV1759-448`

## Status counts
- matched_exact_sku_stock_resolved: `3`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `DV1759-448` | matched_exact_sku_stock_resolved | Shopify SKU `DV1759-448` | Tiny `DV1759-448` id `1056606147` | saldo LK CONTROLE: 0.0
- `DV1759-448-2` | matched_exact_sku_stock_resolved | Shopify SKU `DV1759-448-2` | Tiny `DV1759-448-2` id `1057156405` | saldo LK CONTROLE: 1.0
- `DV1759-448-1` | matched_exact_sku_stock_resolved | Shopify SKU `DV1759-448-1` | Tiny `DV1759-448-1` id `1056606149` | saldo LK CONTROLE: 0.0
- `DV1759-448-4` | tiny_duplicate_exact_code_blocked | Shopify SKU `DV1759-448-4` | Tiny `DV1759-448-4` id `1056596870`

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
