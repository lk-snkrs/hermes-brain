# Fase 1 — Hermes Central Integration Auth Broker — inventory e drift report — 2026-06-28

- Criado em: 2026-06-28T14:56:47Z
- Escopo: backup local + inventory/smoke read-only + drift scan
- External writes: 0
- values_printed: false

## Backup

- Source: `/opt/data/scripts/hermes_cli_run.py`
- Backup: `/opt/data/backups/hermes-cli-run-pre-auth-broker-20260628T145647Z.py`
- Source sha256: `be5479b1621d12bd8e87c0e84a772b2d0792108ddb4d5be3287c181f00bd7117`
- Backup sha256: `be5479b1621d12bd8e87c0e84a772b2d0792108ddb4d5be3287c181f00bd7117`

## Inventory/smoke commands

### inventory
- Command: `/opt/data/home/.local/bin/hermes-cli-integrations inventory`
- Exit code: `0`
- Stdout sanitizado:
```text
{
  "items": [
    {
      "commands": {
        "vercel": true
      },
      "name": "vercel",
      "notes": "map VERCEL_API_TOKEN -> VERCEL_TOKEN for CLI",
      "secret_names_present": [
        "VERCEL_API_TOKEN",
        "VERCEL_API_TOKEN_LUCASCIMINO"
      ],
      "values_printed": false
    },
    {
      "commands": {
        "gws": true
      },
      "name": "google_workspace",
      "notes": "gws installed; Doppler OAuth fallback available",
      "secret_names_present": [
        "GMAIL_CLIENT_ID",
        "GMAIL_CLIENT_SECRET",
        "GMAIL_REFRESH_TOKEN",
        "GMAIL_LUCAS_REFRESH_TOKEN"
      ],
      "values_printed": false
    },
    {
      "commands": {
        "ntn": true
      },
      "name": "notion",
      "notes": "map NOTION_API_KEY -> NOTION_TOKEN if needed",
      "secret_names_present": [
        "NOTION_API_KEY",
        "NOTION_TOKEN_LK",
        "NOTION_TOKEN_ZPR"
      ],
      "values_printed": false
    },
    {
      "commands": {
        "lin": true
      },
      "name": "linear",
      "notes": "missing secret blocks auth",
      "secret_names_present": [
        "LINEAR_API_KEY"
      ],
      "values_printed": false
    },
    {
      "commands": {
        "sentry-cli": true
      },
      "name": "sentry",
      "notes": "missing secret blocks auth",
      "secret_names_present": [
        "SENTRY_AUTH_TOKEN"
      ],
      "values_printed": false
    },
    {
      "commands": {
        "supabase": true
      },
      "name": "supabase",
      "notes": "management CLI uses SUPABASE_ACCESS_TOKEN",
      "secret_names_present": [
        "SUPABASE_ACCESS_TOKEN",
        "SUPABASE_LK_URL",
        "SUPABASE_LK_SERVICE_KEY"
      ],
      "values_printed": false
    },
    {
      "commands": {
        "wrangler": true
      },
      "name": "cloudflare_wrangler",
      "notes": "verify scope before DNS/workers writes",
      "secret_names_present": [
        "CLOUDFLARE_API_TOKEN",
        "CF_API_TOKEN",
        "CF_R2_API_TOKEN"
      ],
      "values_printed": false
    },
    {
      "commands": {
        "gh": true
      },
      "name": "github",
      "notes": "use env token for gh/api noninteractive",
      "secret_names_present": [
        "GITHUB_TOKEN",
        "GITHUB_TOKEN_LUCASCIMINO"
      ],
      "values_printed": false
    },
    {
      "commands": {
        "shopify": true
      },
      "name": "shopify_lk",
      "notes": "Admin API read-only smoke",
      "secret_names_present": [
        "SHOPIFY_STORE",
        "SHOPIFY_STORE_URL",
        "SHOPIFY_ACCESS_TOKEN",
        "SHOPIFY_ADMIN_TOKEN"
      ],
      "values_printed": false
    },
    {
      "commands": {
        "klaviyo": true
      },
      "name": "klaviyo",
      "notes": "API read-only smoke",
      "secret_names_present": [
        "KLAVIYO_API_KEY"
      ],
      "values_printed": false
    }
  ],
  "values_printed": false
}
```

### smoke_selected
- Command: `/opt/data/home/.local/bin/hermes-cli-integrations smoke shopify_lk github notion google_workspace klaviyo supabase`
- Exit code: `0`
- Stdout sanitizado:
```text
{
  "results": {
    "github": {
      "method": "gh_api",
      "rc": 0,
      "status": "ok"
    },
    "google_workspace": {
      "method": "gws_gmail_users_getProfile",
      "rc": 2,
      "status": "failed"
    },
    "klaviyo": {
      "method": "klaviyo_get_flows_stdout",
      "rc": 124,
      "status": "failed"
    },
    "notion": {
      "method": "ntn_whoami",
      "rc": 0,
      "status": "ok"
    },
    "shopify_lk": {
      "method": "shopify_store_execute",
      "rc": 0,
      "status": "ok"
    },
    "supabase": {
      "project_count": null,
      "rc": 0,
      "status": "ok"
    }
  },
  "values_printed": false
}
```

## Drift summary

- Total matches: 209
- direct_login_auth_drift_candidate: 42
- historical_or_governance_evidence: 48
- legacy_fallback_or_drift_candidate: 36
- needs_review: 83

