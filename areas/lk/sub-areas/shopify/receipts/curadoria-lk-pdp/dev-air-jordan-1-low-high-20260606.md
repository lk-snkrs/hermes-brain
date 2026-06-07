# Receipt — Curadoria LK PDP — DEV Air Jordan 1 Low + High

Data: 2026-06-06
Executor: Hermes lk-shopify
Status: DEV aplicado e verificado por Admin Asset API/readback/static QA; preview público redirecionou para live e ficou inconclusivo.

## Aprovação

Lucas respondeu `Aprovo` após o pedido explícito para subir em DEV: `Aprovo DEV AJ1 Low High`.

## Escopo

Tema DEV: `155065450718` (`unpublished`)
Tema Production: `155065417950` (`main`, verificado sem write)

Asset principal:

- `snippets/lk-variante-top30-visited-v2.liquid`

Novo snippet DEV criado por limite técnico de tamanho:

- `snippets/lk-variante-aj1-low-high-20260606.liquid`

Motivo: tentativa inline no asset principal falhou com Shopify `422` / `Template content exceeds 256 KB limit.` A alternativa segura foi criar snippet separado e inserir apenas um `render` curto no asset principal DEV.

## Markers aplicados em DEV

- `top30-air-jordan-1-low-adult-breadth`
- `top30-air-jordan-1-high-og-breadth`

## Grupos aplicados

### AJ1 Low adulto

- `tenis-air-jordan-1-low-eastside-golf-azul-marinho` — `Eastside Golf`
- `tenis-air-jordan-1-low-elephant-brown-marrom` — `Elephant Brown Marrom`
- `tenis-air-jordan-1-low-floral-canvas-rosa` — `Floral Canvas Rosa`
- `tenis-air-jordan-1-low-lunar-new-year-photon-dust-cinza` — `Lunar New Year Photon Dust`
- `tenis-air-jordan-1-low-multicolor-sashiko-colorido` — `Multicolor Sashiko`
- `tenis-air-jordan-1-low-team-gold-amarelo` — `Team Gold Amarelo`
- `tenis-air-jordan-1-low-year-of-dragon-2024-vinho` — `Year of Dragon 2024`
- `air-jordan-1-low-all-star-carbon-fiber` — `All-Star Carbon Fiber`
- `air-jordan-1-low-alternate-bred-toe` — `Alternate Bred Toe`
- `air-jordan-1-low-aluminium` — `Aluminium Azul`

### AJ1 High/OG adulto

- `tenis-nike-air-jordan-1-high-fragment-design-x-union-la-varsity-red-branco` — `Fragment Design x Union LA V`
- `tenis-air-jordan-1-high-og-black-white-preto` — `OG Black White Preto`
- `tenis-air-jordan-1-high-og-black-metallic-gold-preto` — `OG Black Metallic Gold`
- `tenis-air-jordan-1-high-og-green-glow-verde` — `OG Green Glow Verde`
- `air-jordan-1-high-rebellionaire` — `OG Rebellionaire Cinza`
- `tenis-air-jordan-1-high-og-shattered-backboard-laranja` — `OG Shattered Backboard`
- `tenis-air-jordan-1-high-og-sp-x-travis-scott-mocha` — `OG Sp x Travis Scott Mocha`
- `air-jordan-1-high-og-starfish` — `OG Starfish Laranja`
- `air-jordan-1-high-og-stealth` — `OG Stealth Cinza`
- `tenis-air-jordan-1-high-og-unc-toe-azul` — `OG UNC Toe Azul`

## Artifacts

Packet:

- `/opt/data/tmp/lk_air_jordan_1_low_high_dev_packet_20260606T210430Z.json`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/approval-packets/curadoria-lk-pdp/air-jordan-1-low-high-dev-packet-20260606T210430Z.md`

Apply:

- Failed inline attempt script: `/opt/data/tmp/lk_apply_air_jordan_1_low_high_dev_20260606.py`
- Split-snippet apply script: `/opt/data/tmp/lk_apply_air_jordan_1_low_high_dev_split_20260606.py`
- JSON: `/opt/data/tmp/lk_curadoria_aj1_low_high_dev_apply_20260606T233602Z.json`
- Main readback: `/opt/data/tmp/lk_curadoria_aj1_low_high_dev_main_readback_20260606T233602Z.liquid`
- New snippet readback: `/opt/data/tmp/lk_curadoria_aj1_low_high_dev_snippet_readback_20260606T233602Z.liquid`

Backups:

- Main asset backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-before-aj1-low-high-main-20260606T233602Z.liquid`
- New snippet had no prior content.

QA:

- Script: `/opt/data/tmp/lk_qa_air_jordan_1_low_high_dev_20260606.py`
- JSON: `/opt/data/tmp/lk_curadoria_aj1_low_high_dev_qa_20260606T233602Z.json`

## SHA/readback

- Main before SHA: `32a044cf70547725fbeebe9a065e45067826e815508b919e370b5a2377b5b8ae`
- Main target/readback SHA: `d95f19f7e551d07b95cba8ba4b0a5b88f78342c4ed12ebfc52cf0c87ff51d2a3`
- New snippet target/readback SHA: `cfc3bd2bf953dba718790a8614ece4b8f0ecdb7e2952fb4231beb2298489bc2b`
- Readback match: `true`
- Production unchanged: `true`

## QA estático

Passou:

- Main contém render para `lk-variante-aj1-low-high-20260606`
- `top30-air-jordan-1-low-adult-breadth`: marker `1`, arrays `10/10/10/10`, expected render `5`, missing `[]`
- `top30-air-jordan-1-high-og-breadth`: marker `1`, arrays `10/10/10/10`, expected render `5`, missing `[]`
- Imagens: `20/20` HTTP 200
- Production unchanged: `true`
- URL malformada: `false`
- Placeholder `TenisMoldeLK`: `false`

## Preview público

Tentativa com `preview_theme_id=155065450718` respondeu HTTP 200 para 6 amostras, mas a URL final removeu `preview_theme_id` e caiu em live/canonical. Resultado: preview público inconclusivo, não falha de source.

## Rollback DEV

1. Restaurar o main asset com:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-before-aj1-low-high-main-20260606T233602Z.liquid`

2. Remover o snippet DEV:

`snippets/lk-variante-aj1-low-high-20260606.liquid`

## Próxima decisão

Para Production, o merge terá que considerar dois assets:

- inserir o `render` no main Production;
- criar/atualizar o snippet `snippets/lk-variante-aj1-low-high-20260606.liquid` em Production.
