# LK Merchant Center Feed Read-only Router, 2026-05-11

Generated at: `2026-06-04T09:50:19.874855+00:00`

## Veredito

Merchant Center entrou na Fase 6 como fonte `fact_merchant_center`: status de feed, destinos, issues de item e cruzamento com GSC agora viram fila de diagnóstico, sem write em feed, Shopify ou Google.

## Snapshot

- Escopo de leitura: até 30000 produtos; full catalog esperado: True
- Merchant Center ID presente no Doppler: True
- Produtos/status lidos: 21402
- Itens roteados na fila: 12773
- P1: 12773
- P2: 0
- Produtos com issue de item: 12773
- Produtos com destino reprovado: 11909
- Produtos cruzando oportunidade GSC: 4
- Writes liberados agora: 0

## Top grupos de problema

### 1. P1 · feed_issue_fix_preview · 10399 itens
- Issue codes: mhlsf_full_missing_valid_link_template
- Destinos reprovados: Shopping
- Amostras de produto: local:pt:BR:LIA_LK-5524446-L, local:pt:BR:LIA_LK-5524446-XS, local:pt:BR:LIA_LK-5524446-M, local:pt:BR:LIA_LK-5524446-S, local:pt:BR:LIA_LK-5524446-XL
- Status: `read_only_preview`

### 2. P1 · feed_issue_fix_preview · 1322 itens
- Issue codes: landing_page_error
- Destinos reprovados: DisplayAds, Shopping, SurfacesAcrossGoogle
- Amostras de produto: online:pt:BR:2162246425358063315, online:pt:BR:JCQ007, online:pt:BR:JCQ005, online:pt:BR:JCQ013, online:pt:BR:JCQ012
- Status: `read_only_preview`

### 3. P1 · feed_issue_fix_preview · 614 itens
- Issue codes: missing_item_attribute_for_product_type
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:4096148038527481596, online:pt:BR:12020378807434295587, online:pt:BR:324917400624183249, online:pt:BR:14748919792779393441, online:pt:BR:13632860601308160972
- Status: `read_only_preview`

### 4. P1 · feed_issue_fix_preview · 155 itens
- Issue codes: price_updated, strikethrough_price_updated
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:TB010061-713-1, online:pt:BR:TB010061-713-2, online:pt:BR:TB010061-713-6, online:pt:BR:CU2477010, online:pt:BR:PAC-1936990-L
- Status: `read_only_preview`

### 5. P1 · feed_issue_fix_preview · 49 itens
- Issue codes: landing_page_error, missing_item_attribute_for_product_type
- Destinos reprovados: DisplayAds, Shopping, SurfacesAcrossGoogle
- Amostras de produto: online:pt:BR:7866599083713103688, online:pt:BR:11870629-1, online:pt:BR:Aime5, online:pt:BR:ALO-1465950-OS, online:pt:BR:ALO-4485982-S
- Status: `read_only_preview`

### 6. P1 · feed_issue_fix_preview · 36 itens
- Issue codes: price_updated
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:205759610-8, online:pt:BR:205759610-2, online:pt:BR:205759610-4, online:pt:BR:w6334r-9, online:pt:BR:JQ6446-5
- Status: `read_only_preview`

### 7. P1 · feed_issue_fix_preview · 32 itens
- Issue codes: strikethrough_price_updated
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:DZ5485031-5, online:pt:BR:DZ5485031-3, online:pt:BR:DZ5485031-2, online:pt:BR:DZ6333083, online:pt:BR:DZ6333083-1
- Status: `read_only_preview`

### 8. P1 · feed_issue_fix_preview · 27 itens
- Issue codes: local_stores_lack_inventory, mhlsf_full_missing_valid_link_template
- Destinos reprovados: LocalSurfacesAcrossGoogle, Shopping
- Amostras de produto: local:pt:BR:LIA_30095-1, local:pt:BR:LIA_205759610-4, local:pt:BR:LIA_205759610-5, local:pt:BR:LIA_205759610-6, local:pt:BR:LIA_205759610-2
- Status: `read_only_preview`

### 9. P1 · feed_issue_fix_preview · 26 itens
- Issue codes: landing_page_error, price_updated, strikethrough_price_updated
- Destinos reprovados: DisplayAds, Shopping, SurfacesAcrossGoogle
- Amostras de produto: online:pt:BR:20046-3, online:pt:BR:dd1873-100-1, online:pt:BR:FQ9112100-3, online:pt:BR:HQ6998-600-11, online:pt:BR:HQ6998-600-9
- Status: `read_only_preview`

### 10. P1 · feed_issue_fix_preview · 19 itens
- Issue codes: item_missing_required_attribute, landing_page_error, missing_item_attribute_for_product_type
- Destinos reprovados: SurfacesAcrossGoogle
- Amostras de produto: online:pt:BR:10695397335246538087, online:pt:BR:12603524085191418332, online:pt:BR:2258634078163248862, online:pt:BR:6562590402534581177, online:pt:BR:10002025469927148791
- Status: `read_only_preview`

