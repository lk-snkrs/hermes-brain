# Receipt — Vercel hermes-webhooks 504 fix

- Data/hora: 2026-06-27T17:38:10.726366+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: Operações Hermes / Webhooks
- Responsável humano: Lucas Cimino
- Pedido original: Corrigir alerta Vercel/Sentry de 504 timeouts em /api/webhooks/[route] e executar passos 1 a 6 aprovados por Lucas
- Classificação: infra-sensitive
- Fontes usadas:
- Vercel logs read-only; health checks públicos; gateway local logs; source code /opt/data/hermes-webhooks; webhook_subscriptions local; signed no-op probe
- O que foi feito:
- Backup criado; rota lk-shopify-tiny-stock-sync convertida para run_script determinístico; script adaptado para stdin/env; Vercel proxy recebeu AbortController upstream timeout; deploy produção realizado; probes e testes executados
- Output/artefato:
- Report: reports/governance/vercel-hermes-webhooks-504-fix-2026-06-27.md; deployment: hermes-webhooks-m3in2djwn-lk-snkrs-projects.vercel.app; signed probe HTTP 200 em 1.057s transport=hermes_run_script; Vercel 504 last 15m = 0
- Aprovação: Lucas aprovou explicitamente: Fazer do 1 ao 6
- Envio/publicação: Nenhuma mensagem externa; somente resposta Telegram ao Lucas
- Writes externos: Vercel production deploy aprovado; zero Shopify/Tiny/Klaviyo/customer writes
- Riscos/bloqueios: Mudança em webhook production mitigada por backup, probe assinado no-op, script_timeout 45s e rollback documentado
- Rollback/mitigação: Restaurar backup /opt/data/backups/hermes-webhooks-504-fix-20260627T173304Z para webhook_subscriptions.json, lk_shopify_tiny_stock_sync_dryrun.py e api/webhooks/[route].js; redeploy Vercel se necessário; verificar health/probe
- Próximos passos: Monitorar Vercel 5xx/504 por 24h; se aparecer upstream_timeout, investigar rota específica antes de ampliar mudanças
- Onde foi documentado no Brain: reports/governance/vercel-hermes-webhooks-504-fix-2026-06-27.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
