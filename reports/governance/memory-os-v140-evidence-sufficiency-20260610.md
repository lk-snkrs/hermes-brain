# Memory OS v1.40 — Evidence & Sufficiency Layer

Data: 2026-06-10
Owner: LC Hermes / Hermes Brain Governance
Escopo: local/documental + testes; sem runtime, gateway, cron, provider, Telegram delivery ou writes externos.

## Objetivo

Reduzir respostas confiantes com contexto insuficiente adicionando uma camada explícita de hierarquia de evidência, score de suficiência e TTL por classe de fonte ao Context Router do Memory OS.

## Entregas

1. Evidence Ladder no roteador local:
   - `runtime_live` para perguntas de ativo/online/offline;
   - `decision_ledger` para Mesa COO N/M e decisões;
   - `fresh_health_report` para status do Memory OS;
   - `domain_live_source` para fatos vivos de negócio;
   - `current_state`, `receipts`, `brain_canonical`, `skills`, `session_history` e `chat_summary_or_prompt_memory` em ordem decrescente.

2. Context Sufficiency Score:
   - `must_verify_live_before_claim` para runtime/status ativo;
   - `answer_with_short_evidence` para Mesa COO com ledger;
   - `answer_with_fresh_report_status` para Memory OS;
   - `answer_context_only_or_verify_live_source` para domínios de negócio;
   - `label_assumptions` para contexto geral.

3. TTL policy:
   - runtime/status vivo: `fresh_required`;
   - política/guardrail: `durable`;
   - decisão: ledger/receipt necessário;
   - business live fact: fonte viva quando alegado;
   - chat summary: `stale_hint_only`.

4. Testes e fixtures:
   - `/opt/data/tests/test_memory_os_evidence_sufficiency_v140.py`;
   - `reports/memory-hygiene/context-recall-tests-v140.json`;
   - `reports/memory-hygiene/context-intelligence-latest.json` versão `v1.40`.

## Arquivos alterados/criados

- `/opt/data/scripts/hermes_memory_os_context_intelligence.py`
- `/opt/data/tests/test_memory_os_evidence_sufficiency_v140.py`
- `context/current/*.md`
- `context/packs/*.json`
- `reports/memory-hygiene/context-recall-tests-v130.json`
- `reports/memory-hygiene/context-recall-tests-v140.json`
- `reports/memory-hygiene/context-intelligence-latest.json`
- `areas/operacoes/rotinas/hermes-memory-os-v1.md`
- `areas/operacoes/MAPA.md`
- `empresa/rotinas/_index.md`

## Guardrails preservados

- Sem provider externo de memória.
- Sem alteração de gateway/runtime/crons/Telegram delivery.
- Sem Docker/VPS/Traefik/restart.
- Sem writes Shopify/Tiny/GMC/Klaviyo/WhatsApp/e-mail/banco.
- Sem secrets em relatório/receipt.

## Verificação

A verificação final deve rodar após este relatório e o receipt correspondente serem escritos:

- Memory OS v1.20 tests;
- Memory OS v1.30 tests;
- Memory OS v1.40 tests;
- CLI query `Qual 2/2 do mesa coo?` confirmando `evidence_ladder` e `context_sufficiency`;
- Brain health;
- operational docs guard;
- focused secret scan dos artefatos v1.40.
