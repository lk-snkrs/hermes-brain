# Receipt — Curadoria LK PDP label light production merge

Data: 2026-06-06

## Aprovação

Lucas aprovou fazer merge para Production da correção de tipografia da Curadoria LK PDP.

## Merge executado

Fluxo usado: GitHub PR para `production`, não write direto no live theme.

- Repo: `lk-snkrs/lk-new-theme`
- PR: `https://github.com/lk-snkrs/lk-new-theme/pull/24`
- Branch temporária: removida após merge
- Merge SHA: `75a37fe294f33b9e022165da2120f2e04cfaf118`
- Head SHA: `d8c82af0b4108152d973a7c2ef5d99831ad7c2d9`

Diff verificado antes do merge:

```text
assets/lk-product-card.css | 2 +-
1 file changed, 1 insertion(+), 1 deletion(-)
```

Arquivo único alterado:

```text
M	assets/lk-product-card.css
```

`git diff --check`: passou.

## Alteração

```diff
-.lk-variante .lk-variante__item[href^="/products/"] .lk-variante__label::after{font-size:12px;line-height:1.15;font-weight:600;white-space:normal;color:inherit;}
+.lk-variante .lk-variante__item[href^="/products/"] .lk-variante__label::after{font-size:12px;line-height:1.15;font-weight:300;white-space:normal;color:inherit;}
```

## Backup Production antes do merge

- Theme Production: `155065417950`
- Asset: `assets/lk-product-card.css`
- Backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-label-light-production-20260606/20260606T094326Z-production-theme-155065417950-assets__lk-product-card.before.css`

## Readback

GitHub `origin/production` após merge:

- regra nova presente: sim
- regra antiga ausente: sim

Shopify live Asset API poll:

- tentativa 1: antiga `1`, nova `0`
- tentativa 2: antiga `0`, nova `1`
- live SHA depois: `4cd78a73c9cf4b917fd7f074763d7162f6ba3d05d1dbd42eb9fd66518e06208d`

## QA público pós-merge

JSON local:

- `/opt/data/tmp/lk_live_label_light_postmerge_multiqa.json`
- `/opt/data/tmp/lk_live_yeezy_focus_postmerge.json`

Resultados:

- `tenis-air-jordan-1-mid-glitter-swoosh-azul`
  - bloco presente
  - rail `grid`
  - 5 cards
  - `::after font-weight: 300`

- `new-balance-530-white-natural-indigo-1`
  - bloco presente
  - rail `grid`
  - 5 cards
  - `::after font-weight: 300`

- `yeezy-slide-glow-green`
  - 1ª tentativa focada: bloco presente, rail `grid`, 5 cards, `::after font-weight: 300`
  - tentativas seguintes: bloco ausente no HTML público, padrão compatível com edge/cache ou variação pública do render, não com falha da regra CSS; quando o bloco aparece, a regra está correta.

## Escopo preservado

Não alterado:

- produtos
- preço
- estoque
- checkout
- snippets de grupos
- imagens/handles/labels
- apps

## Rollback

Opções:

1. Reverter o PR/commit no GitHub `production`.
2. Restaurar o backup do asset Production listado acima.
