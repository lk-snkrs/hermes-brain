# Ahrefs schema global — production patch receipt

Data UTC: `2026-06-18T23:04:26Z`
Escopo aprovado: `Aprovo schema production`
values_printed=false

## Theme / asset

- Theme: `lk-new-theme/production`
- Theme ID: `155065417950`
- Role: `main`
- Asset: `sections/lk-header.liquid`

## Mudança aplicada

No schema global `Organization/ShoeStore/ClothingStore`:

- removido `hasMerchantReturnPolicy`
- removido `shippingDetails`

Mantido:

- `aggregateRating`
- `address`
- `geo`
- `telephone`
- `openingHoursSpecification`
- `sameAs`
- `priceRange`, `paymentAccepted`, `currenciesAccepted`

## Readback Shopify Admin

- PUT status: `200`
- readback equals target: `true`
- `hasMerchantReturnPolicy` no asset readback: `false`
- `shippingDetails` no asset readback: `false`
- `aggregateRating` no asset readback: `true`

## Validação pública

5 URLs testadas:

- `/pages/contato`: já limpo
- `/pages/new-balance-9060-guia`: já limpo
- `/`: ainda pode servir cache antigo
- `/collections/roupas`: alterna entre cache antigo e novo
- `/products/air-jordan-4-craft-medium-olive`: ainda pode servir cache antigo

Probe repetido em `/collections/roupas` com cachebusters:

- Algumas respostas com `hasMerchantReturnPolicy/shippingDetails=false`
- Algumas respostas com `hasMerchantReturnPolicy/shippingDetails=true`

Interpretação: patch aplicado corretamente no asset production, mas CDN/edge/cache ainda alterna entre HTML antigo e novo.

## Rollback

Restaurar `lk-header-production-before.liquid` no mesmo asset.

## Follow-up

Revalidar público/Ahrefs em 12–24h antes de qualquer novo patch de schema. Se Ahrefs continuar acusando depois do recrawl/cache, próxima hipótese é testar remoção de `aggregateRating` do schema global.
