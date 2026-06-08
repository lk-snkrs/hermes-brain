# Hermes Webhooks Vercel — canonical ingress rule

Date: 2026-06-07
Owner: Hermes Geral / Operações Hermes
Scope: documentary/local governance only

## Decision

Lucas instructed that all agents should know to use `hermes-webhooks` on Vercel whenever Hermes needs to receive external webhooks, for example Shopify webhooks.

Canonical shape:

```text
External provider -> hermes-webhooks Vercel -> Hermes Gateway webhook route -> deterministic processor/agent -> Brain/receipt/output
```

Known project and URL:

- Local project: `/opt/data/hermes-webhooks`
- Primary public URL: `https://hermes-webhooks.vercel.app/webhooks/<route>`
- Custom domains are not canonical until verified end-to-end with the same provider-signed probe.

## Rule taught to agents

1. Prefer the maintained Vercel proxy for public webhook ingress instead of inventing n8n/Railway/Zapier/tunnels when `hermes-webhooks` can cover the provider class.
2. Keep provider-specific verification/normalization branches.
3. For Shopify, validate `X-Shopify-Hmac-Sha256` over the raw body at Vercel, preserve the body, map the topic into the event Hermes expects, then re-sign with the correct Hermes route secret.
4. Separate secrets by boundary: provider ingress secret, Hermes route signing secret, and Vercel/deploy token. Never print values.
5. Treat generic `202 accepted` as transport acceptance only. Business success requires deterministic response and downstream evidence such as ledger/receipt/state.
6. Deploys, env/secrets, upstream provider configuration, gateway restarts, and external writes still require current scoped approval with rollback and verification.

## Files updated

- `AGENTS.md` — boot-minimum rule for all Brain-operating agents.
- `areas/operacoes/rotinas/webhooks-to-brain.md` — canonical ingress workflow and guardrails.
- `skills/devops/webhook-subscriptions/SKILL.md` — reusable operational skill updated in local Hermes skills.
- Built-in memory — compact pointer added so future sessions remember the canonical default.

## Non-actions

- No Vercel deploy.
- No Vercel env/secret mutation.
- No Shopify webhook creation/update.
- No Hermes Gateway restart.
- No Docker/VPS/Traefik/runtime change.
- No external write.

## Verification result

- Brain health: PASS (`FAIL=0`, `WARN=0`), JSON `/tmp/brain-health-hermes-webhooks-vercel-final5-20260607.json`.
- Structural operating-layer audit: PASS (`rc=0`, stdout empty).
- Focused secret scan on changed artifacts: `0` hits.

Secret values do not appear in this receipt or related docs.
