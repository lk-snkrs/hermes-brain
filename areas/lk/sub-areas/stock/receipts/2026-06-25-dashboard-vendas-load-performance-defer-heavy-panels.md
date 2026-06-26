# Receipt — Performance /vendas — painéis pesados sob demanda

- Data/hora: 2026-06-26T00:17:11.996718+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Stock OS / Vendas
- Responsável humano: Hermes LK Stock
- Pedido original: Lucas perguntou se o load do Dashboard demorar é normal e se dá para melhorar.
- Classificação: external-write
- Fontes usadas:
- Medição produção container lk-estoque-web: /vendas 29ms, summary 13ms, health 142ms, time-summary 2ms, executive-summary 3983ms, lista-julio/alerts/saneamento timeout 15015ms; código commit 87cbbcf.
- O que foi feito:
- Identificado que o load percebido era impactado por endpoints pesados disparados automaticamente. Alterado /vendas para auto-carregar apenas analytics e Shopify Sales OS leves no bloco secundário; Lista Júlio, alertas e saneamento passaram para botões sob demanda. Testes adicionados para impedir regressão.
- Output/artefato:
- Commit 87cbbcf Defer heavy sales dashboard panels; GitHub feat/stock-os-api-adapter local=remote; npm test 41/41; Impeccable []; validação HTML auto_loads_julio=false auto_loads_alerts=false auto_loads_sanitation=false.
- Aprovação: Sem deploy/restart em produção nesta etapa; aguardando aprovação escopada de Lucas para aplicar no container.
- Envio/publicação: Código pushado para GitHub; produção ainda não alterada.
- Writes externos: GitHub push do branch feat/stock-os-api-adapter; Tiny write 0; Shopify write 0; Notion write 0; Docker restart 0; compra automática 0; contato externo 0.
- Riscos/bloqueios: Sem alteração produtiva ainda. Próximo passo de deploy exige backup, docker cp src/. e restart limitado a lk-estoque-web.
- Rollback/mitigação: Reverter commit 87cbbcf antes do deploy ou restaurar backup de container caso deploy seja aprovado posteriormente.
- Próximos passos: Se Lucas aprovar, aplicar no container lk-estoque-web com backup e smoke autenticado.
- Onde foi documentado no Brain: Skill lk-stock reference stock-sales-vendas-five-rounds-pattern-20260625.md atualizada com regra de endpoints pesados sob demanda.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
