# Runtime Truth Reconciler — 2026-06-10

Timestamp: 2026-06-10 11:20 UTC

Escopo: read-only Hermes cron/runtime evidence vs Hermes Brain documentation.

Fonte viva solicitada: `cronjob list`.

Resultado da fonte: `cronjob` não disponível no PATH deste runtime; fallback canônico executado sem mutação:

```bash
HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all
```

## Resumo da evidência viva

- Jobs totais: 36.
- Ativos: 32.
- Pausados: 4.
- `last_status` não-ok: 0.
- Erros explícitos de delivery do scheduler na listagem: 0.
- Falhas em stdout de job: 0 observadas pela listagem resumida.
- Jobs ativos sem primeira execução registrada: 0.

## Anomalias atuais

Nenhuma anomalia ativa observada na evidência viva desta execução. Todos os 36 jobs listados têm último status `ok`; os 4 jobs pausados também têm último status `ok` histórico.

## Mudança de inventário vs 2026-06-09

- Contagem mudou: 32 → 36 jobs totais; 28 → 32 ativos; 4 pausados estável.
- Novos jobs ativos/ok observados na evidência viva:
  - `bc96bb03d2b0` — Hermes Memory OS daytime checker/router — 30min alert-only — `deliver=origin`.
  - `6792657c0be7` — LK POS pós-compra WhatsApp auto-worker — `deliver=local`.
  - `e4c6b7c9b6dc` — Hermes Memory OS weekly observability local/silent — `deliver=local`.
  - `e2f169cc046a` — LK POS Shopify→fila reconciliador — `deliver=local`.
- Não houve job removido, `last_status` não-ok, delivery error explícito ou job ativo sem primeira execução registrada na evidência atual.
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
- `bc96bb03d2b0` — Hermes Memory OS daytime checker/router — 30min alert-only — ativo, `ok`.
- `955dc769b5a6` — LK specialist Telegram gateway watchdog — configurado como `origin`, mas pausado.

## Gaps de reconciliação documental

Gaps acionáveis/documentais:

1. Atualizar documentação/índices de rotina, em rodada própria, para refletir os 4 jobs ativos/ok que apareceram na evidência viva de 2026-06-10: `bc96bb03d2b0`, `6792657c0be7`, `e4c6b7c9b6dc`, `e2f169cc046a`.
2. Manter documentos de Mordomo/LK Growth/SPITI/LK specialist gateway watchdogs como históricos/pausados até nova evidência viva de reativação.

## O que não foi alterado

- Não houve mudança de Docker, VPS, Traefik, redes, containers ou gateway.
- Não houve mudança de cron schedule/delivery/prompt/script.
- Não houve contato externo, campanha, Shopify, GMC, Notion, WhatsApp, email ou segredo.
- Foram atualizados apenas documentos/relatórios do Brain sob caminhos permitidos.

## Artefatos atualizados

- `areas/operacoes/inventarios/crons-agentes-profiles.md`
- `reports/governance/runtime-truth-reconciler-2026-06-10.md`
- `reports/brain-health-check-2026-06-10-runtime-truth-reconciler.json` (gerado ao final da rotina)
