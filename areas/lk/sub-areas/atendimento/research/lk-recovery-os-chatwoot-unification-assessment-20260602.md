---
title: lk-recovery-os + Chatwoot unification assessment
created_at_utc: 2026-06-02
area: lk/atendimento
systems: [shopify, chatwoot, cloudflare-worker, supabase, crisp, klaviyo]
repo: https://github.com/lk-snkrs/lk-recovery-os
head: 306fcee
status: assessment-only
---

# LK Recovery OS + Chatwoot unification assessment

## Scope

Lucas asked whether the existing GitHub project `lk-snkrs/lk-recovery-os` can be connected/studied and how to unite it with the new Shopify lifecycle + Chatwoot architecture.

This assessment is read-only: no production writes, no Shopify webhook creation, no Worker deploy, no Chatwoot/WhatsApp message sends.

## Access / clone

- Repo cloned read-only to `/opt/data/lk-recovery-os`.
- Current branch: `main`.
- Latest commit observed: `306fcee 2026-05-28 15:16:57 -0300 Fix audit_log loop + GH Actions spam + Worker resiliency (#20)`.
- Public Worker health checked: `https://recovery.lucascimino.com/healthz` returned `{"service":"lk-recovery","status":"ok"}`.

## Codebase shape

Approximate local footprint, excluding `.git`, node_modules, venvs:

- Python: 72 files / ~16.8k lines.
- TypeScript: 26 files / ~7.1k lines.
- Tests: 155 Python tests and 41 Worker/Vitest tests pass locally after installing dependencies.
- Main production-looking path is Cloudflare Worker under `workers/recovery-os`.
- Earlier FastAPI/Python app still exists under `src/lk_recovery_os`, plus scripts and GitHub Actions.

## Existing architecture found

The repo is much more advanced than a simple abandoned-cart script. It already contains most of the hard Shopify lifecycle foundation:

### Cloudflare Worker

Worker endpoint list exposed at `/` includes:

- `POST /shopify/checkouts/create`
- `POST /shopify/checkouts/update`
- `POST /shopify/orders/create`
- `POST /shopify/carts/create`
- `POST /shopify/carts/update`
- `POST /events/storefront`
- `POST /links/whatsapp/mint`
- `POST /webhooks/crisp/inbound`
- `POST /webhooks/klaviyo/event`
- `POST /callbacks/crisp/whatsapp`
- `POST /callbacks/provider`
- `cron */10 * * * * (T1 + anchor drain + marketing reconcile + scoring)`

Important files:

- `workers/recovery-os/src/index.ts`: routing, Shopify HMAC, Worker cron.
- `workers/recovery-os/src/shopify.ts`: Shopify checkout webhook normalizer.
- `workers/recovery-os/src/ingestion.ts`: persists checkout events, marks checkout completed from orders, stitches identities, fires Klaviyo Started Checkout.
- `workers/recovery-os/src/t1.ts`: T1 candidate collection and Crisp WhatsApp send path.
- `workers/recovery-os/src/crisp.ts`: Crisp WhatsApp template API + Crisp inbox notes/profile lookups.
- `workers/recovery-os/src/inbound.ts`: Shopify cart webhook + storefront beacon ingestion.
- `workers/recovery-os/src/scoring.ts`: behavioral scoring and recovery candidate materialization.
- `workers/recovery-os/src/supabase.ts`: Supabase REST client.

### Data model / persistence

Primary persistence is Supabase/PostgREST, not Chatwoot:

- `raw_events`
- `checkouts`
- `identity_events`
- `identity_links`
- `identity_clusters`
- `recovery_candidates`
- `recovery_sequences`
- `recovery_messages`
- `suppression_list`
- `cooldowns`
- `audit_log`

This is valuable. It is the event ledger / identity spine the Chatwoot-only MVP does not have.

### Identity / scoring strengths

The repo already solves difficult problems:

- Shopify checkout webhooks normalized to stable checkout IDs.
- `orders/create` marks corresponding checkout completed through checkout_id, cart_token, checkout_token fallback.
- Storefront beacon catches product/cart behavior before checkout.
- Klaviyo/Crisp identity enrichment exists.
- Identity clustering/backward stitching exists.
- Scoring engine detects non-checkout intent: product views, add to cart, begin checkout, WhatsApp click, etc.
- Cooldowns, phone caps, suppression list, and per-tick phone dedupe exist.

This aligns strongly with the research recommendation: event-driven lifecycle receiver + delayed/cron eligibility + fallback.

## What's not aligned with Lucas's current direction

### 1. It is Crisp-centric

There are zero Chatwoot references in the repo. Search for `chatwoot` returned no files/matches.

Current outbound/inbox integration is Crisp:

- `sendCrispWhatsappTemplate`
- `crispPostInboxNote`
- `crispFindSession`
- `crispGetProfile`
- Crisp inbound webhook and callbacks.

Lucas has now chosen Chatwoot as customer-service system, not Crisp. So we should preserve the recovery brain but replace the provider adapter layer.

### 2. Current Worker config appears live-send oriented

`workers/recovery-os/wrangler.toml` has:

- `LK_RECOVERY_DRY_RUN = "false"`
- `LK_RECOVERY_PAUSE = "false"`
- `LK_LIVE_SEND_ENABLED = "true"`
- `LK_WHATSAPP_SEND_ENABLED = "true"`
- `T1_TEMPLATE_NAME = "lk_checkout_abandonado_30min_v4"`

This is the opposite of the new safe Chatwoot-first stance (`dry_run=true`, `write_enabled=false`, no public replies). I did not verify deployed Cloudflare secret/vars; the file is a strong risk signal, not proof of actual live sending right now.

