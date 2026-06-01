# Runtime Truth Reconciler — 2026-05-31

Timestamp UTC: 2026-05-31T11:20:43Z
Timestamp BRT: 2026-05-31T08:20:43-0300

## Escopo

Reconciliação read-only entre evidência viva de crons Hermes e documentação do Hermes Brain.

## Fonte viva usada

- Comando solicitado: `cronjob list`.
- Resultado neste runtime: `cronjob` não encontrado no PATH.
- Fallback canônico usado com sucesso: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.
- Nenhum cron foi executado manualmente; evidência read-only apenas.

## Resumo da evidência viva

- Total de jobs listados: **27**.
- Ativos: **23**.
- Pausados/disabled: **4**.
- `last_status` não-ok: **1**.
- Erros explícitos de delivery: **0**.
- Jobs sem `Last run` ainda: **1**.
- Jobs com `deliver=origin`: **4**.

## Inventário completo — 2026-05-31

| id | Nome | Schedule | Deliver | Estado | Último status |
|----|------|----------|---------|--------|---------------|
| f5a23dd6a1bd | Lucas Brain daily intelligence loop | 0 5 * * * | local | active | ok (2026-05-31T05:05) |
| edd06fe19397 | Hermes runtime + cron watchdog no_agent | */30 * * * * | local | active | ok (2026-05-31T11:00) |
| 7c688553e293 | LK Daily Sales Brief read-only mandatory delivery | 0 11 * * * | local | active | ok (2026-05-31T11:01) |
| 953b9055458e | LK Weekly CEO Review read-only mandatory delivery | 0 12 * * 1 | local | active | ok (2026-05-25T12:01) |
| 71b147362ec1 | Zipper Gmail style learning refresh | 20 6 * * * | local | active | ok (2026-05-31T06:21) |
| 4bb4e2223fd3 | Hermes compression failure self-heal watchdog | */10 * * * * | local | active | ok (2026-05-31T11:10) |
| c3bb587519d2 | LK Pulso Comercial 16h read-only delivery | 0 19 * * * | local | active | ok (2026-05-30T19:00) |
| e3279babbc4a | LK 09h previous-day sales report external delivery | 0 12 * * * | local | active | ok (2026-05-30T12:00) |
| a2ead305eab2 | LK 19h30 physical store close external delivery | 30 22 * * * | local | active | ok (2026-05-30T22:30) |
| ac0b440e2643 | Mordomo Telegram gateway watchdog | every 1m | local | **paused** | ok (2026-05-30T15:52) |
| 357d40a5863e | Zipper OS vendas 09h WhatsApp/email | 0 12 * * 1-5 | local | active | ok (2026-05-29T12:00) |
| 876d54c62ccd | LK Growth Telegram gateway watchdog | every 1m | local | **paused** | ok (2026-05-30T15:52) |
| 749ee30b51eb | Mesa COO diária Telegram | 0 9 * * * | **origin** | active | ok (2026-05-31T09:01) |
| 663e3e6a148c | SPITI Telegram gateway watchdog | every 1m | local | **paused** | ok (2026-05-30T15:52) |
| 3fc45b0830c6 | Hermes Brain Fechamento Ágil 23h + Brain Sync | 0 2 * * * | local | active | ok (2026-05-31T02:06) |
| f4c499e85eac | Lucas Brain weekly Learning Loop report | 15 12 * * 1 | local | active | ok (2026-05-25T12:20) |
| d03fa04e1188 | Hermes Brain Operating Layer structural watchdog | 10 11 * * * | local | active | ok (2026-05-31T11:10) |
| 2404c0766d33 | Hermes Brain Runtime Truth Reconciler | 20 11 * * * | local | active | ok (2026-05-30T11:23) |
| 98478b820720 | Relatório Hermes diário 23h + 02h para Lucas | 30 5 * * * | **origin** | active | ok (2026-05-31T05:32) |
| d9badcd83411 | Hermes Brain strict-runtime guard watchdog | 0 10 * * * | local | active | ok (2026-05-31T10:00) |
| c1ce34b4449a | Hermes multi-profile latency watchdog | every 15m | **origin** | active | ok (2026-05-31T11:15) |
| 787134d4ac5c | LK Weekly Collection Sort Rule B | 0 9 * * 5 | local | active | **error: Script timed out after 120s** (2026-05-29T06:02) |
| a1d1e36f8075 | LK Weekly Catalog Badges BEST SELLER sync | 30 9 * * 5 | local | active | sem last run |
| 5bacaa61bb12 | claude-proxy-watchdog | every 5m | local | active | ok (2026-05-31T11:17) |
| 3cd1011edf33 | claude-max-proxy watchdog | every 5m | local | active | ok (2026-05-31T11:17) |
| 955dc769b5a6 | LK specialist Telegram gateway watchdog | every 1m | **origin** | **paused** | ok (2026-05-30T15:52) |
| b78ae7ac81d0 | Hermes all Telegram gateways watchdog | every 1m | **origin** | active | ok (2026-05-31T11:19) |

## Gaps e drifts acionáveis

1. **Timeout persistente:** `787134d4ac5c` — `LK Weekly Collection Sort Rule B` segue com `last_status=error` por timeout de 120s desde 2026-05-29. Próximo run: 2026-06-05T09:00Z. Ação recomendada: revisar duração/timeout/implementação do script em uma frente própria; nada foi alterado neste run.
2. **Watchdogs de profiles pausados:** `Mordomo Telegram gateway watchdog`, `LK Growth Telegram gateway watchdog`, `SPITI Telegram gateway watchdog` e `LK specialist Telegram gateway watchdog` aparecem pausados na evidência viva. Isso precisa ser reconciliado com a documentação que ainda descreve alguns desses profiles como ativos/monitorados.
3. **Novos watchdogs/runtime a documentar:** `claude-proxy-watchdog`, `claude-max-proxy watchdog` e `Hermes all Telegram gateways watchdog` estão ativos na evidência viva e devem ser incorporados ao inventário documental de runtime/profiles.
4. **Catalog Badges sem primeira execução:** `LK Weekly Catalog Badges BEST SELLER sync` está ativo, mas ainda sem `Last run`; aguardando primeira execução em 2026-06-05T09:30Z.
5. **`deliver=origin` em watchdog:** `LK specialist Telegram gateway watchdog` está pausado mas configurado como `origin`; se reativado, validar se a entrega em Telegram é realmente desejada ou se deve seguir silent-OK/local.

## Saídas intencionais `deliver=origin`

Confirmados na evidência viva:

- `Mesa COO diária Telegram` (`749ee30b51eb`) — ok.
- `Relatório Hermes diário 23h + 02h para Lucas` (`98478b820720`) — ok.
- `Hermes multi-profile latency watchdog` (`c1ce34b4449a`) — ok; alerta condicional.
- `Hermes all Telegram gateways watchdog` (`b78ae7ac81d0`) — ok; alerta condicional.

## O que não foi alterado

- Nenhum schedule, delivery, prompt, script, profile, Docker/gateway, VPS, Traefik, container, rede, sistema externo, campanha, Shopify, GMC, Notion, WhatsApp, email ou secret foi alterado.
- Nenhum segredo foi impresso ou versionado neste relatório.
- Este relatório é read-only / documental.

## Verificação

- Brain health check: `python3 scripts/brain_health_check.py --json reports/brain-health-check-2026-05-31-runtime-truth-reconciler.json` — **All checks passed** (`FAIL=0`, `WARN=0`).
- Secret scan dos arquivos tocados: **possible_secrets 0**.
- `git diff --check` nos arquivos tocados: sem problemas.
