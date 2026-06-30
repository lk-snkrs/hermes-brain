# Receipt — Tiny negative remaining 19 SKUs zeroed and read model synced

- Data/hora: 2026-06-29T19:42:19.481517+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK Sneakers / Stock / Tiny / Inventory Hub
- Responsável humano: Hermes LK Stock
- Pedido original: Lucas aprovou: APROVO Tiny estoque: zerar no Tiny somente os 19 SKUs exatos do pacote negative_19_tiny_identity_classification_20260629.json, usando lk-tiny estoque balanco com readback antes/depois, sem Shopify write e sem outros SKUs.
- Classificação: external-write
- Fontes usadas:
- Pacote negative_19_tiny_identity_classification_20260629.json; Tiny produto.obter.estoque readback por tiny_id; lk-tiny estoque balanco wrapper governado; Supabase read model via psql/Doppler; Stock Cockpit model health; values_printed=false.
- O que foi feito:
- Executado Tiny write tipo B quantidade 0 no depósito LK | CONTROLE ESTOQUE para os 19 SKUs exatos aprovados; após falha de readback textual, foi usado readback direto por tiny_id/produto.obter.estoque para evitar falso bloqueio; todos os 19 terminaram com controle=0; atualizado read model Supabase apenas para esses 19 SKUs com backup.
- Output/artefato:
- Tiny: 19/19 final readback ok com controle=0; Tiny writes performed 19; Shopify write 0; outros SKUs 0. Supabase backup lk_stock_items_backup_20260629_tiny_negative_19_zero com 19 linhas; Supabase update 19 linhas. Health pós-sync: negativeRows 0, missingSkuOrSize 5, technicalIssues 251, parentBaseAnomalies 215, totalHealthSignals 471; queue saneamento 469. Supabase readback-only ok: items 8550, duplicate_business_rows 0, MR530SG sentinel ok.
- Aprovação: APROVADO por Lucas via Telegram: zerar no Tiny somente os 19 SKUs exatos do pacote negative_19_tiny_identity_classification_20260629.json, usando lk-tiny estoque balanco com readback antes/depois, sem Shopify write e sem outros SKUs.
- Envio/publicação: Nenhum envio externo a cliente/canal.
- Writes externos: Tiny produto.atualizar.estoque.php para 19 SKUs aprovados; Supabase public.lk_stock_items para os mesmos 19 SKUs; Shopify write 0.
- Riscos/bloqueios: Tiny balanço tipo B altera fonte real de estoque; readback confirmou controle=0. Alguns SKUs têm saldo total maior por reservado/outros depósitos; a correção foi apenas depósito LK | CONTROLE ESTOQUE. Restam 5 SKU/tamanho ausente e 249 problemas técnicos acionáveis, mas negativos ficaram zerados.
- Rollback/mitigação: Para rollback Tiny, usar negative_19_consolidated_final_readback_20260629.json e logs apply por SKU para restaurar controle anterior via lk-tiny estoque balanco; para Supabase, restaurar os 19 registros de lk_stock_items_backup_20260629_tiny_negative_19_zero e revalidar health/readback.
- Próximos passos: Tratar próximos blocos do Cockpit: 5 SKU/tamanho ausente, 249 problemas técnicos acionáveis e 215 parent/base não vendável; opcional deploy/validar Cockpit UI se ainda houver commit pendente.
- Onde foi documentado no Brain: Resultados em negative_19_consolidated_final_readback_20260629.json, negative_19_tiny_apply_result_by_id_20260629.json, negative_19_st45_final_write_readback_20260629.json, post_tiny_negative_19_zero_health_20260629.json e SQL supabase_update_after_tiny_negative_19_zero_20260629.sql.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
