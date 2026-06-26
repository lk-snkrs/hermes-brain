# LK GMC P1 Price — Merchant API v1 Final Verification

Status: `gmc_p1_required_attributes_zero_final_verified`

## Implementado

- Registrado/autorizado o projeto GCP `openclaw-hst` (`279776001868`) no Merchant Center via Merchant API `developerRegistration:registerGcp`.
- Aplicado `productAttributes.price` via Merchant API ProductInputs v1 para 35 produtos, usando preço Shopify/Data Spine do relatório Wave6.
- Campo alterado: `price` somente.
- Data source: `accounts/*/dataSources/10636492695`.

## Resultado de execução

- PATCH v1 executados: 35/35.
- Verificação inicial após apply: 32/35 já refletidos; 3 ainda em propagação.
- Recheck final posterior de `productstatuses`: 23.245 linhas lidas.
- Required attribute rows: 0.
- Required attribute counts: {}.

## Rollback privado

- `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-13-p1-attribute-wave6-price-merchant-api-v1-executor-rollback-20260513T160309Z.json`

## Não executado

- Delete Merchant/GMC.
- Shopify/Tiny/database writes.
- Feed fetch/manual upload.
- Campanha, Klaviyo, WhatsApp, Notion ou mensagem externa.
