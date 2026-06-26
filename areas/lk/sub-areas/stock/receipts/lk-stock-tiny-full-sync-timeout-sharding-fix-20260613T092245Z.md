# Receipt — LK Stock Tiny full sync timeout sharding fix

- Data/hora: 2026-06-13T09:23:13.048807+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK Sneakers / Stock OS
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas respondeu seguir ao diagnóstico de timeout do cron LK Stock Tiny full sync nightly read-only.
- Classificação: local-write
- Fontes usadas:
- Cron c45da7bb0fcb last_status=error por timeout 3600s; relatório real 20260613T062031Z status ok rows_updated=3028 rows_failed=0; testes unittest locais.
- O que foi feito:
- Adicionado suporte a offset/limit no full sync; wrapper cron agora calcula 3 shards UTC 06/07/08 e processa aproximadamente 1010 linhas por shard; mantido throttle 1.2s e batching SQLite commit_every=25; cron existente atualizado para 20 6,7,8 * * *.
- Output/artefato:
- Script areas/lk/sub-areas/stock/scripts/lk_stock_tiny_full_sync.py atualizado; wrapper /opt/data/profiles/lk-stock/scripts/lk_stock_tiny_full_sync_nightly.py atualizado; cron c45da7bb0fcb renomeado para LK Stock Tiny sharded full sync nightly read-only.
- Aprovação: Escopo aprovado por reply “Seguir” ao incidente de timeout; sem Tiny/Shopify writes.
- Envio/publicação: Telegram final após verificação.
- Writes externos: 0
- Riscos/bloqueios: Primeira execução sharded real ocorrerá na próxima janela; se Tiny rate-limit/transiente ocorrer, job continua alertando partial/failure.
- Rollback/mitigação: Reverter diff dos scripts e restaurar cron c45da7bb0fcb para schedule 20 6 * * * e nome anterior.
- Próximos passos: Observar próxima execução 06:20/07:20/08:20 UTC; se houver partial por Tiny, investigar ledger do DB do shard.
- Onde foi documentado no Brain: Receipt canônico criado via Memory OS writer; testes e smoke registrados na resposta.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
