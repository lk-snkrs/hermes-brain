# Receipt — Production — ASICS Gel NYC guia/FAQ/schema

Data: 20260626T011552Z
Origem: `[LK] Growth`
Aprovação explícita Lucas: publicar em produção o guia/FAQ/schema ASICS Gel NYC preparado no dev theme `155065450718`, limitado ao asset `snippets/lk-goc-guide-contract.liquid`, restrito à collection `/collections/asics-gel-nyc` por handle/id/title, sem alterar SEO title/meta, descrição Admin, produtos, preço, estoque, ordenação, GMC, campanhas, Klaviyo ou checkout.
values_printed=false

## Collection

- URL: `/collections/asics-gel-nyc`
- Collection ID: `1128952955102`
- Produto ACTIVE vinculado: `tenis-asics-gel-nyc-graphite-grey-black-preto`

## Executado

Tema production: `155065417950`
Asset alterado: `snippets/lk-goc-guide-contract.liquid`

Publicado somente o bloco ASICS Gel NYC extraído do DEV, com condição restrita por:
- `collection.handle == 'asics-gel-nyc'`
- collection id `1128952955102`
- title contendo `asics gel nyc` ou `asics gel-nyc`

## Readback asset

Workdir:
`areas/lk/sub-areas/growth/work/asics-gel-nyc-production-20260626/`

Arquivos:
- `prod-snippet-before.liquid`
- `asics-gel-nyc-block-from-dev.liquid`
- `prod-snippet-target.liquid`
- `prod-snippet-readback.liquid`

Readback:
- `matches=true`
- `has_asics_gel_nyc=true`
- `has_guide=true`
- preserva blocos existentes de Lululemon Define e ASICS Gel-1130.

## QA público

URL validada:
`https://lksneakers.com.br/collections/asics-gel-nyc?sort_by=manual&filter.v.price.gte=0&cache=false&qa=asics-nyc-prod-after`

Resultado:
- HTTP 200;
- guia renderizado: `ASICS Gel NYC: running retrô, conforto urbano e presença técnica`;
- FAQ visível;
- FAQPage count = 1;
- sem Liquid error;
- sem `sob encomenda`, `4 a 6 semanas` ou `pronta entrega`.

Regressões checadas:
- `/collections/asics-gel-1130`: HTTP 200, FAQPage 1, sem vazamento ASICS Gel NYC, sem Liquid error.
- `/collections/lululemon-define-jacket`: HTTP 200, FAQPage 1, sem vazamento ASICS Gel NYC, sem Liquid error.
- `/collections/adidas-sambae`: HTTP 200, FAQPage 1, sem Liquid error.
- `/collections/adidas-tokyo`: HTTP 200, FAQPage 1, sem Liquid error.
- `/collections/puma-speedcat`: HTTP 200, FAQPage 1, sem Liquid error.

## Non-actions

Não alterado:
- SEO title/meta;
- descrição Admin;
- produtos;
- preço;
- estoque/Tiny/inventory;
- ordenação;
- GMC;
- campanhas;
- Klaviyo;
- checkout.

## Próximo passo

Medir D+7/D+14. Opcional futuro: ajustar SEO title/meta da collection ASICS Gel NYC em packet separado, pois hoje o Shopify usa title/meta automáticos (`ASICS Gel NYC: 1 modelos | LK Sneakers`).
