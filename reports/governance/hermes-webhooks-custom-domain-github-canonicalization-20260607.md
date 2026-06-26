# Hermes Webhooks — custom domain preferred + GitHub canonical repo — 2026-06-07

## User direction

Lucas approved:

1. Use the custom domain for provider configuration.
2. Publish the proxy source to `https://github.com/lucascimino/hermes-webhook.git`.
3. Keep validating upstream provider configuration when activating providers.
4. Keep the rule that transport status is not business success.

## Documentation updates

Updated the canonical operational URL to:

```text
https://hermes-webhooks.lucascimino.com/webhooks/<route>
```

Kept the Vercel project URL as a technical alias:

```text
https://hermes-webhooks.vercel.app/webhooks/<route>
```

Updated references:

- Brain `AGENTS.md`
- Brain `areas/operacoes/rotinas/webhooks-to-brain.md`
- Local project README `/opt/data/hermes-webhooks/README.md`
- Skill `webhook-subscriptions`
- Evolution reconciliation runbook
- LK POS/Shopify addendum
- Boot memory pointer

## GitHub publication

Repository:

```text
https://github.com/lucascimino/hermes-webhook.git
```

Publication result:

- initialized local Git repo at `/opt/data/hermes-webhooks`
- committed versionable source only
- excluded `.vercel`, env files, and `node_modules`
- pushed `main`
- verified local HEAD equals remote `origin/main`

Remote facts verified through GitHub API:

- full name: `lucascimino/hermes-webhook`
- visibility: private
- default branch: `main`
- README present on remote

## Runtime verification

Health checks after documentation/repo publication:

- `https://hermes-webhooks.lucascimino.com/health` → `200 OK`, `Server: Vercel`, `platform=webhook`
- `https://hermes-webhooks.vercel.app/health` → `200 OK`, `Server: Vercel`, `platform=webhook`

Provider-signed no-op probes were already completed earlier in the same correction window:

- Shopify signed fake non-POS payload → `200 OK`, `status=ignored`, no alert/queue
- Evolution signed fake inbound/fromMe=false payload → `200 OK`, `matched=0`, `updated=0`

## Security verification

Focused versioned-source token-shape scan for `/opt/data/hermes-webhooks`:

- token-shaped secret hits: `0`

Secrets were fetched only in-process from Doppler and were not printed or committed.

## Remaining operational rule

Before considering a real provider live, verify the upstream admin/API points to the preferred custom domain and selected events, then validate deterministic downstream state/ledger/receipt. HTTP `200`/`202` alone is transport proof, not business success.
