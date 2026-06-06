# Approval packet — Curadoria LK PDP label light fix

Data: 2026-06-06

## Pedido/correção de Lucas

Lucas apontou que a fonte dos títulos dos produtos em `CURADORIA LK / OUTRAS VARIAÇÕES` ainda está em negrito e deve ser light.

## Diagnóstico read-only

PDP analisada:

- `tenis-air-jordan-1-mid-glitter-swoosh-azul`

CDP/computed style:

- `.lk-variante` presente: true
- `.lk-variante__rail` display: `grid`
- cards: 5
- `.lk-variante__label` base: `fontWeight: 400`, mas `fontSize: 0px`

Causa real encontrada:

- o texto visual está sendo renderizado por pseudo-elemento `::after` no asset `assets/lk-product-card.css`, não pelo texto base do span.
- regra atual:

```css
.lk-variante .lk-variante__item[href^="/products/"] .lk-variante__label::after{font-size:12px;line-height:1.15;font-weight:600;white-space:normal;color:inherit;}
```

Portanto o hotfix anterior em `assets/lk-variante.css` deixou o span em 400, mas não pegou o texto visual do `::after`, que continua 600.

## Patch proposto

Arquivo alvo DEV:

- Theme DEV: `155065450718` (`lk-new-theme/dev`, unpublished)
- Asset: `assets/lk-product-card.css`

Alteração exata:

```diff
-.lk-variante .lk-variante__item[href^="/products/"] .lk-variante__label::after{font-size:12px;line-height:1.15;font-weight:600;white-space:normal;color:inherit;}
+.lk-variante .lk-variante__item[href^="/products/"] .lk-variante__label::after{font-size:12px;line-height:1.15;font-weight:300;white-space:normal;color:inherit;}
```

## Escopo

Apenas CSS de label visual da Curadoria LK PDP.

Não altera:

- produtos
- preço
- estoque
- checkout
- apps
- snippets de grupos
- imagens/handles/labels
- Production/live

## QA após DEV

Rodar em pelo menos:

- `tenis-air-jordan-1-mid-glitter-swoosh-azul`
- `yeezy-slide-glow-green`
- `new-balance-530-white-natural-indigo-1`

Checks:

- HTTP 200
- bloco Curadoria presente
- 5 cards
- rail `display:grid`
- pseudo-elemento/label visual com `font-weight: 300`
- labels continuam aparecendo
- sem alteração de cards/handles

## Rollback

Restaurar backup pré-write do asset DEV `assets/lk-product-card.css`.

## Aprovação necessária

Para aplicar no DEV, Lucas precisa aprovar explicitamente:

`Aprovo aplicar no tema DEV 155065450718 a correção CSS da Curadoria LK PDP em assets/lk-product-card.css, trocando o font-weight do ::after das labels de 600 para 300, sem mexer em Production.`
