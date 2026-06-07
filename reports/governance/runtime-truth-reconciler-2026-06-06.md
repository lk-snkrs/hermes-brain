# Runtime Truth Reconciler — 2026-06-06

Timestamp: 2026-06-06 11:20 UTC

Escopo: read-only Hermes cron/runtime evidence vs Hermes Brain documentation.

Fonte viva solicitada: `cronjob list`.

Resultado da fonte: `cronjob` não disponível no PATH deste runtime; fallback canônico executado sem mutação:

```bash
HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all
```

## Resumo da evidência viva

- Jobs totais: 31.
- Ativos: 27.
- Pausados: 4.
- `last_status` não-ok: 1.
- Erros explícitos de delivery do scheduler na listagem: 0.
- Falhas em stdout de job: 1, no próprio stdout do job não-ok.
- Jobs ativos sem primeira execução registrada: 0.

## Anomalias atuais

### 1. Hermes Brain Operating Layer structural watchdog (`d03fa04e1188`)

- Estado: ativo.
- Deliver: `local`.
- Último run: 2026-06-06T11:10:28Z.
- Status: `error: Script exited with code 1`.
- Sintoma redigido sem segredos: o watchdog informa que aplicou auto-heal criando `memories/daily/2026-06-06.md`, mas ainda encontrou gap: `memories/hot.md stale >3 days`.
- Ação tomada neste reconciler: nenhuma mudança de runtime/cron/Docker/VPS; apenas registro documental desta evidência viva.
- Próxima ação recomendada: frente própria de higiene do Operating Layer/memória para atualizar ou reconciliar `memories/hot.md`, se ainda aplicável, sem tratar isso como falha de delivery.

## Recuperações / drift positivo vs 2026-06-05

- `c3bb587519d2` — LK Pulso Comercial 16h read-only delivery: agora consta `ok` na evidência viva; não deve mais ser tratado como falha ativa WACLI/parser JSON sem nova evidência.
- `e3279babbc4a` — LK 09h previous-day sales report external delivery: segue `ok`.
- `a2ead305eab2` — LK 19h30 physical store close external delivery: segue `ok`.
- `357d40a5863e` — Zipper OS vendas 09h WhatsApp/email: segue `ok`.
- `787134d4ac5c` — LK Weekly Collection Sort Rule B: segue `ok`; não há timeout ativo na evidência atual.
- `a1d1e36f8075` — LK Weekly Catalog Badges BEST SELLER sync: segue com primeira execução registrada e `ok`.

## Mudança de inventário vs 2026-06-05

- A contagem viva passou de 29 para 31 jobs totais, 25 para 27 ativos, 4 pausados estável.
- Jobs observados na evidência viva que precisam permanecer documentados como ativos/ok ou serem incorporados em rodada própria de documentação operacional quando relevante:
  - `f5a23dd6a1bd` — LC Hermes daily intelligence loop — systemwide — ativo, `local`, `ok`.
  - `7c688553e293` — LK Daily Sales Brief read-only mandatory delivery — ativo, `local`, `ok`.
  - `953b9055458e` — LK Weekly CEO Review read-only mandatory delivery — ativo, `local`, `ok`.
  - `71b147362ec1` — Zipper Gmail style learning refresh — ativo, `local`, `ok`.
  - `5bacaa61bb12` — claude-proxy-watchdog — ativo, `local`, `ok`.
  - `3cd1011edf33` — claude-max-proxy watchdog — ativo, `local`, `ok`.
  - `a97a6317b197` — Zipper post-PDF follow-up watchdog — ativo, `local`, `ok`.
  - `7b7ae67655c5` — wacli pessoal sync watchdog — ativo, `local`, `ok`.

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

1. Atualizar/evitar repetir pendência antiga que tratava `c3bb587519d2` como falha atual; hoje ele consta `ok`.
2. Registrar a nova anomalia atual como `d03fa04e1188` — Operating Layer structural watchdog com `memories/hot.md stale >3 days` — sem mexer em runtime neste reconciler.
3. Atualizar a contagem documental de crons vivos para 31 totais / 27 ativos / 4 pausados quando a documentação depender de inventário atual.
4. Manter Mordomo/LK Growth/SPITI gateway watchdogs como pausados/históricos até nova evidência runtime.

## O que não foi alterado

- Não houve mudança de Docker, VPS, Traefik, redes, containers ou gateway.
- Não houve mudança de cron schedule/delivery/prompt/script.
- Não houve contato externo, campanha, Shopify, GMC, Notion, WhatsApp, email ou segredo.
- Foram atualizados apenas documentos/relatórios do Brain sob caminhos permitidos.

## Artefatos atualizados

- `areas/operacoes/inventarios/crons-agentes-profiles.md`
- `reports/governance/runtime-truth-reconciler-2026-06-06.md`
- `reports/brain-health-check-2026-06-06-runtime-truth-reconciler.json` (gerado ao final da rotina)
