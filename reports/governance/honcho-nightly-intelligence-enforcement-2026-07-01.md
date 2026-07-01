# Honcho nightly intelligence enforcement — 2026-07-01

Mode: local/silent-OK governance. values_printed=false. No external writes, no provider mutation, no runtime restart, no Docker/VPS/Traefik/gateway restart.

## Executive status
- Status: `attention_controlled`
- Honcho explicitly used by this cron: context=attempted; search=useful (10 sanitized hits); reasoning_non_empty=True; raw content printed=false.
- Provider health: gateway health `ok` version `0.17.0`; quality auditor `ok` score 92/100.
- Agents: expected active OK 7/7; canonical profiles configured/protocol-aware/local-skill coverage 17/17.
- Usefulness: partial_attention_controlled because semantic contamination status `attention` ratio=0.75; cleanup remains read-only and safe_to_delete_now=False.

## Configured / active / functioning / protocol-aware / useful
- configured: `True`
- active: `True`
- functioning: `True`
- protocol_aware: `True`
- useful: `partial_attention_controlled`

## Profile coverage
| Profile | live | configured | active | functioning | protocol-aware | local skill | aiPeer | recall |
|---|---:|---|---|---|---|---|---|---|
| default-opt-data | 1 | True | True | True | True | True | hermes-default | hybrid |
| brain-process | 0 | True | True | True | True | True | brain-process | hybrid |
| hermes-ops-readonly | 0 | True | True | True | True | True | hermes-ops-readonly | hybrid |
| lc-claude-cli | 1 | True | True | True | True | True | lc-claude-cli | hybrid |
| lk-analyst-readonly | 0 | True | True | True | True | True | lk-analyst-readonly | hybrid |
| lk-collection-optimizer | 1 | True | True | True | True | True | lk-collection-optimizer | hybrid |
| lk-content | 1 | True | True | True | True | True | lk-content | hybrid |
| lk-content-reviewer | 0 | True | True | True | True | True | lk-content-reviewer | hybrid |
| lk-finance | 1 | True | True | True | True | True | lk-finance | hybrid |
| lk-growth | 1 | True | True | True | True | True | lk-growth | hybrid |
| lk-ops | 1 | True | True | True | True | True | lk-ops | hybrid |
| lk-shopify | 1 | True | True | True | True | True | lk-shopify | hybrid |
| lk-stock | 1 | True | True | True | True | True | lk-stock | hybrid |
| lk-trends | 1 | True | True | True | True | True | lk-trends | hybrid |
| mordomo | 1 | True | True | True | True | True | mordomo | hybrid |
| spiti | 1 | True | True | True | True | True | spiti | hybrid |
| spiti-atendimento | 1 | True | True | True | True | True | spiti-atendimento | hybrid |

## Sanitized audit results
- all-agents: HIGH=0 WARN=3; artifact `/opt/data/reports/hermes_honcho_all_agents_audit_20260701T054247Z.json`; possible secret hits in artifact=0.
- memory quality: status=ok, score=92, pending queue=211 work units, dialectic_non_empty=True.
- semantic contamination: status=attention, score=55, contamination_ratio=0.75, previous_ratio=0.75, useful_ratio=0.281; no raw examples printed.
- cleanup candidates: status=attention, candidate_count=52, safe_to_delete_now=False; no deletion attempted.
- recent logs: counts only, raw logs not printed. Containers checked: honcho-api-1, honcho-deriver-1.

## Controlled attention / non-actions
- `semantic_contamination`: {"area": "semantic_contamination", "status": "attention", "contamination_ratio": 0.75, "previous_ratio": 0.75, "above_baseline": false, "safe_to_delete_now": false}
- `cleanup_candidates`: {"area": "cleanup_candidates", "status": "attention", "candidate_count": 52, "safe_to_delete_now": false}
- `honcho_queue`: {"area": "honcho_queue", "status": "watch", "pending_work_units": 211, "quality_status": "ok", "action": "monitor; no mutation from cron"}
- `all_agents_warning`: {"area": "all_agents_warning", "status": "watch", "message": "lk-collection-optimizer: live gateway without TELEGRAM_BOT_TOKEN boolean"}
- `all_agents_warning`: {"area": "all_agents_warning", "status": "watch", "message": "lk-content: live gateway without TELEGRAM_BOT_TOKEN boolean"}
- `all_agents_warning`: {"area": "all_agents_warning", "status": "watch", "message": "lk-growth: live gateway without TELEGRAM_BOT_TOKEN boolean"}
- `honcho_logs`: {"area": "honcho_logs", "status": "watch", "container": "honcho-api-1", "classes": {"auth": 160, "embedding_error": 1}, "raw_logs_printed": false}
- `honcho_logs`: {"area": "honcho_logs", "status": "watch", "container": "honcho-deriver-1", "classes": {"auth": 3}, "raw_logs_printed": false}

## Actionable blockers
- none. No approval packet created; no Telegram alert required.

## Verification
- Required auditors executed: all-agents, memory quality, semantic contamination with write-latest, cleanup candidate export with write-latest, gateway /health, recent log class counts.
- Secrets/raw content/PII/tokens/IDs: not printed; values_printed=false.
- Runtime mutations: none. External writes: none. Provider cleanup/deletion: none.
