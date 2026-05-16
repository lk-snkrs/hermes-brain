# LK GMC Google & YouTube channel read-only diagnostic — 2026-05-14

Generated: `2026-05-14T21:58:50.630693+00:00`

Status: `approved_read_only_diagnostic_complete`

## Escopo
- Diagnóstico read-only do canal Shopify `Google & YouTube` e da fonte Merchant API principal.
- Nenhum write, resync, fetchNow, settings change ou alteração Shopify/Merchant.

## Achados
- Publicações Shopify encontradas: `['Online Store', 'Facebook & Instagram', 'Google & YouTube', 'Point of Sale', 'Linktree', 'Pinterest', 'TikTok', 'Attentive']`
- Google & YouTube publication ID suffix: `79416787166`
- Amostra: `6` SKUs; encontrados no Shopify `6`; publicados no Google & YouTube `6`.
- Stale price vs Shopify na amostra: `5`.

## Amostra
- `01424-002-2`: Shopify price `8999.99`, compare-at `None`, Google & YouTube published `True`, Merchant price `5999.90`, issues `['price_updated', 'price_updated', 'price_updated']`.
- `553558140-7`: Shopify price `1799.99`, compare-at `1599.99`, Google & YouTube published `True`, Merchant price `1499.99`, issues `['price_updated', 'price_updated', 'price_updated']`.
- `AQ9129-170-5`: Shopify price `2749.99`, compare-at `2449.90`, Google & YouTube published `True`, Merchant price `2599.99`, issues `['price_updated', 'price_updated', 'price_updated']`.
- `AQ9129-170-7`: Shopify price `3349.99`, compare-at `2449.90`, Google & YouTube published `True`, Merchant price `2599.99`, issues `['price_updated', 'price_updated', 'price_updated']`.
- `AQ9129-170-9`: Shopify price `3349.99`, compare-at `2449.90`, Google & YouTube published `True`, Merchant price `2599.99`, issues `['price_updated', 'price_updated', 'price_updated']`.
- `GW3773-39`: Shopify price `3799.99`, compare-at `1699.99`, Google & YouTube published `True`, Merchant price `3799.99`, issues `['landing_page_error', 'landing_page_error', 'landing_page_error']`.

## Shopify channel/catalog evidence

- Google & YouTube channel: handle `google`, productsCount `1810`, app `Google & YouTube`.
- Google & YouTube catalog: `Channel Catalog 79416787166 for Google`, status `ACTIVE`.
- Shopify `productFeeds`: `0` nodes exposed.
- `productResourceFeedback`: not available with current token/scope (`read_resource_feedbacks` / sales-channel app scope required).

## Interpretação
- All sampled SKUs are active/found and published on Shopify Google & YouTube, so channel eligibility is not the blocker at publication level.
- Merchant final Content API price remains stale vs Shopify current price for sampled SKUs; this points to Google & YouTube sync/output state or Merchant source merge, not Shopify catalog price itself.
- Shopify API exposes some app/query surfaces, but installation/config details were not enough to inspect Google channel sync settings safely.

## Próximo checklist read-only/UI
- Shopify Admin > Sales channels > Google & YouTube: abrir product sync/status/feed diagnostics.
- Filtrar pelos SKUs amostra e confirmar se o app mostra preço antigo, erro de sync, pending review ou last synced timestamp.
- Merchant Center > Products > Data sources: confirmar se DS 10636492695 aparece como Google & YouTube/Content API channel e se há regra/attribute source para price.
- Merchant Center > Automatic improvements > Item updates: manter ligado por enquanto; só alterar com packet separado.
- Se UI mostrar botão de resync/reprocess em Google & YouTube, preparar plano com screenshots + rollback/monitor antes de qualquer execução.

## Not performed
- Shopify write
- Shopify app/channel config change
- Google & YouTube resync button
- Merchant write
- ProductInputs PATCH
- Content API write
- data source update/delete
- automatic item updates setting change
- feed upload/fetchNow
- Tiny write
- campaign/send/contact
