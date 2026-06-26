# Rollback — Production — ASICS Gel NYC guia/FAQ/schema

Data: 20260626T011552Z

## Rollback production

Restaurar no tema production `155065417950` o asset:
`snippets/lk-goc-guide-contract.liquid`

a partir de:
`areas/lk/sub-areas/growth/work/asics-gel-nyc-production-20260626/prod-snippet-before.liquid`

## Validação pós-rollback

- `/collections/asics-gel-nyc` HTTP 200;
- bloco `lk-guia-asics-gel-nyc` ausente;
- FAQPage específico removido da collection;
- sem Liquid error;
- regressões ASICS Gel-1130, Lululemon Define, Sambae, Tokyo e Speedcat sem erro.

Não tocar SEO title/meta, descrição Admin, produtos, preço, estoque, GMC, campanhas, Klaviyo ou checkout.
