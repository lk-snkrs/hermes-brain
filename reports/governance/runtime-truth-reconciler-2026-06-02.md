# Runtime Truth Reconciler — 2026-06-02

Timestamp UTC: 2026-06-02T11:21:00Z
Timestamp BRT: 2026-06-02T08:21:00-0300

## Escopo

Reconciliação read-only entre evidência viva de crons Hermes e documentação do Hermes Brain.

## Fonte viva usada

- Comando solicitado: `cronjob list`.
- Resultado neste runtime: `cronjob` não encontrado no PATH (`command not found`).
- Fallback canônico usado com sucesso: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.
- Nenhum cron foi executado manualmente; evidência read-only apenas.

## Resumo da evidência viva

- Total de jobs listados: **29**.
- Ativos: **25**.
- Pausados/disabled: **4**.
- `last_status` não-ok: **5**.
- Erros explícitos de delivery do scheduler: **0** na listagem.
- Falhas de envio externo aprovadas registradas em stdout: **4**.
- Jobs ativos sem `Last run` ainda: **1**.
- Jobs com `deliver=origin`: **4 ativos + 1 pausado**.

## Inventário completo — 2026-06-02

| id | Nome | Schedule | Deliver | Estado | Último status |
|----|------|----------|---------|--------|---------------|
| f5a23dd6a1bd | Lucas Brain daily intelligence loop | 0 5 * * * | local | active | ok (2026-06-02T05:06) |
| edd06fe19397 | Hermes runtime + cron watchdog no_agent | */30 * * * * | local | active | ok (2026-06-02T11:00) |
| 7c688553e293 | LK Daily Sales Brief read-only mandatory delivery | 0 11 * * * | local | active | ok (2026-06-02T11:00) |
| 953b9055458e | LK Weekly CEO Review read-only mandatory delivery | 0 12 * * 1 | local | active | ok (2026-06-01T12:01) |
| 71b147362ec1 | Zipper Gmail style learning refresh | 20 6 * * * | local | active | ok (2026-06-02T06:21) |
| 4bb4e2223fd3 | Hermes compression failure self-heal watchdog | */10 * * * * | local | active | ok (2026-06-02T11:10) |
| c3bb587519d2 | LK Pulso Comercial 16h read-only delivery | 0 19 * * * | local | active | **error: wacli hermes not authenticated** (2026-06-01T19:00) |
| e3279babbc4a | LK 09h previous-day sales report external delivery | 0 12 * * * | local | active | **error: wacli hermes not authenticated** (2026-06-01T12:00) |
| a2ead305eab2 | LK 19h30 physical store close external delivery | 30 22 * * * | local | active | **error: wacli hermes not authenticated** (2026-06-01T22:30) |
| ac0b440e2643 | Mordomo Telegram gateway watchdog | every 1m | local | **paused** | ok (2026-05-30T15:52) |
| 357d40a5863e | Zipper OS vendas 09h WhatsApp/email | 0 12 * * 1-5 | local | active | **error: wacli account hermes not authenticated** (2026-06-01T12:00) |
| 876d54c62ccd | LK Growth Telegram gateway watchdog | every 1m | local | **paused** | ok (2026-05-30T15:52) |
| 749ee30b51eb | Mesa COO diária Telegram | 0 9 * * * | **origin** | active | ok (2026-06-02T09:00) |
| 663e3e6a148c | SPITI Telegram gateway watchdog | every 1m | local | **paused** | ok (2026-05-30T15:52) |
| 3fc45b0830c6 | Hermes Brain Fechamento Ágil 01h + Brain Sync | 0 4 * * * | local | active | ok (2026-06-02T02:07) |
| f4c499e85eac | Lucas Brain weekly Learning Loop report | 15 12 * * 1 | local | active | ok (2026-06-01T12:18) |
| d03fa04e1188 | Hermes Brain Operating Layer structural watchdog | 10 11 * * * | local | active | ok (2026-06-02T11:10) |
| 2404c0766d33 | Hermes Brain Runtime Truth Reconciler | 20 11 * * * | local | active | ok (2026-06-01T11:23) |
| 98478b820720 | Relatório Hermes diário 01h + 02h + 02h15 para Lucas | 30 5 * * * | **origin** | active | ok (2026-06-02T05:32) |
| d9badcd83411 | Hermes Brain strict-runtime guard watchdog | 0 10 * * * | local | active | ok (2026-06-02T10:00) |
| c1ce34b4449a | Hermes multi-profile latency watchdog | every 15m | **origin** | active | ok (2026-06-02T11:17) |
| 787134d4ac5c | LK Weekly Collection Sort Rule B | 0 9 * * 5 | local | active | **error: Script timed out after 120s** (2026-05-29T06:02) |
| a1d1e36f8075 | LK Weekly Catalog Badges BEST SELLER sync | 30 9 * * 5 | local | active | sem last run |
| 5bacaa61bb12 | claude-proxy-watchdog | every 5m | local | active | ok (2026-06-02T11:17) |
| 3cd1011edf33 | claude-max-proxy watchdog | every 5m | local | active | ok (2026-06-02T11:17) |
| 955dc769b5a6 | LK specialist Telegram gateway watchdog | every 1m | **origin** | **paused** | ok (2026-05-30T15:52) |
| b78ae7ac81d0 | Hermes all Telegram gateways watchdog | every 1m | **origin** | active | ok (2026-06-02T11:19) |
| c64a0c63b881 | LK Tiny stock local DB daily fullsync | 20 10 * * * | local | active | ok (2026-06-02T10:45) |
| f9a1d43caf48 | Hermes memory hygiene watchdog 02h15 BRT | 15 5 * * * | local | active | ok (2026-06-02T05:15) |

