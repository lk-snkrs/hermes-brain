# Temporary Worker Invocation Receipt — LK Specialist Agents

Use this receipt whenever LK Growth, LK Shopify, or `[LK] Otimização de Coleções` starts a non-trivial task that may benefit from temporary workers/subagents.

## Required fields

- `owner_agent`: `lk-growth` | `lk-shopify` | `lk-collection-optimizer`
- `request_summary`: short human summary of Lucas's request.
- `demand_classification`: playbook/domain classification.
- `canonical_playbook`: file/path or named playbook used.
- `workers_selected`: list of temporary workers selected.
- `workers_skipped`: list of relevant workers intentionally skipped, with reason.
- `delegation_tool_used`: `yes` | `no`
- `reason_if_no_delegation`: required when `delegation_tool_used=no`.
- `worker_outputs`: one bullet per worker, including evidence/path/status.
- `owner_agent_final_decision`: final consolidated decision by the permanent owner agent.
- `external_writes`: `none` unless Lucas approved exact external write scope.
- `approval_required_next`: what Lucas must approve next, if anything.
- `receipt_path`: final local/Brain path for this receipt.

## Invocation rule

The owner agent must not wait for Lucas to ask “use subagents”. For each normal specialist task:

1. Classify the demand.
2. Select the canonical playbook.
3. Select the minimum useful worker subset.
4. Use `delegate_task` when there are two or more independent research/execution/QA tracks and the tool is available in the current runtime.
5. If `delegate_task` is unavailable, blocked, or not useful, state `delegation_tool_used=no` and explain why.
6. Consolidate as the owner agent; temporary workers do not become permanent agents or user-facing owners.
7. Keep production/external writes approval-gated.

## Minimal inline format for Telegram

When a full file receipt is unnecessary, include this compact block in the answer:

```text
Worker receipt:
- Owner: <profile>
- Playbook: <name/path>
- Workers used: <A, B, C> / none
- Workers skipped: <X because...>
- Delegation tool: yes/no — <reason>
- External writes: none/approved scope
```
