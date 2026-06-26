# Receipt — LK stock Notion purchase per-size correction

- Data/hora: 2026-06-14T23:49:41.306385+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Stock
- Responsável humano: Lucas Cimino
- Pedido original: Registrar e corrigir regra Lucas: compra no Notion sempre uma compra/card por modelo x tamanho; quantidade pode unificar por tamanho
- Classificação: external-write
- Fontes usadas:
- Correção explícita Lucas no Telegram; skill lk-stock reference stock-sales-notion-purchase-button-pattern-20260614.md; dashboard source
- O que foi feito:
- Atualizei skill/reference com a regra; ajustei endpoint POST /api/vendas/notion/adicionar-compra para dividir grade em payloads por tamanho e deduplicar por modelo/SKU+tamanho+quantidade; UI mostra quantidade criada; produção redeployada
- Output/artefato:
- Dashboard commit 4579d94; imagem sales-notion-per-size-20260614T234831Z; botão continua protegido; future clicks criam um card Notion por modelo x tamanho em vez de um card com grade combinada
- Aprovação: Aprovação/correção explícita atual de Lucas no Telegram: 'sempre deve ser uma compra por tamanho x modelo, a quantidade pode unificar'. Escopo: corrigir padrão e implementação do botão Notion; não autoriza compra, reserva, contato fornecedor, Tiny write ou Shopify write.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: Capacidade Notion write permanece atrás de botão autenticado; nenhum page teste criado automaticamente nesta correção; Tiny/Shopify/customer writes 0
- Riscos/bloqueios: Se houver clique real, o endpoint pode criar múltiplos cards; mitigado por regra correta one_purchase_per_model_size_quantity_unified, dedupe per-size e Basic Auth
- Rollback/mitigação: Reverter commit 4579d94 e redeploy da imagem anterior lk-estoque-web-rollback-sales-notion-per-size-20260614t234831z se necessário
- Próximos passos: Usar botão normalmente; cada tamanho vira uma Compra separada no Notion com quantidade unificada
- Onde foi documentado no Brain: areas/lk/sub-areas/stock/receipts/lk-stock-dashboard-notion-per-size-correction-20260614T234923Z.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
