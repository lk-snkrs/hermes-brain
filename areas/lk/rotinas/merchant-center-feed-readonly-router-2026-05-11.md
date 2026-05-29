# LK Merchant Center Feed Read-only Router, 2026-05-11

Generated at: `2026-05-28T12:32:00.062313+00:00`

## Veredito

Merchant Center entrou na Fase 6 como fonte `fact_merchant_center`: status de feed, destinos, issues de item e cruzamento com GSC agora viram fila de diagnóstico, sem write em feed, Shopify ou Google.

## Snapshot

- Escopo de leitura: até 30000 produtos; full catalog esperado: True
- Merchant Center ID presente no Doppler: True
- Produtos/status lidos: 20443
- Itens roteados na fila: 1746
- P1: 1743
- P2: 3
- Produtos com issue de item: 1743
- Produtos com destino reprovado: 37
- Produtos cruzando oportunidade GSC: 4
- Writes liberados agora: 0

## Top grupos de problema

### 1. P1 · feed_issue_fix_preview · 1102 itens
- Issue codes: missing_item_attribute_for_product_type
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:4096148038527481596, online:pt:BR:12020378807434295587, online:pt:BR:324917400624183249, online:pt:BR:14748919792779393441, online:pt:BR:13632860601308160972
- Status: `read_only_preview`

### 2. P1 · feed_issue_fix_preview · 303 itens
- Issue codes: price_updated, strikethrough_price_updated
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:TB010061-713-3, online:pt:BR:TB010061-713-1, online:pt:BR:TB010061-713-2, online:pt:BR:TB010061-713-6, online:pt:BR:APH-7284190-XL
- Status: `read_only_preview`

### 3. P1 · feed_issue_fix_preview · 228 itens
- Issue codes: price_updated
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:TB010061-713-4, online:pt:BR:TB010061-713-7, online:pt:BR:205759610-9, online:pt:BR:205759610-6, online:pt:BR:205759610-7
- Status: `read_only_preview`

### 4. P1 · feed_issue_fix_preview · 38 itens
- Issue codes: strikethrough_price_updated
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:PLAYPRINTED-2, online:pt:BR:PLAYPRINTED-3, online:pt:BR:DZ5485031-5, online:pt:BR:DZ5485031-2, online:pt:BR:DZ6333083
- Status: `read_only_preview`

### 5. P1 · feed_issue_fix_preview · 35 itens
- Issue codes: local_stores_lack_inventory
- Destinos reprovados: LocalSurfacesAcrossGoogle
- Amostras de produto: local:pt:BR:LIA_205759610-4, local:pt:BR:LIA_205759610-5, local:pt:BR:LIA_205759610-6, local:pt:BR:LIA_205759610-2, local:pt:BR:LIA_205759610-7
- Status: `read_only_preview`

### 6. P1 · feed_issue_fix_preview · 14 itens
- Issue codes: restricted_gtin
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:U9060ZGE-9, online:pt:BR:U9060ZGE-4, online:pt:BR:555088108-5, online:pt:BR:553558612-6, online:pt:BR:553558612-7
- Status: `read_only_preview`

### 7. P1 · feed_issue_fix_preview · 6 itens
- Issue codes: utf8_encoding_error
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:CLC-0067294-XXL, online:pt:BR:CLC-0067294-L, online:pt:BR:CLC-0067294-M, online:pt:BR:CLC-0067294-XS, online:pt:BR:CLC-0067294-S
- Status: `read_only_preview`

### 8. P1 · feed_issue_fix_preview · 4 itens
- Issue codes: condition_updated_from_detected
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: local:pt:BR:LIA_IG6192-3, local:pt:BR:LIA_IG6192-2, local:pt:BR:LIA_IG6192-4, local:pt:BR:LIA_IG6192-1
- Status: `read_only_preview`

