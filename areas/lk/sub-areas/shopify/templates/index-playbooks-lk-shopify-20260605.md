# Index — Playbooks práticos LK Shopify

Data: 2026-06-05
Status: templates locais/Brain; sem runtime, cron, write Shopify, Tiny ou produção.
Dono: LK Shopify.

Use estes playbooks junto do template base `preview-aprovacao-shopify.md`.

## Playbooks

1. `playbook-correcao-tema-lk-shopify-20260605.md`
   - Para bug de layout, CSS, Liquid, snippet, section, PDP, collection, cart, search, header/footer.
2. `playbook-feature-cart-drawer-minicart-20260605.md`
   - Para cart drawer, minicart, quick add, sticky add-to-cart, upsell, barra de frete e features de compra.
3. `playbook-preco-promo-aprovado-20260605.md`
   - Para mudanças de price/compare-at price já decididas/aprovadas por Lucas/LK Ops.
4. `playbook-cro-pdp-surface-20260605.md`
   - Para hipóteses CRO em PDP/cart/collection/page cuja execução seja superfície Shopify.
5. `playbook-qa-readback-pos-write-20260605.md`
   - Para verificar execução aprovada, comparar approval packet vs fonte viva e emitir receipt.

## Regra de uso

- Primeiro classificar a demanda e selecionar o playbook.
- Sempre preencher `preview-aprovacao-shopify.md` antes de pedir aprovação para write.
- LKGOC/guia/experiência editorial de coleção sai daqui e vai para `[LK] Otimização de Coleções`.
- Tiny continua verdade de estoque; Shopify é superfície/evento.
- Produção, preço, estoque, app, webhook, feed, campanha e contato externo exigem aprovação escopada.
