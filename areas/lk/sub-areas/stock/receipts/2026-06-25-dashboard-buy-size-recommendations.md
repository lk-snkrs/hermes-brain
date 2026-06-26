# Receipt — Dashboard Stock OS mostra Comprar tamanhos no card

- Data/hora: 2026-06-25T18:56:09.395251+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Stock OS / UI
- Responsável humano: lk-stock
- Pedido original: Lucas pediu corrigir o card para mostrar explicitamente Comprar tamanhos: 34, 40 no exemplo U204LMMC, em vez de apenas recomendação por produto.
- Classificação: external-write
- Fontes usadas:
- Mensagem de Lucas; Stock OS API container; src/public/dashboard-utils.js; src/public/index.html; npm test; Impeccable; smoke container /estoque/acoes.
- O que foi feito:
- Implementado cálculo recommended_buy_sizes em groupStockCardProducts: usa variantes zeradas dentro da curva carregada e o tamanho imediatamente abaixo do menor tamanho positivo quando existe; renderiza pill buy-size-reco com Comprar tamanhos: lista. U204LMMC recomenda 34, 40, mantendo grade disponível 35/4 36/4 37/7 38/2 39/2 41/1.
- Output/artefato:
- Commit b7f16f1 em feat/stock-os-api-adapter; container lk-estoque-web atualizado. Smoke: cardStock=20, recommended='34, 40', htmlHasBuyText=true, htmlHasClass=true.
- Aprovação: Pedido direto de Lucas para corrigir UI do dashboard. Escopo read-only/UI.
- Envio/publicação: Telegram final para Lucas
- Writes externos: GitHub push na branch feat/stock-os-api-adapter; atualização de src/public/dashboard-utils.js e src/public/index.html no container lk-estoque-web e restart. Tiny write 0; Shopify write 0; Notion write 0; contato externo 0.
- Riscos/bloqueios: Não cria compra automática nem altera estoque real. A recomendação é visual/operacional, baseada em estoque zerado por tamanho e vendas ponderadas já disponíveis.
- Rollback/mitigação: Backup local .hermes/backups/buy-size-recommendations-20260625T185135Z; backup container /opt/data/profiles/lk-stock/backups/lk-estoque-web-buy-size-reco-20260625T185505Z; rollback via git revert b7f16f1.
- Próximos passos: Se necessário, evoluir regra de curva por modelo/gênero para tamanhos acima do maior tamanho carregado.
- Onde foi documentado no Brain: Skill lk-stock atualizada com regra recommended_buy_sizes e texto exato Comprar tamanhos: 34, 40.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
