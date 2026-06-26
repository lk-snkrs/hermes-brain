# Receipt — DEV preview — Adidas Samba Marrom guide/FAQ/schema

Data: 20260625T192845Z
Origem: `[LK] Growth`
Tema DEV: `155065450718`
Asset: `snippets/lk-goc-guide-contract.liquid`
Status: DEV preparado; produção intocada.

## Escopo

Preparado guia/FAQ/schema para a collection canônica `adidas-samba-marrom`, após LK Shopify criar/ativar a superfície 200 OK.

## O que foi feito

- Backup DEV antes: `areas/lk/sub-areas/growth/work/adidas-samba-marrom-dev-20260625/dev-snippet-before.liquid`
- Target DEV: `areas/lk/sub-areas/growth/work/adidas-samba-marrom-dev-20260625/dev-snippet-target.liquid`
- Readback DEV: `areas/lk/sub-areas/growth/work/adidas-samba-marrom-dev-20260625/dev-snippet-readback2.liquid`
- Condição restrita por:
  - `collection.handle == 'adidas-samba-marrom'`
  - collection id `1128947417310`
  - title contendo `adidas samba marrom`

## QA

Preview verificado via fetch:
`https://lksneakers.com.br/collections/adidas-samba-marrom?preview_theme_id=155065450718&cache=false&qa=samba-marrom-dev-fetch-20260625`

Resultado:
- Collection 3 itens no preview.
- Guia LK renderizado.
- FAQ visível com 5 perguntas.
- Sem termos proibidos detectados no snippet target: `sob encomenda`, `pronta entrega`, `4 a 6 semanas`.
- Production/main não recebeu write.

Observação: `urllib` sem sessão preview foi redirecionado/servido pelo tema production `155065417950`; por isso a validação final de preview foi feita pelo fetch raw/simplificado, que confirmou `Shopify.previewMode=true` e theme `155065450718`.

## Non-actions

Não alterado:
- Shopify production theme;
- SEO title/meta da collection;
- descrição da collection;
- produtos;
- preço;
- estoque/inventory/Tiny;
- ordenação;
- GMC;
- campanhas;
- Klaviyo;
- checkout.

## Próximo approval necessário

Para publicar em produção, exigir aprovação explícita e escopada para copiar apenas o bloco Adidas Samba Marrom do DEV para production `155065417950`, asset `snippets/lk-goc-guide-contract.liquid`, com rollback/readback público.