## Matches sanitizados
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/skills/software-development/runtime-profile-map/SKILL.md:22` — For all-agent CLI/MCP coverage audits, remember that “policy propagated” is not “runtime migrated”: after checking profile-local `AGENTS.md`/`SOUL.md`, also inventory CLIs through Hermes wrapper PATH, smoke MCPs/read-onl…
- `needs_review` `shopify_access_token_ref` — `/opt/data/skills/devops/webhook-subscriptions/scripts/shopify_hmac_candidate_probe.py:28` — "SHOPIFY_ACCESS_TOKEN",
- `historical_or_governance_evidence` `mcp_login` — `/opt/data/skills/devops/lucas-runtime-operations/references/central-integration-auth-broker-prd-20260628.md:24` — - MCP OAuth HTTP tokens are cached under `~/.hermes/mcp-tokens/<server>.json`; direct MCP login per profile can duplicate auth state unless ownership is centralized.
- `direct_login_auth_drift_candidate` `shopify_login` — `/opt/data/skills/devops/lucas-runtime-operations/references/central-integration-auth-broker-prd-20260628.md:38` — 6. Acceptance criteria: agents never run `shopify login`/`shopify store auth`/`hermes mcp login` individually unless an approved exception; `values_printed=false`; mutations blocked without approval.
- `direct_login_auth_drift_candidate` `shopify_login` — `/opt/data/skills/devops/lucas-runtime-operations/references/central-integration-auth-broker-prd-20260628.md:54` — shopify login
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/skills/devops/lucas-runtime-operations/references/central-integration-auth-broker-prd-20260628.md:55` — shopify store auth
- `direct_login_auth_drift_candidate` `hermes_mcp_login` — `/opt/data/skills/devops/lucas-runtime-operations/references/central-integration-auth-broker-prd-20260628.md:56` — hermes mcp login
- `historical_or_governance_evidence` `mcp_login` — `/opt/data/skills/devops/lucas-runtime-operations/references/central-integration-auth-broker-prd-20260628.md:57` — mcp login
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/skills/devops/lucas-runtime-operations/references/central-integration-auth-broker-prd-20260628.md:58` — SHOPIFY_ACCESS_TOKEN
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/skills/devops/lucas-runtime-operations/references/central-integration-auth-broker-prd-20260628.md:59` — shopify-admin-graphql
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/skills/devops/doppler-secrets-operations/SKILL.md:26` — - `references/shopify-auth-doppler-cli-bridge-20260627.md` — Shopify cron/runtime auth bridge: distinguish Doppler secret presence, Hermes CLI env alias injection, and official Shopify CLI OAuth; use Doppler-first CLI br…
- `needs_review` `shopify_access_token_ref` — `/opt/data/skills/devops/doppler-secrets-operations/SKILL.md:159` — - `OK SHOPIFY_ACCESS_TOKEN`
- `needs_review` `shopify_access_token_ref` — `/opt/data/skills/devops/doppler-secrets-operations/references/shopify-auth-doppler-cli-bridge-20260627.md:5` — 1. **Secret exists in Doppler** — e.g. `SHOPIFY_ACCESS_TOKEN`, `SHOPIFY_ADMIN_TOKEN`, `SHOPIFY_API_TOKEN`, plus store names.
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/skills/devops/doppler-secrets-operations/references/shopify-auth-doppler-cli-bridge-20260627.md:7` — 3. **Official CLI OAuth is stored** — `shopify store auth list --json` and `shopify store execute` succeed without the Hermes bridge.
- `needs_review` `shopify_access_token_ref` — `/opt/data/skills/devops/doppler-secrets-operations/references/shopify-auth-doppler-cli-bridge-20260627.md:15` — - target `SHOPIFY_ACCESS_TOKEN` from `SHOPIFY_ACCESS_TOKEN`, `SHOPIFY_ADMIN_TOKEN`, `SHOPIFY_API_TOKEN`;
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/skills/devops/doppler-secrets-operations/references/shopify-auth-doppler-cli-bridge-20260627.md:22` — A headless `shopify store auth --store ... --scopes ...` can hang waiting for browser/callback. Do not persist a Doppler Shopify token manually into `~/.config/shopify-cli-store-nodejs/config.json` as a durable workaroun…
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/skills/mcp/mcp-connections/SKILL.md:36` — - Prefer official/approved CLI or Hermes wrapper first for integrations when a governed CLI path exists. For LK Sneakers Shopify Admin GraphQL specifically, official OAuth is configured and the primary path is `/opt/data…
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/skills/productivity/lk-operational-intelligence/SKILL.md:430` — `shopify-admin-graphql` is fallback only if official OAuth is broken/expired. Do not use raw Admin HTTP (`urllib`/`requests`/`curl`) for Shopify. Keep `--allow-mutations` absent unless Lucas approves an exact write with …
- `needs_review` `shopify_access_token_ref` — `/opt/data/skills/productivity/lk-operational-intelligence/references/lk-shopify-pos-daily-store-sales-query-20260626.md:45` — secrets={k:os.environ.get(k,'') for k in ['SHOPIFY_STORE_URL','SHOPIFY_ACCESS_TOKEN']}
- `needs_review` `shopify_access_token_ref` — `/opt/data/skills/productivity/lk-operational-intelligence/references/lk-theme-production-publish-admin-api-20260515.md:19` — - Secret names: `SHOPIFY_STORE_URL`, `SHOPIFY_ACCESS_TOKEN`.
- `needs_review` `shopify_access_token_ref` — `/opt/data/skills/productivity/lk-operational-intelligence/references/lk-theme-mega-menu-all-models-link-20260515.md:37` — - fetch `SHOPIFY_STORE_URL` and `SHOPIFY_ACCESS_TOKEN` from Doppler/local token without printing secrets
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/skills/productivity/lk-operational-intelligence/references/absorbed-lk-content-operations/SKILL.md:174` — `shopify-admin-graphql` is fallback only if official OAuth is broken/expired. Do not use raw Admin HTTP (`urllib`/`requests`/`curl`) for Shopify. Keep `--allow-mutations` absent unless Lucas approves an exact write with …
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/skills/productivity/lk-operational-intelligence/references/absorbed-lk-gmc-operations/SKILL.md:107` — `shopify-admin-graphql` is fallback only if official OAuth is broken/expired. Do not use raw Admin HTTP (`urllib`/`requests`/`curl`) for Shopify. Keep `--allow-mutations` absent unless Lucas approves an exact write with …
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/skills/productivity/lk-operational-intelligence/references/absorbed-lk-report-delivery/SKILL.md:182` — `shopify-admin-graphql` is fallback only if official OAuth is broken/expired. Do not use raw Admin HTTP (`urllib`/`requests`/`curl`) for Shopify. Keep `--allow-mutations` absent unless Lucas approves an exact write with …
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/skills/productivity/shopify/SKILL.md:69` — Use `--variables '{...}'` for variables and `--version <api-version>` when pinning API versions. Keep `--allow-mutations` absent by default; any mutation/write requires explicit scoped approval, rollback, and readback. `…
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/skills/productivity/shopify/SKILL.md:98` — `shopify-admin-graphql` is fallback only if official OAuth is broken/expired. Do not use raw Admin HTTP (`urllib`/`requests`/`curl`) for Shopify. Keep `--allow-mutations` absent unless Lucas approves an exact write with …
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/skills/productivity/shopify/references/shopify-official-cli-all-agents-propagation-20260627.md:21` — - If `hermes_cli_run.py` contains a route that rewrites `shopify store execute` into a custom wrapper such as `shopify-admin-graphql`, remove/disable that route after official OAuth is validated.
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/skills/productivity/shopify/references/shopify-official-cli-all-agents-propagation-20260627.md:26` — - Replace custom wrapper calls like `shopify-admin-graphql` in active code paths with official CLI.
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/skills/productivity/shopify/references/shopify-official-cli-all-agents-propagation-20260627.md:37` — - Scan enabled crons and active scripts for `shopify-admin-graphql`, `X-Shopify-Access-Token`, and `/admin/api/.../graphql` in Shopify paths.
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/skills/productivity/shopify/references/shopify-official-cli-all-agents-propagation-20260627.md:47` — After OAuth succeeds, a compatibility bridge that transparently routes `hermes-cli-run shopify store execute` to `shopify-admin-graphql` becomes counterproductive: agents appear to use the official CLI but are still on w…
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/skills/productivity/shopify/references/shopify-cli-interactive-oauth-handoff-20260627.md:3` — Use this reference when Lucas explicitly asks to proceed with official `shopify store auth` instead of the Doppler-first wrapper bridge.
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/skills/productivity/shopify/references/shopify-cli-interactive-oauth-handoff-20260627.md:7` — The official Shopify CLI `shopify store auth` flow starts a local callback server on `127.0.0.1:13387/auth/callback` and expects a browser on the same machine to complete OAuth. In Hermes/Telegram, the user opens the aut…
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/skills/productivity/shopify/references/shopify-cli-interactive-oauth-handoff-20260627.md:16` — shopify store auth --store lk-sneakerss.myshopify.com \
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/skills/productivity/shopify/references/shopify-cli-interactive-oauth-handoff-20260627.md:48` — shopify store auth list --json --no-color
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/skills/productivity/shopify/references/shopify-cli-interactive-oauth-handoff-20260627.md:58` — - Do not persist Doppler admin tokens into Shopify CLI cache files as a substitute for OAuth. If a manual cache experiment was attempted, remove/redact it and keep the supported fallback as the Doppler-first `shopify-adm…
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/skills/productivity/shopify/references/shopify-cli-interactive-oauth-handoff-20260627.md:64` — If interactive OAuth cannot be completed, use the existing Doppler-first CLI bridge: `hermes-cli-run shopify store execute ...` routed through `shopify-admin-graphql`, with mutations blocked by default.
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/skills/productivity/shopify/references/shopify-official-cli-all-agents-force-20260627.md:5` — Use this reference when Lucas asks to make Hermes agents/scripts/crons use Shopify through CLI instead of raw Admin API, or when a Shopify Admin GraphQL helper still points at `shopify-admin-graphql`, `urllib`, `requests…
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/skills/productivity/shopify/references/shopify-official-cli-all-agents-force-20260627.md:24` — 3. Legacy Hermes `shopify-admin-graphql` wrapper only as an incident fallback if official OAuth breaks/expires and Lucas approves continuing instead of renewing OAuth.
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/skills/productivity/shopify/references/shopify-official-cli-all-agents-force-20260627.md:37` — - replace `shopify-admin-graphql` with `hermes-cli-run shopify store execute`;
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/skills/productivity/shopify/references/shopify-official-cli-all-agents-force-20260627.md:40` — - `shopify store auth list --json` or official smoke query;
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/skills/productivity/shopify/references/shopify-official-cli-all-agents-force-20260627.md:50` — - Do not keep a hidden route in `hermes-cli-run` that silently rewrites `shopify store execute` to `shopify-admin-graphql`; after OAuth, the user-facing command must execute the official Shopify CLI path.
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/skills/productivity/shopify/references/shopify-cli-auth-bridge-20260627.md:19` — shopify-admin-graphql --query '...'
- `needs_review` `shopify_access_token_ref` — `/opt/data/skills/productivity/shopify/references/shopify-cli-auth-bridge-20260627.md:24` — - get `SHOPIFY_ACCESS_TOKEN` from Doppler-injected aliases (`SHOPIFY_ACCESS_TOKEN`, `SHOPIFY_ADMIN_TOKEN`, `SHOPIFY_API_TOKEN`);
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/skills/productivity/shopify/references/shopify-cli-auth-bridge-20260627.md:30` — ## Pitfall: official `shopify store auth`
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/skills/productivity/shopify/references/shopify-cli-auth-bridge-20260627.md:32` — `shopify store auth --store ... --scopes ...` stores an online OAuth session, but it requires an interactive browser/callback. In a headless Hermes cron/runtime this may hang or fail to complete. Do not claim official st…
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/skills/productivity/lk-seo-weekly-improvement/SKILL.md:370` — `shopify-admin-graphql` is fallback only if official OAuth is broken/expired. Do not use raw Admin HTTP (`urllib`/`requests`/`curl`) for Shopify. Keep `--allow-mutations` absent unless Lucas approves an exact write with …
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/skills/productivity/lk-seo-weekly-improvement/references/shopify-seo-execution-20260511.md:9` — - Use Doppler `lc-keys/prd` for `SHOPIFY_STORE_URL` and `SHOPIFY_ACCESS_TOKEN`; never print values.
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/skills/productivity/lk-seo-weekly-improvement/references/approved-p1-seo-fields-execution-20260511.md:17` — - Use Doppler `lc-keys/prd` secrets in process only: `SHOPIFY_STORE_URL`, `SHOPIFY_ACCESS_TOKEN`.
- `needs_review` `shopify_access_token_ref` — `/opt/data/skills/productivity/lk-shopify-readonly/SKILL.md:38` — - `SHOPIFY_ACCESS_TOKEN`
- `needs_review` `shopify_access_token_ref` — `/opt/data/skills/productivity/lk-shopify-readonly/SKILL.md:40` — Known historical detail: older docs mention `SHOPIFY_ACCESS_TOKEN` as the correct token name, not `SHOPIFY_API_TOKEN`. If both exist, prefer `SHOPIFY_ACCESS_TOKEN` unless Lucas/Brain says otherwise.
- `needs_review` `shopify_access_token_ref` — `/opt/data/skills/productivity/lk-shopify-readonly/SKILL.md:45` — /opt/data/hermes_bruno_ingest/hermes_doppler.sh exists SHOPIFY_STORE_URL SHOPIFY_ACCESS_TOKEN
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/skills/productivity/lk-shopify-readonly/SKILL.md:75` — TOKEN=[REDACTED] secrets get SHOPIFY_ACCESS_TOKEN -p lc-keys -c prd --plain)"
- `needs_review` `shopify_access_token_ref` — `/opt/data/skills/productivity/lk-shopify-readonly/SKILL.md:315` — 1. **Wrong token name.** Use `SHOPIFY_ACCESS_TOKEN`, not the historical mistaken `SHOPIFY_API_TOKEN` unless confirmed.
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/skills/productivity/lk-shopify-readonly/SKILL.md:355` — `shopify-admin-graphql` is fallback only if official OAuth is broken/expired. Do not use raw Admin HTTP (`urllib`/`requests`/`curl`) for Shopify. Keep `--allow-mutations` absent unless Lucas approves an exact write with …
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/skills/productivity/lk-shopify-product-upload/SKILL.md:430` — `shopify-admin-graphql` is fallback only if official OAuth is broken/expired. Do not use raw Admin HTTP (`urllib`/`requests`/`curl`) for Shopify. Keep `--allow-mutations` absent unless Lucas approves an exact write with …
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/TOOLS.md:35` — **API Key:** Doppler (`SHOPIFY_ACCESS_TOKEN`)
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/TOOLS.md:46` — -H "X-Shopify-Access-Token: [REDACTED] secrets get SHOPIFY_ACCESS_TOKEN --plain)"
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-roas-influencer-correction-readonly-2026-05-10.json:12` — "SHOPIFY_ACCESS_TOKEN": true,
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/reports/cwc-vs-hermes-analysis.md:539` — | Shopify LK | ✅ Ativo | E-commerce, produtos, pedidos | `SHOPIFY_ACCESS_TOKEN` |
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/reports/cwc-vs-hermes-analysis.md:799` — **API Key:** Doppler (SHOPIFY_ACCESS_TOKEN)
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/hermes_bruno_ingest/hermes-brain/reports/daily-consolidation/2026-06-28.md:162` — | Shopify Admin GraphQL deve usar CLI oficial `hermes-cli-run shopify store execute`; wrapper só fallback/incidente | Skills Shopify/LK Shopify/LK Growth/LK Stock + AGENTS/profile prompts | Aplicado em docs/perfis/script…
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/hermes_bruno_ingest/hermes-brain/reports/daily-consolidation/2026-06-28-handoff.json:66` — "verification_needed": "Search ativo por shopify-admin-graphql/raw Admin HTTP em jobs enabled."
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/hermes_bruno_ingest/hermes-brain/reports/daily-consolidation/latest-handoff.json:66` — "verification_needed": "Search ativo por shopify-admin-graphql/raw Admin HTTP em jobs enabled."
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/shopify-official-cli-all-agents-force-2026-06-27.md:40` — - removed the forced route from `shopify store execute` to `shopify-admin-graphql`;
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/shopify-cli-auth-bridge-2026-06-27.md:17` — - `SHOPIFY_ACCESS_TOKEN` from `SHOPIFY_ACCESS_TOKEN`, `SHOPIFY_ADMIN_TOKEN`, or `SHOPIFY_API_TOKEN`.
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/shopify-cli-auth-bridge-2026-06-27.md:29` — shopify-admin-graphql --query '...'
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/shopify-cli-auth-bridge-2026-06-27.md:36` — `shopify store auth` requires an interactive browser callback. In this runtime it did not produce a usable non-interactive OAuth completion. A short-lived manual cache attempt was removed, and backup copies were redacted…
- `direct_login_auth_drift_candidate` `shopify_login` — `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/hermes-central-integration-auth-broker-prd-2026-06-28.md:68` — 4. Impedir que agents façam `shopify login`, `hermes mcp login`, OAuth ou cópia de token por conta própria fora de exceção aprovada.
- `historical_or_governance_evidence` `mcp_login` — `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/hermes-central-integration-auth-broker-prd-2026-06-28.md:174` — 3. **MCP login por profile:** só por exceção documentada quando a integração é realmente profile-specific.
- `direct_login_auth_drift_candidate` `hermes_mcp_login` — `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/hermes-central-integration-auth-broker-prd-2026-06-28.md:178` — - Não fazer `hermes mcp login <server>` em cada agente como rotina normal.
- `direct_login_auth_drift_candidate` `shopify_login` — `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/hermes-central-integration-auth-broker-prd-2026-06-28.md:240` — shopify login
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/hermes-central-integration-auth-broker-prd-2026-06-28.md:241` — shopify store auth
- `direct_login_auth_drift_candidate` `hermes_mcp_login` — `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/hermes-central-integration-auth-broker-prd-2026-06-28.md:242` — hermes mcp login <server>
- `historical_or_governance_evidence` `mcp_login` — `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/hermes-central-integration-auth-broker-prd-2026-06-28.md:325` — - Procurar uso de login direto, raw Shopify Admin HTTP e `mcp login` em scripts/skills/crons/prompts.
- `direct_login_auth_drift_candidate` `shopify_login` — `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/hermes-central-integration-auth-broker-prd-2026-06-28.md:399` — 2. Bloquear hard `shopify login/store auth` no wrapper ou apenas em policy/lint inicialmente?
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/cli-mcp-active-cron-fix-2026-06-27.md:56` — - symlink: `/opt/data/home/.local/bin/shopify-admin-graphql`
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/cli-mcp-active-cron-fix-2026-06-27.md:64` — - `hermes-cli-run shopify-admin-graphql` wrapper surface;
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/shopify-official-oauth-2026-06-27.md:7` — - method: official `shopify store auth`
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/shopify-official-oauth-2026-06-27.md:17` — | `shopify store auth list --json` | 1 session |
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/empresa/gestao/licoes.md:16` — - Shopify: `SHOPIFY_ACCESS_TOKEN` (não `SHOPIFY_API_TOKEN`)
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/empresa/integracoes/shopify.md:10` — - `SHOPIFY_ACCESS_TOKEN`
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/empresa/decisoes/2026-03.md:104` — - Token correto: `SHOPIFY_ACCESS_TOKEN` (não `SHOPIFY_API_TOKEN`)
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/empresa/decisoes/decisoes-permanentes.md:25` — | Token Doppler | `SHOPIFY_ACCESS_TOKEN` (não `SHOPIFY_API_TOKEN`) |
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/memories/lessons.md:16` — - Shopify: `SHOPIFY_ACCESS_TOKEN` (não `SHOPIFY_API_TOKEN`)
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/memories/lk.md:50` — | Shopify | Ativo | `SHOPIFY_ACCESS_TOKEN` |
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/memories/decisions.md:25` — | Token Doppler | `SHOPIFY_ACCESS_TOKEN` (não `SHOPIFY_API_TOKEN`) |
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/receipts/shopify-official-oauth-20260627.md:10` — - Callback OAuth informado por Lucas; shopify store auth list; shopify store execute read-only query.
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/receipts/shopify-official-oauth-20260627.md:19` — - Rollback/mitigação: Rodar shopify store auth logout/remover sessão local do Shopify CLI se necessário; sem estado Shopify externo alterado.
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/receipts/cli-mcp-active-cron-fix-20260627.md:12` — - LK Stock Supabase cron convertido para gate readback via hermes-cli-run supabase db query --linked; Shopify Sales OS e analytics convertidos para wrapper CLI shopify-admin-graphql; skill/AGENTS LK Stock corrigidos para…
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/receipts/cli-mcp-active-cron-fix-20260627.md:19` — - Rollback/mitigação: Restaurar arquivos de /opt/data/backups/cli-mcp-active-cron-fix-20260627T132053Z e remover symlink /opt/data/home/.local/bin/shopify-admin-graphql se necessário.
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/receipts/shopify-official-cli-all-agents-force-20260627.md:12` — - Propagada regra Shopify official CLI first para 59 instruction files, 28 cron jobs e skills relevantes; removido route hermes-cli-run shopify store execute -> shopify-admin-graphql; scripts ativos Shopify migrados para…
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/receipts/shopify-cli-auth-bridge-20260627.md:10` — - Doppler lc-keys/prd via hermes_doppler.py; hermes-cli-run; shopify-admin-graphql wrapper; smoke read-only Shopify shop query.
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/receipts/shopify-cli-auth-bridge-20260627.md:18` — - Riscos/bloqueios: Shopify store auth OAuth oficial continua exigindo browser/callback interativo; ponte atual usa Doppler-first process scoped auth.
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/rotinas/shopify-readonly-sync.md:8` — - Secrets: `SHOPIFY_STORE_URL`, `SHOPIFY_ACCESS_TOKEN`.
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/rotinas/shopify-readonly-sync.md:20` — 1. Confirmar secrets com `hermes_doppler.sh exists SHOPIFY_STORE_URL SHOPIFY_ACCESS_TOKEN`.
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/approval-packets/hermes-webhooks-shopify-route-secret-alignment-20260624.md:19` — 4. Probes assinados com candidatos errados (`SHOPIFY_ADMIN_TOKEN`, `SHOPIFY_API_TOKEN`, `SHOPIFY_ACCESS_TOKEN`) foram rejeitados pela Vercel com `invalid_shopify_signature`.
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/reports/hermes-webhooks-shopify-signature-reconciliation-20260624.md:55` — | `SHOPIFY_ACCESS_TOKEN` | Vercel rejeita `invalid_shopify_signature` |
- `direct_login_auth_drift_candidate` `shopify_login` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/implementation-plans/hermes-central-integration-auth-broker-2026-06-28.md:66` — shopify login
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/implementation-plans/hermes-central-integration-auth-broker-2026-06-28.md:68` — shopify store auth
- `direct_login_auth_drift_candidate` `hermes_mcp_login` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/implementation-plans/hermes-central-integration-auth-broker-2026-06-28.md:69` — hermes mcp login
- `direct_login_auth_drift_candidate` `shopify_login` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/implementation-plans/hermes-central-integration-auth-broker-2026-06-28.md:148` — shopify login
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/implementation-plans/hermes-central-integration-auth-broker-2026-06-28.md:149` — shopify store auth
- `direct_login_auth_drift_candidate` `hermes_mcp_login` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/implementation-plans/hermes-central-integration-auth-broker-2026-06-28.md:150` — hermes mcp login
- `needs_review` `mcp_login` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/implementation-plans/hermes-central-integration-auth-broker-2026-06-28.md:151` — mcp login
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/implementation-plans/hermes-central-integration-auth-broker-2026-06-28.md:152` — SHOPIFY_ACCESS_TOKEN
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/implementation-plans/hermes-central-integration-auth-broker-2026-06-28.md:153` — shopify-admin-graphql
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/contexto/ferramentas.md:24` — - `SHOPIFY_ACCESS_TOKEN`
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/contexto/geral.md:47` — | Shopify | Ativo | `SHOPIFY_ACCESS_TOKEN` |
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/rotinas/morning-briefing.md:18` — - `SHOPIFY_ACCESS_TOKEN` se consultar Shopify
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/rotinas/data-spine-readonly-2026-05-11.md:99` — - OK `SHOPIFY_ACCESS_TOKEN`.
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/AGENTS.md:7` — Não executar `shopify store auth --verbose` nem comandos Shopify CLI em modo verbose quando houver risco de telemetria imprimir `env_shopify_variables`, tokens, webhook secrets ou qualquer secret. Para capturar URL OAuth…
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/CONNECTORS-READONLY-INVENTORY.md:20` — - Segredos usados sem exposição: `SHOPIFY_STORE_URL`/`SHOPIFY_STORE` e `SHOPIFY_ACCESS_TOKEN`/`SHOPIFY_ADMIN_TOKEN`.
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/handoffs/handoff-runtime-tools-lk-growth-shopify-browser-2026-05-27.md:54` — - Nunca imprimir `SHOPIFY_ACCESS_TOKEN` ou credenciais Doppler.
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/handoffs/handoff-runtime-tools-lk-growth-shopify-browser-2026-05-27.md:66` — - `SHOPIFY_ACCESS_TOKEN`
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/semrush-technical-fix-20260627T1715Z/RECEIPT.md:70` — Durante a sessão anterior, Shopify CLI verbose expôs variáveis sensíveis no output de background. Regra adicionada ao Brain para não usar `shopify store auth --verbose`; capturar OAuth URL via `BROWSER` wrapper sem verbo…
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-production/block-b-schema-asics-nb740-20260627T1705Z/RECEIPT.md:97` — - regra adicionada ao `AGENTS.md`: não usar `shopify store auth --verbose`; capturar OAuth URL com wrapper `BROWSER` simples;
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-cli-oauth-readback-block-a-20260627T162047Z/RECEIPT.md:15` — /opt/data/home/.local/bin/hermes-cli-run shopify store auth --help
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-cli-oauth-readback-block-a-20260627T162047Z/RECEIPT.md:23` — /opt/data/home/.local/bin/hermes-cli-run shopify store auth   --store lk-sneakerss.myshopify.com   --scopes read_products,read_content,read_themes,read_metaobjects --json
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-cli-oauth-readback-block-a-20260627T162047Z/RECEIPT.md:31` — /opt/data/home/.local/bin/hermes-cli-run shopify store auth   --store lk-sneakerss.myshopify.com   --scopes read_products,read_content,read_themes,read_metaobjects
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-cli-oauth-readback-block-a-20260627T162047Z/RECEIPT.md:39` — /opt/data/home/.local/bin/hermes-cli-run shopify store auth   --store lk-sneakerss.myshopify.com   --scopes read_products,read_content,read_themes,read_metaobjects --verbose
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-cli-oauth-readback-block-a-20260627T162047Z/RECEIPT.md:58` — Resultado sanitizado: CLI `shopify=true`; secrets Shopify presentes por nome (`SHOPIFY_STORE`, `SHOPIFY_STORE_URL`, `SHOPIFY_ACCESS_TOKEN`, `SHOPIFY_ADMIN_TOKEN`); `values_printed=false`.
- `direct_login_auth_drift_candidate` `shopify_store_auth` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-cli-oauth-readback-block-a-20260627T162047Z/RECEIPT.md:87` — 1. **Preferida:** Lucas/Hermes interativo completar `shopify store auth` oficial para `lk-sneakerss.myshopify.com` com escopos read-only. Depois Growth retoma Admin/theme readback.
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/receipt-judgeme-whatsapp-review-inspection-20260613.md:25` — - `SHOPIFY_ACCESS_TOKEN`: OK
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/receipts/lk-pos-postpurchase-shopify-hmac-correction-packet-2026-06-09.md:17` — "SHOPIFY_ACCESS_TOKEN": {"exists": true, "len": 38},
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/receipts/lk-pos-postpurchase-shopify-webhook-401-hmac-investigation-2026-06-09.md:85` — - `SHOPIFY_ACCESS_TOKEN`: presente
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/receipts/lk-recovery-os-audit-20260603-0024z.md:103` — - `SHOPIFY_ACCESS_TOKEN`
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/receipts/lk-recovery-os-incident-not-working-20260603-1338z.md:65` — - `SHOPIFY_ACCESS_TOKEN`
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/receipts/lk-recovery-os-incident-not-working-20260603-1338z.md:71` — - `SHOPIFY_ACCESS_TOKEN` → `orders.json`: HTTP 404
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/receipts/lk-recovery-os-incident-not-working-20260603-1338z.md:75` — Conclusão provável: o Worker usa `SHOPIFY_ACCESS_TOKEN`, mas o token válido para recheck de orders no Doppler é `SHOPIFY_ADMIN_TOKEN`. Sem corrigir o secret usado pelo Worker, o T1 falha fechado.
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/receipts/lk-recovery-os-incident-not-working-20260603-1338z.md:93` — 1. Atualizar secret de produção do Worker `SHOPIFY_ACCESS_TOKEN` para o valor válido de `SHOPIFY_ADMIN_TOKEN` do Doppler, sem expor valor.
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/receipts/lk-recovery-os-shopify-correct-recheck-fallback-local-20260603-1350z.md:21` — O achado anterior contra Doppler não deve ser comunicado como “Shopify errado”. A formulação correta é: **o Worker estava rígido demais em um único secret/env (`SHOPIFY_ACCESS_TOKEN`) e não tentava o token admin alternat…
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/receipts/lk-recovery-os-shopify-correct-recheck-fallback-local-20260603-1350z.md:37` — 1. `SHOPIFY_ACCESS_TOKEN`
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/receipts/lk-recovery-os-shopify-correct-recheck-fallback-local-20260603-1350z.md:46` — - `falls back to SHOPIFY_ADMIN_TOKEN when SHOPIFY_ACCESS_TOKEN cannot read orders`
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/receipts/lk-recovery-os-shopify-recheck-fallback-deploy-20260603-1411z.md:26` — 1. `SHOPIFY_ACCESS_TOKEN`
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/receipts/lk-recovery-os-shopify-recheck-fallback-deploy-20260603-1411z.md:40` — - teste de fallback quando `SHOPIFY_ACCESS_TOKEN` falha e `SHOPIFY_ADMIN_TOKEN` lê orders.
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/receipts/shopify-pos-restock-webhook-verification-20260609.md:13` — - `SHOPIFY_ACCESS_TOKEN`: present
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/receipts/lk-recovery-os-superpowers-readonly-audit-20260603-0051z.md:107` — - `SHOPIFY_ACCESS_TOKEN`
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/reports/lk-pos-restock-exception-monitor-fix-20260627.md:30` — - `ensure_doppler()` exige `SHOPIFY_ACCESS_TOKEN` + `HERMES_WEBHOOK_SECRET` para o monitor local.
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/receipts/lk-shopify-sales-os-token-nameerror-autoheal-20260628.md:12` — - Corrigido bug local NameError: removida chamada a token() inexistente no caminho migrado para Shopify CLI oficial; mantida checagem de presença de SHOPIFY_ACCESS_TOKEN sem imprimir valor; backup criado antes da edição.
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/handoffs/2026-06-26-new-balance-740-publicability-shopify-readonly-result.md:4` — - Fonte viva consultada: Shopify Admin GraphQL read-only em 2026-06-26T09:20Z; public readback HTTP em `lksneakers.com.br`; Doppler `lc-keys/prd` injetou `SHOPIFY_STORE_URL` e `SHOPIFY_ACCESS_TOKEN` sem imprimir valores …
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/handoffs/2026-06-26-new-balance-740-publicability-collection-request.md:4` — - Fonte viva consultada: Shopify Admin GraphQL read-only em 2026-06-26T09:05Z; Doppler `lc-keys/prd` injetou `SHOPIFY_STORE_URL` e `SHOPIFY_ACCESS_TOKEN` sem imprimir valores (`values_printed=false`).
- `direct_login_auth_drift_candidate` `shopify_login` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/2026-06-05-google-customer-reviews-opt-in-approved-add-blocked.md:48` — - redireciona para Shopify login com `errorHint=no_cookie_session`.
- `direct_login_auth_drift_candidate` `shopify_login` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/2026-06-05-google-customer-reviews-opt-in-approval-attempt.md:21` — - result: redirected to Shopify login with `errorHint=no_cookie_session`.
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/approval-packets/2026-06-26-new-balance-740-publicability-write-preview-blocked-pending-stock.md:7` — Secrets: Doppler `lc-keys/prd` via helper; `SHOPIFY_STORE_URL` e `SHOPIFY_ACCESS_TOKEN` presentes; `values_printed=false`.
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/approval-packets/checkout-gift-bag-20260610.md:21` — - Secrets verificados por presença via Doppler: `SHOPIFY_STORE_URL`, `SHOPIFY_ACCESS_TOKEN` e GitHub token disponível; valores não foram impressos.
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/checkout-microfunnel-measurement-audit-20260610.md:10` — - `SHOPIFY_ACCESS_TOKEN`: presente no Doppler.
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/prds/prd-pdp-google-reviews-popup-cron-20260626.md:430` — - `SHOPIFY_ACCESS_TOKEN`: presente.
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/approval-packets/20260626T0905Z-new-balance-740-unblock-readonly-packet.md:21` — - **Shopify Admin read-only consultado em:** 2026-06-26T09:05Z via GraphQL query; `values_printed=false`; secrets `SHOPIFY_STORE_URL` e `SHOPIFY_ACCESS_TOKEN` existem no Doppler e foram injetados sem imprimir valores.
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/puma-speedcat-lkgoc-optimization-20260606T233058Z/RECEIPT-SUBIR-BLOCKED-NO-SHOPIFY-ENV.md:16` — ABORT missing Shopify env: SHOPIFY_STORE_URL/SHOPIFY_STORE and SHOPIFY_ACCESS_TOKEN/SHOPIFY_ADMIN_TOKEN/SHOPIFY_API_TOKEN
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/puma-speedcat-lkgoc-optimization-20260606T233058Z/RECEIPT-CANDIDATE-READY.md:27` — - `SHOPIFY_ACCESS_TOKEN` / `SHOPIFY_ADMIN_TOKEN` / `SHOPIFY_API_TOKEN`
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/content/receipts/lk-content-prd-config-continued-20260607.md:41` — - `SHOPIFY_ACCESS_TOKEN`
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/content/receipts/lk-content-gate7-shopify-tiny-readonly-20260607.md:27` — - Required secrets present: `SHOPIFY_ACCESS_TOKEN`, `SHOPIFY_STORE`
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/agentes/lk/TOOLS.md:6` — - Shopify LK: `SHOPIFY_ACCESS_TOKEN`, `SHOPIFY_STORE`, `SHOPIFY_STORE_URL`
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/agentes/lk/SOUL.md:87` — **Doppler keys:** `SUPABASE_LK_SERVICE_KEY`, `SUPABASE_LK_URL`, `SHOPIFY_ACCESS_TOKEN`, `KLAVIYO_API_KEY`
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/agentes/lk/AGENTS.md:75` — - Shopify LK (`SHOPIFY_ACCESS_TOKEN`) — leitura de produtos, pedidos, clientes
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/skills/lk-shopify-readonly/SKILL.md:37` — - `SHOPIFY_ACCESS_TOKEN`
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/skills/lk-shopify-readonly/SKILL.md:39` — Known historical detail: older docs mention `SHOPIFY_ACCESS_TOKEN` as the correct token name, not `SHOPIFY_API_TOKEN`. If both exist, prefer `SHOPIFY_ACCESS_TOKEN` unless Lucas/Brain says otherwise.
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/skills/lk-shopify-readonly/SKILL.md:44` — /opt/data/hermes_bruno_ingest/hermes_doppler.sh exists SHOPIFY_STORE_URL SHOPIFY_ACCESS_TOKEN
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/skills/lk-shopify-readonly/SKILL.md:74` — TOKEN=[REDACTED] secrets get SHOPIFY_ACCESS_TOKEN -p lc-keys -c prd --plain)"
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/skills/lk-shopify-readonly/SKILL.md:264` — 1. **Wrong token name.** Use `SHOPIFY_ACCESS_TOKEN`, not the historical mistaken `SHOPIFY_API_TOKEN` unless confirmed.
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_execute_approved_abc_20260514.py:178` — token = [REDACTED] or secrets.get('SHOPIFY_ADMIN_TOKEN') or secrets.get('SHOPIFY_API_TOKEN')
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_os_daily_sales_brief_20260511.py:111` — token = [REDACTED] or ''
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_gmc_source_governance_investigation_20260514.py:115` — token = [REDACTED] or secrets.get('SHOPIFY_ADMIN_TOKEN') or secrets.get('SHOPIFY_API_TOKEN') or ''
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_gmc_source_governance_investigation_20260514.py:126` — token = [REDACTED] or secrets.get('SHOPIFY_ADMIN_TOKEN') or secrets.get('SHOPIFY_API_TOKEN') or ''
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_gmc_local_cd_pos_source_validation_20260512.py:120` — shopify_token = [REDACTED] or ''
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_gmc_local_cd_shopify_live_preview_20260512.py:128` — shopify_token = [REDACTED] or ''
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_sourcing_decision_fields_v8_20260515.py:107` — shop_token=[REDACTED]
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_os_weekly_ceo_review_20260511.py:122` — token = [REDACTED] or ''
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_gmc_required_attrs_preview_20260512.py:59` — token = [REDACTED] or secrets.get('SHOPIFY_ADMIN_ACCESS_TOKEN')
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_phase5_generate_klaviyo_ready_visual_preview_20260511.py:91` — token = [REDACTED] '')
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_needs_data_autofix_readonly_20260512.py:388` — shop = Shopify(secrets['SHOPIFY_STORE_URL'], secrets['SHOPIFY_ACCESS_TOKEN'])
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_gmc_p0_url_checkout_review_20260512.py:65` — token = [REDACTED] or secrets.get('SHOPIFY_ADMIN_ACCESS_TOKEN')
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_os_data_spine_snapshots_20260511.py:91` — token = [REDACTED] or ''
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_p0_remaining_followup_readonly_20260511.py:22` — shop_token=[REDACTED]
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_gmc_b_remaining_shopify_live_probe_20260512.py:81` — token = [REDACTED] or ''
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_gmc_google_youtube_channel_readonly_diagnostic_20260514.py:53` — token=[REDACTED] or secrets.get('SHOPIFY_ADMIN_TOKEN') or secrets.get('SHOPIFY_API_TOKEN') or ''
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_weekly_influencer_sales_report.py:176` — token = [REDACTED] or secrets.get('SHOPIFY_ADMIN_TOKEN') or secrets.get('SHOPIFY_API_TOKEN')
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_apply_approved_p1_seo_fields_20260511.py:148` — secrets = doppler_secrets(['SHOPIFY_STORE_URL', 'SHOPIFY_ACCESS_TOKEN'])
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_apply_approved_p1_seo_fields_20260511.py:150` — token = [REDACTED]
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_p0_blocked_six_live_recheck_20260511.py:13` — TINY=secrets['TINY_API_TOKEN']; SHOP=secrets['SHOPIFY_ACCESS_TOKEN']
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_phase5_generate_klaviyo_visual_preview_20260511.py:59` — token = [REDACTED] "")
- `needs_review` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_sourcing_current_lk_price_reference_v7_20260515.py:107` — shop_token=[REDACTED]
- `historical_or_governance_evidence` `shopify_access_token_ref` — `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_os_sales_reports_whatsapp_email_designmd_20260516.py:289` — token = [REDACTED] or ''
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/hermes_doppler.py:51` — "SHOPIFY_ACCESS_TOKEN", "SHOPIFY_STORE", "GA4_LK_PROPERTY_ID",
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/hermes_doppler.py:57` — "SHOPIFY_ACCESS_TOKEN", "SHOPIFY_STORE", "EVOLUTION_API_KEY",
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/hermes_doppler.py:61` — "SHOPIFY_ACCESS_TOKEN", "SHOPIFY_ADMIN_TOKEN", "SHOPIFY_API_TOKEN",
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/hermes_doppler.py:77` — "SHOPIFY_ACCESS_TOKEN", "SHOPIFY_STORE",
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/hermes_doppler.py:92` — "SHOPIFY_ACCESS_TOKEN", "SHOPIFY_STORE", "SHOPIFY_STORE_URL",
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/hermes_doppler.py:97` — "SHOPIFY_ACCESS_TOKEN", "SHOPIFY_STORE",
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/hermes_doppler.py:101` — "KLAVIYO_API_KEY", "OPENROUTER_API_KEY", "SHOPIFY_ACCESS_TOKEN", "SHOPIFY_STORE",
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/hermes_doppler.py:104` — "SHOPIFY_ACCESS_TOKEN", "SHOPIFY_STORE", "GSC_SITE_URL",
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/hermes_doppler.py:109` — "GA4_LK_SERVICE_ACCOUNT", "SHOPIFY_ACCESS_TOKEN", "SHOPIFY_STORE",
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/lk_store_sale_restock_alert.py.bak-daily-limit-20260609T181418Z:78` — token = [REDACTED] or ''
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/lk_store_sale_restock_alert.py.bak-daily-limit-20260609T181418Z:99` — token = [REDACTED] or '')
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/lk_hermes_whatsapp_responder.py.bak-20260615Twhatsapp-stockos-audit:1659` — token = [REDACTED] or secrets.get("SHOPIFY_ACCESS_TOKEN") or secrets.get("SHOPIFY_API_TOKEN")
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/lk_hermes_whatsapp_responder.py:1823` — token = [REDACTED] or secrets.get("SHOPIFY_ACCESS_TOKEN") or secrets.get("SHOPIFY_API_TOKEN")
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/shopify_admin_graphql_cli.py:37` — return os.environ.get("SHOPIFY_ACCESS_TOKEN") or os.environ.get("SHOPIFY_ADMIN_TOKEN") or os.environ.get("SHOPIFY_API_TOKEN") or ""
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/lk_valentines_top_customers_preview.py:215` — token = [REDACTED] or os.environ.get("SHOPIFY_ADMIN_TOKEN") or os.environ.get("SHOPIFY_API_TOKEN")
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/hermes_cli_integrations.py:45` — CliDef("shopify_lk", ["shopify"], ["SHOPIFY_STORE", "SHOPIFY_STORE_URL", "SHOPIFY_ACCESS_TOKEN", "SHOPIFY_ADMIN_TOKEN"], "Admin API read-only smoke"),
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/lk_pos_postpurchase_shopify_reconciler.py:50` — os.environ.get('SHOPIFY_ACCESS_TOKEN')
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/hermes_daily_intelligence_preflight.py:47` — "lk-shopify": ["SHOPIFY_ACCESS_TOKEN", "SHOPIFY_SHOP_DOMAIN"],
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/hermes_daily_intelligence_preflight.py:51` — "SHOPIFY_ACCESS_TOKEN", "SHOPIFY_STORE",
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/lk_store_sale_restock_alert.py:104` — token = [REDACTED] or ''
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/lk_store_sale_restock_alert.py:125` — token = [REDACTED] or '')
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/hermes_cli_run.py:27` — ("SHOPIFY_ACCESS_TOKEN", ["SHOPIFY_ACCESS_TOKEN", "SHOPIFY_ADMIN_TOKEN", "SHOPIFY_API_TOKEN"]),
- `legacy_fallback_or_drift_candidate` `shopify_admin_graphql` — `/opt/data/scripts/hermes_cli_run.py:30` — "shopify-admin-graphql": [
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/hermes_cli_run.py:31` — ("SHOPIFY_ACCESS_TOKEN", ["SHOPIFY_ACCESS_TOKEN", "SHOPIFY_ADMIN_TOKEN", "SHOPIFY_API_TOKEN"]),
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/backups/hermes_daily_intelligence_preflight.py.20260623T0502Z.bak:46` — "lk-shopify": ["SHOPIFY_ACCESS_TOKEN", "SHOPIFY_SHOP_DOMAIN"],
- `needs_review` `shopify_access_token_ref` — `/opt/data/scripts/backups/hermes_daily_intelligence_preflight.py.20260623T0502Z.bak:50` — "SHOPIFY_ACCESS_TOKEN", "SHOPIFY_STORE",

## Interpretação inicial

- A presença de ocorrências históricas/governança não significa falha ativa; precisa revisão antes de patch.
- Ocorrências `direct_login_auth_drift_candidate` e `legacy_fallback_or_drift_candidate` são candidatas para Fase 2/3.
- Nenhum valor de secret foi intencionalmente impresso; saída foi redigida por padrões locais antes de salvar.


## Supplemental targeted retry — 2026-06-28T14:58:45Z

Command:

```bash
/opt/data/home/.local/bin/hermes-cli-integrations smoke google_workspace klaviyo
```

Sanitized result:

```json
{
  "results": {
    "google_workspace": {"method": "gws_gmail_users_getProfile", "rc": 2, "status": "failed"},
    "klaviyo": {"method": "klaviyo_get_flows_stdout", "rc": 0, "status": "ok"}
  },
  "values_printed": false
}
```

Interpretation:

- Klaviyo initial `rc=124` appears transient; targeted retry is OK.
- Google Workspace remains failed with `rc=2`; classify as non-blocking for Shopify/Auth Broker Fase 1, but should be handled as a separate integration health item if Lucas wants.
- No secrets printed; external writes 0.
