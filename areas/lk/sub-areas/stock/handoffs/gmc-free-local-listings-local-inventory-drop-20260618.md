# Handoff para LK Stock — GMC Free Local Listings queda local

Data UTC: 2026-06-18T22:19:25Z
Origem: LK Growth / Telegram Lucas

## Contexto mínimo

- Merchant Center account: LK Sneakers Apparels `5297679409`.
- E-mail Google: queda Free local listings BR de 2.088 para 1.632 entre 2026-06-17 22:10 BRT e 2026-06-18 04:10 BRT.
- Read-only Merchant API em 2026-06-18T22:15Z:
  - total local offers: 11.537.
  - Free Local Listings BR approved: 475.
  - Free Local Listings BR disapproved: 11.062.
  - Local Inventory Ads BR approved: 1.
  - Local Inventory Ads BR disapproved: 11.536.
  - `local_stores_lack_inventory`: 11.062 em FREE_LOCAL_LISTINGS e 11.062 em LOCAL_INVENTORY_ADS.
  - `mhlsf_full_missing_valid_link_template`: 11.247 em LOCAL_INVENTORY_ADS.
  - `googleExpirationDate`: 0 expirando nos próximos 3 dias; 0 expirados.

## Pedido ao LK Stock

Validar se há falha operacional/sistêmica no envio de inventário local para Merchant/Simprosys/loja física, sem Growth consultar Tiny/Shopify estoque direto.

Responder com evidência suficiente para classificar:

1. Falha real de inventário local ausente para store/local feed?
2. Queda por sincronização/latência Simprosys?
3. Ruptura/ausência real por variantes/grade?
4. Necessidade de reconciliação SKU/Variant/Store code?

## Observação Growth

Growth não deve prometer disponibilidade nem consultar estoque direto. Qualquer ação em GMC/feed/Simprosys exige approval do Lucas e rollback.
