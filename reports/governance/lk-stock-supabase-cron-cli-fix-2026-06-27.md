# LK Stock Supabase cron CLI-first fix — 2026-06-27

Status: done
Values printed: false
External writes: Supabase read-model tables only (`lk_stock_snapshots`, `lk_stock_items`)

## Scope

Fixed the existing cron `LK Stock OS Supabase read-model sync hourly` after it had been disabled during the raw API migration.

## Changes

- Re-enabled the existing cron; schedule and local delivery preserved.
- Rewrote `/opt/data/profiles/lk-stock/scripts/lk_stock_os_supabase_sync.py` to remove raw HTTP/API usage.
- Source is local LK OS SQLite (`lk_os_phase5.sqlite`), not Hub raw HTTP.
- Destination write uses `hermes-cli-run supabase --workdir /opt/data/profiles/lk-stock db query --linked --file ...`.
- Large payloads are split into 58 bounded CLI SQL chunks to avoid Supabase Management API request-size errors.
- Guardrails preserved: Tiny write 0, Shopify write 0, public availability promise 0.

## Evidence

- Cron enabled: true.
- Cron deliver: local.
- Cron schedule: `20 5,6,7,8,9,10,11,12,13,14,15,16 * * *`.
- Dry-run: status ok; source rows 14466; chunks 58; values_printed false.
- Live run: status ok; upserted 14466 rows; chunks_ok 58; values_printed false.
- Supabase readback: snapshot_exists 1; current_snapshot_items 14466.
- Active enabled cron raw API scan: active_raw_count 0.
- JSON/syntax: ok.
- Brain health: All checks passed.

## Backups

- `/opt/data/backups/cli-mcp-raw-api-migration-20260627/lk-stock-cron-jobs.before-disable-raw-supabase.json`
- `/opt/data/backups/cli-mcp-raw-api-migration-20260627/lk-stock-cron-jobs.before-reenable-supabase-cli-sync.json`

## Rollback

Restore one of the cron backups and/or revert the script from version control/local backup. If data rollback is needed, delete the snapshot run `local_sql_5cce34e091697b7358591ef4` from `lk_stock_snapshots`; `lk_stock_items` uses FK cascade.