### 3. The existing GitHub scheduled identity sync is failing

Recent GitHub Actions runs for `cross-platform-identity-sync` are failing. Latest inspected failure:

- Workflow: `cross-platform-identity-sync`
- Error: Supabase REST GET `identity_links` failed with HTTP 522 Cloudflare origin timeout.

This suggests the identity enrichment side is currently unstable or dependent on Supabase availability. The core Worker may still be up, but this workflow is not healthy.

### 4. Supabase is a dependency/risk

The Worker writes and reads Supabase heavily. Current failures show Supabase/API/origin timeout risk. For LK operations, Chatwoot can be the support surface, but Supabase remains the event/source ledger unless we migrate away.

### 5. Existing flow sends/anchors after sending, rather than internal-first

The current T1 path reserves `recovery_messages`, sends Crisp WhatsApp template, then attempts to anchor/note in Crisp inbox. Lucas's current Chatwoot strategy wants the reverse for MVP:

- create internal context first;
- no public send until approved templates + inbox + policy are ready;
- human-first in Chatwoot.

## Best unification strategy

Do not throw away `lk-recovery-os`. It is already the best foundation for Shopify lifecycle intelligence.

Recommended target architecture:

```text
Shopify + storefront + Klaviyo events
→ lk-recovery-os event receiver / Supabase ledger / identity spine / scoring
→ Provider Adapter interface
→ Chatwoot adapter (internal-first)
→ later WhatsApp Cloud via Chatwoot templates, behind explicit gates
```

The correct move is to convert `lk-recovery-os` from “Crisp recovery sender” into “LK Lifecycle OS”.

## Adapter migration plan

### Phase 0 — Freeze customer-facing sends

Before any merge/cutover, require live-send freeze:

- Cloudflare Worker vars/secrets should be verified.
- `LK_RECOVERY_PAUSE=true` or `LK_LIVE_SEND_ENABLED=false` should be applied before experiments.
- No public message sends from the old Crisp path.

### Phase 1 — Add provider abstraction

Create an interface, e.g.:

```ts
interface SupportProvider {
  findOrCreateContact(input): Promise<ContactRef>;
  findOrCreateConversation(input): Promise<ConversationRef>;
  addPrivateNote(input): Promise<NoteRef>;
  applyLabels(input): Promise<void>;
  assignTeam(input): Promise<void>;
  sendTemplate?(input): Promise<SendResult>;
}
```

Then implement:

- `CrispProvider` from existing `crisp.ts` for legacy/reference only.
- `ChatwootProvider` as the new default.

### Phase 2 — Internal-only Chatwoot T1

Change T1 abandoned cart behavior to:

```text
candidate eligible
→ create/update Chatwoot contact
→ create/find Chatwoot conversation in Shopify Carrinho Abandonado inbox
→ apply labels
→ assign team atendimento whatsapp
→ add private note with recovery URL, product, contact, source, cooldown metadata
→ record recovery_messages/status = internal_context_created
→ no public message
```

This matches the MVP 1A script already created locally, but uses the stronger `lk-recovery-os` data model and Worker/event pipeline.

### Phase 3 — Lifecycle events beyond cart

Add handlers/notes for:

- `orders/create`: pedido feito / aguardando aprovação.
- `orders/paid`: pedido aprovado.
- fulfillment event: pedido enviado.
- delivery-confirmed event only if a reliable tracking source exists.
- follow-up de venda as marketing, opt-in/cooldown/template-gated.

These should write Chatwoot context first. Public WhatsApp later only with approved templates and explicit gates.

### Phase 4 — Optional public WhatsApp via Chatwoot

After Meta/WhatsApp Cloud inbox is working in Chatwoot:

- use Chatwoot message API with `template_params`.
- each message type has category and template name.
- order events likely Utility; abandoned cart/follow-up likely Marketing.
- keep caps, opt-out and quiet hours from Recovery OS.

## What to reuse from old project

Keep/reuse:

- Shopify HMAC webhook receiver.
- checkout/cart/order normalizers.
- Supabase event ledger.
- identity graph / backward stitch.
- scoring engine.
- cooldowns and suppression list.
- order recheck before sending/creating recovery action.
- audit_log and funnel reporting.
- tests around Shopify normalizer, callback idempotency, cooldowns.

Replace/disable:

- Crisp WhatsApp send path.
- Crisp inbox note anchor path.
- Crisp profile enrichment eventually, unless retained as historical enrichment only.
- live-send defaults in `wrangler.toml`.

Add:

- Chatwoot API adapter.
- Chatwoot labels/team/inbox config.
- internal-only statuses.
- lifecycle event taxonomy beyond T1.
- admin/funnel endpoint that reports internal contexts created, not just sends.

## Immediate risks to handle before implementation

1. **Double system risk:** old Worker may still be active while Elle/MVP script also exists. Need single owner for Shopify webhook topics.
2. **Live send risk:** repo config indicates live sending can be active through Crisp. Verify Cloudflare deployed vars and pause before changes.
3. **Supabase availability risk:** GitHub identity sync is failing on Supabase HTTP 522.
4. **Provider migration risk:** if we rip Crisp out too fast, we lose phone/profile enrichment. Migrate via adapter, do not delete first.
5. **WhatsApp policy risk:** abandoned cart/follow-up are marketing; order statuses are utility. Do not blend template categories.
6. **Support UX risk:** Chatwoot conversation creation should be idempotent per lifecycle entity, or support will see duplicated threads.

## Verification performed

Local:

- Python tests: `155 passed, 1 warning`.
- Worker tests: `41 passed`.
- Public Worker health: ok.
- GitHub Actions recent runs inspected: `cross-platform-identity-sync` failing with Supabase 522.

No production mutations performed.
