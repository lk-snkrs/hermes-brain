# Receipt — Dashboard Stock OS — remoção de KPIs vazios do topo

- Data/hora: 2026-06-25T19:31:20.735468+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Stock OS
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas pediu para tirar o bloco superior de métricas coloridas porque não estava preenchido e não fazia sentido operacional.
- Classificação: infra-sensitive
- Fontes usadas:
- Pedido do Lucas no Telegram com screenshot; repo /opt/data/worktrees/lk-stock/LK-Estoque-Web-inicial; container lk-estoque-web; testes npm/impeccable.
- O que foi feito:
- Removido container todayCommandMetrics, renderização JS e CSS command-metrics/command-card; hero Estoque hoje agora fica limpo com decision ledger. Commit bb90af0 enviado ao GitHub e hot patch aplicado no container lk-estoque-web com backup e restart.
- Output/artefato:
- npm test 41/41; npx impeccable detect retornou []; GitHub local=remote bb90af0; smoke container /estoque/hoje HTTP 200; HTML servido sem todayCommandMetrics/class command-metrics/Consulta interna segura/P0 para revisar primeiro e com todayDecisionLedger presente.
- Aprovação: Aprovação escopada no pedido do Lucas para tirar a parte indicada no screenshot; escopo limitado à UI do dashboard Stock OS.
- Envio/publicação: Telegram: resumo final nesta conversa.
- Writes externos: 0
- Riscos/bloqueios: Risco visual/infra baixo; container reiniciado; rollback disponível via backup do container e commit anterior.
- Rollback/mitigação: /opt/data/profiles/lk-stock/backups/lk-estoque-web-remove-empty-top-metrics-20260625T192921Z; git revert bb90af0 se necessário.
- Próximos passos: Nenhum obrigatório; acompanhar visualmente se Lucas quiser outra simplificação.
- Onde foi documentado no Brain: Skill lk-stock reference stock-dashboard-link-routes-weighted-ranking-toggle-lessons-20260625.md atualizada com regra para não exibir KPIs vazios/não populados na primeira dobra.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
