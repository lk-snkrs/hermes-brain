# LK Merchant Center Feed Read-only Router, 2026-05-11

Generated at: `2026-06-10T00:46:55.970162+00:00`

## Veredito

Merchant Center entrou na Fase 6 como fonte `fact_merchant_center`: status de feed, destinos, issues de item e cruzamento com GSC agora viram fila de diagnóstico, sem write em feed, Shopify ou Google.

## Snapshot

- Escopo de leitura: até 30000 produtos; full catalog esperado: True
- Merchant Center ID presente no Doppler: True
- Produtos/status lidos: 23896
- Itens roteados na fila: 4157
- P1: 4152
- P2: 5
- Produtos com issue de item: 4152
- Produtos com destino reprovado: 1417
- Produtos cruzando oportunidade GSC: 5
- Writes liberados agora: 0

## Top grupos de problema

### 1. P1 · feed_issue_fix_preview · 2627 itens
- Issue codes: missing_item_attribute_for_product_type
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:10831998063178300125, online:pt:BR:17132474926828267951, online:pt:BR:5563935503216555176, online:pt:BR:18003584147887747403, online:pt:BR:10131134412697596529
- Status: `read_only_preview`

### 2. P1 · feed_issue_fix_preview · 1169 itens
- Issue codes: local_stores_lack_inventory
- Destinos reprovados: LocalSurfacesAcrossGoogle, Shopping
- Amostras de produto: local:pt:BR:LIA_w4535r-1, local:pt:BR:LIA_w4535r-3, local:pt:BR:LIA_w4535r-4, local:pt:BR:LIA_w4535r-5, local:pt:BR:LIA_w4535r-2
- Status: `read_only_preview`

### 3. P1 · feed_issue_fix_preview · 206 itens
- Issue codes: mhlsf_full_missing_valid_link_template
- Destinos reprovados: Shopping
- Amostras de produto: local:pt:BR:LIA_ST33, local:pt:BR:LIA_FOG21-4, local:pt:BR:LIA_FOG21-5, local:pt:BR:LIA_FOG21-1, local:pt:BR:LIA_FOG21-2
- Status: `read_only_preview`

### 4. P1 · feed_issue_fix_preview · 35 itens
- Issue codes: restricted_gtin
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:U9060ZGE-9, online:pt:BR:U9060ZGE-4, online:pt:BR:1203A655-100-7, online:pt:BR:FN4193100-2, online:pt:BR:U574LGIL-8
- Status: `read_only_preview`

### 5. P1 · feed_issue_fix_preview · 35 itens
- Issue codes: strikethrough_price_updated
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:DZ5485031-2, online:pt:BR:DZ6333083, online:pt:BR:DZ6333083-1, online:pt:BR:DZ6333083-2, online:pt:BR:DZ6333083-4
- Status: `read_only_preview`

### 6. P1 · feed_issue_fix_preview · 11 itens
- Issue codes: item_missing_required_attribute, landing_page_error, missing_item_attribute_for_product_type
- Destinos reprovados: Shopping, SurfacesAcrossGoogle
- Amostras de produto: online:pt:BR:10695397335246538087, online:pt:BR:2258634078163248862, online:pt:BR:6562590402534581177, online:pt:BR:10002025469927148791, online:pt:BR:3876299146406606317
- Status: `read_only_preview`

### 7. P1 · feed_issue_fix_preview · 11 itens
- Issue codes: local_stores_lack_inventory, mhlsf_full_missing_valid_link_template
- Destinos reprovados: LocalSurfacesAcrossGoogle, Shopping
- Amostras de produto: local:pt:BR:LIA_30095-1, local:pt:BR:LIA_u9060aga-2, local:pt:BR:LIA_u9060aga-7, local:pt:BR:LIA_u9060aga-1, local:pt:BR:LIA_u9060aga-4
- Status: `read_only_preview`

### 8. P1 · feed_issue_fix_preview · 10 itens
- Issue codes: price_updated, strikethrough_price_updated
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:4096148038527481596, online:pt:BR:7866599083713103688, online:pt:BR:DV1748601-2, online:pt:BR:DV1748601-4, online:pt:BR:DV1748601-5
- Status: `read_only_preview`

