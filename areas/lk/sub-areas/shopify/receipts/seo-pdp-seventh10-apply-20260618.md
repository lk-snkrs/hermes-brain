# Receipt — SEO PDP apply lote 7

Data: 2026-06-18T20:14:36.268496+00:00
Escopo aprovado por Lucas: aplicar no Shopify apenas `seo.title` e `seo.description` dos 10 produtos do lote 7, com snapshot antes, readback Admin depois e QA público.
Sistema: Shopify Admin GraphQL.
Campos alterados: somente `seo.title` e `seo.description` de Product.
Sem alteração de preço, estoque, disponibilidade, descrição de PDP, tags, coleções, tema ou checkout.

## Arquivos

- Snapshot antes: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-seventh-scan-20260618/seo_pdp_seventh10_before_20260618.json`
- Readback depois: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-seventh-scan-20260618/seo_pdp_seventh10_after_readback_20260618.json`
- QA público: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-seventh-scan-20260618/seo_pdp_seventh10_public_qa_20260618.json`
- QA público slow retry/cache edge: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-seventh-scan-20260618/seo_pdp_seventh10_public_slow_retry_20260618.json`

## Execução

- `values_printed=false`
- `apply_count=10`
- `user_errors=[]`
- `all_match=True`

## Produtos alterados

1. `tenis-on-running-cloudsolo-loewe-teal-eggshell-azul-1`
2. `tenis-on-running-cloudsolo-loewe-sand-burgundy-bege`
3. `tenis-on-running-cloudsolo-loewe-taupe-eggshell-marrom`
4. `tenis-on-running-cloudsolo-loewe-teal-eggshell-azul`
5. `tenis-on-running-cloudsolo-loewe-red-eggshell-vermelho`
6. `tenis-on-running-cloudsolo-loewe-black-eggshell-preto`
7. `tenis-jordan-5-retro-white-metallic-2026-metalizado`
8. `tenis-jordan-4-retro-lakers-roxo`
9. `tenis-jordan-4-retro-toro-bravo-2026-vermelho-1`
10. `tenis-jordan-4-retro-toro-bravo-2026-vermelho`

## QA

Admin readback:
- todos os 10 produtos bateram exatamente com os valores-alvo.

QA público:
- `handles_total=10`
- `handles_any_round_match=9`
- `handles_all_rounds_match=1`
- `handles_still_not_public_match=['tenis-on-running-cloudsolo-loewe-teal-eggshell-azul-1']` no QA inicial; slow retry confirmou match em 1 rodada e oscilação posterior de cache público para esse handle, sem Liquid error.
- `slow_retry_any_match=true`
- `slow_retry_liquid_error_count=0`

## Rollback

Para desfazer, restaurar os valores anteriores a partir de:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-seventh-scan-20260618/seo_pdp_seventh10_before_20260618.json`

Rollback deve alterar somente:
- `seo.title`
- `seo.description`

Depois repetir Admin readback e QA público title/meta.