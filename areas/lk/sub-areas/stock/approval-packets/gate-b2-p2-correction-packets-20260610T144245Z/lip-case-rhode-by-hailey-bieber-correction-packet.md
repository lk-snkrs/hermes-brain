# Gate B2 P2 — correction packet — lip-case-rhode-by-hailey-bieber

- title: `Lip Case Rhode By Hailey Bieber`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `13`
- prefixes: `LIPCASE, LIPCASE, LIPCASE, LIPCASE, LIPCASE, LIPCASE, LIPCASE, LIPCASE, LIPCASE, LIPCASE, LIPCASE, LIPCASE, LIPCASE`

## Status counts
- matched_exact_sku_stock_resolved: `7`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `5`

## Linhas principais
- `LIPCASE` | matched_exact_sku_stock_resolved | Shopify SKU `LIPCASE` | Tiny `LIPCASE` id `1061753885` | saldo LK CONTROLE: 0.0
- `LIPCASE-1` | matched_exact_sku_stock_resolved | Shopify SKU `LIPCASE-1` | Tiny `LIPCASE-1` id `1061753908` | saldo LK CONTROLE: 0.0
- `LIPCASE-10` | matched_exact_sku_stock_resolved | Shopify SKU `LIPCASE-10` | Tiny `LIPCASE-10` id `1061753937` | saldo LK CONTROLE: 0.0
- `LIPCASE-11` | shopify_duplicate_sku_blocked | Shopify SKU `LIPCASE-11` | Tiny `LIPCASE-11` id `1061753940`
- `LIPCASE-2` | shopify_variant_tiny_missing | Shopify SKU `LIPCASE-2` | Tiny `` id ``
- `LIPCASE-3` | shopify_variant_tiny_missing | Shopify SKU `LIPCASE-3` | Tiny `` id ``
- `LIPCASE-4` | shopify_variant_tiny_missing | Shopify SKU `LIPCASE-4` | Tiny `` id ``
- `LIPCASE-5` | shopify_variant_tiny_missing | Shopify SKU `LIPCASE-5` | Tiny `` id ``
- `LIPCASE-6` | shopify_variant_tiny_missing | Shopify SKU `LIPCASE-6` | Tiny `` id ``
- `LIPCASE-7` | matched_exact_sku_stock_resolved | Shopify SKU `LIPCASE-7` | Tiny `LIPCASE-7` id `1061753926` | saldo LK CONTROLE: 0.0
- `LIPCASE-8` | matched_exact_sku_stock_resolved | Shopify SKU `LIPCASE-8` | Tiny `LIPCASE-8` id `1061753930` | saldo LK CONTROLE: 0.0
- `LIPCASE-9` | matched_exact_sku_stock_resolved | Shopify SKU `LIPCASE-9` | Tiny `LIPCASE-9` id `1061753934` | saldo LK CONTROLE: 0.0
- `LIPCASE2-1` | matched_exact_sku_stock_resolved | Shopify SKU `LIPCASE2-1` | Tiny `LIPCASE2-1` id `1061754065` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
