# LK GMC Package B Identifier Fix, 2026-05-12

Status: `gmc_package_b_identifier_fix_applied_verified_second_pass_no_new_safe_rows`

## Resumo executivo
- Pacote: `B_online_identifier_fix`
- Modo: `apply_cumulative_then_second_pass`
- Registros B no snapshot: 954
- Aplicados/verificados: 93
- Segunda passada depois do A: 0 novos seguros
- Preservados sem alvo unambíguo: 854
- Preservados por alvo já existente/old ainda presente: 7
- Falhas finais: 0
- Snapshot privado de rollback: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-12-package-b-identifier-fix-rollback.json`

## Interpretação
- Mantive o B estrito: só SKU alvo unambíguo foi aplicado.
- Depois do A, rodei B novamente; não havia novo B seguro para aplicar.
- Não forcei os 854 ambíguos.

## Não tocado
- local_channel
- shopify
- feed
- database
- campaign_or_external_send
- google_business_profile
- pos_inventory

## Arquivos
- JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-package-b-identifier-fix.json`
- CSV: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-package-b-identifier-fix.csv`
