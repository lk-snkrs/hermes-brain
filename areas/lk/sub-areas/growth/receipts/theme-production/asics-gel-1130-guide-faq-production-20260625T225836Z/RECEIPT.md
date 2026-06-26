# Receipt — Production — ASICS Gel-1130 guide/FAQ/schema

Data: 20260625T225836Z
Origem: `[LK] Growth`
Aprovação: Lucas respondeu `Aprovo` após DEV/readback.
Tema production: `155065417950`
Asset: `snippets/lk-goc-guide-contract.liquid`
values_printed=false

## Escopo executado

Publicado em production somente o bloco ASICS Gel-1130 no asset `snippets/lk-goc-guide-contract.liquid`.

Condição restrita:
- `collection.handle == 'asics-gel-1130'`
- collection id contém `1128948203742`
- title contém `asics gel-1130` ou `asics gel 1130`

## Artefatos

- Backup production antes: `areas/lk/sub-areas/growth/work/asics-gel-1130-production-20260625/prod-before.liquid`
- Bloco aplicado: `areas/lk/sub-areas/growth/work/asics-gel-1130-production-20260625/asics-gel-1130-block.liquid`
- Target production: `areas/lk/sub-areas/growth/work/asics-gel-1130-production-20260625/prod-target.liquid`
- Readback production: `areas/lk/sub-areas/growth/work/asics-gel-1130-production-20260625/prod-readback2.liquid`

## Readback técnico

- PUT Shopify Admin: HTTP 200.
- Readback asset production: `has_asics=true`, tamanho `48680`, `matches=true`.
- Blocos existentes preservados: Lululemon Define, Adidas Samba Marrom, Campus, SL72 e Gazelle.
- Termos proibidos no bloco: nenhum (`sob encomenda`, `pronta entrega`, `4 a 6 semanas`).

## QA público

URL canônica:
`https://lksneakers.com.br/collections/asics-gel-1130`

Resultado:
- URL base 200 OK.
- Guia ASICS Gel-1130 presente.
- FAQPage schema presente (`faqpage_count=1`).
- `Liquid error=false`.
- Tema production `155065417950`.

URL pública validada:
`https://lksneakers.com.br/collections/asics-gel-1130?sort_by=manual&filter.v.availability=1&qa=asics-prod-fetch`

## Regressões

Readback público de controle:
- Lululemon Define: 200, FAQPage preservado, sem vazamento ASICS.
- Adidas Samba Marrom: 200, FAQPage preservado, sem vazamento ASICS.
- Campus: 200, FAQPage preservado, sem vazamento ASICS.
- SL72: 200, FAQPage preservado, sem vazamento ASICS.
- Gazelle: 200, FAQPage preservado, sem vazamento ASICS.

## Non-actions confirmadas

Não alterado:
- SEO title/meta da collection;
- descrição da collection;
- produtos;
- preço;
- estoque/Tiny/inventory;
- ordenação;
- GMC;
- campanhas;
- Klaviyo;
- checkout;
- outros assets/theme files.

## Rollback

Restaurar `prod-before.liquid` no tema production `155065417950`, asset `snippets/lk-goc-guide-contract.liquid`.
