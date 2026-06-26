# LK Content — Gate 7 Shopify/Tiny read-only

Date: 2026-06-07
Profile: `lk-content`
Scope: Shopify/Tiny read-only validation and guardrails
Source of secrets: Doppler `lc-keys/prd`

## Result

Status: OK operacional, com observação Tiny.

## Evidence

- Job ID: `39fe0f2748d8`
- Output file: `/opt/data/profiles/lk-content/cron/output/39fe0f2748d8/2026-06-07_21-07-28.md`
- Overall script status: `partial` by strict initial classifier
- Operational interpretation: OK for Gate 7 read-only because both APIs were reached with HTTP 200 and no writes were executed.
- `values_printed`: `false`
- `writes_performed`: `0`
- `external_write_performed`: `false`
- Shopify write performed: `false`
- Tiny write performed: `false`
- Active cron jobs after cleanup/check: `0`

## Shopify

- Required secrets present: `SHOPIFY_ACCESS_TOKEN`, `SHOPIFY_STORE`
- Shopify read-only smoke HTTP status: `200`
- Shopify status: `ok`
- Readback evidence: shop name/domain/myshopify domain present, currency `BRL`, timezone `America/Sao_Paulo`, plan name present.

## Tiny

- Required/candidate secrets present: `TINY_API_TOKEN`, `TINY_CLIENT_ID`, `TINY_CLIENT_SECRET`
- Tiny products search HTTP status: `200`
- Records returned: `0`
- Initial classifier status: `partial_or_failed_read` because the sentinel search intentionally returned no matching records.
- Operational interpretation: API reach/auth validated; no-records response is acceptable for a safe sentinel read-only query.

## Changes made

- Updated central non-secret `PROFILE_SECRET_MAP['lk-content']` to include Tiny credential names.
- Added local Gate 7 script: `/opt/data/profiles/lk-content/scripts/gate7_shopify_tiny_readonly_check.py`.
- Added integration guardrail doc: `/opt/data/profiles/lk-content/integrations/shopify-tiny.md`.

## Guardrails

LK Content may use Shopify/Tiny read-only data for editorial/CRM context. It must not use stock as a prioritization factor. Writes to price, stock, product core data, theme, publication, Tiny operational records, or mass changes remain blocked without explicit approval.

No secrets, tokens, headers, full credential URLs, private keys, or raw env values were printed or stored.
