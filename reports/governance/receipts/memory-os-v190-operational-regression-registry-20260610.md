# Receipt — Memory OS v1.90 Operational Regression Registry

Data UTC: 2026-06-10T15:44:47Z
Executor: Hermes Agent / default profile
Escopo: local/documental + testes

## Aprovação

Lucas aprovou: “Continuar memory 1.90”.

## O que foi feito

- Extendido `/opt/data/scripts/hermes_memory_os_context_intelligence.py` para v1.90.
- Adicionado `register_operational_regression` para registrar erros operacionais em JSONL sanitizado.
- Adicionado `build_regression_prevention_plan` para agrupar itens abertos por classe de erro e testes necessários.
- Adicionada sanitização de sintomas com `[REDACTED]` para tokens/secrets/payloads sensíveis.
- Adicionado fail-closed para auto-heal fora da allowlist local/documental: L2/L3 vira `approval_required` + `approval_packet_required`.
- Criados testes permanentes em `/opt/data/tests/test_memory_os_regression_registry_v190.py`.
- Bootstrap gerou `context-intelligence-latest.json` v1.90, `operational-regression-tests-v190.json` e `context-recall-tests-v190.json`.
- Atualizados docs canônicos: rotina Memory OS, MAPA de Operações e índice de rotinas.
- Criado relatório técnico: `reports/governance/memory-os-v190-operational-regression-registry-20260610.md`.

## Artefatos principais

- `scripts/hermes_memory_os_context_intelligence.py`
- `tests/test_memory_os_regression_registry_v190.py`
- `reports/memory-hygiene/context-intelligence-latest.json`
- `reports/memory-hygiene/operational-regression-tests-v190.json`
- `reports/memory-hygiene/context-recall-tests-v190.json`
- `areas/operacoes/rotinas/hermes-memory-os-v1.md`
- `areas/operacoes/MAPA.md`
- `empresa/rotinas/_index.md`

## Estado do bootstrap v1.90

- `version`: `v1.90`
- `status`: `ok`
- `current_states_written`: 10
- `context_packs_written`: 6
- `synthetic_recall_tests_written`: 10
- `deliveries` inclui `operational_regression_registry` e `regression_prevention_plan`
- `external_writes`: false
- `runtime_changes`: false
- CLI `--self-test` saudável: stdout `0` bytes

## Verificação final

Gates executados em 2026-06-10 após implementação, bootstrap, documentação e skill update:

- `test_memory_os_autoheal_v120.py`: 3 tests OK.
- `test_memory_os_context_intelligence_v130.py`: 4 tests OK.
- `test_memory_os_evidence_sufficiency_v140.py`: 4 tests OK.
- `test_memory_os_contradiction_ttl_v150.py`: 5 tests OK.
- `test_memory_os_decision_continuity_v160.py`: 5 tests OK.
- `test_memory_os_subagent_context_contract_v170.py`: 5 tests OK.
- `test_memory_os_selftest_silent_ok_v180.py`: 5 tests OK.
- `test_memory_os_regression_registry_v190.py`: 4 tests OK.
- CLI `--self-test`: `self_test_stdout_bytes=0`.
- Contradiction scan: `status=ok`, `finding_count=0`, `scanned_files=377`.
- Brain health: todas categorias `FAIL=0 WARN=0`; `All checks passed.`
- Operational docs guard: `scanned_files=386`, `fail_count=0`.
- Focused secret scan: `files_scanned=17`, `possible_secrets=0`.

## Guardrails

Não foram tocados:

- runtime/gateway/Docker/VPS/Traefik/SSH;
- crons live / Telegram delivery;
- provider externo/Mem0/Honcho;
- Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/banco;
- secrets/tokens/payloads sensíveis.
