# Nike Mind 001 — Claude-SEO / GEO / FAQPage Audit

Generated: 2026-06-19T21:06:09.244549+00:00

## Verdict

Status: `blocked_public_cache`.

The implementation is correct in Shopify Admin and in the production theme preview, but the live public storefront without `preview_theme_id` is still serving old render/schema variants. Therefore, by Claude-SEO/GEO standards, the PDPs are **not yet public_ok**.

## What passes

- `custom.faq` exists as JSON on both Nike Mind PDPs.
- Each product has 7 product-specific FAQ questions.
- `body_html` was cleaned: no visible FAQ questions inside the product description.
- Production theme asset `sections/lk-pdp.liquid` now has SD08 logic:
  - direct `product.metafields.custom.faq.value` for FAQPage;
  - product FAQ is the single source when present;
  - institutional FAQ only as fallback;
  - hidden marker `data-lk-faq-schema-version="sd08-20260619"` for public validation.
- `preview_theme_id=155065417950` passes:
  - SD08 marker present;
  - 7/7 FAQ visible;
  - JSON-LD FAQPage exactly 7 questions;
  - no institutional FAQ mixed into product FAQPage;
  - therapeutic disclaimer present.

## What fails publicly

Live public URL without preview still fails:

- Pearl Pink latest public: no SD08 marker, generic institutional FAQPage only.
- Light Smoke Grey latest public: no SD08 marker, old product FAQ + institutional FAQ.
- Public render is still old even after product body clean, SD08 theme patch, and republish of the same main theme.

## Claude-SEO interpretation

This is no longer a copy/metafield issue. It is a storefront public render/cache issue. Calling the work complete would violate the LK PDP Claude-SEO/GEO/FAQPage Standard.

## Required next action

Do not replicate to other PDPs until this pilot reaches `public_ok`.

Next technical path:

1. Continue timed public revalidation.
2. If stale persists, escalate as Shopify public render/cache/theme issue.
3. Avoid injecting FAQ into `body_html` as a workaround, because that violates the standard.

## Evidence files

[
  {
    "file": "/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/nike-mind-001-claude-seo-geo-audit-20260619/admin-theme-readback.json",
    "size": 2064
  },
  {
    "file": "/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/nike-mind-001-claude-seo-geo-audit-20260619/public-validation-after-body-clean.json",
    "size": 22107
  },
  {
    "file": "/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/nike-mind-001-claude-seo-geo-audit-20260619/public-validation-sd08.json",
    "size": 21586
  },
  {
    "file": "/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/nike-mind-001-claude-seo-geo-audit-20260619/final-public-claude-seo-validation.json",
    "size": 11472
  },
  {
    "file": "/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/nike-mind-001-claude-seo-geo-audit-20260619/late-public-validation.json",
    "size": 1309
  }
]
