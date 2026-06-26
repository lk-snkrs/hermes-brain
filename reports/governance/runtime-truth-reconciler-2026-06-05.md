# Runtime Truth Reconciler — 2026-06-05

Timestamp: 2026-06-05 11:20 UTC

Escopo: read-only Hermes cron/runtime evidence vs Hermes Brain documentation.

Fonte viva solicitada: `cronjob list`.

Resultado da fonte: `cronjob` não disponível no PATH deste runtime; fallback canônico executado sem mutação:

```bash
HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all
```

## Resumo da evidência viva

- Jobs totais: 29.
- Ativos: 25.
- Pausados: 4.
- `last_status` não-ok: 1.
- Erros explícitos de delivery do scheduler na listagem: 0.
- Falhas em stdout de job com envio externo aprovado: 1.
- Jobs ativos sem primeira execução registrada: 0.

## Anomalias atuais

### 1. LK Pulso Comercial 16h read-only delivery (`c3bb587519d2`)

- Estado: ativo.
- Deliver: `local`.
- Último run: 2026-06-04T19:00:34Z.
- Status: `error: Script exited with code 1`.
- Sintoma redigido sem segredos: falha durante envio externo aprovado via WACLI/parser JSON em `/opt/data/scripts/lk_report_external_delivery.py`.
- Ação tomada neste reconciler: nenhuma reautenticação, nenhum retry externo, nenhum write em runtime.
- Próxima ação recomendada: frente própria para validar WACLI/account/output JSON do fluxo LK 16h, com guardrails de externo já existentes.

## Recuperações / drift positivo vs 2026-06-04

- `e3279babbc4a` — LK 09h previous-day sales report external delivery: agora consta `ok` na evidência viva.
- `a2ead305eab2` — LK 19h30 physical store close external delivery: agora consta `ok` na evidência viva.
- `357d40a5863e` — Zipper OS vendas 09h WhatsApp/email: agora consta `ok` na evidência viva.
- `787134d4ac5c` — LK Weekly Collection Sort Rule B: executou em 2026-06-05T09:01 com status `ok`; não há timeout ativo na evidência atual.
- `a1d1e36f8075` — LK Weekly Catalog Badges BEST SELLER sync: executou pela primeira vez em 2026-06-05T09:39 com status `ok`; não deve mais ser classificado como job ativo sem primeira execução.

## Jobs pausados na evidência viva

- `ac0b440e2643` — Mordomo Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `876d54c62ccd` — LK Growth Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `663e3e6a148c` — SPITI Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `955dc769b5a6` — LK specialist Telegram gateway watchdog — pausado, `deliver=origin`, último status ok em 2026-05-30T15:52.

Documentação que ainda descreve esses watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.

## Jobs com `deliver=origin`

Saídas intencionais/condicionais observadas:

- `749ee30b51eb` — Mesa COO diária Telegram — ativo, `ok`.
- `98478b820720` — Relatório Hermes diário 01h + 02h + 02h15 para Lucas — ativo, `ok`.
- `c1ce34b4449a` — Hermes multi-profile latency watchdog — ativo, `ok`.
- `b78ae7ac81d0` — Hermes all Telegram gateways watchdog — ativo, `ok`.
- `955dc769b5a6` — LK specialist Telegram gateway watchdog — configurado como `origin`, mas pausado.

## Gaps de reconciliação documental

1. Atualizar/evitar repetir pendência antiga que tratava quatro rotinas externas como falhas atuais; hoje apenas `c3bb587519d2` está não-ok.
2. Atualizar docs que classificam `a1d1e36f8075` como “sem primeira execução”; agora há run `ok` em 2026-06-05.
3. Manter Mordomo/LK Growth/SPITI gateway watchdogs como pausados/históricos até nova evidência runtime.
4. Abrir frente própria, se Lucas quiser, para falha do LK 16h WACLI/parser JSON; este reconciler não executou nenhuma ação externa.

## O que não foi alterado

- Não houve mudança de Docker, VPS, Traefik, redes, containers ou gateway.
- Não houve mudança de cron schedule/delivery/prompt/script.
- Não houve contato externo, campanha, Shopify, GMC, Notion, WhatsApp, email ou segredo.
- Foram atualizados apenas documentos/relatórios do Brain sob caminhos permitidos.

## Artefatos atualizados

- `areas/operacoes/inventarios/crons-agentes-profiles.md`
- `reports/governance/runtime-truth-reconciler-2026-06-05.md`
- `reports/brain-health-check-2026-06-05-runtime-truth-reconciler.json` (gerado ao final da rotina)
