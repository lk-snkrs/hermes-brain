# Receipt — 204L lk-collection-v2 dev

- Data: 2026-05-28 19:32 BRT
- Theme: lk-new-theme/dev
- Theme ID: 155065450718
- Produção alterada: não
- Collection: new-balance-204l
- Asset: sections/lk-collection.liquid

## Mudanças
- 204L migrado para namespace `lk-collection-v2` no dev theme.
- Removido uso do bloco legacy `.lk-204l-coll-preview` para o 204L.
- Tipografia do H1/H2 fixada em `Cormorant Garamond` dentro do namespace v2.
- Bloco editorial pós-grid ajustado para não usar o rótulo “Sinal editorial” na 204L.

## Validação read-only
- `.lk-collection-v2`: presente.
- `.lk-204l-coll-preview` na 204L: ausente.
- H1: Cormorant Garamond, 42.88px no viewport 1280px.
- H2: Cormorant Garamond, 34px no viewport 1280px.
- Collage desktop: 372px de altura.
- Gap entre fim do hero editorial e toolbar/listagem: 0px.
- JSON-LD: 4 blocos presentes.
- Produção: não tocada.

## Preview
https://lksneakers.com.br/collections/new-balance-204l?preview_theme_id=155065450718&lkqa=v2-audit2

## Rollback
Restaurar `sections/lk-collection.liquid` a partir do backup:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/lk-collection-v2-204l-dev-20260528-192814/sections__lk-collection.before.liquid`
