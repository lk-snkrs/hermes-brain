# Approval packet — Curadoria LK PDP label font-weight light

Data: 2026-06-06

## Contexto

Lucas reportou que a fonte dos títulos/labels dos produtos em "outras variações" está com aparência pesada/negrito e deve ser light.

## Diagnóstico read-only

Página pública testada:

- `https://lksneakers.com.br/products/tenis-on-running-cloudsolo-loewe-lime-green-amarelo`

Resultado atual em Production via CDP:

- bloco presente: `true`
- marker: `top30-on-running-cloudsolo-loewe`
- labels renderizados: `Black`, `Turquoise`, `White Light Grey`, `White Orange`, `Dark Sand Cream`
- `getComputedStyle(.lk-variante__label).fontWeight`: `400`
- `getComputedStyle(.lk-variante__label, '::after').fontWeight`: `300`

Interpretação:

- A correção anterior mirou o pseudo-elemento `::after` em `assets/lk-product-card.css`.
- No grupo Cloudsolo, os textos são renderizados diretamente no `span.lk-variante__label`, não via `::after`.
- Por isso o visual continua em `400` no texto real, enquanto o `::after` aparece como `300` mas com `content: none`.

## Correção proposta

Asset a alterar:

- `assets/lk-variante.css`

Patch local preparado:

```css
/* LK Curadoria PDP label weight hotfix 2026-06-06: labels should render light, not regular/bold. */
.lk-variante__label,
.lk-variante__item.is-current .lk-variante__label{
  font-weight:300 !important;
}
```

## Validação por preview/injeção local

Foi feita simulação no browser por injeção temporária de CSS, sem write externo:

Antes:

- labels: `400`, `400`, `400`, `400`, `400`

Depois com CSS proposto:

- labels: `300`, `300`, `300`, `300`, `300`
- `::after`: `300` mantido

## Risco

Baixo.

Impacto esperado:

- Todas as labels `.lk-variante__label` da Curadoria/Outras variações passam de `400` para `300`.
- Também neutraliza o peso `500` do estado atual (`.is-current`) caso ele apareça em outros contextos.

Não altera:

- produtos;
- estoque;
- preço;
- checkout;
- apps;
- lógica Liquid;
- imagens;
- grupos de curadoria.

## Rollback

Restaurar a regra anterior no fim de `assets/lk-variante.css`:

```css
/* LK Curadoria PDP label weight hotfix 2026-06-05: labels should not render bold. */
.lk-variante__label,
.lk-variante__item.is-current .lk-variante__label{
  font-weight:400;
}
```

## Próxima decisão solicitada

Aprovar aplicação primeiro no tema DEV (`155065450718`) do asset:

- `assets/lk-variante.css`

Após DEV:

1. readback Shopify DEV;
2. QA visual/CDP em PDP Cloudsolo + PDP com label via `::after`;
3. se aprovado, preparar PR/merge para Production.
