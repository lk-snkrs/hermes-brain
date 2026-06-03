# Curadoria LK — Apparel/Feminino Rule Dev Apply

Data UTC: `2026-06-02T13:16:26.867807+00:00`

## Regra aplicada
- Lululemon/Alo Yoga: cores do mesmo modelo primeiro; depois completa com linha/set coerente.

## Resultado
- Top 30 com bloco: `4/30`
- Bloqueados: `26`
- Production control blocks: `0`

## QA resumo
- `jaqueta-lululemon-define-nulu`: blocks `0`, items `0`, labels ``, current `False`, errors `0`, markers ``
- `calca-alo-yoga-airlift-high-waist-7-8-line-up-legging-gravel-bege`: blocks `0`, items `0`, labels ``, current `False`, errors `0`, markers ``
- `top-alo-yoga-airlift-line-up-gravel-bege`: blocks `0`, items `0`, labels ``, current `False`, errors `0`, markers ``

## Top30 bloqueados
- `tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo`
- `tenis-nike-vomero-premium-flat-stout-marrom`
- `tenis-new-balance-204l-timberwolf-bege`
- `tenis-adidas-samba-disney-101-dalmatians-penny-branco`
- `nike-moon-shoe-sp-jacquemus-alabaster-amarelo`
- `slide-nike-mind-001-black-chrome-preto`
- `tenis-adidas-samba-og-white-floral-embroidery-branco`
- `tenis-nike-vomero-premium-sail-coconut-milk-branco`
- `tenis-adidas-samba-og-crochet-pack-orbit-green-verde`
- `tenis-onitsuka-tiger-mexico-66-sabot-beige-green-bege`
- `mule-bravest-studios-bear-claw-black-preto`
- `tenis-new-balance-9060-mushroom-arid-stone-camurca`
- `tenis-nike-vomero-premium-black-volt-preto`
- `tenis-adidas-sl-72-og-scarlet-crochet-vermelho`
- `tenis-onitsuka-tiger-mexico-66-sd-beige-beet-juice-bege`
- `travis-scott-x-air-jordan-1-low-og-reverse-mocha`
- `tenis-nike-moon-shoe-sp-jacquemus-off-white`
- `jaqueta-lululemon-define-nulu`
- `tenis-nike-vomero-premium-alabaster-amarelo`
- `tenis-new-balance-530-turtledove-mushroom-mesh-casual`
- `tenis-adidas-sl72-og-maroon-almost-yellow-marrom`
- `nike-sb-dunk-low-sandy-ebay-2022`
- `tenis-adidas-samba-og-x-disney-pixar-toy-story`
- `tenis-onitsuka-tiger-mexico-66-sd-kill-bill-amarelo`
- `tenis-nike-vomero-premium-white-bright-crimson-branco`
- `tenis-onitsuka-tiger-mexico-66-white-black-branco`

## Rollback
Backups `before__snippet.liquid` neste receipt.

## QA retry após 429
- Full QA inicial bateu 429 no storefront; retry após cooldown validou amostras representativas.
- Lululemon Define Nulu: 1 bloco, 5 itens, produto atual excluído por link exato, sem Liquid errors.
- Alo Yoga Air line: 1 bloco, 5 itens, produto atual excluído por link exato, sem Liquid errors.
- Samba OG e Travis Scott continuaram funcionando.
- Bravest continua bloqueado por falta de família/linha suficiente.
