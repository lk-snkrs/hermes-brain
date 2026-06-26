---
title: LK Recovery OS operational status check
created_at_utc: 2026-06-02
area: lk/atendimento
status: partial_ok_supabase_unhealthy
---

# LK Recovery OS operational status check

Asked: whether the abandoned-cart capture system is now correct/working.

## Findings

- GitHub `CI` latest runs on `37a5c055` are green.
- GitHub `cross-platform-identity-sync` latest scheduled run is green after PR #23.
- GitHub `t1-runner` is intentionally deprecated/manual-only; schedule disabled to prevent double-sends. Its historical failures from 2026-05-28 are not current scheduler failures.
- Cloudflare Worker route from `workers/recovery-os/wrangler.toml` is the current owner of webhook ingestion + T1 cron:
  - route: `recovery.lucascimino.com`
  - cron: `*/10 * * * *`
  - dry-run: `LK_RECOVERY_DRY_RUN=true`
  - Chatwoot provider: `LK_SUPPORT_PROVIDER=chatwoot`
  - internal-only: `LK_CHATWOOT_INTERNAL_ONLY=true`
  - customer sends disabled: `LK_LIVE_SEND_ENABLED=false`, `LK_WHATSAPP_SEND_ENABLED=false`, `LK_EMAIL_SEND_ENABLED=false`
- Worker health check:
  - `https://recovery.lucascimino.com/healthz` returned HTTP 200 with `{"service":"lk-recovery","status":"ok"}`.
- Vercel project is deployed/READY/PROMOTED for commit `37a5c055`, author `lk@lksneakers.com.br`, but `/healthz` on `lk-recovery-os.vercel.app` remains intermittently timing out. This appears separate from current Worker-owned capture.
- Supabase read-only probes for `raw_events`, `checkouts`, `recovery_sequences`, `recovery_messages`, and `audit_log` returned HTTP 522 or timed out. A retry script attempting current event checks timed out after 5 minutes.

## Operational conclusion

- Code/deploy/workflow state: OK.
- Worker ingress health: OK.
- Current customer-facing sending: intentionally OFF / dry-run/internal-only.
- Supabase data plane: NOT healthy at check time (522/timeouts), so cannot verify recent captured cart rows or claim end-to-end capture is currently functioning.

## Recommended next check

When Supabase recovers, run read-only verification of recent rows:

- latest `raw_events` for Shopify checkout/cart events;
- latest `checkouts` rows;
- latest `recovery_candidates` if scoring is enabled;
- latest `recovery_messages`/`audit_log` for dry-run/internal Chatwoot context behavior.