## Gaps e drifts acionáveis

1. **Falhas de envio externo por WACLI não autenticado:** quatro jobs ativos de entrega aprovada falharam no último run por autenticação WACLI ausente/expirada: LK Pulso 16h (`c3bb587519d2`), LK 09h (`e3279babbc4a`), LK 19h30 (`a2ead305eab2`) e Zipper Vendas 09h (`357d40a5863e`). Ação recomendada: frente própria de autenticação/validação WACLI; este reconciler não alterou contas, tokens ou env.
2. **Timeout persistente:** `787134d4ac5c` — `LK Weekly Collection Sort Rule B` segue com `last_status=error` por timeout de 120s desde 2026-05-29. Próximo run: 2026-06-05T09:00Z. Ação recomendada: revisar duração/timeout/implementação do script em frente própria.
3. **Watchdogs de profiles pausados:** `Mordomo Telegram gateway watchdog`, `LK Growth Telegram gateway watchdog`, `SPITI Telegram gateway watchdog` e `LK specialist Telegram gateway watchdog` continuam pausados na evidência viva. Reconciliar documentação que ainda trate esses watchdogs como ativos.
4. **Catalog Badges sem primeira execução:** `LK Weekly Catalog Badges BEST SELLER sync` está ativo, mas ainda sem `Last run`; aguardando primeira execução prevista em 2026-06-05T09:30Z.
5. **Novos jobs vs relatório anterior:** `LK Tiny stock local DB daily fullsync` (`c64a0c63b881`) e `Hermes memory hygiene watchdog 02h15 BRT` (`f9a1d43caf48`) aparecem na evidência viva e devem entrar na documentação operacional quando houver rodada própria.
6. **Drift nominal/schedule de documentação:** o Fechamento Ágil aparece agora como `Hermes Brain Fechamento Ágil 01h + Brain Sync` com schedule `0 4 * * *`; o relatório executivo aparece como `Relatório Hermes diário 01h + 02h + 02h15 para Lucas` com schedule `30 5 * * *`. Docs antigas que ainda digam 23h/02h sem a mudança de runtime devem ser reconciliadas com cuidado, sem inferir mudança de intenção a partir do nome apenas.
7. **`deliver=origin` em watchdog pausado:** `LK specialist Telegram gateway watchdog` está pausado mas configurado como `origin`; se reativado, validar se a entrega em Telegram é desejada ou se deve seguir silent-OK/local.

## Saídas intencionais `deliver=origin`

Confirmados na evidência viva:

- `Mesa COO diária Telegram` (`749ee30b51eb`) — ok.
- `Relatório Hermes diário 01h + 02h + 02h15 para Lucas` (`98478b820720`) — ok.
- `Hermes multi-profile latency watchdog` (`c1ce34b4449a`) — ok; alerta condicional.
- `Hermes all Telegram gateways watchdog` (`b78ae7ac81d0`) — ok; alerta condicional.
- `LK specialist Telegram gateway watchdog` (`955dc769b5a6`) — pausado, mas configurado como `origin`.

## O que não foi alterado

- Nenhum schedule, delivery, prompt, script, profile, Docker/gateway, VPS, Traefik, container, rede, sistema externo, campanha, Shopify, GMC, Notion, WhatsApp, email ou secret foi alterado.
- Nenhum segredo foi impresso ou versionado neste relatório.
- Este relatório é read-only / documental.

## Verificação

- Brain health check: `python3 scripts/brain_health_check.py --json reports/brain-health-check-2026-06-02-runtime-truth-reconciler.json` — **All checks passed** (`FAIL=0`, `WARN=0`).
- Secret scan dos arquivos tocados: **possible_secrets 0**.
- `git diff --check` nos arquivos tocados: sem problemas.
