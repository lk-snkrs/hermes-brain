# Nike Mind — recommendations audit + approval packet

Generated UTC: 2026-06-07T12:12:36.153501+00:00

## Facts verified
- Shopify collection products: 18
- GMC products sampled/listed: 5000; statuses listed: 5000
- Merchant matched products: 18/18
- Merchant unmatched products: 0/18
- Products missing all barcodes/GTIN in Shopify variants: 11/18
- Public collection: status=200 title='Nike Mind 001 Original na LK Sneakers' FAQ=1 product_links=48
- Public guide: status=200 title='Nike Mind 001 e 002: Guia LK de Escolha' FAQ=1 product_links=12

## Merchant products needing attention
- Tênis Nike Mind 002 Light Smoke Grey Cinza / tenis-nike-mind-002-light-smoke-grey-cinza: missing_barcode_gtin; SKUs=HQ4308-003-3, HQ4308-003-4, HQ4308-003-5, HQ4308-003-6, HQ4308-003-7, HQ4308-003-2, HQ4308-003-8, HQ4308-003-1, HQ4308-003-9, HQ4308-003-10, HQ4308-003-11, HQ4308-003-12, HQ4308-003-13
- Tênis Nike Mind 002 Black Hyper Crimson Preto / tenis-nike-mind-002-black-hyper-crimson-preto: missing_barcode_gtin; SKUs=HQ4308-001-5, HQ4308-001-6, HQ4308-001-7, HQ4308-001-8, HQ4308-001-9, HQ4308-001-4, HQ4308-001-10, HQ4308-001-2, HQ4308-001-11, HQ4308-001-3, HQ4308-001-12, HQ4308-001-1, HQ4308-001-13
- Tênis Nike Mind 002 Light Khaki Bege / tenis-nike-mind-002-light-khaki-bege: missing_barcode_gtin; SKUs=NKE-9054174-34, NKE-9054174-35, NKE-9054174-36, NKE-9054174-37, NKE-9054174-38, NKE-9054174-39, NKE-9054174-40, NKE-9054174-41, NKE-9054174-42, NKE-9054174-43, NKE-9054174-44, NKE-9054174-45, NKE-9054174-46
- Tênis Nike Mind 002 Sail Bege / tenis-nike-mind-002-sail-bege: missing_barcode_gtin; SKUs=HQ4310-100-34, HQ4310-100-35, HQ4310-100-36, HQ4310-100-37, HQ4310-100-38, HQ4310-100-39, HQ4310-100-40, HQ4310-100-41, HQ4310-100-42, HQ4310-100-43, HQ4310-100-44, HQ4310-100-45, HQ4310-100-46
- Tênis Nike Mind 002 Grey Football Grey Cinza / tenis-nike-mind-002-grey-football-grey-cinza: missing_barcode_gtin; SKUs=HQ4310-002-34, HQ4310-002-35, HQ4310-002-36, HQ4310-002-37, HQ4310-002-38, HQ4310-002-39, HQ4310-002-40, HQ4310-002-41, HQ4310-002-42
- Chinelo Slide Nike Mind 001 Blackened Blue Azul / slide-nike-mind-001-blackened-blue-azul: missing_barcode_gtin; SKUs=HQ4307-400-38, HQ4307-400-39, HQ4307-400-40, HQ4307-400-41, HQ4307-400-42, HQ4307-400-43, HQ4307-400-44
- Chinelo Slide Nike Mind 001 'Team Red' Vermelho / slide-nike-mind-001-team-red-vermelho: missing_barcode_gtin; SKUs=HQ4307-601, HQ4307-602, HQ4307-603, HQ4307-604, HQ4307-605, HQ4307-606, HQ4307-607, HQ4307-608, HQ4307-609
- Chinelo Slide Nike Mind 001 Sail Bege / slide-nike-mind-001-sail-bege: missing_barcode_gtin; SKUs=HQ4307-100-34, HQ4307-100-35, HQ4307-100-36, HQ4307-100-37, HQ4307-100-38, HQ4307-100-39, HQ4307-100-40, HQ4307-100-41, HQ4307-100-42, HQ4307-100-43, HQ4307-100-44, HQ4307-100-45, HQ4307-100-46
- Chinelo Slide Nike Mind 001 Mineral Slate Verde / slide-nike-mind-001-mineral-slate-verde: missing_barcode_gtin; SKUs=HQ4307-300-38, HQ4307-300-39, HQ4307-300-40, HQ4307-300-41, HQ4307-300-42, HQ4307-300-43, HQ4307-300-44
- Chinelo Slide Nike Mind 001 Pearl Pink Rosa / slide-nike-mind-001-pearl-pink-rosa: missing_barcode_gtin; SKUs=HQ4309-610-34, HQ4309-610-35, HQ4309-610-36, HQ4309-610-37, HQ4309-610-38, HQ4309-610-39, HQ4309-610-40
- Chinelo Slide Nike Mind 001 White Speed Red Branco / slide-nike-mind-001-white-speed-red-branco: missing_barcode_gtin; SKUs=HQ4307-101-34, HQ4307-101-35, HQ4307-101-36, HQ4307-101-37, HQ4307-101-38, HQ4307-101-39, HQ4307-101-40, HQ4307-101-41, HQ4307-101-42, HQ4307-101-43, HQ4307-101-44, HQ4307-101-45, HQ4307-101-46

