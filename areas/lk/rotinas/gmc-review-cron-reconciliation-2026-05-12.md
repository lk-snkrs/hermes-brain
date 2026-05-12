# LK GMC Review Cron Reconciliation, 2026-05-12

## Contexto

Lucas apontou corretamente que, no PRD do LK Operating System, existe uma cadência-alvo separada para **GMC Review**:

- Quinta 09h BRT — GMC Review.

A Fase 8 havia consolidado Daily, Weekly, SEO/CRO e os guards manuais, mas não havia ativado a cadência separada do Google Merchant Center.

## Correção operacional

Foi criado um cron Hermes `no_agent` read-only para o GMC Review.

- Automation ID: `LK-AUTO-007`.
- Nome: `LK GMC Review read-only mandatory delivery`.
- Job ID: `d4c26da4cd48`.
- Cadência: quinta-feira 09:00 BRT.
- Schedule UTC: `0 12 * * 4`.
- Entrega: `origin`.
- Script runtime: `/opt/data/scripts/lk_gmc_review_watchdog.py`.
- Fonte Brain: `scripts/lk_merchant_center_feed_readonly_router_20260511.py`.

## Contrato de segurança

Permitido:

- Ler status de produtos no Merchant Center.
- Agrupar issues/feed/destinos reprovados.
- Entregar report interno no Telegram/origin.
- Gerar artefatos Brain de diagnóstico.

Bloqueado sem aprovação separada:

- Merchant/feed write.
- Supplemental feed update.
- Shopify write.
- GSC admin/Indexing API.
- Conteúdo público.
- Campanha/envio.
- n8n.

## Teste manual

O watchdog foi executado manualmente antes do cron:

- Produtos/status lidos: 5000.
- Itens na fila P1/P2: 963.
- P1: 963.
- P2: 0.
- Produtos com issue: 963.
- Produtos com destino reprovado: 708.
- Cruzamentos com GSC: 1.
- Writes liberados agora: 0.

## Impacto na Fase 8

O completion audit da Fase 8 foi atualizado:

- Automations tracked: 7.
- Active crons: 4.
- Mandatory deliveries: 3.
- Read-only preview crons: 1.
- Manual guards ready: 3.
- Fails: 0.
- Warnings: 0.
- n8n/writes/envios externos/compra/marketplace: 0.

## Rollback

Se precisar desligar:

1. `cronjob list`.
2. Pausar ou remover `d4c26da4cd48`.

Não há write produtivo para reverter.
