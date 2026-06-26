# LK Variante — Air Jordan 1 Low Travis Scott Dev Preview Receipt

Data UTC: 2026-06-02T12:27:17.921281+00:00

## Correção de regra
Cápsula Travis Scott separada da família Air Jordan 1 Low regular. Não mistura Travis Scott com colorways normais.

## Observação de ranking
A ordem deste preview é **provisória/curadoria de proximidade**, não declarada como ranking final de mais vendidos. Para produção, precisa refresh/score de vendas antes.

## Assets alterados no dev
- `snippets/lk-variante-air-jordan-1-low-travis.liquid`
- `sections/lk-pdp.liquid`

## Readback
- `snippets/lk-variante-air-jordan-1-low-travis.liquid`: readback_match `True`, sha `eeed131bdb0f8fc6`, size `2500`
- `sections/lk-pdp.liquid`: readback_match `True`, sha `ef7ce93499288df3`, size `122345`

## Grupo preview Travis Scott
- `Medium Olive` — `tenis-air-jordan-1-low-og-sp-x-travis-scott-medium-olive-verde`
- `Reverse Mocha` — `travis-scott-x-air-jordan-1-low-og-reverse-mocha`
- `Velvet Brown` — `tenis-air-jordan-1-low-og-sp-x-travis-scott-velvet-brown-marrom`
- `Black Phantom` — `travis-scott-x-air-jordan-1-low-og-sp-black-phantom`
- `Mocha` — `tenis-air-jordan-1-low-og-sp-x-travis-scott-mocha`
- `Canary` — `tenis-travis-scott-x-air-jordan-1-low-og-canary-amarelo`

## QA

### travis_medium_olive
- status: `200`
- Travis marker: `1`
- Regular AJ1 Low marker: `0`
- items: `5`
- labels: `Reverse Mocha, Velvet Brown, Black Phantom, Mocha, Canary`
- produto atual no bloco: `False`
- Liquid errors: `0`

### regular_low_control
- status: `200`
- Travis marker: `0`
- Regular AJ1 Low marker: `1`
- items: `5`
- labels: `Vintage Grey, Jade Smoke, Black Medium Grey, Taxi, Light Smoke Grey`
- produto atual no bloco: `False`
- Liquid errors: `0`

### high_control
- status: `200`
- Travis marker: `0`
- Regular AJ1 Low marker: `0`
- items: `0`
- labels: ``
- produto atual no bloco: `False`
- Liquid errors: `0`

### production_travis_control
- status: `200`
- Travis marker: `0`
- Regular AJ1 Low marker: `0`
- items: `0`
- labels: ``
- produto atual no bloco: `False`
- Liquid errors: `0`

## Rollback
Backups pré-upload salvos neste diretório. Reupar `before__sections__lk-pdp.liquid` e remover/reverter o snippet Travis para rollback dev.
