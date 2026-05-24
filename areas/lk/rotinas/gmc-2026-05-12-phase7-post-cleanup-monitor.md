# LK GMC Phase 7 Post-cleanup Monitor, 2026-05-12

Status: `gmc_phase7_post_cleanup_monitor_readonly_ready`

## Resumo executivo
- Merchant products atuais: 23194
- Merchant productstatuses atuais: 23194
- Online/local atuais: 11617 / 11577
- Local C/D cleanup: old IDs ausentes 63/63; replacement IDs presentes 14/14
- Linhas com item issues: 2563
- Instâncias de item issues: 11791
- Linhas com destination problem: 17

## Top item issues atuais
- missing_item_attribute_for_product_type: 10152
- price_updated: 1002
- strikethrough_price_updated: 486
- restricted_gtin: 103
- item_missing_required_attribute: 10
- image_single_color: 8
- reserved_gtin: 6
- landing_page_error: 5
- condition_updated_from_detected: 4
- restricted_nfs_policy_violation: 4
- image_link_broken: 4
- coupon_gtin: 3

## Top destination statuses atuais
- SurfacesAcrossGoogle:approved: 11601
- LocalSurfacesAcrossGoogle:approved: 11577
- Shopping:approved: 11568
- DisplayAds:approved: 11567
- SurfacesAcrossGoogle:disapproved: 16
- DisplayAds:disapproved: 1

## Veredito
- Pós-limpeza local C/D segue saudável: 63 old IDs continuam ausentes e 14 replacement rows continuam presentes. A limpeza está encerrada operacionalmente; o próximo ganho deve vir de diagnostics/delta, não de repetir deletes locais.

## Próximo bloco seguro
- Read-only diagnostics delta after Merchant reprocessing window: compare issue codes/counts against this Phase 7 baseline.
- If issues remain material, build a new approval packet only from exact current product IDs with rollback snapshot; no broad deletes.
- Refresh Mission Control with this baseline once diagnostics stabilizes.

## Não executado
- merchant_product_delete
- merchant_product_insert
- merchant_product_update
- content_api_custombatch
- datafeed_fetchNow
- feed_update
- shopify_write
- tiny_write
- database_write
- pos_or_local_inventory_setting_change
- campaign_or_external_send

## Arquivos
- JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-phase7-post-cleanup-monitor.json`
- CSV issues: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-phase7-post-cleanup-monitor-issue-summary.csv`
