# Shopify Support Packet — stale rendered PDP HTML after theme/product updates

## Summary

Storefront: `https://lksneakers.com.br`  
Production theme ID: `155065417950`  
Component: PDP `Curadoria LK` / `LK Variante` labels.

We updated the Production theme source and product metadata, and readbacks/GitHub sync confirm the corrected source is present. However, the public storefront intermittently serves old rendered PDP HTML containing stale labels. Results vary between monitor rounds, suggesting different render/cache nodes are returning different HTML versions.

## Current fresh probe

- Fresh probe stale count: `8` of `9` checked URLs.
- Fresh probe OK count: `1`.

### Stale now

- AJ1 Mid: `tenis-air-jordan-1-mid-glitter-swoosh-azul` — group `top30-air-jordan-1-mid-regular` — stale labels examples: `SE Electro Orange Laranja`; cf-cache-status=`DYNAMIC`; CSS=//lksneakers.com.br/cdn/shop/t/91/assets/lk-product-card.css?v=126935296543503562861779896322, //lksneakers.com.br/cdn/shop/t/91/assets/lk-product-card.css?v=126935296543503562861779896322
- AJ1 High: `air-jordan-1-high-85-college-navy` — group `top30-air-jordan-1-high-regular` — stale labels examples: `AJ1 High Atmosphere Rosa`, `AJ1 High Chicago Lost and Found Vermelho`, `AJ1 High Dark Mocha Marrom`; cf-cache-status=`DYNAMIC`; CSS=//lksneakers.com.br/cdn/shop/t/91/assets/lk-product-card.css?v=126935296543503562861779896322, //lksneakers.com.br/cdn/shop/t/91/assets/lk-product-card.css?v=126935296543503562861779896322
- Shox TL: `tenis-nike-shox-tl-black-cave-stone-preto` — group `top30-nike-shox-tl-regular` — stale labels examples: `Shox TL Black Dynamic Yellow Preto`, `Shox TL Blue Tint Orange Azul`, `Shox TL Orewood Brown Cave Stone Bege`; cf-cache-status=`DYNAMIC`; CSS=//lksneakers.com.br/cdn/shop/t/91/assets/lk-product-card.css?v=126935296543503562861779896322, //lksneakers.com.br/cdn/shop/t/91/assets/lk-product-card.css?v=126935296543503562861779896322
- Foam Runner: `yeezy-foam-runner-carbon` — group `top30-yeezy-foam-runner-regular` — stale labels examples: `Foam Runner MX Cinder Marrom`, `Foam Runner MX Sand Grey Cinza`, `Foam Runner Onyx Preto`; cf-cache-status=`DYNAMIC`; CSS=//lksneakers.com.br/cdn/shop/t/91/assets/lk-product-card.css?v=126935296543503562861779896322, //lksneakers.com.br/cdn/shop/t/91/assets/lk-product-card.css?v=126935296543503562861779896322
- Adidas Tokyo: `tenis-adidas-tokyo-off-white-core-black-branco` — group `top30-adidas-tokyo-regular` — stale labels examples: `Tokyo Core Black Preto`, `Tokyo Crew White Floral Embroidery Branco`, `Tokyo Black Floral Embroidery Preto`; cf-cache-status=`DYNAMIC`; CSS=//lksneakers.com.br/cdn/shop/t/91/assets/lk-product-card.css?v=126935296543503562861779896322, //lksneakers.com.br/cdn/shop/t/91/assets/lk-product-card.css?v=126935296543503562861779896322
- Yeezy 350: `yeezy-boost-350-v2-onyx` — group `top30-yeezy-350-regular` — stale labels examples: `Yeezy Boost 350 V2 Steel Grey Cinza`, `Yeezy Boost 350 V2 Zyon Marrom`, `Boost 350 V2 Boné Branco`; cf-cache-status=`DYNAMIC`; CSS=//lksneakers.com.br/cdn/shop/t/91/assets/lk-product-card.css?v=126935296543503562861779896322, //lksneakers.com.br/cdn/shop/t/91/assets/lk-product-card.css?v=126935296543503562861779896322
- Alo Serenity: `moletom-alo-yoga-cropped-serenity-coverup-athletic-heather-grey-cinza` — group `top30-alo-serenity-coverup-line` — stale labels examples: `Cropped Serenity Coverup Black Preto`, `Cropped Serenity Coverup Bluestone Azul`, `Cropped Serenity Coverup Ivory Off White`; cf-cache-status=`DYNAMIC`; CSS=//lksneakers.com.br/cdn/shop/t/91/assets/lk-product-card.css?v=126935296543503562861779896322, //lksneakers.com.br/cdn/shop/t/91/assets/lk-product-card.css?v=126935296543503562861779896322
- Adidas Sambae: `tenis-adidas-sambae-linen-gum-bege` — group `top30-adidas-sambae-regular` — stale labels examples: `adidas Sambae x KSENIASCHNAIDER Black Multicolor Colorido`, `adidas Sambae Denim Azul`, `adidas Sambae Core Black Metallic Gold Preto`; cf-cache-status=`DYNAMIC`; CSS=//lksneakers.com.br/cdn/shop/t/91/assets/lk-product-card.css?v=126935296543503562861779896322, //lksneakers.com.br/cdn/shop/t/91/assets/lk-product-card.css?v=126935296543503562861779896322

