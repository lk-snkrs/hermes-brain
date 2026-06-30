# Receipt — SPITI provider auth repair

- Data/hora: 2026-06-30T19:56:57.232240+00:00
- Agente/profile/cron: default
- Empresa/área: Operações Hermes / Runtime SPITI
- Responsável humano: Lucas Cimino
- Pedido original: Corrigir Provider authentication failed no @SPITI_HermesBot
- Classificação: local-write
- Fontes usadas:
- Logs SPITI, auth/config hashes sanitizados, Telegram getMe, smoke hermes -z, approval packet hermes-provider-auth-spiti-codex-repair-20260630.md
- O que foi feito:
- Backup profile-local; sync somente credential_pool.openai-codex do default; remoção de provider local stale; smoke OK; restart scoped spiti; readback Telegram/API/Webhook/DOPPLER; smoke pós-restart OK
- Output/artefato:
- reports/governance/hermes-provider-auth-spiti-codex-repair-2026-06-30.md
- Aprovação: Lucas aprovou via opção: Aprovo corrigir só o SPITI
- Envio/publicação: Telegram resumo executivo
- Writes externos: 0
- Riscos/bloqueios: rc=134 no hermes -z continua como warning de shutdown pós-output; logs antigos ainda contêm 401 anterior à correção
- Rollback/mitigação: Restaurar auth.json.before/config.yaml.before de /opt/data/backups/spiti-codex-auth-repair-20260630T195453Z/ e reiniciar somente spiti
- Próximos passos: Monitorar se SPITI volta a emitir 401; não fazer batch global sem evidência por profile
- Onde foi documentado no Brain: reports/governance/hermes-provider-auth-spiti-codex-repair-2026-06-30.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
