# Receipt — Shopify archive zero-stock selected 8 9 10 with nonselected denylist

- Data/hora: 2026-06-19T20:06:34.947590+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Shopify / Stock cleanup
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas aprovou arquivar índices 8, 9 e 10 do último lote exibido e corrigiu que os outros itens acima já haviam sido recusados/não eram para arquivar.
- Classificação: external-write
- Fontes usadas:
- CSV do lote: areas/lk/sub-areas/shopify/approval-packets/shopify-active-zero-sales-360d-confirmed-zero-stock-next10-after-selected-3-4-6-10-archive-20260619T200147Z.csv; Stock OS/Tiny sync auditado por SKU; Shopify Admin GraphQL readback.
- O que foi feito:
- Arquivados via Shopify productUpdate(status: ARCHIVED) somente os índices 8, 9 e 10. Índices 1 a 7 foram preservados ACTIVE e registrados como denylist para não reofereir nesta rodada.
- Output/artefato:
- Backup: areas/lk/sub-areas/shopify/approval-packets/shopify-archive-zero-stock-selected-8-9-10-backup-20260619T200612Z.json; Report: areas/lk/sub-areas/shopify/approval-packets/shopify-archive-zero-stock-selected-8-9-10-report-deny-unselected-20260619T200612Z.json; Próximo CSV: areas/lk/sub-areas/shopify/approval-packets/shopify-active-zero-sales-360d-confirmed-zero-stock-next10-after-selected-8-9-10-archive-deny-unselected-20260619T200612Z.csv.
- Aprovação: Aprovação escopada no Telegram: arquivar 8 9 10; correção operacional: os outros acima não eram para arquivar.
- Envio/publicação: Resposta Telegram com resultado, reconhecimento da correção e próximos candidatos já sem os recusados.
- Writes externos: Shopify product status ARCHIVED: 3 produtos. Tiny write 0; inventory/price/SKU/title/tag/collection/theme/campaign/customer-contact 0.
- Riscos/bloqueios: Rollback disponível por backup: retornar selected products para ACTIVE se Lucas pedir. Itens 1 a 7 do lote foram preservados ACTIVE e excluídos dos próximos candidatos.
- Rollback/mitigação: Usar backup JSON e executar productUpdate(status: ACTIVE) nos produtos selecionados que estavam ACTIVE antes do run.
- Próximos passos: Continuar a limpeza apenas com candidatos novos, excluindo rejeitados da rodada.
- Onde foi documentado no Brain: Report, backup e next CSV em approval-packets; receipt canônico em areas/lk/sub-areas/shopify/receipts/.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
