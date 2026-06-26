# Curadoria LK — Product cache nudge receipt — 2026-06-02

## Approval

Lucas selected: `Aprovo touch/nudge nos produtos stale listados`.

## Write executed

Created/updated technical product metafield on 7 stale product handles:

- namespace: `hermes`
- key: `curadoria_cache_nudge`
- type: `single_line_text_field`
- value: `curadoria-antistale-nudge 2026-06-02T22:30:32Z`

This was intended only to bump product `updatedAt` / cache invalidation. It does not alter visible title, price, stock, collection, SEO, media, checkout, discount or availability.

## Products nudged

- tenis-air-jordan-1-mid-glitter-swoosh-azul
- air-jordan-1-high-85-college-navy
- tenis-nike-shox-tl-black-cave-stone-preto
- yeezy-foam-runner-carbon
- tenis-adidas-tokyo-off-white-core-black-branco
- moletom-alo-yoga-cropped-serenity-coverup-athletic-heather-grey-cinza
- tenis-adidas-sambae-linen-gum-bege

## Readback

All 7 products read back the target metafield and updatedAt timestamps after the mutation. Full backup/readback:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/production-canonical-audit-20260602/option-b-preview/production-hotfix-antistale-20260602T221343Z/product-nudge/product-nudge-report.json`

## Live QA after nudge

Status: **still not fully propagated**.

Passed in latest QA:

- NB 530 canônico
- AJ1 Mid
- AJ1 OG Mocha removido

Still stale:

- AJ1 High: AJ1 High Atmosphere Rosa, AJ1 High Chicago Lost and Found Vermelho, AJ1 High Dark Mocha Marrom, AJ1 High Lucky Green Verde, AJ1 High Next Chapter Vermelho
- Shox TL: Shox TL Black Dynamic Yellow Preto, Shox TL Blue Tint Orange Azul, Shox TL Orewood Brown Cave Stone Bege, Shox TL Pumice Night Maroon Cinza, Shox TL Sunrise Gradient Laranja
- Foam Runner: Foam Runner MX Cinder Marrom, Foam Runner MX Sand Grey Cinza, Foam Runner Onyx Preto, Foam Runner Sand Bege, Foam Runner Stone Sage Bege
- Adidas Tokyo: Tokyo Core Black Preto, Tokyo Crew White Floral Embroidery Branco, Tokyo Black Floral Embroidery Preto, Tokyo Pure Sulfur Amarelo, Tokyo Silver Metallic Prata
- Yeezy 350 controle: Yeezy Boost 350 V2 Steel Grey Cinza, Yeezy Boost 350 V2 Zyon Marrom, Boost 350 V2 Boné Branco, 350 V2 Static Non-Reflective (2023) Branco, Boost 350 v2 Zebra Branco
- Alo Serenity: Cropped Serenity Coverup Black Preto, Cropped Serenity Coverup Bluestone Azul, Cropped Serenity Coverup Ivory Off White, Cropped Serenity Coverup Light Cocoa Bege, Cropped Serenity Coverup Navy Azul
- Adidas Sambae: adidas Sambae x KSENIASCHNAIDER Black Multicolor Colorido, adidas Sambae Denim Azul, adidas Sambae Core Black Metallic Gold Preto, adidas Sambae Cloud White Silver Metallic Gold Branco, adidas Sambae Cloud White Collegiate Green Branco

## Interpretation

Even product `updatedAt` did not immediately purge all stale PDP HTML. The remaining pages continue returning an old HTML response that references an old versioned CSS URL, so the source/theme/product nudge is not reflected yet on those routes.

## Rollback

Rollback for product nudge: use `product-nudge-report.json` backup. For each product:

- if `before_metafield` was null, delete metafield `hermes.curadoria_cache_nudge`;
- if it existed, restore the previous value/type.

Theme rollback files are in:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/production-canonical-audit-20260602/option-b-preview/production-hotfix-antistale-20260602T221343Z`
