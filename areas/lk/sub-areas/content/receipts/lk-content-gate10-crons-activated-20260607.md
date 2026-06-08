# LK Content — Gate 10 crons activated

Date: 2026-06-07
Profile: `lk-content`
Scope: Gate 10 — Crons próprios
Approval: Lucas approved activation in Telegram with “Aprovado” after receiving cadence and kill criteria packet.

## Result

Status: OK — 3 recurring jobs created and verified active/scheduled.

## Jobs created

1. `LK Content — Calendário mensal v0`
   - job_id: `d4d4bf090aa7`
   - schedule: `0 12 1 * *` UTC = day 1 at 09:00 BRT
   - next_run_at: `2026-07-01T12:00:00+00:00`
   - deliver: origin Telegram chat
   - profile: `lk-content`

2. `LK Content — Planejamento semanal`
   - job_id: `a4a705ff28ca`
   - schedule: `30 12 * * 1` UTC = Mondays at 09:30 BRT
   - next_run_at: `2026-06-08T12:30:00+00:00`
   - deliver: origin Telegram chat
   - profile: `lk-content`

3. `LK Content — Radar Growth Trends`
   - job_id: `18dbd1e2c54d`
   - schedule: `0 13 * * 3` UTC = Wednesdays at 10:00 BRT
   - next_run_at: `2026-06-10T13:00:00+00:00`
   - deliver: origin Telegram chat
   - profile: `lk-content`

## Guardrails embedded in job prompts

- No recursive cron creation.
- No Klaviyo draft/send/schedule/flow activation.
- No Shopify/Tiny/Merchant/ads writes.
- No public publishing or external contact.
- No promises about price, stock, discount, availability, reservation, or delivery.
- No secrets printed.
- Outputs are planning/read-only decision packets.

## Verification

- Cron list after activation returned count: `3`.
- All jobs state: `scheduled`.
- All jobs enabled: `true`.
- All jobs use profile: `lk-content`.
- Delivery target: `origin` Telegram chat.

## Notes

Scheduler returns next_run_at in UTC. Schedules were corrected to UTC equivalents so the intended BRT cadence is preserved.
