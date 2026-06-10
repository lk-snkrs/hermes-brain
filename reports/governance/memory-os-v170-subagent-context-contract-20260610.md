# Memory OS v1.70 — Subagent Context Contract v2

Data: 2026-06-10
Escopo aprovado: local/documental + testes.

## Objetivo

Padronizar o contexto entregue a subagentes para reduzir erro por:

- prompt gigante ou fontes demais;
- ausência de `context/current/*.md`;
- chat summary tratado como verdade;
- claim runtime/online/offline sem evidência viva;
- subagente executando ação A3/A4 sem approval packet;
- resposta sem evidência, incerteza ou ações não tomadas.

## Entregas

1. Contrato v2 para subagente
   - `build_subagent_context_contract(pack, task, risk_level)`.
   - Schema: `hermes.memory_os.subagent_context_contract.v2`.
   - Versão: `v1.70`.
   - Orçamento: máximo 8 fontes, 2500 tokens hint, até 3 receipts e 2 current files.

2. Validação fail-closed
   - `validate_subagent_context_contract(contract)`.
   - Bloqueia falta de guardrails, excesso de fontes, ausência de current state, falta de retorno de evidências, A3/A4 sem approval packet e intenção externa sem escopo.

3. Handoff packet
   - `create_subagent_handoff_packet(contract)`.
   - Truth policy: `chat_summary=hint_only`, runtime exige live evidence, fato vivo de negócio exige fonte viva.
   - Stop conditions: fonte obrigatória ausente, write externo sem aprovação, runtime claim sem evidência, pedido de secret/token.

4. Fixtures/reports
   - `reports/memory-hygiene/subagent-context-contract-tests-v170.json`.
   - `reports/memory-hygiene/context-recall-tests-v170.json`.
   - `reports/memory-hygiene/context-intelligence-latest.json` versão `v1.70`.

5. Testes permanentes
   - `/opt/data/tests/test_memory_os_subagent_context_contract_v170.py`.
   - Cobre contrato budgetado/guardrailed, validação de overbudget/guardrails, A3/A4 sem approval packet, handoff sem raw chat summary e bootstrap v1.70.

## Estado do bootstrap

- `version`: `v1.70`.
- `status`: `ok`.
- `current_states_written`: 10.
- `context_packs_written`: 6.
- `synthetic_recall_tests_written`: 10.
- `deliveries` inclui `subagent_context_contract_v2` e `subagent_handoff_packet`.
- `external_writes`: false.
- `runtime_changes`: false.

## Guardrails preservados

- Sem runtime/gateway/Docker/VPS/Traefik/SSH.
- Sem cron live ou Telegram delivery change.
- Sem provider externo/Mem0/Honcho.
- Sem Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/banco.
- Sem secrets/tokens/payloads sensíveis.

## Verificação

Verificação final registrada no receipt correspondente após reexecução dos gates.
