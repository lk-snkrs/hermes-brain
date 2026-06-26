# Receipt — SEO PDP pacote 100 / primeiros 25

Data: 2026-06-18T22:23:09.344811+00:00
Escopo aprovado por Lucas: aplicar os primeiros 25 do pacote de 100, somente `seo.title` e `seo.description`.
Sistema: Shopify Admin GraphQL.
Campos alterados: somente `seo.title` e `seo.description` de Product.
Sem alteração de preço, estoque, disponibilidade, descrição de PDP, tags, coleções, tema ou checkout.

## Arquivos

- Snapshot antes: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-100-scan-20260618/seo_pdp_100_first25_before_20260618.json`
- Readback depois: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-100-scan-20260618/seo_pdp_100_first25_after_readback_20260618.json`
- QA público: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-100-scan-20260618/seo_pdp_100_first25_public_qa_20260618.json`
- QA público slow retry do handle sem URL pública: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-100-scan-20260618/seo_pdp_100_first25_public_slow_retry_20260618.json`

## Execução

- `values_printed=false`
- `apply_count=25`
- `user_errors=[]`
- `all_match=True`

## Produtos alterados

1. `tenis-nike-air-max-1-x-patta-hyper-crimson-branco`
2. `tenis-nike-air-max-1-x-patta-monarch-laranja`
3. `tenis-nike-air-max-90-x-patta-sp-cyber-branco`
4. `tenis-nike-air-zoom-vomero-5-doernbecher-2023-laranja`
5. `tenis-on-running-x-kith-on-k-tech-2-spirulina-barley-verde`
6. `tenis-on-cloudtilt-x-loewe-white-branco`
7. `tenis-onitsuka-tiger-tokuten-charcoal-birch-cinza`
8. `tenis-onitsuka-tiger-x-versace-sakura-leather-loafers-brown-blue-marrom`
9. `tenis-onitsuka-tiger-x-versace-tai-chi-sakura-suede-sneakers-blue-azul`
10. `tenis-onitsuka-tiger-x-versace-tai-chi-sakura-metallic-sneakers-silver-gold-prateado`
11. `tenis-asics-gel-nyc-graphite-grey-black-preto`
12. `tenis-asics-gel-1130-white-black-silver-prata-1`
13. `tenis-asics-gel-1130-white-pure-silver-prata`
14. `tenis-asics-gel-1130-white-clay-canyon-branco`
15. `tenis-asics-gel-1130-black-pure-silver-prata-1`
16. `tenis-asics-gel-1130-black-pure-silver-prata`
17. `tenis-asics-marvel-vs-capcom-x-kith-x-asics-gel-kayano-14-ryu-branco`
18. `tenis-adidas-ballerina-bad-bunny-flamboyan-vermelho`
19. `tenis-adidas-tokyo-mary-jane-crystal-sky-cream-white-azul`
20. `tenis-adidas-tokyo-mary-jane-cream-white-red-gold-metallic-creme`
21. `tenis-adidas-badbo-1-0-rise-branco`
22. `tenis-nike-shox-tl-orewood-brown-cave-stone-bege`
23. `tenis-nike-shox-tl-blue-tint-orange-azul`
24. `tenis-nike-shox-tl-sunrise-gradient-laranja`
25. `tenis-nike-shox-tl-velvet-brown-denim-turquoise-marrom`

## QA

Admin readback:
- todos os 25 produtos bateram exatamente com os valores-alvo.

QA público:
- `handles_total=25`
- `handles_any_round_match=24`
- `handles_all_rounds_match=24`
- `handles_still_not_public_match=['tenis-on-cloudtilt-x-loewe-white-branco']` — Admin/API bate, produto está ACTIVE, mas `onlineStoreUrl=null` e o fallback público retornou HTTP 404 no slow retry; sem Liquid error. Não alterei canais/publicação porque não estava aprovado.
- `liquid_error_count=0`

## Rollback

Para desfazer, restaurar os valores anteriores a partir de:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-100-scan-20260618/seo_pdp_100_first25_before_20260618.json`

Rollback deve alterar somente:
- `seo.title`
- `seo.description`

Depois repetir Admin readback e QA público title/meta.