### 9. P2 · gsc_feed_pdp_alignment_preview · 3 itens
- Issue codes: no_item_issue_code
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:HQ4307-001-4, local:pt:BR:LIA_U9060BLC-9, online:pt:BR:HQ2050-103-10
- Status: `read_only_preview`

### 10. P1 · feed_issue_fix_preview · 2 itens
- Issue codes: coupon_gtin
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:FZ4167-200-6, local:pt:BR:LIA_FZ4167-200-6
- Status: `read_only_preview`

### 11. P1 · feed_issue_fix_preview · 2 itens
- Issue codes: image_single_color
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: local:pt:BR:LIA_U9060PSD-5, local:pt:BR:LIA_U9060PSD-1
- Status: `read_only_preview`

### 12. P1 · feed_issue_fix_preview · 1 itens
- Issue codes: availability_updated
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:20054-3
- Status: `read_only_preview`

## Amostras de fila individual

### 1. P1 · feed_issue_fix_preview
- Produto: Camisa Aphase Check - Light Yellow Bege
- Link: https://lksneakers.com.br/products/camisa-aphase-check-light-yellow-bege?currency=BRL&country=BR&variant=47007457738974&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- Issues: 9 · availability_updated, availability_updated, availability_updated, price_updated, price_updated
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 2. P1 · feed_issue_fix_preview
- Produto: 34
- Link: https://lksneakers.com.br/products/tenis-adidas-samba-og-silver-metallic-cracked-leather-prateado
- Issues: 6 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 3. P1 · feed_issue_fix_preview
- Produto: 35
- Link: https://lksneakers.com.br/products/tenis-onitsuka-tiger-mexico-66-slip-on-white-pure-silver-prateado
- Issues: 6 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 4. P1 · feed_issue_fix_preview
- Produto: 35
- Link: https://lksneakers.com.br/products/tenis-nike-zoom-vomero-5-metallic-silver-blue-tint-prateado-azul
- Issues: 6 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 5. P1 · feed_issue_fix_preview
- Produto: 35
- Link: https://lksneakers.com.br/products/tenis-new-balance-1906l-silver-metallic-black-prata
- Issues: 6 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 6. P1 · feed_issue_fix_preview
- Produto: 35
- Link: https://lksneakers.com.br/products/tenis-nike-zoom-vomero-5-metallic-silver-platinum-violet-prateado-violeta
- Issues: 6 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 7. P1 · feed_issue_fix_preview
- Produto: 35
- Link: https://lksneakers.com.br/products/tenis-onitsuka-tiger-mexico-66-glitter-pack-pure-silver-prateado
- Issues: 6 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 8. P1 · feed_issue_fix_preview
- Produto: 37
- Link: https://lksneakers.com.br/products/tenis-new-balance-530-beige-angora-creme-1069960456
- Issues: 6 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

## Top issue codes

- missing_item_attribute_for_product_type: 2495
- price_updated: 1596
- strikethrough_price_updated: 1029
- local_stores_lack_inventory: 35
- restricted_gtin: 23
- utf8_encoding_error: 18
- availability_updated: 6
- condition_updated_from_detected: 4
- restricted_nfs_policy_violation: 4
- coupon_gtin: 3
- image_single_color: 2
- reserved_gtin: 2
- pause_expired: 2
- sexual_interests_policy_violation: 1
- vehicles_policy_violation: 1

## Guardrails

- Merchant Center status is fact_merchant_center for feed health; Shopify remains source for product data and commerce state.
- Feed, Shopify, PDP, image, title/meta, Merchant Center and Google admin changes require preview and Lucas approval.
- This step uses GET/list endpoints only and does not call insert/update/delete/custombatch or supplemental feed mutations.
- No customer PII is used or exported.

## O que não foi feito

- merchant_center_write
- feed_update
- supplemental_feed_update
- product_insert
- product_delete
- shopify_write
- theme_write
- gsc_admin_change
- indexing_api_submit
- content_publish
- campaign_or_customer_send
- cron_creation
