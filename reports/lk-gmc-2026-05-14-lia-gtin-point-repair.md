# LK GMC Local/LIA GTIN point repair — 2026-05-14

Gerado em: `2026-05-14T18:35:18.184730+00:00`
Delayed reverify: `2026-05-14T18:36:52.613867+00:00`

## Resultado
- Status: `completed_verified`
- Reparos: `4`
- Execução: `{'patched': 4}`
- Readback inicial: `{'match': 2, 'mismatch': 2}`
- Readback delayed: `{'match': 4}`
- Productstatuses finais com issue GTIN alvo nos 34: `0`; `{}`

## Observação
- Dois reparos demoraram a aparecer no `products.get` inicial, mas bateram no delayed reverify.
- Os 34 IDs `local:LIA_*` ficaram sem `reserved_gtin`/`restricted_gtin` no recheck final.

## Não executado
- Shopify write
- Tiny write
- POS/local inventory config
- price/title/category/image/availability update
- feed upload/fetch
- campaign/message/send
