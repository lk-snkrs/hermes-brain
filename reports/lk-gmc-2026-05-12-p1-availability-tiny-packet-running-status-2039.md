# LK GMC P1-B Availability Tiny Packet — running status

Generated: 2026-05-12 ~20:39 UTC

## Status

- Process: `proc_3ffabd6b94b9`
- OS PID: `186` shell / `190` python child
- Command: `python3 scripts/lk_gmc_p1_availability_tiny_packet_20260512.py --tiny-index-sleep 2.5 --tiny-sleep 4.0`
- Mode: read-only/no-write
- State observed: running; python child in `hrtimer_nanosleep`, consistent with conservative pacing or Tiny backpressure cooldown.

## Pre-run Tiny probe

- `produtos.pesquisa` page 1 returned `retorno.status=OK`
- `numero_paginas=181`
- `produtos_len=100`

## Current artifacts

- Existing private Tiny stock cache: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_reconciliation/lk-gmc-2026-05-12-p1-availability-tiny-packet-tiny-stock-cache.jsonl`
- Cache currently has 8 OK stock rows from the earlier run, all `ready_for_availability_apply_if_lucas_approves`, proposed `out of stock` from valid Tiny official-deposit evidence.
- The current rerun has not yet appended new stock rows at this checkpoint, likely still building Tiny index or cooling down after a non-OK page retry.

## Guardrails

No writes performed:

- Merchant writes: 0
- Tiny writes: 0
- Shopify writes: 0
- feed/fetch writes: 0
- DB/POS writes: 0
- campaign/external sends: 0

Tiny API error/rate-limit remains blocking evidence only (`blocked_tiny_stock_api_error`), never stock-zero evidence.

## Next

Keep process alive and wait for completion notification. On completion, parse final JSON/CSV/MD and produce final counts: ready/in-stock/out-of-stock/blocked.
