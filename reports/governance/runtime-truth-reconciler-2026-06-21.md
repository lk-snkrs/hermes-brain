# Runtime Truth Reconciler — 2026-06-21

## 1. Timestamp e escopo

- Timestamp da execução: 2026-06-21 11:20 UTC.
- Escopo: reconciliação read-only/local entre evidência viva de crons Hermes e documentação do Hermes Brain.
- Workdir: `/opt/data/hermes_bruno_ingest/hermes-brain`.

## 2. Fonte viva

- Comando solicitado: `cronjob list`.
- Resultado: indisponível neste runtime (`cronjob: command not found`).
- Fallback canônico usado: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

## 3. Resumo da evidência viva

- Total: 42 jobs.
- Ativos: 38 jobs.
- Pausados: 4 jobs.
- `last_status` não-ok: 0.
- Erros explícitos de delivery do scheduler na listagem: 0.
- Jobs ativos sem primeira execução registrada: 0.

## 4. Anomalias atuais

Nenhuma anomalia runtime ativa encontrada na listagem viva: todos os jobs com execução registrada aparecem com `last_status=ok`, sem erro explícito de delivery e sem job ativo sem `Last run`.

## 5. Drift vs snapshot anterior

- Contagem estável vs 2026-06-20: 42 totais / 38 ativos / 4 pausados.
- Os três jobs Honcho recém-observados em 2026-06-20 continuam vivos, ativos, `deliver=origin` e `ok`:
  - `7d32b8b77317` Honcho Hermes memory watchdog silent-OK.
  - `39b176e08174` Honcho memory quality auditor silent-OK.
  - `16dfc4d14c85` Honcho Intelligence Layer v1 weekly silent-OK.
- `2e5bc91d27d6` Hermes Nightly Operations Audit OS — 02h50 BRT segue ativo/local/ok e ainda merece reconciliação documental de owner/finalidade/critério de sucesso em rodada própria.
- Documentação que descreve Mordomo/LK Growth/SPITI gateway watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.

## 6. Jobs pausados

| id | nome | deliver | último status |
|---|---|---:|---|
| `ac0b440e2643` | Mordomo Telegram gateway watchdog | local | ok em 2026-05-30T15:52:55.213145+00:00 |
| `876d54c62ccd` | LK Growth Telegram gateway watchdog | local | ok em 2026-05-30T15:52:55.226608+00:00 |
| `663e3e6a148c` | SPITI Telegram gateway watchdog | local | ok em 2026-05-30T15:52:55.201503+00:00 |
| `955dc769b5a6` | LK specialist Telegram gateway watchdog | origin | ok em 2026-05-30T15:52:55.190857+00:00 |

## 7. Jobs `deliver=origin`

`deliver=origin` não é falha por si só; é saída intencional/condicional quando documentada.

Ativos:

- `749ee30b51eb` Mesa COO diária Telegram — ok.
- `98478b820720` Relatório Hermes diário 01h+02h+02h15+02h25+02h50 + Score 0–100 — 03h Telegram — ok.
- `518634d5ea60` Reminder OS — 2h open-loop watchdog — ok.
- `7d32b8b77317` Honcho Hermes memory watchdog silent-OK — ok.
- `39b176e08174` Honcho memory quality auditor silent-OK — ok.
- `16dfc4d14c85` Honcho Intelligence Layer v1 weekly silent-OK — ok.

Pausado:

- `955dc769b5a6` LK specialist Telegram gateway watchdog — pausado/ok histórico.

## 8. Gaps documentais/acionáveis

1. Jobs Honcho `deliver=origin` + “silent-OK” continuam vivos e OK, mas precisam de documentação explícita de owner, finalidade, critério de sucesso, contrato de alerta e por que `origin` é intencional.
2. `2e5bc91d27d6` Hermes Nightly Operations Audit OS — 02h50 BRT continua vivo/local/ok e ainda merece reconciliação documental de owner/finalidade/critério de sucesso.
3. Watchdogs de gateway Mordomo/LK Growth/SPITI/LK specialist continuam pausados; manter docs como histórico/pausado até evidência viva de reativação.

