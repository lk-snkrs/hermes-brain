# Receipt — LK POS 147843 Stock OS miss live crosswalk promotion

- Data/hora: 2026-06-17T15:48:58.487436+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK Sneakers / Stock OS / POS alerts
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas apontou novo erro: alerta POS #147843 item JR0035-3 apareceu como não encontrado pelo LK Stock OS.
- Classificação: local-write
- Fontes usadas:
- Shopify Sales OS local DB para POS #147843; Stock OS full catalog DB; crosswalk live read-only Shopify↔Tiny para JR0035, DL4081684 e NUD-7601374; Tiny depósito LK | CONTROLE ESTOQUE.
- O que foi feito:
- Confirmei miss no lookup estável, rodei fallback live read-only e auditei todos os 3 itens do pedido #147843. Promovi 26 variantes resolvidas para nova DB local/pointers e reconstrui canonical_current/FTS.
- Output/artefato:
- Itens vendidos agora consultáveis: JR0035-3 estoque 3; DL4081684-3 estoque 0; NUD-7601374-S estoque 1. POS de hoje após correção: 3 linhas, misses 0, não consultáveis 0. Teste alerta POS 17 passed.
- Aprovação: Correção local/read-only a partir de bug apontado por Lucas; sem write externo.
- Envio/publicação: Resposta Telegram.
- Writes externos: 0
- Riscos/bloqueios: Um SKU NUD do prefixo ficou Tiny missing fora dos itens vendidos; promessa pública continua bloqueada; full sync/full catalog não cobre SKU criado/vendido após snapshot até nova promoção/sync.
- Rollback/mitigação: Reapontar lk_stock_os_current_pointer.json/gate_b2_current_pointer.json para lk_stock_os_current_full_live_match_tiny_stock_20260617T105109Z_FULLCATALOG.db.
- Próximos passos: Transformar esta correção em rotina automática/worker de pós-alerta POS se Lucas aprovar reduzir misses sem intervenção manual.
- Onde foi documentado no Brain: Skill lk-stock atualizada: auditar todos os itens do mesmo pedido POS e considerar janela pós-snapshot.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
