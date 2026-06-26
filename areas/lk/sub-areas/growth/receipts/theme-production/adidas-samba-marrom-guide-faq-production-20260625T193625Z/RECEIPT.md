# Receipt — Production — Adidas Samba Marrom guide/FAQ/schema

Data: 20260625T193625Z
Origem: `[LK] Growth`
Aprovação: Lucas respondeu “seguir, aprovado” após DEV/readback.
Tema production: `155065417950`
Asset: `snippets/lk-goc-guide-contract.liquid`
values_printed=false

## Escopo executado

Publicado em production somente o bloco Adidas Samba Marrom no asset `snippets/lk-goc-guide-contract.liquid`.

Condição restrita:
- `collection.handle == 'adidas-samba-marrom'`
- collection id contém `1128947417310`
- title contém `adidas samba marrom`

## Artefatos

- Backup production antes: `areas/lk/sub-areas/growth/work/adidas-samba-marrom-production-20260625/prod-before.liquid`
- Bloco aplicado: `areas/lk/sub-areas/growth/work/adidas-samba-marrom-production-20260625/samba-marrom-block.liquid`
- Target production: `areas/lk/sub-areas/growth/work/adidas-samba-marrom-production-20260625/prod-target.liquid`
- Readback production: `areas/lk/sub-areas/growth/work/adidas-samba-marrom-production-20260625/prod-readback2.liquid`

## Readback técnico

- PUT Shopify Admin: HTTP 200.
- Readback asset production: `has_samba=true`, tamanho `32926`, contém Campus/SL72/Gazelle preservados.
- Termos proibidos no bloco: nenhum (`sob encomenda`, `pronta entrega`, `4 a 6 semanas`).

## QA público

URL canônica:
`https://lksneakers.com.br/collections/adidas-samba-marrom`

Resultado:
- Base URL 200 OK, mas ainda serviu cache antigo no primeiro readback pós-publicação (`page_cache`, sem guia).
- URL com filtro/ordenação 200 OK renderizou pelo tema production `155065417950` com:
  - guia Adidas Samba Marrom presente;
  - FAQPage schema presente (`faqpage_count=1`);
  - `Liquid error=false`.

URL pública validada com render production atualizado:
`https://lksneakers.com.br/collections/adidas-samba-marrom?sort_by=manual&filter.v.availability=1&qa=filtered-final`

Interpretação: write production está aplicado e renderiza corretamente; a URL base ainda está em propagação/cache Shopify. Não fiz cache-touch adicional em template/collection porque a aprovação desta etapa ficou limitada ao asset.

## Regressões

Readback público de controle:
- Campus: 200, FAQPage preservado, sem bloco Samba Marrom.
- SL72: 200, FAQPage preservado, sem bloco Samba Marrom.
- Gazelle: 200, FAQPage preservado, sem bloco Samba Marrom.
- Samba geral: 200, FAQPage preservado, sem bloco Samba Marrom.

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
