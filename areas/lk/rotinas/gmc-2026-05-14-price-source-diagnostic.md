# LK GMC price source diagnostic — 2026-05-14

Generated: `2026-05-15T20:18:11.325693+00:00`

Input products: `152`

## Diagnosis counts
- merchant_stale_vs_shopify_and_public: `108`
- merchant_matches_shopify_admin: `44`

## Interpretação
- `merchant_stale_vs_shopify_and_public`: Merchant/Content não acompanha Shopify Admin nem `/products/{handle}.js`; provável fonte/sobrescrita/cache do Merchant, não erro de preço Shopify.
- `merchant_matches_shopify_admin`: sem ação de preço necessária no readback atual.
- `shopify_admin_public_diverge`: precisa investigar Markets/publicação antes de escrever preço.

## Não executado
- Merchant write
- Content API write
- Shopify write
- Tiny write
- feed fetch/upload
- campaign/message/send
