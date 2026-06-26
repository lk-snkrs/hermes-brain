# LK Merchant Center Feed Read-only Router, 2026-05-11

Generated at: `2026-06-26T09:28:07.839348+00:00`

## Veredito

Merchant Center entrou na Fase 6 como fonte `fact_merchant_center`: status de feed, destinos, issues de item e cruzamento com GSC agora viram fila de diagnóstico, sem write em feed, Shopify ou Google.

## Snapshot

- Escopo de leitura: até 30000 produtos; full catalog esperado: True
- Merchant Center ID presente no Doppler: True
- Produtos/status lidos: 21673
- Itens roteados na fila: 10765
- P1: 10761
- P2: 4
- Produtos com issue de item: 10761
- Produtos com destino reprovado: 23
- Produtos cruzando oportunidade GSC: 5
- Writes liberados agora: 0

## Top grupos de problema

### 1. P1 · feed_issue_fix_preview · 10467 itens
- Issue codes: local_requires_review
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: local:pt:BR:LIA_LK-5524446-L, local:pt:BR:LIA_LK-5524446-XS, local:pt:BR:LIA_LK-5524446-M, local:pt:BR:LIA_LK-5524446-S, local:pt:BR:LIA_LK-5524446-XL
- Status: `read_only_preview`

### 2. P1 · feed_issue_fix_preview · 73 itens
- Issue codes: invalid_color
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:ALO-9029342-M, online:pt:BR:ADI-9091550-38, online:pt:BR:ADI-9091550-39, online:pt:BR:ADI-9091550-37, online:pt:BR:ADI-9091550-36
- Status: `read_only_preview`

### 3. P1 · feed_issue_fix_preview · 73 itens
- Issue codes: invalid_color, local_requires_review
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: local:pt:BR:LIA_ALO-9029342-M, local:pt:BR:LIA_ADI-9091550-39, local:pt:BR:LIA_ADI-9091550-36, local:pt:BR:LIA_ADI-9091550-35, local:pt:BR:LIA_ADI-9091550-34
- Status: `read_only_preview`

### 4. P1 · feed_issue_fix_preview · 36 itens
- Issue codes: strikethrough_price_updated
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:DZ5485031-1, online:pt:BR:DZ5485031-5, online:pt:BR:DZ5485031-3, online:pt:BR:DZ5485031-2, online:pt:BR:DZ6333083
- Status: `read_only_preview`

### 5. P1 · feed_issue_fix_preview · 33 itens
- Issue codes: restricted_gtin
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:U9060ZGE-9, online:pt:BR:U9060ZGE-4, online:pt:BR:1203A655-100-7, online:pt:BR:FN4193100-2, online:pt:BR:m2002rdb
- Status: `read_only_preview`

### 6. P1 · feed_issue_fix_preview · 21 itens
- Issue codes: price_updated
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:ST19-4, online:pt:BR:205759610-9, online:pt:BR:205759610-6, online:pt:BR:205759610-7, online:pt:BR:205759610-8
- Status: `read_only_preview`

### 7. P1 · feed_issue_fix_preview · 18 itens
- Issue codes: local_requires_review, local_stores_lack_inventory
- Destinos reprovados: LocalSurfacesAcrossGoogle
- Amostras de produto: local:pt:BR:LIA_1183B566021-6, local:pt:BR:LIA_1183B566021-1, local:pt:BR:LIA_1183B566021-3, local:pt:BR:LIA_1183B566021-5, local:pt:BR:LIA_1183B566021-4
- Status: `read_only_preview`

### 8. P1 · feed_issue_fix_preview · 17 itens
- Issue codes: missing_item_attribute_for_product_type
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:9780847872657, online:pt:BR:9783836572231, online:pt:BR:9783836597982, online:pt:BR:9783836596299, online:pt:BR:ALO-4649822-OS
- Status: `read_only_preview`

### 9. P1 · feed_issue_fix_preview · 5 itens
- Issue codes: landing_page_error
- Destinos reprovados: DisplayAds, Shopping, SurfacesAcrossGoogle
- Amostras de produto: online:pt:BR:15014470994320532817, online:pt:BR:5706324928133224313, online:pt:BR:CQ9446400-1, online:pt:BR:DN4045001, online:pt:BR:HJ0513-500-6
- Status: `read_only_preview`

