# Audit — todos os crons Hermes — 2026-06-26

Data UTC: 2026-06-26T13:08Z

## Veredito

Estado geral: **quase tudo correto**.

- Total de jobs: `44`
- Ativos: `40`
- Pausados: `4`
- Scripts referenciados faltando: `0`
- Jobs ativos overdue >15min: `0`
- Jobs ativos com `last_status=ok`: `38`
- Jobs ativos sem primeira execução: `1` futuro/one-shot esperado
- Jobs ativos com `last_status=error`: `1`

O único job ativo non-OK é:

```text
e3279babbc4a — LK 09h previous-day sales report external delivery
last_status=error
last_run_at=2026-06-26T12:00:58Z
next_run_at=2026-06-27T12:00:00Z
```

Esse erro foi corrigido localmente e no Brain PR #151, mas **não rodei o envio externo manualmente**. Por isso o scheduler ainda mostra `last_status=error` até a próxima execução real aprovada do cron.

## Classificação do único erro ativo

### `e3279babbc4a` — LK 09h previous-day sales report external delivery

Status cron atual: `error`.

Causa original:

```text
generated payload missing message/html/email_meta
```

Correção já aplicada antes deste audit:

- Restaurado o contrato completo do gerador LK OS sales reports.
- Restaurado `config/lk-report-delivery-targets.json`.
- PR #151 mergeado no `main` do `hermes-brain`.

Verificação neste audit, sem envio externo:

```text
python3 /opt/data/scripts/lk_report_external_delivery.py --report previous-day-09h
→ dry_run_ok
send_requested=false
subject="LK OS · Fechamento de ontem — 25/06"
```

Interpretação: **erro de metadata do cron está stale**, mas o caminho de geração/delivery está corrigido em dry-run. Para mudar `last_status` para `ok`, seria preciso aguardar o próximo tick real ou executar o cron/script com `--send`, que envia WhatsApp/e-mail e não foi feito sem pedido explícito.

## Job ativo sem primeira execução

```text
00a9f839879f — Honcho utility go/no-go review one-shot
next_run_at=2026-06-29T01:10:16Z
last_status=null
last_run_at=null
```

Classificação: **esperado**. É one-shot futuro; sem run ainda não é erro.

## Deliver origin ativo

Ativos com `deliver=origin`: `4`.

- `749ee30b51eb` — Mesa COO diária Telegram — `ok`, esperado.
- `98478b820720` — Relatório Hermes diário 03h Telegram — `ok`, obrigatório/esperado.
- `518634d5ea60` — Reminder OS 2h open-loop watchdog — `ok`, deve ser silent-OK e só alertar loop acionável.
- `00a9f839879f` — Honcho utility go/no-go review one-shot — futuro, ainda sem execução.

Não há indício de delivery `origin` indevido neste snapshot.

## Pausados

Pausados: `4`, todos com último status `ok` e estado `paused`:

- `ac0b440e2643` — Mordomo Telegram gateway watchdog
- `876d54c62ccd` — LK Growth Telegram gateway watchdog
- `663e3e6a148c` — SPITI Telegram gateway watchdog
- `955dc769b5a6` — LK specialist Telegram gateway watchdog

Classificação: histórico/pausado; não é falha ativa.

## Verificações executadas

- Cron registry parse: `44 total / 40 active / 4 paused`.
- Missing scripts check: `0`.
- Overdue >15min: `0`.
- Active non-OK: `1`, classificado acima.
- Python cron scripts compile: `29` scripts, `0` erros.
- Brain health: `ok`.
- Strict-runtime guard: `fail_count=0`, `scanned_files=2589`.
- Kanban diagnostics LK: `0`.
- LK 09h delivery dry-run: `dry_run_ok`, `send_requested=false`.
- Secrets: valores não impressos; `values_printed=false`.

## O que não foi feito

- Não executei `cronjob run e3279babbc4a` porque ele é job de envio externo aprovado e dispararia WhatsApp/e-mail.
- Não alterei cron schedule, deliver, enabled/state, prompt ou script.
- Não reiniciei gateway, Docker, VPS, Traefik ou perfis.
- Não mexi em secrets.

## Próximo passo recomendado

Nenhuma ação urgente no Task OS/cron scheduler.

Para zerar o `last_status=error` do `e3279babbc4a`, opções seguras:

1. **Aguardar o próximo run natural** em `2026-06-27T12:00:00Z`.
2. Se Lucas quiser reenvio/validação real agora, pedir aprovação explícita para rodar o job com envio externo, pois isso pode enviar WhatsApp/e-mail.

## Conclusão

Os crons estão operacionalmente saudáveis, com uma exceção de status stale pós-correção:

```text
healthy_or_expected = 43/44
active_currently_attention = 1/44
```

A exceção tem dry-run corrigido e não foi executada em modo send por segurança.
