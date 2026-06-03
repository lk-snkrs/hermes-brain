# Curadoria LK Option B — Production promotion receipt — 2026-06-02

## Scope approved
- Promote the Dev-validated Curadoria LK Option B snippet to Shopify Production.
- Touch `sections/lk-pdp.liquid` only if needed to force recompilation.
- Sync GitHub `production` with Shopify Production readbacks.

## Shopify Production readback
- Theme: `lk-new-theme/production` / main / Theme ID `155065417950`.
- Snippet: `snippets/lk-variante-top30-visited.liquid`.
- Snippet readback SHA12: `3ddbc92afb29`.
- Section: `sections/lk-pdp.liquid`.
- Section readback SHA12: `68944b5fe7a7`.

## GitHub
- Repo: `lk-snkrs/lk-new-theme`.
- `origin/production` matches Shopify Production readbacks exactly for both snippet and section.
- Current `origin/production` commit observed: `5ff9ad3` (`Update from Shopify for theme lk-new-theme/production`).
- Temporary PR #19 was opened from `hermes/curadoria-lk-batch9-production-20260602`, but was redundant/dirty because `production` already contained the Shopify-sync commits. PR #19 was closed and the temporary branch was deleted.

## QA evidence
- Source/readback: pass.
- GitHub vs Shopify readback: pass exact match for snippet and section.
- Dev preview QA: passed after using a proper preview session/cookie.
- Production live QA immediately after promotion: partial edge-cache stale.
  - Canonical NB 530: pass (`top30-nb-530`, short labels).
  - AJ1 OG Mocha: pass (0 blocks, legacy group removed).
  - Some sampled PDPs still served old labels from edge cache, despite source/readback/GitHub being correct: AJ1 Mid, AJ1 High, Shox TL, Foam Runner, Sambae.

## Interpretation
The writable source of truth is synchronized and correct. The remaining issue is storefront edge/render cache propagation on some PDP URLs, not a second source copy: asset scan found the old markers only inside the updated snippet source/readback, and `origin/production` now equals Shopify Production readbacks.

## Rollback
Restore backed-up Production assets from the report directory:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/production-canonical-audit-20260602/option-b-preview/production-promotion-20260602/`
Then readback both assets and run live QA.

## Follow-up
Monitor live PDPs until edge cache reflects the source. Do not claim full live storefront pass until the sampled stale PDPs return short labels.
