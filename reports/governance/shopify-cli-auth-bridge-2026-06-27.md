# Shopify CLI auth bridge — 2026-06-27

## Status

- status: done
- request: adicionar auth da Shopify para uso CLI-first em Hermes
- values_printed: false
- external writes: 0
- Shopify writes/mutations: 0
- local secret persistence: removed/redacted after failed manual cache attempt

## What changed

Updated `/opt/data/scripts/hermes_cli_run.py` so Shopify has a governed auth path through the Hermes Doppler-first CLI wrapper:

1. Added Shopify env alias mapping:
   - `SHOPIFY_ACCESS_TOKEN` from `SHOPIFY_ACCESS_TOKEN`, `SHOPIFY_ADMIN_TOKEN`, or `SHOPIFY_API_TOKEN`.
   - `SHOPIFY_STORE` from `SHOPIFY_STORE`, `SHOPIFY_STORE_URL`, or `SHOPIFY_SHOP_NAME`.
2. Added redaction for Shopify token shapes (`shpat_`, `shpua_`, `shpca_`, `shptka_`) and `X-Shopify-Access-Token` headers.
3. Routed this common command shape:

```bash
hermes-cli-run shopify store execute --store lk-sneakerss.myshopify.com --json --query 'query { shop { name myshopifyDomain } }'
```

through the authenticated Hermes CLI wrapper:

```bash
shopify-admin-graphql --query '...'
```

This keeps the CLI-first operational surface while avoiding the interactive Shopify OAuth prompt in cron/runtime.

## Why not store official Shopify OAuth session now

`shopify store auth` requires an interactive browser callback. In this runtime it did not produce a usable non-interactive OAuth completion. A short-lived manual cache attempt was removed, and backup copies were redacted so no Shopify token remains in the Shopify CLI config cache.

The active auth path is therefore Doppler-first and process-scoped via `/opt/data/scripts/hermes_doppler.py` → `/opt/data/home/.local/bin/hermes-cli-run`.

## Verification

| Gate | Result |
|---|---:|
| `py_compile hermes_cli_run.py shopify_admin_graphql_cli.py` | OK |
| `hermes-cli-run shopify store execute ... shop { name myshopifyDomain }` | OK |
| Shopify domain readback | `lk-sneakerss.myshopify.com` |
| Mutation block through same route | OK (`mutation_blocked`) |
| Secret scan focused | 0 hits |
| Brain health | All checks passed |
| `git diff --check` | OK |

## Rollback

Restore previous `/opt/data/scripts/hermes_cli_run.py` from git/backups and remove only the Shopify routing/aliases. No external Shopify state was changed.
