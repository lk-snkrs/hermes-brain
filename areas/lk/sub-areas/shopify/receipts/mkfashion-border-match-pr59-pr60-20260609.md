# Receipt — mKFashion CTA border match

Data: 2026-06-09
Perfil: LK Shopify
Repo: `lk-snkrs/lk-new-theme`

## Pedido

Lucas enviou print mostrando que a borda do botão `Provar Virtualmente` estava diferente da borda do botão `Compre Já` e pediu igualar.

Imagem: `/opt/data/profiles/lk-shopify/image_cache/img_0ca169246e72.jpg`

## Diagnóstico

`Compre Já` usa no tema:

```css
.pi-actions .shopify-payment-button__button--unbranded {
  border: 1px solid var(--light-gray) !important;
}
```

O Provador ainda usava borda hard-coded mais escura:

```css
border: 1px solid #d8d8d8;
```

## Correção

Atualizado `layout/theme.liquid` e cópias repo-wide em `projetos/lk-new-theme/...`:

- Anchor config do Provador agora usa:

```css
border:1px solid var(--light-gray);
```

- Runtime tuner agora define inicialmente:

```js
button.style.border = '1px solid var(--light-gray)';
```

- E copia a borda computada do próprio botão `Compre Já` quando disponível:

```js
var buyNowButton = document.querySelector('.pi-actions .shopify-payment-button__button--unbranded, .pi-actions .shopify-payment-button__button');
if (buyNowButton && window.getComputedStyle) {
  var buyNowBorder = window.getComputedStyle(buyNowButton).border;
  if (buyNowBorder && buyNowBorder !== '0px none rgb(0, 0, 0)') button.style.border = buyNowBorder;
}
```

Mantido:

- CTA limpo `Provar Virtualmente`.
- Sem ícone.
- Sem `NEW`.
- Gap equalizer preservado.
- `Compre Já` preservado.

## Fluxo

### DEV primeiro

PR: https://github.com/lk-snkrs/lk-new-theme/pull/59
Merge commit: `c168aad0bbe3`

Verificações:

```text
PASS origin/dev border match verification
PASS shopify_dev_border_match_readback
```

### Production depois

PR: https://github.com/lk-snkrs/lk-new-theme/pull/60
Merge commit: `8f112d3d944d`

Verificações:

```text
PASS origin/production border match verification
PASS shopify_production_border_match_readback
```

Readback Production:

- Theme: `155065417950`
- Name: `lk-new-theme/production`
- Role: `main`
- `anchor_light_gray`: 3
- `old_d8`: 0
- `runtime_light_gray`: 1
- `buy_now_selector`: 1
- `computed_border`: 1
- `button_text`: 1
- `icon24`: 0
- `NEW`: 0

## Non-actions

- Não houve write direto via Shopify Admin/Asset API.
- Não houve alteração de produto, preço, estoque, checkout, app config, GMC, Klaviyo, WhatsApp ou campanha.
- Segredos não foram impressos.

## Rollback

- Reverter DEV: `c168aad0bbe3`
- Reverter Production: `8f112d3d944d`
