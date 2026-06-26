# Memory OS v1.80 — Silent-OK Self-Test Contract

Data: 2026-06-10
Escopo aprovado: local/documental + testes.

## Objetivo

Criar um contrato de self-test diário/no_agent para o Memory OS que valide saúde local sem gerar ruído para Lucas quando tudo está verde.

## Entregas

1. Self-test local
   - `run_memory_os_self_test(brain)`.
   - Schema: `hermes.memory_os.self_test.v1.80`.
   - Verifica artefatos críticos do Memory OS sem rede, runtime, cron, Telegram ou write externo.

2. Contrato de stdout silent-OK
   - `format_memory_os_self_test_stdout(result)`.
   - `status=ok` retorna string vazia.
   - `status=attention` retorna alerta sanitizado/actionable.

3. CLI
   - `/opt/hermes/.venv/bin/python /opt/data/scripts/hermes_memory_os_context_intelligence.py --self-test --brain <brain>`.
   - Em ambiente saudável: stdout exatamente vazio.

4. Fixture
   - `reports/memory-hygiene/self-test-contract-v180.json`.
   - Declara checks e contrato `silent_ok`.

5. Bootstrap
   - `context-intelligence-latest.json` versão `v1.80`.
   - `deliveries` inclui `silent_ok_self_test`.
   - `external_writes=false` e `runtime_changes=false`.

## Checks atuais

- `context_intelligence_latest`
- `contradiction_scan_ok`
- `ttl_fixture`
- `decision_continuity_fixture`
- `subagent_contract_fixture`
- `recall_fixture`
- `current_state_memory_os`

## Testes permanentes

- `/opt/data/tests/test_memory_os_selftest_silent_ok_v180.py`

Cobertura:

- self-test saudável retorna `status=ok` e `alert_text=''`;
- fixture ausente gera `status=attention` e alerta acionável;
- formatador retorna stdout vazio no OK;
- CLI `--self-test` é silencioso quando saudável;
- bootstrap escreve `self-test-contract-v180.json` e report v1.80.

## Guardrails

- Não agenda cron.
- Não altera delivery Telegram.
- Não muda runtime, gateway, Docker, VPS, Traefik, SSH.
- Não ativa provider externo/Mem0/Honcho.
- Não toca Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/banco.
- Não imprime secrets/tokens/payloads sensíveis.

## Verificação

Verificação final registrada no receipt correspondente após reexecução dos gates.
