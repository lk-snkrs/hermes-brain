# Receipt — Memory OS v1.40 Evidence & Sufficiency Layer

Data: 2026-06-10
Executor: Hermes Agent default profile
Escopo aprovado por Lucas: próximo pacote Memory OS após v1.30, local/documental + testes.

## Resultado

Implementado o pacote Memory OS v1.40 para tornar o Context Router mais conservador e verificável antes de respostas críticas.

## Mudanças principais

- `build_context_plan(query)` agora inclui:
  - `evidence_ladder`;
  - `context_sufficiency`;
  - `ttl_policy`;
  - `operational_error_classes`.
- Bootstrap do contexto agora gera `context-intelligence-latest.json` com `version=v1.40`.
- Testes sintéticos ampliados de 7 para 10 casos, incluindo:
  - `runtime_active_requires_live_evidence`;
  - `mesa_2of2_sufficient_with_ledger`;
  - `chat_summary_is_hint_not_truth`.
- Current state files passaram a declarar TTL/evidence ladder mínimo.
- Rotina e índices do Brain foram atualizados.

## Evidência de escopo

Não houve alteração em:

- runtime/gateway/processos;
- crons vivos/delivery;
- Docker/VPS/Traefik;
- providers/model routing;
- Telegram delivery;
- Shopify/Tiny/GMC/Klaviyo/WhatsApp/e-mail/banco;
- secrets/credenciais.

## Verificação

Executado em 2026-06-10T14:35Z–14:36Z:

- `/opt/hermes/.venv/bin/python /opt/data/tests/test_memory_os_autoheal_v120.py -v` → 3 testes OK.
- `/opt/hermes/.venv/bin/python /opt/data/tests/test_memory_os_context_intelligence_v130.py -v` → 4 testes OK.
- `/opt/hermes/.venv/bin/python /opt/data/tests/test_memory_os_evidence_sufficiency_v140.py -v` → 4 testes OK.
- `scripts/hermes_memory_os_context_intelligence.py --query 'Qual 2/2 do mesa coo?'` → `schema=v1.40`, `route=mesa_coo_decision_sequence`, `evidence_ladder[0]=decision_ledger`, `context_sufficiency.score=90`.
- Brain health → All checks passed.
- Operational docs guard → `fail_count=0`.
- Focused secret scan → `files_scanned=27 possible_secrets=0`.
