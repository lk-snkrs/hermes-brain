# LK GMC Correction Preview, 2026-05-12

Generated at: `2026-05-12T01:47:41.404184+00:00`

## Veredito

Status: `gmc_correction_preview_ready_readonly`

Transforma os P1 do Merchant Center em pacotes de correção preview-only. Não altera Merchant Center, Shopify, feed, PDP, Search Console, campanhas ou n8n.

## Resumo

- Product statuses lidos na origem: 5000
- Fila origem P1/P2: 963 itens, 963 P1
- Produtos com destino reprovado: 708
- Pacotes gerados: 6 (1 P0, 3 P1, 2 P2)
- Itens cobertos por pacotes preview-only: 963
- Writes/envios/contatos/compras/marketplace/n8n: 0/0/0/0/0

## Pacotes

### P0 · P0_admin_url_checkout_landing_review
- Itens afetados: 40
- Estimativa com reprovação: 40
- Superfície provável: Merchant account / checkout URL / PDP availability
- Próximo seguro: verify checkout/PDP URL samples in browser/admin and prepare exact admin fix preview; no URL/feed write now
- Aprovação necessária para write: Merchant/Shopify admin change or feed URL rule change
- Top issue codes: item_missing_required_attribute=40, missing_item_attribute_for_product_type=37, checkout_url_invalid=36, landing_page_error=4
- Top atributos no sample: age group=64, gender=64, size=32
- Sample IDs: online:pt:BR:JI3185-7, online:pt:BR:HQ4309-610-40, online:pt:BR:U204L2SZ-36, online:pt:BR:U1906LNT-10, online:pt:BR:JH5439-8, online:pt:BR:JH5439-6, online:pt:BR:HQ4307-101-38, online:pt:BR:HQ4307-300-43

### P1 · P1_required_attributes_feed_mapping
- Itens afetados: 826
- Estimativa com reprovação: 658
- Superfície provável: Shopify product data or feed mapping for required attributes
- Próximo seguro: create attribute template by product type: age_group, gender, color, size, material/pattern where applicable; preview exact mapping only
- Aprovação necessária para write: Shopify product/metafield update or Merchant feed rule/supplemental feed update
- Top issue codes: item_missing_required_attribute=658, missing_item_attribute_for_product_type=479, sexual_interests_policy_violation=1, restricted_nfs_policy_violation=1, strikethrough_price_updated=1
- Top atributos no sample: age group=96, gender=96, size=48
- Sample IDs: online:pt:BR:LIA_1182A708.020-5, online:pt:BR:LIA_IH3999-38, online:pt:BR:FV5029-010-43, online:pt:BR:LIA_1201A789-020-38, online:pt:BR:LIA_IQ8601-001-44, online:pt:BR:LIA_DB4612-100-7, online:pt:BR:KAWS005, online:pt:BR:LIA_398846_18-2

### P1 · P1_gtin_identifier_compliance_review
- Itens afetados: 14
- Estimativa com reprovação: 0
- Superfície provável: Identifier policy / GTIN / identifier_exists mapping
- Próximo seguro: prepare SKU-level identifier compliance list; decide whether GTIN is valid, blank, or identifier_exists=false before feed write
- Aprovação necessária para write: Shopify metafield/feed identifier mapping update
- Top issue codes: restricted_gtin=14
- Top atributos no sample: n/a
- Sample IDs: online:pt:BR:FN4193100-2, online:pt:BR:U9060NRI-7, online:pt:BR:AQ3692-004-5, online:pt:BR:553558612-6, online:pt:BR:DD1503601-39, online:pt:BR:FN5880-001-3, online:pt:BR:HF7743-001-6, online:pt:BR:IH5459-3

### P1 · P1_local_inventory_program_review
- Itens afetados: 10
- Estimativa com reprovação: 10
- Superfície provável: Local inventory feed / local surfaces configuration
- Próximo seguro: review whether LK wants LocalSurfaces active and reconcile local inventory feed mapping before any change
- Aprovação necessária para write: Merchant local inventory feed/config update
- Top issue codes: local_stores_lack_inventory=10
- Top atributos no sample: n/a
- Sample IDs: local:pt:BR:LIA_205759 610-2, local:pt:BR:LIA_205759 610-3, local:pt:BR:LIA_CZ8065 100-7, local:pt:BR:LIA_HF3144 100-8, local:pt:BR:LIA_HF3144 100-3, local:pt:BR:LIA_HV5980 231-3, local:pt:BR:LIA_HV5980 231-2, local:pt:BR:LIA_HV5980 231-5

### P2 · P2_price_sync_monitor
- Itens afetados: 70
- Estimativa com reprovação: 0
- Superfície provável: Merchant price crawl freshness / Shopify price sync
- Próximo seguro: monitor unless persistent with disapproval; compare sample PDP price vs Merchant after next crawl
- Aprovação necessária para write: price/feed change only if persistent mismatch is verified
- Top issue codes: price_updated=64, strikethrough_price_updated=28
- Top atributos no sample: n/a
- Sample IDs: online:pt:BR:TB010061-713-3, online:pt:BR:TB010061-713-1, online:pt:BR:TB010061-713-4, online:pt:BR:w6334r-8, online:pt:BR:w6334r-10, online:pt:BR:ID2529-3, online:pt:BR:01424-002-2, online:pt:BR:CJ5378700-36

### P2 · P2_other_feed_issue_review
- Itens afetados: 3
- Estimativa com reprovação: 0
- Superfície provável: Other Merchant issue
- Próximo seguro: review issue details and sample products before proposing any write
- Aprovação necessária para write: depends on issue; no write allowed from this preview
- Top issue codes: condition_updated_from_detected=2, reserved_gtin=1
- Top atributos no sample: n/a
- Sample IDs: local:pt:BR:LIA_IG6192-3, local:pt:BR:LIA_IG6192-2, local:pt:BR:LIA_CZ0790-102-4

## Checks

- OK: `source_router_available` — Merchant router JSON has grouped issues and queue sample.
- OK: `writes_blocked` — Preview performs no external write/send/contact/purchase.
- OK: `packages_cover_all_groups` — Packages cover grouped queue counts from Merchant router.

## Não executado

- merchant_center_write
- supplemental_feed_update
- product_insert_update_delete
- shopify_product_or_variant_write
- shopify_theme_or_pdp_write
- gsc_admin_or_indexing_submit
- campaign_or_customer_send
- supplier_contact
- purchase_or_po
- n8n_flow_creation
