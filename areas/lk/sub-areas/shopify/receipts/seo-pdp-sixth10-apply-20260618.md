# Receipt — SEO PDP apply lote 6

Data: 2026-06-18T18:19:49.026617+00:00
Escopo aprovado: aplicar lote 6 SEO PDP de 10 produtos.
Sistema: Shopify Admin GraphQL.
Campos alterados: somente `seo.title` e `seo.description` de Product.
Sem alteração de preço, estoque, disponibilidade, descrição de PDP, tags, coleções ou tema.

## Arquivos

- Snapshot antes: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-sixth-scan-20260618/seo_pdp_sixth10_before_20260618.json`
- Readback depois: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-sixth-scan-20260618/seo_pdp_sixth10_after_readback_20260618.json`
- QA público inicial: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-sixth-scan-20260618/seo_pdp_sixth10_public_qa_20260618.json`
- QA público retry lento: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-sixth-scan-20260618/seo_pdp_sixth10_public_slow_retry_20260618.json`

## Execução

- `values_printed=false`
- `apply_count=10`
- `user_errors=[]`
- `all_match=True`

## Produtos alterados

1. `tenis-air-jordan-4-og-sp-x-nigel-sylvester-brick-after-brick-branco`
2. `tenis-nike-air-jordan-chase-b-x-travis-scott-x-jumpman-jack-tr-black-night-silver-preto`
3. `tenis-nike-air-jordan-4-retro-black-cat-preto`
4. `tenis-nike-air-jordan-1-retro-low-og-sp-travis-scott-shy-pink-bege`
5. `tenis-nike-air-jordan-1-retro-low-og-sp-travis-scott-sail-tropical-pink-rosa`
6. `tenis-nike-vomero-premium-tangerine-tint-laranja`
7. `tenis-nike-vomero-premium-pearl-pink-rosa`
8. `tenis-nike-vomero-premium-barely-green-verde`
9. `tenis-nike-vomero-premium-x-renegade-x-cinnamon-marrom`
10. `tenis-nike-vomero-premium-x-melitta-baumeister-total-orange-laranja`

## QA

Admin readback:
- todos os 10 produtos bateram exatamente com os valores-alvo.

QA público inicial:
- `handles_total=10`
- `handles_any_round_match=5`
- `handles_all_rounds_match=3`
- `liquid_error_count=0`

QA público retry lento nos 5 handles inicialmente stale:
- `retried=5`
- `handles_any_retry_match=5`
- `handles_all_retry_match=5`
- `handles_still_not_public_match=[]`
- `liquid_error_count=0`

Interpretação:
- Admin/API confirmou 10/10 imediatamente.
- O público teve cache/CDN parcial na primeira rodada, mas convergiu no retry lento; não houve Liquid error.

Revalidação posterior antes do lote 7:
- Foi detectado 1 produto do lote 6 divergente no Admin (`tenis-nike-vomero-premium-x-melitta-baumeister-total-orange-laranja`).
- Reapliquei o alvo já aprovado dentro do mesmo escopo de SEO fields.
- Repair/readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-sixth-scan-20260618/seo_pdp_sixth10_repair_melitta_readback_20260618.json`
- Resultado repair: `admin_match=true`, `user_errors=[]`, `liquid_error_count=0`.
- Público desse handle ainda pode alternar cache, mas Admin/API voltou a `10/10` antes do packet do lote 7.

## Rollback

Para desfazer, restaurar os valores anteriores a partir de:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-sixth-scan-20260618/seo_pdp_sixth10_before_20260618.json`

Rollback deve alterar somente:
- `seo.title`
- `seo.description`

Depois repetir Admin readback e QA público title/meta.