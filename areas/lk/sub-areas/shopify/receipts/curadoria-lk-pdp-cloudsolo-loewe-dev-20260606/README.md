# Receipt — Curadoria LK PDP Cloudsolo Loewe DEV

Data: 2026-06-06T10:16:27Z

## Aprovação

Lucas aprovou aplicar no tema DEV `155065450718` o pacote Curadoria LK PDP Cloudsolo Loewe em `snippets/lk-variante-top30-visited-v2.liquid`, adicionando o grupo `top30-on-running-cloudsolo-loewe`, sem mexer em Production/produtos/preço/estoque/checkout.

## Escopo executado

Tema:

- ID: `155065450718`
- Nome: `lk-new-theme/dev`
- Role verificado antes do write: `unpublished`

Asset alterado:

- `snippets/lk-variante-top30-visited-v2.liquid`

Mudança:

- Adicionado 1 grupo nos arrays `lk_top30_*`:
  - marker: `top30-on-running-cloudsolo-loewe`
  - name: `On Running Cloudsolo Loewe`
  - handles: 16
  - labels: 16
  - images: 16

## Grupo adicionado

Handles/labels:

1. `tenis-on-running-cloudsolo-loewe-lime-green-amarelo` — `Lime Green`
2. `tenis-on-running-cloudsolo-loewe-black-preto` — `Black`
3. `tenis-on-running-cloudsolo-loewe-turquoise-azul` — `Turquoise`
4. `tenis-on-running-cloudsolo-loewe-white-light-grey-cinza` — `White Light Grey`
5. `tenis-on-running-cloudsolo-loewe-white-orange-laranja` — `White Orange`
6. `tenis-on-running-cloudsolo-loewe-dark-sand-cream-bege` — `Dark Sand Cream`
7. `tenis-on-running-cloudsolo-loewe-sand-turquoise-bege` — `Sand Turquoise`
8. `tenis-on-running-cloudsolo-loewe-black-white-preto` — `Black / White`
9. `tenis-on-running-cloudsolo-loewe-khaki-green-sand-verde` — `Khaki Green Sand`
10. `tenis-on-running-cloudsolo-loewe-dark-brown-black-marrom` — `Dark Brown Black`
11. `tenis-on-running-cloudsolo-loewe-black-eggshell-preto` — `Black Eggshell`
12. `tenis-on-running-cloudsolo-loewe-red-eggshell-vermelho` — `Red Eggshell`
13. `tenis-on-running-cloudsolo-loewe-taupe-eggshell-marrom` — `Taupe Eggshell`
14. `tenis-on-running-cloudsolo-loewe-teal-eggshell-azul` — `Burgundy Eggshell`
15. `tenis-on-running-cloudsolo-loewe-sand-burgundy-bege` — `Sand Burgundy`
16. `tenis-on-running-cloudsolo-loewe-teal-eggshell-azul-1` — `Teal Eggshell`

## Readback Admin API

Readback final:

- SHA256: `4b0835bf2d5b12928aebc9a6a71733d86909bb7971a4cfc00a22ef28fcbb3a3f`
- marker count: `1`
- array lengths: `[28, 28, 28, 28, 28]`
- array lengths equal: `true`
- new group index: `27`
- new group handles: `16`
- new group labels: `16`
- new group images: `16`
- all images Shopify CDN: `true`
- malformed https count: `0`

Readback salvo:

- `20260606-dev-theme-155065450718-snippets__lk-variante-top30-visited-v2.readback.liquid`
- `20260606-dev-readback-static-checks.json`

## QA CDP no preview DEV

Arquivos:

- `20260606-dev-cdp-qa-summary.json`

PDPs testadas:

### Lime Green

URL:

- `/products/tenis-on-running-cloudsolo-loewe-lime-green-amarelo`

Resultado:

- bloco presente: `true`
- marker: `top30-on-running-cloudsolo-loewe`
- rail display: `grid`
- cards: `5`
- produto atual excluído: `true`
- imagens: `5`, CDN ok
- labels: `Black`, `Turquoise`, `White Light Grey`, `White Orange`, `Dark Sand Cream`
- fontWeight span: `400`
- fontWeight visual `::after`: `300`

### Black

URL:

- `/products/tenis-on-running-cloudsolo-loewe-black-preto`

Resultado:

- bloco presente: `true`
- marker: `top30-on-running-cloudsolo-loewe`
- rail display: `grid`
- cards: `5`
- produto atual excluído: `true`
- imagens: `5`, CDN ok
- labels: `Lime Green`, `Turquoise`, `White Light Grey`, `White Orange`, `Dark Sand Cream`
- fontWeight span: `400`
- fontWeight visual `::after`: `300`

### Teal Eggshell

URL:

- `/products/tenis-on-running-cloudsolo-loewe-teal-eggshell-azul-1`

Resultado:

- bloco presente: `true`
- marker: `top30-on-running-cloudsolo-loewe`
- rail display: `grid`
- cards: `5`
- produto atual excluído: `true`
- imagens: `5`, CDN ok
- labels: `Lime Green`, `Black`, `Turquoise`, `White Light Grey`, `White Orange`
- fontWeight span: `400`
- fontWeight visual `::after`: `300`

## Rollback

Backup pré-write:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-cloudsolo-loewe-dev-20260606/20260606T101234Z-dev-theme-155065450718-snippets__lk-variante-top30-visited-v2.before.liquid`

Rollback: restaurar esse asset no tema DEV `155065450718`.

## Não feito

- Production não foi alterado.
- Nenhum produto foi alterado.
- Preço/estoque/checkout não foram tocados.
- Nenhum app/campanha/Klaviyo/GMC/Meta foi alterado.

## Observação operacional

O primeiro readback imediato retornou stale por alguns segundos; revalidação Admin API confirmou o asset final com marker e arrays corretos. QA storefront/CDP passou no preview DEV depois do readback final.
