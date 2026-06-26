# Runtime Truth Reconciler — 2026-05-28

Timestamp UTC: 2026-05-28T11:20:20Z

## Escopo

Reconciliação read-only entre evidência viva de crons Hermes e documentação do Hermes Brain.

## Fonte viva usada

- Comando solicitado: `cronjob list`.
- Resultado neste runtime: comando `cronjob` não encontrado no PATH; usado fallback canônico `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all` a partir de `/opt/data/hermes_bruno_ingest/hermes-brain`.
- Nenhum cron foi executado manualmente.

## Resumo da evidência viva

- Total de jobs listados: 21.
- Ativos: 21.
- Pausados/disabled listados: 0.
- `last_status` não-ok: 1.
- Erros explícitos de delivery: 0 na listagem atual.
- Jobs ativos sem `Last run` ainda: 0.

## Anomalias de `last_status`

1. `Hermes Brain Operating Layer structural watchdog` — ativo, `local`, script `brain_operating_layer_audit.py`, último status `error: Script exited with code 1`.
   - Saída resumida: auto-heal criou `memories/daily/2026-05-28.md`, mas o audit ainda encontrou `memories/hot.md stale >3 days`.
   - Interpretação: gap de higiene/memória operacional; não é erro de delivery.

## Delivery observado

- `origin` observado sem erro explícito:
  - `Mesa COO diária Telegram`.
  - `Relatório Hermes diário 23h + 02h para Lucas`.
  - `Hermes multi-profile latency watchdog`.
- `local` confirmado para os watchdogs de gateway, Fechamento 23h, Runtime Truth Reconciler, Operating Layer, strict-runtime guard, relatórios LK listados e rotinas script-only listadas.

## Gaps / drift documental acionável

1. `Hermes Brain Operating Layer structural watchdog` está ativo, mas o último run falhou por `memories/hot.md` stale; precisa de follow-up de higiene de memória/hot context.
2. Seções antigas de `areas/operacoes/inventarios/crons-agentes-profiles.md` ainda descrevem alguns watchdogs/relatórios como `origin` em narrativas históricas; a evidência viva de 2026-05-28 confirma `local` para LK Daily Sales Brief, LK Weekly CEO Review, Mordomo gateway, LK Growth gateway, SPITI gateway, Runtime+Cron watchdog, Compression self-heal, Operating Layer, Runtime Truth Reconciler e strict-runtime guard.
3. Contagem viva permanece `21 ativos / 0 pausados` em relação ao snapshot de 2026-05-27, mas agora existe 1 status não-ok; o inventário foi atualizado com seção datada sem alterar seções históricas.

## O que não foi alterado

- Nenhum schedule, delivery, prompt, script, profile, Docker/gateway, VPS, Traefik, container, rede, sistema externo, campanha, Shopify, GMC, Notion, WhatsApp, email ou secret foi alterado.
- Nenhum segredo foi impresso ou versionado neste relatório.

## Verificação

- Brain health check: `python3 scripts/brain_health_check.py --json reports/brain-health-check-2026-05-28-runtime-truth-reconciler.json` — `All checks passed` (`FAIL=0 / WARN=0`).
- Secret scan escopado aos arquivos tocados: `scoped_possible_secrets 0`.
- `git diff --check` escopado aos arquivos tocados: sem saída / sem erros.
