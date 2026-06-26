# LK GMC — A42/B20 recheck + Content API fallback preview

Gerado em: `2026-05-15T21:29:11.554025+00:00`
Status: `fallback_preview_ready_no_write`

## Recheck
- A Content API match: `1/42`
- A Merchant API v1 match: `1/42`
- B ausente products.list: `20/20`
- B ausente productstatuses.list: `20/20`

## Fallback preparado
- Candidatos Content API price-only: `41`
- Decisões: `{'candidate_content_api_upsert_price_only': 41, 'no_action_already_matches': 1}`
- Escopo planejado: `products.insert`/upsert Content API para recursos `source=api`, preservando recurso completo e alterando apenas `price`.
- Excluído: `salePrice`, strikethrough, Shopify, Tiny, feed, campanha.

## Aprovação necessária

Para executar o fallback, usar frase explícita:

`aprovo GMC fallback Content API price-only 42`

Sem isso, não executar write adicional.

## Artefatos
- JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-15-a42-b20-recheck-content-fallback-preview.json`
- CSV: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-15-a42-b20-recheck-content-fallback-preview-fallback-price-only.csv`

## Não executado
- Content API upsert
- Merchant ProductInputs PATCH
- Shopify write
- Tiny write
- feed fetch/upload
- salePrice/strikethrough update
- campaign/message/contact
