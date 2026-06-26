# Approval Packet — SEO/CRO Pacote B: performance mobile e scripts de terceiros

Gerado em: 2026-06-18T14:45:07Z

## Status

Somente diagnóstico read-only executado. Nenhum write em Shopify/theme/apps foi feito neste pacote.

## Evidência — baseline Lighthouse

- Desktop performance: 59
- Desktop LCP: 1.4 s; TBT: 820 ms; main thread: 6.9 s
- Mobile performance: 43
- Mobile FCP: 2.3 s; LCP: 4.4 s; TBT: 12,950 ms; TTI: 22.5 s; main thread: 38.4 s
- Mobile third-party blocking: Third-party code blocked the main thread for 4,800 ms

## Evidência — payload por tipo

- Total: 381 requests / 4125.5 KB
- Script: 124 requests / 1717.9 KB
- Other: 208 requests / 1289.9 KB
- Image: 32 requests / 777.1 KB
- Document: 6 requests / 156.4 KB
- Font: 4 requests / 154.2 KB
- Stylesheet: 7 requests / 29.9 KB
- Media: 0 requests / 0.0 KB
- Third-party: 160 requests / 1578.3 KB

## Principais causadores de bloqueio mobile

### Shopify
- Blocking: 2700 ms
- Main thread: 4405 ms
- Transfer: 471.1 KB
- URLs principais:
  - `https://cdn.shopify.com/extensions/019ed4e2-0f90-76a6-96f9-9d7e2dc9a58e/swym-relay-770/assets/swym-ext-shopify.js`
  - `https://cdn.shopify.com/extensions/019ed4e2-0f90-76a6-96f9-9d7e2dc9a58e/swym-relay-770/assets/apps.bundle.js?v=5.0.6`
  - `https://cdn.shopify.com/extensions/019ed4e2-0f90-76a6-96f9-9d7e2dc9a58e/swym-relay-770/assets/atw_nudge.js`
### Facebook
- Blocking: 925 ms
- Main thread: 1072 ms
- Transfer: 228.1 KB
- URLs principais:
  - `https://connect.facebook.net/signals/config/1018779385487104?v=2.9.338&r=stable&domain=lksneakers.com.br&hme=ed806287581422089c496fd48550730`
  - `https://connect.facebook.net/en_US/fbevents.js`
  - `https://www.facebook.com/tr/?id=1018779385487104&ev=PageView&dl=https%3A%2F%2Flksneakers.com.br%2F&rl=&if=false&ts=1781793810981&iw=false&sw`
### Klaviyo
- Blocking: 456 ms
- Main thread: 920 ms
- Transfer: 117.4 KB
- URLs principais:
  - `https://static.klaviyo.com/onsite/js/WnsRcu/klaviyo.js?company_id=WnsRcu`
  - `https://static.klaviyo.com/onsite/js/build-preview/commit-0d1cc388b3e8756318ae46f9aa30aad3aeb88be5/sharedUtils.36a556587a74b8fed5db.js?cb=2`
  - `https://static.klaviyo.com/onsite/js/build-preview/commit-0d1cc388b3e8756318ae46f9aa30aad3aeb88be5/1011.0ab7438f38097e529f79.js`
### Google Tag Manager
- Blocking: 366 ms
- Main thread: 473 ms
- Transfer: 641.1 KB
- URLs principais:
  - `https://www.googletagmanager.com/gtag/js?id=AW-11062830837`
  - `https://www.googletagmanager.com/gtag/js?id=G-HVFGK8SQQT`
  - `https://www.googletagmanager.com/gtag/js?id=G-HVFGK8SQQT&cx=c&gtm=4e66g1`
### Google/Doubleclick Ads
- Blocking: 139 ms
- Main thread: 192 ms
- Transfer: 9.7 KB
- URLs principais:
  - `https://googleads.g.doubleclick.net/pagead/viewthroughconversion/11062830837/?random=1781793811621&cv=11&fst=1781793811621&bg=ffffff&guid=ON`
  - `https://googleads.g.doubleclick.net/pagead/viewthroughconversion/11392887484/?random=1781793819509&cv=11&fst=1781793819509&bg=ffffff&guid=ON`
  - `https://googleads.g.doubleclick.net/pagead/viewthroughconversion/11392887484/?random=1781793810238&cv=11&fst=1781793810238&bg=ffffff&guid=ON`
### JSDelivr CDN
- Blocking: 109 ms
- Main thread: 269 ms
- Transfer: 24.0 KB
- URLs principais:
  - `https://cdn.jsdelivr.net/npm/mk-sdk-git@latest/dist/mk-sdk.js?v=1`
  - `https://cdn.jsdelivr.net/npm/mk-sdk-git@1.1.43/dist/mk-core.js`
### Crisp
- Blocking: 109 ms
- Main thread: 319 ms
- Transfer: 3.2 KB
- URLs principais:
  - `https://client.crisp.chat/l.js`
### Pinterest
- Blocking: 0 ms
- Main thread: 0 ms
- Transfer: 38.6 KB
- URLs principais:
  - `https://s.pinimg.com/ct/lib/main.e5585f3b.js`
  - `https://ct.pinterest.com/static/ct/token_create.js`
  - `https://s.pinimg.com/ct/core.js`

