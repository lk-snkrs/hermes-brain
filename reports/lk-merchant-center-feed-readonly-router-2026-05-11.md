# LK Merchant Center Feed Read-only Router, 2026-05-11

Generated at: `2026-05-14T14:04:48.634367+00:00`

## Veredito

Merchant Center entrou na Fase 6 como fonte `fact_merchant_center`: status de feed, destinos, issues de item e cruzamento com GSC agora viram fila de diagnóstico, sem write em feed, Shopify ou Google.

## Snapshot

- Escopo de leitura: até 30000 produtos; full catalog esperado: True
- Merchant Center ID presente no Doppler: True
- Produtos/status lidos: 23279
- Itens roteados na fila: 599
- P1: 598
- P2: 1
- Produtos com issue de item: 598
- Produtos com destino reprovado: 24
- Produtos cruzando oportunidade GSC: 2
- Writes liberados agora: 0

## Top grupos de problema

### 1. P1 · feed_issue_fix_preview · 232 itens
- Issue codes: price_updated
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:TB010061-713-1, online:pt:BR:TB010061-713-4, online:pt:BR:TB010061-713-2, online:pt:BR:TB010061-713-6, online:pt:BR:TB010061-713-7
- Status: `read_only_preview`

### 2. P1 · feed_issue_fix_preview · 127 itens
- Issue codes: price_updated, strikethrough_price_updated
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:40041-1, online:pt:BR:ST19-1, online:pt:BR:20054-3, online:pt:BR:30095-1, online:pt:BR:PAC-0379230-L
- Status: `read_only_preview`

### 3. P1 · feed_issue_fix_preview · 72 itens
- Issue codes: missing_item_attribute_for_product_type
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:2669418431140851356, online:pt:BR:16354631407067711955, online:pt:BR:5830504980213147042, online:pt:BR:3104193228761997124, online:pt:BR:12273029318518873414
- Status: `read_only_preview`

### 4. P1 · feed_issue_fix_preview · 66 itens
- Issue codes: restricted_gtin
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:U9060ZGE-9, online:pt:BR:U9060ZGE-4, online:pt:BR:1203A655-100-7, online:pt:BR:FN4193100-2, online:pt:BR:U574LGIL-8
- Status: `read_only_preview`

### 5. P1 · feed_issue_fix_preview · 44 itens
- Issue codes: strikethrough_price_updated
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:PLAYPRINTED-3, online:pt:BR:BB0231S-005, online:pt:BR:DZ5485031-5, online:pt:BR:DZ5485031-2, online:pt:BR:DZ6333083
- Status: `read_only_preview`

### 6. P1 · feed_issue_fix_preview · 19 itens
- Issue codes: landing_page_error
- Destinos reprovados: DisplayAds, Shopping, SurfacesAcrossGoogle
- Amostras de produto: online:pt:BR:1624428988081867066, online:pt:BR:10591784840915585992, online:pt:BR:12475328072847087695, online:pt:BR:10695397335246538087, online:pt:BR:14252480804615463970
- Status: `read_only_preview`

### 7. P1 · feed_issue_fix_preview · 9 itens
- Issue codes: availability_updated
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:RH24-2, online:pt:BR:RH24-1, online:pt:BR:SLPTMCS-2, online:pt:BR:SLFTPVNV-1, online:pt:BR:SLSTMCS-2
- Status: `read_only_preview`

### 8. P1 · feed_issue_fix_preview · 5 itens
- Issue codes: landing_page_pending_crawl, missing_item_attribute_for_product_type
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:12666760103914768713, online:pt:BR:7793455940120203308, online:pt:BR:17233744321540595259, online:pt:BR:3332348645938802802, online:pt:BR:11942764414726006273
- Status: `read_only_preview`

### 9. P1 · feed_issue_fix_preview · 4 itens
- Issue codes: condition_updated_from_detected
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: local:pt:BR:LIA_IG6192-3, local:pt:BR:LIA_IG6192-2, local:pt:BR:LIA_IG6192-4, local:pt:BR:LIA_IG6192-1
- Status: `read_only_preview`

