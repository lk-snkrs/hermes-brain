# Receipt — LK POS alert HQ2050-001 Stock OS miss fix

- Data/hora: 2026-06-16T21:55:23.733304+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK Sneakers / Stock OS / POS alerts
- Responsável humano: Hermes lk-stock
- Pedido original: Corrigir alerta POS #147835 que mostrou HQ2050-001-5 como não encontrado no LK Stock OS.
- Classificação: local-write
- Fontes usadas:
- Stock OS DB local; crosswalk live read-only Shopify↔Tiny por prefixo HQ2050-001; Tiny depósito LK | CONTROLE ESTOQUE; pytest; readback do alerta.
- O que foi feito:
- Produto novo HQ2050-001 não estava na superfície current_local_stock. Rodei fallback live read-only, encontrei 15 variantes com match exato Shopify↔Tiny sem duplicidades e promovi para DB/pointer local.
- Output/artefato:
- SKU HQ2050-001-5 tamanho 38 agora resolve: estoque 0 un. no LK Stock OS local; alerta #147835 renderiza Estoque atual: 0 un. (LK Stock OS local) e mantém pergunta de reposição.
- Aprovação: Correção local/read-only solicitada por Lucas; sem write Tiny/Shopify/cliente.
- Envio/publicação: Resposta Telegram.
- Writes externos: 0
- Riscos/bloqueios: Saldo 0 após venda indica reposição pode fazer sentido; promessa pública segue bloqueada pelo guardrail padrão.
- Rollback/mitigação: Reapontar lk_stock_os_current_pointer.json e gate_b2_current_pointer.json para DB anterior lk_stock_os_current_internal_consult_overlay_20260616T_INTERNAL_CONSULT_FIX.db.
- Próximos passos: Monitorar se outros produtos novos caem em miss; aplicar mesmo fallback/promote local e depois avaliar sync de catálogo se recorrente.
- Onde foi documentado no Brain: Skill lk-stock atualizada com padrão POS miss -> live read-only crosswalk -> promoção local.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
