# LK GMC Local C/D 63 Old LIA Cleanup Execution, 2026-05-12

Status: `gmc_local_cd_63_old_lia_cleanup_applied_verified`

## Resumo executivo
- Pacote: `local_cd_63_old_lia_cleanup_execution`
- Aprovação: Lucas opção 1 no Telegram, executar exatamente os 63 IDs locais antigos do approval packet final.
- Modo: `apply`
- Linhas aprovadas: 63
- Old IDs presentes no preflight: 63
- Old IDs já ausentes no preflight/idempotentes: 0
- Deletes OK/idempotentes: 63
- Falhas: 0
- Old IDs verificados ausentes: 63
- Old IDs ainda presentes: 0
- Replacement IDs verificados presentes: 14 / 14
- Replacement IDs ausentes: 0
- Snapshot privado rollback+execução: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-12-local-cd-63-old-lia-cleanup-execution-rollback-and-execution.json`

## Interpretação
- Foram removidos somente IDs locais antigos `local:pt:BR:LIA_<old_sku>` aprovados no pacote final.
- As linhas replacement locais atuais foram preservadas e verificadas após a execução.

## Não tocado
- online_products
- replacement_local_rows
- local_inventory_channel_or_pos_settings
- shopify
- tiny
- feed
- database
- campaign_or_external_send
- customer_facing_surfaces

## Arquivos
- JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-local-cd-63-old-lia-cleanup-execution.json`
- CSV: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-local-cd-63-old-lia-cleanup-execution.csv`
