# Receipt — Merge Production: Curadoria LK PDP label light

Data: 2026-06-06T13:39:22Z

## Aprovação

Lucas corrigiu o termo operacional: "Não é promover, é fazer merge".

Aprovação explícita registrada:

- "Aprovo fazer merge para Production da correção font-weight:300"

## Escopo executado

Merge para Production via GitHub PR.

Asset alterado:

- `assets/lk-variante.css`

Mudança:

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

## GitHub merge

Branch:

- `hermes/lk-variante-label-light-production-20260606`

Commit local:

- `1b2a415a61bb17965f3bdcbb77bb3f1eddd08a71`

PR:

- https://github.com/lk-snkrs/lk-new-theme/pull/26

Merge:

- mergeable: `true`
- mergeable_state: `clean`
- merged: `true`
- merge SHA: `e2a1ede70df53b20b6c423d1f1ba2771ec985e7c`
- remote branch deleted: `true`

Verificação Git:

- `git diff --check -- assets/lk-variante.css`: passou
- diff: `1 file changed, 2 insertions(+), 2 deletions(-)`

## Shopify Production readback

Production theme:

- `155065417950`

Readback asset:

- `assets/lk-variante.css`

Resultado:

- bytes: `2745`
- SHA256: `ab25b871819f9e5699490bb68303909cd5ff96610db39a37ffc0d04e2edd0128`
- contém `font-weight:300 !important`: `true`
- contém hotfix antigo `font-weight:400;`: `false`

Arquivo:

- `20260606T133922Z/readback-1.json`

## QA live Production — texto real no span

PDP pública:

- `https://lksneakers.com.br/products/tenis-on-running-cloudsolo-loewe-lime-green-amarelo`

Resultado CDP:

- marker: `top30-on-running-cloudsolo-loewe`
- cardCount: `5`
- labels: `Black`, `Turquoise`, `White Light Grey`, `White Orange`, `Dark Sand Cream`
- span font-weight: `300`, `300`, `300`, `300`, `300`
- `::after` font-weight: `300`, `300`, `300`, `300`, `300`
- `::after content`: `none` em todos, esperado para esse grupo

Arquivo:

- `20260606T133922Z/production-live-cloudsolo-cdp.json`

## QA live Production — labels via pseudo-elemento ::after

PDP pública:

- `https://lksneakers.com.br/products/tenis-air-jordan-1-mid-glitter-swoosh-azul`

Resultado CDP:

- marker: `top30-air-jordan-1-mid-regular`
- cardCount: `5`
- labels: `Wolf Grey`, `Panda`, `Electro Orange`, `Canyon Rust`, `Aqua Tint`
- span font-weight: `300`, `300`, `300`, `300`, `300`
- `::after` font-weight: `300`, `300`, `300`, `300`, `300`
- `::after content`: preenchido corretamente

Arquivo:

- `20260606T133922Z/production-live-after-cdp.json`

## Interpretação

Correção em Production cobriu os dois caminhos de renderização:

1. texto real no `span.lk-variante__label`, usado no grupo Cloudsolo;
2. texto visual via `.lk-variante__label::after`, usado em grupos com anti-stale visual labels.

## Rollback

Opção preferencial:

- Reverter o PR #26 / merge SHA `e2a1ede70df53b20b6c423d1f1ba2771ec985e7c`.

Rollback CSS manual:

```css
/* LK Curadoria PDP label weight hotfix 2026-06-05: labels should not render bold. */
.lk-variante__label,
.lk-variante__item.is-current .lk-variante__label{
  font-weight:400;
}
```

## Status final

Merge Production + Shopify readback + QA live público: **passou**.
