# LK GMC — Monitor read-only pós A/B/C, 2026-05-14

Gerado em: `2026-05-14T15:23:33.436004+00:00`

## Resultado
- Status: `post_abc_clean_for_target_scope`
- 12 IDs DRAFT/404 removidos: 12/12 seguem ausentes por `products.get` e `productstatuses.get`.
- 64 atributos C: 64/64 sem diagnóstico alvo de `color/ageGroup/gender`.
- Productstatuses lidos: 23267
- Linhas com issues no catálogo geral: 524

## Top diagnósticos gerais atuais
- `price_updated`: 1089
- `strikethrough_price_updated`: 516
- `restricted_gtin`: 100
- `missing_item_attribute_for_product_type`: 44
- `availability_updated`: 30
- `landing_page_error`: 27
- `image_single_color`: 8
- `reserved_gtin`: 6
- `image_link_broken`: 6
- `landing_page_pending_crawl`: 5
- `condition_updated_from_detected`: 4
- `restricted_nfs_policy_violation`: 4

## Não executado
- Merchant write/delete/patch
- Shopify publish/redirect/write
- Tiny write
- Notion write
- feed fetch/upload
- campaign/message/customer/supplier contact

## Próximo gate seguro
Build next residual preview only after reviewing current full diagnostics; no second Merchant/Shopify/Notion write without explicit inline approval.
