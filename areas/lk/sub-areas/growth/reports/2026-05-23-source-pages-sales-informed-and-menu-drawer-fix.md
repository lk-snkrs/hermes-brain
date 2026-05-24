# 2026-05-23 — Source Pages sales-informed hero + mobile drawer fix

## Pedido do Lucas

1. Corrigir todas as páginas GEO/SEO feitas antes sem lógica de hero baseada em produto mais vendido.
2. Corrigir o menu mobile que sobrepunha o header no preview do tema.

## O que foi feito

### 1) Source Pages GEO — hero sales-informed

Foram reprocessadas as páginas-fonte GEO com base em dados reais de pedidos Shopify, priorizando produtos ACTIVE e mais vendidos como hero/foto principal e primeiro item da vitrine.

URLs finais vigentes:

- `https://lksneakers.com.br/pages/onitsuka-tiger-original-brasil-guia-lk`
  - Hero: `Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo`
  - Handle produto: `tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo`
  - Base de vendas: 176 unidades / 169 pedidos no scan

- `https://lksneakers.com.br/pages/new-balance-204l-original-brasil-guia-lk`
  - Hero: `Tênis New Balance 204L Mushroom Arid Stone Marrom`
  - Handle produto: `tenis-new-balance-204l-mushroom-arid-stone-marrom`
  - Base de vendas: 117 unidades / 113 pedidos no scan

- `https://lksneakers.com.br/pages/adidas-sl-72-og-vs-rs-guia-lk`
  - Hero: `Tênis adidas SL 72 Og Maroon Almost Yellow Marrom`
  - Handle produto: `tenis-adidas-sl72-og-maroon-almost-yellow-marrom`
  - Base de vendas: 39 unidades / 39 pedidos no scan

- `https://lksneakers.com.br/pages/yeezy-original-brasil-guia-lk`
  - Hero: `Yeezy Boost 350 V2 Onyx`
  - Handle produto: `yeezy-boost-350-v2-onyx`

- `https://lksneakers.com.br/pages/air-jordan-travis-scott-original-brasil-guia-lk`
  - Hero: `Air Jordan 1 Low OG SP x Travis Scott Medium Olive`
  - Handle produto: `tenis-air-jordan-1-low-og-sp-x-travis-scott-medium-olive-verde`

- `https://lksneakers.com.br/pages/lululemon-original-brasil-guia-lk`
  - Hero: `Jaqueta Lululemon Define Nulu`
  - Handle produto: `jaqueta-lululemon-define-nulu`

Validação pública das URLs finais:

- Todas retornaram HTTP 200.
- Todas têm produto hero esperado presente no HTML.
- Todas com `FAQPage` schema presente.
- Todas com H1 único.
- Termos proibidos zerados nas verificações públicas: `pronta entrega`, `encomenda`, `estoque`, `marketplace`, `legit-check`.

Observação: para contornar cache persistente Shopify/CDN em páginas antigas, foi adotado padrão de handle final com sufixo `-guia-lk`, alinhado ao caso Lululemon.

### 2) Theme production — cache-bust dos cases Liquid

Ajustado o theme production para que os templates hardcoded de source pages usem os handles finais, evitando que os cases antigos continuem servindo conteúdo em cache.

Assets alterados em production:

- `sections/lk-geo-source-pages-v2.liquid`
- `sections/lk-geo-source-pages-packet-d.liquid`
- `sections/main-page.liquid` — removido override antigo específico de Lululemon old handle.

Receipt principal:

- `areas/lk/sub-areas/growth/receipts/shopify-source-pages/final-handle-theme-case-fix-20260523-100401/receipt.json`

### 3) Menu mobile — dev theme

Diagnóstico:

- O drawer mobile usava `top: var(--header-height, 64px)`.
- No mobile real, existe announcement bar acima do header; por isso o drawer/backdrop começava cedo demais e visualmente sobrepunha parte do header.

Correção aplicada apenas no dev theme `lk-new-theme/dev`:

