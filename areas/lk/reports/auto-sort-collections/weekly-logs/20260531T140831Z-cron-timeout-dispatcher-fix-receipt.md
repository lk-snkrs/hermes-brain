# Receipt — LK Weekly Collection Sort Rule B cron timeout fix

- Timestamp UTC: 2026-05-31T14:08:31Z
- Scope: local/runtime cron-facing wrapper only.
- Cron/script: `/opt/data/scripts/lk_weekly_collection_sort_ruleB.sh`
- Business runner: `/opt/data/hermes_bruno_ingest/scripts/apply_all_manual_collections_ruleB_net_sales_ga4_20260528.py`

## Diagnosis

The previous failure was a scheduler/no_agent timeout around ~120s, not evidence that the Rule B sorting logic or Shopify credentials failed. The full Rule B runner can take several minutes, so a synchronous cron script can exceed the scheduler script timeout.

## Change made

The cron-facing shell wrapper was converted into a fast dispatcher:

- exits quickly for the scheduler;
- starts the long runner asynchronously;
- uses a lock to avoid duplicate concurrent runs;
- writes dispatch and async runner logs;
- supports `LK_WEEKLY_COLLECTION_SORT_DRY_RUN=1` for read-only verification.

## Verification evidence

Read-only/dry-run verification completed before this receipt:

- shell syntax check: OK;
- executable bit: OK;
- dry-run dispatch: OK;
- async dry-run runner exit: `0`;
- dry-run selected collections: `140`;
- dry-run would reorder: `42`;
- active Rule B runner after verification: `active=0`.

Verified logs:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/weekly-logs/20260531T140229Z-dry-run-dispatch.log`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/weekly-logs/20260531T140229Z-dry-run-async.log`

## What was not done

No real Shopify apply/reorder was run during this continuation. `seguir` was treated as permission to continue safe/local verification and documentation only, not as approval for an out-of-window Shopify write.

## Next observation

The old cron `last_status` may remain as the previous error until the next scheduled/manual real run updates it. Next weekly run should be observed via the dispatch/async logs after the scheduled window.
