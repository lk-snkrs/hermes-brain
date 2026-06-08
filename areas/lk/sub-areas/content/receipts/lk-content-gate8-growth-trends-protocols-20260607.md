# LK Content — Gate 8 Growth/Trends protocols

Date: 2026-06-07
Profile: `lk-content`
Scope: Gate 8 — Pesquisa, LK Growth e LK Trends

## Result

Status: OK

Gate 8 was implemented as a read-only/documental operating protocol. No external writes, sends, contacts, purchases, reservations, Shopify/Tiny/Merchant/Klaviyo changes, or recurring cron jobs were created.

## Files created

- `/opt/data/profiles/lk-content/integrations/lk-growth-trends.md`
- `/opt/data/profiles/lk-content/templates/intelligence-request-lk-growth-trends.md`
- `/opt/data/profiles/lk-content/templates/intelligence-handoff-response-lk-growth-trends.md`

## Sources consulted

- LK Growth Weekly Command Center playbook
- LK Growth Decision Router
- LK Trends routing criteria v1
- LK Trends weekly report model v1
- LK Content editorial calendar skill

## Protocol summary

LK Content may request read-only intelligence from LK Growth and LK Trends for campaigns, calendars, newsletters, CRM/Klaviyo, social repurpose, guides, and post-mortems.

- LK Growth contributes demand/performance/SEO/GEO/CRO/commercial evidence.
- LK Trends contributes external sneaker/fashion signals and routing: boost, sourcing, catálogo-preview, watchlist, ignorar.
- LK Content converts evidence into premium editorial narrative, copy, calendar, creative brief, and CRM decisions.

## Guardrails

Allowed without further approval:

- read-only research;
- local reports;
- decision packets;
- internal handoffs;
- copy/creative previews;
- documentary calendar planning.

Still blocked without explicit current approval:

- Klaviyo draft/send/schedule/flow activation;
- Shopify/Tiny/Merchant writes;
- contact with suppliers/Júlio/third parties;
- purchase/reservation/negotiation;
- public publishing;
- price, stock, catalog, product, theme, ads, or recurring cron changes.

## Verification

- Protocol file read back successfully.
- Request template read back successfully.
- Handoff template read back successfully.
- Active cron jobs after Gate 8: `0`.
- Secrets printed: no.