### 10. P2 · gsc_feed_pdp_alignment_preview · 4 itens
- Issue codes: no_item_issue_code
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:HQ4307-002-11, online:pt:BR:HQ4307-001-10, online:pt:BR:HQ4307-001-11, online:pt:BR:HQ2050-103-10
- Status: `read_only_preview`

### 11. P1 · feed_issue_fix_preview · 3 itens
- Issue codes: price_updated, strikethrough_price_updated
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:4096148038527481596, online:pt:BR:7866599083713103688, online:pt:BR:DH4401101
- Status: `read_only_preview`

### 12. P1 · feed_issue_fix_preview · 2 itens
- Issue codes: image_link_internal_error
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:L49154600-41, online:pt:BR:L49154600-37
- Status: `read_only_preview`

## Amostras de fila individual

### 1. P1 · feed_issue_fix_preview
- Produto: 34
- Link: https://lksneakers.com.br/products/tenis-adidas-samba-og-silver-metallic-cracked-leather-prateado
- Issues: 6 · price_updated, price_updated, price_updated, strikethrough_price_updated, strikethrough_price_updated
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 2. P1 · feed_issue_fix_preview
- Produto: 38
- Link: https://lksneakers.com.br/products/tenis-adidas-samba-og-cream-white-cardboard-creme
- Issues: 6 · price_updated, price_updated, price_updated, strikethrough_price_updated, strikethrough_price_updated
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 3. P1 · feed_issue_fix_preview
- Produto: Moletom Fear Of God Essentials Classic Full Zip-Up Jet Black Preto
- Link: https://lksneakers.com.br/products/moletom-fear-of-god-essentials-classic-full-zip-up-jet-black-preto
- Issues: 6 · availability_updated, availability_updated, availability_updated, price_updated, price_updated
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 4. P1 · feed_issue_fix_preview
- Produto: Tênis Nike Dunk Low Blue Paisley Azul
- Link: https://lksneakers.com.br/products/nike-dunk-low-blue-paisley?currency=BRL&country=BR&variant=45065961767134&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- Issues: 6 · price_updated, price_updated, price_updated, strikethrough_price_updated, strikethrough_price_updated
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 5. P1 · feed_issue_fix_preview
- Produto: Tênis Nike Air Jordan 1 Low SE Sky J Mauve Roxo
- Link: https://lksneakers.com.br/products/air-jordan-1-low-se-sky-j-mauve?currency=BRL&country=BR&variant=45278615175390&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- Issues: 5 · restricted_gtin, restricted_gtin, strikethrough_price_updated, strikethrough_price_updated, strikethrough_price_updated
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 6. P1 · feed_issue_fix_preview
- Produto: Boné Aimé Leon Dore Saint George Logo Hat Bege/Marrom
- Link: https://lksneakers.com.br/products/bone-aime-leon-dore-saint-george-logo-hat-bege-marrom
- Issues: 3 · availability_updated, availability_updated, availability_updated
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 7. P1 · feed_issue_fix_preview
- Produto: Calça Saint Studio Plissada Tech Preto
- Link: https://lksneakers.com.br/products/calca-saint-studio-plissada-tech-preto?currency=BRL&country=BR&variant=46145845362910&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- Issues: 3 · price_updated, price_updated, price_updated
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 8. P1 · feed_issue_fix_preview
- Produto: Crocs Classic Clog x The Cars Lightning McQueen Vermelho
- Link: https://lksneakers.com.br/products/crocs-classic-clog-x-the-cars-lightning-mcqueen-vermelho?currency=BRL&country=BR&variant=44834189738206&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- Issues: 3 · price_updated, price_updated, price_updated
- Destinos reprovados: nenhum
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

## Top issue codes

- local_requires_review: 10562
- invalid_color: 292
- strikethrough_price_updated: 120
- price_updated: 75
- restricted_gtin: 68
- missing_item_attribute_for_product_type: 34
- local_stores_lack_inventory: 18
- landing_page_error: 15
- image_link_internal_error: 8
- image_single_color: 8
- availability_updated: 6
- reserved_gtin: 4
- pause_expired: 2
- image_too_small_for_high_resolution: 1

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
