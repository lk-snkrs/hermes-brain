# Receipt — SEO PDP sétimo lote follow-up de 25

Data: 2026-06-19T19:27:16.783031+00:00
Escopo aprovado por Lucas: aplicar os 25 produtos do approval packet `seo-pdp-seventh25-approval-packet-20260619`, somente `seo.title` e `seo.description`.
Sistema: Shopify Admin GraphQL.
Campos alterados: somente `seo.title` e `seo.description` de Product.
Sem alteração de preço, estoque, disponibilidade, descrição de PDP, tags, coleções, tema, checkout, canal, GMC, Klaviyo ou campanha.

## Arquivos

- Approval JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo-pdp-seventh25-approval-candidates-20260619.json`
- Snapshot antes: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_seventh25_before_20260619T192518Z.json`
- Readback depois: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_seventh25_after_readback_20260619T192518Z.json`
- QA público: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_seventh25_public_qa_20260619T192518Z.json`

## Execução

- `values_printed=false`
- `apply_count=25`
- `user_errors=[]`
- `all_match=True`

## Produtos alterados

1. `tenis-air-jordan-1-low-og-rookie-of-year-marrom`
2. `tenis-air-jordan-1-low-og-sp-x-travis-scott-velvet-brown-marrom`
3. `tenis-air-jordan-1-low-og-year-of-snake-2025-cinza`
4. `air-jordan-1-mid-wolf-grey`
5. `tenis-air-jordan-1-low-lucky-green-verde`
6. `tenis-air-jordan-1-low-wolf-grey-cinza`
7. `air-jordan-1-low-se-tie-dye`
8. `tenis-air-jordan-1-low-og-obsidian-unc-azul`
9. `tenis-air-jordan-1-low-dark-grey-womans-cinza`
10. `tenis-nike-air-jordan-1-low-coral-bege`
11. `tenis-nike-air-jordan-1-low-og-olive-verde`
12. `air-jordan-1-mid-kentucky-blue`
13. `air-jordan-1-low-true-blue`
14. `tenis-air-jordan-1-low-pink-foam-white-rosa`
15. `tenis-new-balance-9060-sea-salt-moonbeam-branco`
16. `tenis-new-balance-9060-sea-salt-raincloud-cinza`
17. `tenis-new-balance-9060-sea-salt-concrete-branco`
18. `tenis-nike-vomero-premium-sail-coconut-milk-branco`
19. `tenis-nike-vomero-premium-particle-rose-burgundy-rosa`
20. `tenis-new-balance-550-x-aime-leon-dore-brown-marrom`
21. `tenis-nike-vomero-premium-blue-tint-azul`
22. `tenis-on-running-cloudtilt-loewe-denim-blue-azul`
23. `tenis-on-running-cloudsolo-loewe-black-preto`
24. `pop-mart-labubu-the-monsters-coca-cola-series-super-surprise-figure`
25. `pop-mart-labubu-the-monsters-coca-cola-series-look-what-i-found-figure`

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
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_seventh25_before_20260619T192518Z.json`

Rollback deve alterar somente:
- `seo.title`
- `seo.description`

Depois repetir Admin readback e QA público title/meta.