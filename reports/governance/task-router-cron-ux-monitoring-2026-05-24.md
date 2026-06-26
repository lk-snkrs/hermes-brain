# Task Router + Cron UX Monitoring — 2026-05-24

## Escopo

Monitoramento read-only após ativação da Fase 7B e correção de UX da Mesa COO no Telegram.

## Evidências verificadas

- Horário da checagem: 2026-05-24T23:51:06Z.
- `cron/scheduler.py` mtime: 2026-05-24T21:39:28Z.
- `agent/lucas_task_router.py` mtime: 2026-05-24T22:02:38Z.
- Gateways vivos com start posterior aos patches:
  - Main `/opt/data`: PID 7, start 2026-05-24T23:23:02Z.
  - LK Growth `/opt/data/profiles/lk-growth`: PID 76, start 2026-05-24T23:24:07Z.
  - Mordomo `/opt/data/profiles/mordomo`: PID 77, start 2026-05-24T23:24:07Z.
  - SPITI `/opt/data/profiles/spiti`: PID 86, start 2026-05-24T23:24:09Z.
- Health checks:
  - API `127.0.0.1:8642/health`: OK.
  - Webhook `127.0.0.1:8644/health`: OK.
- Logs recentes `gateway.log` e `agent.log` após 23h UTC:
  - `Cronjob Response`: 0 ocorrências recentes.
  - `HERMES_INLINE_BUTTONS`: 0 ocorrências recentes.
  - `To stop or manage this job`: 0 ocorrências recentes.
  - `decision_json`/preflight metadata: 0 ocorrências recentes.
  - delivery errors recentes: 0.
- Cron `Mesa COO diária Telegram`:
  - enabled.
  - deliver: `origin`.
  - próxima execução: 2026-05-25T09:00:00Z.
  - último status: OK, sem `last_delivery_error`.

## Verificação automatizada

Comando executado:

```bash
/opt/hermes/.venv/bin/python -m pytest \
  tests/cron/test_scheduler.py::TestDeliverResultWrapping \
  tests/agent/test_lucas_task_router_preflight.py -q
```

Resultado:

- 23 passed.
- 1 warning benigno de permissão de `.pytest_cache` em `/opt/hermes`; não afeta os testes.

## Conclusão

O runtime vivo está carregando código posterior aos patches. O caminho de entrega cron com botões nativos está coberto por regressões e os logs recentes não mostram novo vazamento de wrapper/metadata.

A próxima validação real é a execução automática da Mesa COO em 2026-05-25T09:00:00Z. A expectativa é entrega limpa no Telegram: texto humano + botões nativos, sem header/footer de cron, job id, JSON, comentário HTML ou preflight metadata.

## Se voltar a vazar

1. Capturar a mensagem visível no Telegram.
2. Conferir se o output do job tinha marcador `HERMES_INLINE_BUTTONS` válido.
3. Conferir se a entrega passou pelo live adapter ou fallback standalone.
4. Rodar novamente `TestDeliverResultWrapping`.
5. Só reiniciar gateway se o mtime do patch for posterior ao start do processo vivo.
