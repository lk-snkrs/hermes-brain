# Receipt — Curadoria LK PDP — merge para Production da rodada completa

Data: 2026-06-06
Executor: Hermes lk-shopify

## Aprovação

Lucas aprovou explicitamente via Telegram: `merge para production`.

## Escopo aprovado

Merge scoped do segmento validado no DEV para Production em:

- Tema DEV: `155065450718` (`unpublished`)
- Tema Production: `155065417950` (`main`)
- Asset: `snippets/lk-variante-top30-visited-v2.liquid`

Escopo do segmento: início do bloco `Adidas Sambae regular` até antes do bloco `New Balance 550 regular/special`.

Incluído no Production:

1. Expansão do grupo `top30-adidas-sambae-regular`
   - `tenis-adidas-sambae-x-hello-kitty-cloud-white-clear-pink-branco` — label `Hello Kitty`
2. Novo grupo `top30-new-balance-2002r-protection-pack`
   - `tenis-new-balance-2002r-protection-pack-phantom-cinza-camurca-mesh` — `Phantom`
   - `tenis-new-balance-2002r-protection-pack-rain-cloud-suede-mesh` — `Rain Cloud`
3. Novo grupo `top30-asics-gel-nyc-regular-special`
   - `tenis-asics-gel-nyc-graphite-grey-black-preto` — `Graphite Grey`
   - `tenis-asics-gel-nyc-x-pleasures-barely-rose-rosa` — `Pleasures Rose`
4. Novo grupo `top30-on-running-cloudtilt-regular-loewe`
   - `tenis-on-running-cloudtilt-preto-e-branco` — `Black Ivory`
   - `tenis-on-running-cloudtilt-loewe-denim-blue-azul` — `Loewe Blue`
   - `tenis-on-running-cloudtilt-loewe-denim-grey-cinza` — `Loewe Grey`

## Método

Merge scoped por Shopify Admin Asset API, não full-file sync cego.

- Source DEV readback SHA: `11e1939aad3adfccc3fb6ea33cf0eb9c7f5050de72803ec45a6d6af2393b773d`
- Production before SHA: `f0b86521f3e85dd528405d2b09655fab98325f92a65d99da51ecbc80438b5723`
- Production target/readback SHA: `571fb07f73aa1cce794ac8481a645bbbaf46eb98cc52f4092f07d607db3d3acb`
- Readback match: `true`
- Segment matches DEV: `true`

## Backups e artifacts

- Backup Production antes do merge:
  `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/prod-before-curadoria-complete-merge-20260606T170254Z.liquid`
- Target aplicado:
  `/opt/data/tmp/lk_curadoria_complete_prod_merge_target_20260606T170254Z.liquid`
- Readback Production:
  `/opt/data/tmp/lk_curadoria_complete_prod_merge_readback_20260606T170254Z.liquid`
- Apply JSON:
  `/opt/data/tmp/lk_curadoria_complete_prod_merge_apply_20260606T170254Z.json`
- QA público JSON:
  `/opt/data/tmp/lk_curadoria_complete_prod_public_qa_20260606.json`

## QA estático / source

Passou no readback Production:

- `top30-adidas-sambae-regular`: marker único, arrays 11/11/11/11, `Hello Kitty` presente, render esperado por PDP: 5 cards.
- `top30-new-balance-2002r-protection-pack`: marker único, arrays 2/2/2/2, render esperado por PDP: 1 card.
- `top30-asics-gel-nyc-regular-special`: marker único, arrays 2/2/2/2, render esperado por PDP: 1 card.
- `top30-on-running-cloudtilt-regular-loewe`: marker único, arrays 3/3/3/3, render esperado por PDP: 2 cards.
- URLs malformadas: `false`.
- Placeholder `TenisMoldeLK`: `false`.

Preserve checks:

- `top30-new-balance-550-regular-special`: count preservado `1 → 1`.
- `top30-air-jordan-3-regular-special`: count preservado `1 → 1`.
- `top30-nike-air-zoom-vomero-5-regular-special`: count preservado `0 → 0`.

## Coverage scan pós-merge

Scanner read-only pós-merge:

- `product_count`: `2331`
- `covered_handles_dev`: `607`
- `covered_handles_prod`: `603`
- `groups_detected_dev`: `41`
- `groups_detected_prod`: `41`

Aviso não bloqueante do scanner: `FutureWarning` no regex `re.split(r'[|~~,\s]+', ...)`, já conhecido.

## QA público

QA público cache-busted rodou 2 ciclos de 3 rounds em amostras Sambae Hello Kitty, NB 2002R Phantom, ASICS Gel-NYC Graphite, Cloudtilt Black e Cloudtilt Grey.

Resultado público no momento do merge: inconclusivo/instável.

- Houve muitos HTTP `503` intermitentes no HTML/JS.
- Quando HTML 200 apareceu nas novas PDPs, o marker novo ainda não apareceu no HTML capturado.
- PDP antiga/controlada NB550 mostrou `lk-variante`, `Outras variações`, `data-lk-variante` e `top30`, provando que a superfície Curadoria renderiza em Production para grupos já propagados.

Interpretação: source/readback Production está correto; storefront público ainda não está estável para confirmar render dos novos grupos. Não fazer rollback só por esse estado inicial sem foco adicional, porque Asset API + static QA provam o source aplicado.

## Rollback

Rollback possível restaurando o backup Production acima no mesmo asset `snippets/lk-variante-top30-visited-v2.liquid` do tema `155065417950`, seguido de readback SHA e QA público.

## Status

- Merge para Production: executado.
- Source/readback/static QA: aprovado.
- Public QA: inconclusivo/instável por 503 e ausência inicial dos novos markers no HTML cache-busted.
