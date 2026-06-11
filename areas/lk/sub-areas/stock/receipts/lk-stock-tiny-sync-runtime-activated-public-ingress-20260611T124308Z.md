# Receipt — LK Stock Tiny Sync runtime ativado com ingress público Vercel

- Data/hora: 2026-06-11T12:44:25.366196+00:00
- Agente/profile/cron: [LK] Estoque Loja Física / lk-stock
- Empresa/área: LK Sneakers / Estoque Loja Física / Stock OS
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas pediu concluir próximos passos: limpar package-lock, criar receipt, atualizar PRD e configurar URL Tiny/Olist do webhook Tiny Stock.
- Classificação: infra-sensitive
- Fontes usadas:
- Deploy/probes Vercel hermes-webhooks; Hermes Gateway local; SQLite runtime /opt/data/hermes_bruno_ingest/local_sql/lk_stock_tiny_sync/runtime.db; unittest Stock OS; cron registry Hermes; PRD Stock OS.
- O que foi feito:
- Removido package-lock.json transitório sem dependências no repo hermes-webhooks; ingress público Vercel já deployado e validado; secret de rota alinhado sem expor valores; probes negativo/válido executados; readback SQLite confirmou snapshots TEST-TINY-PUBLIC-HMAC-40 e TEST-TINY-PUBLIC-QUERY-40; cron registry verificado; PRD atualizado nesta rodada.
- Output/artefato:
- Rota pública operacional: https://hermes-webhooks.lucascimino.com/webhooks/lk-stock/tiny/stock?secret=[REDACTED] Rota processa Tiny stock snapshot em modo local/read-only, sem Tiny/Shopify writes e sem liberar promessa pública de disponibilidade.
- Aprovação: Aprovação escopada de Lucas no Telegram: 'FAZER OS PROXIMOS PASSOS' incluindo configurar no Tiny/Olist a URL.
- Envio/publicação: Telegram final para Lucas; nenhuma mensagem cliente/fornecedor/campanha.
- Writes externos: Vercel env/deploy previamente executado; Tiny/Olist pendente se não houver ferramenta/UI/API segura disponível nesta sessão; Tiny write 0; Shopify write 0; cliente/fornecedor 0.
- Riscos/bloqueios: URL Tiny/Olist depende de configuração na UI da integração Tiny/Olist (Configurações > E-commerce > Integrações > integração > Webhook > URL de notificações do estoque). Não imprimir secrets. DB local é cache/read model; Tiny LK | CONTROLE ESTOQUE segue fonte de verdade. Trace externo delivery_id Tiny ainda não é preservado 1:1 no source_event_id do snapshot.
- Rollback/mitigação: Remover/limpar URL de notificações do estoque na integração Tiny/Olist; remover/rotacionar LK_STOCK_TINY_WEBHOOK_SECRET e LK_STOCK_HERMES_ROUTE_SECRET no Vercel/Doppler; redeploy hermes-webhooks; desabilitar rota lk-stock-tiny-stock no Gateway se necessário; manter DB local como evidência sem usar para promessa pública.
- Próximos passos: Confirmar configuração Tiny/Olist na UI se ferramenta automatizada não estiver disponível; depois disparar evento real ou teste autorizado e verificar ledger/readback.
- Onde foi documentado no Brain: areas/lk/sub-areas/stock/PRD.md; areas/lk/sub-areas/stock/receipts/lk-stock-tiny-sync-runtime-activated-public-ingress-20260611T124308Z.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
