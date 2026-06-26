# Rollback — DEV — ASICS Gel NYC guia/FAQ/schema

Data: 20260626T011354Z

## Rollback DEV

Restaurar no tema DEV `155065450718` o asset:
`snippets/lk-goc-guide-contract.liquid`

a partir de:
`areas/lk/sub-areas/growth/work/asics-gel-nyc-dev-20260626/dev-snippet-before.liquid`

## Produção

Nenhum rollback production necessário nesta etapa: theme production não foi alterado para ASICS Gel NYC.

## Validação pós-rollback

- preview `/collections/asics-gel-nyc?preview_theme_id=155065450718` sem bloco ASICS Gel NYC;
- produção permanece HTTP 200;
- sem Liquid error;
- sem alteração de produtos/preço/estoque/GMC/Klaviyo/campanhas/checkout.
