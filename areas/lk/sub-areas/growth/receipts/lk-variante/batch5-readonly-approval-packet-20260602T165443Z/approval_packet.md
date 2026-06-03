# Curadoria LK — Batch 5 read-only approval packet

## Escopo
- Read-only: product JS público + receipts locais.
- Nenhum upload de tema, nenhum write Shopify, nenhum produto/preço/estoque alterado.

## Recomendação
Batch 5 recomendado para Dev preview: Air Jordan 1 High regular/story (6 itens), Yeezy Slide (7), Nike Shox TL (7). Bloquear Asics Gel-1130 por só ter 4 cores únicas após dedupe; não subir com duplicados sem aprovação explícita.

## air-jordan-1-high
- Marker sugerido: `top30-air-jordan-1-high-regular`
- Itens selecionados: 6
- Renderiza 5 alternativas por PDP: sim
- Handles:
  - `tenis-air-jordan-1-high-og-black-metallic-gold-preto` — Tênis Nike Air Jordan 1 High Og Black Metallic Gold Preto
  - `air-jordan-1-high-85-college-navy` — Tênis Nike Air Jordan 1 High 85 College Navy Azul
  - `air-jordan-1-high-atmosphere` — Tênis Nike Air Jordan 1 High Atmosphere Rosa
  - `air-jordan-1-high-chicago-lost-and-found` — Tênis Nike Air Jordan 1 High Chicago Lost and Found Vermelho
  - `air-jordan-1-high-dark-mocha` — Tênis Nike Air Jordan 1 High Dark Mocha Marrom
  - `air-jordan-1-high-lucky-green` — Tênis Nike Air Jordan 1 High Lucky Green Verde
- Excluídos/segurados:
  - `tenis-nike-air-jordan-1-high-fragment-design-x-union-la-varsity-red-branco`
  - `air-jordan-1-high-next-chapter`

## yeezy-slide
- Marker sugerido: `top30-yeezy-slide`
- Itens selecionados: 7
- Renderiza 5 alternativas por PDP: sim
- Handles:
  - `yeezy-slide-onyx` — Tênis Yeezy Slide Onyx Preto
  - `tenis-adidas-yeezy-slide-slate-marine-azul-escuro` — Tênis adidas Yeezy Slide Slate Marine Azul Escuro
  - `yeezy-slide-azure` — Tênis Yeezy Slide Azure Azul
  - `yeezy-slide-bone-937693978` — Tênis Yeezy Slide Boné Branco
  - `yeezy-slide-glow-green` — Tênis Yeezy Slide Glow Green Verde
  - `yeezy-slide-ochre-925686464` — Tênis Yeezy Slide Ochre Marrom
  - `yeezy-slide-pure-2022` — Tênis Yeezy Slide Pure (2022) Bege

## nike-shox-tl
- Marker sugerido: `top30-nike-shox-tl`
- Itens selecionados: 7
- Renderiza 5 alternativas por PDP: sim
- Handles:
  - `tenis-nike-shox-tl-pumice-night-maroon-cinza` — Tênis Nike Shox TL Pumice Night Maroon Cinza
  - `tenis-nike-shox-tl-black-cave-stone-preto` — Tênis Nike Shox TL Black Cave Stone Preto
  - `tenis-nike-shox-tl-black-dynamic-yellow-preto` — Tênis Nike Shox TL Black Dynamic Yellow Preto
  - `tenis-nike-shox-tl-blue-tint-orange-azul` — Tênis Nike Shox TL Blue Tint Orange Azul
  - `tenis-nike-shox-tl-orewood-brown-cave-stone-bege` — Tênis Nike Shox TL Orewood Brown Cave Stone Bege
  - `tenis-nike-shox-tl-sunrise-gradient-laranja` — Tênis Nike Shox TL Sunrise Gradient Laranja
  - `tenis-nike-shox-tl-velvet-brown-denim-turquoise-marrom` — Tênis Nike Shox TL Velvet Brown Denim Turquoise Marrom

## asics-gel-1130
- Marker sugerido: `top30-asics-gel-1130`
- Itens selecionados: 4
- Renderiza 5 alternativas por PDP: não
- Handles:
  - `tenis-asics-gel-1130-black-pure-silver-prata` — Tênis ASICS Gel-1130 Black Pure Silver Prata
  - `tenis-asics-gel-1130-white-black-silver-prata` — Tênis ASICS Gel-1130 White Black Silver Prata
  - `tenis-asics-gel-1130-white-clay-canyon-branco` — Tênis ASICS Gel-1130 White Clay Canyon Branco
  - `tenis-asics-gel-1130-white-pure-silver-prata` — Tênis ASICS Gel-1130 White Pure Silver Prata
- Excluídos/segurados:
  - `tenis-asics-gel-1130-black-pure-silver-prata-1`
  - `tenis-asics-gel-1130-white-black-silver-prata-1`

## Interpretação
- Seguir com 3 grupos no Dev preview: AJ1 High, Yeezy Slide, Nike Shox TL.
- Asics Gel-1130 deve ficar fora por enquanto: incluir duplicados criaria experiência fraca e pode parecer erro.
- AJ1 High mantém Lost and Found, mas exclui Fragment x Union e Next Chapter por cápsula/collab especial.

## Risco
- Baixo se aplicado primeiro apenas no Dev/unpublished theme.
- Risco principal: agrupamento semântico de AJ1 High; mitigado por exclusão de collabs fortes.

## Próxima decisão
Aprovar upload no tema Dev/unpublished para criar preview do Batch 5 com esses 3 grupos?
