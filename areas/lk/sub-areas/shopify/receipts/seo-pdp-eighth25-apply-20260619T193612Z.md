# Receipt — SEO PDP oitavo lote follow-up de 25

Data: 2026-06-19T19:38:07.647514+00:00
Escopo aprovado por Lucas: aplicar os 25 produtos do approval packet `seo-pdp-eighth25-approval-packet-20260619`, somente `seo.title` e `seo.description`.
Sistema: Shopify Admin GraphQL.
Campos alterados: somente `seo.title` e `seo.description` de Product.
Sem alteração de preço, estoque, disponibilidade, descrição de PDP, tags, coleções, tema, checkout, canal, GMC, Klaviyo ou campanha.

## Arquivos

- Approval JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo-pdp-eighth25-approval-candidates-20260619.json`
- Snapshot antes: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_eighth25_before_20260619T193612Z.json`
- Readback depois: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_eighth25_after_readback_20260619T193612Z.json`
- QA público: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_eighth25_public_qa_20260619T193612Z.json`

## Execução

- `values_printed=false`
- `apply_count=25`
- `user_errors=[]`
- `all_match=True`

## Produtos alterados

1. `tenis-new-balance-9060-kids-raincloud-cinza`
2. `pop-mart-labubu-the-monsters-coca-cola-series-little-snowman-figure`
3. `pop-mart-labubu-the-monsters-coca-cola-series-surprise-shake-vinyl-plush-figure-pingente`
4. `tenis-on-running-cloudsolo-loewe-turquoise-azul`
5. `camiseta-fear-of-god-essentials-classic-short-sleeve-bright-white-branco`
6. `tenis-on-running-cloudsolo-loewe-lime-green-amarelo`
7. `tenis-on-running-cloudsolo-loewe-white-light-grey-cinza`
8. `tenis-puma-speedcat-faded-cool-cucumber-alpine-snow-verde`
9. `tenis-on-running-cloudsolo-loewe-sand-turquoise-bege`
10. `tenis-on-running-cloudsolo-loewe-dark-sand-cream-bege`
11. `tenis-a-ma-maniere-x-air-force-1-low-triple-white-branco`
12. `moletom-represent-clo-question-your-innocence-vintage-grey-cinza`
13. `bone-represent-clo-micro-owners-club-jet-black-preto`
14. `tenis-on-running-cloudsolo-loewe-dark-brown-black-marrom`
15. `tenis-on-running-cloudtilt-loewe-denim-grey-cinza`
16. `jaqueta-alo-yoga-airbrush-corset-full-zip-lunar-grey-cinza`
17. `calca-alo-yoga-legging-airlift-high-waist-light-speed-lunar-grey-cinza`
18. `calca-alo-yoga-legging-airlift-high-waist-light-speed-black-preto`
19. `top-alo-yoga-airlift-light-speed-hooded-lunar-grey-cinza`
20. `camiseta-skims-baby-tee-worn-in-jersey-snow-contrast-branco`
21. `polo-skims-baby-tee-worn-in-jersey-light-heather-grey-cinza`
22. `calca-alo-yoga-airlift-mesh-high-waist-darling-stirrup-legging-preto`
23. `calca-alo-yoga-airlift-mesh-high-waist-darling-stirrup-legging-azul`
24. `tenis-puma-speedcat-faded-carnation-pink-alpine-snow-rosa`
25. `kaws-holiday-singapore-vinyl-figure-brown-toy-art-marrom`

## QA

Admin readback:
- todos os 25 produtos bateram exatamente com os valores-alvo.

QA público:
- `handles_total=25`
- `handles_any_round_match=25`
- `handles_all_rounds_match=25`
- `handles_still_not_public_match=[]`
- `liquid_error_count=0`

## Rollback

Para desfazer, restaurar os valores anteriores a partir de:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_eighth25_before_20260619T193612Z.json`

Rollback deve alterar somente:
- `seo.title`
- `seo.description`

Depois repetir Admin readback e QA público title/meta.