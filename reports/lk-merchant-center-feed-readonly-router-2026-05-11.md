# LK Merchant Center Feed Read-only Router, 2026-05-11

Generated at: `2026-05-12T00:37:09.752806+00:00`

## Veredito

Merchant Center entrou na Fase 6 como fonte `fact_merchant_center`: status de feed, destinos, issues de item e cruzamento com GSC agora viram fila de diagnóstico, sem write em feed, Shopify ou Google.

## Snapshot

- Merchant Center ID presente no Doppler: True
- Produtos/status lidos: 5000
- Itens roteados na fila: 963
- P1: 963
- P2: 0
- Produtos com issue de item: 963
- Produtos com destino reprovado: 708
- Produtos cruzando oportunidade GSC: 1
- Writes liberados agora: 0

## Top grupos de problema

### 1. P1 · feed_issue_fix_preview · 345 itens
- Issue codes: item_missing_required_attribute
- Destinos reprovados: DisplayAds, Shopping, SurfacesAcrossGoogle
- Amostras de produto: online:pt:BR:LIA_1182A708.020-5, online:pt:BR:LIA_IH3999-38, online:pt:BR:FV5029-010-43, online:pt:BR:LIA_1201A789-020-38, online:pt:BR:LIA_IQ8601-001-44
- Status: `read_only_preview`

### 2. P1 · feed_issue_fix_preview · 307 itens
- Issue codes: item_missing_required_attribute, missing_item_attribute_for_product_type
- Destinos reprovados: DisplayAds, Shopping, SurfacesAcrossGoogle
- Amostras de produto: online:pt:BR:HV0823-100-5, online:pt:BR:BQ6472104-1, online:pt:BR:1201A789-020-41, online:pt:BR:1183C468200-2, online:pt:BR:DD0587-002-43
- Status: `read_only_preview`

### 3. P1 · feed_issue_fix_preview · 167 itens
- Issue codes: missing_item_attribute_for_product_type
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:17132474926828267951, online:pt:BR:12020378807434295587, online:pt:BR:2635861299432826332, online:pt:BR:12136334699203773021, online:pt:BR:17912240090608697983
- Status: `read_only_preview`

### 4. P1 · feed_issue_fix_preview · 42 itens
- Issue codes: price_updated
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:TB010061-713-3, online:pt:BR:TB010061-713-1, online:pt:BR:TB010061-713-4, online:pt:BR:w6334r-8, online:pt:BR:w6334r-10
- Status: `read_only_preview`

### 5. P1 · feed_issue_fix_preview · 33 itens
- Issue codes: checkout_url_invalid, item_missing_required_attribute, missing_item_attribute_for_product_type
- Destinos reprovados: DisplayAds, Shopping, SurfacesAcrossGoogle
- Amostras de produto: online:pt:BR:JI3185-7, online:pt:BR:HQ4309-610-40, online:pt:BR:U204L2SZ-36, online:pt:BR:U1906LNT-10, online:pt:BR:JH5439-8
- Status: `read_only_preview`

### 6. P1 · feed_issue_fix_preview · 22 itens
- Issue codes: price_updated, strikethrough_price_updated
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:20048-2, online:pt:BR:ST52-5, online:pt:BR:JR7435-2, online:pt:BR:JQ6445-1, online:pt:BR:JQ6446-2
- Status: `read_only_preview`

### 7. P1 · feed_issue_fix_preview · 14 itens
- Issue codes: restricted_gtin
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:FN4193100-2, online:pt:BR:U9060NRI-7, online:pt:BR:AQ3692-004-5, online:pt:BR:553558612-6, online:pt:BR:DD1503601-39
- Status: `read_only_preview`

### 8. P1 · feed_issue_fix_preview · 10 itens
- Issue codes: local_stores_lack_inventory
- Destinos reprovados: LocalSurfacesAcrossGoogle
- Amostras de produto: local:pt:BR:LIA_205759 610-2, local:pt:BR:LIA_205759 610-3, local:pt:BR:LIA_CZ8065 100-7, local:pt:BR:LIA_HF3144 100-8, local:pt:BR:LIA_HF3144 100-3
- Status: `read_only_preview`

