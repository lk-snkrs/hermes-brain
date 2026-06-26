# Receipt — Shopify archive zero-stock selected 1 2 unseen 203730

- Data/hora: 2026-06-19T20:38:56.627397+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Shopify / Stock cleanup
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas aprovou arquivar índices 1 e 2 do lote inédito 20260619T203730Z de produtos ACTIVE, 360+ dias sem venda paga e saldo zero confirmado.
- Classificação: external-write
- Fontes usadas:
- CSV do lote: areas/lk/sub-areas/shopify/approval-packets/shopify-active-zero-sales-360d-confirmed-zero-stock-next10-unseen-after-user-correction-20260619T203730Z.csv; Stock OS/Tiny sync auditado por SKU; Shopify Admin GraphQL readback.
- O que foi feito:
- Arquivados via Shopify productUpdate(status: ARCHIVED) os 2 produtos selecionados. Backup criado antes da mutação; readback confirmou selecionados ARCHIVED e não selecionados preservados ACTIVE. Próximos foram regenerados com denylist de lotes já exibidos.
- Output/artefato:
- Backup: areas/lk/sub-areas/shopify/approval-packets/shopify-archive-zero-stock-selected-1-2-unseen-203730-backup-20260619T203830Z.json; Report: areas/lk/sub-areas/shopify/approval-packets/shopify-archive-zero-stock-selected-1-2-unseen-203730-report-20260619T203830Z.json; Próximo CSV inédito: areas/lk/sub-areas/shopify/approval-packets/shopify-active-zero-sales-360d-confirmed-zero-stock-next10-unseen-after-user-correction-20260619T203841Z.csv.
- Aprovação: Aprovação escopada no Telegram: arquivar 1 e 2.
- Envio/publicação: Resposta Telegram com resultado e próximos candidatos inéditos.
- Writes externos: Shopify product status ARCHIVED: 2 produtos. Tiny write 0; inventory/price/SKU/title/tag/collection/theme/campaign/customer-contact 0.
- Riscos/bloqueios: Rollback disponível por backup: retornar selected products para ACTIVE se Lucas pedir. Itens não selecionados do lote foram preservados ACTIVE.
- Rollback/mitigação: Usar backup JSON e executar productUpdate(status: ACTIVE) nos produtos selecionados que estavam ACTIVE antes do run.
- Próximos passos: Lucas pode escolher índices do próximo lote inédito exibido para continuar a limpeza.
- Onde foi documentado no Brain: Report, backup e next CSV em approval-packets; receipt canônico em areas/lk/sub-areas/shopify/receipts/.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
