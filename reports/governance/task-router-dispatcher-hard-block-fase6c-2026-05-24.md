# Task Router Técnico v1 — Fase 6C Dispatcher Hard Block

Data: 2026-05-24
Status: implementado em código e verificado; pendente de restart controlado para ativar a última alteração no processo vivo

## Objetivo

Transformar o Task Router de orientação interna em bloqueio hard no dispatcher de ferramentas para turnos em modo `preparar_approval_packet`, `bloquear_por_aprovacao` ou handoff especialista.

## Mudança feita

Arquivo alterado:

- `/opt/hermes/agent/lucas_task_router.py`
- `/opt/hermes/tests/run_agent/test_run_agent.py`

O guardrail já bloqueava ferramentas externas/produção em rotas com approval/handoff, incluindo:

- `send_message`
- `cronjob`
- interações browser mutantes (`browser_click`, `browser_type`, `browser_press`)
- `terminal` com padrões de produção/externo (`curl POST/PUT/PATCH/DELETE`, `shopify`, `klaviyo`, `vercel --prod`, `kubectl apply/delete/rollout`, `terraform apply/destroy`, `docker restart/up/down/rm`, `ssh`)
- `execute_code` com chamadas externas/produção (`requests/httpx/urllib` write, `smtplib`, `boto3`, `googleapiclient`, `shopify`, `klaviyo`)

Nesta fase foi fechado um gap: `delegate_task` também passa a ser bloqueado quando a rota exige approval/handoff. Motivo: subagentes podem herdar ferramentas amplas e executar writes externos sem carregar o mesmo contexto de aprovação do turno principal.

## TDD

Teste RED criado antes da alteração:

```bash
/opt/hermes/.venv/bin/python -m pytest tests/run_agent/test_run_agent.py::TestExecuteToolCalls::test_task_router_blocks_delegate_task_when_approval_packet_required -q -o 'addopts='
```

Resultado RED esperado:

```text
FAILED ... Expected '_dispatch_delegate_task' to not have been called. Called 1 times.
```

Implementação mínima:

- adicionar `delegate_task` a `_EXTERNAL_SIDE_EFFECT_TOOLS` em `agent/lucas_task_router.py`.

Resultado GREEN:

```text
1 passed
```

## Regressão executada

Comando:

```bash
/opt/hermes/.venv/bin/python -m pytest \
  tests/agent/test_lucas_task_router_preflight.py \
  tests/run_agent/test_run_agent.py::TestExecuteToolCalls::test_task_router_blocks_external_send_when_approval_packet_required \
  tests/run_agent/test_run_agent.py::TestExecuteToolCalls::test_task_router_allows_read_only_tool_during_approval_packet \
  tests/run_agent/test_run_agent.py::TestExecuteToolCalls::test_task_router_blocks_delegate_task_when_approval_packet_required \
  tests/cron/test_scheduler.py::TestDeliverResultWrapping \
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
PYTHONPYCACHEPREFIX=/tmp/hermes-pycache /opt/hermes/.venv/bin/python -m py_compile agent/lucas_task_router.py run_agent.py tests/run_agent/test_run_agent.py
```

Resultado: exit 0.

## Secret scan

Scan focado dos arquivos tocados retornou achados em fixtures antigas de teste (`tests/run_agent/test_run_agent.py`) que já estavam mascaradas/redigidas em output e não foram adicionadas pela mudança desta fase. Nenhum segredo foi incluído na linha nova de `delegate_task`.

## Estado operacional

- Código em disco: atualizado.
- Testes: passando.
- Última mudança (`delegate_task` no hard block): requer restart controlado do gateway principal para carregar o módulo novo no processo vivo.
- Sem alteração em Shopify/GMC/Klaviyo/Meta/WhatsApp/produção externa.

## Rollback

Remover `delegate_task` de `_EXTERNAL_SIDE_EFFECT_TOOLS` em `/opt/hermes/agent/lucas_task_router.py` e reverter o teste novo associado em `/opt/hermes/tests/run_agent/test_run_agent.py`.

## Próximo passo

Ativar via restart controlado do gateway principal e verificar:

1. API `/health`;
2. webhook `/health`;
3. Telegram conectado;
4. mensagem real pós-restart sem vazamento de metadata técnica;
5. regressão curta do Task Router.
