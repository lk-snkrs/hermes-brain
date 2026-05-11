# LK SEO/CRO weekly operationalization — 2026-05-11

Session learning from Lucas: when he says “módulo de CO” in the LK OS context, interpret as the weekly **SEO/CRO** improvement module already planned in the PRD, not as a one-off SEO report.

## Durable decisions

- The module must run weekly and produce a score/grade, goals, and concrete page/PDP improvements.
- The score comes from the Claude SEO skill family derived from `AgriciDaniel/claude-seo`: `seo-audit`, `seo-page`, `seo-content`, `seo-ecommerce`, plus `seo-schema`, `seo-geo`, and `seo-google` when available.
- SEO must become a fixed improvement queue. A “nice audit” with no next actions is a failure.
- Weekly reports should track current score, prior score when available, next target, and the top actions needed to increase the score.
- Keep the process read-only by default: auditing, scoring, Search Console/Merchant/Shopify reads, and recommendation previews are allowed; public writes require Lucas approval.

## Runtime cron created

- Cron name: `LK SEO/CRO weekly Claude SEO improvement loop`
- Job ID: `15777e3416dc`
- Schedule: `0 13 * * 1` (Monday 13:00 UTC / 10:00 BRT)
- Delivery: origin/Telegram
- Mode: read-only audit + recommendations
- Workdir: `/opt/data/hermes_bruno_ingest/hermes-brain-follow-20260510`

## Brain/versioning artifacts

- Brain PR: `lk-snkrs/hermes-brain#65`
- Merge commit: `9438ce8` (`docs(lk): operationalize weekly SEO CRO module`)
- Canonical Brain skill: `skills/lk-seo-weekly-improvement/SKILL.md`
- Routine: `areas/lk/rotinas/seo-cro-weekly-improvement-loop.md`
- Updated: `areas/lk/projetos/lk-operating-system-prd.md`, `areas/lk/projetos/lk-os-implementation-control.md`, `empresa/skills/_index.md`, `empresa/rotinas/_index.md`, `CHANGELOG.md`

## Guardrail reminder

Do not let the cron or manual weekly process write to Shopify, Tiny, Search Console, Merchant Center, theme/Liquid, feed settings, Klaviyo, WhatsApp, or any customer-facing channel. Use `needs_approval` and prepare a preview for any public change.
