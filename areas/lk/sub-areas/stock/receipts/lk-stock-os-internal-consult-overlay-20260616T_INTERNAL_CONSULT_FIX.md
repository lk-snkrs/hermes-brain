# Receipt — LK Stock OS internal consult overlay — redução de bloqueios consultáveis

- Data/hora: 2026-06-16T18:18:37.479756+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Estoque Loja Física
- Responsável humano: Hermes lk-stock
- Pedido original: Corrigir bloqueios/não resolvidos da Stock OS DB para identificar quantidade em estoque quando possível sem write Tiny/Shopify.
- Classificação: local-write
- Fontes usadas:
- Stock OS pointer atual; SQLite lk_stock_os_current_tiny_full_sync_20260616T082014Z.db; Tiny read-only produto.obter.estoque para 218 SKUs com Tiny exato único; full_live_match_decisions; testes locais.
- O que foi feito:
- Criado overlay local/read-only lk_stock_os_internal_consult_overlay.py; promovidas 218 linhas com Tiny exato único para consulta interna de quantidade; classificadas 255 linhas parent/base como não-variante de estoque; pointer atualizado para nova DB; guardrails públicos preservados.
- Output/artefato:
- Bloqueios não consultáveis caíram de 652 para 179; local_consult_safe 3567/3746; public_availability_safe=0; availability_claim_allowed=0; writes externos=0.
- Aprovação: Não exigiu aprovação externa: local/read-only/cache. Tiny/Shopify/Notion/cliente não foram alterados.
- Envio/publicação: Resposta no Telegram após verificação.
- Writes externos: 0
- Riscos/bloqueios: Ainda restam 179 linhas bloqueadas por duplicidade Tiny, duplicidade Shopify sem Tiny exato único ou Tiny missing; identidade não resolvida permanece explicitamente identity_resolved_safe=0 em 718 linhas.
- Rollback/mitigação: Voltar pointer artifacts.sqlite_db para /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_tiny_full_sync_20260616T082014Z.db; nova DB é cópia overlay local.
- Próximos passos: Resolver remanescentes por lane: 100 Tiny duplicate, 64 Shopify duplicate sem Tiny único, 15 Tiny missing; sem write externo salvo aprovação escopada.
- Onde foi documentado no Brain: Script, report JSON/CSV/MD, pointer e receipt em areas/lk/sub-areas/stock/.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
