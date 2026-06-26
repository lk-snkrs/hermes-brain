# Receipt — Crisp Plugin Canary 0/1 implemented locally — 2026-05-21

## Scope

- Canary level: 0/1
- Mode: observe_only
- Auto-reply enabled: false
- Crisp real/Marketplace connection: not configured
- Hugo Workflow/MCP: not used

## Implemented in Hermes repo

Repo:

- `/opt/data/hermes_bruno_ingest/hermes-agent-v0.13.0`

Local commit:

- `e35981c` — `feat: add Crisp plugin webhook canary receiver`

Files added/changed by this slice:

- `gateway/integrations/__init__.py`
- `gateway/integrations/crisp.py`
- `gateway/platforms/webhook.py`
- `tests/gateway/test_crisp_plugin_integration.py`
- `tests/fixtures/crisp/plugin_hook_message_send.json`
- `tests/fixtures/crisp/plugin_hook_operator_message.json`
- `tests/fixtures/crisp/plugin_hook_bot_echo.json`
- `docs/plans/crisp-plugin-canary-config-example.md`
- `areas/lk/sub-areas/crm/templates/crisp-plugin-canary-receipt-template.md` (Brain template)

## What was built

- Synthetic Crisp Plugin Hook fixtures with no customer data.
- Pure Crisp normalizer helper.
- Crisp HMAC verifier helper for isolated tests.
- `kind: crisp_plugin` branch in the existing Hermes webhook adapter.
- `observe_only` mode that:
  - accepts visitor `message:send` events;
  - ignores operator/bot/plugin echo events;
  - deduplicates repeated events;
  - returns JSON status;
  - does not trigger Hermes agent runs;
  - does not send customer-facing replies.

## Verification

Command run after commit:

```bash
/opt/hermes/.venv/bin/python -m pytest tests/gateway/test_crisp_plugin_integration.py tests/gateway/test_webhook_adapter.py tests/gateway/test_webhook_signature_rate_limit.py -q
```

Result:

- `67 passed in 3.60s`

Additional checks:

- JSON fixtures validated with `python3 -m json.tool` before tests.
- `git status --short` after commit only shows pre-existing unrelated dirty files:
  - `agent/context_compressor.py`
  - `gateway/platforms/telegram.py`
  - `tests/agent/test_context_compressor.py`

## Safety

- Customer-facing replies sent: none
- Crisp Marketplace real endpoint configured: none
- Docker/VPS/gateway restarted: no
- Secrets printed: none
- Doppler values read: no

## Notes

The repo was already dirty before this work with unrelated context-compression/Telegram files. This Crisp slice was committed separately and did not stage those files.
