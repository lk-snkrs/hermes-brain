# Reminder OS ledger

Este arquivo documenta o schema. Os eventos ativos ficam em `reminders.jsonl`.

## Schema v0

Allowed statuses: `open`, `waiting_lucas`, `waiting_event`, `scheduled_check`, `kanban_tracked`, `done`, `expired`.

Allowed severities: `low`, `medium`, `high`.

Campos mínimos:

- `id`: identificador estável, ex. `rem-20260612-001`.
- `title`: título curto do loop.
- `owner`: dono lógico/agente/profile.
- `status`: `open`, `waiting_lucas`, `waiting_event`, `scheduled_check`, `kanban_tracked`, `done`, `expired`.
- `next_action`: próxima ação concreta.

Campos recomendados:

- `source`: conversa, Mesa COO, Kanban, Memory OS, Brain, cron, especialista.
- `severity`: `low`, `medium`, `high`.
- `due_at`: ISO UTC quando houver prazo.
- `next_review_at`: ISO UTC para retomada.
- `evidence`: caminho Brain/Kanban/sessão/relatório.
- `risk`: o que acontece se esquecer.
- `created_at`, `updated_at`: ISO UTC.

## Regras

Exemplo válido:

```json
{"id":"rem-20260612-001","title":"Retomar PRD Reminder OS","owner":"Hermes Geral","status":"scheduled_check","severity":"medium","next_action":"Executar Fase 1 local","next_review_at":"2026-06-12T16:00:00Z","evidence":"areas/operacoes/prds/reminder-os-prd-v1-2026-06-12.md"}
```

Exemplo inválido:

```json
{"title":"Pendente sem dono","status":"urgent"}
```

Motivo: falta `id`, `owner`, `next_action`; `urgent` não é status permitido.

- Nunca salvar segredos, tokens, PII desnecessária ou dumps de fonte viva.
- Use ponteiro para fonte/evidência, não copie dados grandes.
- Fechar (`done`) ou expirar (`expired`) quando o loop não precisar mais voltar.
