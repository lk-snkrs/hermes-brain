# Validation addendum — corrected collection order next20b

Data: 2026-05-28T14:36:07Z

## Summary

- Coleções processadas: 20
- Shopify `collectionReorderProducts` userErrors: 0
- Total de moves aplicados: 224
- Admin top 8 = regra comercial recomputada: 20/20
- Admin full order = regra comercial recomputada: 20/20
- Público top = Admin top: 19/20 direto

## Public storefront divergence

### Aimé Leon Dore x Porsche (`aime-leon-dore-x-porsche`)

Status técnico/comercial:

- Admin top 8 bate com a regra comercial recomputada: **sim**
- Admin full order bate com a regra comercial recomputada: **sim**
- Público `products.json` retorna apenas 2 produtos disponíveis, por isso `public_top_matches_admin=false` quando comparado estritamente contra top 8 Admin.

Interpretação:

A divergência pública é esperada/aceitável para esta coleção: os 2 produtos que aparecem no público são exatamente os 2 primeiros do Admin e são os únicos storefront-available no retorno público. Os demais itens do Admin estão classificados como `not_storefront_available_final` e não aparecem no `products.json` público.

Top público observado:

1. Boné Aimé Leon Dore x Porsche Colorblock Logo Pristine Off White
2. Boné Aimé Leon Dore Porsche Nylon Logo Jet Black Preto

## Não ações

- Nenhum cron ativado.
- Nenhum produto, preço, estoque, tag, tema, SEO, GMC, checkout ou campanha alterado.
- Mudança restrita à ordenação de coleções MANUAL aprovadas.

## Rollback

Rollback snapshot:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/corrected-apply-next20b-20260528T143607Z/rollback-snapshot-pre-write-immediate.json`
