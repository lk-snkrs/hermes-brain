# Receipt — Curadoria LK PDP — Production merge SB Dunk Low collabs/cápsulas

Data: 2026-06-06
Executor: Hermes lk-shopify
Status: Production source aplicado e verificado; public HTML respondeu 200 mas não exibiu marker/bloco na captura.

## Aprovação

Lucas aprovou explicitamente após DEV:

`Merge por favor`

## Escopo

Tema DEV: `155065450718` (`unpublished`)
Tema Production: `155065417950` (`main`)
Asset: `snippets/lk-variante-top30-visited-v2.liquid`

Merge scoped: extrair do DEV somente o bloco aprovado `top30-nike-sb-dunk-low-collabs-breadth` e inserir no Production atual, preservando grupos existentes.

## Grupo publicado no source Production

Marker:

`top30-nike-sb-dunk-low-collabs-breadth`

Produtos:

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

Merge script:

- `/opt/data/tmp/lk_merge_sb_dunk_collabs_to_production_20260606.py`

Merge JSON:

- `/opt/data/tmp/lk_curadoria_sb_dunk_collabs_prod_merge_20260606T203957Z.json`

Backup Production antes do merge:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/prod-before-sb-dunk-collabs-20260606T203957Z.liquid`

Target/readback:

- Target: `/opt/data/tmp/lk_curadoria_sb_dunk_collabs_prod_target_20260606T203957Z.liquid`
- Readback: `/opt/data/tmp/lk_curadoria_sb_dunk_collabs_prod_readback_20260606T203957Z.liquid`

QA:

- Script: `/opt/data/tmp/lk_qa_sb_dunk_collabs_production_20260606.py`
- JSON: `/opt/data/tmp/lk_curadoria_sb_dunk_collabs_prod_qa_20260606T203957Z.json`

## Readback / SHA

- DEV SHA before/after: `32a044cf70547725fbeebe9a065e45067826e815508b919e370b5a2377b5b8ae`
- DEV unchanged: `true`
- Production before SHA: `3289f066f3d4202e21148bd2fbaa4f862c85a7fcad4e67ca3749e002af289b60`
- Production target/readback SHA: `142523f70dd41b79be7468a2d5a0a7a9c50f3ae8427febff1c03f06870e51265`
- Readback match: `true`

## Preserve checks

Markers preservados no readback Production:

- `top30-new-balance-9060-adult-breadth`: `1`
- `top30-nike-air-max-1-regular-collabs`: `1`
- `top30-on-running-cloudtilt-regular-loewe`: `1`
- `top30-nike-dunk-low-regular-breadth`: `1`
- novo `top30-nike-sb-dunk-low-collabs-breadth`: `1`

## QA estático

Passou:

- Marker count: `1`
- Arrays handles/labels/images/titles: `10/10/10/10`
- Expected render cards: `5`
- Missing handles: `[]`
- Duplicates: `false`
- Imagens: `10/10` HTTP 200
- URL malformada: `false`
- Placeholder `TenisMoldeLK`: `false`

## QA público

- 10/10 amostras SB responderam HTTP `200`.
- 0/10 capturas continham marker/bloco `lk-variante`/`Outras variações` no HTML retornado.

Interpretação: source Production está correto por Admin Asset API/readback/static QA; render público da superfície Curadoria não foi comprovado nesta bateria. Não é motivo automático para rollback porque o source e preserve checks passaram.

## Rollback

Restaurar o backup Production:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/prod-before-sb-dunk-collabs-20260606T203957Z.liquid`

## Próxima decisão

- Monitorar/retestar público mais tarde; ou
- preparar próxima rodada DEV read-only/aprovação.
