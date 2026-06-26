# Task Router — Fase 7B: Handoff packets limpos para especialistas

Data: 2026-05-24
Status: implementado e verificado localmente

## Objetivo

Garantir que rotas com especialista ou approval boundary produzam handoff/approval packet limpo para Lucas e para o domínio dono, sem vazar metadata técnica e sem permitir que `delegate_task` seja usado como bypass de aprovação.

## Mudanças implementadas

### Runtime

Arquivo: `/opt/hermes/agent/lucas_task_router.py`

- Adicionado `build_specialist_handoff_packet()`.
- Packet gerado com campos humanos:
  - Destino
  - Por quê
  - Pedido limpo
  - Evidências
  - Preview
  - Risco
  - Bloqueios
  - Permitido sem nova aprovação
  - Rollback
  - Decisão
- Packet omite `decision_json`, `route_id`, raw preflight metadata, job IDs e boilerplate técnico.
- Preflight agora injeta contrato interno de handoff packet quando a decisão exige handoff, executor especialista ou action de approval.
- Resultado sintético do guardrail de dispatcher agora inclui `handoff_packet` limpo para orientar a resposta do modelo quando uma ferramenta mutante é bloqueada.
- Mensagem de bloqueio deixou de expor `route_id` e passa a mencionar o destino humano/especialista.

### Anti-bypass

- `delegate_task` permanece classificado como ferramenta com potencial side-effect em rotas de handoff/approval.
- Em modo approval/handoff, o dispatcher bloqueia `delegate_task` antes da chamada.
- O bloqueio orienta a preparar evidência, preview e rollback localmente.
- Ferramentas read-only continuam liberadas para coletar evidências e preparar packet.

## Testes adicionados

Arquivo: `/opt/hermes/tests/agent/test_lucas_task_router_preflight.py`

- `test_specialist_handoff_packet_is_clean_and_actionable`
  - valida packet com Destino/Pedido/Evidências/Preview/Bloqueios/Rollback;
  - garante ausência de `delegate_task`, `decision_json`, `route_id` e ID de rota.

- `test_delegate_task_block_returns_handoff_packet_instead_of_bypassing_approval`
  - valida que uma tentativa de delegar publicação Shopify em rota LK Growth é bloqueada;
  - valida que o resultado inclui `handoff_packet` limpo;
  - valida que o ID de rota não vaza.

## Verificação executada

```bash
pytest tests/agent/test_lucas_task_router_preflight.py -q
# 10 passed

pytest tests/run_agent/test_run_agent.py::TestExecuteToolCalls::test_task_router_blocks_external_send_when_approval_packet_required \
       tests/run_agent/test_run_agent.py::TestExecuteToolCalls::test_task_router_allows_read_only_tool_during_approval_packet \
       tests/run_agent/test_run_agent.py::TestExecuteToolCalls::test_task_router_blocks_delegate_task_when_approval_packet_required -q
# 3 passed

pytest tests/agent/test_lucas_task_router_preflight.py \
       tests/run_agent/test_run_agent.py::TestExecuteToolCalls::test_task_router_blocks_external_send_when_approval_packet_required \
       tests/run_agent/test_run_agent.py::TestExecuteToolCalls::test_task_router_allows_read_only_tool_during_approval_packet \
       tests/run_agent/test_run_agent.py::TestExecuteToolCalls::test_task_router_blocks_delegate_task_when_approval_packet_required -q
# 13 passed

python -m py_compile agent/lucas_task_router.py
# OK

curl -fsS http://127.0.0.1:8642/health
# {"status":"ok","platform":"hermes-agent"}

curl -fsS http://127.0.0.1:8644/health
# {"status":"ok","platform":"webhook"}
```

Observação: a tentativa inicial de rodar regressões do dispatcher usou nome de classe errado (`TestAIAgentToolExecution`) e retornou exit code 5 sem coletar testes; o comando foi corrigido para `TestExecuteToolCalls` e passou.

## Guardrails preservados

- Nenhum write externo executado.
- Nenhuma publicação Shopify/GMC/Klaviyo/Meta feita.
- Nenhum contato com cliente/WhatsApp/e-mail feito.
- Nenhum cron alterado.
- Nenhum Docker/VPS/Traefik/volume/network alterado.
- Nenhum restart de gateway executado nesta fase.

## Ativação runtime

As mudanças em `/opt/hermes/agent/lucas_task_router.py` exigem restart controlado do gateway para plena ativação no processo vivo. API e webhook estão saudáveis no momento da verificação, mas o código novo só é carregado pelo runtime após reinício do processo que usa esse módulo.

## Próximo passo recomendado

Se Lucas quiser aplicar agora no Telegram/gateway vivo: executar restart controlado com verificação de processo, API, webhook e logs de Telegram. Caso contrário, manter como patch validado aguardando janela de ativação.
