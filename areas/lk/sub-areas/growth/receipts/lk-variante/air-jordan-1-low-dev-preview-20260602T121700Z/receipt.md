# LK Variante — Air Jordan 1 Low Dev Preview Receipt

Data UTC: 2026-06-02T12:17:16.045808+00:00

## Regra aplicada
Piloto criado apenas para **Air Jordan 1 Low** — mesma silhueta/tipo, variação por cor/material.

Excluído do grupo neste MVP:
- Air Jordan 1 High
- Air Jordan 1 Mid
- Air Jordan 1 OG/SP/SE/Elevate/collabs especiais

## Produto de teste
`/products/air-jordan-1-low-vintage-grey`

## Assets alterados no dev
- `snippets/lk-variante-air-jordan-1-low.liquid`
- `sections/lk-pdp.liquid`

## Readback
- `snippets/lk-variante-air-jordan-1-low.liquid`: readback_match `True`, sha `acc107df7ce6d15f`, size `2396`
- `sections/lk-pdp.liquid`: readback_match `True`, sha `12581eb25d1ed4f7`, size `122270`

## Grupo hardcoded do preview
- `Midnight Navy` — `tenis-air-jordan-1-low-midnight-navy-wolf-grey-azul-marinho`
- `Vintage Grey` — `air-jordan-1-low-vintage-grey`
- `Jade Smoke` — `tenis-air-jordan-1-low-jade-smoke-multicolor`
- `Black Medium Grey` — `air-jordan-1-low-black-medium-grey`
- `Taxi` — `air-jordan-1-low-taxi`
- `Light Smoke Grey` — `air-jordan-1-low-light-smoke-grey`

## QA

### aj1_low_vintage_grey
- status: `200`
- AJ1 Low marker: `1`
- Samba marker: `0`
- items: `3`
- Curadoria LK: `1`
- labels: `Black Medium Grey, Taxi, Light Smoke Grey`
- Liquid errors: `0`

### aj1_low_midnight_navy
- status: `200`
- AJ1 Low marker: `1`
- Samba marker: `0`
- items: `5`
- Curadoria LK: `1`
- labels: `Vintage Grey, Jade Smoke, Black Medium Grey, Taxi, Light Smoke Grey`
- Liquid errors: `0`

### aj1_high_control
- status: `404`
- AJ1 Low marker: `0`
- Samba marker: `0`
- items: `0`
- Curadoria LK: `0`
- labels: ``
- Liquid errors: `0`

### samba_control
- status: `200`
- AJ1 Low marker: `0`
- Samba marker: `1`
- items: `5`
- Curadoria LK: `1`
- labels: `Cream Black Gum, White Blue Gum, Black White Gum, Scarlet Gum, Green White Gum`
- Liquid errors: `0`

### production_control
- status: `200`
- AJ1 Low marker: `0`
- Samba marker: `0`
- items: `0`
- Curadoria LK: `0`
- labels: ``
- Liquid errors: `0`

## Rollback
Backups pré-upload salvos neste diretório. Reupar `before__sections__lk-pdp.liquid` e remover/reverter o snippet Air Jordan 1 Low para rollback dev.
