# Receipt — Hermes follow-up 1-2-3 2026-06-25

- Data/hora: 2026-06-25T12:59:04.783895+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: operacoes
- Responsável humano: Lucas Cimino
- Pedido original: Lucas pediu Fazer 1 e 2 e 3: migrar LK Stock para secret_doppler, tratar Linear e warnings Telegram.
- Classificação: local-write
- Fontes usadas:
- Runtime local, Doppler lc-keys/prd helper/API, webhook_subscriptions.json, certificação no-op, Bot API getMe, logs locais e Linear smoke.
- O que foi feito:
- Rotas LK Stock migradas para secret_doppler WEBHOOK_SECRET sem literal local; WEBHOOK_SECRET canonizado no Doppler; helper default map atualizado; Linear diagnosticado; warnings Telegram classificados como watch sem degradação atual.
- Output/artefato:
- Webhooks 14/14 pass; Linear HTTP 401 com LINEAR_API_KEY presente porém inválido; Telegram getMe 12/12 OK; relatório em reports/governance/hermes-followup-1-2-3-2026-06-25.md.
- Aprovação: Aprovação no Telegram: Fazer 1 e 2 e 3.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: 0
- Riscos/bloqueios: Linear permanece bloqueado até token válido; WEBHOOK_SECRET é alias de compatibilidade para runtime atual.
- Rollback/mitigação: Backups em /opt/data/backups/webhook_subscriptions_*; para rollback restaurar webhook_subscriptions.json e remover/ajustar alias conforme necessário; hermes_doppler.py tem diff local revertível.
- Próximos passos: Se Linear for necessário, Lucas deve fornecer/autorizar token Linear válido; opcionalmente em janela futura restartar main gateway helper-launched para usar segredos específicos HERMES/LK_STOCK.
- Onde foi documentado no Brain: reports/governance/hermes-followup-1-2-3-2026-06-25.md; skill webhook-subscriptions reference lk-stock-dynamic-webhook-secret-doppler-alias-20260625.md.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
