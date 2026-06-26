# LK GMC — Missing color high-confidence apply — 2026-05-31

Status: `gmc_missing_color_high_confidence_apply_finished`

## Resultado
- Linhas aprovadas: 783
- Execução: {'patched_color_productinputs_v1': 765, 'failed_patch_color_productinputs_v1': 18}
- Verificação por Content API products list: 765/783

## Antes
- Missing color products: 1001
- Required attr counts: {'color': 1001, 'size': 244, 'age group': 214, 'gender': 214, 'price': 23}

## Depois imediato
- Missing color products: 246
- Required attr counts: {'color': 246, 'size': 241, 'age group': 211, 'gender': 211, 'price': 23}
- Observação: itemLevelIssues do GMC podem levar horas/dias para cair; validação D+7 recomendada.

## Rollback privado
- `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-31-missing-color-high-confidence-fast-apply-rollback-20260531T170812Z.json`

## Não executado
- price_update
- availability_update
- title_update
- image_update
- gtin_update
- feed_fetch_or_reprocess
- shopify_write
- tiny_write
- campaign_or_message_send
