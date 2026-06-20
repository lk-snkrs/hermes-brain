# Receipt — Shopify archive zero-stock selected 2 3 4 unseen 201732 and Balenciaga discrepancy

- Data/hora: 2026-06-19T20:21:50.735364+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Shopify / Stock cleanup + Stock OS discrepancy
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas aprovou arquivar índices 2, 3 e 4 do lote inédito 20260619T201732Z e sinalizou que o produto Balenciaga BB0231S-005 Branco exibido no lote está errado porque existe estoque físico.
- Classificação: external-write
- Fontes usadas:
- CSV do lote: areas/lk/sub-areas/shopify/approval-packets/shopify-active-zero-sales-360d-confirmed-zero-stock-next10-unseen-after-user-correction-20260619T201732Z.csv; Stock OS/Tiny sync auditado por SKU; Shopify Admin GraphQL readback; crosswalk live read-only para BB0231S-005.
- O que foi feito:
- Arquivados via Shopify productUpdate(status: ARCHIVED) os índices 2, 3 e 4. Readback confirmou selecionados ARCHIVED e não selecionados preservados ACTIVE. Produto Balenciaga BB0231S-005 não foi arquivado; investigação read-only mostrou Tiny live e Stock OS com saldo 0 apesar do sinal humano de estoque físico, abrindo divergência operacional.
- Output/artefato:
- Backup: areas/lk/sub-areas/shopify/approval-packets/shopify-archive-zero-stock-selected-2-3-4-unseen-201732-backup-20260619T201920Z.json; Report: areas/lk/sub-areas/shopify/approval-packets/shopify-archive-zero-stock-selected-2-3-4-unseen-201732-report-20260619T201920Z.json; Próximo CSV inédito: areas/lk/sub-areas/shopify/approval-packets/shopify-active-zero-sales-360d-confirmed-zero-stock-next10-unseen-after-archive-2-3-4-and-stock-correction-20260619T202042Z.csv; Discrepancy report: areas/lk/sub-areas/stock/reports/balenciaga-bb0231s-005-stock-discrepancy-20260619T202100Z.json.
- Aprovação: Aprovação escopada no Telegram: arquivar 2 3 4. Investigação do produto com estoque físico foi read-only/local.
- Envio/publicação: Resposta Telegram com resultado, divergência e próximos candidatos.
- Writes externos: Shopify product status ARCHIVED: 3 produtos. Tiny write 0; inventory/price/SKU/title/tag/collection/theme/campaign/customer-contact 0.
- Riscos/bloqueios: Balenciaga BB0231S-005: físico informado por Lucas conflita com Tiny/Stock OS saldo 0; não arquivar nem prometer disponibilidade pública até reconciliar Tiny/físico/SKU.
- Rollback/mitigação: Usar backup JSON e executar productUpdate(status: ACTIVE) nos produtos selecionados que estavam ACTIVE antes do run.
- Próximos passos: Lucas pode escolher índices do próximo lote inédito. Para Balenciaga BB0231S-005, próximo passo é conferência física/Tiny: ajustar lançamento/depósito no Tiny ou identificar se a peça física está em outro SKU/código; qualquer Tiny/Shopify write exige aprovação separada.
- Onde foi documentado no Brain: Report, backup, next CSV, discrepancy report e receipt canônico no Brain.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
