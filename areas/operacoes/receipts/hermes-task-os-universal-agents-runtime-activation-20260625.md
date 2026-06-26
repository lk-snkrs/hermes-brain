# Receipt — Hermes Task OS universal agents runtime activation 2026-06-25

- Data/hora: 2026-06-25T17:20:18.952907+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: operacoes
- Responsável humano: Lucas Cimino
- Pedido original: Lucas autorizou ativar a regra Task OS universal nos runtimes vivos.
- Classificação: infra-sensitive
- Fontes usadas:
- AGENTS.md profile-local; global gateway watchdog; /proc exact HERMES_HOME process inspection; gateway_state.json; API/webhook health; Task OS Kanban diagnostics.
- O que foi feito:
- Managed specialist gateways reiniciados/reativados; spiti-atendimento surface scrub corrigido no watchdog; validação pós-ativação concluída.
- Output/artefato:
- reports/governance/hermes-task-os-universal-agents-runtime-activation-2026-06-25.md
- Aprovação: Aprovação explícita de Lucas: pode dar restart e ativar.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: 0
- Riscos/bloqueios: Main/default não foi reiniciado por guardrail de self-restart; precisa shell externo/mecanismo próprio se Lucas quiser ativação imediata do Main.
- Rollback/mitigação: Usar backups de AGENTS.md em /opt/data/backups/task-os-universal-agents-20260625T165853Z e reexecutar watchdog; para desfazer patch do watchdog, reverter diff local de scrub pós-Doppler.
- Próximos passos: Observar comportamento dos especialistas; ativar Main/default externamente se necessário.
- Onde foi documentado no Brain: reports/governance/hermes-task-os-universal-agents-runtime-activation-2026-06-25.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
