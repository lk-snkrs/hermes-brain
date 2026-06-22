# Receipt — Memory OS reconhece Honcho como provider governado

- Data/hora: 2026-06-21T12:39:28.827443+00:00
- Agente/profile/cron: Hermes/Operações + Memory OS
- Empresa/área: areas/operacoes
- Responsável humano: Hermes/Operações + Memory OS
- Pedido original: Lucas aprovou Opção A: tratar Honcho como provider governado sem mexer no runtime
- Classificação: local-write
- Fontes usadas:
- Mesa COO 2026-06-21 Decisão 1/3 aprovada por Lucas
- scripts/hermes_memory_hygiene_watchdog.py
- scripts/hermes_memory_os_daytime_checker.py
- scripts/hermes_memory_os_context_recovery_probe.py
- scripts/hermes_memory_os_weekly_observability.py
- memories/politica-memoria-hermes.md
- O que foi feito:
- Política Memory OS separa Mem0/provider externo genérico de Honcho governado
- Watchdog local aceita memory.provider=honcho apenas quando honcho.json e watchdog Honcho passam health/workspace/peer/save/recall
- Scorecard, context-recovery e weekly observability deixam de alertar por provider ativo quando Honcho está governado
- Output/artefato:
- py_compile=ok; honcho_watchdog_stdout_bytes=0; memory_hygiene_stdout_bytes=0; daytime_status=ok; context_status=ok; weekly_stdout_bytes=0; scoped_possible_secrets=0; values_printed=false
- Aprovação: Aprovado por Lucas no Telegram: Fazer / Opção A local-documental, sem runtime
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: Nenhum
- Riscos/bloqueios: Se Honcho degradar health/workspace/peer/watchdog, Memory OS volta a action_required
- Rollback/mitigação: Reverter patches locais nos quatro scripts e na política/AGENTS; rerodar py_compile, watchdogs e secret scan
- Próximos passos: Manter silent-OK; alertar Lucas só se Honcho deixar de cumprir checks governados
- Onde foi documentado no Brain: areas/operacoes/receipts/memory-os-honcho-provider-governed-20260621.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