### OK now

- Canonical NB 530: `new-balance-530-white-natural-indigo-1` — group `top30-nb-530` — labels: `Turtledove`, `Silver Cream`, `Silver White`, `Steel Grey`, `Silver Blue`; cf-cache-status=`DYNAMIC`

## Monitor evidence: intermitent stale render

- Round 1: pass=False, bad_count=7, OK=Foam Runner, stale=AJ1 Mid, AJ1 High, Shox TL, Adidas Tokyo, Yeezy 350, Alo Serenity, Adidas Sambae
- Round 2: pass=False, bad_count=7, OK=AJ1 Mid, stale=AJ1 High, Shox TL, Foam Runner, Adidas Tokyo, Yeezy 350, Alo Serenity, Adidas Sambae
- Round 3: pass=False, bad_count=8, OK=none, stale=AJ1 Mid, AJ1 High, Shox TL, Foam Runner, Adidas Tokyo, Yeezy 350, Alo Serenity, Adidas Sambae
- Round 4: pass=False, bad_count=7, OK=Foam Runner, stale=AJ1 Mid, AJ1 High, Shox TL, Adidas Tokyo, Yeezy 350, Alo Serenity, Adidas Sambae
- Round 5: pass=False, bad_count=7, OK=Yeezy 350, stale=AJ1 Mid, AJ1 High, Shox TL, Foam Runner, Adidas Tokyo, Alo Serenity, Adidas Sambae
- Round 6: pass=False, bad_count=7, OK=AJ1 Mid, stale=AJ1 High, Shox TL, Foam Runner, Adidas Tokyo, Yeezy 350, Alo Serenity, Adidas Sambae

## Actions already attempted

- Production snippet corrected with short labels.
- New snippet path created: `snippets/lk-variante-top30-visited-v2.liquid`.
- PDP section changed to render the v2 snippet; Asset API readback confirmed v2 render count and no old render call.
- Global CSS fallback attempted; Asset API readback confirmed CSS update.
- Product-level technical metafield nudge applied to stale products to bump `updatedAt`; Admin/API readback confirmed.
- GitHub `production` fetched and compared against Shopify readbacks; no source drift found.
- Multiple public `.com.br` cache-busted fetches still returned old labels intermittently.

## Request to Shopify Support

Please investigate/purge stale rendered product HTML/cache for the affected PDPs. The public storefront appears to be serving old rendered HTML from some nodes even though current theme assets and products have been updated and read back successfully.

## Evidence files

- Structured JSON packet: `support-packet-data.json`
- Fresh HTML/header captures are saved in this directory: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/production-canonical-audit-20260602/option-b-preview/production-hotfix-antistale-20260602T221343Z/shopify-support-packet-20260602`
- Extended monitor JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/production-canonical-audit-20260602/option-b-preview/production-hotfix-antistale-20260602T221343Z/product-nudge/edge-watch-wait-revalidate-extended.json`
- Post-nudge monitor JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/production-canonical-audit-20260602/option-b-preview/production-hotfix-antistale-20260602T221343Z/product-nudge/edge-watch-after-product-nudge.json`
- V2 switch readback report: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/production-canonical-audit-20260602/option-b-preview/production-hotfix-antistale-20260602T221343Z/v2-switch-readback-report.json`
- CSS readback report: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/production-canonical-audit-20260602/option-b-preview/production-hotfix-antistale-20260602T221343Z/css-antistale-readback-report.json`
- GitHub sync/readback report: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/production-canonical-audit-20260602/option-b-preview/production-hotfix-antistale-20260602T221343Z/github-sync-prep-report.json`
- Product nudge report: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/production-canonical-audit-20260602/option-b-preview/production-hotfix-antistale-20260602T221343Z/product-nudge/product-nudge-report.json`
