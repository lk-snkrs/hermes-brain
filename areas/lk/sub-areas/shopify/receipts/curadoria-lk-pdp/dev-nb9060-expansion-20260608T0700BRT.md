# Receipt — Curadoria LK PDP DEV NB9060 expansion (2026-06-08)

- values_printed: false
- gerado: 2026-06-08 07:49:18 BRT
- aprovação interpretada: Lucas respondeu `Aprovo` após pergunta escopada para DEV/unpublished New Balance 9060 adulto; não autoriza Production/merge.
- target DEV: lk-new-theme/dev / theme `155065450718` / role `unpublished`
- Production verificado sem write: lk-new-theme/production / theme `155065417950` / role `main`
- main asset DEV: `snippets/lk-variante-top30-visited-v2.liquid`
- split asset DEV: `snippets/lk-variante-nb9060-expansion-20260608.liquid`
- marker: `top30-new-balance-9060-expansion-20260608`

## Mudança executada

- Worker receipt compacto: `demand_classification=shopify_theme_dev_curadoria_pdp_write`; `canonical_playbook=Curadoria LK PDP split-snippet DEV`; `workers_selected=preflight/readback/static-qa/public-preview-sample`; `workers_skipped=delegation_tool_unavailable_not_needed`; `delegation_tool_used=no`; `owner_agent_final_decision=DEV aplicado e Production inalterado`.
- Criado/atualizado split snippet NB9060 no DEV.
- Inserida uma render line no main Curadoria DEV.
- Nenhum write em Production. Nenhum produto/preço/estoque/metafield/app/campanha alterado.

## Evidência

- Product `.js` preflight: 10/10 OK/available.
- Image HEAD preflight: 10/10 OK image.
- Main DEV SHA12 inicial antes do NB9060: `7b5e88f521ba` → readback final `97758147c9a9`.
- Split DEV SHA12 final readback: `f650721c8cbb`.
- Observação de autocorreção: a primeira versão do split chegou a readback `76d4b922f707`; corrigi no mesmo escopo DEV para limitar o bloco a 5 cards por PDP, seguindo padrão canônico da Curadoria LK.
- Render line count no main DEV: `1`.
- Static QA ok: `True`; erros: `[]`; simulação: 10 PDPs membros renderizam 5 alternativas, excluindo o produto atual.
- Production main unchanged: `True` (`a377c2ca1168` → `a377c2ca1168`).
- Public preview HTML sample: 3/3 HTTP 200, mas `preview_theme_id` foi removido do final URL; classificado como inconclusivo para DEV render, não falha de source/readback.

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

1. Restaurar `snippets/lk-variante-top30-visited-v2.liquid` no DEV removendo a render line `{%- render 'lk-variante-nb9060-expansion-20260608' -%}`. Arquivo local de rollback preparado: `/opt/data/tmp/curadoria_nb9060_dev_20260608/rollback_original_dev_main_remove_nb9060.liquid`.
2. Remover/zerar o split snippet DEV `snippets/lk-variante-nb9060-expansion-20260608.liquid`; ele não existia antes da execução NB9060. O arquivo `/opt/data/tmp/curadoria_nb9060_dev_20260608/backup_dev_split.liquid` representa apenas a versão intermediária autocorrigida, não o baseline pré-operação.
3. Re-read Admin Asset API e confirmar ausência de `top30-new-balance-9060-expansion-20260608`/render line.

## Artefatos locais

- Preflight: `/opt/data/tmp/curadoria_nb9060_dev_20260608/preflight.json`
- Resultado: `/opt/data/tmp/curadoria_nb9060_dev_20260608/result.json`
- Readback main: `/opt/data/tmp/curadoria_nb9060_dev_20260608/readback_dev_main.liquid`
- Readback split: `/opt/data/tmp/curadoria_nb9060_dev_20260608/readback_dev_split.liquid`
