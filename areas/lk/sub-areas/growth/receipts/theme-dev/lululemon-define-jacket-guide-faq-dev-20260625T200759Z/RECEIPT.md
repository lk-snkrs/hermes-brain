# Receipt — DEV preview — Lululemon Define Jacket guide/FAQ/schema

Data: 20260625T200759Z
Origem: `[LK] Growth`
Tema DEV: `155065450718`
Asset: `snippets/lk-goc-guide-contract.liquid`
Status: DEV preparado; produção intocada.

## Pré-requisito Shopify

Collection canônica criada/ativada:
- URL: `https://lksneakers.com.br/collections/lululemon-define-jacket`
- Handle: `lululemon-define-jacket`
- Legacy ID: `1128948367582`
- Produtos: 6 ACTIVE
- Receipt Shopify consolidado: `areas/lk/sub-areas/shopify/receipts/lululemon-define-jacket-collection-20260625T200548Z.md`

## Escopo Growth DEV

Preparado guia/FAQ/schema para a collection canônica `lululemon-define-jacket`.

Condição restrita por:
- `collection.handle == 'lululemon-define-jacket'`
- collection id `1128948367582`
- title contendo `lululemon define jacket`

## Artefatos

- Backup DEV antes: `areas/lk/sub-areas/growth/work/lululemon-define-jacket-dev-20260625/dev-snippet-before.liquid`
- Target DEV: `areas/lk/sub-areas/growth/work/lululemon-define-jacket-dev-20260625/dev-snippet-target.liquid`
- Readback DEV: `areas/lk/sub-areas/growth/work/lululemon-define-jacket-dev-20260625/dev-snippet-readback2.liquid`

## QA

Preview verificado via fetch:
`https://lksneakers.com.br/collections/lululemon-define-jacket?preview_theme_id=155065450718&cache=false&qa=lululemon-define-dev-fetch`

Resultado:
- Collection 6 itens no preview.
- Guia LK renderizado.
- FAQ visível com 5 perguntas.
- Copy cobre Nulu vs Luon, cropped vs regular, fit/modelagem, uso athleisure e autenticidade.
- Sem termos proibidos no bloco: `sob encomenda`, `pronta entrega`, `4 a 6 semanas`.
- Production/main não recebeu write.

Observação técnica: `urllib` sem sessão preview serviu production `155065417950`; por isso a validação de preview foi feita pelo fetch que confirmou o conteúdo renderizado do preview.

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

Para publicar em produção, exigir aprovação explícita e escopada para copiar apenas o bloco Lululemon Define Jacket do DEV para production `155065417950`, asset `snippets/lk-goc-guide-contract.liquid`, com rollback/readback público e regressão de Samba Marrom/Campus/SL72/Gazelle.
