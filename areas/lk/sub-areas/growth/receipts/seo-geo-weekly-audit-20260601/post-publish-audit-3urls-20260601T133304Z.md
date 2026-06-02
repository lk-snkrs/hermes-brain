# LK Sneakers — SEO+GEO weekly audit post-publish validation

Timestamp UTC: 2026-06-01T13:33:04Z
Scope: read-only public storefront validation after schema/free-shipping deployment.
URLs audited:
- Home: https://lksneakers.com.br/
- PDP: https://lksneakers.com.br/products/nike-dunk-low-rose-whisper
- Collection: https://lksneakers.com.br/collections/air-jordan-1

## Executive correction

The incoming weekly report is partially outdated/inaccurate.

Corrections:
- Organization JSON-LD is present on the homepage and is not the current priority gap.
- `OfferPromo` is not a valid Schema.org type observed/needed here; promo/free-shipping is implemented as `OfferShippingDetails` + `freeShippingThreshold`.
- Free shipping schema is live on Organization/Store and PDP offer variants.
- The correct institutional schema rating intentionally remains Google rating `4.89` with `reviewCount: 433`; Judge.me remains app/store review evidence (`4.37`, seen on page source), not the global Organization rating.
- PageSpeed API quota/performance limitation remains a measurement gap; this audit used public HTTP/mobile structural proxies, not a Lighthouse mobile lab score.

## Topic 1 — Weekly report correction / score update

Recommended scores after factual correction:
- SEO: 73/100 (was 68 in incoming report; baseline 65; target 80)
- GEO: 73/100 (was 70 in incoming report; baseline 67; target 75)

Rationale:
- +3 to SEO because Organization schema is present, Product schema has shipping/return details, and homepage/PDP/collection have clean title/meta/H1/canonical.
- +3 to GEO because llms.txt is live, AI bot access is open, and priority GEO source pages are present.
- Scores are not higher because mobile performance is still unmeasured by PSI/Lighthouse and HTML payload is large (~1.15–1.31 MB), plus review density remains weak.

## Topic 2 — Mobile/technical audit over 3 URLs

Home:
- HTTP 200 desktop/mobile.
- Mobile median full request proxy: ~331 ms.
- HTML bytes: ~1,149,219.
- Title in actual head: `LK Sneakers São Paulo | Tênis Originais no Jardins — Nike, Adidas, New Balance`.
- Meta description length: 187 chars; a little long/truncated risk.
- H1 count: 1.
- Images: 31; missing alt: 0; lazy images: 28.
- Scripts: 67 mobile; external scripts: 14.

PDP Nike Dunk Low Rose Whisper:
- HTTP 200 desktop/mobile.
- Mobile median full request proxy: ~505 ms.
- HTML bytes: ~1,241,376.
- Title in actual head: `Tênis Nike Dunk Low Rose Whisper Rosa por R$ 1.499,99 em até 10x | LK Sneakers`.
- Meta description length: 126 chars.
- H1 count: 1.
- Images: 22; missing alt: 0; lazy images: 19.
- Scripts: 71 mobile; external scripts: 15.

Collection Air Jordan 1:
- HTTP 200 desktop/mobile.
- Mobile median full request proxy: ~540 ms.
- HTML bytes: ~1,314,212.
- Title in actual head: `Air Jordan 1 Original | Low, Mid, High, OG | LK Sneakers`.
- Meta description length: 140 chars.
- H1 count: 1.
- Images: 42; missing alt: 0; lazy images: 41.
- Scripts: 69 mobile; external scripts: 14.

Interpretation:
- Mobile SEO structure is healthy.
- Main technical risk is payload weight and JS/app footprint, especially collection and PDP.
- Need PSI/Lighthouse mobile once quota/tooling is available to score LCP/CLS/INP properly.

## Topic 3 — Schema post-publication validation

Home:
- 2 JSON-LD blocks.
- Parse errors: 0.
- Types include: Organization, ShoeStore, ClothingStore, PostalAddress, GeoCoordinates, AggregateRating, MerchantReturnPolicy, OfferShippingDetails, WebSite, SearchAction.
- `aggregateRating`: present.
- `shippingDetails`: present.
- `freeShippingThreshold`: present.
- `hasMerchantReturnPolicy`: present.

PDP:
- 4 JSON-LD blocks.
- Parse errors: 0.
- Root blocks: Organization/Store, Product, BreadcrumbList, FAQPage.
- Product offers: 8.
- Offers with shippingDetails: 8/8.
- Offers with hasMerchantReturnPolicy: 8/8.
- FAQ count: 7.

