# FINAL SUCCESS — GMC LIA linkTemplate repatch — 2026-06-08

Generated: `2026-06-08T15:33:50.577144+00:00`

## Approval

Lucas approved in-current-turn:

> Aprovo repatch GMC dos 162 itens LIA com link_template faltando, com snapshot, readback e rollback.

## Scope

- Surface: Google Merchant Center / Merchant API
- Write executed: yes
- Shopify changed: no
- Prices/stock/GTIN/title changed: no
- Fields patched: `linkTemplate`, `mobileLinkTemplate`, `adsRedirect`
- Pattern: current product link + `store_code={store_code}`

## Execution

### Main repatch

- Targets from approved recheck: 162
- Patch ok: 162
- Patch fail: 0
- Skipped: 0
- Immediate readback confirmed linkTemplate: 69
- Immediate readback still processing/with issue: 93

Immediate readback was partially stale/processing; a full rescan was used as final verification.

### Residual processing

After the first rescan, a small residual set still appeared while Merchant processing/feed updates were settling.

- Residual batch 4: ok 4 / fail 0
- Residual batch 13: ok 13 / fail 0

These residuals were patched under the same approved issue scope and then allowed processing time before final scan.

## Final verification

Final full scan result:

- Pages scanned: 23
- `mhlsf_full_missing_valid_link_template` remaining: 0
- Generated at: 2026-06-08T15:33:29.387969+00:00

## Evidence files

- Approved target scan: `before_scan_missing_link_template_162.json`
- Snapshot before patch: `snapshot_before_patch.json`
- Main patch results: `patch_results.jsonl`
- Main readback: `readback_after_patch.json`
- Main summary: `patch_summary.json`
- Residual scan 4: `residual_scan_missing_link_template_4.json`
- Residual patch results 4: `patch_results_residual_4.jsonl`
- Residual scan 13: `residual_scan_missing_link_template_13.json`
- Residual patch results 13: `patch_results_residual_13.jsonl`
- Final scan: `final_scan_missing_link_template.json`
- Rollback plan: `ROLLBACK_PLAN.md`

## Rollback

Rollback plan saved in `ROLLBACK_PLAN.md`. Snapshot preserved. No rollback executed because final verification is clean.

## Follow-up

Because this issue regressed once after a previous clean scan, recheck again in 24–72h and D+7 to confirm feed/dataSource persistence.
