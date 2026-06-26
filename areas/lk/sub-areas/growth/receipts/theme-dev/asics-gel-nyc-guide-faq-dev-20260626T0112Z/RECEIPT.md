# Receipt — DEV — ASICS Gel NYC guia/FAQ/schema

Data: 20260626T011354Z
Origem: `[LK] Growth`
Escopo: preparar DEV/preview após LK Shopify criar `/collections/asics-gel-nyc`.
values_printed=false

## Collection

- URL: `/collections/asics-gel-nyc`
- Collection ID: `1128952955102`
- Produto ACTIVE vinculado: `tenis-asics-gel-nyc-graphite-grey-black-preto`
- Produção antes: HTTP 200, `FAQPage=0`, sem Liquid error.

## Executado

Tema DEV: `155065450718`
Asset: `snippets/lk-goc-guide-contract.liquid`

Adicionado bloco condicional restrito por:
- `collection.handle == 'asics-gel-nyc'`
- collection id `1128952955102`
- title contendo `asics gel nyc` ou `asics gel-nyc`

Conteúdo preparado:
- guia visual pós-grid;
- FAQ visível;
- FAQPage schema no asset DEV;
- linguagem premium/comercial, sem disponibilidade/estoque/prazo operacional.

## Evidência

Workdir:
`areas/lk/sub-areas/growth/work/asics-gel-nyc-dev-20260626/`

Arquivos:
- `asics-gel-nyc-admin-before.json`
- `dev-snippet-before.liquid`
- `prod-snippet-before.liquid`
- `dev-snippet-target.liquid`
- `dev-snippet-readback.liquid`

Readback asset DEV:
- `matches=true`
- `has_asics_gel_nyc=true`
- `has_guide=true`
- preserva blocos existentes: Taekwondo, Lululemon Define, ASICS Gel-1130.

Preview markdown validado:
- URL com `preview_theme_id=155065450718`
- guia `ASICS Gel NYC: running retrô, conforto urbano e presença técnica` renderizado;
- FAQ visível;
- sem Liquid error;
- sem `sob encomenda`, `4 a 6 semanas` ou `pronta entrega`.

Observação: validação raw HTML do preview não refletiu o theme preview/cookie de forma consistente, mas o asset DEV foi lido de volta com o schema e o preview simplificado renderizou o bloco visual. Produção foi checada separadamente e segue sem o bloco ASICS Gel NYC.

## Produção

Não alterada para o guia/schema ASICS Gel NYC nesta etapa.

Produção atual:
- HTTP 200;
- `FAQPage=0` para ASICS Gel NYC;
- sem Liquid error;
- sem termos operacionais antigos.

## Non-actions

Não alterado:
- preço;
- estoque/Tiny/inventory;
- produtos;
- ordenação;
- GMC;
- campanhas;
- Klaviyo;
- checkout;
- theme production.

## Próximo passo

Se aprovado, publicar em production o bloco ASICS Gel NYC no asset `snippets/lk-goc-guide-contract.liquid`, mantendo condição restrita por handle/id/title, com rollback e readback público. Opcionalmente ajustar SEO title/meta da collection porque hoje o Shopify gera título/meta automáticos (`ASICS Gel NYC: 1 modelos | LK Sneakers`).
