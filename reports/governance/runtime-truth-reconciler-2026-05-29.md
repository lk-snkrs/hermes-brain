# Runtime Truth Reconciler — 2026-05-29

Timestamp UTC: 2026-05-29T11:20:00Z

## Escopo

Reconciliação read-only entre evidência viva de crons Hermes e documentação do Hermes Brain.

## Fonte viva usada

- Comando solicitado: `cronjob list`.
- Resultado neste runtime: `cronjob` não encontrado no PATH.
- Fallback canônico usado com sucesso: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.
- Nenhum cron foi executado manualmente.

## Resumo da evidência viva

- Total de jobs listados: 19.
- Ativos: 19.
- Pausados/disabled listados: 0.
- `last_status` não-ok: 1.
- Erros explícitos de delivery: 0.
- Jobs ativos sem `Last run` ainda: 0.

## Anomalias / drift a reconciliar

1. `LK Weekly Collection Sort Rule B` (`787134d4ac5c`) — ativo, `local`, script `lk_weekly_collection_sort_ruleB.sh`; último run retornou `error: Script timed out after 120s: /opt/data/scripts/lk_weekly_collection_sort_ruleB.sh`.
   - Ação documental sugerida: revisar se o timeout é esperado, se o script deve ser otimizado ou se precisa de nova janela/estratégia de execução.

2. Jobs com `deliver=origin` ainda observados como saídas/executivos, não como sucesso silencioso:
   - `Mesa COO diária Telegram` (`749ee30b51eb`) — ok.
   - `Relatório Hermes diário 23h + 02h para Lucas` (`98478b820720`) — ok.
   - `Hermes multi-profile latency watchdog` (`c1ce34b4449a`) — ok.
   - Ação documental sugerida: manter esses itens explicitamente como entregas intencionais e não heurísticas de ruído.

3. Jobs históricos que não apareceram mais na listagem viva atual:
   - `Hermes Brain Operating Layer structural watchdog`.
   - `Hermes Brain strict-runtime guard watchdog`.
   - `Hermes Brain Runtime Truth Reconciler`.
   - Ação documental sugerida: tratar como removidos da evidência viva atual até nova prova.

## Cobertura confirmada na listagem viva atual

A listagem atual confirma `local` para os watchdogs/gateways/relatórios restantes, incluindo:

- LK Daily Sales Brief
- LK Weekly CEO Review
- Zipper Gmail style learning refresh
- Hermes compression failure self-heal watchdog
- LK Pulso Comercial 16h
- LK 09h previous-day sales report
- LK 19h30 physical store close
- Mordomo Telegram gateway watchdog
- Zipper OS vendas 09h WhatsApp/email
- LK Growth Telegram gateway watchdog
- SPITI Telegram gateway watchdog
- Hermes Brain Fechamento Ágil 23h + Brain Sync
- Lucas Brain weekly Learning Loop report

## O que não foi alterado

- Nenhum schedule, delivery, prompt, script, profile, Docker/gateway, VPS, Traefik, container, rede, sistema externo, campanha, Shopify, GMC, Notion, WhatsApp, email ou secret foi alterado.
- Nenhum segredo foi impresso ou versionado neste relatório.

## Verificação

- Brain health check: `python3 scripts/brain_health_check.py --json reports/brain-health-check-2026-05-29-runtime-truth-reconciler.json`
- Secret scan escopado aos arquivos tocados: `scoped_possible_secrets 0`
- `git diff --check` escopado aos arquivos tocados: sem saída / sem erros
