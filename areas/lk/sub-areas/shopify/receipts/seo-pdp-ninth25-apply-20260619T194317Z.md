# Receipt — SEO PDP nono lote follow-up de 25

Data: 2026-06-19T19:45:11.946454+00:00
Escopo aprovado por Lucas: aplicar os 25 produtos do approval packet `seo-pdp-ninth25-approval-packet-20260619`, somente `seo.title` e `seo.description`.
Sistema: Shopify Admin GraphQL.
Campos alterados: somente `seo.title` e `seo.description` de Product.
Sem alteração de preço, estoque, disponibilidade, descrição de PDP, tags, coleções, tema, checkout, canal, GMC, Klaviyo ou campanha.

## Arquivos

- Approval JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo-pdp-ninth25-approval-candidates-20260619.json`
- Snapshot antes: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_ninth25_before_20260619T194317Z.json`
- Readback depois: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_ninth25_after_readback_20260619T194317Z.json`
- QA público: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_ninth25_public_qa_20260619T194317Z.json`

## Execução

- `values_printed=false`
- `apply_count=25`
- `user_errors=[]`
- `all_match=True`

## Produtos alterados

1. `kaws-holiday-taipei-vinyl-figure-black-brown-grey-set-toy-art`
2. `pop-mart-minnie-mickey-family-cute-together-keychain-series-figures-aberto`
3. `pop-mart-mickey-family-cute-together-keychain-series-figures-aberto`
4. `pop-mart-disney-mickey-family-together-series-plush-keychain-single-blind-box-lacrada`
5. `pop-mart-disney-mickey-family-together-series-plush-keychain-sealed-case-8-blind-box-lacrado`
6. `pop-mart-secret-huguinho-zezinho-luizinho-mickey-family-cute-together-keychain-series-figures-aberto`
7. `pop-mart-teco-mickey-family-cute-together-keychain-series-figures-aberto`
8. `pop-mart-tico-mickey-family-cute-together-keychain-series-figures-aberto`
9. `pop-mart-pateta-mickey-family-cute-together-keychain-series-figures-aberto`
10. `pop-mart-margarida-mickey-family-cute-together-keychain-series-figures-aberto`
11. `pop-mart-donald-mickey-family-cute-together-keychain-series-figures-aberto`
12. `lip-case-rhode-by-hailey-bieber-limited-edition-shade-amarelo`
13. `pop-mart-crybaby-crying-again-series-vinyl-face-plush-sealed-case-6-blind-box-lacradas`
14. `pop-mart-labubu-the-monsters-coca-cola-series-special-sofa-figure`
15. `pop-mart-labubu-the-monsters-coca-cola-series-snowy-mountain-figure`
16. `medicom-toy-bearbrick-katsushika-hokusai-thirty-six-views-of-tomitake-fine-wind-clear-morning-1000-toy-art-multi`
17. `tenis-adidas-samba-disney-101-dalmatians-penny-branco`
18. `tenis-adidas-samba-og-earth-strata-wonder-white-marrom`
19. `tenis-adidas-samba-og-crochet-pack-orbit-green-verde`
20. `tenis-adidas-samba-og-cream-white-cardboard-creme`
21. `tenis-adidas-samba-jane-white-blue-gum-branco`
22. `tenis-adidas-samba-jane-white-black-branco`
23. `camisa-aime-leon-dore-soccer-jersey-pristine-bege`
24. `camiseta-aime-leon-dore-postcard-cream-bege`
25. `camiseta-aime-leon-dore-saint-george-asphalt-preto`

## QA

Admin readback:
- todos os 25 produtos bateram exatamente com os valores-alvo.

QA público:
- `handles_total=25`
- `handles_any_round_match=25`
- `handles_all_rounds_match=24`
- `handles_still_not_public_match=[]`
- `liquid_error_count=0`

## Rollback

Para desfazer, restaurar os valores anteriores a partir de:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_ninth25_before_20260619T194317Z.json`

Rollback deve alterar somente:
- `seo.title`
- `seo.description`

Depois repetir Admin readback e QA público title/meta.