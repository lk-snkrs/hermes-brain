# Receipt — Puma Speedcat LKGOC Zero-Base v2

Data UTC: 20260606T191256Z
Status: **DEV_READY_FOR_LUCAS_VISUAL_APPROVAL / PRODUCTION_BLOCKED**

## Resumo

Puma Speedcat refeita no DEV a partir do shell New Balance 204L.

Regra obedecida:

- copiar shell 204L;
- mudar só texto e imagens;
- remover layout/classes próprias Puma;
- manter Production intocado.

## Tema

DEV:

- ID: `155065450718`
- Nome: `lk-new-theme/dev`
- Role: `unpublished`

Production/main:

- ID: `155065417950`
- Nome: `lk-new-theme/production`
- Role: `main`
- Alterado: **não**

## Asset aplicado

- `snippets/lk-goc-collection.liquid`

Readback:

- candidate sha: `b983e2bf8d57acada47d8fa024a417de9621c150bb5df404124e2f3c503c34db`
- readback ok: `True`
- bad Puma classes: `False`

## QA final interno

Status: `PASS_TECHNICAL_AND_STRUCTURAL_READY_FOR_LUCAS_VISUAL_APPROVAL`

Checks:

- ✅ has_puma_title: True
- ✅ has_204l_shell_classes: True
- ❌ has_bad_puma_layout_classes: False
- ✅ has_guide_id: True
- ✅ has_vogue_img: True
- ✅ has_overkill: True
- ✅ no_discount_in_lkgoc_sections: True
- ✅ discount_exists_only_global: True
- ✅ no_liquid_error: True
- ✅ has_faqpage: True
- ✅ no_prod_theme_t91_assets: True
- ✅ hero_before_visual_grid: True
- ✅ visual_grid_before_guide: True
- ✅ class_sets_identical_to_gold: True
- ✅ class_jaccard_vs_gold: 1.0

## Observação sobre “desconto”

A palavra aparece no DOM global por script de reviews/cupom, fora das seções LKGOC. No bloco LKGOC Puma, o check `no_discount_in_lkgoc_sections` passou.

## Artefatos visuais

- Side-by-side 204L vs Puma V2: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/puma-speedcat-lkgoc-zero-base-v2-20260606T190620Z/qa-v2/SIDE-BY-SIDE-204L-vs-PUMA-V2.png`
- Puma desktop: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/puma-speedcat-lkgoc-zero-base-v2-20260606T190620Z/qa-v2/puma-speedcat-v2-desktop.png`
- Puma mobile: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/puma-speedcat-lkgoc-zero-base-v2-20260606T190620Z/qa-v2/puma-speedcat-v2-mobile.png`
- Gold 204L desktop: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/puma-speedcat-lkgoc-zero-base-v2-20260606T190620Z/qa-v2/gold-204l-desktop.png`

## Preview DEV

Abrir em sequência:

1. `https://lk-sneakerss.myshopify.com/?preview_theme_id=155065450718`
2. `https://lk-sneakerss.myshopify.com/collections/puma-speedcat`

## Rollback DEV

Snapshots antes do write:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/puma-speedcat-lkgoc-zero-base-v2-20260606T190620Z/snippets__lk-goc-collection.liquid.shopify-before`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/puma-speedcat-lkgoc-zero-base-v2-20260606T190620Z/sections__lk-collection.liquid.shopify-before`

Rollback: restaurar `snippets/lk-goc-collection.liquid.shopify-before` no tema DEV após verificar `role: unpublished`.

## Decisão necessária

Lucas precisa aprovar visualmente. Sem aprovação explícita, nenhum merge para Production.
