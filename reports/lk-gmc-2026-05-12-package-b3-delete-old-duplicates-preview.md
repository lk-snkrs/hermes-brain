# LK GMC Package B3 Delete Old Duplicate Identifiers Preview, 2026-05-12

Status: `gmc_package_b3_delete_old_duplicates_preview_ready_no_writes`

## Resumo executivo
- Linhas avaliadas: 854
- Candidatos delete-old-only prontos para aprovação: 0
- Snapshot privado preview/rollback: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-12-package-b3-delete-old-duplicates-preview-rollback-preview.json`

## Veredito
- Os 854 B restantes foram bloqueados pelo guard same-ID: `old_product_id == correct_existing_product_id`.
- Portanto, não existe pacote delete-old-only seguro aqui; esses itens são no-op/valid_after_shopify_live.
- Nenhuma escrita foi feita e nenhuma aprovação de delete deve ser pedida para estes 854.

## Não tocado
- merchant_product_write_or_delete
- shopify_write
- feed
- database
- campaign_or_external_send
- local_channel
- pos_inventory

## Arquivos
- JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-package-b3-delete-old-duplicates-preview.json`
- CSV: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-package-b3-delete-old-duplicates-preview.csv`
