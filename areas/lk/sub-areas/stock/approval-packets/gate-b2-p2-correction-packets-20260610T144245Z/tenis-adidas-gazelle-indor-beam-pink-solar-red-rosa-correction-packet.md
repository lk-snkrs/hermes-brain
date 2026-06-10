# Gate B2 P2 — correction packet — tenis-adidas-gazelle-indor-beam-pink-solar-red-rosa

- title: `Tênis adidas Gazelle Indor "Beam Pink Solar Red" Rosa`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `5`
- prefixes: `IE1058, IE1058, IE1058, IE1058, IE1058`

## Status counts
- matched_exact_sku_stock_resolved: `2`
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `2`

## Linhas principais
- `IE1058` | shopify_duplicate_sku_blocked | Shopify SKU `IE1058` | Tiny `` id ``
- `IE1058-4` | shopify_variant_tiny_missing | Shopify SKU `IE1058-4` | Tiny `` id ``
- `IE1058-1` | shopify_variant_tiny_missing | Shopify SKU `IE1058-1` | Tiny `` id ``
- `IE1058-2` | matched_exact_sku_stock_resolved | Shopify SKU `IE1058-2` | Tiny `IE1058-2` id `1056481274` | saldo LK CONTROLE: 0.0
- `IE1058-3` | matched_exact_sku_stock_resolved | Shopify SKU `IE1058-3` | Tiny `IE1058-3` id `1067599314` | saldo LK CONTROLE: 0.0

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