### 9. P1 · feed_issue_fix_preview · 6 itens
- Issue codes: strikethrough_price_updated
- Destinos reprovados: no_disapproved_destination
- Amostras de produto: online:pt:BR:DC0774200-9, online:pt:BR:DC0774200-6, online:pt:BR:DC0774200, online:pt:BR:DC0774502-9, online:pt:BR:DC0774502-5
- Status: `read_only_preview`

### 10. P1 · feed_issue_fix_preview · 4 itens
- Issue codes: item_missing_required_attribute, landing_page_error, missing_item_attribute_for_product_type
- Destinos reprovados: SurfacesAcrossGoogle
- Amostras de produto: online:pt:BR:2258634078163248862, online:pt:BR:6562590402534581177, online:pt:BR:3876299146406606317, online:pt:BR:11810372920072143991
- Status: `read_only_preview`

### 11. P1 · feed_issue_fix_preview · 4 itens
- Issue codes: item_missing_required_attribute, missing_item_attribute_for_product_type
- Destinos reprovados: SurfacesAcrossGoogle
- Amostras de produto: online:pt:BR:10621083909303937387, online:pt:BR:14088693984092512857, online:pt:BR:1736512501686486863, online:pt:BR:6531799355487598672
- Status: `read_only_preview`

### 12. P1 · feed_issue_fix_preview · 3 itens
- Issue codes: checkout_url_invalid, item_missing_required_attribute
- Destinos reprovados: DisplayAds, Shopping, SurfacesAcrossGoogle
- Amostras de produto: online:pt:BR:HQ4307-605, online:pt:BR:ST88, online:pt:BR:HQ4307-400-43
- Status: `read_only_preview`

## Amostras de fila individual

### 1. P1 · feed_issue_fix_preview
- Produto: (sem título)
- Link: (sem link)
- Issues: 21 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: Shopping, DisplayAds, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 2. P1 · feed_issue_fix_preview
- Produto: (sem título)
- Link: (sem link)
- Issues: 21 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: Shopping, DisplayAds, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 3. P1 · feed_issue_fix_preview
- Produto: (sem título)
- Link: (sem link)
- Issues: 21 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: Shopping, DisplayAds, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 4. P1 · feed_issue_fix_preview
- Produto: (sem título)
- Link: (sem link)
- Issues: 21 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: Shopping, DisplayAds, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 5. P1 · feed_issue_fix_preview
- Produto: (sem título)
- Link: (sem link)
- Issues: 21 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: Shopping, DisplayAds, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 6. P1 · feed_issue_fix_preview
- Produto: (sem título)
- Link: (sem link)
- Issues: 21 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: Shopping, DisplayAds, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 7. P1 · feed_issue_fix_preview
- Produto: (sem título)
- Link: (sem link)
- Issues: 21 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: Shopping, DisplayAds, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

### 8. P1 · feed_issue_fix_preview
- Produto: (sem título)
- Link: (sem link)
- Issues: 21 · missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type, missing_item_attribute_for_product_type
- Destinos reprovados: Shopping, DisplayAds, SurfacesAcrossGoogle
- Destinos pendentes: nenhum
- Motivo: produto com issue/reprovação em Merchant Center
- Status: `read_only_preview`

## Top issue codes

- item_missing_required_attribute: 9655
- missing_item_attribute_for_product_type: 2454
- price_updated: 192
- strikethrough_price_updated: 87
- checkout_url_invalid: 36
- restricted_gtin: 22
- local_stores_lack_inventory: 10
- landing_page_error: 4
- restricted_nfs_policy_violation: 3
- condition_updated_from_detected: 2
- sexual_interests_policy_violation: 1
- reserved_gtin: 1

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
