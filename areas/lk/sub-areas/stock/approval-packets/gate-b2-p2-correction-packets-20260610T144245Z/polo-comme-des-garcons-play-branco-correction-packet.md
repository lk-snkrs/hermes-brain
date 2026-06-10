# Gate B2 P2 — correction packet — polo-comme-des-garcons-play-branco

- title: `Polo Comme des Garçons PLAY Red Emblem White Branco`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `1`
- prefixes: `CDGP2`

## Status counts
- shopify_duplicate_sku_blocked: `1`

## Linhas principais
- `CDGP2` | shopify_duplicate_sku_blocked | Shopify SKU `CDGP2` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
