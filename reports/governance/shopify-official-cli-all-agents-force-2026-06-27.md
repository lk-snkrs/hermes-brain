# Shopify official CLI forced across agents — 2026-06-27

## Status

- status: done
- request: force all agents to use the official Shopify CLI after interactive OAuth
- store: `lk-sneakerss.myshopify.com`
- values_printed: false
- Shopify writes/mutations: 0
- runtime/gateway/Docker/VPS restarts: 0

## Rule now enforced

For Shopify Admin GraphQL, Hermes agents, scripts and crons must use:

```bash
/opt/data/home/.local/bin/hermes-cli-run shopify store execute \
  --store lk-sneakerss.myshopify.com \
  --json \
  --query '<GraphQL>'
```

- `--allow-mutations` stays absent by default.
- Any Shopify mutation/write still requires scoped approval, rollback and readback.
- Legacy wrapper/raw Admin HTTP is not a normal path; if official OAuth breaks/expires, block and renew OAuth before continuing unless Lucas approves a specific incident exception.

## Surfaces updated

| Surface | Count |
|---|---:|
| Profile/root/Brain `AGENTS.md` + `SOUL.md` instruction files with policy | 59/59 |
| Cron registries validated | 11/11 |
| Shopify-related cron jobs with official CLI rule | 28/28 |
| Skill files patched with Shopify official CLI primary rule | 109 |
| Active enabled cron Shopify raw/wrapper gaps | 0 |

## Code changes

- `/opt/data/scripts/hermes_cli_run.py`
  - removed the forced route from `shopify store execute` to `shopify-admin-graphql`;
  - kept Shopify env aliasing/redaction;
  - `hermes-cli-run shopify store execute ...` now runs the official Shopify CLI path.
- `/opt/data/profiles/lk-stock/scripts/lk_shopify_sales_os_supabase_direct.py`
  - Shopify fetch now uses official CLI `shopify store execute`.
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/scripts/shopify_sales_os.py`
  - Shopify GraphQL helper now uses official CLI.
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/scripts/shopify_sales_analytics_enrich.py`
  - Shopify GraphQL helper now uses official CLI.
- `/opt/data/profiles/lk-growth/scripts/lk_growth_impact_review.py`
  - Shopify collection readback now uses official CLI.

## Verification

| Gate | Result |
|---|---:|
| Official Shopify CLI smoke | OK |
| Store readback | `lk-sneakerss.myshopify.com` |
| Official CLI mutation block | OK |
| `py_compile` touched Python files | OK |
| Cron JSON registries | 11/11 OK |
| Enabled cron Shopify raw/wrapper gaps | 0 |
| Changed-script secret scan | 0 hits |
| Brain health | All checks passed |
| `git diff --check` | OK |

## Backup

Backup directory:

`/opt/data/backups/shopify-official-cli-force-20260627T151833Z`

## Notes

- No Shopify data mutation was executed.
- No gateway/profile runtime restart was done; instruction/runtime behavior will apply to new agent/cron runs through file context and cron prompts.
- The official Shopify CLI OAuth token remains in the official local Shopify CLI config cache with local permissions hardened to `0600`; token value was not printed.
