# LK GMC — A42/B20 recheck + Content API fallback preview

Gerado em: `2026-05-15T21:29:11.554025+00:00`
Status: `fallback_preview_ready_no_write`

## Recheck
- A Content API match: `1/42`
- A Merchant API v1 match: `1/42`
- A match propagado: `online:pt:BR:IG5932-4` (`1799.99 BRL`, sem salePrice).
- A ainda divergente do `target_shopify_price_brl`: `41/42`.
- B ausente products.list: `20/20`
- B ausente productstatuses.list: `20/20`

## Conclusão
- O PATCH ProductInputs do pacote A foi aceito na execução aprovada (`42/42 patched_price_only_v1` no relatório `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-15-approved-packets-a42-b20.json`), mas a propagação permanece majoritariamente pendente: só `1/42` bate agora no Content API e Merchant API v1.
- O pacote B permanece OK: os 20 IDs seguem ausentes em `products.list` e `productstatuses.list`.
- Nenhum write adicional foi executado neste recheck.

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

## Resumo Telegram
LK GMC recheck A42/B20 pós-execução: A propagou só 1/42 (Content API 1/42, Merchant API v1 1/42; match IG5932-4). Os outros 41 ainda não batem o preço Shopify alvo. B continua OK: 20/20 ausentes em products.list e 20/20 ausentes em productstatuses.list. Não executei nenhum write novo. Se quiser continuar, próximo passo requer aprovação explícita para fallback Content API source=api price-only nos 41 pendentes.

## Não executado
- Content API upsert
- Merchant ProductInputs PATCH
- Shopify write
- Tiny write
- feed fetch/upload
- salePrice/strikethrough update
- campaign/message/contact
