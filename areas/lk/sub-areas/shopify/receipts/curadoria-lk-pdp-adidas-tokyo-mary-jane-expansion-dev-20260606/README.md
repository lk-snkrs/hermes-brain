# Curadoria LK PDP — Adidas Tokyo Mary Jane Expansion — DEV Receipt — 2026-06-06

## Status

DEV aplicado e validado para o escopo aprovado: expansão Adidas Tokyo Mary Jane.

## Aprovação

Lucas: `Aprovo DEV Adidas Tokyo Mary Jane Expansion`

## Escopo executado

- Theme DEV: `155065450718`
- Theme name: `lk-new-theme/dev`
- Role: `unpublished`
- Asset: `snippets/lk-variante-top30-visited-v2.liquid`
- Grupo/marker: `top30-adidas-tokyo-regular`
- Antes: 6 handles / 6 labels / 6 images / 6 titles
- Depois: 10 handles / 10 labels / 10 images / 10 titles
- Production: não alterado neste passo

## Itens adicionados

1. `tenis-adidas-tokyo-mary-jane-cream-white-red-gold-metallic-creme` — `Mary Jane Cream`
2. `tenis-adidas-tokyo-mary-jane-crystal-sky-cream-white-azul` — `Mary Jane Sky`
3. `tenis-adidas-tokyo-mary-jane-sandy-pink-earth-strata-rosa` — `Mary Jane Pink`
4. `tenis-adidas-tokyo-mj-core-black-cream-white-gold-metallic-preto` — `MJ Core Black`

## Readback DEV

- Action: `put`
- Before SHA: `5f725da9067e988cb2e8e52664d35d1c65aaeaef68d9fc7df02b0934438137fc`
- Candidate SHA: `d12399d85661b323c34fbb77b20a5ed7dd0f7a5b668ec46e91374194a267e725`
- Readback convergiu na tentativa: 2
- Readback SHA: `d12399d85661b323c34fbb77b20a5ed7dd0f7a5b668ec46e91374194a267e725`
- Marker count: 1
- Static counts pós-readback:
  - handles: 10
  - labels: 10
  - images: 10
  - titles: 10
- Novos 4 handles presentes: sim
- Errors: `[]`

## QA visual DEV

PDPs testadas via CDP:

1. `tenis-adidas-tokyo-mary-jane-cream-white-red-gold-metallic-creme`
2. `tenis-adidas-tokyo-mary-jane-crystal-sky-cream-white-azul`
3. `tenis-adidas-tokyo-mj-core-black-cream-white-gold-metallic-preto`

Resultado:

- Block: true
- Marker: `top30-adidas-tokyo-regular`
- Rail display: `grid`
- Card count: 5
- Labels dos cards: `fontWeight 300`
- `::after` dos labels: `fontWeight 300`

## Caveat visual

O CSS do tema DEV ainda renderiza o título `Outras variações` com `fontWeight 500`. Esse não fazia parte do escopo aprovado `Aprovo DEV Adidas Tokyo Mary Jane Expansion`; a correção do título já foi aplicada/validada em Production no PR #28, mas não foi aplicada ao asset CSS do tema DEV neste passo.

## Backups / rollback

- Backup DEV pré-write:
  - `/opt/data/tmp/lk-dev-before-adidas-tokyo-mary-jane-expansion.liquid`
- Readback DEV pós-write:
  - `/opt/data/tmp/lk-dev-after-adidas-tokyo-mary-jane-expansion.liquid`

Rollback DEV: restaurar o backup pré-write no asset `snippets/lk-variante-top30-visited-v2.liquid` do tema DEV, mediante aprovação se solicitado.

## Artefatos

- Apply script: `/opt/data/tmp/lk_apply_adidas_tokyo_mary_jane_dev.py`
- Apply stdout: `/opt/data/tmp/lk_apply_adidas_tokyo_mary_jane_dev.stdout`
- Apply result JSON: `/opt/data/tmp/lk-dev-adidas-tokyo-mary-jane-expansion-apply-result.json`
- QA files: `/opt/data/tmp/lk_tokyo_mj_dev_qa/*.json`

## Non-actions

Não foram alterados produtos, preços, estoque, checkout, Tiny, GMC, apps, tracking, campanhas ou Production neste passo.
