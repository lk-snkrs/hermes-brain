# Receipt — Curadoria LK PDP — DEV SB Dunk Low collabs/cápsulas

Data: 2026-06-06
Executor: Hermes lk-shopify
Status: DEV aplicado e verificado por Admin Asset API/readback/static QA; preview público redirecionou para live e ficou inconclusivo.

## Aprovação

Lucas respondeu `Aprovo` após o pedido explícito para subir o packet `Aprovo DEV SB Dunk collabs`. Interpretação operacional: aprovação atual para upload em DEV/unpublished somente.

## Escopo

Tema DEV: `155065450718` (`unpublished`)
Tema Production: `155065417950` (`main`, somente verificado como controle; sem write)
Asset: `snippets/lk-variante-top30-visited-v2.liquid`

Marker aplicado em DEV:

`top30-nike-sb-dunk-low-collabs-breadth`

## Grupo aplicado

- `albino-preto-x-nike-sb-dunk-low-pearl-white` — `Albino & Preto`
- `april-skateboards-x-nike-sb-dunk-low-turbo-green` — `April Turbo`
- `ben-jerrys-x-dunk-low-sb-chunky-dunky` — `Chunky Dunky`
- `born-x-raised-x-nike-sb-dunk-low-one-block-at-a-time` — `Born x Raised`
- `concepts-x-nike-sb-dunk-low-orange-lobster` — `Orange Lobster`
- `crenshaw-skate-club-x-nike-sb-dunk-low` — `Crenshaw`
- `fly-streetwear-x-dunk-low-pro-sb-gardenia` — `Fly Gardenia`
- `grateful-dead-x-nike-sb-dunk-low-yellow-bear` — `Grateful Dead`
- `jarritos-x-nike-sb-dunk-low` — `Jarritos`
- `huf-x-nike-sb-dunk-low-new-york` — `HUF New York`

## Artifacts

Packet:

- `/opt/data/tmp/lk_sb_dunk_collabs_packet_20260606T191558Z.json`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/approval-packets/curadoria-lk-pdp/sb-dunk-low-collabs-dev-packet-20260606T191558Z.md`

Apply:

- Script: `/opt/data/tmp/lk_apply_sb_dunk_collabs_dev_20260606.py`
- JSON: `/opt/data/tmp/lk_curadoria_sb_dunk_collabs_dev_apply_20260606T191846Z.json`
- Target: `/opt/data/tmp/lk_curadoria_sb_dunk_collabs_dev_target_20260606T191846Z.liquid`
- Readback: `/opt/data/tmp/lk_curadoria_sb_dunk_collabs_dev_readback_20260606T191846Z.liquid`

Backup DEV antes do PUT:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-before-sb-dunk-collabs-20260606T191846Z.liquid`

QA:

- Script: `/opt/data/tmp/lk_qa_sb_dunk_collabs_dev_20260606.py`
- JSON: `/opt/data/tmp/lk_curadoria_sb_dunk_collabs_dev_qa_20260606T191846Z.json`

## SHA/readback

- DEV before SHA: `3a8e1987300c5f5b1e067922d10c8d3bf7c92ce3501bae5b6c10551781b43f93`
- DEV target/readback SHA: `32a044cf70547725fbeebe9a065e45067826e815508b919e370b5a2377b5b8ae`
- Readback match: `true`
- Production contained marker before apply: `false`

## QA estático

Passou:

- Marker count: `1`
- Arrays handles/labels/images/titles alinhados: `10/10/10/10`
- Expected render cards por PDP: `5`
- Missing handles: `[]`
- Duplicate handles: `false`
- Imagens: `10/10` HTTP 200
- PDP público dos candidatos antes do write: `10/10` HTTP 200
- URL malformada: `false`
- Placeholder `TenisMoldeLK`: `false`

## Preview público

Tentativa com `preview_theme_id=155065450718` respondeu HTTP 200 para 5 amostras, mas a URL final removeu `preview_theme_id` e caiu em live/canonical. Resultado: preview público inconclusivo, não falha de source.

## Rollback DEV

Restaurar via Asset API o backup:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-before-sb-dunk-collabs-20260606T191846Z.liquid`

## Próxima decisão

Se aprovado, preparar merge para Production do marker `top30-nike-sb-dunk-low-collabs-breadth` usando o readback DEV como fonte canônica e preservando Production atual.
