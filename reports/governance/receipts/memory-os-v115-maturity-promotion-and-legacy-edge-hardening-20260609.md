# Receipt — Memory OS v1.15 — alerta único de mature e hardening de legados ambíguos

- Data/hora: 2026-06-09T20:10:35.263402+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: Hermes / Memory OS / Brain Governance
- Responsável humano: Lucas Cimino
- Pedido original: Lucas disse seguir após v1.14; continuar sem falsificar ciclos e fechar hardening seguro restante
- Classificação: local-write
- Fontes usadas:
- reports/governance/memory-os-v115-maturity-promotion-and-legacy-edge-hardening-20260609.md
- reports/memory-hygiene/cycle-maturity-latest.json
- O que foi feito:
- Adicionado alerta único de promoção mature no wrapper de 30min
- Persistido state anti-repetição em cycle-maturity-alert-state.json
- Endurecido script JSON receipt via event hook unknown
- Endurecido Markdown report receipt fora de receipts via writer register-existing
- Output/artefato:
- v1.15 local concluído; pilot/OK permanece silencioso; mature avisará uma vez quando 21/21 ciclos reais ocorrerem
- Aprovação: Lucas: Seguir
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: nenhum
- Riscos/bloqueios: Sem risco externo; escopo local/documental.
- Rollback/mitigação: Reverter patches v1.15 nos três scripts alterados e remover report/receipt v1.15; nenhum externo/prod foi alterado
- Próximos passos: Observar próximos ciclos e evoluir somente por escopo aprovado.
- Onde foi documentado no Brain: reports/governance/memory-os-v115-maturity-promotion-and-legacy-edge-hardening-20260609.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
