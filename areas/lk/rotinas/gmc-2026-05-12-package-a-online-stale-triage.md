# LK GMC Package A Online Stale Triage, 2026-05-12

Status: `gmc_package_a_online_stale_triage_applied_verified`

## Resumo executivo
- Pacote: `A_online_stale_triage`
- Modo: `apply_final_verified`
- Registros A no snapshot: 2415
- Product IDs verificados ausentes no final: 2415
- Falhas finais: 0
- Snapshot privado de rollback: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-12-package-a-online-stale-triage-rollback.json`

## Interpretação
- Executei o pacote A por product IDs online exatos do bucket `online_unmatched_possible_stale`.
- A execução foi concluída em rodadas por causa de timeout local e consistência eventual da Content API; o critério final é live: todos os IDs A estão ausentes.
- Não mexi em local, Shopify, feed, banco ou POS.

## Não tocado
- local_channel
- shopify
- feed
- database
- campaign_or_external_send
- google_business_profile
- pos_inventory

## Arquivos
- JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-package-a-online-stale-triage.json`
- CSV: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-package-a-online-stale-triage.csv`
