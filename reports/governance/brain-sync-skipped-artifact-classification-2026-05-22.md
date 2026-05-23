# Brain Sync skipped artifact classification — 2026-05-22

Scope: classification of files skipped by `brain_sync_safe.py --dry-run --verbose` after the approved governance package.

## Summary
- Skipped files parsed: `40`.
- Skip reasons: `{'suffix_not_allowed': 12, 'not_in_allowlist': 26, 'deny_part': 2}`.

## Classification
### `local_receipt_or_audit_evidence` — 21
- `areas/lk/sub-areas/crm/receipts/lk-crisp-callback-image-test-2026-05-20T124752Z.json`
- `areas/lk/sub-areas/crm/receipts/lk-crisp-callback-webhook-n8n-setup-2026-05-20T123923Z.json`
- `areas/lk/sub-areas/crm/receipts/lk-crisp-definitive-body-text-canary-2026-05-21-FIX020030.json`
- `areas/lk/sub-areas/crm/receipts/lk-crisp-note-image-test-2026-05-20T130117Z.json`
- `areas/lk/sub-areas/crm/receipts/lk-crisp-note-image-test-to-981119821-2026-05-20T130912Z.json`
- `areas/lk/sub-areas/crm/receipts/lk-crm-retroactive-missed-t1-send-2026-05-21.json`
- `areas/lk/sub-areas/crm/receipts/lk-recovery-os-callback-anchor-retry-2026-05-21.json`
- `areas/lk/sub-areas/crm/receipts/lk-recovery-os-callback-endpoint-anchor-gate-2026-05-21.json`

### `local_sensitive_or_raw_runtime_artifact` — 6
- `areas/lk/operacoes/lk-os-status-audit-latest.json`
- `areas/lk/sub-areas/crm/n8n-snapshots/20260521T124131Z-8heG4ZyRp85p0MQj-LK---Crisp-WhatsApp-Callback-Capture-ATIVO-.json`
- `areas/lk/sub-areas/crm/n8n-snapshots/20260521T124131Z-HTTOStvvzcz0sELN-LK---Crisp-WhatsApp-Callback-Debug.json`
- `areas/lk/sub-areas/crm/n8n-snapshots/20260521T124131Z-kWQbmEMuvdipcGjd-LK---Checkout-Abandonado-30min-24h-72h-Polling-GraphQL---Crisp-ATIVO-.json`
- `areas/operacoes/reports/mordomo-email-intake-readonly-audit-2026-05-18.json`
- `config/lk-report-delivery-targets.json`

### `local_runtime_script_not_versioned_by_allowlist` — 5
- `alert_system.py`
- `areas/operacoes/scripts/hermes_runtime_cron_watchdog.py`
- `brain_sync.sh`
- `hermes_remediate.sh`
- `monitor_daemon.py`

### `generated_report_artifact_local_only` — 5
- `reports/brain-sync-safe-dry-run-2026-05-22-bruno-audit.txt`
- `reports/brain-sync-safe-dry-run-2026-05-22-final-bruno-audit.txt`
- `reports/brain-sync-safe-dry-run-2026-05-22-gap-closure.txt`
- `reports/brain-sync-safe-dry-run-2026-05-22-governance-control-plane.txt`
- `reports/brain-sync-safe-dry-run-2026-05-22-hermes-audit.txt`

### `other_review_needed` — 3
- `areas/lk/sub-areas/growth/reports/patches/lk-checkout-30min-filter-v3.js`
- `areas/lk/sub-areas/growth/reports/patches/lk-checkout-30min-mark-sent-v3.js`
- `areas/zipper/logs/zpr_pdf_sends.jsonl`

## Recommended policy
- Keep local-only receipts/raw JSON/config/scripts out of the safe-sync allowlist unless a specific artifact is promoted to durable documentation.
- Review `report_candidate_review_for_allowlist` manually; allowlist only concise governance reports needed by future agents.
- Scripts should remain local runtime artifacts unless separately reviewed, tested, and explicitly approved for versioning.
- Large generated LK sales/CRO/GMC artifacts should stay local or be summarized into durable `.md` reports.

## External side effects
None. Dry-run only; no git push/sync write executed.
