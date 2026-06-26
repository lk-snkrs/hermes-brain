# Receipt — SEO PDP apply lote 8

Data: 2026-06-18T22:14:28.434337+00:00
Escopo aprovado por Lucas: aplicar no Shopify apenas `seo.title` e `seo.description` dos 10 produtos do lote 8, com snapshot antes, readback Admin depois e QA público.
Sistema: Shopify Admin GraphQL.
Campos alterados: somente `seo.title` e `seo.description` de Product.
Sem alteração de preço, estoque, disponibilidade, descrição de PDP, tags, coleções, tema ou checkout.

## Arquivos

- Snapshot antes: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-eighth-scan-20260618/seo_pdp_eighth10_before_20260618.json`
- Readback depois: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-eighth-scan-20260618/seo_pdp_eighth10_after_readback_20260618.json`
- QA público: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-eighth-scan-20260618/seo_pdp_eighth10_public_qa_20260618.json`

## Execução

- `values_printed=false`
- `apply_count=10`
- `user_errors=[]`
- `all_match=True`

## Produtos alterados

1. `tenis-jordan-5-retro-wolf-grey-2026-cinza`
2. `tenis-new-balance-990v6-made-in-usa-cinza-castlerock`
3. `tenis-new-balance-gator-run-shadow-red-vermelho`
4. `tenis-new-balance-gator-run-black-preto`
5. `tenis-nike-craft-general-purpose-shoe-tom-sachs-field-brown-marrom`
6. `tenis-nike-kobe-5-protro-lower-merion-aces-away-prata`
7. `tenis-nike-craft-general-purpose-shoe-tom-sachs-archive-dark-sulfur`
8. `tenis-tom-sachs-x-nikecraft-general-purpose-summit-white-branco`
9. `tenis-nike-craft-general-purpose-shoe-tom-sachs`
10. `tenis-nike-air-max-1-x-patta-noise-aqua-azul`

## QA

Admin readback:
- todos os 10 produtos bateram exatamente com os valores-alvo.

QA público:
- `handles_total=10`
- `handles_any_round_match=10`
- `handles_all_rounds_match=10`
- `handles_still_not_public_match=[]`
- `liquid_error_count=0`

## Rollback

Para desfazer, restaurar os valores anteriores a partir de:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-eighth-scan-20260618/seo_pdp_eighth10_before_20260618.json`

Rollback deve alterar somente:
- `seo.title`
- `seo.description`

Depois repetir Admin readback e QA público title/meta.