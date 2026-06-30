# Receipt — Hermes all-agents provider auth audit

- Data/hora: 2026-06-30T16:59:56.147765+00:00
- Agente/profile/cron: default
- Empresa/área: Operações Hermes / Runtime
- Responsável humano: Lucas Cimino
- Pedido original: Auditar todos os agentes com alerta Provider authentication failed
- Classificação: read-only
- Fontes usadas:
- Processos /proc HERMES_HOME, logs sanitizados, auth list/config check sem valores, smokes hermes -z por profile
- O que foi feito:
- Auditados 17 profiles; falha atual localizada no lk-ops; histórico/stale separado de funcionamento atual; criado approval packet scoped para correção lk-ops
- Output/artefato:
- reports/governance/hermes-all-agents-provider-auth-audit-2026-06-30.md; areas/operacoes/approval-packets/hermes-provider-auth-lk-ops-codex-repair-20260630.md
- Aprovação: Auditoria read-only autônoma; correção de auth/restart ainda pendente de aprovação explícita
- Envio/publicação: Telegram resumo executivo
- Writes externos: 0
- Riscos/bloqueios: lk-ops com openai-codex token_expired atual; outros profiles com histórico/dormant ou smoke inconclusivo sem 401 atual
- Rollback/mitigação: Remover report/packet/receipt locais se necessário; nenhuma mudança runtime/auth executada
- Próximos passos: Se Lucas aprovar, executar packet de reparo somente no lk-ops com backup, sync credential_pool.openai-codex do default, smoke e restart scoped
- Onde foi documentado no Brain: reports/governance/hermes-all-agents-provider-auth-audit-2026-06-30.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
