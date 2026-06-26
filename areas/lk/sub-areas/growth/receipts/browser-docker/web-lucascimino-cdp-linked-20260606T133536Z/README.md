# LK Browser CDP linked — 20260606T133536Z

Endpoint privado para Hermes/MCP/Playwright:

- `http://lk-browser-web:9223`
- `http://lk-browser-web:9223/json/version`

Validações:

- JSON version: HTTP 200 a partir do container Hermes
- JSON list: HTTP 200 a partir do container Hermes
- WebSocket CDP: HTTP 101 handshake a partir do container Hermes

Rollback:

```bash
docker rm -f lk-browser-cdp-proxy
docker network disconnect hermes-agent-5ajw_default lk-browser-web
```
