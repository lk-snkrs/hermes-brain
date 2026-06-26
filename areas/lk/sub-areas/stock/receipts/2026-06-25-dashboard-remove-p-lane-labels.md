# Receipt — Dashboard Stock OS sem labels P0/P1/P2

- Data/hora: 2026-06-25T17:10:53.274307+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Stock OS / UI
- Responsável humano: lk-stock
- Pedido original: Lucas disse que não concorda com a lógica P0/P1/P2 e que ela não faz sentido para o dashboard.
- Classificação: external-write
- Fontes usadas:
- Mensagem de Lucas com screenshot; código src/public/index.html, src/index.js, test/app.test.js; npm test; Impeccable detect; smoke container.
- O que foi feito:
- Removida linguagem P0/P1/P2 da UI operacional: filtros e cards agora mostram Comprar/repor, Corrigir cadastro e Monitorar contexto. Ledger e Ação necessária passaram a usar rotuloAcaoEstoque/detalheAcaoEstoque. Criadas rotas humanas /estoque/repor, /estoque/cadastro e /estoque/monitorar, mantendo /estoque/p0/p1/p2 apenas como aliases técnicos.
- Output/artefato:
- Commit 1a7c1cf em feat/stock-os-api-adapter; produção/container lk-estoque-web atualizado e reiniciado; /estoque/acoes, /estoque/repor, /estoque/cadastro, /estoque/monitorar, /vendas e /reposicao HTTP 200; smoke confirmou human=true e badVisibleP=false; npm test 39/39; Impeccable [].
- Aprovação: Pedido direto de Lucas para corrigir lógica visual do dashboard. Escopo: UI/rotas/read-only dashboard; sem Tiny/Shopify/Notion/customer write.
- Envio/publicação: Telegram final para Lucas
- Writes externos: GitHub branch feat/stock-os-api-adapter push; container lk-estoque-web /app/src atualizado e reiniciado. Tiny write 0; Shopify write 0; Notion write 0; contato externo 0.
- Riscos/bloqueios: Mudança de linguagem pode preservar campos técnicos internos para compatibilidade; mitigado traduzindo na UI e mantendo aliases antigos ocultos.
- Rollback/mitigação: Backup local .hermes/backups/remove-p-lanes-from-ui-20260625T170847Z e backup container /opt/data/profiles/lk-stock/backups/lk-estoque-web-remove-p-lanes-ui-20260625T170935Z; rollback via git revert 1a7c1cf.
- Próximos passos: Se Lucas quiser, próximo passo é revisar a lógica de ordenação de compra/reposição além da linguagem visual.
- Onde foi documentado no Brain: Skill lk-stock atualizada com Operational action labels rule.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
