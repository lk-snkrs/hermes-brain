# Gate B2 P2 — correction packet — tenis-vans-knu-skool-mte-1-lx-imran-potato-azul

- title: `Tênis Vans Knu Skool MTE-1 LX Imran Potato Azul`
- priority: `P2_saneamento`
- lane: `SHOPIFY_DUPLICATE_PACKET`
- proposed_action: Preparar diff Shopify por variante/SKU duplicado e rollback; NÃO executar write sem aprovação escopada.
- row_count: `2`
- prefixes: `VN000E3QBX9, VN000E3QBX9`

## Status counts
- shopify_duplicate_sku_blocked: `1`
- shopify_variant_tiny_missing: `1`

## Linhas principais
- `VN000E3QBX9` | shopify_duplicate_sku_blocked | Shopify SKU `VN000E3QBX9` | Tiny `` id ``
- `VN000E3QBX9-1` | shopify_variant_tiny_missing | Shopify SKU `VN000E3QBX9-1` | Tiny `` id ``

## Guardrails
- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/runtime novo: `0`
- Promessa de disponibilidade pública: `0`
- Rollback: descartar artefatos locais; nada externo alterado.
