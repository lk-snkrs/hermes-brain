# Receipt — Shopify archive zero-stock selected 1 2 3 4 6 7 8 9

- Data/hora: 2026-06-19T19:09:29.490327+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Shopify + Stock
- Responsável humano: Hermes lk-stock
- Pedido original: Arquivar somente os itens 1,2,3,4,6,7,8,9 do último lote de 10 produtos seguros; manter 5 e 10 ativos; enviar próximos 10 candidatos.
- Classificação: external-write
- Fontes usadas:
- Shopify Admin GraphQL productUpdate/readback; Stock OS DB local tiny_full_sync 2026-06-19; approval-packet identity-safe 20260619
- O que foi feito:
- Backup local criado; productUpdate(status: ARCHIVED) executado somente em 8 product IDs selecionados; readback confirmou os 8 ARCHIVED e os 2 não selecionados ainda ACTIVE.
- Output/artefato:
- changed_count=8; skipped_count=0; error_count=0; all_selected_verified_archived=true; all_not_selected_verified_active=true; report=/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/approval-packets/shopify-archive-zero-stock-selected-1-2-3-4-5-9-report-20260619T190837Z.json
- Aprovação: Lucas no Telegram: "arquivar 1 2 3 4 6 7 8 9" — aprovação escopada para status Shopify ARCHIVED somente nesses índices do lote imediatamente anterior.
- Envio/publicação: Telegram DM: resumo, confirmação dos não selecionados e próximos 10 candidatos.
- Writes externos: Shopify productUpdate status=ARCHIVED em 8 produtos; Tiny write 0; price/stock/SKU/title/tag/collection/theme/campaign write 0.
- Riscos/bloqueios: Rollback depende de reativar via productUpdate(status: ACTIVE) a partir do backup; itens 5 e 10 foram preservados ativos por não estarem no escopo.
- Rollback/mitigação: /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/approval-packets/shopify-archive-zero-stock-selected-1-2-3-4-5-9-backup-20260619T190837Z.json contém before.status e IDs para productUpdate(status: ACTIVE).
- Próximos passos: Se Lucas aprovar, arquivar outro subconjunto ou novo lote de 10 com backup/readback.
- Onde foi documentado no Brain: /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/approval-packets/shopify-archive-zero-stock-selected-1-2-3-4-5-9-report-20260619T190837Z.json
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
