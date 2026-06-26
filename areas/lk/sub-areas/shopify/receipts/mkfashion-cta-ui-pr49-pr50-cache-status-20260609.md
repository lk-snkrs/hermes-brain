# Receipt — mKFashion CTA UI correction + public cache status

Data: 2026-06-09
Perfil: LK Shopify
Repo: `lk-snkrs/lk-new-theme`

## Correção do Lucas

Lucas informou que o botão do Provador ficou horrível e que deve seguir exatamente a lógica de UI/UX dos botões da PDP (`Adicionar ao carrinho` / `Compre Já`), não parecer um card/selo da Trust Bar.

Imagem enviada: `/opt/data/profiles/lk-shopify/image_cache/img_2266a320d9cf.jpg`

Problemas visuais na imagem:

- Ícone/câmera do vendor visível.
- Badge vermelho `NEW` visível.
- Texto `PROVE EM VOCÊ` com cara de selo/card, não CTA.
- Visual distante dos CTAs da PDP.

## Decisão de UI aplicada

O Provador deve renderizar como CTA secundário limpo:

- Texto único: `Provar Virtualmente`.
- Sem ícone.
- Sem badge `NEW`.
- Fundo branco `#fff`.
- Texto preto `#111`.
- Borda clara `#d8d8d8`.
- Altura mínima `50px`.
- Tipografia uppercase, 11px, peso 500, letter-spacing `.18em`.
- Continua após `.pi-actions .shopify-payment-button` e antes da Trust Bar.
- `Compre Já` continua visível no mobile.

## Fluxo seguido

### DEV

PR: https://github.com/lk-snkrs/lk-new-theme/pull/49
Merge commit: `1364f949e1e6`

Verificações:

```text
PASS origin/dev CTA UI verification
PASS shopify_dev_readback_cta_ui
```

Readback DEV:

- Theme: `155065450718`
- Name: `lk-new-theme/dev`
- Role: `unpublished`
- `cta_style`: 3
- `button_text`: 1
- `aria`: 1
- `old_offwhite`: 0
- `NEW`: 0
- `width:24px`: 0
- old mKFashion refs: 0
- `Compre Já` mobile visible: true

### Production

PR: https://github.com/lk-snkrs/lk-new-theme/pull/50
Merge commit: `f331654d6721`

Verificações:

```text
PASS origin/production CTA UI verification
PASS shopify_production_readback_cta_ui
```

Readback Production main:

- Theme: `155065417950`
- Name: `lk-new-theme/production`
- Role: `main`
- `cta_style`: 3
- `button_text`: 1
- `old_offwhite`: 0
- `width:24px`: 0
- `NEW`: 0
- `Compre Já` mobile visible: true

## Public cache / edge status

Mesmo com GitHub + Shopify Admin readback corretos, a URL pública sem preview continuou servindo o bloco antigo:

- `cta_style`: 0
- `button_text`: 0
- `old_offwhite`: 3
- `icon24_in_tune`: 1

Isso ocorreu em múltiplos rounds com cache-bust.

Para validar se o código correto está mesmo no theme main, foi testada a mesma PDP com `preview_theme_id=155065417950`:

URL:

`https://www.lksneakers.com.br/products/new-balance-530-white-natural-indigo-1?preview_theme_id=155065417950&_qa=main_preview_check`

Resultado:

```text
status: 200
cta_style: 3
old_offwhite: 0
button_text: 1
icon24: 0
cache_marker: 1
sdk: 1
```

Conclusão: o tema main/Production está com o código novo; a URL pública sem preview ainda está presa em cache/edge/stale compiled HTML no momento da verificação.

## Cache refresh adicional

Para tentar forçar recompilação da PDP sem write direto no Shopify Admin, foi feito um touch mínimo na seção PDP:

### DEV cache refresh

PR: https://github.com/lk-snkrs/lk-new-theme/pull/51
Merge commit: `437b713fdc75`

### Production cache refresh

PR: https://github.com/lk-snkrs/lk-new-theme/pull/52
Merge commit: `c2e1ab0cb144`

Production readback depois do cache refresh:

- layout novo OK
- section marker OK
- `payment_visible`: true
- `payment_hide_none`: false

Mas a URL pública sem preview ainda continuou stale durante os rounds da sessão.

## Non-actions

- Não houve write direto via Shopify Asset API/Admin na theme Production.
- Não houve mudança em produto, preço, estoque, checkout, app config, GMC, Klaviyo, WhatsApp ou campanha.
- Secrets não foram impressos.

## Estado final honesto

- Código correto: mergeado em DEV e Production.
- Shopify Admin/readback Production: correto.
- Main theme com `preview_theme_id=155065417950`: correto.
- URL pública sem preview: ainda stale no momento da verificação; não declarar live público 100% até novo check sem preview passar.

## Rollback

Rollback lógico dos PRs:

- CTA UI DEV: revert `1364f949e1e6`
- CTA UI Production: revert `f331654d6721`
- Cache refresh DEV: revert `437b713fdc75`
- Cache refresh Production: revert `c2e1ab0cb144`

## Referência atualizada

Skill/reference atualizada para registrar que a interpretação correta não é Trust Bar/card, e sim CTA secundário da PDP, sem ícone e sem `NEW`; também registra o pitfall de Admin readback fresco vs público stale.
