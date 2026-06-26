# Ahrefs schema global — dev patch receipt

Data UTC: `2026-06-18T23:01:57Z`
Escopo aprovado: patch somente em dev theme. Production writes = 0.
values_printed=false

## Theme / asset

- Theme: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Role: `unpublished`
- Asset: `sections/lk-header.liquid`

## Mudança aplicada

No schema global `Organization/ShoeStore/ClothingStore`:

- removido `hasMerchantReturnPolicy`
- removido `shippingDetails`

Mantido:

- `Organization/ShoeStore/ClothingStore`
- `address`
- `geo`
- `telephone`
- `openingHoursSpecification`
- `sameAs`
- `aggregateRating` por enquanto

## Readback autenticado Shopify

Após retry do PUT:

- PUT: `200`
- readback equals target: `true`
- `hasMerchantReturnPolicy` no target/readback: `false`
- `shippingDetails` no target/readback: `false`

## Preview público

Tentativas com `preview_theme_id=155065450718` ainda retornaram HTML com `hasMerchantReturnPolicy` e `shippingDetails`.

Interpretação: preview público não é confiável neste ambiente/cache para validar dev theme, como já ocorreu em outros assets. Não usei esse preview como critério de sucesso.

## Arquivos

- Backup: `lk-header-dev-before.liquid`
- Target: `lk-header-dev-after.proposed.liquid`
- Receipt JSON: `receipt.json`

## Rollback

Restaurar `lk-header-dev-before.liquid` no asset `sections/lk-header.liquid` do theme `155065450718`.

## Próximo passo recomendado

Rodar validação em dev por método autenticado/preview confiável ou, se Lucas aprovar, aplicar micro-patch em production com rollback imediato e validar HTML público/cachebuster em 5 URLs.
