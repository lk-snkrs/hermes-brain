# Receipt — Dispatch Handoff Adidas Samba Marrom para LK Shopify

Data: 20260625T184558Z
Origem: `[LK] Growth`
Destino: `[LK] Shopify` / `lk-shopify`
Board: `lk-growth-ops`
Task ID: `t_ae530570`
Handoff: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/handoffs/adidas-samba-marrom-surface-handoff-20260625T184438Z.md`

## Escopo aprovado

Validar/criar/ativar collection canônica Adidas Samba Marrom, preferencialmente `/collections/adidas-samba-marrom`, usando apenas produtos Adidas Samba marrom ativos já existentes.

## Guardrails

- Sem consulta/alteração de estoque/disponibilidade/grade/Tiny/inventory.
- Sem alteração de preço.
- Sem alteração de campanhas, GMC, Klaviyo ou checkout.
- Sem SEO title/meta/descrição editorial sem aprovação separada.
- Growth só prepara guia/FAQ/schema após superfície 200 OK e receipt Shopify.

## Status do dispatch

Task status após dispatch: `running`
Assignee: `lk-shopify`
Dispatch result: `DispatchResult(reclaimed=0, promoted=0, spawned=[('t_ae530570', 'lk-shopify', '/opt/data/kanban/boards/lk-growth-ops/workspaces/t_ae530570')], skipped_unassigned=[], auto_assigned_default=[], skipped_nonspawnable=[], skipped_per_profile_capped=[], crashed=[], auto_blocked=[], timed_out=[], stale=[], respawn_guarded=[], rate_limited=[])`
Runs snapshot: `[{"id": 16, "task_id": "t_ae530570", "profile": "lk-shopify", "status": "running", "worker_pid": 86837, "started_at": 1782413158, "ended_at": null, "outcome": null, "error": null}]`

## Próximo passo esperado

Aguardar LK Shopify devolver receipt em `areas/lk/sub-areas/shopify/receipts/` com handle/id/title, URL 200 OK, lógica de inclusão, rollback e readback público.


## Verificação posterior

- Task status: `running`
- Current run id: `16`
- Worker PID: `86837`
- Verificado em: `20260625T184624Z`
