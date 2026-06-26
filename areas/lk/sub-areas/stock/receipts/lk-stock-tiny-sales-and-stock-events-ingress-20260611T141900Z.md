# Receipt — LK Stock Tiny vendas + lançamentos de estoque ingress

- Data/hora: 2026-06-11T14:19:31.344893+00:00
- Agente/profile/cron: [LK] Estoque Loja Física / lk-stock
- Empresa/área: LK Sneakers / Estoque Loja Física / Stock OS
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas corrigiu o escopo: Stock OS precisa receber vendas e lançamentos de estoque para reconciliar saída/baixa e entrada/ajuste.
- Classificação: infra-sensitive
- Fontes usadas:
- Docs oficiais Tiny/Olist Webhooks do Tiny; Vercel hermes-webhooks; Hermes Gateway webhook_subscriptions; probes públicos route lk-stock-tiny-events; SQLite runtime local.
- O que foi feito:
- Criado processor local lk_stock_tiny_events_processor.py para classificar payload Tiny/Olist de vendas/pedidos e estoque; adicionada rota dinâmica lk-stock-tiny-events event tiny_webhook; ajustado Vercel para route lk-stock-tiny-events enviar x-github-event tiny_webhook; deploy Vercel produção realizado; chmod executável corrigido; probes públicos válidos para inclusao_pedido e estoque retornaram HTTP 200.
- Output/artefato:
- URL canônica para Tiny/Olist vendas + lançamentos de estoque: https://hermes-webhooks.lucascimino.com/webhooks/lk-stock/tiny/events?secret=[REDACTED] Venda é registrada como tiny_order_event com stock_decrement_executed=0; estoque é registrado como tiny_stock_snapshot. Nenhum write externo de Tiny/Shopify.
- Aprovação: Aprovação/correção escopada de Lucas no Telegram: precisamos saber vendas e estoque para baixa/reconciliação e lançamento de entrada.
- Envio/publicação: Telegram final para Lucas; nenhuma mensagem cliente/fornecedor/campanha.
- Writes externos: Vercel deploy/proxy update e rota Gateway local; Tiny/Olist UI ainda será salva manualmente por Lucas; Tiny write 0; Shopify write 0; cliente/fornecedor 0.
- Riscos/bloqueios: Tiny/Olist UI pode ter campos separados URL da notificação de pedidos e URL de notificações do estoque; usar a mesma URL canônica events com secret nos dois. Baixa de estoque não é executada pelo Stock OS; Tiny continua fonte de verdade e Stock OS apenas registra/reconcilia.
- Rollback/mitigação: No painel Tiny/Olist desligar vendas e lançamentos de estoque ou remover URLs; remover lk-stock-tiny-events de webhook_subscriptions; redeploy Vercel revertendo x-github-event tiny_webhook; manter receipts/ledger como evidência local.
- Próximos passos: Lucas colar a URL canônica com secret real nos campos/integrações de vendas e lançamentos de estoque, salvar, depois avisar para readback em logs/SQLite.
- Onde foi documentado no Brain: areas/lk/sub-areas/stock/PRD.md; areas/lk/sub-areas/stock/receipts/lk-stock-tiny-sales-and-stock-events-ingress-20260611T141900Z.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
