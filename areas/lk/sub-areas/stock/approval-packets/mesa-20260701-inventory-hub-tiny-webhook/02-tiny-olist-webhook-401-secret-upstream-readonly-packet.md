# Approval packet — LK Stock Tiny/Olist webhook 401 reconciliation

- date: 2026-07-01
- owner: `lk-stock`
- requested_by: Mesa COO 2026-07-01 Decisão 3/3
- classification: A2/A3 if executed; this packet is read-only/local only
- values_printed: false
- external_writes: 0
- current_status: prepared; not executed

## Problem

The LK Stock audit found that Shopify → Hermes → dry-run Tiny route is working for the main Shopify path, but Tiny/Olist webhook route is not proven end-to-end.

Evidence from `areas/lk/sub-areas/stock/reports/2026-06-30-inventory-hub-supabase-shopify-tiny-webhook-audit.md`:

- `hermes-webhooks` health returns HTTP 200.
- Hermes central webhook platform has LK stock routes registered.
- Signed no-op `lk-shopify-tiny-stock-sync` returns HTTP 200, ignored/no-write, `write_executed=false`.
- Real Shopify POSTs are reaching Hermes for the main route.
- Tiny/Olist route `lk-stock-tiny-stock-snapshot` signed no-op returned HTTP 401.
- Conclusion: do not call Tiny/Olist webhook active until secret/upstream/proxy are reconciled and a no-op probe returns HTTP 200.

## Scope if Lucas later approves execution

Prepare a separate Tiny/Olist webhook reconciliation run for `lk-stock`, including:

1. Read-only inventory:
   - list configured local route names and expected verifier type;
   - identify upstream/public path expected for Tiny/Olist;
   - check secret-name presence via Doppler/helper/broker only, no values;
   - compare Vercel proxy route, Hermes route, and local script expectation.
2. No-op probe design:
   - use a harmless event/payload with explicit no-write mode;
   - verify expected HTTP status and reason;
   - confirm `write_executed=false` in ledger/logs.
3. Mutation gates:
   - if secret/upstream/env changes are needed, create a new explicit execution approval packet with rollback/readback;
   - do not silently update Vercel env, Hermes route secret, Doppler, webhook subscription, Tiny/Olist upstream, or gateway config.
4. Post-fix required proof if later approved:
   - HTTP 200 for signed/query-secret no-op as applicable;
   - event ledger entry with `write_executed=false`;
   - route remains non-customer-facing;
   - no Shopify/Tiny/Supabase write occurred.

## Explicitly blocked now

- Changing Doppler/Vercel/Hermes webhook secrets.
- Creating or editing Tiny/Olist/Shopify webhook subscriptions.
- Gateway restart or webhook platform restart.
- Tiny write, Shopify write, Supabase write.
- Treating route as functioning before no-op proof passes.

## Success criteria for future execution

- Tiny/Olist webhook route has documented upstream + verifier alignment.
- No-op probe returns expected HTTP 200 without writes.
- Ledger proves no-write mode.
- `values_printed=false` and secret scan clean.

## Reminder OS

- Reminder OS loop needed: yes
- Reminder OS owner: `lk-stock`
- Reminder OS next action: perform read-only route/secret/upstream reconciliation; produce execution packet only if mutation is required.
- Reminder OS review trigger: Lucas approval for webhook reconciliation, or next LK Stock audit showing Tiny/Olist route 401.
- Reminder OS evidence: this packet + source audit report path above.


## Execution update — 2026-07-01

Lucas approved `Corrigir ambos`. Execution report: `areas/lk/sub-areas/stock/reports/mesa-20260701-inventory-hub-tiny-webhook-execution/execution-report.md`. Values printed: false. External writes: 0.
