# Receipt — LKGOC NB 204L Guia LK: seleção das 6 melhores imagens em DEV

Data: 2026-06-09
Tema: `155065450718` / `lk-new-theme/dev`
Role verificado por API: `unpublished`
Escopo: preview DEV da página `/pages/new-balance-204l-original-brasil-guia-lk`

## Pedido
Lucas pediu para escolher as 6 melhores imagens da galeria atual, que estava com 10 imagens.

## Ação executada
- Mantidos 6 cards de imagem na galeria visual.
- Removidas imagens redundantes/repetitivas.
- Critério da seleção: força visual, leitura on feet, proporção do modelo, variação de enquadramento e valor editorial/comercial.
- Imagens mantidas:
  - `image_card_32` — on feet / proporção baixa;
  - `image_card_33` — corpo inteiro;
  - `image_card_34` — close on feet;
  - `image_card_37` — look editorial;
  - `image_card_51` — editorial PUSS PUSS;
  - `image_card_53` — on feet editorial / shape baixo.

## QA executado
- Fetch preview DEV:
  - `role_unpublished=True`
  - `Liquid error=False`
  - `figure_count=6`
- Playwright QA:
  - mobile: `liquid=0`, `image_cards=6`, `grid_visible=true`
  - desktop: `liquid=0`, `image_cards=6`, `grid_visible=true`

## Evidências locais
- HTML verificado: `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/204l-guide-selected-6-images-verified.html`
- Screenshot mobile: `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/204l-guide-selected-6-mobile-20260609.png`
- Screenshot desktop: `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/204l-guide-selected-6-desktop-20260609.png`
- Backup local antes da seleção: `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/templates__page.nb204l-guide.before-select-6-images.json`

## Produção
Nenhuma alteração em Production. Mudança está apenas no DEV/unpublished.
