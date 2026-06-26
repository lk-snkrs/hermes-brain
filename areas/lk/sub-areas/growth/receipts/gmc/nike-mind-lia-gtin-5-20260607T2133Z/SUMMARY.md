# GMC write receipt — Nike Mind LIA GTIN 5 itens

Data: 2026-06-07T21:33:46.509874+00:00
Escopo: aplicar GTIN em 5 produtos Local/LIA no Google Merchant, quando o item online irmão tinha o mesmo `offerId` normalizado e mesmo `variant_id` Shopify.

## Resultado

- Tentados: `5`
- Sucesso/readback OK: `0`
- Falhas: `5`
- Shopify alterado: `false`
- GMC alterado: `true`

## Arquivos

- `before_snapshots.json`
- `update_results.json`
- `rollback_plan.json`
- `summary.json`

## Rollback

Restaurar recursos originais de `before_snapshots.json` via `products.update`.


## Post-attempt readback

- Readback OK: `0`
- Still missing: `5`
- Conclusion: No successful GMC GTIN application confirmed
