# Approval packet — configurar captura GA4/GTM dos eventos cart drawer cross-sell v3

- **Data:** 2026-06-25
- **Perfil:** lk-shopify
- **Superfície:** Analytics / GA4-GTM / LK Sneakers storefront
- **Status:** preparado; **nenhum write externo de analytics executado**.

## Contexto

O cart drawer cross-sell v3 curated-light + tracking está em Production via PR #102. O tema já emite eventos sem PII para `window.dataLayer` e `CustomEvent`:

- `lk_cart_cross_sell_view`
- `lk_cart_cross_sell_click`
- `lk_cart_cross_sell_add`

## Evidência read-only

Detecção pública:

- HTML público contém `dataLayer`.
- GA4 ID detectado: `G-HVFGK8SQQT`.
- GTM `GTM-...` não foi detectado por string estática.
- HTML público contém v3 e os três eventos de tracking.
- `/collections/all/products.json` ausente.

Arquivo local:

- `/opt/data/profiles/lk-shopify/workdirs/cart-drawer-cross-sell-xy-20260625/gtm_ga4_public_detection_v3_tracking.json`

Spec:

- `areas/lk/sub-areas/shopify/reports/2026-06-25-cart-drawer-cross-sell-v3-ga4-capture-spec.md`

## Bloqueio atual

Revalidação runtime automatizada do `dataLayer` continua bloqueada por Shopify HTTP 429 no `/cart/add.js` na sessão CDP.

Última tentativa leve:

- PDP HTML: 200, v3/tracking presentes, sem `/collections/all`.
- `/cart.js`: 200 JSON.
- `/cart/add.js` via CDP: 429, então o bloco não renderizou na sessão automatizada e eventos runtime não puderam ser confirmados.

Reminder OS existente:

- `rem-lk-shopify-cart-drawer-v3-tracking-runtime-qa-20260625`

## Escopo proposto com aprovação

Configurar captura dos eventos no analytics disponível, priorizando caminho com menor risco:

1. descobrir via integração/config read-only qual é o caminho real: GA4 direto, Google tag, Shopify pixel/app ou GTM não detectado no HTML;
2. criar eventos customizados/reportáveis:
   - `lk_cart_cross_sell_view`
   - `lk_cart_cross_sell_click`
   - `lk_cart_cross_sell_add`
3. registrar dimensões/parâmetros úteis:
   - `surface`
   - `map_version`
   - `strategy`
   - `recommended_handle`
   - `position`
   - `score_bucket`
   - `status`
   - `rendered_count`
4. se possível, marcar como conversão/microconversão apenas `lk_cart_cross_sell_add` com `status=success`.

## Não incluído

- Shopify theme change;
- produto/preço/estoque/checkout;
- GMC/ads/Klaviyo/WhatsApp/e-mail;
- criação de campanhas;
- envio de PII;
- alteração de consentimento/pixels além da captura dos três eventos.

## Risco

Médio-baixo, mas é write externo de analytics/configuração. Precisa approval explícito.

Riscos específicos:

- duplicação de evento se integração atual já captura dataLayer automaticamente;
- GA4 custom dimensions podem demorar para aparecer em relatórios;
- se não houver GTM, pode ser necessário configurar no GA4/Google tag/Shopify channel conforme ferramenta disponível.

## Rollback

- remover/desativar os três eventos customizados/tags/triggers criados;
- não exige revert de tema se a captura for somente GA4/GTM/config;
- se houver qualquer alteração de tema/pixel adicional, criar rollback separado antes.

## Aprovação necessária

`Aprovo configurar captura GA4/GTM dos eventos cart drawer cross-sell v3`

`values_printed=false`.
