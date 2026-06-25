# Approval packet — cart drawer cross-sell v3 curated-light + tracking

- **Data:** 2026-06-25
- **Perfil:** lk-shopify
- **Superfície:** Shopify theme — `snippets/lk-cart-drawer.liquid`
- **Status:** preparado; **nenhum write executado** para v3/tracking.

## Escopo proposto

1. Trocar o mapa ativo v2 public-filtered pelo mapa **v3 curated-light**.
2. Adicionar tracking sem PII para:
   - `lk_cart_cross_sell_view`;
   - `lk_cart_cross_sell_click`;
   - `lk_cart_cross_sell_add`.
3. Enviar eventos para `window.dataLayer` e `CustomEvent`, sem dependência de vendor.

## Evidência

Relatório:

- `areas/lk/sub-areas/shopify/reports/2026-06-25-cart-drawer-cross-sell-v3-quality-tracking.md`

Artefatos locais:

- v3 map: `/opt/data/profiles/lk-shopify/workdirs/cart-drawer-cross-sell-xy-20260625/cart_drawer_cross_sell_candidate_map_v3_curated_light.json`
- review: `/opt/data/profiles/lk-shopify/workdirs/cart-drawer-cross-sell-xy-20260625/cross_sell_v2_rules_quality_review.json`

## Diferença v2 → v3

| Versão | Handles | Regras |
|---|---:|---:|
| v2 public-filtered atual | 26 | 46 |
| v3 curated-light proposto | 22 | 37 |

## Não incluído

- Produto/preço/estoque;
- checkout config;
- metafields;
- GMC, ads, Klaviyo, WhatsApp, e-mail;
- qualquer query de estoque/Tiny;
- alteração de layout fora do cart drawer upsell.

## QA planejado

1. DEV readback SHA do snippet.
2. `node --check` no JS extraído.
3. Verificar `/collections/all/products.json` count `0`.
4. Fluxo público com sessão temporária:
   - add X com regra forte;
   - drawer abre;
   - v3 renderiza Y esperado;
   - produto X excluído;
   - checkout visível;
   - carrinho limpo ao final.
5. Verificar `dataLayer` recebeu view/click/add em sessão local/CDP.
6. GitHub PR narrow + Production readback Shopify.

## Rollback

Reverter o PR v3/tracking para voltar ao PR #101 / v2 public-filtered.

## Aprovação necessária

`Aprovo DEV e merge Production cart drawer cross-sell v3 curated-light + tracking`