### 10. P1 · feed_issue_fix_preview · 4 itens
- Issue codes: image_single_color
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:U9060PSD-1, online:pt:BR:U9060PSD-5, local:pt:BR:LIA_U9060PSD-5, local:pt:BR:LIA_U9060PSD-1
- Status: `read_only_preview`

### 11. P1 · feed_issue_fix_preview · 4 itens
- Issue codes: reserved_gtin
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:CZ0790-102-4, online:pt:BR:FN5880-001-4, local:pt:BR:LIA_CZ0790-102-4, local:pt:BR:LIA_FN5880-001-4
- Status: `read_only_preview`

### 12. P1 · feed_issue_fix_preview · 2 itens
- Issue codes: coupon_gtin
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:FZ4167-200-6, local:pt:BR:LIA_FZ4167-200-6
- Status: `read_only_preview`

## Amostras de fila individual

### 1. P1 · feed_issue_fix_preview
- Produto: Boné Aphase Basic Project - Used Black Preto
- Link: https://lksneakers.com.br/products/bone-aphase-basic-project-used-black-preto?currency=BRL&country=BR&variant=47007181209822&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- Issues: 9 · availability_updated, availability_updated, availability_updated, price_updated, price_updated
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 2. P1 · feed_issue_fix_preview
- Produto: Bolsa Aime Leon Dore Porsche Canvas Tote Bag - Cor Natural
- Link: https://lksneakers.com.br/products/bolsa-aime-leon-dore-porsche-canvas-tote-bag
- Issues: 6 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 3. P1 · feed_issue_fix_preview
- Produto: Bolsa Aimé Leon Dore x Porsche Nylon Briefcase Preto | LK Sneakers
- Link: https://lksneakers.com.br/products/bolsa-aime-leon-dore-x-porsche-nylon-briefcase-preto
- Issues: 6 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 4. P1 · feed_issue_fix_preview
- Produto: Calça Aphase Dusty - Stoned Beige Bege
- Link: https://lksneakers.com.br/products/calca-aphase-dusty-stoned-beige-bege?currency=BRL&country=BR&variant=47007263293662&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- Issues: 6 · price_updated, price_updated, price_updated, strikethrough_price_updated, strikethrough_price_updated
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 5. P1 · feed_issue_fix_preview
- Produto: Calça Saint Studio Plissada Tech Preto
- Link: https://lksneakers.com.br/products/calca-saint-studio-plissada-tech-preto?currency=BRL&country=BR&variant=46142651269342&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- Issues: 6 · price_updated, price_updated, price_updated, strikethrough_price_updated, strikethrough_price_updated
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 6. P1 · feed_issue_fix_preview
- Produto: Camisa Aphase Check - Light Yellow Bege
- Link: https://lksneakers.com.br/products/camisa-aphase-check-light-yellow-bege?currency=BRL&country=BR&variant=47007457706206&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- Issues: 6 · price_updated, price_updated, price_updated, strikethrough_price_updated, strikethrough_price_updated
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 7. P1 · feed_issue_fix_preview
- Produto: Camiseta Aphase Quadrile - Dirty Black Preto
- Link: https://lksneakers.com.br/products/camiseta-aphase-quadrile-dirty-black-preto?currency=BRL&country=BR&variant=47007585599710&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- Issues: 6 · price_updated, price_updated, price_updated, strikethrough_price_updated, strikethrough_price_updated
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 8. P1 · feed_issue_fix_preview
- Produto: Camiseta Pace PRB Off White
- Link: https://lksneakers.com.br/products/camiseta-pace-prb-off-white?currency=BRL&country=BR&variant=47019108434142&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- Issues: 6 · price_updated, price_updated, price_updated, strikethrough_price_updated, strikethrough_price_updated
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

## Top issue codes

- price_updated: 1080
- strikethrough_price_updated: 517
- missing_item_attribute_for_product_type: 180
- restricted_gtin: 100
- landing_page_error: 63
- availability_updated: 30
- image_single_color: 8
- reserved_gtin: 6
- image_link_broken: 6
- landing_page_pending_crawl: 5
- condition_updated_from_detected: 4
- restricted_nfs_policy_violation: 4
- coupon_gtin: 3
- multiple_sizes: 2
- pause_expired: 2

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
