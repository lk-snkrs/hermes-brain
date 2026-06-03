# Receipt — AJ1 Low OG regular Curadoria hotfix — 2026-06-02

## Veredito
Hotfix aplicado em Production para corrigir PDP `tenis-air-jordan-1-low-og-mocha-marrom` e família AJ1 Low OG regular.

O grupo `top30-air-jordan-1-low-og-regular` foi desativado/removido do snippet porque renderizava labels longos e UX quebrada no bloco Curadoria LK.

## Assets tocados
- `snippets/lk-variante-top30-visited.liquid`
  - antes: `a62a0ba774c3`
  - depois/readback: `96044f026d31`
  - marker `top30-air-jordan-1-low-og-regular` no readback: `0`
- `sections/lk-pdp.liquid`
  - touch/recompilação para limpar render cacheado da Shopify
  - antes: `af4999c2fd1d`
  - depois/readback: `dfbae21956d2`

## Motivo do touch da section
Após o readback do snippet, o storefront `.com.br` ainda serviu HTML antigo em algumas rotas. A section ativa que chama o snippet é `sections/lk-pdp.liquid`; o touch mínimo forçou recompilação/propagação.

## QA live final
- handles verificados: `12`
- duplicates: `0`
- forbidden stale groups: `0`
- Liquid errors: `0`
- pass: `True`

Amostras-chave:
- `tenis-air-jordan-1-low-og-mocha-marrom`: 0 bloco Curadoria LK após hotfix.
- `tenis-air-jordan-1-low-og-barrons-cinza`: 0 bloco Curadoria LK após hotfix.
- `tenis-new-balance-530-arid-stone-cinza`: 1 bloco apenas, `top30-nb-530`.
- `tenis-air-jordan-1-low-midnight-navy-wolf-grey-azul-marinho`: 1 bloco, `air-jordan-1-low`.

## GitHub sync
- Repo: `lk-snkrs/lk-new-theme`
- Branch: `production`
- Sync pass: `True`

## Rollback
Backups:
- Snippet before: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/aj1-og-regular-production-hotfix-20260602T200907Z/production-before.liquid`
- Bloco removido: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/aj1-og-regular-production-hotfix-20260602T200907Z/removed-block.liquid`
- Section before: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/aj1-og-regular-production-hotfix-20260602T200907Z/lk-pdp.before.liquid`

Rollback do hotfix:
1. Restaurar `snippets/lk-variante-top30-visited.liquid` de `production-before.liquid`; ou reinserir `removed-block.liquid` no ponto do comentário de hotfix.
2. Restaurar `sections/lk-pdp.liquid` de `lk-pdp.before.liquid` se quiser remover o comentário de touch.

## Não alterado
Não foram alterados produtos, preço, estoque, checkout, apps, GMC/feed, Klaviyo, Meta, Tiny, campanhas ou menus.
