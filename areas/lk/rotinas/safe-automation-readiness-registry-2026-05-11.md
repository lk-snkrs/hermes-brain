# LK Safe Automation Readiness Registry, 2026-05-11

Generated at: `2026-05-11T21:45:57.893106+00:00`

## Veredito

Fase 8 foi aberta no modo correto: catálogo e dry-run, sem criar cron, n8n, envio externo ou write produtivo.

## Snapshot

- Automações candidatas: 6
- Crons criados: 0
- n8n flows criados: 0
- Envios externos: 0
- Writes produtivos: 0
- Ativações exigindo aprovação Lucas: 6

## Gates globais de ativação

- At least one clean manual dry-run for each automation before approval request.
- Secret/PII scan clean on generated artifacts.
- Rollback/pause command documented before cron/n8n activation.
- Silent-OK contract defined: no spam when everything is normal.
- Medium/high risk automations require explicit Lucas approval with cadence and delivery target.

## Automações candidatas

### LK-AUTO-001 · Daily Sales Brief read-only

- Risco: `low`
- Modo agora: `dry_run_only`
- Cadência candidata: daily 08:00 BRT
- Contrato silent-OK: If generated successfully with no material anomaly, stay silent or save to Brain only; alert only on relevant sales/stock anomaly.
- Dry-run: Run the existing read-only briefing script/report generation manually and verify no PII/secrets before any recurring delivery.
- Próximo passo recomendado: Run 3 manual dry-runs on separate days before cron approval.
- Proibido agora: Telegram auto-send, email send, WhatsApp send, Shopify/Tiny writes

### LK-AUTO-002 · Weekly CEO Review read-only

- Risco: `low`
- Modo agora: `dry_run_only`
- Cadência candidata: weekly Monday 09:00 BRT
- Contrato silent-OK: Save report quietly; alert Lucas only if P0/P1 decisions are generated or data source is stale.
- Dry-run: Generate next weekly review locally with Shopify+GA4+Tiny read-only and compare source freshness labels.
- Próximo passo recomendado: Candidate for first read-only cron after one more clean manual run.
- Proibido agora: recurring Telegram delivery, campaign/customer action, stock/price writes

### LK-AUTO-003 · SEO/CRO weekly monitor read-only

- Risco: `low`
- Modo agora: `dry_run_only`
- Cadência candidata: weekly Monday 10:00 BRT
- Contrato silent-OK: Alert only when new P1/P2 SEO opportunity or Merchant issue appears; do not auto-write Shopify.
- Dry-run: Run Search Console, Merchant, PDP low-conversion routers manually and confirm writes_allowed_now=0.
- Próximo passo recomendado: Safe as read-only monitor only after Lucas approves cadence/delivery.
- Proibido agora: Shopify SEO writes, H1/body/theme edits, Merchant/feed writes, Indexing API submits

### LK-AUTO-004 · Approval Learning Ledger refresh

- Risco: `low`
- Modo agora: `dry_run_only`
- Cadência candidata: on-demand or post-PR hook, not time-based initially
- Contrato silent-OK: No message unless a pending item changes status or a contradiction is detected.
- Dry-run: Regenerate ledger locally and compare counts/status with source artifacts.
- Próximo passo recomendado: Keep as manual post-action step until ledger pattern stabilizes.
- Proibido agora: automatic approval, automatic execution, external notifications

### LK-AUTO-005 · Klaviyo CRM draft watcher

- Risco: `medium`
- Modo agora: `dry_run_only`
- Cadência candidata: manual only for now
- Contrato silent-OK: No automatic send; only surface draft readiness/risks.
- Dry-run: List campaign/draft IDs read-only and produce readiness packet without UI deep links unless verified.
- Próximo passo recomendado: Do not automate yet; keep on-demand readiness preview.
- Proibido agora: send campaign, schedule campaign, customer contact, unverified deep link in output

### LK-AUTO-006 · On-demand sourcing router

- Risco: `medium`
- Modo agora: `dry_run_only`
- Cadência candidata: event/manual only
- Contrato silent-OK: No background full-sync; run only for named approved item and return preview.
- Dry-run: Given one approved mock decision, generate a no-contact lookup plan and verify no network contact/send occurs.
- Próximo passo recomendado: Wait for one specific sourcing approval; do not create cron.
- Proibido agora: supplier contact, purchase commitment, full-sync prices, stock write

