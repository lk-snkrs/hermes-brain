# Ahrefs Schema — pacote de 100 — sublote 04/04, URLs 76–100

Data UTC: `2026-06-18T22:56:19Z`
Escopo: read-only; writes externos = 0; values_printed=false

## Escopo

Sublote 04 de 25 URLs do pacote de 100 URLs prioritárias do issue Ahrefs:

- `Structured data has schema.org validation error`
- Base: Ahrefs full audit `20260618T202702Z`
- Ranking: top 100 por `traffic` desc e `page_rating` desc
- Este sublote: ranks `76–100`

## Resultado do sublote

- URLs auditadas: `25`
- HTTP público: páginas 200 no dataset Ahrefs; extração JSON-LD OK nas amostras fetchadas
- Tipos encontrados:
  - Collections: `BreadcrumbList`, `CollectionPage`, objeto global `Organization/ShoeStore/ClothingStore`
  - Pages institucionais/guias: objeto global `Organization/ShoeStore/ClothingStore`
- `jsonld_validation_kinds` no CSV Ahrefs veio vazio, então a causa exata precisa ser inferida por inspeção do JSON-LD e/ou validação externa.

## URLs do sublote

- 76 `/collections/roupas`
- 77 `/collections/saint-studio`
- 78 `/collections/sale`
- 79 `/collections/shorts`
- 80 `/collections/slyce`
- 81 `/collections/sufgang`
- 82 `/collections/uniqlo-x-kaws`
- 83 `/pages/acompanhe-seu-pedido`
- 84 `/pages/adidas-modelos`
- 85 `/pages/adidas-samba-vs-campus-00s`
- 86 `/pages/contato`
- 87 `/pages/garantia-de-autenticidade-lk`
- 88 `/pages/instrucoes-de-compra`
- 89 `/pages/jordan-4-guia-2026`
- 90 `/pages/lk-na-imprensa`
- 91 `/pages/new-balance-530-vs-2002r`
- 92 `/pages/new-balance-9060-guia`
- 93 `/pages/new-balance-modelos`
- 94 `/pages/nike-modelos`
- 95 `/pages/onitsuka-tiger-modelos`
- 96 `/pages/onitsuka-tiger-vs-asics-gel-1130`
- 97 `/pages/politica-de-devolucao-e-reembolso`
- 98 `/pages/politica-de-frete`
- 99 `/pages/politica-de-privacidade`
- 100 `/pages/politica-de-termos-de-uso`

## Causa provável

O erro não parece ser página-a-página. O padrão é global, vindo de:

- `sections/lk-header.liquid`
- bloco `Organization + ClothingStore JSON-LD (SD-03)`
- renderiza em todas as páginas pelo header group

Objeto atual:

- `@type`: `["Organization", "ShoeStore", "ClothingStore"]`
- inclui campos locais bons: `address`, `geo`, `openingHoursSpecification`, `telephone`, `sameAs`, etc.
- inclui campos mais propensos a erro em validação estrita:
  - `hasMerchantReturnPolicy`
  - `shippingDetails`
  - possivelmente `aggregateRating` em objeto global de loja/organization

Hipótese principal: Ahrefs/Schema.org está marcando propriedades de oferta/comércio (`OfferShippingDetails`, `MerchantReturnPolicy`) anexadas ao objeto global `Organization/ShoeStore/ClothingStore`. Esses campos são mais seguros quando ligados a `Product/Offer` ou removidos do schema global.

## Recomendação conservadora

Não mexer página por página.

Preparar patch em dev theme para o schema global:

1. Remover `shippingDetails` do objeto global `Organization/ShoeStore/ClothingStore`.
2. Remover `hasMerchantReturnPolicy` do objeto global, ou mover para lugar semanticamente correto se necessário.
3. Manter dados locais e de confiança:
   - `Organization/ShoeStore/ClothingStore`
   - `name`, `url`, `logo`, `image`
   - `address`, `geo`, `hasMap`, `telephone`
   - `openingHoursSpecification`
   - `sameAs`
   - `priceRange`, `paymentAccepted`, `currenciesAccepted`
4. Avaliar `aggregateRating` separadamente:
   - manter no micro-piloto se validação externa passar;
   - remover se Ahrefs continuar acusando após retirada de shipping/return.

## Impacto esperado

Como o bloco é global, um único patch em `lk-header.liquid` pode reduzir milhares das `10.003` ocorrências de schema.org validation error.

## Risco

- Baixo/médio para SEO: remove campos potencialmente inválidos de schema global.
- Baixo para UX: nenhuma mudança visual.
- Médio para rich results se o Google usava esses campos globais, mas Product/Offer schema deve ser a fonte mais correta para shipping/return.

## Approval necessário

Próximo passo seguro:

- aplicar patch somente em dev theme;
- validar 5 URLs com schema extraído;
- se OK, pedir aprovação separada para production.

## Arquivos gerados

- `schema-top100-sublote-04-rows76-100.csv`
- `schema-sublote04-jsonld-audit.json`
- `schema-sublote04-jsonld-audit-summary.csv`
- `lk-header-production-readonly.liquid`
