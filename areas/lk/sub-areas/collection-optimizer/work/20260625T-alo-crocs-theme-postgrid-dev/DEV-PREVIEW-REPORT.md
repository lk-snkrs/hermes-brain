# DEV Preview — correção pós-grid LKGOC Alo Yoga + Crocs McQueen

Data: 2026-06-25  
Aprovação Lucas: “vamos seguir” / “seguir, pode faze”.  
Theme DEV: `lk-new-theme/dev` (`theme_id=155065450718`, `role=unpublished`)  
Production/main: não promovido nesta etapa.  
values_printed: false

## O que foi feito

Após a tentativa via `descriptionHtml` falhar e ser revertida, a correção foi aplicada no caminho correto de tema DEV/unpublished:

1. `sections/lk-collection.liquid`
   - adiciona copy curta de banner para `alo-yoga-1` e `crocs-mcqueen` via override de descrição;
   - evita que HTML editorial da collection seja usado como descrição de topo;
   - mantém o guia LKGOC no ponto pós-grid controlado pelo tema.
2. `snippets/lk-goc-collection.liquid`
   - mantém/ajusta o guia pós-grid dos dois handles;
   - remove linguagem sensível de disponibilidade do bloco Crocs.

## QA DEV público

| Handle | HTTP | H1 | FAQPage | Guia | Bloco citável | Como escolher | Perguntas frequentes | Liquid error | Pós-grid |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `alo-yoga-1` | 200 | 1 | 1 | 1 | 1 | 2 | 1 | não | ✅ guia depois de `Mostrando 24 de` |
| `crocs-mcqueen` | 200 | 1 | 1 | 1 | 1 | 1 | 1 | não | ✅ guia depois de `1 itens/Ordenar` |

### Posições extraídas do texto DEV

- Alo Yoga: `Ordenar:` 2953 → `Mostrando 24 de` 7856 → `Guia editorial LK` 7890
- Crocs McQueen: `1 itens` 2944 → `Ordenar:` 2952 → `Guia editorial LK` 3419

## Screenshots DEV

- `dev-preview-alo-mobile.png`
- `dev-preview-crocs-mobile.png`

## Produção

Não houve promoção para production/main. A produção permanece no estado pós-rollback anterior. O DEV resolve o problema estrutural que production ainda tem em Crocs e reduz duplicidade em Alo.

## Rollback DEV

Rollback preparado:

`rollback_dev_theme_assets.py`

Backups usados:

- `unpublished-155065450718-lk-new-theme_dev-sections__lk-collection.liquid.before-lkgoc-alo-crocs-postgrid-patch`
- `unpublished-155065450718-lk-new-theme_dev-snippets__lk-goc-collection.liquid.before-lkgoc-alo-crocs-postgrid-patch`

## Próxima aprovação necessária

Para production/main, ainda precisa approval explícito de Lucas porque envolve theme production/customer-facing.

Frase segura:

> Aprovo promover para production/main a correção LKGOC pós-grid de Alo Yoga e Crocs McQueen validada no DEV `lk-new-theme/dev` (`theme_id=155065450718`), limitada a `sections/lk-collection.liquid` e `snippets/lk-goc-collection.liquid`, sem preço, estoque, produtos, ordenação, GMC, Klaviyo, campanhas ou checkout, com backup, readback público, QA mobile e rollback.
