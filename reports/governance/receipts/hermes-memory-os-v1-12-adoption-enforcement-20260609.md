# Receipt — Hermes Memory OS v1.12 — enforcement de receipt_writer

- Data/hora: 2026-06-09T18:13:05.724184+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: Operações / Hermes Memory OS
- Responsável humano: Lucas Cimino
- Pedido original: Corrigir drifts hook-only atuais e impedir recorrência em receipts novos
- Classificação: local-write
- Fontes usadas:
- reports/memory-hygiene/adoption-latest.json
- /opt/data/scripts/hermes_memory_os_receipt_writer.py
- /opt/data/scripts/hermes_memory_os_event_hook.py
- O que foi feito:
- Registrados receipts existentes com drift via receipt_writer --register-existing sem sobrescrever conteúdo
- Hook v1.12 passou a tratar receipt novo hook-only como enforcement attention
- Protocolos e AGENTS LK/LKGOC atualizados para writer obrigatório
- Output/artefato:
- adoption gap_count 0 após correção dos drifts correntes
- enforcement local anti-recorrência ativo para hook-only receipt
- Aprovação: Lucas pediu corrigir drifts e implementar enforcement anti-recorrência; escopo local/documental/silent
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: nenhum
- Riscos/bloqueios: Sem risco externo; escopo local/documental.
- Rollback/mitigação: Reverter patches em writer/hook/protocolos/AGENTS e remover registros writer v1.12 se necessário; rerodar adoption_linter
- Próximos passos: Observar próximos ciclos e evoluir somente por escopo aprovado.
- Onde foi documentado no Brain: Skill hermes-brain-governance reference Memory OS v1.12; protocolos receipt/handoff; AGENTS LK e LKGOC
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
