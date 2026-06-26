# Receipt — Kanban dispatcher direct readiness integration

- Data/hora: 2026-06-25T19:55:10.689916+00:00
- Agente/profile/cron: default
- Empresa/área: Hermes Task OS / Kanban dispatcher
- Responsável humano: Hermes
- Pedido original: Lucas pediu integrar diretamente os guards no Task OS/dispatcher e perguntou se isso era relacionado ao Task OS.
- Classificação: local-write
- Fontes usadas:
- hermes_cli/kanban_db.py; tests/hermes_cli/test_kanban_db.py; scripts handoff guards; runtime process validation; Kanban diagnostics; Brain health.
- O que foi feito:
- Patchado dispatch_once para worker_readiness_fn e _default_worker_readiness_preflight; readiness failure agora bloqueia antes de spawn; testes adicionados; runtime site-packages patchado; dispatchers LK com dispatch_in_gateway=true reiniciados e validados.
- Output/artefato:
- reports/governance/kanban-dispatcher-direct-readiness-integration-2026-06-25.md; /opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages/hermes_cli/kanban_db.py; /opt/hermes/tests/hermes_cli/test_kanban_db.py
- Aprovação: Lucas: vamos integrar DIRETAMENTE.
- Envio/publicação: Resumo final no Telegram.
- Writes externos: 0
- Riscos/bloqueios: Main/default não foi self-restarted neste turno; patch em disco fica ativo para Main no próximo restart seguro. LK dispatchers relevantes foram reiniciados.
- Rollback/mitigação: Restaurar backups em /opt/data/backups/kanban-dispatcher-readiness-integration-20260625T194726Z/ e reiniciar gateways afetados se necessário.
- Próximos passos: Opcional: restart seguro do Main/default para ativar também o dispatcher Main, quando Lucas quiser/sem risco de interromper a conversa.
- Onde foi documentado no Brain: Sim: report governance, receipt e referência de skill kanban-orchestrator.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
