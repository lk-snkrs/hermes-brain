# Curadoria LK — Static 5-card Dev Fix Receipt

Data UTC: `2026-06-02T12:46:45.710766+00:00`

## Escopo
- Aprovado: “Aplicar”.
- Tema dev apenas.
- Render estático por handle/imagem para garantir 5 cards e não depender de `all_products`.
- Sem texto best seller no storefront.

## Readback
- `snippets/lk-variante-samba-jane.liquid`: readback `False`, sha `a1c05b0bc2d00729`, size `2433`, public statuses `[200, 200, 200, 200, 200, 200]`
- `snippets/lk-variante-air-jordan-1-low.liquid`: readback `True`, sha `56adb26ffe8aaf31`, size `3563`, public statuses `[200, 200, 200, 200, 200, 200]`
- `snippets/lk-variante-air-jordan-1-low-travis.liquid`: readback `True`, sha `51c40819a70bf8f9`, size `3887`, public statuses `[200, 200, 200, 200, 200, 200]`

## QA resumo
- `tenis-adidas-samba-jane-white-black-branco`: status `200`, blocks `0`, items `0`, current_in_links `False`, liquid_errors `2`, labels ``
- `tenis-adidas-samba-jane-white-blue-gum-branco`: status `200`, blocks `0`, items `0`, current_in_links `False`, liquid_errors `2`, labels ``
- `tenis-adidas-samba-jane-scarlet-gum-vermelho`: status `200`, blocks `0`, items `0`, current_in_links `False`, liquid_errors `2`, labels ``
- `tenis-adidas-samba-jane-black-white-gum-preto`: status `200`, blocks `0`, items `0`, current_in_links `False`, liquid_errors `2`, labels ``
- `tenis-adidas-samba-jane-green-white-gum-verde`: status `200`, blocks `0`, items `0`, current_in_links `False`, liquid_errors `2`, labels ``
- `tenis-adidas-samba-jane-cream-black-gum-bege`: status `200`, blocks `0`, items `0`, current_in_links `False`, liquid_errors `2`, labels ``
- `air-jordan-1-low-vintage-grey`: status `200`, blocks `1`, items `5`, current_in_links `False`, liquid_errors `2`, labels `Midnight Navy, Jade Smoke, Black Medium Grey, Taxi, Light Smoke Grey`
- `tenis-air-jordan-1-low-midnight-navy-wolf-grey-azul-marinho`: status `200`, blocks `1`, items `5`, current_in_links `False`, liquid_errors `2`, labels `Vintage Grey, Jade Smoke, Black Medium Grey, Taxi, Light Smoke Grey`
- `tenis-air-jordan-1-low-jade-smoke-multicolor`: status `200`, blocks `1`, items `5`, current_in_links `False`, liquid_errors `2`, labels `Vintage Grey, Midnight Navy, Black Medium Grey, Taxi, Light Smoke Grey`
- `air-jordan-1-low-black-medium-grey`: status `200`, blocks `1`, items `5`, current_in_links `False`, liquid_errors `2`, labels `Vintage Grey, Midnight Navy, Jade Smoke, Taxi, Light Smoke Grey`
- `air-jordan-1-low-taxi`: status `200`, blocks `1`, items `5`, current_in_links `False`, liquid_errors `2`, labels `Vintage Grey, Midnight Navy, Jade Smoke, Black Medium Grey, Light Smoke Grey`
- `air-jordan-1-low-light-smoke-grey`: status `200`, blocks `1`, items `5`, current_in_links `False`, liquid_errors `2`, labels `Vintage Grey, Midnight Navy, Jade Smoke, Black Medium Grey, Taxi`
- `tenis-air-jordan-1-low-og-sp-x-travis-scott-medium-olive-verde`: status `200`, blocks `0`, items `0`, current_in_links `False`, liquid_errors `2`, labels ``
- `tenis-air-jordan-1-low-og-sp-x-travis-scott-velvet-brown-marrom`: status `200`, blocks `0`, items `0`, current_in_links `False`, liquid_errors `2`, labels ``
- `travis-scott-x-air-jordan-1-low-og-sp-black-phantom`: status `200`, blocks `0`, items `0`, current_in_links `False`, liquid_errors `2`, labels ``
- `travis-scott-x-air-jordan-1-low-og-reverse-mocha`: status `200`, blocks `0`, items `0`, current_in_links `False`, liquid_errors `2`, labels ``
- `tenis-air-jordan-1-low-og-sp-x-travis-scott-mocha`: status `200`, blocks `0`, items `0`, current_in_links `False`, liquid_errors `2`, labels ``
- `tenis-travis-scott-x-air-jordan-1-low-og-canary-amarelo`: status `200`, blocks `0`, items `0`, current_in_links `False`, liquid_errors `2`, labels ``
- `high_control`: status `200`, blocks `0`, items `0`, current_in_links `None`, liquid_errors `2`, labels ``
- `prod_control`: status `200`, blocks `0`, items `0`, current_in_links `None`, liquid_errors `0`, labels ``

## Rollback
Backups pré-upload `before__*` neste diretório.
