# LK GMC Package B3 Delete Old Duplicate Identifiers Execution, 2026-05-12

Status: `gmc_package_b3_delete_old_duplicates_applied_verified`

## Resumo executivo
- Pacote: `B3_delete_old_duplicate_identifier_execution`
- Aprovação: Lucas opção 1, executar B3
- Linhas aprovadas: 854
- Deletes OK/idempotentes: 854
- Falhas: 0
- Old IDs verificados ausentes: 841
- Correct IDs verificados presentes: 13
- Snapshot privado de rollback: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-12-package-b3-delete-old-duplicates-execution-rollback.json`

## Interpretação
- Delete-old-only remove os IDs antigos duplicados e mantém os IDs corretos existentes no Merchant.
- Nenhum produto correto, Shopify, feed, banco, local/POS ou campanha foi alterado.

## Não tocado
- shopify_write
- feed
- database
- campaign_or_external_send
- local_channel
- pos_inventory
- google_business_profile

## Arquivos
- JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-package-b3-delete-old-duplicates-execution.json`
- CSV: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-package-b3-delete-old-duplicates-execution.csv`
## Status posterior / correção

- Este resultado foi **superseded** por rollback corretivo: o preview B3 era inseguro porque `old_product_id` e `correct_existing_product_id` eram iguais nos 854 casos.
- A execução removeu produtos reais, então foi revertida imediatamente com reinserção dos recursos originais.
- Relatório corretivo: `reports/lk-gmc-2026-05-12-package-b3-emergency-rollback-restore.md`.
- Estado verificado após rollback: 23.147 produtos no Merchant; 854/854 IDs B3 presentes novamente.

