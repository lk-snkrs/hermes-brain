# Mac Chrome control from VPS Hermes — technical note

- Created UTC: 2026-06-05T19:37:37Z
- Context: Lucas wants Hermes running on Hostinger VPS to control Chrome on his Mac/laptop.

## Recommendation

Use a dedicated Playwright MCP server running on the Mac, reachable from VPS Hermes through SSH/Tailscale/reverse tunnel. Do not expose Chrome DevTools or MCP ports publicly.

## Why

- Hermes docs support MCP stdio and remote HTTP MCP servers.
- Playwright MCP supports persistent profiles, HTTP/SSE port mode, Chrome CDP endpoints, and a Chrome extension mode for existing tabs.
- Chrome 136+ no longer honors remote debugging switches against the default Chrome data directory; debugging must use a non-standard `--user-data-dir` or Chrome for Testing. This is also safer because it avoids exposing the user's main browser cookies/session.

## Architecture options

### Preferred v1: Mac Playwright MCP with dedicated persistent profile

Mac runs:

```bash
mkdir -p ~/.hermes-browser/lk-profile ~/.hermes-browser/output
npx -y @playwright/mcp@latest \
  --port 8931 \
  --host 127.0.0.1 \
  --user-data-dir ~/.hermes-browser/lk-profile \
  --output-dir ~/.hermes-browser/output \
  --shared-browser-context
```

Connectivity from VPS should be private via one of:

- Tailscale: VPS connects to `http://<mac-tailscale-ip>:8931/...` if Mac binds to Tailscale IP, or use SSH local forward.
- Reverse SSH tunnel from Mac to VPS:

```bash
ssh -N -R 127.0.0.1:8931:127.0.0.1:8931 <vps-user>@<vps-host>
```

Hermes `~/.hermes/profiles/lk-growth/config.yaml` then adds remote MCP URL for the forwarded endpoint. Exact endpoint path/transport must be verified against the running Playwright MCP/Hermes version.

### Existing Chrome/tab control

Use Playwright MCP Chrome Extension if Lucas truly needs existing logged-in browser tabs/session. This is more sensitive and should require explicit approval per session.

### Avoid

- Do not bind Chrome DevTools `--remote-debugging-port` to `0.0.0.0`.
- Do not expose MCP port directly to the internet.
- Do not automate the main personal Chrome profile through remote debugging.

## Security gates

- Read-only browsing by default.
- External writes/customer-facing actions still require explicit Lucas approval.
- Use a separate Chrome profile for LK operations.
- Prefer Tailscale/SSH tunnel with localhost binding only.


## Setup update — 2026-06-05T20:15:40Z

- Lucas provided Mac Tailscale IP: `100.91.116.104`.
- Mac Playwright MCP endpoint shown by local process: `http://100.91.116.104:8931/mcp`.
- VPS profile config written: `/opt/data/home/.hermes/profiles/lk-growth/config.yaml` with `mcp_servers.playwright.url`.
- Connectivity check initially reached endpoint with HTTP 400 on raw GET, confirming network path.
- Later checks returned `Connection refused`, meaning Mac is reachable but Playwright MCP process is not listening/running at that moment.
- Next action: Lucas should rerun Playwright MCP command on Mac; then verify MCP initialize/list_tools from VPS.


## Verification — 2026-06-05T20:18:01Z

- MCP streamable HTTP connection from VPS to Mac succeeded.
- Session initialized successfully.
- Listed 23 Playwright MCP tools including browser_navigate, browser_snapshot, browser_click, browser_tabs, browser_take_screenshot.
- A later connectivity check timed out, likely because Mac process/network became unavailable after first test or Mac sleep/firewall/session interruption.
- Recommended Mac command for long-running worker: wrap Playwright MCP with `caffeinate -dimsu`.


## Active profile config correction — 2026-06-05T20:21:13Z

- Correct active `HERMES_HOME` for Telegram LK Growth gateway is `/opt/data/profiles/lk-growth`.
- Added Playwright MCP to `/opt/data/profiles/lk-growth/config.yaml`.
- Backup: `/opt/data/profiles/lk-growth/config.yaml.bak-playwright-mcp-20260605T202033Z`.
- Disabled mistakenly-created inactive config under `/opt/data/home/.hermes/profiles/lk-growth/`.
- User requested option 1: restart LK Growth Hermes gateway to load MCP tools.
