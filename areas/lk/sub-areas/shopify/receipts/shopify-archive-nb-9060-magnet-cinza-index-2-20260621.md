# Receipt — Shopify archive NB 9060 Magnet Cinza index 2

- Data/hora: 2026-06-21T12:51:52.865205+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Shopify / Stock cleanup
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas respondeu "Arquivar 2" ao relatório de New Balance 9060/530 ativos online, 0 venda paga e saldo zero confirmado; índice 2 = Tênis New Balance 9060 Magnet Cinza.
- Classificação: external-write
- Fontes usadas:
- Shopify Admin live readback ACTIVE/online antes e ARCHIVED depois; Sales OS local paid non-cancelled units=0; Stock OS DB local / Tiny sync com 11 SKUs auditados e saldo total confirmado 0 observado em 2026-06-21T12:20:31Z.
- O que foi feito:
- Arquivado somente o produto Shopify gid://shopify/Product/9026107211998 / handle tenis-new-balance-9060-magnet-cinza via productUpdate(status: ARCHIVED).
- Output/artefato:
- Report: areas/lk/sub-areas/shopify/approval-packets/shopify-archive-single-nb-9060-magnet-cinza-index-2-report-20260621T125130Z.json; backup: areas/lk/sub-areas/shopify/approval-packets/shopify-archive-single-nb-9060-magnet-cinza-index-2-backup-20260621T125130Z.json.
- Aprovação: Aprovação escopada de Lucas no Telegram: Arquivar 2.
- Envio/publicação: Nenhum envio externo/customer-facing; somente write Shopify Product.status aprovado.
- Writes externos: Shopify product status ARCHIVED: 1; Tiny write 0; inventory/price/SKU/title/tag/collection/theme/campaign/customer contact 0.
- Riscos/bloqueios: Rollback possível com productUpdate(status: ACTIVE) para o mesmo product_id usando o backup; Shopify inventoryQuantity diverge visualmente, mas estoque truth usado foi Stock OS/Tiny sync conforme guardrail.
- Rollback/mitigação: Reverter gid://shopify/Product/9026107211998 para ACTIVE se Lucas pedir, usando backup JSON; nenhum outro campo foi alterado.
- Próximos passos: Nenhuma ação pendente; demais produtos do relatório não foram alterados.
- Onde foi documentado no Brain: Receipt canônico + report/backup JSON no Brain.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
