# Receipt — SEO PDP quarto lote follow-up de 25

Data: 2026-06-19T19:00:35.657611+00:00
Escopo aprovado por Lucas: aplicar os 25 produtos do approval packet `seo-pdp-fourth25-approval-packet-20260619`, somente `seo.title` e `seo.description`.
Sistema: Shopify Admin GraphQL.
Campos alterados: somente `seo.title` e `seo.description` de Product.
Sem alteração de preço, estoque, disponibilidade, descrição de PDP, tags, coleções, tema, checkout, canal, GMC, Klaviyo ou campanha.

## Arquivos

- Approval JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo-pdp-fourth25-approval-candidates-20260619.json`
- Snapshot antes: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_fourth25_before_20260619T185836Z.json`
- Readback depois: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_fourth25_after_readback_20260619T185836Z.json`
- QA público: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_fourth25_public_qa_20260619T185836Z.json`

## Execução

- `values_printed=false`
- `apply_count=25`
- `user_errors=[]`
- `all_match=True`

## Produtos alterados

1. `air-jordan-1-low-smoke-grey-toe-1`
2. `air-jordan-1-low-all-star-carbon-fiber`
3. `tenis-air-jordan-1-high-og-denim-azul`
4. `tenis-air-jordan-1-low-se-silver-metallic-cinza`
5. `air-jordan-1-high-og-stealth`
6. `tenis-air-jordan-1-retro-high-og-first-in-flight-azul`
7. `air-jordan-1-elevate-low-se-lucky-green`
8. `air-jordan-1-retro-low-og-black-cement`
9. `tenis-onitsuka-tiger-mexico-66-sd-clay-canyon-cream-marrom`
10. `tenis-onitsuka-tiger-mexico-66-kids-birch-rust-orange-bege-1`
11. `tenis-onitsuka-tiger-mexico-66-tgrs-crystal-pink-cream-rosa`
12. `tenis-onitsuka-tiger-mexico-66-tgrs-silver-cream-prateado`
13. `tenis-onitsuka-tiger-mexico-66-sd-white-rose-gold-branco`
14. `tenis-onitsuka-tiger-mexico-66-kids-white-dragon-fruit-branco`
15. `tenis-onitsuka-tiger-mexico-mid-runner-cream-directoire-blue-bege`
16. `tenis-onitsuka-tiger-delegation-chunk-black-black-preto`
17. `tenis-onitsuka-tiger-mexico-66-kids-white-directoire-blue-branco`
18. `tenis-onitsuka-tiger-mexico-66-kids-white-dragon-fruit-branco-1`
19. `tenis-onitsuka-tiger-mexico-66-sd-exposed-foam-peacoat-azul`
20. `tenis-onitsuka-tiger-mexico-66-sd-vin-mantle-green-ivory-verde`
21. `tenis-onitsuka-tiger-mexico-66-kids-beige-grass-green-marrom`
22. `tenis-onitsuka-tiger-mexico-66-tgrs-ivory-cream-bege`
23. `tenis-onitsuka-tiger-mexico-66-kids-birch-indian-ink-cinza`
24. `tenis-onitsuka-tiger-mexico-66-sd-exposed-foam-jade-verde`
25. `tenis-onitsuka-tiger-mexico-66-first-kids-white-huddle-yellow-branco`

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
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_fourth25_before_20260619T185836Z.json`

Rollback deve alterar somente:
- `seo.title`
- `seo.description`

Depois repetir Admin readback e QA público title/meta.