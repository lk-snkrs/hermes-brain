# LK GMC Package B3 Emergency Rollback Restore, 2026-05-12

Status: `gmc_package_b3_emergency_rollback_restored_verified`

## Resumo executivo
- Registros B3 totais: 854
- Ausentes antes do restore: 0
- Já presentes antes do restore: 854
- Restore OK: 0
- Restore falhou: 0
- Verificados presentes depois: 854
- Ainda ausentes: 0
- Merchant products após verificação: 23147
- Auditoria privada: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-12-package-b3-emergency-rollback-restore.json`

## Interpretação
- O preview B3 gerou falsos positivos porque old_product_id e target_product_id eram iguais para os 854.
- Executei rollback corretivo: reinseri os recursos originais que ficaram ausentes e não alterei os que já estavam presentes.
- Estado restaurado/verificado antes de qualquer novo pacote.

## Não tocado
- shopify_write
- feed
- database
- campaign_or_external_send
- local_channel
- pos_inventory
- google_business_profile
