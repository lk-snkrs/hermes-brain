# Curadoria LK — Production anti-stale hotfix receipt — 2026-06-02

## Approval

Lucas approved: `Aprovo o 3` after being offered option 3: hotfix Production anti-stale for Curadoria LK labels by handle/group with backup, readback, QA live and rollback.

## Scope executed

Production theme only: `lk-new-theme/production` / theme ID `155065417950`.

Assets touched:

- `snippets/lk-variante-top30-visited.liquid`
- `snippets/lk-variante-top30-visited-v2.liquid` (new forced-include snippet)
- `sections/lk-pdp.liquid`
- `assets/lk-product-card.css`

No product, price, stock, checkout, discount, app, campaign, GMC, Klaviyo, Meta, WhatsApp or customer-facing send was changed.

## Readback evidence

- Compact snippet hotfix readback report: `upload-compact-readback-report.json`
- V2 include switch readback report: `v2-switch-readback-report.json`
- CSS visual guard readback report: `css-antistale-readback-report.json`
- GitHub sync report: `github-sync-prep-report.json`

GitHub `origin/production` auto-synced from Shopify and matched readbacks; no manual PR/merge was necessary after fetch/reset. Latest observed production sync commit in report: see `github-sync-prep-report.json`.

## QA live result

Status: **not fully resolved visually/live**.

Passed in latest QA:

- NB 530 canônico
- Yeezy 350
- AJ1 OG Mocha removido

Still stale in latest QA:

- AJ1 Mid: Wolf Grey Cinza, Panda Preto, SE Electro Orange Laranja, 'Canyon Rust' Multicolor, Aqua Blue Tint Verde
- AJ1 High: AJ1 High Atmosphere Rosa, AJ1 High Chicago Lost and Found Vermelho, AJ1 High Dark Mocha Marrom, AJ1 High Lucky Green Verde, AJ1 High Next Chapter Vermelho
- Shox TL: Shox TL Black Dynamic Yellow Preto, Shox TL Blue Tint Orange Azul, Shox TL Orewood Brown Cave Stone Bege, Shox TL Pumice Night Maroon Cinza, Shox TL Sunrise Gradient Laranja
- Foam Runner: Foam Runner MX Cinder Marrom, Foam Runner MX Sand Grey Cinza, Foam Runner Onyx Preto, Foam Runner Sand Bege, Foam Runner Stone Sage Bege
- Adidas Tokyo: Tokyo Core Black Preto, Tokyo Crew White Floral Embroidery Branco, Tokyo Black Floral Embroidery Preto, Tokyo Pure Sulfur Amarelo, Tokyo Silver Metallic Prata
- Alo Serenity: Cropped Serenity Coverup Black Preto, Cropped Serenity Coverup Bluestone Azul, Cropped Serenity Coverup Ivory Off White, Cropped Serenity Coverup Light Cocoa Bege, Cropped Serenity Coverup Navy Azul
- Adidas Sambae: adidas Sambae x KSENIASCHNAIDER Black Multicolor Colorido, adidas Sambae Denim Azul, adidas Sambae Core Black Metallic Gold Preto, adidas Sambae Cloud White Silver Metallic Gold Branco, adidas Sambae Cloud White Collegiate Green Branco

## Interpretation

Theme source/readbacks/GitHub are current and include multiple anti-stale layers:

1. compact handle-to-short-label guard inside the original snippet;
2. forced new snippet include `lk-variante-top30-visited-v2`;
3. section render switched to v2;
4. CSS visual label guard in a globally loaded CSS asset.

However the remaining PDPs are still serving old cached HTML that also references an old versioned CSS asset URL, so neither new Liquid nor new CSS can affect those already-cached responses until Shopify invalidates/re-renders the product route.

## Rollback

Rollback options:

1. Restore original snippet from `snippet.before.liquid`.
2. Restore section from `section.before-v2-switch.liquid` or `section.before.liquid`.
3. Restore CSS from `lk-product-card.before.css`.
4. Remove `snippets/lk-variante-top30-visited-v2.liquid` if no longer used.

Backup directory:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/production-canonical-audit-20260602/option-b-preview/production-hotfix-antistale-20260602T221343Z`

## Next required approval if Lucas wants immediate force

The remaining immediate-force option is a narrow Shopify product/template cache nudge for the stale product handles (for example, a no-op product/template/metafield touch or equivalent Admin product write that changes `updated_at` without changing visible product data, if Shopify permits it). This is a Shopify product write and therefore requires separate explicit approval and rollback/readback plan.
