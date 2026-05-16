# LK PDP mobile decision-area CRO — size/CTA/WhatsApp/encomenda (2026-05-15)

Use this reference when Lucas asks for PDP mobile conversion refinements around the final buying decision area.

## Validated scope from session

Target file/theme: `sections/lk-pdp.liquid` in repo `lk-new-theme`, dev theme `lk-new-theme/dev` (`155065450718`).

Validated preview URL pattern:

```text
https://lksneakers.com.br/products/<handle>?preview_theme_id=155065450718
```

For Samba Jane the working preview was:

```text
https://lksneakers.com.br/products/tenis-adidas-samba-jane-black-white-gum-preto?preview_theme_id=155065450718
```

## CRO rules learned

1. **Decision hierarchy on mobile:** keep the PDP buying path tight: price/installment → size → primary CTA → trust/try-on → fulfillment caveat → details. Do not let secondary actions compete with the primary CTA.
2. **Selected size needs strong visual state:** selected size should be visibly black/filled and also reflected in the label (`Tamanho: <badge>`), not only a subtle border.
3. **Unavailable sizes need explicit clarity:** use a muted tile/background, strike-through, and small `Esgotado` label. Do not rely on a faint diagonal line only.
4. **Dynamic checkout / `COMPRE JÁ` competes on mobile:** hide `.pi-actions .shopify-payment-button` at the mobile breakpoint unless Lucas explicitly asks to keep it. Keep `ADICIONAR AO CARRINHO` as the only primary decision CTA in the mobile buying block.
5. **Reduce CTA-adjacent noise:** reduce vertical padding around price/size/actions so the CTA stays visually close to price and size.
6. **Encomenda notice order correction:** `Sujeito a encomenda · 4-6 semanas · Confirme no WhatsApp` should appear **above** `Detalhes do produto`, not below the expanded description. Lucas explicitly pointed to this in screenshot review.
7. **Floating WhatsApp must never cover ATC:** on PDP mobile, move floating WhatsApp/chat widgets above the sticky ATC. If the widget comes from an app/snippet that is rendered outside the PDP file or not present locally, add a scoped PDP detector that classifies fixed/sticky WhatsApp-like anchors and applies a bottom offset class only on mobile. Do not globally alter footer/social WhatsApp links.

## Implementation pattern

In `sections/lk-pdp.liquid`:

- Tighten spacing:
  - `.pi-price-block` bottom padding around `14px`.
  - `.pi-section` around `12–14px` vertical padding.
  - `.pi-actions` around `10–12px` top and `8–10px` bottom.
- Add `.pi-section__label strong` badge style for selected size.
- Add `.pi-size__unavailable` markup inside disabled/unavailable size buttons.
- Add mobile CSS:

```css
@media (max-width: 749px) {
  .pi-actions .shopify-payment-button { display: none !important; }
  .lk-pdp-wa-offset { bottom: calc(92px + env(safe-area-inset-bottom, 0px)) !important; }
}
```

- Move the `{% comment %} Encomenda notice {% endcomment %}` block so it sits before the `{% comment %} Description accordion {% endcomment %}` block.
- If needed, add a scoped detector inside the PDP script:

```js
function offsetPdpFloatingWhatsApp() {
  if (window.innerWidth > 749) return;
  var candidates = Array.prototype.slice.call(document.querySelectorAll('a[href*="wa.me"], a[href*="whatsapp"], [class*="whatsapp" i], [id*="whatsapp" i], [class*="wa-" i], [id*="wa-" i]'));
  candidates.forEach(function(el) {
    if (!el || el.closest('.pdp-info') || el.closest('.ft') || el.classList.contains('lk-pdp-wa-offset')) return;
    var style = window.getComputedStyle(el);
    var rect = el.getBoundingClientRect();
    var isFloating = (style.position === 'fixed' || style.position === 'sticky') && rect.width > 24 && rect.height > 24 && rect.bottom > (window.innerHeight - 140);
    if (isFloating) el.classList.add('lk-pdp-wa-offset');
  });
}
offsetPdpFloatingWhatsApp();
window.addEventListener('load', offsetPdpFloatingWhatsApp);
setTimeout(offsetPdpFloatingWhatsApp, 1200);
setTimeout(offsetPdpFloatingWhatsApp, 3000);
```

## Upload/verification details

- Before dev theme upload, verify exact theme name/role: `lk-new-theme/dev` + `unpublished`.
- Snapshot the remote asset under `backups/theme-dev/<timestamp>/` before uploading.
- Asset API readback may show a hash mismatch immediately in the same script even when the second read matches; rerun a focused readback and verify distinctive strings plus final SHA before treating upload as failed.
- Browser navigation to the preview can time out while the page still loads; use snapshot/readback to verify DOM order if visual tooling cannot land at the exact scroll position.
- Verify in snapshot/DOM order that `Encomenda notice` / `Sujeito a encomenda` appears before `Description accordion` / `Detalhes do produto`.

## Non-actions

This preview flow does not authorize production upload, product/price/stock edits, Shopify app changes, WhatsApp sends, campaigns, or publishing a theme. Production promotion still needs explicit Lucas approval and the production backup/readback workflow.