# Gate B2 P2 — correction packet — medicom-toy-x-nike-sb-dunk-be-rbrick

- title: `Tênis Medicom Toy x Nike SB Dunk Be@rbrick Preto`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `2`
- prefixes: `CZ5127001, CZ5127001`

## Status counts
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `1`

## Linhas principais
- `CZ5127001` | shopify_duplicate_sku_blocked | Shopify SKU `CZ5127001` | Tiny `CZ5127001` id `1055935985` | saldo LK CONTROLE: 0.0
- `CZ5127001-1` | shopify_variant_tiny_missing | Shopify SKU `CZ5127001-1` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
