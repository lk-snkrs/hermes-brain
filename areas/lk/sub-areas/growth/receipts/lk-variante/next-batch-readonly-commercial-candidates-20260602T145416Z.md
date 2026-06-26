# Curadoria LK / LK Variante — próximos candidatos comerciais read-only

Timestamp UTC: 20260602T145416Z

## Escopo executado

Leitura apenas:

- Shopify Admin Orders API: pedidos dos últimos 180 dias, sem PII, apenas status financeiro/cancelamento e line_items para contagem de unidades por produto.
- Shopify Admin Products API: catálogo ativo para agrupar por modelo/silhueta/linha.
- Shopify Theme Asset GET: leitura dos snippets de Curadoria LK em production para excluir grupos já cobertos.

Não houve upload de tema, produto, preço, estoque, app, campanha, GMC, Klaviyo, Meta, Tiny ou WhatsApp.

## Critério aplicado

- Sneaker: mesma silhueta/tipo; collab/cápsula separada.
- Vestuário: regra especial de look/linha já registrada para Lululemon/Alo Yoga, mas este pacote prioriza próximos grupos sneaker com sinal comercial.
- Ranking: unidades vendidas em pedidos pagos/não cancelados nos últimos 180 dias. Quando faltar venda suficiente para completar 5 opções, manter copy neutra `Curadoria LK` e completar por proximidade/curadoria.

## Próximos grupos recomendados

1. Adidas Gazelle
   - Produtos ativos no catálogo: 31
   - Unidades 180d: 12
   - Top sinal comercial:
     - `tenis-adidas-gazelle-indoor-maroon-almost-yellow-marrom` — 3u
     - `tenis-adidas-gazelle-indoor-liberty-london-floral-embroidery-stripes-multi-color` — 2u
     - `tenis-adidas-gazelle-indoor-liberty-london-floral-embroidery-multi-color` — 1u
     - `tenis-adidas-gazelle-indoor-bad-bunny-cabo-rojo-rosa` — 1u
     - `tenis-adidas-gazelle-indoor-x-clot-by-edison-chen-off-white-branco` — 1u
     - `tenis-adidas-gazelle-x-bad-bunny-core-white-bege` — 1u
   - Nota semântica: separar futuramente Bad Bunny/Clot se Lucas preferir cápsulas isoladas; para primeiro preview, manter Gazelle Indoor/Gazelle próxima e não chamar de best seller no frontend.

2. Air Jordan 4
   - Produtos ativos no catálogo: 35
   - Unidades 180d: 11
   - Top sinal comercial:
     - `tenis-air-jordan-4-retro-metallic-gold-branco` — 3u
     - `nike-sb-x-air-jordan-4-retro-pine-green` — 1u
     - `tenis-nike-air-jordan-4-retro-black-cat-preto` — 1u
     - `air-jordan-4-frozen-moments` — 1u
     - `tenis-nike-air-jordan-4-retro-tex-worn-blue-denim-azul` — 1u
     - `air-jordan-4-craft-medium-olive` — 1u
   - Nota semântica: AJ4 pode ser agrupado por silhueta, mas SB x AJ4 Pine Green é cápsula/collab; recomendo separar se houver 5+ AJ4 SB/collab suficientes, senão usar como item de proximidade com cautela.

3. Adidas Taekwondo Mei Ballet
   - Produtos ativos no catálogo: 11
   - Unidades 180d: 10
   - Top sinal comercial:
     - `adidas-taekwondo-mei-ballet-branco-e-preto` — 3u
     - `tenis-adidas-taekwondo-mei-ballet-preto` — 3u
     - `adidas-taekwondo-mei-ballet-preto-e-branco` — 2u
     - `tenis-adidas-taekwondo-mei-ballet-branco-e-prata` — 1u
     - `tenis-adidas-wmns-taekwondo-mei-white-scarlet-gum-couro` — 1u
     - `sapatilha-onitsuka-tiger-wmns-taekwondo-mei-ballet-clear-pink-gum-camurca` — 0u
   - Nota semântica: revisar o último handle porque o título começa com Onitsuka, mas foi classificado por Taekwondo Mei; não usar no preview sem checagem visual.

4. Adidas Handball Spezial
   - Produtos ativos no catálogo: 15
   - Unidades 180d: 9
   - Top sinal comercial:
     - `tenis-adidas-handball-spezial-earth-strata-gum-marrom` — 3u
     - `tenis-adidas-handball-spezial-bordo` — 2u
     - `tenis-adidas-handball-spezial-sporty-rich-brown-marrom` — 1u
     - `tenis-adidas-handball-spezial-lt-collegiate-green-cream-white-verde` — 1u
     - `tenis-adidas-handball-spezial-sporty-rich-pink-rosa` — 1u
     - `tenis-adidas-handball-spezial-green-pink-velvet-verde` — 1u
   - Nota semântica: Sporty & Rich é collab; pode ficar separada se houver volume de opções. Para preview neutro, usar apenas como proximidade se necessário.

## Próxima ação segura proposta

Montar no dev/unpublished um Batch 3 com 4 grupos:

- Gazelle
- Air Jordan 4 regular, excluindo collab se a lista regular tiver 6+ opções boas
- Taekwondo Mei Ballet, após revisar o handle classificado como Onitsuka
- Handball Spezial regular, com tratamento cauteloso das collabs

## Aprovação necessária para escrever no dev theme

Upload em tema dev/unpublished ainda é Shopify write. Para eu aplicar no dev e fazer QA de preview, aprovação sugerida:

> Pode aplicar no dev o Batch 3 da Curadoria LK com Gazelle, Air Jordan 4, Taekwondo Mei Ballet e Handball Spezial, seguindo as regras de separar collab quando fizer sentido e sem mexer em production/produtos/preço/estoque/apps.

## Artefatos locais

- JSON bruto de candidatos: `/opt/data/tmp/lk-variante-next-candidates-readonly.json`
- JSON priorizado: `/opt/data/tmp/lk-variante-next-candidates-priority-readonly.json`
- Handles já ativos em production: `/opt/data/tmp/lk-variante-production-parsed-handles.json`
