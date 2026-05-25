# Task Router Técnico — Fase 6C Dispatcher Guardrail

Data: 2026-05-24
Status: implementado e ativo no runtime atual

## Objetivo

Adicionar bloqueio duro no dispatcher de ferramentas quando o Task Router classificar o turno como aprovação/handoff. O objetivo é impedir que o Hermes Geral execute contato externo, publicação ou produção quando a rota exige preview/approval packet primeiro.

## Escopo implementado

Arquivos de runtime:

- `/opt/hermes/agent/lucas_task_router.py`
- `/opt/hermes/run_agent.py`

Testes:

- `/opt/hermes/tests/run_agent/test_run_agent.py`
- `/opt/hermes/tests/agent/test_lucas_task_router_preflight.py`

## Comportamento

Quando a decisão atual tiver `action=preparar_approval_packet`, `action=bloquear_por_aprovacao`, `handoff_required=true` ou executor diferente de `hermes-geral`, o dispatcher passa a bloquear ferramentas de side effect externo/produção.

Bloqueios cobertos:

- `send_message`
- `cronjob`
- `delegate_task`
- browser actions interativas (`browser_click`, `browser_type`, `browser_press`)
- `terminal` quando o comando parecer produção/externo, por exemplo POST/PUT/PATCH/DELETE via curl, Docker restart/down/up, SSH, Shopify/Klaviyo, deploys
- `execute_code` quando o código indicar chamadas externas mutantes ou integrações sensíveis

Continua permitido para montar evidência/preview local:

- leitura de arquivos
- busca local
- web search/extract
- session search
- browser snapshot/console/get images
- documentação local segura

## UX esperada

O bloqueio aparece para o modelo como resultado sintético de ferramenta, não como mensagem crua ao Lucas. O modelo deve responder de forma limpa:

- dizer que a ação exige aprovação explícita;
- preparar evidência/preview/rollback local;
- não mostrar JSON, wrappers, job IDs ou metadata interna.

## Verificação executada

Comando:

```bash
/opt/hermes/.venv/bin/python -m pytest \
  tests/agent/test_lucas_task_router_preflight.py \
  tests/cron/test_scheduler.py::TestDeliverResultWrapping \
  tests/run_agent/test_run_agent.py::TestExecuteToolCalls::test_task_router_blocks_external_send_when_approval_packet_required \
  tests/run_agent/test_run_agent.py::TestExecuteToolCalls::test_task_router_blocks_delegate_task_when_approval_packet_required \
  tests/run_agent/test_run_agent.py::TestExecuteToolCalls::test_task_router_allows_read_only_tool_during_approval_packet \
  -q -o 'addopts=' && \
python3 /opt/data/hermes_bruno_ingest/hermes-brain/scripts/test_hermes_task_router.py
```

Resultado:

```text
19 passed, 1 warning
Ran 5 tests
OK
```

Compilação:

```bash
PYTHONPYCACHEPREFIX=/tmp/hermes-pycache /opt/hermes/.venv/bin/python -m py_compile agent/lucas_task_router.py run_agent.py
```

Resultado: exit 0.

Health checks depois da ativação:

```text
http://127.0.0.1:8642/health 200
http://127.0.0.1:8644/health 200
```

Processos atuais conferidos:

```text
Gateway principal e perfis lk-growth, mordomo e spiti ativos.
PIDs atuais: 6, 236, 239, 242.
```

Secret scan focado:

- arquivos runtime/router: 0 achados;
- segmento novo de testes Task Router: 0 achados;
- `tests/run_agent/test_run_agent.py` completo contém achados antigos/fake fixtures fora do segmento alterado.

## Limites atuais

- O guardrail é heurístico para `terminal`/`execute_code`; ele bloqueia padrões claros de produção/externo, mas não substitui aprovação humana para comandos ambíguos.
- Não executa handoff automático real para specialist profiles; apenas impede side effects e orienta approval/handoff.
- Não altera registry de cron, Shopify, GMC, Klaviyo, Meta, WhatsApp ou produção.

## Rollback

Rollback lógico sem remover código:

```bash
HERMES_LUCAS_TASK_ROUTER_GUARDRAIL_DISABLED=true
```

Rollback completo de código:

1. remover chamadas a `_task_router_tool_block_result` no dispatcher de `/opt/hermes/run_agent.py`;
2. remover imports `task_router_tool_block_message` e `task_router_synthetic_block_result`;
3. remover funções de guardrail em `/opt/hermes/agent/lucas_task_router.py`;
4. rodar testes de regressão;
5. restart controlado do gateway.

## Próximo passo recomendado — Fase 6D

Transformar o bloqueio em UX de decisão 1/N:

1. quando bloquear, gerar approval packet curto;
2. oferecer botões `Fazer`, `Não fazer`, `Agendar`, `Outro` apenas quando houver ação externa clara;
3. garantir que o texto técnico interno nunca apareça no Telegram;
4. adicionar teste end-to-end de transcript limpo + resposta limpa.