### 11. P1 · feed_issue_fix_preview · 16 itens
- Issue codes: landing_page_error, missing_item_attribute_for_product_type
- Destinos reprovados: SurfacesAcrossGoogle
- Amostras de produto: online:pt:BR:17132474926828267951, online:pt:BR:8259662579508245136, online:pt:BR:8370112528719469130, online:pt:BR:2421339187503443526, online:pt:BR:5081227975339163665
- Status: `read_only_preview`

### 12. P1 · feed_issue_fix_preview · 10 itens
- Issue codes: landing_page_error, price_updated
- Destinos reprovados: DisplayAds, Shopping, SurfacesAcrossGoogle
- Amostras de produto: online:pt:BR:205759610-9, online:pt:BR:205759610-6, online:pt:BR:205759610-7, online:pt:BR:205759610-5, online:pt:BR:205759610-3
- Status: `read_only_preview`

## Amostras de fila individual

### 1. P1 · feed_issue_fix_preview
- Produto: 38
- Link: https://lksneakers.com.br/products/tenis-adidas-samba-og-cream-white-cardboard-creme
- Issues: 9 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: Shopping, DisplayAds, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 2. P1 · feed_issue_fix_preview
- Produto: Jaqueta Aphase Relaxed Denim- Black Preto
- Link: https://lksneakers.com.br/products/jaqueta-aphase-relaxed-denim-black-preto?currency=BRL&country=BR&variant=47007281283294&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- Issues: 9 · landing_page_error, landing_page_error, landing_page_error, price_updated, price_updated
- Destinos reprovados: Shopping, DisplayAds, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 3. P1 · feed_issue_fix_preview
- Produto: Tênis Dunk Low Next Nature Pink Pale Coral Rosa
- Link: https://lksneakers.com.br/products/dunk-low-next-nature-pink-pale-coral?currency=BRL&country=BR&variant=44269130940638&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- Issues: 9 · landing_page_error, landing_page_error, landing_page_error, price_updated, price_updated
- Destinos reprovados: Shopping, DisplayAds, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 4. P1 · feed_issue_fix_preview
- Produto: Tênis Nike Air Jordan 1 Low Se "Glitter Swoosh" Branco
- Link: https://lksneakers.com.br/products/tenis-air-jordan-1-low-se-gs-glitter-swoosh-branco-1?currency=BRL&country=BR&variant=44746890608862&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- Issues: 9 · landing_page_error, landing_page_error, landing_page_error, price_updated, price_updated
- Destinos reprovados: Shopping, DisplayAds, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 5. P1 · feed_issue_fix_preview
- Produto: Tênis Nike Air Jordan 1 Retro Low OG Chicago (2025) Vermelho
- Link: https://lksneakers.com.br/products/tenis-nike-air-jordan-1-retro-low-og-chicago-2025-vermelho?currency=BRL&country=BR&variant=47670376661214&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- Issues: 9 · landing_page_error, landing_page_error, landing_page_error, price_updated, price_updated
- Destinos reprovados: Shopping, DisplayAds, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 6. P1 · feed_issue_fix_preview
- Produto: Tênis Nike Air Jordan 1 Retro Low OG Chicago (2025) Vermelho
- Link: https://lksneakers.com.br/products/tenis-nike-air-jordan-1-retro-low-og-chicago-2025-vermelho?currency=BRL&country=BR&variant=47670376595678&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- Issues: 9 · landing_page_error, landing_page_error, landing_page_error, price_updated, price_updated
- Destinos reprovados: Shopping, DisplayAds, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 7. P1 · feed_issue_fix_preview
- Produto: Tênis Nike Dunk Low Black Paisley Preto
- Link: https://lksneakers.com.br/products/nike-dunk-low-black-paisley?currency=BRL&country=BR&variant=44265080586462&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- Issues: 9 · landing_page_error, landing_page_error, landing_page_error, price_updated, price_updated
- Destinos reprovados: Shopping, DisplayAds, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 8. P1 · feed_issue_fix_preview
- Produto: Tênis Nike Dunk Low Fossil Rose Azul/Rosa
- Link: https://lksneakers.com.br/products/nike-dunk-low-fossil-rose?currency=BRL&country=BR&variant=44265073148126&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- Issues: 9 · landing_page_error, landing_page_error, landing_page_error, price_updated, price_updated
- Destinos reprovados: Shopping, DisplayAds, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

## Top issue codes

- mhlsf_full_missing_valid_link_template: 10441
- landing_page_error: 4270
- missing_item_attribute_for_product_type: 1719
- price_updated: 681
- strikethrough_price_updated: 648
- local_stores_lack_inventory: 54
- item_missing_required_attribute: 36
- restricted_gtin: 30
- restricted_nfs_policy_violation: 19
- availability_updated: 18
- utf8_encoding_error: 18
- condition_updated_from_detected: 8
- image_link_internal_error: 6
- sexual_interests_policy_violation: 5
- image_single_color: 4

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
