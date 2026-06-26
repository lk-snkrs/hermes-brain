# Task Router Técnico v1 — Fase 6A Runtime Preflight Metadata

Data: 2026-05-24
Status: implementado em código, pendente de ativação por restart controlado do runtime/gateway

## Objetivo

Conectar o Task Router v1 ao runtime Hermes sem transformar o classificador em ponto único de falha e sem executar writes externos. A integração desta fase é **metadata-only/read-only**: o router classifica a mensagem atual e injeta um bloco interno no turno do modelo para orientar handoff, approval packet e bloqueios de produção.

## Arquivos alterados

Runtime Hermes:

- `/opt/hermes/agent/lucas_task_router.py`
- `/opt/hermes/run_agent.py`
- `/opt/hermes/tests/agent/test_lucas_task_router_preflight.py`

Brain/router existente usado como fonte:

- `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/hermes_task_router.py`
- `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/test_hermes_task_router.py`

## Como funciona

1. `run_agent.py` chama `build_preflight_user_message(user_message)` no início de cada turno.
2. `agent/lucas_task_router.py` carrega, quando disponível, o classificador Brain em:
   - `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/hermes_task_router.py`
3. O classificador retorna JSON determinístico com rota, executor, action e approvals.
4. O runtime prepende ao turno um bloco interno:
   - `HERMES TASK ROUTER PREFLIGHT`
   - `decision_json`
   - política de não executar writes externos quando `preparar_approval_packet` ou `bloquear_por_aprovacao`
   - política de não vazar JSON/wrappers/job IDs no Telegram
5. O texto limpo do usuário é preservado para transcript quando não houver override prévio.

## Guardrails

- Fail-open: se o router não existir, falhar ou estiver desabilitado, o Hermes continua funcionando.
- Read-only: a integração só injeta metadata no prompt; não chama APIs externas, não executa ferramentas e não altera produção.
- Opt-out técnico:
  - `HERMES_LUCAS_TASK_ROUTER_DISABLED=true`
- Override de caminho:
  - `HERMES_LUCAS_TASK_ROUTER_PATH=/caminho/para/hermes_task_router.py`
- Sem restart ainda: código foi alterado em disco; o gateway/runtime em execução precisa de ativação controlada para carregar o novo módulo.

## Verificação executada

Comando principal:

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

Smoke test do preflight:

```text
lk-growth-content lk-growth preparar_approval_packet
contains_prefight True
```

Compilação:

```bash
PYTHONPYCACHEPREFIX=/tmp/hermes-pycache /opt/hermes/.venv/bin/python -m py_compile agent/lucas_task_router.py run_agent.py
```

Resultado: exit 0.

Scan focado de segredos nos arquivos alterados:

```text
secret_findings 0
```

## Resultado operacional

A próxima mensagem recebida pelo runtime **após restart controlado** terá metadata de roteamento antes do modelo decidir ferramentas/resposta. Isso reduz o risco de o Hermes Geral executar tarefas que deveriam virar:

- handoff para `lk-growth`, `mordomo`, `spiti`;
- approval packet local;
- bloqueio por aprovação.

## O que ainda não foi feito nesta fase

- Não houve restart de gateway/Docker.
- Não houve mutação de cron registry.
- Não houve bloqueio hard no dispatcher de ferramentas.
- Não houve alteração em Shopify/GMC/Klaviyo/Meta/WhatsApp/produção.

## Próximo passo recomendado — Fase 6B

Ativação controlada do runtime:

1. snapshot/checagem read-only dos PIDs/profiles atuais;
2. restart drain-aware do gateway principal, se Lucas aprovar;
3. verificação de saúde API/webhook/Telegram;
4. smoke test de mensagem LK Growth para confirmar metadata carregada sem vazamento ao usuário;
5. relatório de ativação/rollback.

## Rollback lógico

Sem mexer no código, é possível desabilitar no ambiente antes de restart:

```bash
HERMES_LUCAS_TASK_ROUTER_DISABLED=true
```

Rollback de código: remover import e bloco de preflight em `/opt/hermes/run_agent.py`, e remover `/opt/hermes/agent/lucas_task_router.py` + teste associado.
