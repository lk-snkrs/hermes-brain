# Curadoria LK — Title Escape Static Render Fix Receipt

Data UTC: `2026-06-02T12:48:29.069183+00:00`

## Escopo
Tema dev apenas; correção de Liquid syntax por apóstrofos em títulos estáticos.

## Readback
- `snippets/lk-variante-samba-jane.liquid`: readback `False`, sha `c53ec26eef9723fb`, size `3607`
- `snippets/lk-variante-air-jordan-1-low.liquid`: readback `True`, sha `14dddf8b28819c96`, size `3135`
- `snippets/lk-variante-air-jordan-1-low-travis.liquid`: readback `True`, sha `255e350eed375560`, size `3376`

## QA
- `samba_white_black`: status `200`, blocks `1`, items `5`, current `False`, liquid `0`, labels `White Blue Gum, Scarlet Gum, Black White Gum, Green White Gum, Cream Black Gum`
- `samba_cream`: status `200`, blocks `1`, items `5`, current `False`, liquid `0`, labels `White Black, White Blue Gum, Scarlet Gum, Black White Gum, Green White Gum`
- `aj1_vintage`: status `200`, blocks `1`, items `5`, current `False`, liquid `0`, labels `Midnight Navy, Jade Smoke, Black Medium Grey, Taxi, Light Smoke Grey`
- `aj1_midnight`: status `200`, blocks `1`, items `5`, current `False`, liquid `0`, labels `Vintage Grey, Jade Smoke, Black Medium Grey, Taxi, Light Smoke Grey`
- `travis_medium`: status `200`, blocks `1`, items `5`, current `False`, liquid `0`, labels `Velvet Brown, Black Phantom, Reverse Mocha, Mocha, Canary`
- `travis_velvet`: status `200`, blocks `1`, items `5`, current `False`, liquid `0`, labels `Medium Olive, Black Phantom, Reverse Mocha, Mocha, Canary`
- `high_control`: status `200`, blocks `0`, items `0`, current `False`, liquid `0`, labels ``
- `prod_control`: status `200`, blocks `0`, items `0`, current `False`, liquid `0`, labels ``

## Rollback
Backups `before__*` neste diretório.
