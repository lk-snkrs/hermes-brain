# Receipt — Shopify archive zero-stock selected 8 9

- Data/hora: 2026-06-19T19:52:03.885326+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Shopify / Stock
- Responsável humano: Hermes
- Pedido original: Lucas pediu no Telegram: arquivar 8 9 e sugerir outros, no lote atual de produtos ACTIVE, >=360d sem venda paga e saldo zero confirmado por SKU.
- Classificação: external-write
- Fontes usadas:
- CSV aprovado: areas/lk/sub-areas/shopify/approval-packets/shopify-active-zero-sales-360d-confirmed-zero-stock-next10-after-selected-10-2-archive-20260619T194430Z.csv; relatório runtime: areas/lk/sub-areas/shopify/approval-packets/shopify-archive-zero-stock-selected-8-9-report-20260619T195115Z.json; Shopify Admin GraphQL readback; Stock OS/Tiny sync para saldo zero por SKU
- O que foi feito:
- Arquivados via Shopify Admin productUpdate(status: ARCHIVED) os itens 8 e 9; readback confirmou 2/2 arquivados; 8 itens não selecionados permaneceram ACTIVE; próximo lote sugerido auditado com saldo 0 por SKU.
- Output/artefato:
- Backup: areas/lk/sub-areas/shopify/approval-packets/shopify-archive-zero-stock-selected-8-9-backup-20260619T195115Z.json; relatório: areas/lk/sub-areas/shopify/approval-packets/shopify-archive-zero-stock-selected-8-9-report-20260619T195115Z.json; próximo lote CSV: areas/lk/sub-areas/shopify/approval-packets/shopify-active-zero-sales-360d-confirmed-zero-stock-next10-after-selected-8-9-archive-20260619T195115Z.csv
- Aprovação: Aprovação explícita e escopada de Lucas no Telegram nesta conversa: 'arquivar 8 9 , sugerir outros'. Escopo limitado aos índices 8 e 9 do lote exibido imediatamente antes.
- Envio/publicação: Resposta no Telegram com confirmação e sugestões; nenhum contato cliente.
- Writes externos: Shopify Admin GraphQL: productUpdate status ARCHIVED em 2 produtos. Tiny write 0; preço/estoque/SKU/título/tag/coleção/tema/campanha 0.
- Riscos/bloqueios: Rollback disponível via productUpdate(status: ACTIVE) conforme backup; demais itens preservados ACTIVE.
- Rollback/mitigação: Usar backup JSON e aplicar productUpdate(status: ACTIVE) apenas nos produtos com before.status ACTIVE listados no backup.
- Próximos passos: Aguardar Lucas aprovar quais índices do novo lote sugerido devem ser arquivados; sem novo write até aprovação escopada.
- Onde foi documentado no Brain: Receipt criado pelo Memory OS writer; backup/relatório/CSV em approval-packets.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
