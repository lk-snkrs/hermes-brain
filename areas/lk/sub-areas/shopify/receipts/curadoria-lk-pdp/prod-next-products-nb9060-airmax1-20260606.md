# Receipt — Curadoria LK PDP — Production merge NB 9060 adultos + Air Max 1

Data: 2026-06-06
Executor: Hermes lk-shopify
Status: Production aplicado e verificado

## Aprovação

Lucas respondeu `1`; foi feita confirmação de segurança via botão/clarify:

`Sim — aprovo merge para Production: NB 9060 adultos + Air Max 1`

## Escopo

Tema DEV: `155065450718` (`unpublished`)
Tema Production: `155065417950` (`main`)
Asset: `snippets/lk-variante-top30-visited-v2.liquid`

Merge scoped: somente os blocos já aprovados/aplicados em DEV:

- `top30-new-balance-9060-adult-breadth`
- `top30-nike-air-max-1-regular-collabs`

## Artifacts

- Script merge: `/opt/data/tmp/lk_merge_next_products_nb9060_airmax1_to_production_20260606.py`
- Merge JSON: `/opt/data/tmp/lk_curadoria_next_products_nb9060_airmax1_prod_merge_20260606T173456Z.json`
- Backup Production antes do write: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/prod-before-next-products-nb9060-airmax1-20260606T173456Z.liquid`
- Target Production: `/opt/data/tmp/lk_curadoria_next_products_nb9060_airmax1_prod_target_20260606T173456Z.liquid`
- Readback Production: `/opt/data/tmp/lk_curadoria_next_products_nb9060_airmax1_prod_readback_20260606T173456Z.liquid`
- QA script: `/opt/data/tmp/lk_qa_next_products_nb9060_airmax1_production_20260606.py`
- QA JSON: `/opt/data/tmp/lk_curadoria_next_products_nb9060_airmax1_prod_qa_20260606T173456Z.json`

## Readback

- DEV source SHA: `d0f835bc1fd639a98688d47f36f3d8532848adb8f4f0a1a1316e6dda5514ff27`
- DEV after SHA: `d0f835bc1fd639a98688d47f36f3d8532848adb8f4f0a1a1316e6dda5514ff27`
- DEV unchanged: `true`
- Production before SHA: `571fb07f73aa1cce794ac8481a645bbbaf46eb98cc52f4092f07d607db3d3acb`
- Production target/readback SHA: `10f3456c5506da3a459715a2781f9a004dae9333ef8b9e76725088c007717738`
- Readback match: `true`

## QA estático Production

Passou:

- `top30-new-balance-9060-adult-breadth`
  - marker count: `1`
  - handles/labels/images/titles: `7/7/7/7`
  - expected render cards: `5`
- `top30-nike-air-max-1-regular-collabs`
  - marker count: `1`
  - handles/labels/images/titles: `8/8/8/8`
  - expected render cards: `5`
- Image checks: `15/15` HTTP 200
- Malformed URLs: `false`
- Placeholder `TenisMoldeLK`: `false`

## Scan pós-Production

Scanner padrão pós-merge:

- `product_count`: `2331`
- DEV: `625` covered handles / `43` groups
- Production: `621` covered handles / `43` groups

Warning conhecido não bloqueante:

- `FutureWarning: Possible set symmetric difference at position 2` no scanner.

## QA público

Primeiro QA público com leitura parcial de 80KB retornou HTML 200 para amostras, mas sem marker/hint — provável corte de captura/camada de cache.

Foi feito QA focado lendo até ~900KB:

- `new-balance-9060-black-cement-black-cat-preto`
  - HTML 200
  - `top30-new-balance-9060-adult-breadth`: `1`
  - `Outras variações`: `1`
- Controle antigo `tenis-new-balance-550-sashiko-pack-pecan-marrom`
  - HTML 200
  - bloco antigo presente
- Air Max 1 amostras:
  - `concepts-x-air-max-1-sp-mellow`: marker `1`, `Outras variações` `1`
  - `travis-scott-x-nike-air-max-1-cactus-brown`: marker `1`, `Outras variações` `1`
  - `tenis-nike-air-max-1-x-patta-monarch-laranja`: marker `1`, `Outras variações` `1`
  - `kasina-x-nike-air-max-1-won-ang-grey`: em retry persistente, marker `1`, `Outras variações` `1`
  - `tenis-nike-air-max-1-x-patta-hyper-crimson-branco`: em retry persistente, marker `1`, `Outras variações` `1`

Interpretação: source/readback correto e storefront público provou render em amostras representativas após leitura completa/retry.

## Rollback

Restaurar Production com:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/prod-before-next-products-nb9060-airmax1-20260606T173456Z.liquid`

## Próximo passo recomendado

Preparar nova rodada read-only/approval packet para:

1. Nike Dunk Low regular
2. Nike SB Dunk Low collabs/cápsulas
