# LK SEO/GEO Experiment — Top 10 Collection FAQ + Editorial Copy

Date: 2026-05-22
Status: dev theme implemented, pending Lucas approval for production
Dev theme: `155065450718` (`lk-new-theme/dev`)
Asset: `sections/lk-collection.liquid`
Backup/rollback: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/shopify-theme-backups/lk-collection-top10-geo-faq-dev-20260522-181848`

## Selection logic

Chosen from the decision-grade refresh combining collection visit relevance and Google/GSC opportunity. The goal is to improve discoverability, AI citation readiness, and collection conversion intent without exposing operational stock/encomenda taxonomy.

## Collections implemented

1. `/collections/onitsuka-tiger-todos-os-modelos`
2. `/collections/new-balance-204l`
3. `/collections/air-jordan-travis-scott`
4. `/collections/lululemon`
5. `/collections/adidas-samba-jane`
6. `/collections/onitsuka-tiger-mexico-66`
7. `/collections/nike-mind-001`
8. `/collections/yeezy`
9. `/collections/nike-x-jacquemus-moon-shoe-sp`
10. `/collections/nude-project`

## What changed in dev

- Added/confirmed demand-led editorial description overrides for all 10 collections.
- Added collection-specific FAQ override with 4 intent-led questions per collection.
- Added matching `FAQPage` JSON-LD for each collection-specific FAQ.
- Avoided duplicate visible FAQ: the template uses the native FAQ area and replaces generic FAQ content only for target collection handles.
- Copy follows LK premium/minimal tone and avoids public taxonomy around pronta entrega/encomenda/estoque.

## Validation

- Shopify Admin API readback hash matched local asset after PUT to dev.
- Browser preview check confirmed marker FAQ and FAQPage schema for NB 204L and Yeezy.
- Browser batch fetch confirmed marker FAQ and FAQPage schema present for all 10 handles in dev preview.
- Local content check: 10/10 handles present; `lk_faq_override` present; forbidden terms absent in the changed asset.

## Production approval packet

Impact:
- Higher relevance for Google long-tail questions around fit, authenticity, model comparison and colorway choice.
- Better AI citation readiness via explicit FAQ blocks and structured data.
- Cleaner collection-level commercial copy that supports buyer decision without over-operational wording.

Risk:
- Medium-low: customer-facing collection copy and schema, scoped by collection handle.
- No product price, stock, feed, campaign, WhatsApp, Klaviyo or checkout changes.

Rollback:
- Restore `sections/lk-collection.liquid` from backup `asset.before` in the backup directory above, or revert the Git diff for this asset.

Approval needed:
- Production publish requires explicit Lucas approval in the current turn.

Impact review:
- Use existing weekly experiment cron to compare GSC impressions/clicks/CTR/queries and GA4 collection engagement after indexation window.