- `sections/lk-header.liquid`
- Drawer e backdrop agora usam `--lk-drawer-offset`.
- JS calcula o offset real via `header.getBoundingClientRect().bottom` antes de abrir o menu.
- Também recalcula em resize/orientation change e durante scroll se o drawer estiver aberto.

Validação via browser console no preview:

- `hasPatch: true`
- `headerBottom: 100`
- `cssVar: 100px`
- `panelTop: 100px`
- `backdropTop: 100px`
- `headerZ: 1001`
- `panelZ: 999`
- Resultado: drawer/backdrop começam abaixo do header real, sem cobrir o header.

Preview:

- `https://lksneakers.com.br/?preview_theme_id=155065450718`

Receipt:

- `areas/lk/sub-areas/growth/receipts/theme-dev/menu-drawer-offset-fix-20260523-095538/receipt.json`

### 4) Menu mobile — production aprovado

Após aprovação explícita do Lucas (`Ficou ótimo aprovado`), o fix do menu mobile foi promovido para o tema principal `lk-new-theme/production` (`155065417950`).

Assets alterados:

- `sections/lk-header.liquid`
  - Mesmo patch validado no dev theme: `--lk-drawer-offset` + `updateDrawerOffset()`.
  - Admin readback confirmado após lag inicial.
- `assets/lk-product-card.css`
  - Override cache-safe temporário/permanente de baixa superfície: `top: var(--lk-drawer-offset, 100px) !important` para `.lk-drawer__panel` e `.lk-drawer__backdrop` no mobile.
  - Motivo: Shopify page cache continuou servindo HTML antigo por alguns minutos; o CSS asset garante que o drawer não sobreponha o header mesmo durante propagação.

Validação pública final:

- URL pública com cache-busting carregou `sections/lk-header.liquid` atualizado.
- `hasDynamicHeader: true`
- `oldInlinePanel: false`
- Browser computed style após simular drawer aberto:
  - `headerBottom: 100`
  - `drawerOffset: 100px`
  - `panelTop: 100px`
  - `backdropTop: 100px`
  - `panelZ: 999`
  - `backdropZ: 998`

Receipts:

- `areas/lk/sub-areas/growth/receipts/theme-production/menu-drawer-offset-fix-20260523-131306/receipt.json`
- `areas/lk/sub-areas/growth/receipts/theme-production/menu-drawer-css-cache-override-20260523-132022/receipt.json`

## Rollback

### Source pages / production

- Restaurar assets pelos arquivos `.before.liquid` no receipt:
  - `final-handle-theme-case-fix-20260523-100401/`
- Reverter handles das páginas pelos JSON `.before.json` em:
  - `source-pages-alt-handles-sales-informed-20260523-125230/`
- Remover redirects criados se necessário.

### Menu dev

- Restaurar `sections/lk-header.liquid` a partir de:
  - `theme-dev/menu-drawer-offset-fix-20260523-095538/lk-header.before.liquid`

### Menu production

- Restaurar `sections/lk-header.liquid` a partir de:
  - `theme-production/menu-drawer-offset-fix-20260523-131306/lk-header.before.liquid`
- Restaurar `assets/lk-product-card.css` a partir de:
  - `theme-production/menu-drawer-css-cache-override-20260523-132022/lk-product-card.before.css`

## Pendências / watchouts

- As URLs finais estão OK e devem ser usadas como fonte canônica operacional.
- Algumas URLs antigas ainda podem responder 200 temporariamente por cache Shopify/CDN mesmo sem page handle ativo no Admin. Os redirects foram criados, mas o cache público pode demorar a refletir. Cron D+7 foi atualizado para validar URLs finais e redirects.
- Menu mobile já está aplicado em production e validado publicamente. Watchout: manter o override em `assets/lk-product-card.css` até termos certeza de que o cache de página não está servindo HTML antigo para nenhum usuário; depois pode ser removido se a seção dinâmica permanecer estável.

## Cron / Impact Review

Atualizados/criados:

- `LK GEO Source Pages D+7 Impact Review` — job `e0088791bb3b`
- `LK D+7 impact review — Packet D GEO Source Pages` — job `31b40105c4e5`
- `LK Menu Drawer Production D+7 Review` — job `f81883cce339`
