# Receipt — Handoff Kanban — Lululemon Define Jacket collection

Data: 20260625T195632Z
Origem: `[LK] Growth`
Destino: `lk-shopify`
Board: `lk-growth-ops`
Task ID: `t_2443c1f6`

## Escopo

Validar/criar/ativar collection canônica `/collections/lululemon-define-jacket` usando apenas produtos Lululemon Define ativos já existentes.

## Guardrails

- Não consultar/alterar estoque, Tiny ou inventory.
- Não alterar preço.
- Não alterar campanhas, GMC, Klaviyo ou checkout.
- Não alterar SEO title/meta ou descrição editorial sem aprovação separada.
- Não criar produto novo.

## Handoff

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/handoffs/lululemon-define-jacket-surface-handoff-20260625T195532Z.md`

## Dispatch

Criado e despachado via Kanban. Worker spawnado em:
`/opt/data/kanban/boards/lk-growth-ops/workspaces/t_2443c1f6`

Status no momento do receipt:
`{'id': 't_2443c1f6', 'title': '[LK Shopify] Criar/validar collection canônica Lululemon Define Jacket', 'body': 'Aprovado por Lucas: validar/criar/ativar collection canônica Lululemon Define Jacket.\n\nHandoff completo: /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/handoffs/lululemon-define-jacket-surface-handoff-20260625T195532Z.md\n\nEscopo:\n- URL preferida: /collections/lululemon-define-jacket\n- title sugerido: Lululemon Define Jacket\n- usar apenas produtos Lululemon Define ativos já existentes\n- fazer preview/readback público 200 OK\n- registrar receipt com collection id/handle/produtos/rollback\n\nGuardrails rígidos:\n- não consultar ou alterar estoque/Tiny/inventory\n- não alterar preço\n- não alterar campanhas, GMC, Klaviyo ou checkout\n- não alterar SEO title/meta ou descrição editorial sem aprovação separada\n- não criar produto novo\n- não alterar produtos fora de membership da collection\n\nDepois da superfície 200 OK, Growth prepara guia/FAQ/schema em dev; Shopify não deve publicar conteúdo Growth nesta task.\n', 'assignee': 'lk-shopify', 'status': 'running', 'priority': 80, 'created_by': 'lk-growth', 'created_at': 1782417372, 'started_at': 1782417373, 'completed_at': None, 'workspace_kind': 'scratch', 'workspace_path': '/opt/data/kanban/boards/lk-growth-ops/workspaces/t_2443c1f6', 'claim_lock': 'a921c308b1df:165621', 'claim_expires': 1782418287, 'tenant': None, 'result': None, 'idempotency_key': 'lk-lululemon-define-jacket-surface-20260625', 'consecutive_failures': 0, 'worker_pid': 165672, 'last_failure_error': None, 'max_runtime_seconds': None, 'last_heartbeat_at': 1782417387, 'current_run_id': 20, 'workflow_template_id': None, 'current_step_key': None, 'skills': '["kanban-worker"]', 'max_retries': 2, 'branch_name': None, 'model_override': None, 'session_id': None, 'goal_mode': 0, 'goal_max_turns': None}`
