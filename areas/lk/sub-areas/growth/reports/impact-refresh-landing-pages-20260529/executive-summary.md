# LK Growth — Executive summary: GA4 + Shopify refresh

Run UTC: 2026-05-29T22:17:52Z

Scope: 10 collection landing pages from the Top 10 collection GEO/FAQ overrides experiment.

Windows:
- Before: 2026-05-15..2026-05-21
- After: 2026-05-22..2026-05-28

Sources:
- GA4 Data API read-only, dimension `landingPagePlusQueryString`; metrics `sessions`, `totalUsers`, `addToCarts`, `checkouts`, `ecommercePurchases`, `purchaseRevenue`.
- Shopify Admin REST read-only, orders by `landing_site` containing each collection handle; valid paid/partially_paid orders only; cancelled/fraud-like orders excluded.

## Verdict

Do not revert.

The experiment remains commercially safe, with better reach and a stronger checkout/revenue signal, but conversion is not broadly proven across all 10 pages. The post-period upside is concentrated in Nike x Jacquemus Moon Shoe and traffic growth in Onitsuka Mexico 66 / Nike Mind 001 / Lululemon.

## Aggregate result — 10 pages

- GA4 sessions: 1,810 → 2,591 (+43.1%)
- GA4 users: 1,757 → 2,501 (+42.3%)
- GA4 add_to_cart: 44 → 43 (-2.3%)
- GA4 checkouts: 9 → 15 (+66.7%)
- GA4 purchases: 3 → 2 (-33.3%)
- GA4 purchaseRevenue: R$ 9,629.99 → R$ 10,800.00 (+12.1%)
- Shopify orders attributed by landing_site: 2 → 5 (+150.0%)
- Shopify revenue attributed by landing_site: R$ 3,959.10 → R$ 21,449.99 (+441.8%)

Rates:
- GA4 ATC rate: 2.43% → 1.66%
- GA4 checkout rate: 0.50% → 0.58%
- GA4 session→purchase CVR: 0.17% → 0.08%

## Main page findings

- Nike x Jacquemus Moon Shoe: strongest commercial signal. GA4 revenue R$ 7,349.99 → R$ 10,800.00; Shopify landing_site revenue R$ 3,959.10 → R$ 21,449.99; checkouts 3 → 11.
- Onitsuka Mexico 66: largest traffic lift. Sessions 176 → 837; ATC 4 → 12; checkout 0 → 1; no attributed purchase yet.
- Nike Mind 001: sessions 33 → 92 and ATC 0 → 3, but purchase/revenue fell vs one pre-period purchase.
- Lululemon: sessions 174 → 232, but ATC 4 → 1 and no purchase yet.
- Samba Jane: GSC had positive signal in the D+7 review, but GA4/Shopify conversion remains flat in this 7d window.
- Onitsuka todos and 204L: sessions down; no revenue attributed in either window.

## Caveats

- Window is short: 7 days before vs 7 days after.
- Shopify attribution is strict first landing page via `landing_site`; it does not measure assisted journeys or post-entry product/collection influence.
- GA4 and Shopify revenue differ due attribution/modeling/event behavior; use directionality, not exact equality.
- No external writes, no Shopify changes, no campaign changes.

## Recommended next step

Maintain current production state. Next read-only review should be D+14/D+21 with the same GA4 + Shopify method, and separate CRO follow-up for pages with traffic up but weak ATC/purchase: Lululemon, Nike Mind 001, Onitsuka Mexico 66.
