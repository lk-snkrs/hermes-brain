# LK Content — Gate 10 cron approval packet prepared

Date: 2026-06-07
Profile: `lk-content`
Scope: Gate 10 — Crons próprios

## Result

Status: approval packet prepared; recurring cron activation pending explicit approval.

No recurring cron jobs were created in this step because Gate 10 requires approved cadence and kill criteria before real recurring jobs.

## Files created

- `/opt/data/profiles/lk-content/integrations/crons.md`
- `/opt/data/profiles/lk-content/templates/cron-output-lk-content.md`
- `/opt/data/profiles/lk-content/templates/cron-approval-packet-gate10.md`

## Proposed initial crons

1. Monthly calendar v0 — day 1 at 09:00 BRT.
2. Weekly planning — Mondays at 09:30 BRT.
3. Growth/Trends radar — Wednesdays at 10:00 BRT, silent if no actionable opportunity.

Post-mortem remains one-shot after approved sends. Risk/opportunity alert is not recommended for initial activation.

## Guardrails

Allowed outputs:

- read-only research;
- Telegram/local report;
- documentary calendar;
- decision packet;
- brief/copy/preview;
- internal handoff.

Blocked without explicit current approval:

- Klaviyo draft/send/schedule/flow activation;
- Shopify/Tiny/Merchant/ads writes;
- public publishing;
- external contacts;
- purchase/reservation/negotiation;
- price, stock, discount, availability, or delivery promises.

## Verification

- Cron proposal read back successfully.
- Approval packet read back successfully.
- Active cron jobs after preparation: `0`.
- Secrets printed: no.
- External writes performed: `0`.

## Pending approval phrase

To activate the proposed recurring jobs, Lucas/Renan can approve with:

“Pode ativar os 3 crons iniciais do Gate 10 com essa cadência e kill criteria.”
