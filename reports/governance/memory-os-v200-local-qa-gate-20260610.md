# Memory OS v2.0 — Local QA Gate

Data: 2026-06-10
Escopo aprovado: local/documental + testes.

## Objetivo

Consolidar a verificação completa do Memory OS em um plano local determinístico, para evitar fechamento de pacote com checklist manual incompleto ou claim de sucesso sem evidência fresca.

## Entregas

1. Plano de QA local
   - `build_memory_os_qa_gate_plan(brain, tests_dir)`.
   - Retorna JSON com todos os checks necessários para Memory OS v1.20-v2.0.
   - Não executa comandos; é `plan_only`.

2. Validação de segurança
   - `validate_memory_os_qa_gate_plan(plan)`.
   - Bloqueia comandos com sinais de runtime/rede/writes externos: Docker, SSH, curl, wget, kubectl, systemctl, restart, Telegram, provedores, etc.
   - Plano declara `local_only=true`, `external_writes=false`, `runtime_changes=false`.

3. CLI plan-only
   - `--qa-plan` imprime JSON do plano v2.0 sem executar checks.
   - Não há claim de sucesso; sucesso exige rodada fresca real dos comandos.

4. Fixture v2.0
   - `reports/memory-hygiene/local-qa-gate-v200.json`.
   - `reports/memory-hygiene/context-recall-tests-v200.json`.
   - `context-intelligence-latest.json` versão `v2.0`.

## Checks cobertos pelo plano

- `test_memory_os_autoheal_v120`
- `test_memory_os_context_intelligence_v130`
- `test_memory_os_evidence_sufficiency_v140`
- `test_memory_os_contradiction_ttl_v150`
- `test_memory_os_decision_continuity_v160`
- `test_memory_os_subagent_context_contract_v170`
- `test_memory_os_selftest_silent_ok_v180`
- `test_memory_os_regression_registry_v190`
- `test_memory_os_local_qa_gate_v200`
- `bootstrap_context_intelligence`
- `self_test_silent_ok`
- `contradiction_scan`
- `brain_health_check`
- `operational_docs_guard`
- `focused_secret_scan`

## Testes permanentes

- `/opt/data/tests/test_memory_os_local_qa_gate_v200.py`

Cobertura:

- completude do plano;
- validação fail-closed contra comandos runtime/network;
- formatação plan-only sem claim de execução;
- bootstrap v2.0;
- CLI `--qa-plan` JSON, sem execução.

## Guardrails

- Não executa runtime/gateway/provider/Docker/VPS/Telegram/cron/writes externos.
- Não agenda cron.
- Não altera delivery Telegram.
- Não imprime secrets/tokens/payloads sensíveis.
- É plano/contrato local + testes.

## Verificação

Verificação final registrada no receipt correspondente após reexecução dos gates.
