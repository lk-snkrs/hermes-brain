# Runtime Truth Reconciler — 2026-06-20

Timestamp: 2026-06-20 11:20 UTC

Escopo: read-only Hermes cron/runtime evidence vs Hermes Brain documentation.

Fonte viva solicitada: `cronjob list`.

Resultado da fonte: `cronjob` não disponível no PATH deste runtime; fallback canônico executado sem mutação:

```bash
HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all
```

## Resumo da evidência viva

- Jobs totais: 42.
- Ativos: 38.
- Pausados: 4.
- `last_status` não-ok: 0.
- Erros explícitos de delivery do scheduler na listagem: 0.
- Falhas em stdout de job: 0 observadas pela listagem resumida.
- Jobs ativos sem primeira execução registrada: 0.

## Anomalias atuais

Nenhuma anomalia de falha ativa observada: todos os jobs listados com execução registrada têm último status `ok`, e não há erro explícito de delivery na listagem.

Atenção documental/runtime:

- A contagem viva subiu de 39 para 42 jobs vs 2026-06-19: 35 → 38 ativos; 4 pausados estável. Não houve `last_status` não-ok nem delivery error; tratar como drift documental de inventário, não como falha runtime.
- Novos jobs vivos na evidência, todos ativos/`deliver=origin`/último status `ok`: `7d32b8b77317` Honcho Hermes memory watchdog silent-OK, `39b176e08174` Honcho memory quality auditor silent-OK, `16dfc4d14c85` Honcho Intelligence Layer v1 weekly silent-OK.
- `2e5bc91d27d6` — Hermes Nightly Operations Audit OS — 02h50 BRT — continua ativo/local/ok e ainda merece reconciliação documental de owner, finalidade e critério de sucesso em rodada própria.

## Mudança de inventário vs 2026-06-19

- Contagem mudou: 39 → 42 jobs totais; 35 → 38 ativos; 4 pausados estável.
- Novos jobs identificáveis por comparação com o relatório anterior: `7d32b8b77317`, `39b176e08174`, `16dfc4d14c85`.
- Nenhum `last_status` não-ok ou delivery error explícito.
- Nenhum job ativo sem primeira execução registrada.
- Jobs previamente problemáticos continuam `ok` e não devem permanecer como falha ativa sem nova evidência: `d03fa04e1188`, `c3bb587519d2`, `e3279babbc4a`, `a2ead305eab2`, `357d40a5863e`, `787134d4ac5c`, `a1d1e36f8075`.

## Jobs pausados na evidência viva

- `ac0b440e2643` — Mordomo Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `876d54c62ccd` — LK Growth Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `663e3e6a148c` — SPITI Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `955dc769b5a6` — LK specialist Telegram gateway watchdog — pausado, `deliver=origin`, último status ok em 2026-05-30T15:52.

Documentação que ainda descreve esses watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.

## Jobs com `deliver=origin`

Saídas intencionais/condicionais observadas:

- `749ee30b51eb` — Mesa COO diária Telegram — ativo, `ok`.
- `98478b820720` — Relatório Hermes diário 01h+02h+02h15+02h25+02h50 + Score 0–100 — 03h Telegram — ativo, `ok`.
- `518634d5ea60` — Reminder OS — 2h open-loop watchdog — ativo, `ok`.
- `7d32b8b77317` — Honcho Hermes memory watchdog silent-OK — ativo, `ok`.
- `39b176e08174` — Honcho memory quality auditor silent-OK — ativo, `ok`.
- `16dfc4d14c85` — Honcho Intelligence Layer v1 weekly silent-OK — ativo, `ok`.
- `955dc769b5a6` — LK specialist Telegram gateway watchdog — configurado como `origin`, mas pausado.

## Gaps de reconciliação documental

Gaps acionáveis/documentais:

1. Reconciliar os três jobs Honcho novos (`7d32b8b77317`, `39b176e08174`, `16dfc4d14c85`) em documentação de owner, finalidade, critério de sucesso, contrato silent-OK e motivo de `deliver=origin`.
2. Documentar/reconciliar `2e5bc91d27d6` em rodada própria, especialmente owner, finalidade e critério de sucesso.
3. Manter documentos de Mordomo/LK Growth/SPITI/LK specialist gateway watchdogs como históricos/pausados até nova evidência viva de reativação.

## O que não foi alterado

- Não houve mudança de Docker, VPS, Traefik, redes, containers ou gateway.
- Não houve mudança de cron schedule/delivery/prompt/script.
- Não houve contato externo, campanha, Shopify, GMC, Notion, WhatsApp, email ou segredo.
- Foram atualizados apenas documentos/relatórios do Brain sob caminhos permitidos.

## Artefatos atualizados

- `areas/operacoes/inventarios/crons-agentes-profiles.md`
- `reports/governance/runtime-truth-reconciler-2026-06-20.md`
- `reports/brain-health-check-2026-06-20-runtime-truth-reconciler.json` (resultado final registrado após execução)

