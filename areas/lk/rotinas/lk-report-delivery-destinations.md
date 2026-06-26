# LK Report Delivery Destinations

Updated: 2026-05-18

## Approved/intended destinations

- WhatsApp: `Grupo LK Vendas`
- Email: `lk@lksneakers.com.br`
- Telegram/origin: Lucas approval, previews, receipts, and sensitive decision notes.

## Guardrails

- WhatsApp group receives polished operational sales readouts only.
- Email receives the DesignMD/newsletter HTML companion with subject and preheader.
- Strategic recommendations, decisions, next steps, blockers, and approval requests go to Lucas via Telegram/origin, not to the WhatsApp group or report email.
- External sends still require the configured send pipeline and current approval rules for exact payload/cadence when applicable.

## Resolved technical destination

Read-only wacli lookup on account `hermes` resolved Lucas's `Grupo LK Vendas` destination to:

- Chat name: `[LK] Vendas/Trocas/Envios`
- JID: `120363314625506305@g.us`
- Account: `hermes`

Machine-readable config: `/opt/data/hermes_bruno_ingest/hermes-brain/config/lk-report-delivery-targets.json`.

Current watchdogs still generate Telegram/origin previews unless explicit external send automation is enabled with approved payload/cadence.
