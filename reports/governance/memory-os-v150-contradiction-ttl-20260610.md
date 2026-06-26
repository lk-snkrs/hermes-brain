# Memory OS v1.50 — Contradiction Detector + Current State TTL Enforcement

Data: 2026-06-10
Escopo aprovado: local/documental + testes.

## Objetivo

Reduzir erro operacional causado por contexto contraditório ou evidência vencida, especialmente para perguntas como:

- “está ativo/online/offline?”
- “status atual do Memory OS?”
- preço/estoque/disponibilidade/status vivo
- conflitos entre current state, runtime docs e reports

## Entregas

1. Detector de contradições explícitas
   - Função: `detect_context_contradictions(brain)`.
   - Lê marcadores sanitizados `memory-os-claim` em current/runtime/reports.
   - Agrupa por `subject + claim_type` e bloqueia conflitos em claims voláteis, por exemplo `runtime_status=active` vs `runtime_status=offline`.
   - Evita inferência fuzzy para não transformar guardrails como “não prova runtime ativo” em falso positivo.

2. TTL enforcement
   - Função: `enforce_ttl_for_plan(plan, evidence)`.
   - Bloqueia claim de runtime ativo quando `runtime_readonly_evidence` está ausente ou vencida.
   - Limites atuais:
     - `runtime_readonly_evidence`: 15 minutos.
     - `domain_live_source`: 30 minutos.
     - `health_report`: 180 minutos.
     - `current_state_pointer`: 10080 minutos.

3. Bootstrap v1.50
   - Script: `/opt/data/scripts/hermes_memory_os_context_intelligence.py`.
   - Report principal: `reports/memory-hygiene/context-intelligence-latest.json`.
   - Report de contradições: `reports/memory-hygiene/context-contradictions-latest.json`.
   - Fixture TTL: `reports/memory-hygiene/context-ttl-tests-v150.json`.
   - Recall v1.50: `reports/memory-hygiene/context-recall-tests-v150.json`.

4. Testes permanentes
   - Arquivo: `/opt/data/tests/test_memory_os_contradiction_ttl_v150.py`.
   - Cobertura:
     - conflito `active/offline` bloqueia current claim;
     - context pointer não gera falso positivo;
     - runtime stale bloqueia claim ativo;
     - runtime fresco permite claim;
     - bootstrap grava versão v1.50 e fixture TTL.

## Estado gerado pelo bootstrap

- `version`: `v1.50`.
- `status`: `ok`.
- `current_states_written`: 10.
- `context_packs_written`: 6.
- `synthetic_recall_tests_written`: 10.
- `contradiction_scan.status`: `ok`.
- `contradiction_scan.finding_count`: 0.
- `contradiction_scan.scanned_files`: 356 no report principal; 358 no report dedicado após escrita dos artefatos finais.
- `external_writes`: false.
- `runtime_changes`: false.

## Guardrails preservados

- Sem Docker/VPS/Traefik/SSH/gateway/runtime/provider/cron live changes.
- Sem mudança em entrega Telegram.
- Sem Mem0/Honcho/provider externo.
- Sem writes externos em Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/banco.
- Sem secrets impressos ou persistidos.
- Chat summary continua apenas pista, não verdade final.

## Regra operacional nova

Antes de responder com certeza sobre status atual volátil:

1. usar o router para obter `answer_mode`;
2. aplicar `enforce_ttl_for_plan` com evidência disponível;
3. se `can_answer_claim=false`, responder que precisa de evidência fresca e não afirmar o status;
4. se houver contradição em `context-contradictions-latest.json`, bloquear o claim e consultar a fonte de maior tier.

## Artefatos alterados/criados

- `/opt/data/scripts/hermes_memory_os_context_intelligence.py`
- `/opt/data/tests/test_memory_os_contradiction_ttl_v150.py`
- `/opt/data/tests/test_memory_os_evidence_sufficiency_v140.py`
- `/opt/data/hermes_bruno_ingest/hermes-brain/context/current/*.md`
- `/opt/data/hermes_bruno_ingest/hermes-brain/context/packs/*.json`
- `/opt/data/hermes_bruno_ingest/hermes-brain/reports/memory-hygiene/context-intelligence-latest.json`
- `/opt/data/hermes_bruno_ingest/hermes-brain/reports/memory-hygiene/context-contradictions-latest.json`
- `/opt/data/hermes_bruno_ingest/hermes-brain/reports/memory-hygiene/context-ttl-tests-v150.json`
- `/opt/data/hermes_bruno_ingest/hermes-brain/reports/memory-hygiene/context-recall-tests-v150.json`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/rotinas/hermes-memory-os-v1.md`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/MAPA.md`
- `/opt/data/hermes_bruno_ingest/hermes-brain/empresa/rotinas/_index.md`

## Verificação

Verificação final registrada no receipt correspondente após reexecução dos gates.
