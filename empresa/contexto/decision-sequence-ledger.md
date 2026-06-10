# Decision Sequence Ledger

Status: canônico local v0.2 / Memory OS v1.60
Criado em: 2026-06-10T14:13:27Z
Atualizado em: 2026-06-10T15:07:05Z
Escopo: persistir sequências de decisão da Mesa COO e fluxos similares antes de enviar apenas `Decisão 1/N` no Telegram.

## Problema

A Mesa COO envia uma decisão por vez (`1/N`), mas até agora a fila completa precisava ser reconstruída por sessão, daily, receipts e handoffs. Isso falha quando Lucas pergunta `qual 2/2?`, responde `Não fazer`, `Fazer`, `aprovado` ou `já fiz`.

## Regra central

Antes de enviar `Decisão 1/N`, o gerador deve registrar localmente a sequência completa em JSONL append-only. O Telegram continua recebendo um card por vez; o Brain passa a saber deterministicamente qual é o próximo item.

## Caminhos

- Eventos machine-readable: `empresa/contexto/decision-sequences/YYYY-MM-DD.jsonl`
- Resumo humano opcional: `empresa/contexto/decision-sequences/YYYY-MM-DD.md`
- Handoffs materiais continuam em: `empresa/contexto/handoffs/` e `empresa/contexto/handoff-ledger.md`

## Evento mínimo

```json
{
  "schema": "hermes.decision_sequence.v1.60",
  "event_id": "deterministic-or-uuid",
  "sequence_id": "mesa_coo:YYYY-MM-DD:<source>",
  "decision_id": "mesa_coo:YYYY-MM-DD:1ofN:<slug>",
  "created_at_utc": "...",
  "event_type": "sequence_created|decision_sent|lucas_response|action_started|receipt_created|sequence_closed",
  "index": 1,
  "total": 2,
  "domain": "LK|Zipper|SPITI|Hermes|Mordomo",
  "title": "...",
  "safe_action": "...",
  "approval_scope": "...",
  "blocked_actions": ["..."],
  "evidence_paths": ["..."],
  "response_value": "fazer|nao_fazer|agendar|outro|null",
  "status_after": "pending_send|sent|approved_preview|declined|snoozed|done|blocked|superseded",
  "next_decision_id": "..."
}
```

## Semântica de respostas Lucas

- `Não fazer`: marcar somente o item aberto como `declined`, registrar `do_not_do`, avançar para o próximo item aberto ou fechar sequência.
- `Fazer`: executar apenas o `safe_action` do card. Para A3/A4, isso significa preparar preview/approval packet, não produção.
- `Aprovado`: preservar o escopo do card anterior; não vira autorização genérica para runtime/externo.
- `Já fiz`: verificar fonte local proporcional, registrar `done` quando evidência existir e avançar.
- Pergunta `qual N/M?`: ler este ledger primeiro; fallback para session_search/daily/handoff só se ledger estiver ausente.

## Memory OS v1.60

- Helper local: `/opt/data/scripts/hermes_memory_os_context_intelligence.py`.
- Funções canônicas: `write_decision_sequence_ledger`, `resolve_decision_sequence_query`, `record_lucas_decision_response`, `approval_scope_gate`, `load_decision_sequence_state`.
- Fixture/regressão: `reports/memory-hygiene/decision-continuity-tests-v160.json`.
- Teste permanente: `/opt/data/tests/test_memory_os_decision_continuity_v160.py`.
- Gate obrigatório: antes de agir sobre `APROVO`/`Fazer`, rodar mentalmente ou programaticamente o equivalente de `approval_scope_gate`; se o intended action não estiver no escopo do item, bloquear.

## Guardrails

- Ledger local não autoriza produção.
- Não guardar secrets, tokens, payloads brutos sensíveis ou dumps de banco/API.
- Telegram só recebe próxima decisão, bloqueio, exceção, falha ou fechamento curto.
- Handoffs materiais devem referenciar `sequence_id` e `decision_id`.
