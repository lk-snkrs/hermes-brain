# FINAL STATUS — GMC Nike Mind LIA GTIN attempt

Data: 2026-06-07T21:38:28.678213+00:00

## Resultado final

- Updates tentados: `5`
- Updates confirmados por readback: `0`
- Shopify alterado: `false`
- GMC write tentado: `true`
- GMC write confirmado: `false`

## Bloqueio

A Content API `products.update` não confirmou aplicação para produtos Local/LIA:

1. rejeitou campos imutáveis no body (`offerId`, depois `targetCountry`);
2. com body sanitizado, retornou `500/timeout`;
3. readback posterior confirmou que os 5 itens continuam sem GTIN.

## Conclusão

Nenhum GTIN foi aplicado. O caminho correto para esses 5 itens é via mecanismo de fonte/feed local/supplemental do Merchant, não update direto do produto local via Content API neste formato.

## Próxima ação recomendada

Preparar supplemental/feed update para os 5 `offerId` Local/LIA:

- `LIA_HQ4307-600-3` → `198727220471`
- `LIA_HQ4307-600-4` → `198727220471`
- `LIA_HQ4307-003-7` → `0198958709615`
- `LIA_HQ4307-002-5` → `0198958707406`
- `LIA_HQ4307-003-5` → `0198958709264`
