# Receipt — mKFashion Trust Grid lower-gap balance

Data: 2026-06-09
Perfil: LK Shopify
Repo: `lk-snkrs/lk-new-theme`

## Pedido

Lucas enviou print mostrando que o espaçamento abaixo do botão `Provar Virtualmente` até a Trust Bar ainda estava maior que o espaçamento acima do botão. Pediu corrigir para o espaçamento de baixo ser igual ao de cima.

Imagem: `/opt/data/profiles/lk-shopify/image_cache/img_a46ab3d2c0db.jpg`

## Diagnóstico

O host do mKFashion já estava com margem simétrica (`8px 0`), mas a Trust Grid tinha margem própria:

```css
.lk-trust-grid { margin: 14px 0 18px; }
```

Quando a Trust Grid vinha logo após `#mk-tryon-button-host`, essa margem superior adicionava gap extra abaixo do botão.

## Correção

Adicionada regra escopada em `sections/lk-pdp.liquid`:

```css
#mk-tryon-button-host + .lk-trust-grid { margin-top: 0; }
```

A regra só remove o top margin da Trust Grid quando ela é imediatamente precedida pelo host do Provador. O gap inferior passa a ser controlado pelo próprio host do Provador (`8px`), igual ao gap superior.

Mantido:

- `margin-top:8px;margin-bottom:8px` no anchor style.
- `host.style.margin = '8px 0';` no tuner.
- CTA limpo `Provar Virtualmente`.
- Sem ícone / sem `NEW`.
- `Compre Já` preservado.

## Fluxo

### DEV primeiro

PR: https://github.com/lk-snkrs/lk-new-theme/pull/55
Merge commit: `a11d35870c39`

Verificações:

```text
PASS origin/dev trust gap verification
PASS shopify_dev_trust_gap_readback
```

### Production depois

PR: https://github.com/lk-snkrs/lk-new-theme/pull/56
Merge commit: `214db26c611f`

Verificações:

```text
PASS origin/production trust gap verification
PASS shopify_production_trust_gap_readback
```

Readback Production:

- Theme: `155065417950`
- Name: `lk-new-theme/production`
- Role: `main`
- `trust_gap_rule`: 1
- `anchor_symmetric`: 3
- `host_symmetric`: 1
- `button_text`: 1
- `icon24`: 0

## Non-actions

- Não houve write direto via Shopify Admin/Asset API.
- Não houve alteração de produto, preço, estoque, checkout, app config, GMC, Klaviyo, WhatsApp ou campanha.
- Segredos não foram impressos.

## Rollback

- Reverter DEV gap fix: `a11d35870c39`
- Reverter Production gap fix: `214db26c611f`
