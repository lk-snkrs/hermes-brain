# Approval Packet — ASICS Gel NYC — DEV para production

Data: 20260626T011354Z
Status: DEV preparado; production ainda não alterada.

## URL

`/collections/asics-gel-nyc`

## Estado atual

- Collection criada por LK Shopify.
- 1 produto ACTIVE vinculado: `tenis-asics-gel-nyc-graphite-grey-black-preto`.
- Produção HTTP 200.
- FAQPage production atual: 0.
- DEV contém guia/FAQ/schema no asset `snippets/lk-goc-guide-contract.liquid`.

## Recomendação

Publicar em produção o bloco ASICS Gel NYC já preparado em DEV, restrito à collection por handle/id/title.

Opcional em segundo passo: ajustar SEO title/meta da collection, porque hoje o title/meta são gerados automaticamente pelo Shopify (`ASICS Gel NYC: 1 modelos | LK Sneakers`).

## Escopo de publicação production proposto

- Asset: `snippets/lk-goc-guide-contract.liquid`
- Condição: `collection.handle == 'asics-gel-nyc'` ou id `1128952955102` ou title contendo ASICS Gel NYC.
- Não mexer em descrição Admin, produtos, preço, estoque, ordenação, GMC, campanhas, Klaviyo ou checkout.

## Aprovação sugerida

`Aprovo publicar em produção o guia/FAQ/schema ASICS Gel NYC preparado no dev theme 155065450718, limitado ao asset snippets/lk-goc-guide-contract.liquid, restrito à collection /collections/asics-gel-nyc por handle/id/title, sem alterar SEO title/meta, descrição Admin, produtos, preço, estoque, ordenação, GMC, campanhas, Klaviyo ou checkout, com rollback e readback público.`
