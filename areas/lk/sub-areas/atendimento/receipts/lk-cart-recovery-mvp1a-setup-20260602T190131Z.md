---
title: LK Carrinho Abandonado MVP 1A setup
created_at_utc: 2026-06-02T19:01:31Z
area: lk/atendimento
system: shopify-chatwoot
mode: internal-only
---

# LK Carrinho Abandonado MVP 1A setup

## Scope approved by Lucas

Lucas asked to proceed with **MVP Carrinho Abandonado 1A** after research on abandoned cart using Chatwoot.

MVP 1A boundary:

- Shopify read-only abandoned checkout intake.
- Chatwoot internal-only setup and triage objects.
- No customer-visible WhatsApp/message send.
- No Shopify write.
- No Tiny/stock promise.
- No cron/schedule activation yet.

## Implementation

Created worker script:

```text
/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/scripts/lk_cart_recovery_mvp1a.py
```

Main behavior:

1. Fetches Shopify abandoned checkouts from Admin REST `checkouts.json`.
2. Filters out:
   - completed checkouts;
   - closed checkouts;
   - records without recovery URL;
   - records without contact;
   - very recent records under the configured age threshold.
3. Ensures internal Chatwoot API inbox:
   - `Shopify Carrinho Abandonado`
4. Ensures labels:
   - `carrinho-abandonado`
   - `shopify`
   - `recuperacao`
   - `humano`
5. When eligible new checkout exists and `--apply` is used:
   - creates contact in Chatwoot;
   - creates conversation in the API inbox;
   - assigns team `atendimento whatsapp` when available;
   - adds private note with checkout context and recovery URL;
   - applies labels;
   - records checkout ID in local idempotency state.

## Chatwoot writes performed

Internal-only writes performed:

- Created/confirmed inbox:
  - ID: `1`
  - Name: `Shopify Carrinho Abandonado`
  - Type: `Channel::Api`
- Created/confirmed labels:
  - `carrinho-abandonado`
  - `shopify`
  - `recuperacao`
  - `humano` already existed

No customer messages were sent.

## Live Shopify dry-run result

Command mode: dry-run.

Report:

```text
/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/reports/lk_cart_recovery_mvp1a_20260602T190115Z_dryrun.json
```

Result:

- fetched: `6`
- eligible: `0`
- already_processed: `0`
- written_internal: `0`
- reason distribution: all fetched records were `completed_checkout`

Interpretation: current Shopify abandoned-checkout endpoint returned historical recovered/completed checkouts; there were no currently eligible abandoned checkouts to create conversations for at verification time.

## Apply run result

Report:

```text
/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/reports/lk_cart_recovery_mvp1a_20260602T190043Z_apply.json
```

Result:

- fetched: `6`
- eligible: `0`
- written_internal: `0`
- inbox setup: completed
- label setup: completed

## Verification

- Script syntax verified with `python3 -m py_compile`.
- Chatwoot API readback verified:
  - inbox `Shopify Carrinho Abandonado` exists as `Channel::Api`.
  - labels now include `carrinho-abandonado`, `shopify`, `recuperacao`.
  - teams include `atendimento whatsapp` ID `2`.
- Post-setup dry-run verified missing labels is empty and inbox is present.

## Not done / remaining

- No cron/scheduled automation activated.
- No WhatsApp live inbox connected by this step.
- No customer-facing message or WhatsApp template sent.
- No Shopify webhook created.
- No Shopify/Tiny/stock writes.

## Next recommended step

If Lucas wants it continuous, prepare/approve MVP 1A scheduler:

- run every 15 or 30 minutes;
- use min age threshold, e.g. 30–60 minutes;
- cap per run;
- keep customer sends disabled;
- monitor report/state files.
