# Memory OS ledger retention and boot-memory watch policy — 2026-06-26

## Purpose

Keep Memory OS useful and quiet without losing audit evidence.

## Scope

Applies to local Memory OS artifacts under:

```text
reports/memory-hygiene/
```

and boot-memory files measured by:

```text
reports/memory-hygiene/latest.json
```

## Policy

### 1. Event ledgers

Memory OS JSONL ledgers are append-only operational evidence. Do not truncate/delete them casually.

Thresholds used by the maintenance audit:

| Level | Size | Action |
|---|---:|---|
| OK | `<10MB` | Monitor only |
| Watch | `>=10MB` and `<50MB` | Track growth; no mutation |
| Compact candidate | `>=50MB` | Prepare lossless archive + tail compaction approval before mutating |

Current compact candidate:

```text
reports/memory-hygiene/adoption-events.jsonl ~77MB
```

### 2. Lossless compaction pattern

If compaction is approved later, use a lossless pattern:

1. Back up original full JSONL with timestamp and checksum.
2. Write compressed archive (`.jsonl.gz`) for historical evidence.
3. Keep a recent tail in the active JSONL, e.g. last N days or last N lines.
4. Write a rollup JSON containing counts, date range, status counts, and checksum of archived source.
5. Rerun Memory OS scorecard/adoption/daytime checks.
6. Write receipt via Memory OS receipt writer.

Do not compact if any checker depends on full-history replay without a rollup substitute.

### 3. Boot-memory watchlist

Files with usage `>=80%` are watchlisted but not automatically compacted unless one of these is true:

- watchdog classifies them as near-saturation or over-limit;
- Lucas has already approved that profile's auto-compaction scope;
- the file is default boot memory and safe local compaction is clearly needed under the standing policy.

Current watchlist:

- `profiles/lk-stock/memories/USER.md` — 83.9%.
- `profiles/lk-shopify/memories/USER.md` — 82.2%.
- `memories/USER.md` — 81.7%.
- `profiles/lk-finance/memories/USER.md` — 80.2%.

### 4. Honcho utility guardrail

Honcho is governed auxiliary memory, not the Brain. Shopify/order/customer/webhook facts found in Honcho search must be treated as operational hints only, not as personal facts about Lucas. Order/customer truth must come from Brain/source-live/Shopify/Tiny as applicable.

## Tooling

Maintenance audit script:

```text
/opt/data/scripts/hermes_memory_os_maintenance_audit.py
```

Latest output:

```text
reports/memory-hygiene/maintenance-latest.json
```

The script is read-only by default and `--write-latest` writes only sanitized JSON.

## Non-actions

This policy does not authorize:

- deleting/truncating ledgers;
- overwriting profile memories;
- Honcho runtime/provider changes;
- gateway/Docker/VPS/Traefik restart;
- external business-system writes.