## Top bootup/script cost

- `https://lksneakers.com.br/` — total 10147 ms; scripting 1123 ms; parse/compile 320 ms
- `https://lksneakers.com.br/cdn/wpm/b0638fccbw0def4e15pf2fc89d8m825804c5m.js` — total 9813 ms; scripting 6809 ms; parse/compile 65 ms
- `Unattributable` — total 6427 ms; scripting 290 ms; parse/compile 0 ms
- `https://cdn.shopify.com/extensions/019ed4e2-0f90-76a6-96f9-9d7e2dc9a58e/swym-relay-770/assets/swym-ext-shopify.js` — total 2784 ms; scripting 2073 ms; parse/compile 167 ms
- `https://lksneakers.com.br/cdn/s/trekkie.storefront.370ef8ffef154dc56bb5a814fea4666724353464.min.js` — total 1771 ms; scripting 829 ms; parse/compile 13 ms
- `https://connect.facebook.net/signals/config/1018779385487104?v=2.9.338&r=stable&domain=lksneakers.com.br&hme=ed806287581422089c496fd485507306546b29379` — total 701 ms; scripting 632 ms; parse/compile 68 ms
- `https://cdn.shopify.com/extensions/019ed4e2-0f90-76a6-96f9-9d7e2dc9a58e/swym-relay-770/assets/apps.bundle.js?v=5.0.6` — total 536 ms; scripting 437 ms; parse/compile 88 ms
- `https://www.googletagmanager.com/gtag/js?id=AW-11062830837` — total 473 ms; scripting 398 ms; parse/compile 69 ms
- `https://lksneakers.com.br/cdn/shopifycloud/storefront/assets/storefront/load_feature-1bd60354.js` — total 398 ms; scripting 394 ms; parse/compile 2 ms
- `https://static.klaviyo.com/onsite/js/WnsRcu/klaviyo.js?company_id=WnsRcu` — total 396 ms; scripting 386 ms; parse/compile 3 ms
- `https://connect.facebook.net/en_US/fbevents.js` — total 370 ms; scripting 236 ms; parse/compile 133 ms
- `https://lksneakers.com.br/cdn/shopifycloud/perf-kit/shopify-perf-kit-3.5.2.min.js` — total 364 ms; scripting 323 ms; parse/compile 22 ms

## Interpretação

- O gargalo principal continua sendo mobile: performance 43, LCP 4.4s e TBT 12.950ms.
- O maior bloco de oportunidade não é imagem/CLS; é execução JS e web pixels/app embeds.
- SWYM/Wishlist é o maior causador individual em blocking time dentro do grupo Shopify: `swym-ext-shopify.js` + bundles relacionados.
- Facebook Pixel, Klaviyo e Google Tag Manager também têm custo relevante e exigem cautela porque impactam mensuração, remarketing e CRM.
- Há sinais de duplicidade/carga pesada de gtag/Google Ads/GA4 e Shopify Web Pixels; isso precisa ser auditado antes de qualquer bloqueio/desativação.

## Proposta do Pacote B — sem write ainda

### B1 — Quick win seguro: inventário e deduplicação de tags
- Mapear origem de cada pixel/tag: Shopify Customer Events/Web Pixels, theme liquid, app embed, GTM, apps.
- Identificar duplicidades de GA4/Google Ads/Facebook e preparar remoção/pausa somente onde houver duplicidade comprovada.
- Risco: baixo/médio; pode afetar mensuração se removido errado. Precisa approval packet específico.
### B2 — SWYM/Wishlist: lazy/defer controlado
- Testar em dev/unpublished theme uma estratégia de carregar wishlist após interação/idle ou apenas onde o botão aparece.
- Preservar função de wishlist; não remover app.
- Risco: médio; pode afetar ícone de wishlist/PDP/coleções. Exige preview e QA visual.
### B3 — Klaviyo/Crisp/Attentive: condicionar formulários e chat
- Validar se popups/chat podem carregar após consentimento, delay ou intenção; sem pausar CRM/campanhas.
- Risco: médio/alto porque envolve captação e atendimento.
### B4 — Google Fonts
- Reduzir famílias/pesos carregados ou mover para fonte local/preconnect otimizado.
- Risco: baixo/médio visual; exige QA visual.

## Critério de sucesso sugerido

- Mobile TBT reduzir pelo menos 25% no preview.
- Mobile performance sair de 43 para 55+ no preview, sem quebrar wishlist, add-to-cart, pixel base, Klaviyo e chat.
- Readback com Lighthouse mobile + QA manual em home, coleção e PDP.

## Bloqueio

Qualquer alteração em app embed, web pixel, theme asset ou configuração de tag é write externo e exige aprovação explícita atual de Lucas.

## Rollback planejado

- Antes de qualquer write: snapshot do theme asset/config/app embed afetado.
- Se mexer em pixels/tags: registrar estado anterior e origem exata.
- Rollback por restauração do asset/config anterior e reexecução de Lighthouse/QA.

## Próxima decisão

Recomendação: aprovar somente a fase B1 read-only aprofundada + preview B2 em dev/unpublished theme. Não aprovar remoção/desativação de pixel/app ainda.