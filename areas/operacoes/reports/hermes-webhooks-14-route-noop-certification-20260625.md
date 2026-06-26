# Hermes Webhooks — certificação no-op 14 rotas — 2026-06-25

## Resultado

- Status: **partial**
- Rotas testadas: 14
- Pass: 10
- Attention: 4
- Writes externos/envios/deploys/env changes/restarts: `0`
- Secrets/signatures impressos: `0`; `values_printed=false`
- Base pública testada: `https://hermes-webhooks.lucascimino.com`

## Rotas PASS

- `lk-content-klaviyo-events` — HTTP `200` — status `processed`
- `lk-evolution-delivery-reconciliation` — HTTP `202` — status `accepted`
- `lk-online-waba-dryrun` — HTTP `200` — status `dry_run_recorded` — external_send_executed `False`
- `lk-shopify-birthday-klaviyo-sync` — HTTP `200` — status `processed`
- `lk-shopify-orders-ingest` — HTTP `200` — status `recorded`
- `lk-shopify-pos-restock` — HTTP `200` — status `ignored` — reason `not_paid_active_pos_order`
- `lk-stock-shopify-sales-os` — HTTP `200` — status `processed`
- `lk-stock-tiny-events` — HTTP `200` — status `ignored` — reason `unknown_tiny_event_shape` — writes_externos `0`
- `lk-stock-tiny-stock` — HTTP `200` — status `processed` — writes_externos `0`
- `lk-stock-tiny-stock-snapshot` — HTTP `200` — status `processed` — writes_externos `0`

## Rotas ATTENTION

- `lk-shopify-tiny-stock-sync` — HTTP `401` — `Invalid signature` — esperado: ignored order_not_paid dry-run
- `lk-shopify-tiny-stock-sync-dryrun` — HTTP `401` — `Invalid signature` — esperado: ignored order_not_paid dry-run
- `lk-stock-shopify-order-paid` — HTTP `401` — `Invalid signature` — esperado: processed local cache no external write
- `lk-stock-shopify-product-update` — HTTP `401` — `Invalid signature` — esperado: processed local cache no external write

## Diagnóstico sanitizado

- As 4 rotas com attention falharam em `Invalid signature` no Hermes após o proxy, não por payload de negócio.
- Essas rotas aparecem no registro dinâmico com `secret_present=true` e sem `secret_doppler`; o proxy Vercel assina com os segredos canônicos por família. Isso sugere drift entre segredo literal da subscription dinâmica e segredo canônico do proxy/route, sem imprimir valores.
- As rotas Tiny stock que tinham falhado com payload vazio passaram quando usado payload no-op com `sku` probe e `saldo=0`; gravaram apenas ledger/cache local com `public_availability_safe=0` e `availability_claim_allowed=0`.

## Próximo gate se Lucas quiser corrigir as 4

Preparar approval packet específico para alinhar as quatro subscriptions dinâmicas ao segredo canônico/Doppler esperado, com backup do arquivo de subscriptions, teste no-op, rollback e sem Vercel/Shopify/Tiny/Doppler write salvo aprovação separada.

## Artefatos

- Resultado JSON sanitizado: `/opt/data/tmp/hermes_webhooks_14_route_certification_latest.json`
- Script de certificação: `/opt/data/tmp/hermes_webhooks_14_route_certification.py`
