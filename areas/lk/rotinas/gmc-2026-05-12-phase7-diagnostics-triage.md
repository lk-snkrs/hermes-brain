# LK GMC Phase 7 Diagnostics Triage, 2026-05-12

Status: `gmc_phase7_diagnostics_triage_readonly_ready`

## Resumo executivo
- Merchant products/statuses atuais: 23194 / 23194
- Linhas com item issues: 2563
- Instâncias de item issues: 11791
- Delta vs baseline Phase 7: 0

## Buckets de ação
- P1 `attribute_completion_preview`: 10162 instâncias; produtos afetados=2100; canais={'online': 10162}; recomendação=Build no-write exact-ID attribute completion packet from current diagnostics.
- P3 `merchant_auto_update_monitor`: 1492 instâncias; produtos afetados=380; canais={'online': 1488, 'local': 4}; recomendação=Monitor; usually not a direct remediation target.
- P2 `gtin_policy_review`: 112 instâncias; produtos afetados=75; canais={'online': 74, 'local': 38}; recomendação=Manual catalog/policy review before edit; GTIN changes can be risky.
- P2 `image_asset_review`: 13 instâncias; produtos afetados=7; canais={'local': 2, 'online': 11}; recomendação=Read-only image probe first.
- P3 `misc_manual_review`: 7 instâncias; produtos afetados=6; canais={'online': 7}; recomendação=Sample first.
- P2 `policy_manual_review`: 5 instâncias; produtos afetados=2; canais={'local': 1, 'online': 4}; recomendação=Manual review; avoid automated content edits.

## Veredito
- O próximo bloco com maior alavanca é P1 attribute_completion_preview, seguido por checkout_url_readonly_probe. Nenhum write foi executado; qualquer aplicação exigirá pacote exato e aprovação.

## Próximo bloco seguro
- Build P1 attribute completion preview from exact current product IDs and issue attributes; output no-write approval packet only.

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
- JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-phase7-diagnostics-triage.json`
- CSV buckets: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-phase7-diagnostics-triage-buckets.csv`
