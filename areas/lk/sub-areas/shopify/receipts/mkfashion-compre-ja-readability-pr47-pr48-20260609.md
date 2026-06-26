# Receipt — mKFashion Compre Já restore + readability fix

Data: 2026-06-09
Perfil: LK Shopify
Repo: `lk-snkrs/lk-new-theme`

## Pedido / problema reportado

Lucas apontou dois problemas no Provador Virtual na PDP mobile:

1. `Compre Já` desapareceu.
2. O texto do Provador ficou ilegível; o fundo do Provador deve seguir a cor/família visual da Trust Bar.

Imagem de referência do usuário: `/opt/data/profiles/lk-shopify/image_cache/img_06a891412da1.jpg`.

## Causa encontrada

- O `Compre Já` estava sendo ocultado por CSS mobile pré-existente/ativo em `sections/lk-pdp.liquid`:
  - `.pi-actions .shopify-payment-button { display: none !important; }`
  - `.pi-actions .shopify-payment-button__button`, `.shopify-payment-button__more-options`, `.dynamic-checkout__content` com `display:none`.
- O Provador estava configurado com estilo escuro (`background:#111`) e o SDK/vendor mantinha texto/ícone escuros dentro do shadow DOM, causando baixo contraste.

## Fluxo operacional corrigido

Foi seguido o fluxo exigido por Lucas para tema Shopify:

1. PR em `dev` primeiro.
2. Verificação/readback em DEV.
3. Promoção escopada do commit de DEV para `production`.
4. Verificação/readback em Production.

## PRs

### DEV

- PR: https://github.com/lk-snkrs/lk-new-theme/pull/47
- Base: `dev`
- Merge commit: `47a3e7a66851`
- Título: `fix: restore Compre Já and improve mKFashion readability (#47)`

### Production

- PR: https://github.com/lk-snkrs/lk-new-theme/pull/48
- Base: `production`
- Merge commit: `22baaf2d5ce8`
- Título: `fix: promote Compre Já and mKFashion readability fix (#48)`

A promoção para Production foi feita como promoção escopada do commit já validado em DEV, a partir de `origin/production`, para evitar arrastar drift amplo de `dev`.

## Arquivos alterados

- `sections/lk-pdp.liquid`
- `layout/theme.liquid`
- `projetos/lk-new-theme/layout/theme.liquid`
- `projetos/lk-new-theme/dev-theme/layout/theme.liquid`

## Mudanças aplicadas

### `Compre Já`

No mobile, removido o bloqueio que escondia o dynamic checkout:

- `.pi-actions .shopify-payment-button`: agora `display:block`.
- `.pi-actions .shopify-payment-button__button`: agora `display:flex`, centralizado.
- `.pi-actions .dynamic-checkout__content`: agora `display:block`.
- `.pi-actions .shopify-payment-button__more-options`: continua oculto.

### Provador Virtual / mKFashion

- Botão mKFashion mantém âncora após `.pi-actions .shopify-payment-button`.
- Fundo alterado para `#f5f3f0`, alinhado à Trust Bar.
- Texto forçado para `#111` no botão e spans internos do shadow DOM.
- Borda clara `#e8e6e2`.
- Altura mínima `52px`.
- Remoção do ícone padrão 24px mantida.
- SDK zero-touch mantida; sem retorno do snippet/manual antigo.

## Verificação DEV

### Git `origin/dev`

```text
PASS origin/dev Compre Já + readability static verification
```

Checks:

- `layout/theme.liquid`:
  - `sdk`: 1
  - `offwhite`: 3
  - `button_bg`: 1
  - `span_color`: 1
  - `old_black`: 0
  - `old_refs`: 0
- `sections/lk-pdp.liquid`:
  - `payment_hide_none`: false
  - `payment_visible`: true
  - `button_visible`: true
  - `dynamic_visible`: true
- cópias em `projetos/` com layout mKFashion sincronizado.

### Shopify DEV readback

- Theme ID: `155065450718`
- Nome: `lk-new-theme/dev`
- Role: `unpublished`

Readback:

- Layout:
  - `sdk`: 1
  - `offwhite`: 3
  - `button_bg`: 1
  - `span_color`: 1
  - `old_black`: 0
  - `old_refs`: 0
- Section PDP:
  - `payment_hide_none`: false
  - `payment_visible`: true
  - `button_visible`: true
  - `dynamic_visible`: true

## Verificação Production

### Git `origin/production`

```text
PASS origin/production Compre Já + readability static verification
```

### Shopify Production readback

- Theme ID: `155065417950`
- Nome: `lk-new-theme/production`
- Role: `main`

Readback:

- Layout:
  - `sdk`: 1
  - `offwhite`: 3
  - `button_bg`: 1
  - `span_color`: 1
  - `old_black`: 0
  - `old_refs`: 0
- Section PDP:
  - `payment_hide_none`: false
  - `payment_visible`: true
  - `button_visible`: true
  - `dynamic_visible`: true

### Public HTML marker check

Cache-busted public PDP, 3 rounds:

```text
PASS public_html_marker_check
```

Cada round confirmou:

- SDK: 1
- off-white marker: 3
- `payment_hide_none`: false
- `payment_visible`: true
- `dynamic_visible`: true
- `Adicionar ao carrinho`: presente
- `shopify-payment-button`: presente

## Non-actions

- Nenhum upload direto manual via Shopify Asset API/Admin foi feito.
- Nenhuma alteração em produto, preço, estoque, app, checkout, Klaviyo, WhatsApp, GMC ou campanha.
- Tokens/segredos não foram impressos.

## Rollback

Rollback DEV via PR revertendo:

- `47a3e7a66851`

Rollback Production via PR revertendo:

- `22baaf2d5ce8`

## Aprendizado atualizado

A referência da skill `lk-growth-operations` foi atualizada para registrar:

- não esconder `Compre Já` mobile ao posicionar o Provador;
- validar o child real `.shopify-payment-button__button`, não só o wrapper;
- usar visual off-white/Trust Bar no Provador em vez de preto com texto escuro.
