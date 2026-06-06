# Receipt — Curadoria LK PDP label light fix DEV

Data: 2026-06-06

## Aprovação

Lucas aprovou aplicar em DEV a correção CSS da Curadoria LK PDP em `assets/lk-product-card.css`, trocando o peso visual das labels `::after` de 600 para 300, sem mexer em Production.

## Execução

Tema alvo:

- Theme ID: `155065450718`
- Nome: `lk-new-theme/dev`
- Role confirmado antes do write: `unpublished`

Asset:

- `assets/lk-product-card.css`

Alteração aplicada:

```diff
-.lk-variante .lk-variante__item[href^="/products/"] .lk-variante__label::after{font-size:12px;line-height:1.15;font-weight:600;white-space:normal;color:inherit;}
+.lk-variante .lk-variante__item[href^="/products/"] .lk-variante__label::after{font-size:12px;line-height:1.15;font-weight:300;white-space:normal;color:inherit;}
```

## Backup

Backup pré-write:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-label-light-20260606/20260606T013452Z-dev-155065450718-assets__lk-product-card.before.css`

## Readback

Após reconsulta do asset DEV:

- regra antiga `font-weight:600`: `0`
- regra nova `font-weight:300`: `1`
- asset DEV lido com tamanho: `34043` bytes

Observação: o primeiro readback imediato retornou cache/estado anterior; uma reconsulta logo depois confirmou o update no Shopify Admin Asset API.

## QA visual/computed — DEV preview

URLs abriram com asset DEV `t/92`.

- `tenis-air-jordan-1-mid-glitter-swoosh-azul`
  - bloco: presente
  - rail: `grid`
  - cards: `5`
  - `::after font-weight`: `300`
  - labels: Wolf Grey, Panda, Electro Orange, Canyon Rust, Aqua Tint

- `yeezy-slide-glow-green`
  - bloco: presente
  - rail: `grid`
  - cards: `5`
  - `::after font-weight`: `300`
  - labels: Slate Marine, Azure, Bone, Ochre, Onyx

- `new-balance-530-white-natural-indigo-1`
  - bloco: presente
  - rail: `grid`
  - cards: `5`
  - `::after font-weight`: `300`
  - labels: Turtledove, Silver Cream, Silver White, Steel Grey, Silver Blue

QA JSON local:

- `/opt/data/tmp/lk_dev_label_light_multiqa.json`

## Escopo preservado

Não alterado:

- Production/live
- produtos
- preço
- estoque
- checkout
- snippets de grupos
- imagens/handles/labels

## Rollback

Para rollback em DEV, restaurar o backup pré-write de `assets/lk-product-card.css` no tema `155065450718`.
