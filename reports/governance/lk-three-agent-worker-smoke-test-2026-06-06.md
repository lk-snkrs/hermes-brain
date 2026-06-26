# LK three-agent worker smoke test

Date: 2026-06-06
Mode: local/read-only smoke test. No Shopify/Tiny/GMC/GitHub/production/external writes.

## Scope

Profiles tested:

- `lk-growth`
- `lk-shopify`
- `lk-collection-optimizer`

Each profile received a non-trivial hypothetical task and was instructed to apply its Worker Invocation Contract: classify demand, choose canonical playbook, select minimum useful temporary workers, use `delegate_task` when available for independent tracks, consolidate as owner, and return a Worker receipt.

Raw outputs copied to:

`/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/worker-smoke-raw-20260606/`

## Results

### LK Growth

Session: `20260606_131619_3dd376`
Raw output: `worker-smoke-raw-20260606/lk-growth-worker-smoke-20260606T131517Z.txt`

Result: PASS.

Evidence from output:

- Delegation executed: `delegate_task` batch with 2 independent tracks.
- Workers selected:
  - Data Scout
  - SEO/CRO/GEO Analyst
- Workers skipped with reasons:
  - GMC/Product Data Analyst
  - Paid Media Analyst
  - Klaviyo/CRM Analyst
  - LK Shopify handoff
  - Collection Optimizer/LKGOC execution worker
  - Governor/Critic dedicated
- `delegation_tool_used: yes`
- External writes: none.
- Owner decision: LK Growth correctly classified the task as non-trivial, delegable, and not decision-grade without real authenticated data.

### LK Shopify

Session: `20260606_131901_976c69`
Raw output: `worker-smoke-raw-20260606/lk-shopify-worker-smoke-20260606T131856Z.txt`

Result: PASS.

Evidence from output:

- Delegation executed with 2 tracks:
  - Shopify Surface Mapper + Theme/Feature Architect
  - Shopify QA Visual Worker + Rollback/Risk Reviewer
- Workers selected:
  - Shopify Surface Mapper
  - Theme/Feature Architect
  - Shopify QA Visual Worker
  - Rollback/Risk Reviewer
- Workers skipped with reasons:
  - CRO/Purchase Flow Worker
  - Preview/Diff Builder
  - Readback/Receipt Verifier
  - LK Growth
  - `[LK] Otimização de Coleções`
  - GitHub/PR worker
  - Tiny/GMC/Klaviyo/ads/WhatsApp workers
- `delegation_tool_used: true`
- External writes: none.
- Owner decision: LK Shopify classified the task as cart drawer/minicart DEV preview preparation and kept DEV/production writes blocked without explicit approval.

### LK Collection Optimizer / LKGOC

Session: `20260606_132150_879ba1`
Raw output: `worker-smoke-raw-20260606/lkgoc-worker-smoke-20260606T132146Z.txt`

Result: PASS.

Evidence from output:

- Delegation executed: `delegation_tool_used: yes`.
- Demand classification:
  - Full LKGOC Rebuild hipotético / rewrite-from-zero / not decision-grade without live data.
- Canonical playbook:
  - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/playbooks/full-lkgoc-rebuild.md`
- Workers selected:
  - Collection Intake Classifier
  - Evidence & SERP Researcher
  - LKGOC Experience Architect
  - SEO/GEO Validator
  - Visual QA Mobile/Desktop Worker
  - Rollback & Receipt Verifier
- Workers skipped with reasons:
  - Guia LK Editorial Writer — skipped because final copy would be unsafe without real research.
  - Shopify DEV Preview Builder — skipped because external writes/real preview were prohibited.
- External writes: none.
- Owner decision: Collection Optimizer correctly kept ownership, treated the task as LKGOC Full, required input/evidence packet before real execution, and kept production blocked.

## Verdict

The Worker Invocation Contract is now operationally proven in a local/read-only smoke test for all three profiles.

This proves:

1. The profiles can load/apply the new contract.
2. They can classify non-trivial demands.
3. They can select minimum temporary worker subsets.
4. They can use delegation for independent tracks in a smoke-test context.
5. They can return a worker receipt with selected/skipped workers and owner decision.
6. They preserved external-write/production guardrails.

## Remaining limit

This is a local one-shot smoke test, not a Telegram live-channel round-trip initiated by Lucas inside each specialist bot. Runtime behavior is proven for `hermes chat` under each profile with the requested toolsets; a stricter end-to-end test would ask Lucas to send a real message to each specialist Telegram bot and verify inbound log + response + receipt there.

## Safety

- No external writes.
- No production writes.
- No secrets preserved.
- Raw outputs are local text artifacts only.
