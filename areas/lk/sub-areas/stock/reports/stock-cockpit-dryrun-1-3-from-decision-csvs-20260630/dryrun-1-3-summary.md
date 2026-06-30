# Stock Cockpit — dry-run 1 a 3 from decision CSVs — 2026-06-30

- generated_at_utc: `2026-06-30T14:59:10.454483+00:00`
- values_printed: false
- external_writes: 0

## Step 1 — Shopify SKU-only dry-run

- input rows: 18
- executable preview rows: 0
- blocked rows: 18
- noop rows: 0
- live_write_allowed: false
- blocker: `decision CSV has no executable target rows`

## Step 2 — Tiny codigo dry-run

- input rows: 116
- executable dry-run rows: 0
- blocked rows: 116
- non-codigo/noop rows: 0
- live_write_allowed: false
- blocker: `decision CSV has no executable Tiny codigo rows`

## Step 3 — Live execution gate

- final_verdict: `blocked_no_executable_rows`
- Shopify live writes: 0
- Tiny live writes: 0
- Supabase writes: 0

## Required to unblock

### Shopify

Fill `decision_action` + `decision_target_sku` for rows where action is `set_target_sku` or `blank_sku`.

### Tiny

Fill `decision_action=set_codigo_existing_tiny`, `decision_tiny_id`, and `decision_target_codigo` for each row to write with `lk-tiny produtos codigo-alterar`.
