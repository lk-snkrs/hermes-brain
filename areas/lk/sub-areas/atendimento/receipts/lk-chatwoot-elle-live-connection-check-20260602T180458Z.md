---
title: LK Chatwoot / Elle live connection check
created_at_utc: 2026-06-02T18:04:58Z
area: lk/atendimento
system: chatwoot-elle
mode: read-only check
---

# LK Chatwoot / Elle live connection check

## Pergunta
Lucas perguntou se a Elle já está lendo tudo e se o Chatwoot está 100% conectado.

## Verificações read-only realizadas

- Public Chatwoot API: `https://chat.lkskrs.online/api`
  - version: `4.14.1`
  - queue_services: `ok`
  - data_services: `failing`
- Elle health: `https://elle.lkskrs.online/healthz`
  - ok: `true`
  - dry_run: `true`
  - write_enabled: `false`
  - kill_switch: `true`
- Authenticated Chatwoot Application API, account `1`:
  - account: `LK Sneakers`
  - labels present: `devolucao`, `estoque`, `financeiro`, `humano`, `pedido`, `prazo`, `reclamacao`, `troca`, `vip`, `whatsapp-api`
  - teams present: `suporte` id `1`, `atendimento whatsapp` id `2`
  - inboxes endpoint returned empty list
  - webhooks endpoint returned empty list
  - integrations apps include `webhook` enabled and `shopify` enabled

## Interpretation

Chatwoot core is online and Elle receiver is reachable, but the stack should not be described as 100% connected right now:

1. Chatwoot health reports `data_services: failing`.
2. No inbox is visible via account API, so WhatsApp inbox is not confirmed/visible.
3. No configured webhook is visible via account webhooks API, so Elle is not confirmed as actively subscribed from Chatwoot despite the receiver being healthy.
4. Elle remains dry-run/write-disabled/kill-switch, so it is not writing notes/labels/routing.

## What was not changed

- No Chatwoot writes.
- No Shopify/Tiny/WhatsApp changes.
- No Docker/VPS changes.
- No messages sent to customers.

## Next safe actions

- Diagnose Chatwoot `data_services: failing` from VPS/logs when SSH access is available.
- Confirm/create the WhatsApp inbox only after approved WhatsApp credentials/scope.
- Confirm/create the Elle webhook subscription if absent, after approval if this requires production write.
- Keep Elle in dry-run until real inbound event flow is observed.
