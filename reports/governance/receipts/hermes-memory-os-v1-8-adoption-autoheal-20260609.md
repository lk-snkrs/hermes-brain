# Receipt — Operações — Hermes Memory OS v1.8 adoption auto-heal — 2026-06-09

- Data/hora: 2026-06-09T15:23:53.412947+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: Operações / Hermes Memory OS
- Responsável humano: Lucas Cimino
- Pedido original: Lucas disse seguir após v1.7 para adicionar auto-heal local limitado de gaps vencidos.
- Classificação: local-write
- Fontes usadas:
- Memory OS v1.7 verde
- hermes_memory_os_daytime_checker.py
- hermes_memory_os_adoption_linter.py
- O que foi feito:
- Adicionado auto-heal local limitado no checker diurno com --adoption-auto-heal-limit default 5.
- Auto-heal roda o hook em gaps pós-graça sem ler ou despejar conteúdo dos artefatos.
- Adicionada supressão HERMES_MEMORY_OS_SUPPRESS_ADOPTION_AUTOHEAL para evitar recursão hook-checker-autoheal.
- Checker reroda o linter depois das tentativas e só fica verde se gap_count=0.
- Teste sintético confirmou attempted=1, healed=1, gap_count=0, routes=[] e stdout final vazio.
- Output/artefato:
- /opt/data/scripts/hermes_memory_os_daytime_checker.py
- reports/memory-hygiene/daytime-latest.json
- reports/governance/receipts/hermes-memory-os-v1-8-autoheal-test-20260609.md
- reports/governance/receipts/hermes-memory-os-v1-8-adoption-autoheal-20260609.md
- Aprovação: Escopo local/documental autorizado por seguir; sem novo cron, sem runtime sensível.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: nenhum
- Riscos/bloqueios: Sem risco externo; escopo local/documental.
- Rollback/mitigação: Definir --adoption-auto-heal-limit 0 ou reverter função auto_heal_adoption_gaps no checker.
- Próximos passos: Observar próximos ciclos e evoluir somente por escopo aprovado.
- Onde foi documentado no Brain: areas/operacoes/prds/hermes-memory-os-v1-prd-2026-06-09.md; areas/operacoes/rotinas/hermes-memory-os-v1.md; areas/operacoes/runtime/hermes-memory-os-dashboard.md; memories/hot.md; memories/daily/2026-06-09.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
