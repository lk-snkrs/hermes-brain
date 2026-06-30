# Receipt — Stock Cockpit real Supabase deterministic correction

- Data/hora: 2026-06-29T16:31:46.184424+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK Sneakers / Stock / Inventory Hub
- Responsável humano: Hermes LK Stock
- Pedido original: Lucas pediu correção real dos blocos 1 a 4 e aprovou política Supabase/read-model determinístico: backup + corrigir somente casos reversíveis sem mexer em Tiny/Shopify.
- Classificação: external-write
- Fontes usadas:
- Stock OS DB/Supabase latest snapshot 20260626T092006Z; Tiny read-only exact SKU readback para negativos; broker Supabase psql; values_printed=false.
- O que foi feito:
- Criado backup Supabase das tabelas latest snapshot; aplicado update determinístico em lk_stock_items: 172 stale Tiny exact readback resolvidos, 99 tamanho único inferidos por léxico de produto one-size, 1 negativo corrigido por readback Tiny atual exato DN1555-200-2=0, 212 parent/base ajustados para NO_ACTION/fora de disponibilidade. Nenhum Tiny/Shopify write.
- Output/artefato:
- Antes health bruto 418 técnicos, 29 negativos, 104 SKU/tamanho ausente, 215 parent/base. Depois: 251 técnicos, 28 negativos, 5 SKU/tamanho ausente, 215 parent/base; fila Erro técnico/saneamento 497 itens: Negativo 28, SKU/tamanho ausente 5, Problema técnico acionável 249, Parent/base não vendável 215. Readback Supabase: items 8550, duplicate_business_rows 0, MR530SG sentinel ok, guardrails tiny_write=0 shopify_write=0 public_availability_promise=0.
- Aprovação: APROVADO por Lucas via Telegram: Supabase/read-model determinístico: backup + corrigir somente casos reversíveis sem mexer em Tiny/Shopify.
- Envio/publicação: Nenhum envio externo; write Supabase production read model aprovado.
- Writes externos: Supabase public.lk_stock_items update + backup tables public.lk_stock_items_backup_20260629_real_correction e public.lk_stock_snapshots_backup_20260629_real_correction.
- Riscos/bloqueios: Correção real limitada ao read model; 28 negativos ainda dependem de Tiny/contagem física, 5 SKU/tamanho ausente permanecem por não serem determinísticos, 249 técnicos permanecem por missing/duplicate/deposit/Shopify-Tiny identity, e 215 parent/base são não-vendáveis esperados. Futuro sync pode sobrescrever se origem upstream reintroduzir dados; backup existe.
- Rollback/mitigação: Restaurar latest snapshot 20260626T092006Z a partir de lk_stock_items_backup_20260629_real_correction e lk_stock_snapshots_backup_20260629_real_correction; depois rodar readback-only e health.
- Próximos passos: Deploy opcional do commit 8f0fe03 para melhor fila visual; próxima correção real exige pacote Tiny negativos ou Shopify/Tiny cadastro por SKU.
- Onde foi documentado no Brain: Approval packet em areas/lk/sub-areas/stock/approval-packets/2026-06-29-stock-cockpit-real-data-correction-policy.md; SQL aplicado arquivado em reports/stock-cockpit-issue-fix-20260629/sql/; relatório pós-correção em post_supabase_deterministic_fix.json.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
