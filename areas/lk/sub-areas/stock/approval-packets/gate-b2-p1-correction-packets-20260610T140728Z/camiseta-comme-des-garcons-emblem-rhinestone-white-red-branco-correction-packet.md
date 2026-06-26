# Gate B2 P1 — correction packet — camiseta-comme-des-garcons-emblem-rhinestone-white-red-branco

- title: `Camiseta Comme des Garçons Emblem Rhinestone White/Red Branco`
- priority: `P1_saneamento`
- lane: `TINY_DUPLICATE_PACKET`
- proposed_action: Preparar saneamento Tiny de código duplicado e rollback/readback; NÃO executar write sem aprovação escopada.
- row_count: `3`
- prefixes: `AX-T801-051, AX-T801-051, AX-T801-051`

## Status counts
- matched_exact_sku_stock_resolved: `2`
- tiny_duplicate_exact_code_blocked: `1`

## Linhas principais
- `AX-T801-051` | matched_exact_sku_stock_resolved | Shopify SKU `AX-T801-051` | Tiny `AX-T801-051` id `1061521475` | saldo LK CONTROLE: 0.0
- `AX-T801-051-1` | matched_exact_sku_stock_resolved | Shopify SKU `AX-T801-051-1` | Tiny `AX-T801-051-1` id `1061521477` | saldo LK CONTROLE: 0.0
- `AX-T801-051-2` | tiny_duplicate_exact_code_blocked | Shopify SKU `AX-T801-051-2` | Tiny `AX-T801-051-2` id `1061587513`

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
