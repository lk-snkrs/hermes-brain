# LK GMC Package B2 Shopify Live Identifier Fix Preview, 2026-05-12

Status: `gmc_package_b2_shopify_live_preview_ready_no_writes`

## Resumo executivo
- Linhas avaliadas a partir do Shopify live probe: 854
- Candidatos prontos para aprovação: 0
- Pulados old ausente: 0
- Pulados target já existente: 0
- Pulados já corretos: 0
- Snapshot privado preview/rollback: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-12-package-b2-shopify-live-preview-rollback-preview.json`

## Veredito
- Shopify live confirmou os 854 variants ativos com SKU, mas o SKU gera o mesmo product ID já existente.
- Com o guard same-ID, B2 agora é no-op: 0 linhas são candidatas a insert-new/delete-old.

## Não tocado
- merchant_product_write_or_delete
- shopify_write
- feed
- database
- campaign_or_external_send
- local_channel
- pos_inventory

## Arquivos
- JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-package-b2-shopify-live-preview.json`
- CSV: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-package-b2-shopify-live-preview.csv`
