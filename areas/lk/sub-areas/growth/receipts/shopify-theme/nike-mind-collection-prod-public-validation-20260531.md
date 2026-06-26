# LK Nike Mind 001/002 — Production Publish Validation

- Timestamp: 2026-05-31
- Approval basis: Lucas replied `Publicar`
- Target: Shopify production/main theme `155065417950`
- URL: https://www.lksneakers.com.br/collections/nike-mind-001

## Assets touched

- `sections/lk-collection.liquid`
  - H1 display override for `collection.handle == 'nike-mind-001'`
  - render hook for `snippets/lk-nike-mind-collection-hero.liquid`
  - render hook for `snippets/lk-nike-mind-guide-panel.liquid`
  - legacy FAQ/schema suppression for Nike Mind
- `assets/lk-collection-v2.css`
  - Nike Mind v2 visual/guide CSS
  - scoped legacy FAQ hide fallback
- `snippets/lk-nike-mind-guide-panel.liquid`
  - post-grid guide panel and CTA to `/pages/guia-nike-mind-001-002`
- `snippets/lk-nike-mind-collection-hero.liquid`
  - top editorial hero for Nike Mind 001/002

## Public storefront validation

Browser URL validated with cache-bust: `?cb=20260531prod2`

- H1: `Nike Mind 001/002` — OK
- Breadcrumb: `HOME / NIKE MIND 001/002` — OK
- Top editorial hero: `.lk-collection-v2--nike-mind-redo` present — OK
- Grid count: page shows `18 itens` — OK
- Post-grid guide: `#lk-guia-nike-mind-001-002` present — OK
- CTA: `ABRIR GUIA COMPLETO NIKE MIND 001/002` → `https://lksneakers.com.br/pages/guia-nike-mind-001-002` — OK
- Legacy `.coll-faq` visible count: `0` — OK
- `FAQPage` JSON-LD count: `1` — OK
- `CollectionPage` JSON-LD count: `1` — OK

## Visual validation

Screenshot artifact: `/opt/data/profiles/lk-growth/cache/screenshots/browser_screenshot_4c92f5c16eb043e6bf889c6ffcabfd52.png`

Visual QA result: approved, no critical breakage. Minor non-blocking observations:

- thin white line above hero main image may be perceived as a design border/residue;
- upper-right campaign image crop is editorial but tight;
- WhatsApp floating button overlaps hero area as usual site behavior.

## Rollback receipts

Primary receipts/backups:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-theme/nike-mind-collection-prod-finalize-20260531T132141Z/receipt.json`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-theme/nike-mind-collection-prod-schema-faq-20260531T132317Z/receipt.json`

Earlier publish receipt attempts/backups also exist under:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-theme/nike-mind-collection-prod-publish-*`

Rollback: restore `.before` asset files via Shopify Admin Asset API PUT to production/main theme `155065417950`.

## Follow-up

D+7 read-only impact/QA review scheduled for 2026-06-07.
