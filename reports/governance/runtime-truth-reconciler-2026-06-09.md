# Runtime Truth Reconciler — 2026-06-09

Timestamp: 2026-06-09 11:20 UTC

Escopo: read-only Hermes cron/runtime evidence vs Hermes Brain documentation.

Fonte viva solicitada: `cronjob list`.

Resultado da fonte: `cronjob` não disponível no PATH deste runtime; fallback canônico executado sem mutação:

```bash
HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all
```

## Resumo da evidência viva

- Jobs totais: 32.
- Ativos: 28.
- Pausados: 4.
- `last_status` não-ok: 0.
- Erros explícitos de delivery do scheduler na listagem: 0.
- Falhas em stdout de job: 0 observadas pela listagem resumida.
- Jobs ativos sem primeira execução registrada: 0.

## Anomalias atuais

Nenhuma anomalia ativa observada na evidência viva desta execução. Todos os 32 jobs listados têm último status `ok`; os 4 jobs pausados também têm último status `ok` histórico.

## Mudança de inventário vs 2026-06-08

- Contagem estável: 32 jobs totais / 28 ativos / 4 pausados.
- Não houve novo job vivo, job removido, `last_status` não-ok, delivery error explícito ou job ativo sem primeira execução registrada na evidência atual.
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
- `98478b820720` — Relatório Hermes diário 01h+02h+02h15 para Lucas — Telegram obrigatório — ativo, `ok`.
- `c1ce34b4449a` — Hermes multi-profile latency watchdog — ativo, `ok`.
- `b78ae7ac81d0` — Hermes all Telegram gateways watchdog — ativo, `ok`.
- `955dc769b5a6` — LK specialist Telegram gateway watchdog — configurado como `origin`, mas pausado.

## Gaps de reconciliação documental

Sem gap acionável novo nesta execução. A rotina mantém como nota de higiene: documentos que descrevam Mordomo/LK Growth/SPITI/LK specialist gateway watchdogs como ativos devem ser lidos como históricos até nova evidência viva de reativação.

## O que não foi alterado

- Não houve mudança de Docker, VPS, Traefik, redes, containers ou gateway.
- Não houve mudança de cron schedule/delivery/prompt/script.
- Não houve contato externo, campanha, Shopify, GMC, Notion, WhatsApp, email ou segredo.
- Foram atualizados apenas documentos/relatórios do Brain sob caminhos permitidos.

## Artefatos atualizados

- `areas/operacoes/inventarios/crons-agentes-profiles.md`
- `reports/governance/runtime-truth-reconciler-2026-06-09.md`
- `reports/brain-health-check-2026-06-09-runtime-truth-reconciler.json` (gerado ao final da rotina)
