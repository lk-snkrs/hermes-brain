# Receipt — Tiny negative stock nine SKUs zeroed and read model synced

- Data/hora: 2026-06-29T18:09:13.648861+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK Sneakers / Stock / Tiny / Inventory Hub
- Responsável humano: Hermes LK Stock
- Pedido original: Lucas aprovou: APROVO Tiny estoque: zerar no Tiny somente os 9 SKUs exatos do pacote tiny_negative_correction_packet.json, usando lk-tiny estoque balanco com readback antes/depois, sem Shopify write e sem outros SKUs.
- Classificação: external-write
- Fontes usadas:
- Pacote tiny_negative_correction_packet.json; Tiny readback antes/depois via TINY_API_TOKEN/Doppler; lk-tiny estoque balanco wrapper governado; Supabase read model via psql/Doppler; Stock Cockpit model health; values_printed=false.
- O que foi feito:
- Executado Tiny write tipo B quantidade 0 no depósito LK | CONTROLE ESTOQUE para os 9 SKUs exatos aprovados; corrigido wrapper para enviar parametro estoque como JSON após tentativa inicial com XML retornar erro Tiny sem alteração; readback pós-write confirmou controle=0 nos 9; atualizado read model Supabase apenas para esses 9 SKUs com backup.
- Output/artefato:
- Tiny: 9/9 SKUs ok_zeroed por readback; Shopify write 0; outros SKUs 0. Supabase backup lk_stock_items_backup_20260629_tiny_negative_zero com 9 linhas; Supabase update 9 linhas. Health pós-sync: negativeRows 19, missingSkuOrSize 5, technicalIssues 251, parentBaseAnomalies 215, totalHealthSignals 490; queue Erro técnico/saneamento 488. Supabase readback-only ok: items 8550, duplicate_business_rows 0, MR530SG sentinel ok.
- Aprovação: APROVADO por Lucas via Telegram: zerar no Tiny somente os 9 SKUs exatos do pacote tiny_negative_correction_packet.json, usando lk-tiny estoque balanco com readback antes/depois, sem Shopify write e sem outros SKUs.
- Envio/publicação: Nenhum envio externo a cliente/canal.
- Writes externos: Tiny produto.atualizar.estoque.php para 9 SKUs aprovados; Supabase public.lk_stock_items para os mesmos 9 SKUs; Shopify write 0.
- Riscos/bloqueios: Tiny balanço tipo B altera fonte real de estoque; readback confirmou controle=0. Restam 19 negativos bloqueados por falta de match exato/correção de cadastro, 5 SKU/tamanho ausente e 249 técnicos. Alguns SKUs têm saldo total maior por reservado/outros depósitos; a correção foi apenas depósito LK | CONTROLE ESTOQUE.
- Rollback/mitigação: Para rollback Tiny, usar tiny_negative_apply_result_20260629.json para restaurar controle anterior por SKU via lk-tiny estoque balanco; para Supabase, restaurar os 9 registros de lk_stock_items_backup_20260629_tiny_negative_zero e revalidar health/readback.
- Próximos passos: Tratar os 19 negativos restantes como pacote cadastro/Tiny no-match; opcional deploy do Cockpit 8f0fe03 para visualização melhor da fila.
- Onde foi documentado no Brain: Resultados em tiny_negative_apply_result_20260629.json, tiny_negative_post_write_readback_20260629.json, post_tiny_negative_zero_health_20260629.json e SQL supabase_update_after_tiny_negative_zero_20260629.sql; skill lk-stock atualizada com o pitfall JSON vs XML do Tiny.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
