# Approval packet — PDP mobile Trust Bar com altura igual ao card Sujeito a encomenda

Data: 2026-06-26
Owner: LK Shopify
Superfície: Shopify theme / `sections/lk-pdp.liquid`
Escopo: PDP mobile, Trust Bar logo abaixo do CTA/Compre Já

## Pedido do Lucas

> “Corrigir, no móbile, a altura da trust bar, deve ser igual do sujeito a encomenda”

Screenshot mostra a Trust Bar mobile — Google avaliações, autenticidade, parcelamento, frete — mais baixa que o card logo abaixo “Sujeito a encomenda · 4-6 semanas”.

## Evidência read-only

Fonte Production lida do GitHub `production`:

`/opt/data/profiles/lk-shopify/workdirs/pdp-mobile-trustbar-height-20260626/prod_sections__lk-pdp.liquid`

CSS atual encontrado:

- Trust Bar mobile `.lk-trust-grid`:
  - `height: 42px;`
  - `min-height: 42px;`
- Card encomenda `.pi-preorder-card`:
  - `min-height: 52px;`
  - `padding: 14px 16px;`

## Interpretação

A Trust Bar foi compactada anteriormente para 42px. No mobile do print, ela está visualmente menor que o aviso de encomenda. Para igualar a altura base, a Trust Bar mobile deve voltar para **52px**, que é a altura mínima do card “Sujeito a encomenda”.

## Patch local proposto

Arquivo único: `sections/lk-pdp.liquid`

Mudança CSS-only:

```diff
.l k-trust-grid mobile
- height: 42px;
- min-height: 42px;
+ height: 52px;
+ min-height: 52px;

.l k-tg__item mobile
- padding: 5px 3px 4px;
+ padding: 6px 3px 5px;
```

Obs.: o diff real não tem espaço em `.lk`; espaço acima evita auto-link/markdown estranho.

## Fora de escopo

- Não muda review count/metafield/cron Google Reviews.
- Não muda texto, ícones ou ordem da Trust Bar.
- Não muda card de encomenda.
- Não muda produto, preço, estoque, checkout, cart drawer, GA4 ou cross-sell.

## QA planejado

Depois de aprovação:

1. Upload em DEV/unpublished theme apenas de `sections/lk-pdp.liquid`.
2. Readback DEV por SHA/substrings:
   - `height: 52px;`
   - `min-height: 52px;`
   - `.pi-preorder-card` preservado.
3. QA mobile PDP com produto encomenda:
   - Trust Bar e “Sujeito a encomenda” com mesma altura base visual;
   - ícones/textos centralizados;
   - CTA e Compre Já preservados;
   - desktop sem alteração material.
4. Se aprovado Production no mesmo escopo: PR para `production`, merge, Shopify Production readback e QA público.

## Risco

Baixo. CSS-only no breakpoint mobile da Trust Bar do PDP. Risco: a Trust Bar ocupa +10px vertical no mobile. É exatamente o pedido para igualar ao card de encomenda.

## Rollback

Plano B apenas se precisar — não é recomendação de reverter.

Restaurar `sections/lk-pdp.liquid` a partir do snapshot:

`/opt/data/profiles/lk-shopify/workdirs/pdp-mobile-trustbar-height-20260626/prod_sections__lk-pdp.liquid`

## Aprovação necessária

Para aplicar em DEV e fazer merge Production no escopo acima:

**Aprovo DEV e merge Production PDP mobile Trust Bar 52px igual encomenda**

Reminder OS loop needed: yes
Reminder OS owner: LK Shopify
Reminder OS next action: aguardar aprovação explícita; aplicar DEV, QA/readback e Production se aprovado.
Reminder OS review trigger: resposta do Lucas aprovando execução ou pedindo outro ajuste visual.
Reminder OS evidence: este approval packet + workdir local com snapshot/target.