### 9. P1 · feed_issue_fix_preview · 9 itens
- Issue codes: item_missing_required_attribute
- Destinos reprovados: Shopping, SurfacesAcrossGoogle
- Amostras de produto: online:pt:BR:3037332819634467443, online:pt:BR:8238106713841029629, online:pt:BR:13153228639919529112, online:pt:BR:16784615169924610596, online:pt:BR:5728263874471437136
- Status: `read_only_preview`

### 10. P1 · feed_issue_fix_preview · 8 itens
- Issue codes: price_updated
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:205759610-9, online:pt:BR:205759610-6, online:pt:BR:205759610-7, online:pt:BR:205759610-8, online:pt:BR:205759610-2
- Status: `read_only_preview`

### 11. P1 · feed_issue_fix_preview · 6 itens
- Issue codes: item_missing_required_attribute, missing_item_attribute_for_product_type
- Destinos reprovados: Shopping, SurfacesAcrossGoogle
- Amostras de produto: online:pt:BR:8636076927660856622, online:pt:BR:8117506143187011782, online:pt:BR:6058066858883881361, online:pt:BR:6810467892295091670, online:pt:BR:7595466067205702554
- Status: `read_only_preview`

### 12. P2 · gsc_feed_pdp_alignment_preview · 5 itens
- Issue codes: no_item_issue_code
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:HQ4307-001-10, online:pt:BR:HQ4307-002-11, local:pt:BR:LIA_HQ4307-003-9, online:pt:BR:HQ4307-003-5, online:pt:BR:HQ2050-103-10
- Status: `read_only_preview`

## Amostras de fila individual

### 1. P1 · feed_issue_fix_preview
- Produto: 42
- Link: https://lksneakers.com.br/products/bota-timberland-6-premium-waterproof-boot-supreme-multi-color-colorido
- Issues: 12 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: Shopping, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 2. P1 · feed_issue_fix_preview
- Produto: Calça Chino Saint Studio Supima Preto
- Link: https://lksneakers.com.br/products/calca-chino-saint-studio-supima-preto
- Issues: 12 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: Shopping, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 3. P1 · feed_issue_fix_preview
- Produto: Calça Nude Project Illegal Jeans Ash Cinza - LK
- Link: https://lksneakers.com.br/products/calca-nude-project-illegal-jeans-ash-cinza
- Issues: 12 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: Shopping, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 4. P1 · feed_issue_fix_preview
- Produto: Calça Nude Project Jeans Soft Velvet Azul Marinho
- Link: https://lksneakers.com.br/products/calca-nude-project-jeans-soft-velvet-azul-marinho
- Issues: 12 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: Shopping, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 5. P1 · feed_issue_fix_preview
- Produto: Calça Saint Studio Jeans Baggy Preta
- Link: https://lksneakers.com.br/products/calca-saint-studio-jeans-baggy-preta
- Issues: 12 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: Shopping, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 6. P1 · feed_issue_fix_preview
- Produto: Calça Saint Studio Wide Alfaiataria Preto
- Link: https://lksneakers.com.br/products/calca-saint-studio-wide-alfaiataria-preto
- Issues: 12 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: Shopping, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 7. P1 · feed_issue_fix_preview
- Produto: Calça Saint Studio Wide Alfaiataria Risca de Giz Cinza
- Link: https://lksneakers.com.br/products/calca-saint-studio-wide-alfaiataria-risca-de-giz-cinza
- Issues: 12 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: Shopping, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 8. P1 · feed_issue_fix_preview
- Produto: Calça Saint Studio Wide Alfaiataria Risca de Giz Preta
- Link: https://lksneakers.com.br/products/calca-saint-studio-wide-alfaiataria-risca-de-giz-preta
- Issues: 12 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: Shopping, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

## Top issue codes

- missing_item_attribute_for_product_type: 5962
- local_stores_lack_inventory: 2362
- mhlsf_full_missing_valid_link_template: 217
- strikethrough_price_updated: 138
- restricted_gtin: 70
- price_updated: 54
- item_missing_required_attribute: 52
- landing_page_error: 31
- image_single_color: 10
- image_link_internal_error: 9
- condition_updated_from_detected: 8
- restricted_nfs_policy_violation: 5
- reserved_gtin: 4
- availability_updated: 3
- image_link_broken: 2

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
