# Follow-up — Onitsuka Tiger public QA mismatch

Status: Shopify Admin fields were updated successfully under approved scope, but public HTML still renders old SEO title/meta and old collection description after cache-busted retries.

## Evidence

Receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-production/onitsuka-tiger-improvement-20260617T115055Z`

- Admin readback matched approved payload.
- Products count unchanged: 160 → 160.
- Public HTML still showed old title/meta.
- Public body still showed old collection description.
- Read-only theme search found collection-specific override in `sections/lk-collection.liquid` for `onitsuka-tiger-todos-os-modelos`.

## Constraint

Original approval explicitly excluded theme changes. No theme write was performed.

## Recommendation

If Lucas wants the visible page to change immediately, approve a **dev-theme/preview first** change limited to the collection-specific override for `onitsuka-tiger-todos-os-modelos`, plus SEO public rendering investigation. Production theme write requires separate explicit approval after preview QA.

Suggested approval wording:

> Aprovo preparar em dev theme/preview a correção visual da coleção `/collections/onitsuka-tiger-todos-os-modelos`, limitada ao override específico em `sections/lk-collection.liquid` e investigação de title/meta público, sem mexer em produtos, preço, estoque, feed/GMC, campanhas, checkout ou publicação de theme production; com backup, QA mobile/desktop e rollback.
