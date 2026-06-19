# Receipt — LK Tiny full sync timeout auto-remediation

- Data/hora: 2026-06-18T10:08:04.243843+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK Sneakers / Stock OS / Tiny sync
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas questionou por que o timeout/trava do sync Tiny não foi auto-corrigido.
- Classificação: local-write
- Fontes usadas:
- cronjob list; cron outputs c45da7bb0fcb; pointer/SQLite tiny_full_sync_runs e ledger; processo órfão ps; wrapper lk_stock_tiny_full_sync_nightly.py.
- O que foi feito:
- Verificado: Sales OS Shopify rodou OK às 05:41 UTC; Tiny full sync 06:20 UTC completou OK depois do timeout do scheduler; shard 08:20 UTC continuou órfão após timeout e completou OK às 10:04:06Z com 3895/3895 updated e rows_failed=0.
- Causa raiz: shards de ~3897 linhas excediam o hard timeout de 3600s do scheduler; o wrapper usava subprocess.run sem timeout/start_new_session/kill group, então o scheduler marcava erro e o child continuava órfão. deliver=local também impedia alerta acionável no Telegram.
- Auto-remediação aplicada: wrapper agora usa 6 shards UTC 6-11, lock anti-overlap, timeout interno 3300s, start_new_session e kill do process group em timeout; cron atualizado para 20 6,7,8,9,10,11 * * * e deliver origin.
- Skill lk-stock atualizada com regra durável: timeout/trava do sync Tiny é falha acionável, não output local silencioso; checar child órfão/pointer/ledger antes de concluir.
- Output/artefato:
- /opt/data/profiles/lk-stock/scripts/lk_stock_tiny_full_sync_nightly.py
- cronjob c45da7bb0fcb schedule=20 6,7,8,9,10,11 * * * deliver=origin
- Aprovação: Auto-remediação local/read-only em cron existente e wrapper local; sem Tiny/Shopify writes.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: 0
- Riscos/bloqueios: Próximo tick 10:20 UTC roda shard adicional com a nova divisão; OK continua silencioso, erro agora volta ao Telegram.
- Rollback/mitigação: Restaurar /opt/data/profiles/lk-stock/scripts/lk_stock_tiny_full_sync_nightly.py.bak-20260618-auto-remediation e cron c45da7bb0fcb para schedule 20 6,7,8 * * * deliver local.
- Próximos passos: Monitorar próximo tick; se ainda exceder 3300s, reduzir ainda mais shard ou otimizar Tiny readback.
- Onde foi documentado no Brain: /opt/data/profiles/lk-stock/skills/productivity/lk-stock/SKILL.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
