# Gate B2 P2 — correction packet — yeezy-foam-runner-onyx

- title: `Tênis Yeezy Foam Runner Onyx Preto`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `1`
- prefixes: `HP8739`

## Status counts
- shopify_duplicate_sku_blocked: `1`

## Linhas principais
- `HP8739` | shopify_duplicate_sku_blocked | Shopify SKU `HP8739` | Tiny `HP8739` id `1069536076` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