## Verificação

- `python3 scripts/brain_health_check.py --json reports/brain-health-check-2026-06-20-runtime-truth-reconciler.json`: `All checks passed` (`FAIL=0/WARN=0`).
- `git diff --check` escopado aos arquivos tocados nesta execução: ok.
- Secret scan escopado aos arquivos tocados nesta execução: `scoped_possible_secrets 0`.

## Apêndice — inventário sanitizado 2026-06-20

| id | estado | deliver | último status | nome |
|---|---|---|---|---|
| `f5a23dd6a1bd` | active | local | ok | LC Hermes daily intelligence loop — systemwide audit + self-improvement |
| `edd06fe19397` | active | local | ok | Hermes runtime + cron watchdog no_agent |
| `7c688553e293` | active | local | ok | LK Daily Sales Brief read-only mandatory delivery |
| `953b9055458e` | active | local | ok | LK Weekly CEO Review read-only mandatory delivery |
| `71b147362ec1` | active | local | ok | Zipper Gmail style learning refresh |
| `4bb4e2223fd3` | active | local | ok | Hermes compression failure self-heal watchdog |
| `c3bb587519d2` | active | local | ok | LK Pulso Comercial 16h read-only delivery |
| `e3279babbc4a` | active | local | ok | LK 09h previous-day sales report external delivery |
| `a2ead305eab2` | active | local | ok | LK 19h30 physical store close external delivery |
| `ac0b440e2643` | paused | local | ok | Mordomo Telegram gateway watchdog |
| `357d40a5863e` | active | local | ok | Zipper OS vendas 09h WhatsApp/email |
| `876d54c62ccd` | paused | local | ok | LK Growth Telegram gateway watchdog |
| `749ee30b51eb` | active | origin | ok | Mesa COO diária Telegram |
| `663e3e6a148c` | paused | local | ok | SPITI Telegram gateway watchdog |
| `3fc45b0830c6` | active | local | ok | Hermes Brain Fechamento Ágil 01h + Brain Sync |
| `f4c499e85eac` | active | local | ok | Lucas Brain weekly Learning Loop report |
| `d03fa04e1188` | active | local | ok | Hermes Brain Operating Layer structural watchdog |
| `2404c0766d33` | active | local | ok | Hermes Brain Runtime Truth Reconciler |
| `98478b820720` | active | origin | ok | Relatório Hermes diário 01h+02h+02h15+02h25+02h50 + Score 0–100 — 03h Telegram |
| `d9badcd83411` | active | local | ok | Hermes Brain strict-runtime guard watchdog |
| `c1ce34b4449a` | active | local | ok | Hermes multi-profile latency watchdog |
| `787134d4ac5c` | active | local | ok | LK Weekly Collection Sort Rule B |
| `a1d1e36f8075` | active | local | ok | LK Weekly Catalog Badges BEST SELLER sync |
| `5bacaa61bb12` | active | local | ok | claude-proxy-watchdog |
| `3cd1011edf33` | active | local | ok | claude-max-proxy watchdog |
| `955dc769b5a6` | paused | origin | ok | LK specialist Telegram gateway watchdog |
| `b78ae7ac81d0` | active | local | ok | Hermes all Telegram gateways watchdog |
| `c64a0c63b881` | active | local | ok | LK Tiny stock local DB daily fullsync |
| `f9a1d43caf48` | active | local | ok | Hermes memory hygiene watchdog 02h15 BRT |
| `a97a6317b197` | active | local | ok | Zipper post-PDF follow-up watchdog |
| `7b7ae67655c5` | active | local | ok | wacli pessoal sync watchdog |
| `810c0d2bf65a` | active | local | ok | LC Mordomo OS real local no-agent watcher |
| `bc96bb03d2b0` | active | local | ok | Hermes Memory OS daytime checker/router — 30min alert-only |
| `6792657c0be7` | active | local | ok | LK POS pós-compra WhatsApp auto-worker |
| `e4c6b7c9b6dc` | active | local | ok | Hermes Memory OS weekly observability local/silent |
| `e2f169cc046a` | active | local | ok | LK POS Shopify→fila reconciliador |
| `23143847316e` | active | local | ok | Brain OS silent-OK health/scanner watchdog — 02h25 BRT local |
| `518634d5ea60` | active | origin | ok | Reminder OS — 2h open-loop watchdog |
| `2e5bc91d27d6` | active | local | ok | Hermes Nightly Operations Audit OS — 02h50 BRT |
| `7d32b8b77317` | active | origin | ok | Honcho Hermes memory watchdog silent-OK |
| `39b176e08174` | active | origin | ok | Honcho memory quality auditor silent-OK |
| `16dfc4d14c85` | active | origin | ok | Honcho Intelligence Layer v1 weekly silent-OK |
