# Receipt — Curadoria LK PDP label light DEV

Data: 2026-06-06T13:33:38Z

## Aprovação

Lucas respondeu: "Aprovo" após pedido explícito para aplicar no tema DEV a correção `font-weight:300` das labels de outras variações.

## Escopo executado

Tema:

- DEV theme ID: `155065450718`

Asset:

- `assets/lk-variante.css`

Mudança alvo:

```css
/* LK Curadoria PDP label weight hotfix 2026-06-06: labels should render light, not regular/bold. */
.lk-variante__label,
.lk-variante__item.is-current .lk-variante__label{
  font-weight:300 !important;
}
```

Não foram alterados:

- produtos;
- preço;
- estoque;
- checkout;
- apps;
- Liquid;
- grupos de curadoria;
- imagens;
- GMC/Meta/Klaviyo/Tiny.

## Readback DEV

Diretório de execução:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-label-light-dev-20260606/20260606T133338Z`

Resultado:

- `ok`: `true`
- theme: `155065450718`
- asset key: `assets/lk-variante.css`
- before bytes: `2745`
- after bytes: `2745`
- before SHA256: `ab25b871819f9e5699490bb68303909cd5ff96610db39a37ffc0d04e2edd0128`
- after SHA256: `ab25b871819f9e5699490bb68303909cd5ff96610db39a37ffc0d04e2edd0128`
- candidate equals readback: `true`
- contém `font-weight:300 !important`: `true`
- contém hotfix antigo `font-weight:400;`: `false`

Observação: a aplicação foi idempotente no DEV; o readback anterior do DEV já continha a regra candidata, e o PUT confirmou que o asset DEV continua exatamente igual ao candidato.

## QA visual DEV — texto real no span

PDP:

- `https://lksneakers.com.br/products/tenis-on-running-cloudsolo-loewe-lime-green-amarelo?preview_theme_id=155065450718`

Resultado:

- bloco: `true`
- marker: `top30-on-running-cloudsolo-loewe`
- rail: `grid`
- cards: `5`
- labels: `Black`, `Turquoise`, `White Light Grey`, `White Orange`, `Dark Sand Cream`
- `getComputedStyle(.lk-variante__label).fontWeight`: `300` em todos os 5 cards
- `getComputedStyle(.lk-variante__label, '::after').fontWeight`: `300`
- `::after content`: `none`, esperado nesse grupo

## QA visual DEV — labels via pseudo-elemento ::after

PDP:

- `https://lksneakers.com.br/products/tenis-air-jordan-1-mid-glitter-swoosh-azul?preview_theme_id=155065450718`

Resultado:

- bloco: `true`
- marker: `top30-air-jordan-1-mid-regular`
- rail: `grid`
- cards: `5`
- labels via `::after`: `Wolf Grey`, `Panda`, `Electro Orange`, `Canyon Rust`, `Aqua Tint`
- span font-weight: `300`
- `::after` font-weight: `300`
- `::after content`: preenchido corretamente

## Interpretação

O bug era de alvo CSS:

- A regra anterior corrigia `::after`.
- No grupo Cloudsolo, o texto visível é o `span.lk-variante__label`, não o `::after`.
- A regra em `assets/lk-variante.css` corrige o texto real e preserva os casos que usam `::after`.

## Rollback DEV

Restaurar o backup `before.value` do diretório:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-label-light-dev-20260606/20260606T133338Z/before.value`

Ou reverter para:

```css
/* LK Curadoria PDP label weight hotfix 2026-06-05: labels should not render bold. */
.lk-variante__label,
.lk-variante__item.is-current .lk-variante__label{
  font-weight:400;
}
```

## Status

DEV readback + QA visual: **passou**.

## Próxima decisão

Para Production, promover via fluxo GitHub/PR e readback/QA live após aprovação explícita.
