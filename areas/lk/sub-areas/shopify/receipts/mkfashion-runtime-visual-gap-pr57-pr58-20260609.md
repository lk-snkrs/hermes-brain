# Receipt — mKFashion runtime visual gap equalizer

Data: 2026-06-09
Perfil: LK Shopify
Repo: `lk-snkrs/lk-new-theme`

## Pedido

Lucas enviou novo print mostrando que o espaçamento acima de `Provar Virtualmente` ainda estava menor que o espaçamento abaixo dele até a Trust Bar.

Imagem: `/opt/data/profiles/lk-shopify/image_cache/img_46697f6380b6.jpg`

## Diagnóstico

O CSS estático anterior não garantiu a igualdade visual percebida. A correção passou a medir o gap real renderizado entre o botão do Provador e a Trust Grid, e usar essa medida como margem superior do próprio host.

## Correção

Adicionado ao tuner do `layout/theme.liquid`:

```js
function balanceVisualGap(host) {
  var trust = host && host.nextElementSibling;
  while (trust && !(trust.classList && trust.classList.contains('lk-trust-grid'))) {
    trust = trust.nextElementSibling;
  }
  if (!trust) trust = document.querySelector('.lk-trust-grid');
  if (!host || !trust || !host.getBoundingClientRect || !trust.getBoundingClientRect) return;

  var hostRect = host.getBoundingClientRect();
  var trustRect = trust.getBoundingClientRect();
  var bottomGap = Math.round(trustRect.top - hostRect.bottom);
  if (bottomGap >= 8 && bottomGap <= 56) {
    host.style.marginTop = bottomGap + 'px';
    host.style.marginBottom = '8px';
  }
}
```

E chamada via `requestAnimationFrame` após o botão ser normalizado.

Mantido:

- CTA limpo `Provar Virtualmente`.
- Sem ícone.
- Sem `NEW`.
- `Compre Já` preservado.
- Host base `8px 0 8px`, com top ajustado dinamicamente para bater com o gap real inferior.

## Fluxo

### DEV primeiro

PR: https://github.com/lk-snkrs/lk-new-theme/pull/57
Merge commit: `c71631ad9763`

Verificações:

```text
PASS origin/dev runtime visual gap verification
PASS shopify_dev_runtime_visual_gap_readback
```

### Production depois

PR: https://github.com/lk-snkrs/lk-new-theme/pull/58
Merge commit: `9cd33c77ce7d`

Verificações:

```text
PASS origin/production runtime visual gap verification
PASS shopify_production_runtime_visual_gap_readback
```

Readback Production:

- Theme: `155065417950`
- Name: `lk-new-theme/production`
- Role: `main`
- `balancer_fn`: 1
- `balancer_call`: 1
- `bottom_gap_calc`: 1
- `margin3`: 1
- `old_margin2`: 0
- `button_text`: 1
- `icon24`: 0
- `NEW`: 0

## Non-actions

- Não houve write direto via Shopify Admin/Asset API.
- Não houve alteração de produto, preço, estoque, checkout, app config, GMC, Klaviyo, WhatsApp ou campanha.
- Segredos não foram impressos.

## Rollback

- Reverter DEV: `c71631ad9763`
- Reverter Production: `9cd33c77ce7d`
