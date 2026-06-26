# Runtime Truth Reconciler — 2026-05-27

Data/hora da coleta: 2026-05-27 11:20 UTC  
Workdir: `/opt/data/hermes_bruno_ingest/hermes-brain`  
Fonte viva: tentativa de localizar `cronjob list` sem comando disponível no PATH; fallback canônico executado com sucesso: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

## Resumo executivo

- Jobs listados: 21.
- Ativos: 21.
- Pausados/disabled listados: 0.
- Delivery `local`: 18.
- Delivery `origin`: 3.
- `last_status` não-ok: 0.
- Jobs ativos sem `Last run`: 0.
- Erros explícitos de delivery na listagem: 0.

## Delivery `origin` observado

Estes jobs entregam em `origin`, sem erro explícito no snapshot:

1. `Mesa COO diária Telegram` — último run `ok` em 2026-05-27T09:01:26 UTC.
2. `Relatório Hermes diário 23h + 02h para Lucas` — último run `ok` em 2026-05-27T05:32:48 UTC.
3. `Hermes multi-profile latency watchdog` — último run `ok` em 2026-05-27T11:19:04 UTC; por ser watchdog de latência, `origin` deve ser tratado como canal de alerta/anomalia, não recibo de sucesso normal.

Nenhuma mudança de delivery foi feita nesta reconciliação.

## Drift / pontos de reconciliação documental

- A contagem viva subiu de `20 ativos / 0 pausados listados` no snapshot de 2026-05-26 para `21 ativos / 0 pausados listados` em 2026-05-27.
- Novo job observado na listagem viva: `Hermes multi-profile latency watchdog` (`hermes_profile_latency_watchdog.py`), ativo, `origin`, último status `ok`.
- Jobs presentes em seções antigas que não aparecem na listagem viva atual continuam históricos até nova evidência, incluindo jobs LK/GMC/WhatsApp regression mencionados em snapshots anteriores.
- Seções antigas do inventário ainda citam alguns watchdogs e relatórios como `origin`; a evidência viva atual confirma `local` para runtime+cron watchdog, compression self-heal, Mordomo gateway, LK Growth gateway, SPITI gateway, Operating Layer, Runtime Truth Reconciler e strict-runtime guard.
- Não há anomalia operacional imediata: todos os jobs listados têm último status `ok`, nenhum delivery error explícito e nenhum ativo sem primeira execução.

## Evidência resumida por job

- `Lucas Brain daily intelligence loop` — active, delivery `local`, último status `ok`.
- `Hermes runtime + cron watchdog no_agent` — active, delivery `local`, último status `ok`.
- `LK Daily Sales Brief read-only mandatory delivery` — active, delivery `local`, último status `ok`.
- `LK Weekly CEO Review read-only mandatory delivery` — active, delivery `local`, último status `ok`.
- `Zipper Gmail style learning refresh` — active, delivery `local`, último status `ok`.
- `Hermes compression failure self-heal watchdog` — active, delivery `local`, último status `ok`.
- `LK Pulso Comercial 16h read-only delivery` — active, delivery `local`, último status `ok`.
- `LK 09h previous-day sales report external delivery` — active, delivery `local`, último status `ok`.
- `LK 19h30 physical store close external delivery` — active, delivery `local`, último status `ok`.
- `Mordomo Telegram gateway watchdog` — active, delivery `local`, último status `ok`.
- `Zipper OS vendas 09h WhatsApp/email` — active, delivery `local`, último status `ok`.
- `LK Growth Telegram gateway watchdog` — active, delivery `local`, último status `ok`.
- `Mesa COO diária Telegram` — active, delivery `origin`, último status `ok`.
- `SPITI Telegram gateway watchdog` — active, delivery `local`, último status `ok`.
- `Hermes Brain Fechamento Ágil 23h + Brain Sync` — active, delivery `local`, último status `ok`.
- `Lucas Brain weekly Learning Loop report` — active, delivery `local`, último status `ok`.
- `Hermes Brain Operating Layer structural watchdog` — active, delivery `local`, último status `ok`.
- `Hermes Brain Runtime Truth Reconciler` — active, delivery `local`, último status `ok`.
- `Relatório Hermes diário 23h + 02h para Lucas` — active, delivery `origin`, último status `ok`.
- `Hermes Brain strict-runtime guard watchdog` — active, delivery `local`, último status `ok`.
- `Hermes multi-profile latency watchdog` — active, delivery `origin`, último status `ok`.

## O que não foi alterado

Nenhum schedule, prompt, delivery, script, profile, Docker/gateway, VPS, Traefik, container, rede, sistema externo, campanha, Shopify, GMC, Notion, WhatsApp, email, banco de dados ou secret foi alterado.

## Verificação

- Inventário atualizado: `areas/operacoes/inventarios/crons-agentes-profiles.md`.
- Health check executado: `python3 scripts/brain_health_check.py --json reports/brain-health-check-2026-05-27-runtime-truth-reconciler.json`.
- Resultado do health check: `FAIL=0 / WARN=0` (`All checks passed`).
- Secret scan escopado nos arquivos tocados: `scoped_possible_secrets 0`.
- `git diff --check` escopado aos arquivos tocados: sem saída, exit code 0.