Collection:
- 3 JSON-LD blocks.
- Parse errors: 0.
- Root blocks: Organization/Store, BreadcrumbList, CollectionPage.
- CollectionPage has ItemList mainEntity.

Interpretation:
- Schema deployment is live and technically parseable on all 3 URLs.
- Organization gap is closed.
- Free shipping threshold implementation is live.

## Topic 4 — Reviews / rating strategy

Evidence:
- Incoming Judge.me metric: 134 reviews, 4.37★.
- Public page source also contains both `4.89` and `4.37` references.
- Organization schema exposes Google institutional rating `4.89`, `reviewCount: 433`.

Interpretation:
- Do not overwrite Organization schema with Judge.me rating; current decision is to preserve Google rating at Organization level.
- Review gap remains business/GEO risk: 134 reviewed items vs ~2326 products equals about 5.7% product review coverage.

Next corrections for approval packet:
- Add PDP post-purchase review capture flow: QR/card insert + email/WhatsApp post-delivery request, requiring explicit channel approval before execution.
- Prioritize review requests for high-traffic/high-margin products and products ranking in collections.
- Add on-site trust copy linking Google reviews, Judge.me product reviews, authenticity page, and physical store.

## Topic 5 — GEO / llms.txt expansion

Evidence:
- llms.txt status: 200.
- Last updated: 2026-05-29 15:23:07 UTC.
- Approx counts: 56 collection links, 101 product links, 58 page links.
- `LK priority GEO source pages` block is present.
- Robots includes access blocks for GPTBot, ChatGPT-User, ClaudeBot, PerplexityBot, OAI-SearchBot, Google-Extended; commercial crawlers Ahrefs/Semrush blocked.
- DataForSEO AI mentions API returned 402 subscription access denied, so direct LLM mention metrics were not available.

Interpretation:
- Foundation is good, not absent.
- Current gap is editorial curation: llms.txt has many links, but top-level editorial guide section has only one explicit guide before the broader link lists.

Recommended expansion:
- Promote priority guides from pages into the `Editorial guides / AI-citable pages` section with short descriptors:
  - Autenticidade LK Sneakers
  - Onitsuka Tiger original no Brasil
  - New Balance 204L original no Brasil
  - Adidas SL 72 OG vs RS
  - Yeezy original no Brasil
  - Air Jordan Travis Scott original no Brasil
  - Guia Adidas Samba
  - Guia Onitsuka Tiger Mexico 66
- Add concise source descriptors: authenticity, sizing, material/version differences, local pickup/store context, return/shipping policy.

## Topic 6 — Complementary schema audit

Current coverage:
- Organization/Store: present.
- WebSite + SearchAction: present on homepage.
- Product + Offer variants: present on PDP.
- BreadcrumbList: present on PDP and collection.
- FAQPage: present on PDP.
- CollectionPage + ItemList: present on collection.
- Shipping and return policy: present.

Recommended next schema opportunities (no write executed):
1. Add `AboutPage` or richer `WebPage` schema to `/pages/autenticidade` with FAQ where visible.
2. Add `LocalBusiness`/`ShoeStore` page-specific reinforcement for `/pages/loja-fisica` if not already present there.
3. Add `ItemList` consistency checks across top manual collections, especially GEO priority collections.
4. Avoid inventing promo schema types; keep using `OfferShippingDetails`, `MerchantReturnPolicy`, `PaymentMethod`, `Offer`.

## Risks

- Performance risk cannot be fully scored without Lighthouse/PSI mobile. HTTP proxy is not a Core Web Vitals substitute.
- HTML payload is large across the 3 pages; likely app/theme bloat contributes to mobile performance risk.
- Review density remains low and can limit trust/AI citation strength.
- DataForSEO AI mentions endpoint unavailable due subscription, so GEO score uses site-readiness evidence, not LLM mention telemetry.

## Rollback

No external storefront write was performed in this audit. If schema regressions appear, rollback should use the existing production receipt backup for schema/free-shipping deployment:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-production/schema-free-shipping-threshold-dev-to-production-20260601T124242Z/`

## Proposed next correction plan

Priority P0:
- Correct the weekly report narrative: Organization JSON-LD is present; remove `Organization absent` and `OfferPromo` wording.

Priority P1:
- Run PSI/Lighthouse mobile when quota/tooling is available.
- Reduce mobile payload/app bloat: audit scripts, collection grid, product recommendations, app embeds.
- Expand top `Editorial guides / AI-citable pages` in llms.txt.

Priority P2:
- Build review capture approval packet.
- Schema test pages: authenticity, store location, top GEO collections.
