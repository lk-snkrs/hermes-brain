# CLI/MCP availability + all-agents API migration audit — 2026-06-27

Status: audit_done
Values printed: false
External writes: 0
Runtime/Docker/VPS restarts: 0

## Answer

No — this environment has the main governed CLIs/wrappers and MCPs installed/configured, and all audited profile instruction files carry the CLI-first policy, but **not every possible CLI/MCP is installed/functioning across every agent**, and there are still **2 enabled cron script paths with raw API code**.

Canonical policy remains: CLI/wrapper first -> MCP second -> raw API only as justified exception.

## CLI/wrapper inventory

Source: `/opt/data/home/.local/bin/hermes-cli-integrations inventory` + direct PATH check with `/opt/data/home/.local/bin`.

| Integration | CLI/wrapper present | Read-only smoke | Notes |
|---|---:|---:|---|
| GitHub `gh` | yes | ok | `gh api` works |
| Vercel | yes | ok | via Hermes CLI wrapper |
| Notion `ntn` | yes | ok | `ntn whoami` works |
| Supabase | yes | ok | CLI token works; project listing/query work |
| Cloudflare/Wrangler | yes | ok | wrapper smoke ok |
| Klaviyo | yes | ok | wrapper smoke ok |
| Sentry | yes | ok | CLI smoke ok |
| Linear `lin` | yes | blocked | CLI exists, but no safe read-only smoke in wrapper |
| Google Workspace `gws` | yes | failed | CLI installed and secrets present, but runtime credentials injection/auth is not functioning in this smoke |
| Shopify | yes | failed | CLI installed; smoke path missing required `--store` flag / wrapper needs hardening |
| WACLI | yes | not smoked here | installed in Hermes PATH; auth state should be checked per account before use |
| mcporter | yes | not smoked here | installed; ad-hoc MCP bridge available |
| himalaya / xurl / x-cli / hf / modal / wandb | not installed in audited PATH | n/a | optional/backlog unless a live workflow needs them |

## MCP availability

Current/default profile MCP tools are active and smoke-tested:

| MCP server | Configured | Toolset exposed | Smoke |
|---|---:|---:|---:|
| time | yes | yes | ok |
| fetch | yes | yes | ok |
| sequential_thinking | yes | yes | ok |
| metricool_readonly | yes | yes | ok |
| dataforseo | yes | yes | ok |

Profile configs mention MCP toolsets broadly. Not every specialist exposes the same MCP set; examples:
- Growth/Content/Trends/Spiti: dataforseo/fetch/time/sequential thinking present.
- Stock: includes `mcp-supabase` in config, but this audit did not verify that MCP server live tool registration is functioning in the current default conversation.
- Shopify: config mentions MCP infrastructure but not a specific Shopify MCP toolset in the compact scan.

## All-agents policy propagation

Audited profile-local `AGENTS.md`/`SOUL.md` where present: **18 profile directories scanned**. The sampled files all include the CLI/MCP/raw-API policy signal. This means the agents were *taught the rule documentally*.

Caveat: teaching != runtime migration. Script-only `no_agent` crons obey only their script content and wrapper availability.

## Cron/script migration status

Cron registries audited: **11**
Cron jobs total: **103**
Enabled jobs: **85**
Script crons: **80**
Prompt crons: **50**
No-agent crons: **79**

Enabled cron scripts still containing raw API primitives:

1. `lk-stock` — `LK Stock OS Supabase read-model sync hourly`
   - script: `/opt/data/profiles/lk-stock/scripts/lk_stock_os_supabase_sync.py`
   - status: active gap; raw Hub/Supabase REST code still present in live file.
2. `lk-stock` — `LK Shopify Sales OS nightly full reconcile read-only`
   - script: `/opt/data/profiles/lk-stock/scripts/lk_shopify_sales_os_nightly_reconcile.py`
   - status: active gap; raw primitive present in read-only/reconcile path.

Enabled cron raw count: **2**.

Broader scripts/skills still contain many raw HTTP/API examples, mostly in reusable skills, tests, one-off scripts, or dormant paths. Those are not all operationally active, but they are not fully migrated.

## Gaps / next migration backlog

1. Fix Google Workspace CLI auth injection for `gws` wrapper.
2. Harden Shopify wrapper smoke to pass `--store` from Doppler/env automatically.
3. Convert or disable the 2 active LK Stock raw cron script paths.
4. Decide whether optional CLIs should be installed: himalaya, xurl/x-cli, hf, modal, wandb. Do not install just because possible; install when a live workflow needs them.
5. Verify specialist-profile MCP registration live per profile only if Lucas wants a full runtime activation audit; this audit checked config/tool availability, not profile gateway restarts.

## Verification performed

- `hermes-cli-integrations inventory`: rc 0.
- `hermes-cli-integrations smoke`: rc 0 with per-integration failures noted above.
- MCP smoke: time/fetch/sequential_thinking/metricool_readonly/dataforseo OK.
- Cron registry scan: 11 registries, 103 jobs.
- Enabled raw cron scan: 2 active gaps.
- No secrets printed: `values_printed=false`.
