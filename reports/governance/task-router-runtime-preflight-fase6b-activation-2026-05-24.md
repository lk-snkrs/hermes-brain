# Task Router Técnico v1 — Fase 6B Ativação Runtime

Data: 2026-05-24
Status: ativado no gateway principal após restart controlado aprovado por Lucas

## Objetivo

Ativar no runtime do Hermes Geral o preflight metadata-only/read-only do Task Router técnico v1, sem criar writes externos e sem mudar Shopify/GMC/Klaviyo/Meta/WhatsApp/produção.

## Evidência de ativação

O gateway foi reiniciado de forma controlada e voltou com os serviços principais:

```text
Starting Hermes Gateway...
✓ webhook connected
[Telegram] Connected to Telegram (polling mode)
✓ telegram connected
[Api_Server] API server listening on http://0.0.0.0:8642
```

Status atual conferido:

```text
✓ Gateway is running (PID: 7, 63, 65, 68)
Other profiles:
  ✓ lk-growth — PID 65
  ✓ mordomo   — PID 63
  ✓ spiti     — PID 68
```

Health checks locais:

```text
http://127.0.0.1:8642/health 200 {"status": "ok", "platform": "hermes-agent"}
http://127.0.0.1:8644/health 200 {"status": "ok", "platform": "webhook"}
```

## Evidência funcional

A mensagem recebida após a ativação passou a carregar o bloco interno de preflight no turno do modelo, com instrução explícita para não expor metadata técnica ao Lucas.

O comportamento esperado é:

- Hermes Geral continua respondendo normalmente quando a rota for dele.
- Tarefas com dono especialista devem virar handoff/delegação ou approval packet local.
- Ações `preparar_approval_packet` ou `bloquear_por_aprovacao` não devem executar write externo/produção.
- A resposta Telegram deve permanecer limpa, sem JSON bruto, job_id, wrapper ou boilerplate.

## Verificação executada nesta sessão

Comando de regressão runtime + scheduler:

```bash
/opt/hermes/.venv/bin/python -m pytest tests/agent/test_lucas_task_router_preflight.py tests/cron/test_scheduler.py::TestDeliverResultWrapping -q -o 'addopts=' && \
python3 /opt/data/hermes_bruno_ingest/hermes-brain/scripts/test_hermes_task_router.py
```

Resultado:

```text
15 passed, 1 warning
Ran 5 tests
OK
```

Compilação:

```bash
PYTHONPYCACHEPREFIX=/tmp/hermes-pycache /opt/hermes/.venv/bin/python -m py_compile agent/lucas_task_router.py run_agent.py
```

Resultado: exit 0.

Scan focado de secrets nos arquivos tocados/usados:

```text
secret_findings 0
```

## Escopo do que foi ativado

Ativado:

- carregamento do router Brain em `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/hermes_task_router.py`;
- injeção metadata-only/read-only no turno atual do modelo;
- preservação do texto limpo do usuário para transcript quando aplicável;
- fail-open se o router falhar/estiver ausente/desabilitado.

Não ativado nesta fase:

- hard-blocker no dispatcher de ferramentas;
- execução automática em profiles especialistas;
- mutação de cron registry;
- qualquer write externo/produção.

## Rollback

Rollback lógico/env antes de novo restart:

```bash
HERMES_LUCAS_TASK_ROUTER_DISABLED=true
```

Rollback de código:

- remover import e bloco de preflight em `/opt/hermes/run_agent.py`;
- remover `/opt/hermes/agent/lucas_task_router.py`;
- remover `/opt/hermes/tests/agent/test_lucas_task_router_preflight.py`.

## Próximo passo recomendado — Fase 6C

Adicionar enforcement mais forte, ainda com testes primeiro:

1. tool-dispatch guardrail para bloquear ferramentas/ações externas quando `requires_approval` estiver ativo;
2. mensagem curta de approval packet em vez de execução direta;
3. handoff automático seguro para `lk-growth`, `mordomo` e `spiti` apenas em modo local/read-only;
4. testes garantindo que o preflight nunca vaze para Telegram/transcripts.
