# LK Content — Google Calendar write smoke — OK

Date: 2026-06-07
Profile: `lk-content`
Scope: Google Calendar scoped write validation
Source of secrets: Doppler `lc-keys/prd`

## Result

Status: OK

Lucas requested validation of autonomous event creation. A one-shot local job created one clearly labelled internal technical event in the LK Content calendar and read it back successfully.

## Evidence

- Job ID: `a1310da18ae7`
- Output file: `/opt/data/profiles/lk-content/cron/output/a1310da18ae7/2026-06-07_21-03-27.md`
- Target calendar: `lk@lksneakers.com.br`
- Credential mode: `service_account_json`
- `values_printed`: `false`
- Create HTTP status: `200`
- Readback HTTP status: `200`
- Event created: yes
- Event updated: no
- Event deleted: no
- Attendees/invites: `0`

## Created event

- Summary: `LK Content — Smoke Test Calendar Write`
- Start: `2026-06-08T10:00:00-03:00`
- End: `2026-06-08T10:15:00-03:00`
- Event ID: `ebm2vqs5jpshfsa3sinmp5s7o0`
- Link: `https://www.google.com/calendar/event?eid=ZWJtMnZxczVqcHNoZnNhM3Npbm1wNXM3bzAgbGtAbGtzbmVha2Vycy5jb20uYnI`

## Guardrails

Autonomous creation is considered validated only for internal LK Content events in the authorized calendar. Updates/deletes, external attendees, non-LK calendars, and recurring automation creation still require explicit scope/kill criteria.

No secrets, tokens, headers, service-account JSON, or private keys were printed.
