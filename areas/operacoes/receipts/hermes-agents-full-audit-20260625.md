# Receipt — Hermes agents full audit

- Data/hora: 2026-06-25T19:08:35.812346+00:00
- Agente/profile/cron: default
- Empresa/área: Hermes Operações / Multi-profile runtime
- Responsável humano: Hermes
- Pedido original: Lucas pediu novo audit nos agentes, AGENTS e etc, perguntando se está tudo OK.
- Classificação: read-only
- Fontes usadas:
- Profile identity files; /proc live gateway env shape; gateway_state.json; hermes kanban stats/diagnostics; hermes cron list --all; Brain health; support identity smoke harness; cron output artifact a97a6317b197.
- O que foi feito:
- Auditou 17 profiles; confirmou Task OS em 17/17 AGENTS e 16/16 SOUL não-default; confirmou 12 gateways reais vivos; rodou Brain health; rodou Kanban diagnostics/stats; rodou smokes seguros em support profiles; identificou 1 cron ativo com erro atual e 1 profile dormant com auth expirada; gerou relatório executivo.
- Output/artefato:
- reports/governance/hermes-agents-full-audit-2026-06-25.md; /opt/data/backups/hermes-agents-audit-20260625T190037Z/
- Aprovação: Read-only/local audit solicitado por Lucas; sem mutation externa/prod/secrets.
- Envio/publicação: Resumo final no Telegram; relatório/receipt no Brain.
- Writes externos: 0
- Riscos/bloqueios: Não é clean-green: cron Zipper post-PDF follow-up watchdog está ativo e falhou com send_failed/server error 463; brain-process dormant está com HTTP 401 token_expired; secondary gateways têm webhook secret herdado no env apesar de webhook disabled.
- Rollback/mitigação: Sem mudanças de runtime. Relatório/receipt podem ser arquivados se substituídos por novo audit.
- Próximos passos: Decidir pausar/repairar cron a97a6317b197; aprovar repair de auth brain-process; aprovar hardening para limpar WEBHOOK_SECRET de secondary gateway envs.
- Onde foi documentado no Brain: Sim: relatório em reports/governance e receipt em areas/operacoes/receipts.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
