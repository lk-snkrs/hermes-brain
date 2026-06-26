# Receipt — Curadoria LK PDP — Air Jordan 3 + Vomero 5 DEV — 2026-06-06

## Escopo aprovado

Lucas aprovou explicitamente: `Aprovo DEV Curadoria Air Jordan 3 + Vomero 5`.

## Shopify write

- Tema DEV: `155065450718`
- Role: `unpublished`
- Asset: `snippets/lk-variante-top30-visited-v2.liquid`
- Ação: `PUT`
- Production: não alterado
- Produtos/preços/estoque/checkout/apps: não alterados

## Grupos aplicados

### Air Jordan 3

- Marker: `top30-air-jordan-3-regular-special`
- Handles: `4`
- Labels: `4`
- Images: `4`
- Titles: `4`

Handles:

- `tenis-nike-air-jordan-3-og-rare-air-preto`
- `tenis-air-jordan-3-retro-black-cat-preto`
- `tenis-air-jordan-3-retro-x-j-balvin-rio-preto`
- `tenis-air-jordan-3-retro-x-wnba-desert-camo-bege`

### Nike Zoom Vomero 5

- Marker: `top30-nike-zoom-vomero-5-regular-special`
- Handles: `4`
- Labels: `4`
- Images: `4`
- Titles: `4`

Handles:

- `tenis-nike-air-zoom-vomero-5-doernbecher-2023-laranja`
- `tenis-nike-zoom-vomero-5-metallic-silver-blue-tint-prateado-azul`
- `tenis-nike-zoom-vomero-5-metallic-silver-platinum-violet-prateado-violeta`
- `tenis-nike-zoom-vomero-5-photon-dust-metallic-silver-cinza`

## Readback DEV

- SHA antes: `d12399d85661b323c34fbb77b20a5ed7dd0f7a5b668ec46e91374194a267e725`
- SHA depois final: `114bd5b4e097e32ac2c6419ac22870372c75129265ebac2402397a890ad47230`
- Convergência marker após primeiro PUT: tentativa `2`
- Ajuste pós-readback: removi aspas escapadas do title `J Balvin "Rio"` para estabilizar a string Liquid/QA; readback final ok na tentativa `2`.

Arquivos:

- Backup antes: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-air-jordan-3-vomero-5-dev-20260606/20260606T153614Z-dev-theme-155065450718-before.liquid`
- Readback final: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-air-jordan-3-vomero-5-dev-20260606/20260606T153726Z-postfix-readback.liquid`
- Receipt inicial: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-air-jordan-3-vomero-5-dev-20260606/20260606T153614Z-receipt.json`
- Receipt final: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-air-jordan-3-vomero-5-dev-20260606/20260606T153726Z-postfix-receipt.json`

## QA estático final

Para ambos os markers:

- Marker count: `1`
- Handles presentes: `4/4`
- Labels presentes: `4/4`
- Images presentes: `4/4`
- Titles presentes: `4/4`
- Duplicate handles: `0`
- Bad URLs: `0`

## QA visual/computed DEV

### Air Jordan 3

URL testada:

`https://lksneakers.com.br/products/tenis-nike-air-jordan-3-og-rare-air-preto?preview_theme_id=155065450718&hermes_qa=dev_aj3_vomero_1`

Resultado:

- Bloco renderizou: `true`
- Marker: `top30-air-jordan-3-regular-special`
- Título: `Outras variações`
- `titleFontWeight`: `300`
- `labelText`: `Black Cat`
- `labelFontWeight`: `300`
- `labelAfterContent`: `none`
- `labelAfterFontWeight`: `300`

### Nike Zoom Vomero 5

URL testada:

`https://lksneakers.com.br/products/tenis-nike-zoom-vomero-5-photon-dust-metallic-silver-cinza?preview_theme_id=155065450718&hermes_qa=dev_aj3_vomero_2`

Resultado:

- Bloco renderizou: `true`
- Marker: `top30-nike-zoom-vomero-5-regular-special`
- Título: `Outras variações`
- `titleFontWeight`: `300`
- `labelText`: `Doernbecher`
- `labelFontWeight`: `300`
- `labelAfterContent`: `none`
- `labelAfterFontWeight`: `300`

## Caveat

Cada grupo tem `4` produtos. Em um PDP individual, o produto atual é excluído, então aparecem até `3` alternativas.

## Rollback

Restaurar o backup antes no asset `snippets/lk-variante-top30-visited-v2.liquid` do tema DEV `155065450718`.
