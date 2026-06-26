# Memory OS v1.90 — Operational Regression Registry

Data: 2026-06-10
Escopo aprovado: local/documental + testes.

## Objetivo

Criar uma camada local para transformar erros operacionais em regressões auditáveis, com teste preventivo e plano de prevenção, sem depender de memória de chat, alerta solto ou correção manual não registrada.

## Entregas

1. Registry append-only
   - `register_operational_regression(registry_path, error_class, symptom, prevention_test, evidence_paths, safe_autoheal, created_at_utc)`.
   - Escreve JSONL sanitizado.
   - Nunca executa a correção; só registra contrato e risco.

2. Sanitização
   - sintomas passam por `sanitize_operational_text`.
   - padrões de token/secret/password/api key são substituídos por `[REDACTED]`.

3. Classificação fail-closed
   - L1: auto-heal local/documental permitido apenas se estiver na allowlist.
   - L2/L3: runtime, Docker, gateway, provider, Telegram, cron, VPS, SSH, Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/banco exigem `approval_packet_required`.

4. Plano de prevenção
   - `build_regression_prevention_plan(registry_path)`.
   - Agrupa itens abertos por `error_class`.
   - Lista `required_tests` e itens que exigem aprovação.

5. Bootstrap v1.90
   - `context-intelligence-latest.json` versão `v1.90`.
   - `deliveries` inclui `operational_regression_registry` e `regression_prevention_plan`.
   - fixture `operational-regression-tests-v190.json`.
   - recall `context-recall-tests-v190.json`.

## Error classes iniciais

- `stale_runtime_claim`
- `decision_sequence_skip`
- `live_business_fact_without_source`
- `chat_summary_as_truth`
- `approval_scope_drift`
- `runtime_restart_needed`

## Testes permanentes

- `/opt/data/tests/test_memory_os_regression_registry_v190.py`

Cobertura:

- registro JSONL sanitizado;
- bloqueio L2/L3 com `approval_packet_required`;
- plano agrupado por classe de erro;
- bootstrap escreve fixture v1.90 e report v1.90.

## Guardrails

- Não executa auto-heal real.
- Não agenda cron.
- Não muda delivery Telegram.
- Não altera runtime, gateway, Docker, VPS, Traefik, SSH.
- Não ativa provider externo/Mem0/Honcho.
- Não toca Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/banco.
- Não imprime secrets/tokens/payloads sensíveis.

## Verificação

Verificação final registrada no receipt correspondente após reexecução dos gates.
