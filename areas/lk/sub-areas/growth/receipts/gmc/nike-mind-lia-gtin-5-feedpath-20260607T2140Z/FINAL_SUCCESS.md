# FINAL SUCCESS — Nike Mind LIA GTIN 5

Data: 2026-06-07T21:44:17.132609+00:00

## Resultado

- Escopo: 5 itens Local/LIA Nike Mind no Google Merchant.
- Critério: GTIN vindo do item online irmão com mesmo `offerId` normalizado e mesmo `variant_id` Shopify.
- GMC alterado: `true`
- Shopify alterado: `false`
- Confirmados por readback: `5/5`
- Restantes sem GTIN: `0`

## Readback

- `local:pt:BR:LIA_HQ4307-600-3` → GTIN `198727220471` | OK `true` | issues: `mhlsf_full_missing_valid_link_template`
- `local:pt:BR:LIA_HQ4307-600-4` → GTIN `198727220471` | OK `true` | issues: `mhlsf_full_missing_valid_link_template`
- `local:pt:BR:LIA_HQ4307-003-7` → GTIN `0198958709615` | OK `true` | issues: `mhlsf_full_missing_valid_link_template`
- `local:pt:BR:LIA_HQ4307-002-5` → GTIN `0198958707406` | OK `true` | issues: `mhlsf_full_missing_valid_link_template`
- `local:pt:BR:LIA_HQ4307-003-5` → GTIN `0198958709264` | OK `true` | issues: `mhlsf_full_missing_valid_link_template`

## Observação importante

Os 5 itens ainda aparecem com issue de veiculação local:

- `mhlsf_full_missing_valid_link_template`
- atributo: `link template`
- detalhe: `A valid [link_template] value with store code is required for the offer to serve`

Ou seja: o problema de GTIN foi corrigido nesses 5, mas ainda existe um gargalo separado de `link_template` para servir Local/LIA.

## Rollback

Arquivo: `ROLLBACK_PLAN.md`
Snapshot original: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/nike-mind-lia-gtin-5-20260607T2133Z/before_snapshots.json`

## Arquivos de evidência

- `final_gtin_readback_with_status.json`
- `products_insert_customattr_gtin_results.json`
- `FINAL_SUCCESS.json`
- `ROLLBACK_PLAN.md`
