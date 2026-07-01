# Approval packet — LK Stock Inventory Hub stale vs Supabase-first repo

- date: 2026-07-01
- owner: `lk-stock`
- requested_by: Mesa COO 2026-07-01 Decisão 3/3
- classification: A3 if executed; this packet is read-only/local only
- values_printed: false
- external_writes: 0
- current_status: prepared; not executed

## Problem

The LK Stock audit found that Supabase read models are updated/protected, but the production/local Inventory Hub container appears stale versus the current `inventory-hub` repo.

Evidence from `areas/lk/sub-areas/stock/reports/2026-06-30-inventory-hub-supabase-shopify-tiny-webhook-audit.md`:

- Supabase Stock OS: latest snapshot has `8550` rows, `duplicate_business_rows=0`, `public_safe_sum=0`, `availability_claim_sum=0`.
- Supabase Shopify Sales OS: latest run `20260630T102309`, source `supabase_direct_shopify_sales_os`.
- Container `lk-estoque-web` is up, but `/app/src/index.js` does not contain current routes:
  - `/api/lk-stock/lookup`
  - `/api/stock-cockpit/v2/*`
- Container `/api/vendas/shopify-sales-os` returns stale signature: `source=shopify_sales_os_db`, `generated_at=2026-06-22T08:50:46.524554Z`.
- Current repo has Supabase-first loader and current API routes, but this version is not reflected in the container serving the Hub.

## Scope if Lucas later approves execution

Prepare and execute a separate deployment/container packet for `lk-stock`/Inventory Hub only, including:

1. Preflight read-only:
   - identify exact repo/workdir/branch/commit for current Inventory Hub;
   - identify exact runtime serving `hub.lksnk.dev` / `lk-estoque-web`;
   - compare container code against repo routes;
   - verify Doppler/broker secret-name presence only, no values.
2. Backup/rollback:
   - capture current container image/id/config/env names only;
   - capture current source commit and current running health responses;
   - prepare rollback to previous container/image/commit.
3. Deploy/restart only after explicit approval:
   - no Docker/container action in this packet;
   - future execution must include scoped approval, rollback command, and readback.
4. Post-deploy readback required:
   - `/api/lk-stock/lookup?q=MR530SG&limit=20` returns JSON, not SPA HTML;
   - `/api/stock-cockpit/v2/health` returns JSON;
   - `/api/vendas/shopify-sales-os` returns Supabase-first current source, not stale `shopify_sales_os_db` 2026-06-22;
   - no public availability flags/unsafe stock claims exposed.

## Explicitly blocked now

- Docker/container deploy/restart/kill.
- Vercel/Traefik/VPS/Hostinger changes.
- Supabase writes/migrations.
- Shopify/Tiny writes.
- Public credential/env changes.
- Customer-facing claims about stock freshness until post-deploy readback passes.

## Success criteria for future execution

- Hub routes reflect current repo behavior.
- Supabase-first reads are visible in endpoint readback.
- Rollback path is tested/documented before deploy.
- `values_printed=false` and secret scan clean.

## Reminder OS

- Reminder OS loop needed: yes
- Reminder OS owner: `lk-stock`
- Reminder OS next action: convert this packet into an execution packet only if Lucas approves deploy/container work.
- Reminder OS review trigger: Lucas approval for A3 deploy/container, or next LK Stock runtime audit showing Hub stale.
- Reminder OS evidence: this packet + source audit report path above.


## Execution update — 2026-07-01

Lucas approved `Corrigir ambos`. Execution report: `areas/lk/sub-areas/stock/reports/mesa-20260701-inventory-hub-tiny-webhook-execution/execution-report.md`. Values printed: false. External writes: 0.
