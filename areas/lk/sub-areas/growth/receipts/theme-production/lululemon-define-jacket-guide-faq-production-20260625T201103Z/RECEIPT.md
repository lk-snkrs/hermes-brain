# Receipt — Production — Lululemon Define Jacket guide/FAQ/schema

Data: 20260625T201103Z
Origem: `[LK] Growth`
Aprovação: Lucas respondeu `aprovo` após DEV/readback.
Tema production: `155065417950`
Asset: `snippets/lk-goc-guide-contract.liquid`
values_printed=false

## Escopo executado

Publicado em production somente o bloco Lululemon Define Jacket no asset `snippets/lk-goc-guide-contract.liquid`.

Condição restrita:
- `collection.handle == 'lululemon-define-jacket'`
- collection id contém `1128948367582`
- title contém `lululemon define jacket`

## Artefatos

- Backup production antes: `areas/lk/sub-areas/growth/work/lululemon-define-jacket-production-20260625/prod-before.liquid`
- Bloco aplicado: `areas/lk/sub-areas/growth/work/lululemon-define-jacket-production-20260625/lululemon-define-block.liquid`
- Target production: `areas/lk/sub-areas/growth/work/lululemon-define-jacket-production-20260625/prod-target.liquid`
- Readback production: `areas/lk/sub-areas/growth/work/lululemon-define-jacket-production-20260625/prod-readback2.liquid`

## Readback técnico

- PUT Shopify Admin: HTTP 200.
- Readback asset production: `has_lululemon_define=true`, tamanho `40888`, `matches=true`.
- Blocos existentes preservados: Adidas Samba Marrom, Campus, SL72 e Gazelle.
- Termos proibidos no bloco: nenhum (`sob encomenda`, `pronta entrega`, `4 a 6 semanas`).

## QA público

URL canônica:
`https://lksneakers.com.br/collections/lululemon-define-jacket`

Resultado:
- URL base 200 OK, mas ainda serviu cache antigo no primeiro readback pós-publicação (`page_cache`, sem guia).
- URL pública com query de QA renderizou pelo tema production `155065417950` com:
  - guia Lululemon Define Jacket presente;
  - FAQPage schema presente (`faqpage_count=1`);
  - `Liquid error=false`.

Interpretação: write production está aplicado e renderiza corretamente; a URL base ainda está em propagação/cache Shopify. Não fiz cache-touch adicional em template/collection porque a aprovação desta etapa ficou limitada ao asset.

## Regressões

Readback público de controle:
- Adidas Samba Marrom: 200, FAQPage preservado, sem vazamento Define.
- Campus: 200, FAQPage preservado, sem vazamento Define.
- SL72: 200, FAQPage preservado, sem vazamento Define.
- Gazelle: 200, FAQPage preservado, sem vazamento Define.

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
