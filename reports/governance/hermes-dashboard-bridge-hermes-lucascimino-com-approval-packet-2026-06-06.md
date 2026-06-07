# Approval Packet — Hermes Web Dashboard bridge at hermes.lucascimino.com

- Date: 2026-06-06
- Request: expose/use Hermes v0.16 Web Dashboard through `hermes.lucascimino.com`
- Owner: Hermes Geral / Lucas runtime governance
- Risk: A3/A4 production control-plane exposure depending on final route/auth implementation

## 1. Current evidence

Read-only/local audit performed before any production write.

### Runtime

- Default Hermes gateway is running v0.16 on `/opt/data`.
- Default gateway process exposes:
  - `API_SERVER_ENABLED=true`
  - `API_SERVER_HOST=0.0.0.0`
  - `API_SERVER_PORT=8642`
  - `WEBHOOK_ENABLED=true`
  - `WEBHOOK_PORT=8644`
- Specialist profile gateways observed with API/webhook disabled:
  - mordomo
  - lk-growth
  - spiti
  - lk-ops
  - lk-shopify
  - lk-trends
  - lk-collection-optimizer

### Local endpoints

- `http://127.0.0.1:8642/health` → `200`, `{"status":"ok","platform":"hermes-agent"}`
- `http://127.0.0.1:8642/v1/models` → `401 Unauthorized`, expected without API key
- `http://127.0.0.1:8644/health` → `200`, `{"status":"ok","platform":"webhook"}`
- `http://127.0.0.1:8643/*` → no service listening

### Dashboard local preview

Started local-only dashboard preview:

- Command shape: `hermes dashboard --host 127.0.0.1 --port 9119 --no-open --skip-build`
- `http://127.0.0.1:9119/` → `200`, dashboard HTML title `Hermes Agent - Dashboard`
- `http://127.0.0.1:9119/api/config` → `401 Unauthorized`
- `http://127.0.0.1:9119/openapi.json` → `200`, OpenAPI title `Hermes Agent`, version `0.16.0`

### Public subdomain

- `hermes.lucascimino.com` resolves through Cloudflare.
- `https://hermes.lucascimino.com/` currently returns `404 page not found`.
- `https://hermes.lucascimino.com/health` currently returns `404 page not found`.
- `https://hermes.lucascimino.com/openapi.json` currently returns `404 page not found`.
- Conclusion: domain exists/routes somewhere, but is not currently bridged to the Hermes dashboard.

## 2. Product goal

Make `https://hermes.lucascimino.com` a safe Hermes Web Dashboard / control-plane entrypoint for Lucas, using Hermes v0.16 dashboard/admin capabilities.

## 3. Recommended implementation model

### Preferred public model

- Run dashboard bound to loopback on the host/container side, not naked public bind.
- Put Cloudflare/Traefik HTTPS in front.
- Require dashboard authentication before sensitive APIs.
- Keep API keys/secrets out of HTML/source/public logs.
- Preserve API server and webhook semantics separately from dashboard UI.

### Safer alternative

- Keep dashboard local-only and access it through SSH tunnel/Tailscale/Cloudflare Access instead of naked public Traefik.
- This is safer but does not fully satisfy a direct public dashboard URL unless Cloudflare Access is configured.

## 4. Execution plan requiring approval

### Pre-write backup

1. Capture current dashboard process state.
2. Capture current gateway state and local health.
3. Capture current Traefik/Docker/compose route config if host access is used.
4. Capture Cloudflare/DNS state if DNS mutation is needed.
5. Store redacted backup/receipt in Brain and backup dir.

### Stage A — local dashboard service

1. Ensure dashboard process can run persistently on `127.0.0.1:9119` or equivalent safe container/host loopback.
2. Verify local UI and auth:
   - `/` returns dashboard HTML.
   - `/api/config` is not public without auth.
   - `/openapi.json` exposure is reviewed; public exposure may need blocking/proxy auth.
3. Decide whether dashboard is supervised by Hermes CLI, systemd, Docker sidecar, or existing runtime process.

### Stage B — bridge domain

Depending on actual host topology:

1. If Traefik already routes `hermes.lucascimino.com`, update only that router/service target to dashboard port.
2. If DNS is missing/wrong, create/update only the `hermes` DNS record.
3. If Cloudflare Access is available/desired, put access policy in front before exposing dashboard.
4. Avoid exposing raw API server `8642` or webhook `8644` as the dashboard unless explicitly intended.

### Stage C — validation

1. Public GET `https://hermes.lucascimino.com/` returns dashboard HTML or auth wall.
2. Public unauthenticated sensitive APIs return `401/403` or are blocked:
   - `/api/config`
   - `/api/sessions`
   - `/api/logs`
   - `/api/skills`
   - `/openapi.json` reviewed/acceptable or blocked.
3. Default Telegram gateway remains connected.
4. API local health remains healthy.
5. Webhook health remains healthy.
6. Specialist profiles remain API/webhook disabled.
7. No tokens/API keys are present in public HTML.

### Rollback

1. Remove/disable only the new dashboard route or restore previous Traefik/DNS config.
2. Stop only the dashboard process if it was newly started for this bridge.
3. Verify `https://hermes.lucascimino.com` no longer reaches dashboard if rollback desired.
4. Verify Telegram/API/webhook return to pre-change state.

## 5. Guardrails

- No secrets printed in terminal, Brain, or Telegram.
- No broad Docker/Traefik/VPS changes.
- No unrelated containers/services/profiles touched.
- No specialist API/webhook surfaces enabled.
- No default model/provider changes.
- No dashboard public exposure without auth review.
- If host/DNS access is blocked or uncertain, stop and report the blocker instead of guessing.

## 6. Approval options

### Option A — Approve read-only host/DNS/Traefik discovery only

Allowed:

- SSH/Hostinger/Cloudflare/DNS/Traefik/Docker read-only inspection.
- No writes.
- Produce exact implementation plan from real host topology.

Not allowed:

- Changing DNS, Traefik, Docker, firewall, dashboard service, gateway restart.

### Option B — Approve full bridge implementation with rollback

Allowed:

- Backup current route/config.
- Start/supervise dashboard if needed.
- Create/update only the `hermes.lucascimino.com` bridge to dashboard.
- Apply auth/proxy restrictions as needed.
- Validate public endpoint and rollback if validation fails.

Still not allowed:

- Broad VPS rebuilds.
- Unrelated domain/routes/services.
- Exposing raw API/webhook ports directly.
- Printing secrets.
- Changing profile model/tooling/business crons.

### Option C — Block public bridge; keep local/SSH tunnel only

Allowed:

- Stop local preview if desired.
- Document SSH tunnel path for Lucas.

## 7. Current recommendation

Proceed with Option A first if we do not already know the live Traefik/Cloudflare topology from current evidence. If Lucas wants speed and explicitly approves production bridge work, proceed with Option B but still perform backup/read-only discovery first and rollback on failed auth/public checks.
