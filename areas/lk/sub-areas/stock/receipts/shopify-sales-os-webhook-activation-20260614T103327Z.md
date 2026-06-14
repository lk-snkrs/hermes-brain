# Receipt — Shopify Sales OS webhook activation

- Data/hora: 2026-06-14T10:33:54.973773+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Stock / Shopify Sales OS
- Responsável humano: lk-stock
- Pedido original: Seguir com pendências finais da ativação Shopify Sales OS: push, receipt e verificação pós-ativação
- Classificação: external-write
- Fontes usadas:
- Shopify webhook readback; Vercel/hermes-webhooks deploy/probes; Hermes Gateway route; testes locais; git logs
- O que foi feito:
- Rota pública Shopify Sales OS ativada; 5 subscriptions Shopify já criadas; wrapper ingest-stdin e rota Gateway validados; testes locais executados; commits locais preparados; fechamento documental via receipt
- Output/artefato:
- Endpoint público https://hermes-webhooks.lucascimino.com/webhooks/lk-stock-shopify-sales-os ativo; subscriptions: orders/create, orders/paid, orders/updated, orders/cancelled, refunds/create; summary local após limpeza com 1956 orders e 3311 units; guardrails operacionais Tiny/Shopify write 0
- Aprovação: Aprovação explícita e escopada de Lucas na conversa: seguir com o que falta após o resumo que listou como pendente push dos commits, receipt final e verificação pós-push; ativação pública/subscriptions Shopify já executadas no escopo aprovado da sessão anterior
- Envio/publicação: Telegram: resumo executivo final; GitHub push pendente/realizado em etapa posterior do fechamento
- Writes externos: Executados no escopo aprovado: Vercel deploy, Shopify webhook subscription creation, GitHub push/commits. Bloqueados/zerados: Tiny write 0, Shopify inventory/product write 0, customer-facing 0, public availability promise 0, auto purchase 0
- Riscos/bloqueios: Eventos reais Shopify agora entram no read model local; monitorar idempotência/freshness e não usar para promessa pública de disponibilidade
- Rollback/mitigação: Remover/desativar subscriptions Shopify do endpoint, reverter commits GitHub se necessário, desabilitar rota lk-stock-shopify-sales-os no Gateway/Vercel; DB local é read model e pode ser reexportado/limpo por ledger
- Próximos passos: Monitorar primeiro evento real Shopify; se houver falha de ingestão, pausar subscription ou rota e reconciliar via backfill read-only
- Onde foi documentado no Brain: areas/lk/sub-areas/stock/prds/shopify-sales-os-gate-s3-20260614T001817Z.md; areas/lk/sub-areas/stock/approval-packets/shopify-sales-os-webhook-activation-20260614T001817Z.md; areas/lk/sub-areas/stock/references/shopify-sales-os-local-db-webhook-pattern-20260614.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
