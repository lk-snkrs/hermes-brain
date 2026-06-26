# Activation receipt — LK temporary worker invocation contract

Data: 2026-06-06
Scope approved by Lucas: patch the 3 LK specialist profiles so worker/subagent invocation becomes automatic, mandatory, and auditable by receipt.

## Files changed

### LK Growth

- `/opt/data/profiles/lk-growth/skills/productivity/lk-growth-operations/SKILL.md`
  - Added `Worker Invocation Contract — obrigatório`.
  - Requires demand classification, canonical playbook selection, minimum worker subset, `delegate_task` when appropriate, explicit reason when no delegation occurs, and worker receipt.
- `/opt/data/profiles/lk-growth/memories/MEMORY.md`
  - Added boot-memory reminder for non-trivial Growth tasks.

### LK Shopify

- `/opt/data/profiles/lk-shopify/skills/productivity/lk-shopify-readonly/SKILL.md`
  - Added `Worker Invocation Contract — obrigatório`.
  - Requires demand classification, canonical playbook selection, minimum worker subset, `delegate_task` when appropriate, explicit reason when no delegation occurs, and worker receipt.
- `/opt/data/profiles/lk-shopify/memories/MEMORY.md`
  - Added boot-memory reminder for non-trivial Shopify tasks.

### LK Collection Optimizer / LKGOC

- `/opt/data/profiles/lk-collection-optimizer/skills/lk-superpowers-collection-optimizer/SKILL.md`
  - Added `Worker Invocation Contract — obrigatório`.
  - Requires opening `AGENTS.md`, classifying the LKGOC demand, selecting the canonical playbook, choosing the minimum useful worker subset, using `delegate_task` when appropriate, explaining no-delegation cases, and recording receipt.
- `/opt/data/profiles/lk-collection-optimizer/memories/MEMORY.md`
  - Added boot-memory reminder for non-trivial LKGOC tasks.

### Shared Brain template

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/templates/temporary-worker-invocation-receipt.md`
  - Created common receipt template with required fields:
    - `owner_agent`
    - `request_summary`
    - `demand_classification`
    - `canonical_playbook`
    - `workers_selected`
    - `workers_skipped`
    - `delegation_tool_used`
    - `reason_if_no_delegation`
    - `worker_outputs`
    - `owner_agent_final_decision`
    - `external_writes`
    - `approval_required_next`
    - `receipt_path`

## Operational effect

The intended runtime behavior is now explicit in each profile-local skill and boot memory:

1. The permanent owner agent must classify each non-trivial request.
2. It must choose a canonical playbook.
3. It must select the minimum useful temporary worker subset.
4. It must call `delegate_task` when there are two or more independent tracks and the tool is available.
5. If it does not delegate, it must say why.
6. It must consolidate the final answer as the permanent owner agent.
7. It must include or save a receipt showing workers selected/skipped.

## Limits

This activation changes profile-local knowledge/skills and Brain templates. It does not restart gateways and does not prove live runtime activation until the affected profiles start a fresh session or reload skills/memory. Toolset/config already showed delegation configured in all 3 profiles, but future smoke tests should verify live behavior in each specialist profile/channel.

## Safety

- No Shopify/Tiny/GMC/GitHub/Docker/VPS/Traefik/write-external action performed.
- No production theme write.
- No secrets preserved.
