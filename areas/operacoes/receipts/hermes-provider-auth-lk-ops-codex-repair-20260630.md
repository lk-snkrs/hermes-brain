# Receipt — LK Ops provider auth repair

- Data/hora: 2026-06-30T17:06:28.883599+00:00
- Agente/profile/cron: default
- Empresa/área: Operações Hermes / Runtime
- Responsável humano: Lucas Cimino
- Pedido original: Corrigir provider authentication failed no lk-ops após auditoria all-agents
- Classificação: local-write
- Fontes usadas:
- Auditoria logs/auth/config/smoke; approval packet hermes-provider-auth-lk-ops-codex-repair-20260630.md; aprovação Telegram de Lucas
- O que foi feito:
- Backup profile-local; sync somente credential_pool.openai-codex do default; remoção de provider local stale; smoke OK; restart scoped lk-ops; readback Telegram/API/Webhook/DOPPLER; smoke pós-restart OK
- Output/artefato:
- reports/governance/hermes-provider-auth-lk-ops-codex-repair-2026-06-30.md
- Aprovação: Lucas: Aprovo
- Envio/publicação: Telegram resumo executivo
- Writes externos: 0
- Riscos/bloqueios: rc=134 no hermes -z continua como warning de shutdown pós-output; logs antigos ainda contêm 401 anterior à correção
- Rollback/mitigação: Restaurar auth.json.before/config.yaml.before de /opt/data/backups/lk-ops-codex-auth-repair-20260630T170418Z/ e reiniciar somente lk-ops
- Próximos passos: Monitorar se lk-ops volta a emitir 401; não fazer batch global sem nova evidência por profile
- Onde foi documentado no Brain: reports/governance/hermes-provider-auth-lk-ops-codex-repair-2026-06-30.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
