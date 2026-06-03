# LKGOC — Visual/Liquid contract

## Princípios

- Coleção é produto-first; grid não pode ser empurrado por artigo longo.
- Guia dedicado usa shell editorial premium tipo Moon Shoe; não usar `main-page` estreito/artigo cru.
- Blocos específicos por `collection.handle`; não contaminar coleção global.

## Técnica Shopify

- Preferir snippet dedicado + `render` condicionado por handle quando section global estiver pesada.
- Não inflar `sections/*.liquid` perto do limite Shopify 256 KB.
- Usar classes específicas por modelo, exemplo `lk-samba-jane-coll-preview`.
- DEV markers são permitidos só em DEV; production não deve manter comentários/markers visíveis ou técnicos.
- Todo upload precisa readback/sha/marker check quando aplicável.

## QA visual

- Desktop screenshot.
- Mobile screenshot.
- Comparar com 204L para coleção.
- Comparar com Moon Shoe para guia.
- Verificar CTA, FAQ, grid, filtros/ordenação e ausência de overflow mobile.
