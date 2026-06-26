# Receipt — Shopify archive zero-stock selected 3 4 6 10

- Data/hora: 2026-06-19T20:02:14.488839+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Shopify / Stock cleanup
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas aprovou arquivar índices 3, 4, 6 e 10 do último lote exibido de produtos ACTIVE, 360+ dias sem venda paga e saldo zero confirmado.
- Classificação: external-write
- Fontes usadas:
- CSV do lote: areas/lk/sub-areas/shopify/approval-packets/shopify-active-zero-sales-360d-confirmed-zero-stock-next10-after-selected-8-9-archive-20260619T195115Z.csv; Stock OS/Tiny sync auditado por SKU; Shopify Admin GraphQL readback.
- O que foi feito:
- Arquivados via Shopify productUpdate(status: ARCHIVED) somente os produtos dos índices 3, 4, 6 e 10. Backup criado antes da mutação; readback confirmou selecionados ARCHIVED e não selecionados do lote ACTIVE.
- Output/artefato:
- Backup: areas/lk/sub-areas/shopify/approval-packets/shopify-archive-zero-stock-selected-3-4-6-10-backup-20260619T200147Z.json; Report: areas/lk/sub-areas/shopify/approval-packets/shopify-archive-zero-stock-selected-3-4-6-10-report-20260619T200147Z.json; Próximo CSV: areas/lk/sub-areas/shopify/approval-packets/shopify-active-zero-sales-360d-confirmed-zero-stock-next10-after-selected-3-4-6-10-archive-20260619T200147Z.csv.
- Aprovação: Aprovação escopada no Telegram: arquivar 3 4 6 10.
- Envio/publicação: Resposta Telegram com resultado e próximos candidatos.
- Writes externos: Shopify product status ARCHIVED: 4 produtos. Tiny write 0; inventory/price/SKU/title/tag/collection/theme/campaign/customer-contact 0.
- Riscos/bloqueios: Rollback disponível por backup: retornar selected products para ACTIVE se Lucas pedir. Produtos não selecionados do lote foram preservados ACTIVE.
- Rollback/mitigação: Usar backup JSON e executar productUpdate(status: ACTIVE) nos produtos selecionados que estavam ACTIVE antes do run.
- Próximos passos: Lucas pode escolher índices do próximo lote exibido para continuar a limpeza.
- Onde foi documentado no Brain: Report, backup e next CSV em approval-packets; receipt canônico em areas/lk/sub-areas/shopify/receipts/.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
