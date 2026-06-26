# Morning QA — LK Shopify/CRO/SEO — 2026-06-16

Generated: 2026-06-16 08:00 BRT approx.
Profile: lk-shopify
Mode: read-only public QA + Brain receipt review
External writes: 0
Shopify writes: 0
Stock/availability validation: not performed; stock remains lk-stock ownership.

## Scope

- Reviewed recent Shopify/PDP receipts from 2026-06-15/16.
- Ran cache-busted public storefront checks on home, key collections, search pages, and representative PDPs.
- Checked related Brain reports for automations/AI endpoints/watchdogs.

## Evidence reviewed

### Recent receipts

- `areas/lk/sub-areas/shopify/receipts/pdp-sizeguide-brand-tables-production-20260615.md`
  - Production PR #80 merged.
  - Production theme readback matched local SHA `7d223086fbc0`.
  - Live QA passed for Onitsuka, Adidas, ASICS, Yeezy, UGG, Nike geral, Jordan Mid control, Vomero control.
- `areas/lk/sub-areas/shopify/receipts/pdp-sizeguide-vomero-premium-production-merge-20260615.md`
  - Production PR #79 merged.
  - Production/DEV readback SHA `8444d3aede2f`.
  - Live QA passed on three Vomero Premium PDPs + Jordan Mid control.
- `areas/lk/sub-areas/collection-optimizer/receipts/pdp-dev-missing-geo-faq-schema-fix-20260616T104541Z.md`
  - DEV-only missing snippet fix for `lk-growth-geo-faq-schema`.
  - Production already had the snippet.
  - DEV preview no longer showed the Liquid missing-snippet error.

### Public storefront QA sampled

URLs fetched with cache-bust/mobile user-agent:

- `/`
- `/collections/sneakers`
- `/collections/new-balance` → redirected to `/collections/new-balance-todos-os-modelos`
- `/collections/nike` → redirected to `/collections/nike-todos-os-modelos`
- `/collections/adidas` → redirected to `/collections/adidas-todos-os-modelos`
- `/search?q=204L`
- `/search?q=9060`
- PDPs:
  - `/products/tenis-nike-vomero-premium-black-volt-preto`
  - `/products/yeezy-slide-glow-green`
  - `/products/air-jordan-1-mid-wolf-grey`
  - `/products/tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo`
  - `/products/samba-og-white-scarlet`
  - `/products/tenis-asics-gt-2160-white-putty-branco`
  - `/products/nike-dunk-low-rose-whisper`

Observed:

- HTTP status 200 for sampled home/collections/search/PDPs.
- No `Liquid error` in sampled public HTML.
- Canonical links present and on `https://lksneakers.com.br`.
- PDPs sampled contain `id="lk-sizeguide-modal"`.
- Product PDPs sampled contain FAQPage signal.
- mKFashion/global script signal appears on sampled pages.
- Search suggestions are present for:
  - `9060` → `/collections/new-balance-9060`, CTA `Ver coleção completa →`.
  - `204L` → `/collections/new-balance-204l`, CTA `Ver coleção completa →`.
- Collection URLs checked:
  - `/collections/new-balance-204l` returned 200.
  - `/collections/new-balance-9060` returned 200.
  - `/collections/nike-vomero-premium` returned 200.
  - `/collections/9060` and `/collections/204l` returned 404, expected because canonical handles include brand prefix.

## Findings

### P0 — no Shopify/storefront P0 found in sampled QA

No sampled public page showed Liquid errors, 500/404 on canonical targets, missing PDP modal shell, or absent search collection suggestion for 204L/9060.

### P1 — external automation risk outside Shopify surface

Brain packet `areas/lk/sub-areas/trends/approval-packets/lk-trends-email-cron-qa-approval-packet-20260616.md` reports a scheduled email cron contradiction:

- Cloudflare email job `lkcfemail1205` is enabled/scheduled.
- Last status says `paused_by_lucas_after_bad_newsletter`.
- Next run: 2026-06-22 12:25 UTC.

This is not Shopify, but it is a customer/team-facing external-send risk if not paused or re-approved.

Recommended safe action: ask Lucas to approve pausing that exact email cron, or route to LK Trends/Hermes Geral for the existing approval packet.

### P1 — atendimento/order-created template health outside Shopify surface

Brain receipt `areas/lk/sub-areas/atendimento/receipts/elle-official-send-persist-and-delivery-audit-20260616.md` reports:

- Abandoned-cart sends: 11 public sends, 0 failed in audited window; 10 delivered/read, 1 accepted without final callback.
- Original order-created template `lk_online_pedido_realizado_v1`: 32 failed due to Meta header mismatch.
- Fallback `lk_pedido_criado`: 14 public sends, 13 delivered/read, 1 failed.

This is not a Shopify-theme issue. It is an LK Atendimento/WhatsApp template health issue. No send/retry/template change was performed here.

### P2 — current Shopify/CRO opportunity: convert passing QA into deeper visual/browser QA only if Lucas wants

The read-only HTML QA is healthy, but it is not a full visual/browser click audit. If the goal today is conversion polish, next useful step is a small browser/mobile visual QA pass on:

- PDP size-guide open/close behavior.
- mKFashion button visibility/spacing.
- Search suggestion mobile layout for `204L` and `9060`.
- Collection first viewport compression on `/collections/sneakers`, `/collections/new-balance-todos-os-modelos`, `/collections/nike-todos-os-modelos`.

No write required for the audit. Any theme fix would need preview/approval.

## Non-actions

- No Shopify Admin write.
- No theme upload.
- No product/collection/price/stock/availability change.
- No Tiny/GMC/Klaviyo/Meta/WhatsApp/email/campaign action.
- No external send.

## Recommended next decision

1. Continue read-only with a **mobile visual/browser QA pack** for PDP/search/collections; or
2. Route/approve the existing **LK Trends cron pause** decision because it has an external-send risk before 2026-06-22.