## 9. O que não foi alterado

Não houve mudança em cron schedule/delivery/prompt/script, gateway/runtime, Docker, VPS, Traefik, redes, containers, sistemas externos, campanhas, Shopify, GMC, Notion, WhatsApp, email, bancos, tokens ou secrets.

## 10. Artefatos atualizados

- `areas/operacoes/inventarios/crons-agentes-profiles.md`
- `reports/governance/runtime-truth-reconciler-2026-06-21.md`
- `reports/brain-health-check-2026-06-21-runtime-truth-reconciler.json`

## 11. Verificação

- `python3 scripts/brain_health_check.py --json reports/brain-health-check-2026-06-21-runtime-truth-reconciler.json`: `All checks passed` (`FAIL=0/WARN=0`).
- `git diff --check` nos artefatos tocados: sem whitespace errors.
- Secret scan escopado dos artefatos tocados: `scoped_possible_secrets 0`.

## 12. Apêndice — inventário sanitizado vivo

Campos preservados: id, estado, deliver, último status/execução e nome. Não inclui prompt bruto, stdout bruto, env vars, tokens, process args ou secrets.

| id | estado | deliver | último status / execução | nome |
|---|---|---:|---|---|
| `f5a23dd6a1bd` | active | local | ok / 2026-06-21T05:13:07.187115+00:00 | LC Hermes daily intelligence loop — systemwide audit + self-improvement |
| `edd06fe19397` | active | local | ok / 2026-06-21T11:00:09.831293+00:00 | Hermes runtime + cron watchdog no_agent |
| `7c688553e293` | active | local | ok / 2026-06-21T11:00:47.564709+00:00 | LK Daily Sales Brief read-only mandatory delivery |
| `953b9055458e` | active | local | ok / 2026-06-15T12:02:58.587007+00:00 | LK Weekly CEO Review read-only mandatory delivery |
| `71b147362ec1` | active | local | ok / 2026-06-21T06:21:04.401599+00:00 | Zipper Gmail style learning refresh |
| `4bb4e2223fd3` | active | local | ok / 2026-06-21T11:20:09.574136+00:00 | Hermes compression failure self-heal watchdog |
| `c3bb587519d2` | active | local | ok / 2026-06-20T19:00:51.188479+00:00 | LK Pulso Comercial 16h read-only delivery |
| `e3279babbc4a` | active | local | ok / 2026-06-20T12:00:46.065199+00:00 | LK 09h previous-day sales report external delivery |
| `a2ead305eab2` | active | local | ok / 2026-06-20T22:31:14.457418+00:00 | LK 19h30 physical store close external delivery |
| `ac0b440e2643` | paused | local | ok / 2026-05-30T15:52:55.213145+00:00 | Mordomo Telegram gateway watchdog |
| `357d40a5863e` | active | local | ok / 2026-06-19T12:00:23.031331+00:00 | Zipper OS vendas 09h WhatsApp/email |
| `876d54c62ccd` | paused | local | ok / 2026-05-30T15:52:55.226608+00:00 | LK Growth Telegram gateway watchdog |
| `749ee30b51eb` | active | origin | ok / 2026-06-21T09:02:06.424776+00:00 | Mesa COO diária Telegram |
| `663e3e6a148c` | paused | local | ok / 2026-05-30T15:52:55.201503+00:00 | SPITI Telegram gateway watchdog |
| `3fc45b0830c6` | active | local | ok / 2026-06-21T04:12:12.930344+00:00 | Hermes Brain Fechamento Ágil 01h + Brain Sync |
| `f4c499e85eac` | active | local | ok / 2026-06-15T12:19:29.987705+00:00 | Lucas Brain weekly Learning Loop report |
| `d03fa04e1188` | active | local | ok / 2026-06-21T11:10:09.316013+00:00 | Hermes Brain Operating Layer structural watchdog |
| `2404c0766d33` | active | local | ok / 2026-06-20T11:24:04.591607+00:00 | Hermes Brain Runtime Truth Reconciler |
| `98478b820720` | active | origin | ok / 2026-06-21T06:01:17.367824+00:00 | Relatório Hermes diário 01h+02h+02h15+02h25+02h50 + Score 0–100 — 03h Telegram |
| `d9badcd83411` | active | local | ok / 2026-06-21T10:02:24.044849+00:00 | Hermes Brain strict-runtime guard watchdog |
| `c1ce34b4449a` | active | local | ok / 2026-06-21T11:11:09.983408+00:00 | Hermes multi-profile latency watchdog |
| `787134d4ac5c` | active | local | ok / 2026-06-19T09:00:09.750931+00:00 | LK Weekly Collection Sort Rule B |
| `a1d1e36f8075` | active | local | ok / 2026-06-19T09:38:58.178925+00:00 | LK Weekly Catalog Badges BEST SELLER sync |
| `5bacaa61bb12` | active | local | ok / 2026-06-21T11:17:09.416522+00:00 | claude-proxy-watchdog |
| `3cd1011edf33` | active | local | ok / 2026-06-21T11:19:11.480755+00:00 | claude-max-proxy watchdog |
| `955dc769b5a6` | paused | origin | ok / 2026-05-30T15:52:55.190857+00:00 | LK specialist Telegram gateway watchdog |
| `b78ae7ac81d0` | active | local | ok / 2026-06-21T11:20:15.141114+00:00 | Hermes all Telegram gateways watchdog |
| `c64a0c63b881` | active | local | ok / 2026-06-21T10:45:08.257023+00:00 | LK Tiny stock local DB daily fullsync |
| `f9a1d43caf48` | active | local | ok / 2026-06-21T05:15:59.512943+00:00 | Hermes memory hygiene watchdog 02h15 BRT |
| `a97a6317b197` | active | local | ok / 2026-06-21T10:55:09.604488+00:00 | Zipper post-PDF follow-up watchdog |
| `7b7ae67655c5` | active | local | ok / 2026-06-21T11:19:09.656378+00:00 | wacli pessoal sync watchdog |
| `810c0d2bf65a` | active | local | ok / 2026-06-21T11:16:09.546899+00:00 | LC Mordomo OS real local no-agent watcher |
| `bc96bb03d2b0` | active | local | ok / 2026-06-21T11:06:11.665821+00:00 | Hermes Memory OS daytime checker/router — 30min alert-only |
| `6792657c0be7` | active | local | ok / 2026-06-21T11:15:09.463462+00:00 | LK POS pós-compra WhatsApp auto-worker |
| `e4c6b7c9b6dc` | active | local | ok / 2026-06-15T12:45:34.207521+00:00 | Hermes Memory OS weekly observability local/silent |
| `e2f169cc046a` | active | local | ok / 2026-06-21T11:20:10.339005+00:00 | LK POS Shopify→fila reconciliador |
| `23143847316e` | active | local | ok / 2026-06-21T05:26:09.358344+00:00 | Brain OS silent-OK health/scanner watchdog — 02h25 BRT local |
| `518634d5ea60` | active | origin | ok / 2026-06-21T10:40:12.019487+00:00 | Reminder OS — 2h open-loop watchdog |
| `2e5bc91d27d6` | active | local | ok / 2026-06-21T05:51:00.265244+00:00 | Hermes Nightly Operations Audit OS — 02h50 BRT |
| `7d32b8b77317` | active | origin | ok / 2026-06-21T11:14:09.537503+00:00 | Honcho Hermes memory watchdog silent-OK |
| `39b176e08174` | active | origin | ok / 2026-06-21T07:20:10.741569+00:00 | Honcho memory quality auditor silent-OK |
| `16dfc4d14c85` | active | origin | ok / 2026-06-19T17:07:55.203946+00:00 | Honcho Intelligence Layer v1 weekly silent-OK |
