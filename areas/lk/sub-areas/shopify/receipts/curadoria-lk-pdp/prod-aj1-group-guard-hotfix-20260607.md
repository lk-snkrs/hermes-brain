# Curadoria LK PDP — AJ1 group guard hotfix

Date: 2026-06-07T00:07:29Z

## Trigger

Lucas confirmed the layout was fixed, but the AJ1 Low PDP still showed two Curadoria blocks: the top Low block made sense, the lower High/OG block did not.

## Root cause

The split snippet `snippets/lk-variante-aj1-low-high-20260606.liquid` had two independent sections. Each section excluded the current product from its card list, but neither section was guarded to render only when `product.handle` belongs to that section's handle array.

Result: Low PDP could render both Low and High groups.

## Change applied

Added per-group Liquid guard:

```liquid
{%- if lk_handles contains product.handle -%}
  <section ...>
  ...
  </section>
{%- endif -%}
```

Applied to both groups:

- `top30-air-jordan-1-low-adult-breadth`
- `top30-air-jordan-1-high-og-breadth`

Themes kept aligned:

- DEV theme `155065450718`, role `unpublished`
- Production theme `155065417950`, role `main`

## Readback evidence

DEV:

- Before SHA: `31d37c719a038f0145d5f482c8aeac987bb202088e614de8ad46e2a780aee0df`
- Target/readback SHA: `96d936e1a2dddd14f419f3388cb46e1454031bfd95183f9c0aa762bac90e7b7a`
- Readback match: true
- Guard count: 2
- Legacy grid count: 0
- Rail count: 2

Production:

- Before SHA: `31d37c719a038f0145d5f482c8aeac987bb202088e614de8ad46e2a780aee0df`
- Target/readback SHA: `96d936e1a2dddd14f419f3388cb46e1454031bfd95183f9c0aa762bac90e7b7a`
- Readback match: true
- Guard count: 2
- Legacy grid count: 0
- Rail count: 2

## Public QA

Low PDP, repeated cache-busted checks:

- `tenis-air-jordan-1-low-eastside-golf-azul-marinho`
- section count: 1
- expected Low marker: true
- wrong High marker: false
- rail count: 1
- legacy grid: false

High PDP had one fresh clean check and one rotating stale check, suggesting edge/cache propagation rather than source logic failure:

- fresh clean check: section count 1, expected High marker true, wrong Low marker false
- later rotating stale check: section count 2, wrong Low marker true

## Artifacts

JSON:

- `/opt/data/tmp/lk_aj1_group_guard_hotfix_20260607T000729Z.json`

Backups:

- DEV: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-before-aj1-group-guard-hotfix-20260607T000729Z.liquid`
- Production: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/prod-before-aj1-group-guard-hotfix-20260607T000729Z.liquid`

Readbacks:

- DEV: `/opt/data/tmp/dev-aj1-group-guard-hotfix-readback-20260607T000729Z.liquid`
- Production: `/opt/data/tmp/prod-aj1-group-guard-hotfix-readback-20260607T000729Z.liquid`

## Rollback

Restore Production `snippets/lk-variante-aj1-low-high-20260606.liquid` from:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/prod-before-aj1-group-guard-hotfix-20260607T000729Z.liquid`
