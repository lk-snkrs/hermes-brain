# LK GMC follow-up previews — 2026-05-21

Gerado em: `2026-05-21T18:57:53.131479+00:00`
Modo: `read-only / preview`; writes executados: `0`.

## Resumo
- products_read: `19642`
- productstatuses_read: `19642`
- packet_a_records: `2`
- missing_color_total: `279`
- missing_color_high_confidence: `181`
- missing_color_medium: `50`
- missing_color_needs_review_or_none: `48`
- landing_triage_records: `19`
- landing_classification_counts: `{'shopify_product_exists_but_public_js_not_200_check_publication_or_handle': 19}`
- writes_performed: `0`

## Packet A — P0 preço Adidas Gazelle x Bad Bunny
- `online:pt:BR:IF9737` — Tênis adidas Gazelle x Bad Bunny Core White Bege
  - Content price atual: `0.00`; Merchant v1 price: `0.00`; público `.js` proposto: `2199.99 BRL`.
  - DataSource API `10636492695` input exists: `False`; autofeed `10525577766` input exists: `False`.
  - Status: `preview_only_needs_explicit_approval_before_price_write`.
- `online:pt:BR:IF9735-9` — Tênis adidas Gazelle x Bad Bunny Core White Bege
  - Content price atual: `0.00`; Merchant v1 price: `0.00`; público `.js` proposto: `2199.99 BRL`.
  - DataSource API `10636492695` input exists: `False`; autofeed `10525577766` input exists: `False`.
  - Status: `preview_only_needs_explicit_approval_before_price_write`.

## Packet B — missing color
- Total color missing: `279`; high confidence: `181`; medium: `50`; revisão humana/sem inferência: `48`.
- CSV: `reports/lk-gmc-2026-05-21-missing-color-preview.csv`
- Amostras high-confidence:
  - `1624428988081867066` — Boné Aimé Leon Dore Porsche Nylon Logo Aspen Gold Amarelo | LK Sneaker → color `Amarelo / Gold`
  - `10591784840915585992` — Boné Saint Studio Art Department Azul - LK → color `Azul`
  - `2258634078163248862` — Calça Chino Saint Studio Supima Preto → color `Preto`
  - `6562590402534581177` — Calça Nude Project Illegal Jeans Ash Cinza - LK → color `Cinza / Ash`
  - `10002025469927148791` — Calça Nude Project Jeans Soft Velvet Azul Marinho → color `Azul`
  - `11810372920072143991` — Calça Saint Studio Wide Alfaiataria Preto → color `Preto`
  - `13622509763707629816` — Calça Saint Studio Wide Alfaiataria Risca de Giz Cinza → color `Cinza`
  - `1072632` — Camiseta Aimé Leon Dore Dove Breakfast White Branco → color `Branco / White`
  - `1072634` — Camiseta Aimé Leon Dore Dove Breakfast White Branco → color `Branco / White`
  - `1072633` — Camiseta Aimé Leon Dore Dove Breakfast White Branco → color `Branco / White`
  - `1072631` — Camiseta Aimé Leon Dore Dove Breakfast White Branco → color `Branco / White`
  - `1073004` — Camiseta Aimé Leon Dore Postcard Cream Bege → color `Cream / Bege`

## Packet C — landing errors / missing price
- Registros triados: `19`
- shopify_product_exists_but_public_js_not_200_check_publication_or_handle: `19`
- CSV: `reports/lk-gmc-2026-05-21-landing-triage.csv`
- Amostras:
  - `1736512501686486863` — public `.js` `404`, Shopify Admin `DRAFT` → `shopify_product_exists_but_public_js_not_200_check_publication_or_handle` — L/g
  - `11810372920072143991` — public `.js` `404`, Shopify Admin `DRAFT` → `shopify_product_exists_but_public_js_not_200_check_publication_or_handle` — Calça Saint Studio Wide Alfaiataria Preto
  - `3876299146406606317` — public `.js` `404`, Shopify Admin `DRAFT` → `shopify_product_exists_but_public_js_not_200_check_publication_or_handle` — Calça Saint Studio Jeans Baggy Preta
  - `6562590402534581177` — public `.js` `404`, Shopify Admin `DRAFT` → `shopify_product_exists_but_public_js_not_200_check_publication_or_handle` — Calça Nude Project Illegal Jeans Ash Cinza - LK
  - `2258634078163248862` — public `.js` `404`, Shopify Admin `DRAFT` → `shopify_product_exists_but_public_js_not_200_check_publication_or_handle` — Calça Chino Saint Studio Supima Preto
  - `12729936352569121203` — public `.js` `404`, Shopify Admin `DRAFT` → `shopify_product_exists_but_public_js_not_200_check_publication_or_handle` — 39
  - `13498809788548851139` — public `.js` `404`, Shopify Admin `DRAFT` → `shopify_product_exists_but_public_js_not_200_check_publication_or_handle` — Moletom Essentials Fear of God Jet black SS24 Preto | LK Sneakers
  - `10002025469927148791` — public `.js` `404`, Shopify Admin `DRAFT` → `shopify_product_exists_but_public_js_not_200_check_publication_or_handle` — Calça Nude Project Jeans Soft Velvet Azul Marinho
  - `4041641007094962608` — public `.js` `404`, Shopify Admin `DRAFT` → `shopify_product_exists_but_public_js_not_200_check_publication_or_handle` — Camisa Saint Studio Trico Palha | LK Sneakers
  - `10591784840915585992` — public `.js` `404`, Shopify Admin `DRAFT` → `shopify_product_exists_but_public_js_not_200_check_publication_or_handle` — Boné Saint Studio Art Department Azul - LK
  - `15031239196158973196` — public `.js` `404`, Shopify Admin `DRAFT` → `shopify_product_exists_but_public_js_not_200_check_publication_or_handle` — 45
  - `13622509763707629816` — public `.js` `404`, Shopify Admin `DRAFT` → `shopify_product_exists_but_public_js_not_200_check_publication_or_handle` — Calça Saint Studio Wide Alfaiataria Risca de Giz Cinza
  - `9250025623243509812` — public `.js` `404`, Shopify Admin `DRAFT` → `shopify_product_exists_but_public_js_not_200_check_publication_or_handle` — Calça Saint Studio Wide Alfaiataria Risca de Giz Preta
  - `12095219918935390905` — public `.js` `404`, Shopify Admin `DRAFT` → `shopify_product_exists_but_public_js_not_200_check_publication_or_handle` — 43
  - `1624428988081867066` — public `.js` `404`, Shopify Admin `DRAFT` → `shopify_product_exists_but_public_js_not_200_check_publication_or_handle` — Boné Aimé Leon Dore Porsche Nylon Logo Aspen Gold Amarelo | LK Sneaker

## Decisões necessárias
- Aprovar ou não Packet A para corrigir apenas preço dos 2 offers para `2199.99 BRL`, com snapshot/readback antes do write.
- Aprovar ou não gerar/applicar uma onda high-confidence de `color` depois de revisar o CSV.
- Para landing/404: decidir por item entre republicar, corrigir link, suprimir/delete no Merchant, ou monitorar.

## O que não fiz
- Content API write
- Merchant API ProductInput PATCH
- supplemental feed upload/fetchNow
- Shopify write
- price/stock/discount change
- campaign/external send
