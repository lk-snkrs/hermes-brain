# Runtime Truth Reconciler — 2026-05-30

Timestamp UTC: 2026-05-30T11:20:00Z
Timestamp BRT: 2026-05-30T08:20:00 BRT

## Escopo

Reconciliação read-only entre evidência viva de crons Hermes e documentação do Hermes Brain.

## Fonte viva usada

- Comando solicitado: `cronjob list`.
- Resultado neste runtime: `cronjob` não encontrado no PATH.
- Fallback canônico usado com sucesso: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.
- Nenhum cron foi executado manualmente; evidência read-only apenas.

## Resumo da evidência viva

- Total de jobs listados: **23** (aumento de 19 → 23 vs evidência de 2026-05-29).
- Ativos: **23**.
- Pausados/disabled: **0**.
- `last_status` não-ok: **1** (timeout persistente).
- Erros explícitos de delivery: **0**.
- Jobs sem `Last run` ainda: **1** (LK Catalog Badges — nunca executou, aguarda próxima sexta).

## Inventário completo — 2026-05-30

| id | Nome | Schedule | Deliver | Último status |
|----|------|----------|---------|---------------|
| f5a23dd6a1bd | Lucas Brain daily intelligence loop | 0 5 * * * | local | ok (2026-05-30T05:08) |
| edd06fe19397 | Hermes runtime + cron watchdog no_agent | */30 * * * * | local | ok (2026-05-30T11:00) |
| 7c688553e293 | LK Daily Sales Brief read-only mandatory delivery | 0 11 * * * | local | ok (2026-05-30T11:01) |
| 953b9055458e | LK Weekly CEO Review read-only mandatory delivery | 0 12 * * 1 | local | ok (2026-05-25T12:01) |
| 71b147362ec1 | Zipper Gmail style learning refresh | 20 6 * * * | local | ok (2026-05-30T06:22) |
| 4bb4e2223fd3 | Hermes compression failure self-heal watchdog | */10 * * * * | local | ok (2026-05-30T11:10) |
| c3bb587519d2 | LK Pulso Comercial 16h read-only delivery | 0 19 * * * | local | ok (2026-05-29T19:01) |
| e3279babbc4a | LK 09h previous-day sales report external delivery | 0 12 * * * | local | ok (2026-05-29T12:00) |
| a2ead305eab2 | LK 19h30 physical store close external delivery | 30 22 * * * | local | ok (2026-05-29T22:30) |
| ac0b440e2643 | Mordomo Telegram gateway watchdog | every 1m | local | ok (2026-05-30T11:19) |
| 357d40a5863e | Zipper OS vendas 09h WhatsApp/email | 0 12 * * 1-5 | local | ok (2026-05-29T12:00) |
| 876d54c62ccd | LK Growth Telegram gateway watchdog | every 1m | local | ok (2026-05-30T11:19) |
| 749ee30b51eb | Mesa COO diária Telegram | 0 9 * * * | **origin** | ok (2026-05-30T09:01) |
| 663e3e6a148c | SPITI Telegram gateway watchdog | every 1m | local | ok (2026-05-30T11:19) |
| 3fc45b0830c6 | Hermes Brain Fechamento Ágil 23h + Brain Sync | 0 2 * * * | local | ok (2026-05-30T02:07) |
| f4c499e85eac | Lucas Brain weekly Learning Loop report | 15 12 * * 1 | local | ok (2026-05-25T12:20) |
| d03fa04e1188 | Hermes Brain Operating Layer structural watchdog | 10 11 * * * | local | ok (2026-05-30T11:10) |
| 2404c0766d33 | Hermes Brain Runtime Truth Reconciler | 20 11 * * * | local | ok (2026-05-29T11:22) |
| 98478b820720 | Relatório Hermes diário 23h + 02h para Lucas | 30 5 * * * | **origin** | ok (2026-05-30T05:31) |
| d9badcd83411 | Hermes Brain strict-runtime guard watchdog | 0 10 * * * | local | ok (2026-05-30T10:01) |
| c1ce34b4449a | Hermes multi-profile latency watchdog | every 15m | **origin** | ok (2026-05-30T11:12) |
| 787134d4ac5c | LK Weekly Collection Sort Rule B | 0 9 * * 5 | local | **error: timeout 120s** (2026-05-29T06:02) |
| a1d1e36f8075 | LK Weekly Catalog Badges BEST SELLER sync | 30 9 * * 5 | local | (sem last run — nunca executou) |

## Drift vs relatório anterior (2026-05-29)

### Novos jobs confirmados em evidência viva (4 adições)

Os seguintes 4 jobs foram listados como ausentes na evidência de 2026-05-29 e agora aparecem:

1. **`d03fa04e1188` — Hermes Brain Operating Layer structural watchdog** (10 11 * * *, local, script `brain_operating_layer_audit.py`) — last run ok 2026-05-30T11:10. Anteriormente ausente da listagem.
2. **`d9badcd83411` — Hermes Brain strict-runtime guard watchdog** (0 10 * * *, local, script `hermes_brain_strict_runtime_guard_watchdog.py`) — last run ok 2026-05-30T10:01. Anteriormente ausente.
3. **`2404c0766d33` — Hermes Brain Runtime Truth Reconciler** (20 11 * * *, local) — este próprio job. Anteriormente ausente.
4. **`a1d1e36f8075` — LK Weekly Catalog Badges BEST SELLER sync** (30 9 * * 5, local, script `lk_catalog_badges_weekly_sync.sh`) — novo job, nunca executou, next run 2026-06-05T09:30.

**Interpretação:** Os 3 watchdogs operacionais estavam presentes na lista mas ausentes no relatório anterior por leitura parcial/truncada. Não há indicação de que foram removidos e recriados; drift documental, não drift real.

### Anomalia persistente

1. **`787134d4ac5c` — LK Weekly Collection Sort Rule B** — `error: Script timed out after 120s: /opt/data/scripts/lk_weekly_collection_sort_ruleB.sh` em 2026-05-29T06:02. Timeout permanece no mesmo estado do relatório anterior. Próximo run: 2026-06-05T09:00.
   - **Ação recomendada:** revisar script `lk_weekly_collection_sort_ruleB.sh` para otimização de tempo de execução, aumento do timeout, ou alternativa de implementação. Não foi alterado neste run (read-only).

### Jobs com deliver=origin (saídas intencionais para Telegram)

Confirmados como entregas executivas intencionais (não ruído):
- `Mesa COO diária Telegram` (`749ee30b51eb`) — ok.
- `Relatório Hermes diário 23h + 02h para Lucas` (`98478b820720`) — ok.
- `Hermes multi-profile latency watchdog` (`c1ce34b4449a`) — ok (alerta condicional).

## O que não foi alterado

- Nenhum schedule, delivery, prompt, script, profile, Docker/gateway, VPS, Traefik, container, rede, sistema externo, campanha, Shopify, GMC, Notion, WhatsApp, email ou secret foi alterado.
- Nenhum segredo foi impresso ou versionado neste relatório.
- Este relatório é read-only / documental.

## Verificação

- Brain health check: `python3 scripts/brain_health_check.py --json reports/brain-health-check-2026-05-30-runtime-truth-reconciler.json`
- Secret scan dos arquivos tocados: pendente (ver resultado na seção de verificação abaixo).
