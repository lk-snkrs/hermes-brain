# Task Router / Cron Telegram Clean Decision UX — Fase 6D

Data: 2026-05-24T21:40:36+00:00

## Problema

Uma decisão da Mesa COO chegou no Telegram com wrapper técnico visível:

- cabeçalho `Cronjob Response`;
- `job_id`;
- separador técnico;
- boilerplate de gestão do cron;
- marcador interno de botões quando não processado pelo runtime.

Isso torna a decisão 1/N inutilizável para Lucas e viola o contrato de Telegram limpo.

## Correção implementada

Arquivo alterado:

- `/opt/hermes/cron/scheduler.py`

Mudança:

- O scheduler agora extrai o marcador oculto `HERMES_INLINE_BUTTONS` do conteúdo bruto antes de aplicar qualquer wrapper legado.
- Quando existe metadata válida de botões, a entrega é tratada como card de decisão e o wrapper do cron é suprimido mesmo se `cron.wrap_response` estiver ligado em um runtime legado.
- O texto enviado preserva somente o conteúdo humano da decisão e passa os botões por `metadata={"inline_buttons": ...}`.

## Regressão adicionada

Arquivo alterado:

- `/opt/hermes/tests/cron/test_scheduler.py`

Teste novo:

- `TestDeliverResultWrapping::test_inline_button_decision_delivery_suppresses_wrapper_even_when_enabled`

Contrato coberto:

- mensagem de decisão com botões não contém `Cronjob Response`;
- não contém `job_id`;
- não contém boilerplate `To stop or manage this job`;
- não contém `HERMES_INLINE_BUTTONS` nem comentário HTML;
- metadata de botões é preservada para renderização nativa no Telegram.

## Verificação

Comando RED inicial:

```bash
/opt/hermes/.venv/bin/python -m pytest tests/cron/test_scheduler.py::TestDeliverResultWrapping::test_inline_button_decision_delivery_suppresses_wrapper_even_when_enabled -q
```

Resultado esperado antes da correção:

- falhou porque `Cronjob Response` ainda aparecia no conteúdo enviado.

Comandos GREEN:

```bash
/opt/hermes/.venv/bin/python -m pytest tests/cron/test_scheduler.py::TestDeliverResultWrapping::test_inline_button_decision_delivery_suppresses_wrapper_even_when_enabled -q
/opt/hermes/.venv/bin/python -m pytest tests/cron/test_scheduler.py::TestDeliverResultWrapping -q
/opt/hermes/.venv/bin/python -m py_compile /opt/hermes/cron/scheduler.py /opt/hermes/gateway/platforms/telegram.py
```

Resultados:

- teste novo: `1 passed`;
- classe de entrega cron: `13 passed`;
- `py_compile`: exit code 0.

Observação: pytest emitiu apenas warning de cache sem permissão em `/opt/hermes/.pytest_cache`; não é falha funcional.

## Status de ativação

A correção está implementada em código-fonte, verificada por testes e ativa no runtime vivo verificado em 2026-05-24T21:45:03+00:00.

Evidência de ativação:

- `/opt/hermes/cron/scheduler.py` mtime: 2026-05-24T21:39:28.725754.
- Processos `hermes gateway run` principais iniciaram depois do patch: `/opt/data` PID 7 em 21:42:50 UTC; perfis `mordomo`, `lk-growth` e `spiti` em 21:42:55 UTC.
- Health checks: API `127.0.0.1:8642/health` 200 OK; webhook `127.0.0.1:8644/health` 200 OK.

## Guardrails preservados

- Nenhum write externo foi feito.
- Nenhum Shopify/GMC/Klaviyo/WhatsApp/e-mail/produção foi alterado.
- Nenhum container/compose/volume/rede/Traefik foi alterado nesta etapa.
