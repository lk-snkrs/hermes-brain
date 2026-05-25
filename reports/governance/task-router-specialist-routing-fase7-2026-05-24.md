# Task Router — Fase 7 Specialist Routing Coverage

Data: 2026-05-24T21:47:41+00:00

## Objetivo

Ampliar a cobertura do Task Router para reduzir execução por conveniência no Hermes Geral quando a tarefa tem dono claro na matriz operacional.

Escopo desta fatia:

- LK Growth analytics/SEO/CRO/GMC read-only → `lk-growth-analytics-readonly` / executor `lk-growth`.
- LK operações/cliente/estoque/preço/disponibilidade/reserva → `lk-ops-commerce-sensitive` / approval boundary.
- Tecnologia/Infra/Mission Control/Vercel/Docker/VPS → `tech-infra-mission-control` / approval packet quando produção/infra.

## Arquivos alterados

Runtime/Brain router:

- `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/hermes_task_router.py`
- `/opt/hermes/agent/lucas_task_router.py`

Regressões:

- `/opt/hermes/tests/agent/test_lucas_task_router_preflight.py`

## TDD

RED:

```bash
/opt/hermes/.venv/bin/python -m pytest tests/agent/test_lucas_task_router_preflight.py -q -o 'addopts='
```

Resultado RED observado:

- 3 falhas esperadas:
  - analytics LK caía em `general-research-content`.
  - LK ops sensível caía em `mordomo-personal-intake`.
  - tech/infra produção caía em `general-research-content`.

GREEN:

- Adicionadas rotas específicas antes das rotas genéricas para preservar precedência.
- `lk-growth-analytics-readonly` envia análise read-only para LK Growth e exige packet para correções/writes.
- `lk-ops-commerce-sensitive` bloqueia por aprovação quando envolve preço/disponibilidade/reserva/cliente/Tiny/Shopify.
- `tech-infra-mission-control` executa read-only/local no Hermes Geral, mas exige approval packet para produção, Docker/VPS/root/SSH/Traefik/secrets/write externo.

Resultado GREEN inicial:

- `7 passed` em `tests/agent/test_lucas_task_router_preflight.py`.

## Ativação sem restart para router Brain

Durante a Fase 7 foi identificado que o runtime fazia cache do módulo Brain por path. Isso poderia manter rotas antigas no processo vivo depois de editar `/opt/data/.../scripts/hermes_task_router.py`.

Correção adicional:

- `/opt/hermes/agent/lucas_task_router.py` agora calcula hash SHA-256 do arquivo Brain router e recarrega o módulo quando o conteúdo muda.
- O carregamento passou a compilar o source diretamente, evitando bytecode stale quando duas edições caem no mesmo segundo.
- Regressão nova: `test_lucas_task_router_reloads_brain_router_when_file_changes`.

Resultado GREEN atualizado:

- `8 passed` em `tests/agent/test_lucas_task_router_preflight.py`.

## Guardrails preservados

- Nenhum envio externo.
- Nenhum cron criado/alterado.
- Nenhum Docker/VPS/gateway/Traefik/volume/rede alterado.
- Nenhum write em Shopify/GMC/Klaviyo/Meta/WhatsApp/e-mail.
- Mudança limitada a classifier local/read-only e regressões.

## Próximos passos

Verificação final desta fatia:

```bash
/opt/hermes/.venv/bin/python -m pytest \
  tests/agent/test_lucas_task_router_preflight.py \
  tests/run_agent/test_run_agent.py::TestExecuteToolCalls::test_task_router_blocks_external_send_when_approval_packet_required \
  tests/run_agent/test_run_agent.py::TestExecuteToolCalls::test_task_router_allows_read_only_tool_during_approval_packet \
  tests/run_agent/test_run_agent.py::TestExecuteToolCalls::test_task_router_blocks_delegate_task_when_approval_packet_required \
  -q -o 'addopts='
/opt/hermes/.venv/bin/python -m py_compile \
  agent/lucas_task_router.py \
  /opt/data/hermes_bruno_ingest/hermes-brain/scripts/hermes_task_router.py
```

Resultado:

- `11 passed`.
- `py_compile` OK.
- Probe CLI do router para analytics LK retornou `route_id=lk-growth-analytics-readonly`, `executor=lk-growth`, `action=delegar_especialista`.
- Health checks read-only: API `127.0.0.1:8642/health` 200; webhook `127.0.0.1:8644/health` 200.

Status de ativação:

- Código-fonte e Brain router estão implementados/testados.
- Como `/opt/hermes/agent/lucas_task_router.py` mudou, um processo gateway que já importou a versão antiga precisa de restart controlado para observar o reload por hash. Nenhum restart foi feito nesta fatia.

Próximo passo seguro: Fase 7B — handoff packet limpo para especialistas, sem usar `delegate_task` como bypass de aprovação.
