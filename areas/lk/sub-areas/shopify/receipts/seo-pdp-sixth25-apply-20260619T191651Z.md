# Receipt — SEO PDP sexto lote follow-up de 25

Data: 2026-06-19T19:18:49.513349+00:00
Escopo aprovado por Lucas: aplicar os 25 produtos do approval packet `seo-pdp-sixth25-approval-packet-20260619`, somente `seo.title` e `seo.description`.
Sistema: Shopify Admin GraphQL.
Campos alterados: somente `seo.title` e `seo.description` de Product.
Sem alteração de preço, estoque, disponibilidade, descrição de PDP, tags, coleções, tema, checkout, canal, GMC, Klaviyo ou campanha.

## Arquivos

- Approval JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo-pdp-sixth25-approval-candidates-20260619.json`
- Snapshot antes: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_sixth25_before_20260619T191651Z.json`
- Readback depois: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_sixth25_after_readback_20260619T191651Z.json`
- QA público: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_sixth25_public_qa_20260619T191651Z.json`

## Execução

- `values_printed=false`
- `apply_count=25`
- `user_errors=[]`
- `all_match=True`

## Produtos alterados

1. `tenis-levis-x-nike-air-max-95-og-light-orewood-brown-denim`
2. `tenis-new-balance-1906l-ice-wine-pink-taffy-rosa`
3. `tenis-new-balance-9060-grey-day-2025-esportivo-casual`
4. `tenis-new-balance-9060-triple-black-preto`
5. `tenis-new-balance-9060-slate-grey-raincloud-cinza`
6. `tenis-new-balance-9060-garter-snake-pearl-grey-verde`
7. `tenis-new-balance-9060-fall-suedes-pack-arid-stone-marrom`
8. `tenis-new-balance-9060-bisque-frosted-glass-bege`
9. `tenis-new-balance-9060-linen-burgundy-bege`
10. `tenis-new-balance-9060-earth-shadow-flat-taupe-marrom`
11. `bolsa-jacquemus-le-chiquito-top-handle-bag-mini-orange-laranja`
12. `bolsa-jacquemus-le-chiquito-signature-bag-mini-ivory-bege`
13. `bolsa-jacquemus-le-grand-bambino-crossbody-flap-bag-croco-embossed-gradient-blue-azul`
14. `bolsa-jacquemus-le-bambino-long-shoulder-bag-black-preto`
15. `bolsa-jacquemus-le-bambino-long-flap-bag-light-brown-marrom`
16. `bolsa-jacquemus-le-chiquito-top-handle-bag-black-preto-dourado`
17. `tenis-new-balance-9060-linen-blue-cinza`
18. `tenis-new-balance-530-white-pearl-grey-branco`
19. `tenis-new-balance-530-silver-metallic-linen-bege`
20. `tenis-new-balance-530-turtledove-mushroom-mesh-casual`
21. `tenis-new-balance-530-silver-metallic-black-cement-prateado`
22. `jordan-1-mid-tropical-twist-igloo-gs`
23. `calca-saint-studio-alfaiataria-leve-prega-dupla-cinza`
24. `tenis-nike-travis-scott-x-jordan-jumpman-jack-tr-university-red`
25. `tenis-air-jordan-1-low-se-legend-coffee-marrom`

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
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_sixth25_before_20260619T191651Z.json`

Rollback deve alterar somente:
- `seo.title`
- `seo.description`

Depois repetir Admin readback e QA público title/meta.