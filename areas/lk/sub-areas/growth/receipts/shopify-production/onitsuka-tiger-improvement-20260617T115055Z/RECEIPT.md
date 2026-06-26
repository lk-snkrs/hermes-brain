# Receipt — Onitsuka Tiger improvement

- Timestamp UTC: 20260617T115055Z
- Collection: `/collections/onitsuka-tiger-todos-os-modelos`
- Collection ID: `gid://shopify/Collection/458490904798`
- Scope applied: `seo.title`, `seo.description`, `descriptionHtml` only.
- Blocked scope respected: products, price, stock, feed/GMC, campaigns, theme, Klaviyo/WhatsApp, checkout.
- Product count before/after: {'count': 160} / {'count': 160}
- Mutation user errors: `None`

## New SEO

- Title: `Onitsuka Tiger Original no Brasil | Mexico 66 e LK`
- Meta: `Onitsuka Tiger original no Brasil: Mexico 66, SD, Sabot e modelos selecionados com curadoria LK, autenticidade e atendimento humano para escolher.`

## QA

- Admin readback fields matched payload: `True`
- Public QA last: `{"http_status": 200, "final_url_path": "/collections/onitsuka-tiger-todos-os-modelos?_hermes_qa=1781697058_1", "title_new_present": false, "meta_new_present": false, "faq_terms_present": false, "jsonld_faq_present": false, "body_len": 199392}`

## Rollback

Use `rollback-payload.json` in this folder to restore previous `seo.title`, `seo.description`, and `descriptionHtml`.

## Impact review

D+7 and D+14: GSC page/query CTR, position; GA4/Shopify organic landing session/PDP/add-to-cart/revenue where available.
