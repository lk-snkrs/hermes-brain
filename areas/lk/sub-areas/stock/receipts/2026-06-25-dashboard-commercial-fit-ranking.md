# Receipt — Dashboard Stock OS ranking por fit comercial LK

- Data/hora: 2026-06-25T17:24:37.796833+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Stock OS / UI
- Responsável humano: lk-stock
- Pedido original: Lucas corrigiu que a ordem dos produtos não fazia sentido e que Crocs McQueen não deve ser prioridade.
- Classificação: external-write
- Fontes usadas:
- Mensagem de Lucas; API /api/estoque/detail em container; código dashboard-utils.js/index.html/testes; npm test; Impeccable detect; smoke container.
- O que foi feito:
- Corrigido compareActionNeeded para ordenar por fit comercial/action class antes de score técnico. Adicionado isCoreLkAssortment/commercialFitRank, tratamento de Crocs/Havaianas/Rhode/acessórios/apparel/kids como non-core para compra, e distinção de MONITOR_OR_REORDER de reposição real. P3 sem demanda não entra mais em Ação necessária salvo estoque negativo.
- Output/artefato:
- Commit c36cfd3 em feat/stock-os-api-adapter; container lk-estoque-web atualizado e reiniciado. Antes Crocs McQueen abria em #1; após deploy, /api/estoque/detail quickFilter=action-needed retorna Crocs nas posições 15 e 16; top 1-2 viraram Yuto Horigome Nike SB e adidas Handball Spezial. npm test 40/40; Impeccable [].
- Aprovação: Pedido direto de Lucas para corrigir a ordem/prioridade no dashboard. Escopo UI/ranking read-only; sem Tiny/Shopify/Notion/customer write.
- Envio/publicação: Telegram final para Lucas
- Writes externos: GitHub branch feat/stock-os-api-adapter push; container lk-estoque-web /app/src/public atualizado e reiniciado. Tiny write 0; Shopify write 0; Notion write 0; contato externo 0.
- Riscos/bloqueios: Ranking usa heurística de fit comercial e pode precisar de refinamento fino por estratégia de compra; mitigado com teste de regressão Crocs McQueen e aliases/rotas preservados.
- Rollback/mitigação: Backup local .hermes/backups/commercial-fit-ranking-20260625T171853Z; backup container /opt/data/profiles/lk-stock/backups/lk-estoque-web-commercial-fit-ranking-20260625T172330Z; rollback via git revert c36cfd3.
- Próximos passos: Se Lucas quiser, refinar a matriz de fit comercial por marca/categoria com pesos explícitos.
- Onde foi documentado no Brain: Skill lk-stock atualizada com Commercial-fit ranking rule.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
