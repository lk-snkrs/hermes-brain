# LK GMC P1 Wave6 — Price via Merchant API v1

Status: `merchant_api_v1_price_apply_verified`

## Escopo
- Campo alterado: `productAttributes.price` somente.
- Fonte de preço: Shopify/Data Spine, relatório Wave6.
- Data source: `accounts/*/dataSources/10636492695`

## Resultado
- Linhas fonte: 35
- Execução: {'patched_price_v1': 35}
- Verificação Merchant API: 32/35
- Verificação Content API: 32/35
- Required rows after: 2
- Counts after: {'price': 2}

## Rollback privado
- `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-13-p1-attribute-wave6-price-merchant-api-v1-executor-rollback-20260513T160309Z.json`

## Não executado
- merchant_delete
- non_price_update
- shopify_write
- tiny_call_or_write
- database_write
- feed_fetch
- campaign_or_message_send
