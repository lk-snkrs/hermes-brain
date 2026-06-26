# Receipt — LK Stock local identity alias — Meia Saint Studio Pima Branco

- Data/hora: 2026-06-12T00:56:19.239035+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK Sneakers / Stock OS
- Responsável humano: Lucas Cimino
- Pedido original: Corrigir a database local do Stock OS para registrar e consultar estoque de produto sem SKU/chave operacional: Meia Saint Studio Pima Branco.
- Classificação: local-write
- Fontes usadas:
- Stock OS DB local, Tiny API read-only produtos.pesquisa/produto.obter.estoque, lk_stock_os_query.py.
- O que foi feito:
- Criada nova DB local apontada por lk_stock_os_current_pointer.json com alias SHOPIFYVAR-48283857780958 ligando Shopify product/variant/inventory/GMC metadata ao Tiny id 1071195617 e saldo 1.0 no depósito LK | CONTROLE ESTOQUE; patch no lookup para buscar tiny_id_candidates e data_quality_gap.
- Output/artefato:
- DB: areas/lk/sub-areas/stock/data/lk_stock_os_current_local_identity_aliases_20260612T005354Z.db; JSON/CSV/packet de alias; PRD atualizado; consulta por variant id/handle/Tiny id retorna 1 linha; 30 tests OK.
- Aprovação: Aprovação explícita de Lucas para corrigir nossa database local; sem aprovação para Tiny/Shopify write.
- Envio/publicação: Nenhum envio externo.
- Writes externos: 0
- Riscos/bloqueios: Alias é consultável internamente por fallback de título; identidade operacional definitiva ainda deve ser saneada com SKU/código/metafield em fluxo separado.
- Rollback/mitigação: Restaurar pointer artifacts.sqlite_db para a DB anterior lk_stock_os_current_variant_promotion_20260611T023437Z.db e remover/ignorar artefatos de alias local.
- Próximos passos: Generalizar fallback título→Tiny para outros produtos sem SKU e manter guardrails public_availability_safe=0/availability_claim_allowed=0.
- Onde foi documentado no Brain: areas/lk/sub-areas/stock/PRD.md; areas/lk/sub-areas/stock/reports/lk-stock-local-identity-alias-meia-saint-studio-pima-branco-20260612T005354Z.json; areas/lk/sub-areas/stock/approval-packets/lk-stock-local-identity-alias-meia-saint-studio-pima-branco-20260612T005354Z.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
