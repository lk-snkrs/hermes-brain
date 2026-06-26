# Approval packet — Cart Drawer small viewport footer overlap fix

- **Data:** 2026-06-25
- **Perfil:** lk-shopify
- **Superfície:** Shopify theme — cart drawer / minicart
- **Pedido do Lucas:** em device pequeno, o botão/rodapé `FINALIZAR COMPRA` sobrepõe/esconde os produtos no cart drawer.
- **Screenshot:** `/opt/data/profiles/lk-shopify/image_cache/img_f6026d0a9ecd.jpg`
- **Status:** patch local preparado; nenhum write Shopify/GitHub executado ainda.

## Evidência

Production source atual lido via GitHub `production`:

- arquivo: `snippets/lk-cart-drawer.liquid`
- snapshot local: `/opt/data/profiles/lk-shopify/workdirs/cart-drawer-footer-overlap-20260625/prod_snippets__lk-cart-drawer.liquid`
- sha256 antes: `7e1e11ffdcf107757beb5d6877de117fb9a68a6e9fa639917673e10bbfd0315c`

Trecho relevante atual:

- `.cart-drawer` usa `height: 100vh; height: 100dvh` e `display:flex`.
- `#cart-drawer-body` usa `overflow:hidden`.
- `.cart-drawer__items` é o único scroll interno.
- `.cart-drawer__footer` tem `flex-shrink:0` e altura visual grande: total, parcela, botão, 4 trust cells, WhatsApp e link de carrinho.

## Interpretação

O fix anterior moveu o upsell para dentro da lista scrollável, mas ainda deixou um caso limite:

- em viewport baixo, o footer não encolhe;
- `#cart-drawer-body` corta overflow;
- a área de produto pode ficar pequena demais;
- visualmente o footer/CTA parece cobrir ou esmagar o produto.

A solução correta não é esconder CTA nem remover confiança; é mudar o comportamento **só em altura pequena**: o corpo inteiro passa a rolar como um fluxo único, então produto → upsell → footer ficam todos acessíveis sem sobreposição.

## Patch proposto

Arquivo alvo:

- `snippets/lk-cart-drawer.liquid`

Target local:

- `/opt/data/profiles/lk-shopify/workdirs/cart-drawer-footer-overlap-20260625/target_snippets__lk-cart-drawer.liquid`
- sha256 depois: `534abbd69dc068e78d13deeb15bf8afedaeaaf77a248cdc75bccfcbf73ce424b`

CSS adicionado antes do media mobile existente:

```css
/* Small viewport safety: when the footer would consume the drawer height, let the body scroll as one flow so checkout never covers products. */
@media (max-height: 720px) {
  #cart-drawer-body {
    overflow-y: auto;
    -webkit-overflow-scrolling: touch;
    overscroll-behavior: contain;
  }
  .cart-drawer__items {
    flex: 0 0 auto;
    min-height: auto;
    overflow: visible;
  }
  .cart-drawer__item {
    grid-template-columns: 72px 1fr;
    gap: 12px;
    padding: 12px 24px;
  }
  .cart-drawer__item-img,
  .cart-drawer__item-img img {
    width: 72px;
    height: 72px;
  }
  .cart-drawer__footer {
    flex: 0 0 auto;
    padding: 14px 24px 16px;
  }
  .cart-drawer__total-price { font-size: 21px; }
  .cart-drawer__installment { margin-bottom: 12px; }
  .cart-drawer__checkout-btn { padding: 13px; }
  .cart-drawer__reassurance {
    gap: 5px;
    margin: 12px 0 4px;
  }
  .cart-drawer__reassurance-item {
    min-height: 38px;
    padding: 7px 6px;
  }
}
```

## Static QA local

Arquivo: `/opt/data/profiles/lk-shopify/workdirs/cart-drawer-footer-overlap-20260625/static_qa.json`

- `@media (max-height: 720px)`: 1
- `#cart-drawer-body` com `overflow-y:auto` nesse breakpoint: yes
- `.cart-drawer__items` com `overflow:visible` nesse breakpoint: yes
- imagens de item compactadas para `72px`: yes
- footer compactado apenas no breakpoint de altura pequena: yes

## QA planejado após aprovação

1. Upload em DEV/unpublished `lk-new-theme/dev`.
2. Readback Admin por SHA.
3. Browser/mobile em viewport baixo, por exemplo 390×640 e 390×600:
   - adicionar produto ao carrinho;
   - abrir drawer pelo fluxo real;
   - confirmar produto visível sem ser coberto pelo botão;
   - confirmar que o corpo rola e footer aparece depois;
   - confirmar CTA `FINALIZAR COMPRA` clicável;
   - confirmar que em viewport normal o comportamento atual continua.
4. Se DEV passar e Lucas já tiver aprovado Production junto, abrir PR GitHub para `production`, merge, Shopify readback e public QA.

## Risco

Baixo/médio. É CSS de layout do cart drawer, mas afeta checkout CTA visual em viewport baixo.

Mitigação:

- breakpoint por altura (`max-height:720px`) limita impacto;
- mantém CTA e trust cells, só compacta e muda scroll;
- não altera produtos, preço, estoque, checkout, metafields, cron, ads ou Klaviyo.

## Rollback

- Reverter o hunk CSS adicionado no `snippets/lk-cart-drawer.liquid`.
- Em Production: revert do PR/commit correspondente.
- Readback Shopify confirmando ausência de `@media (max-height: 720px)`.

## Próxima decisão

Para aplicar em DEV e, se QA passar, promover via PR/merge Production:

`Aprovo DEV e merge Production cart drawer small viewport footer overlap fix`
