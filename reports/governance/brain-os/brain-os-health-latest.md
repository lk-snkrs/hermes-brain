# Brain OS Health Audit

- Generated at: `2026-06-11T14:33:10.608968+00:00`
- Root: `/opt/data/hermes_brain_wave14_publish`
- Mode: `read_only_local_health_audit`
- Hubs audited: `56`
- Average score: `90.3/100`
- Status counts: `{'healthy': 22, 'watch': 34, 'needs_attention': 0, 'critical': 0}`

## Lowest scoring hubs
- `areas/operacoes/projetos/doppler-secrets-operations-ledger` — 82/100 (watch); issues: manifest_source_of_truth_empty, next_steps_not_decision_grade, artifact_index_absolute_paths
- `areas/operacoes/projetos/profile-channel-runtime-inventory` — 84/100 (watch); issues: manifest_source_of_truth_empty, next_steps_not_decision_grade, artifact_index_missing_sample_paths_2
- `areas/operacoes/projetos/telegram-delivery-ux-governance` — 84/100 (watch); issues: manifest_source_of_truth_empty, next_steps_not_decision_grade, artifact_index_missing_sample_paths_3
- `areas/lk/sub-areas/atendimento/projetos/chatwoot` — 85/100 (watch); issues: manifest_schema_missing_or_unaccepted, manifest_source_of_truth_empty, artifact_index_missing_sample_paths_20
- `areas/operacoes/projetos/mcp-tooling-activation-governance` — 85/100 (watch); issues: manifest_source_of_truth_empty, next_steps_not_decision_grade, artifact_index_missing_sample_paths_4
- `areas/lk/projetos/approval-learning-ledger` — 89/100 (watch); issues: manifest_source_of_truth_empty, artifact_index_missing_sample_paths_3
- `areas/lk/projetos/lk-operating-system` — 89/100 (watch); issues: manifest_source_of_truth_empty, artifact_index_missing_sample_paths_5
- `areas/lk/projetos/reporting-briefings` — 89/100 (watch); issues: manifest_source_of_truth_empty, artifact_index_missing_sample_paths_4
- `areas/lk/projetos/shopify-theme-backups-archive` — 89/100 (watch); issues: manifest_source_of_truth_empty, artifact_index_missing_sample_paths_3
- `areas/lk/sub-areas/atendimento/projetos/whatsapp-integration-platform` — 89/100 (watch); issues: manifest_source_of_truth_empty, artifact_index_missing_sample_paths_8

## Top issues
- `manifest_source_of_truth_empty`: 50
- `artifact_index_missing_sample_paths_3`: 8
- `artifact_index_missing_sample_paths_8`: 8
- `artifact_index_missing_sample_paths_7`: 7
- `artifact_index_missing_sample_paths_5`: 7
- `artifact_index_missing_sample_paths_4`: 5
- `artifact_index_missing_sample_paths_6`: 4
- `next_steps_not_decision_grade`: 4
- `artifact_index_missing_sample_paths_2`: 3
- `artifact_index_missing_sample_paths_12`: 2
- `manifest_schema_missing_or_unaccepted`: 1
- `artifact_index_missing_sample_paths_20`: 1
- `artifact_index_missing_sample_paths_15`: 1
- `artifact_index_missing_sample_paths_18`: 1
- `artifact_index_missing_sample_paths_1`: 1

## Guardrails
- Local/read-only audit only.
- No external APIs, runtime, Docker, VPS, cron, or secrets output.
- Scores do not authorize external writes.
