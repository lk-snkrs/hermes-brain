# Receipt — Curadoria LK PDP — Production merge Air Jordan 1 Low + High

Data: 2026-06-06
Executor: Hermes lk-shopify
Status: Production source aplicado e verificado em dois assets; public HTML respondeu 200 mas não exibiu marker/bloco na captura.

## Aprovação

Lucas aprovou explicitamente:

`Aprovado merge`

## Escopo

Tema DEV: `155065450718` (`unpublished`)
Tema Production: `155065417950` (`main`)

Merge scoped em dois assets por limite Shopify de 256 KB no snippet principal.

Asset principal Production:

- `snippets/lk-variante-top30-visited-v2.liquid`

Novo snippet Production:

- `snippets/lk-variante-aj1-low-high-20260606.liquid`

## O que mudou

1. Criado em Production o snippet dedicado com os grupos AJ1:

`snippets/lk-variante-aj1-low-high-20260606.liquid`

2. Inserido no snippet principal Production apenas o render:

`{%- render 'lk-variante-aj1-low-high-20260606', product: product -%}`

## Markers publicados no source Production

- `top30-air-jordan-1-low-adult-breadth`
- `top30-air-jordan-1-high-og-breadth`

## Produtos

### AJ1 Low adulto

- `tenis-air-jordan-1-low-eastside-golf-azul-marinho`
- `tenis-air-jordan-1-low-elephant-brown-marrom`
- `tenis-air-jordan-1-low-floral-canvas-rosa`
- `tenis-air-jordan-1-low-lunar-new-year-photon-dust-cinza`
- `tenis-air-jordan-1-low-multicolor-sashiko-colorido`
- `tenis-air-jordan-1-low-team-gold-amarelo`
- `tenis-air-jordan-1-low-year-of-dragon-2024-vinho`
- `air-jordan-1-low-all-star-carbon-fiber`
- `air-jordan-1-low-alternate-bred-toe`
- `air-jordan-1-low-aluminium`

### AJ1 High/OG adulto

- `tenis-nike-air-jordan-1-high-fragment-design-x-union-la-varsity-red-branco`
- `tenis-air-jordan-1-high-og-black-white-preto`
- `tenis-air-jordan-1-high-og-black-metallic-gold-preto`
- `tenis-air-jordan-1-high-og-green-glow-verde`
- `air-jordan-1-high-rebellionaire`
- `tenis-air-jordan-1-high-og-shattered-backboard-laranja`
- `tenis-air-jordan-1-high-og-sp-x-travis-scott-mocha`
- `air-jordan-1-high-og-starfish`
- `air-jordan-1-high-og-stealth`
- `tenis-air-jordan-1-high-og-unc-toe-azul`

## Artifacts

Merge script:

- `/opt/data/tmp/lk_merge_air_jordan_1_low_high_to_production_20260606.py`

Merge JSON:

- `/opt/data/tmp/lk_curadoria_aj1_low_high_prod_merge_20260606T234041Z.json`

Backups Production:

- Main asset: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/prod-before-aj1-low-high-main-20260606T234041Z.liquid`
- Snippet dedicado não existia antes (`new_backup: null`).

Readbacks:

- Main: `/opt/data/tmp/lk_curadoria_aj1_low_high_prod_main_readback_20260606T234041Z.liquid`
- Snippet: `/opt/data/tmp/lk_curadoria_aj1_low_high_prod_snippet_readback_20260606T234041Z.liquid`

QA:

- Script: `/opt/data/tmp/lk_qa_air_jordan_1_low_high_production_20260606.py`
- JSON: `/opt/data/tmp/lk_curadoria_aj1_low_high_prod_qa_20260606T234041Z.json`

## SHA/readback

- DEV unchanged: `true`
- Production main before SHA: `142523f70dd41b79be7468a2d5a0a7a9c50f3ae8427febff1c03f06870e51265`
- Production main readback SHA: `c64dafba4777418ac7be08c0dafa6224d6fab8dafe3b0aa61029ba7b63f9da8d`
- Production new snippet readback SHA: `4d612836286a203e89325d38dde29ec5ceaf3de324276b76c2bdc3c6cb77b7f0`
- Readback match: `true`

## Preserve checks

Markers preservados no main Production:

- `top30-new-balance-9060-adult-breadth`: `1`
- `top30-nike-air-max-1-regular-collabs`: `1`
- `top30-on-running-cloudtilt-regular-loewe`: `1`
- `top30-nike-dunk-low-regular-breadth`: `1`
- `top30-nike-sb-dunk-low-collabs-breadth`: `1`

## QA estático

Passou:

- Main contém render do snippet dedicado: `true`
- `top30-air-jordan-1-low-adult-breadth`: marker `1`, arrays `10/10/10/10`, expected render `5`
- `top30-air-jordan-1-high-og-breadth`: marker `1`, arrays `10/10/10/10`, expected render `5`
- Imagens: `20/20` HTTP 200
- URL malformada: `false`
- Placeholder `TenisMoldeLK`: `false`

## QA público

- 12/12 amostras responderam HTTP `200`.
- 0/12 capturas continham os markers AJ1 ou `lk-variante`/`Outras variações`.
- 2/12 capturas tinham texto `Curadoria LK` sem marker do bloco novo.

Interpretação: Production source/readback/static QA está correto. Render público do bloco AJ1 não foi comprovado nesta bateria, consistente com caveat recente em outras rodadas onde o HTML público não mostrou a superfície apesar de readback correto.

## Rollback Production

1. Restaurar o main asset:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/prod-before-aj1-low-high-main-20260606T234041Z.liquid`

2. Remover o snippet Production:

`snippets/lk-variante-aj1-low-high-20260606.liquid`

## Próxima decisão

- Monitorar/retestar público mais tarde; ou
- continuar com próxima rodada DEV read-only/approval packet.
