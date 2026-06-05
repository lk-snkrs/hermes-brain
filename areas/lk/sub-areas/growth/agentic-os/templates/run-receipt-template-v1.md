# LK Growth Agentic OS — Run Receipt Template v1

Status: template operacional
Escopo: toda execução agentic do `lk-growth`
Modo padrão: local/read-only salvo no Brain

## Metadata

- run_id: `<YYYYMMDD-HHMM-profile-job-or-manual>`
- date: `<YYYY-MM-DD>`
- trigger: `cron | manual | follow-up | approval-review`
- source_job: `<cron name/job id if applicable>`
- operator: `lk-growth orchestrator`
- autonomy_level_used: `A0 | A1 | A2 | A3-approved | A4-approved`
- external_writes_executed: `no | yes-with-approval-id`
- telegram_sent: `no | yes-actionable-only`

## Objective

- primary_objective: `<what this run is trying to decide or investigate>`
- business_context: `<why this matters for LK>`
- expected_output: `<report | packet | review | decision | alert>`

## Planner Decision

- selected_subagents:
  - `<Growth Data Scout>` — reason: `<why>`
  - `<SEO/GEO Analyst>` — reason: `<why>`
- subagents_not_selected:
  - `<Experiment Reviewer>` — reason: `<why not>`
- required_sources:
  - `<source>` — status: `verified | unavailable | stale | not_needed`
- optional_sources:
  - `<source>` — status: `verified | unavailable | stale | not_needed`
- decision_grade_criteria:
  - `<criterion>`
- abort_or_regrade_conditions:
  - `<condition>`

## Source Status

| Source | Status | Used for | Notes |
|---|---|---|---|
| Brain | verified | context/history | |
| Shopify read-only | unavailable | product/collection | |
| GSC | unavailable | SEO queries | |
| GA4 | unavailable | CRO/funnel | |
| GMC | unavailable | product data | |
| DataForSEO | unavailable | SERP/GEO | |
| PageSpeed/CrUX | unavailable | performance | |

## Specialist Outputs Summary

### Growth Data Scout

- confidence: `high | medium | low`
- key_findings:
  - `<finding>`
- source_gaps:
  - `<gap>`

### SEO/GEO Analyst

- confidence: `high | medium | low`
- key_findings:
  - `<finding>`
- recommendations:
  - `<recommendation>`
- non_decision_grade_reasons:
  - `<reason>`

### CRO/PDP Analyst

- confidence: `high | medium | low`
- key_findings:
  - `<finding>`
- recommendations:
  - `<recommendation>`
- non_decision_grade_reasons:
  - `<reason>`

### GMC/Product Data Analyst

- confidence: `high | medium | low`
- key_findings:
  - `<finding>`
- recommendations:
  - `<recommendation>`
- non_decision_grade_reasons:
  - `<reason>`

### Content/Collection Analyst

- confidence: `high | medium | low`
- key_findings:
  - `<finding>`
- recommendations:
  - `<recommendation>`
- non_decision_grade_reasons:
  - `<reason>`

### Experiment Reviewer

- confidence: `high | medium | low | not_called`
- reviewed_hypotheses:
  - `<hypothesis id>`
- verdicts:
  - `<verdict>`

## Governor Review

- approved_for_A0_A1:
  - `<item>`
- approved_for_A2_recommendation:
  - `<item>`
- blocked_pending_A3_approval:
  - `<item>`
- blocked_pending_A4_approval:
  - `<item>`
- regraded_to_non_decision_grade:
  - `<item>` — reason: `<reason>`
- hallucination_or_source_risks:
  - `<risk>`
- telegram_noise_filtered:
  - `<item not sent>`

## Final Orchestrator Decision

- top_priorities:
  1. `<priority>` — status: `A0/A1/A2/A3-needed/A4-needed`
  2. `<priority>` — status: `A0/A1/A2/A3-needed/A4-needed`
  3. `<priority>` — status: `A0/A1/A2/A3-needed/A4-needed`
- approval_packets_created:
  - `<path or none>`
- local_artifacts_created:
  - `<path>`
- hypothesis_ledger_entries:
  - `<hypothesis id>`
- follow_up_required:
  - `<D+7/D+14/D+30 item>`

## Telegram Summary Candidate

```text
<short actionable summary for Lucas; omit if silent-OK>
```

## What Was Not Done

- No external writes unless explicitly listed above.
- No Shopify/GMC/Klaviyo/Ads/WhatsApp changes unless approved.
- No cron/profile/gateway/runtime changes unless approved.

## Verification

- brain_health_check: `pending | passed | failed`
- secret_scan: `pending | 0_hits | findings_redacted`
- artifacts_readback: `pending | passed | failed`
- next_gate: `<approval or next safe action>`