## Recommended actions
1. GMC coverage fix packet: map each unmatched Shopify product/variant to Merchant offer/feed status; correct feed attributes only after approval. Primary metric: eligible offers and Shopping impressions/clicks.
2. SEO/GEO refinement packet: keep collection/guide structure; enrich PAA blocks and internal links only if GSC D+14 remains low. Primary metric: GSC impressions/query rows and organic sessions.
3. CRO collection preview: create dev-theme/top block only as preview with guide CTA + trust wording. Primary metric: collection→PDP CTR, WhatsApp clicks, add_to_cart/session if event available.

## Approval needed before writes
- Shopify product SEO/copy/theme production: approval required.
- GMC/feed/supplemental feed/fetch/reprocess: approval required.
- Ads/Klaviyo/WhatsApp/customer-facing send: approval required.

## Rollback
- For Shopify writes: snapshot objects before update and restore via Admin API.
- For GMC/feed: keep supplemental feed diff/version and remove/revert affected rows.
- For theme/CRO: dev theme preview first; production only with theme asset snapshot and rollback asset.

## Additional verification — canonical/index/CWV
- URL Inspection canonical collection (`https://lksneakers.com.br/collections/nike-mind-001`): PASS, Submitted and indexed, crawled as MOBILE, canonical aligned, sitemap detected.
- URL Inspection canonical guide (`https://lksneakers.com.br/pages/guia-nike-mind-001-002`): PASS, Submitted and indexed, crawled as MOBILE, canonical aligned, sitemap detected.
- Earlier `www` inspection returned unknown because public final/canonical is non-www; not a production indexing issue.
- Sitemaps: collection in collections sitemap; guide in pages sitemap.
- Rich results via URL Inspection: FAQ detected on both; Breadcrumbs on collection; Review snippets present.
- CrUX URL-level: no URL-level CrUX data for collection/guide due insufficient Chrome traffic; use lab/public QA directionally until URL-level field data appears.

## Updated priority after full audit
1. Product data quality, not Merchant absence: all 18 Shopify products have GMC match, but 11/18 have all variants missing barcode/GTIN in Shopify.
2. SEO/indexing: canonical URLs are indexed; next SEO work should focus on query capture/snippet/GEO, not emergency indexing.
3. CRO: collection has traffic lift; safest next step is dev preview for collection trust/guide CTA, then measure collection→PDP and WhatsApp/ATC.
