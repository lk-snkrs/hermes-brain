# Receipt — Curadoria LK PDP Production NB9060 merge (2026-06-08)

- values_printed: false
- gerado: 2026-06-08 08:27:42 BRT
- aprovação interpretada: Lucas respondeu `Aprovo` em reply direto ao status DEV que indicava como próxima decisão `Aprovo merge Production Curadoria NB9060 via GitHub`; interpretado como aprovação atual para merge Production via GitHub, não Asset API direto.
- caminho Production: GitHub PR → branch `production` → sync Shopify → Admin Asset API readback/QA.
- direct Production Asset API write por Hermes: não executado.

## Escopo

- Theme Production: `lk-new-theme/production` / theme `155065417950` / role `main`.
- Main asset: `snippets/lk-variante-top30-visited-v2.liquid`.
- Split asset: `snippets/lk-variante-nb9060-expansion-20260608.liquid`.
- Marker: `top30-new-balance-9060-expansion-20260608`.
- Mudança: criar split snippet NB9060 e adicionar 1 render line no main Curadoria Production.
- Fora de escopo: produto, preço, estoque, coleção, metafield, GMC, Klaviyo, ads, checkout, desconto, fulfillment e campanha.

## Reconciliation antes do PR

- Shopify Production main SHA12 antes: `a377c2ca1168`.
- `origin/production:snippets/lk-variante-top30-visited-v2.liquid` SHA12 antes: `a377c2ca1168`.
- Split NB9060 não existia em Shopify Production antes do merge.
- Conclusão: GitHub production estava reconciliado com Shopify Production para o asset alvo antes da alteração.

## GitHub

- Repo: `lk-snkrs/lk-new-theme`.
- Branch: `hermes/curadoria-nb9060-production-20260608`.
- Commit local da branch: `79ae0ed`.
- PR: `https://github.com/lk-snkrs/lk-new-theme/pull/36`.
- PR state antes do merge: `MERGEABLE` / `CLEAN`; status checks: vazio.
- Merge commit em `production`: `6cc23dc955e160b0aef6f888a87d35ff85081d72`.

## QA local antes do merge

- `git diff --check`: passou.
- Static Liquid QA: passou.
- Render line count local: `1`.
- Split marker count local: `3`.
- Handle count: `10`.
- Card cap: `lk_rendered_count < 5` presente.
- Malformed URLs/placeholders: não detectados.

## Readback Shopify Production pós-sync

- Poll 1 após merge já convergiu via Shopify sync.
- Main Production SHA12: `d08dd7b15b83`.
- Split Production existe: `true`.
- Split Production SHA12: `fb7a6f56abb9`.
- Render line count no main Production: `1`.
- Static QA readback: `ok: true`; errors: `[]`.
- Simulação estática: 10 PDPs membros renderizam até 5 alternativas e excluem o produto atual.

## QA público

- Amostra inicial cache-busted:
  - `tenis-new-balance-9060-slate-grey-arid-stone-cinza`: HTTP 200, marker presente.
  - `tenis-new-balance-9060-olivine-verde`: HTTP 200, marker presente.
  - `tenis-new-balance-9060-triple-black-preto`: primeiro request HTTP 200 sem marker, mas com Curadoria presente; classificado como edge/cache rotativo.
- Focus QA subsequente:
  - Triple Black: tentativa seguinte HTTP 200, marker presente, 5 cards, produto atual ausente.
  - Pink Granite Silver: 3/3 marker presente.
  - Nori: 3/3 marker presente.
  - Slate Grey: 3/3 marker presente.
- Card QA:
  - Slate Grey Arid Stone: 5 cards, current ausente.
  - Olivine: 5 cards, current ausente.
  - Triple Black: focus retry com 5 cards, current ausente.
- Caveat: houve um miss público inicial em Triple Black, coerente com propagação/cache Shopify Edge; source/readback Production está correto.

## Handles/labels

- `tenis-new-balance-9060-slate-grey-arid-stone-cinza` — Slate Grey Arid Stone
- `tenis-new-balance-9060-olivine-verde` — Olivine
- `tenis-new-balance-9060-sea-salt-new-spruce-dark-artic-grey-cinza` — Sea Salt New Spruce
- `tenis-new-balance-9060-sparrow-flat-taupe-marrom` — Sparrow Flat Taupe
- `tenis-new-balance-9060-slate-grey-cinza` — Slate Grey
- `tenis-new-balance-9060-team-away-grey-cinza` — Team Away Grey
- `tenis-new-balance-9060-reflection-raincloud-quarry-blue-bege` — Reflection Raincloud
- `tenis-new-balance-9060-triple-black-preto` — Triple Black
- `tenis-new-balance-9060-pink-granite-silver-metallic-silver-cinza` — Pink Granite Silver
- `tenis-new-balance-9060-nori-verde` — Nori

## Rollback

Rollback preferencial: GitHub revert/PR do merge `6cc23dc955e160b0aef6f888a87d35ff85081d72`.

Rollback manual escopado, se necessário:

1. Remover do main Production a linha `{%- render 'lk-variante-nb9060-expansion-20260608', product: product -%}`.
2. Remover o arquivo `snippets/lk-variante-nb9060-expansion-20260608.liquid`.
3. Aguardar sync Shopify.
4. Readback Admin Asset API e confirmar: split ausente, render line count `0`, marker ausente.

## Artefatos locais

- PR body: `/opt/data/tmp/curadoria_nb9060_prod_20260608/pr_body.md`.
- Readback OK: `/opt/data/tmp/curadoria_nb9060_prod_20260608/readback_ok.json`.
- Public QA: `/opt/data/tmp/curadoria_nb9060_prod_20260608/public_qa.json`.
- Public focus QA: `/opt/data/tmp/curadoria_nb9060_prod_20260608/public_focus_qa.json`.
- Public card QA: `/opt/data/tmp/curadoria_nb9060_prod_20260608/public_card_qa.json`.
- Triple card focus QA: `/opt/data/tmp/curadoria_nb9060_prod_20260608/public_triple_card_focus.json`.
