# Crisp Marketplace Plugin Canary 0/1 Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task after Lucas approves implementation. Do not mutate Docker/VPS/gateway production without explicit approval and rollback.

**Goal:** Build the safe first slice of the Crisp Marketplace Plugin → Hermes Brain integration: local fixtures, signature verification, event normalization, idempotency/anti-loop, and a non-customer-facing webhook receiver.

**Architecture:** Start inside the Hermes Agent codebase as an extension of the existing webhook platform adapter, because it already has aiohttp, HMAC validation patterns, health endpoint, route config, rate limiting and idempotency. Canary 0/1 must not send customer replies; it should only validate/normalize events and log/receipt safe metadata. A production connection to Crisp Marketplace is a later approval gate.

**Tech Stack:** Python, aiohttp, pytest, Hermes gateway webhook adapter, Doppler for Crisp secrets, Brain markdown receipts.

---

## Safety prelude

### Mandatory constraints

- No Hugo Workflow API or Hugo MCP in this MVP.
- No customer-facing auto-reply in Canary 0/1.
- No Docker/VPS/gateway restart without Lucas approval.
- No printing secrets from Doppler.
- No public Crisp Marketplace connection until tests and approval are complete.

### Working repo

Use the Hermes Agent checkout:

```text
/opt/data/hermes_bruno_ingest/hermes-agent-v0.13.0
```

### PRD source

```text
/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/crm/prds/crisp-marketplace-plugin-hermes-brain-prd-2026-05-21.md
```

---

## Task 1: Confirm clean implementation target

**Objective:** Verify the repo and branch before touching code.

**Files:**
- Read: `/opt/data/hermes_bruno_ingest/hermes-agent-v0.13.0/AGENTS.md`
- Inspect: git status in `/opt/data/hermes_bruno_ingest/hermes-agent-v0.13.0`

**Step 1: Check repository status**

Run:

```bash
cd /opt/data/hermes_bruno_ingest/hermes-agent-v0.13.0
git status --short
git branch --show-current
```

Expected:

- Current branch is known.
- Any pre-existing modifications are listed and not overwritten.

**Step 2: If dirty, classify changes**

If `git status --short` returns files, inspect with:

```bash
git diff --stat
git diff -- <file>
```

Expected:

- Do not overwrite unrelated work.
- If dirty state is unrelated and risky, stop and ask Lucas.

---

## Task 2: Add Crisp sample fixtures

**Objective:** Create minimal synthetic Crisp Plugin Hook payloads for testing without real customer data.

**Files:**
- Create: `tests/fixtures/crisp/plugin_hook_message_send.json`
- Create: `tests/fixtures/crisp/plugin_hook_operator_message.json`
- Create: `tests/fixtures/crisp/plugin_hook_bot_echo.json`

**Step 1: Create visitor message fixture**

Create `tests/fixtures/crisp/plugin_hook_message_send.json`:

```json
{
  "event": "message:send",
  "website_id": "website_canary_123",
  "session_id": "session_canary_abc",
  "data": {
    "type": "text",
    "from": "user",
    "origin": "chat",
    "content": "Olá, vocês têm o Jordan 4 tamanho 40?",
    "timestamp": 1779364800000,
    "fingerprint": 123456789
  }
}
```

**Step 2: Create operator message fixture**

Create `tests/fixtures/crisp/plugin_hook_operator_message.json`:

```json
{
  "event": "message:send",
  "website_id": "website_canary_123",
  "session_id": "session_canary_abc",
  "data": {
    "type": "text",
    "from": "operator",
    "origin": "operator",
    "content": "Oi! Vou verificar para você.",
    "timestamp": 1779364810000,
    "fingerprint": 123456790
  }
}
```

**Step 3: Create bot/plugin echo fixture**

Create `tests/fixtures/crisp/plugin_hook_bot_echo.json`:

```json
{
  "event": "message:send",
  "website_id": "website_canary_123",
  "session_id": "session_canary_abc",
  "data": {
    "type": "text",
    "from": "bot",
    "origin": "plugin",
    "content": "Mensagem enviada pelo plugin",
    "timestamp": 1779364820000,
    "fingerprint": 123456791
  }
}
```

**Step 4: Verify JSON**

Run:

```bash
python -m json.tool tests/fixtures/crisp/plugin_hook_message_send.json >/dev/null
python -m json.tool tests/fixtures/crisp/plugin_hook_operator_message.json >/dev/null
python -m json.tool tests/fixtures/crisp/plugin_hook_bot_echo.json >/dev/null
```

Expected: all commands exit `0`.

---

## Task 3: Add Crisp event normalization helper

**Objective:** Convert Crisp Plugin Hook payloads into a stable internal event model.

**Files:**
- Create: `gateway/integrations/crisp.py`
- Test: `tests/gateway/test_crisp_plugin_integration.py`

**Step 1: Write failing tests**

Create `tests/gateway/test_crisp_plugin_integration.py` with tests for visitor message, operator message, bot echo and missing fields:

```python
import json
from pathlib import Path

from gateway.integrations.crisp import normalize_crisp_plugin_event, should_ignore_crisp_event

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "crisp"


def load_fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text())


def test_normalize_visitor_message():
    event = normalize_crisp_plugin_event(load_fixture("plugin_hook_message_send.json"))

    assert event["source"] == "crisp"
    assert event["website_id"] == "website_canary_123"
    assert event["session_id"] == "session_canary_abc"
    assert event["event_type"] == "message:send"
    assert event["actor_type"] == "user"
    assert event["message_type"] == "text"
    assert event["content"] == "Olá, vocês têm o Jordan 4 tamanho 40?"
    assert event["delivery_id"] == "message:send:website_canary_123:session_canary_abc:123456789"


def test_should_not_ignore_visitor_message():
    event = normalize_crisp_plugin_event(load_fixture("plugin_hook_message_send.json"))
    assert should_ignore_crisp_event(event) is False


def test_should_ignore_operator_message():
    event = normalize_crisp_plugin_event(load_fixture("plugin_hook_operator_message.json"))
    assert should_ignore_crisp_event(event) is True


def test_should_ignore_bot_echo():
    event = normalize_crisp_plugin_event(load_fixture("plugin_hook_bot_echo.json"))
    assert should_ignore_crisp_event(event) is True


def test_normalize_missing_optional_data():
    event = normalize_crisp_plugin_event({
        "event": "message:send",
        "website_id": "w",
        "session_id": "s",
        "data": {}
    })

    assert event["website_id"] == "w"
    assert event["session_id"] == "s"
    assert event["content"] == ""
    assert event["delivery_id"].startswith("message:send:w:s:")
```

**Step 2: Run test to verify failure**

Run:

```bash
python -m pytest tests/gateway/test_crisp_plugin_integration.py -q
```

Expected: FAIL because `gateway.integrations.crisp` does not exist.

**Step 3: Implement helper**

Create `gateway/integrations/crisp.py`:

```python
"""Crisp Marketplace Plugin helpers.

Pure functions only: no network calls, no Doppler calls, no customer replies.
"""

from __future__ import annotations

import hashlib
import hmac
import json
from typing import Any, Dict


SELF_ACTOR_TYPES = {"operator", "bot", "plugin"}
SELF_ORIGINS = {"operator", "bot", "plugin"}


def normalize_crisp_plugin_event(payload: Dict[str, Any]) -> Dict[str, Any]:
    data = payload.get("data") or {}
    event_type = str(payload.get("event") or payload.get("event_type") or "unknown")
    website_id = str(payload.get("website_id") or "")
    session_id = str(payload.get("session_id") or "")
    actor_type = str(data.get("from") or data.get("actor_type") or "unknown")
    origin = str(data.get("origin") or "")
    message_type = str(data.get("type") or "unknown")
    content = data.get("content") or ""
    timestamp = data.get("timestamp") or payload.get("timestamp") or ""
    fingerprint = data.get("fingerprint") or payload.get("fingerprint") or ""

    raw_delivery = ":".join([
        event_type,
        website_id,
        session_id,
        str(fingerprint or timestamp or json.dumps(payload, sort_keys=True)),
    ])

    return {
        "source": "crisp",
        "website_id": website_id,
        "session_id": session_id,
        "event_type": event_type,
        "actor_type": actor_type,
        "origin": origin,
        "message_type": message_type,
        "content": str(content),
        "timestamp": timestamp,
        "fingerprint": fingerprint,
        "delivery_id": raw_delivery,
        "raw": payload,
    }


def should_ignore_crisp_event(event: Dict[str, Any]) -> bool:
    if event.get("event_type") != "message:send":
        return True
    if not event.get("session_id"):
        return True
    if event.get("actor_type") in SELF_ACTOR_TYPES:
        return True
    if event.get("origin") in SELF_ORIGINS:
        return True
    return False


def verify_crisp_signature(raw_body: bytes, timestamp: str, signature: str, secret: str) -> bool:
    """Verify Crisp-style HMAC-SHA256 signature.

    The exact signing base may need adjustment against Crisp's live docs if Plugin
    Hooks differ from Hugo MCP. Keep this function isolated so tests document the
    expected behavior before wiring production.
    """
    if not raw_body or not timestamp or not signature or not secret:
        return False
    signed = timestamp.encode("utf-8") + b"." + raw_body
    expected = hmac.new(secret.encode("utf-8"), signed, hashlib.sha256).hexdigest()
    given = signature.removeprefix("sha256=")
    return hmac.compare_digest(expected, given)
```

**Step 4: Run tests**

Run:

```bash
python -m pytest tests/gateway/test_crisp_plugin_integration.py -q
```

Expected: PASS.

---

## Task 4: Add Crisp signature verification tests

**Objective:** Document the HMAC behavior before hooking it into HTTP handling.

**Files:**
- Modify: `tests/gateway/test_crisp_plugin_integration.py`
- Modify: `gateway/integrations/crisp.py` only if tests expose issue

**Step 1: Add tests**

Append:

```python
import hashlib
import hmac

from gateway.integrations.crisp import verify_crisp_signature


def test_verify_crisp_signature_accepts_valid_signature():
    raw = b'{"event":"message:send"}'
    timestamp = "1779364800"
    secret = "test-secret"
    signature = hmac.new(secret.encode(), timestamp.encode() + b"." + raw, hashlib.sha256).hexdigest()

    assert verify_crisp_signature(raw, timestamp, signature, secret) is True
    assert verify_crisp_signature(raw, timestamp, "sha256=" + signature, secret) is True


def test_verify_crisp_signature_rejects_bad_signature():
    raw = b'{"event":"message:send"}'
    assert verify_crisp_signature(raw, "1779364800", "bad", "test-secret") is False
```

**Step 2: Run tests**

Run:

```bash
python -m pytest tests/gateway/test_crisp_plugin_integration.py -q
```

Expected: PASS.

---

## Task 5: Add route mode for Crisp Plugin Hooks without agent/customer reply

**Objective:** Allow the existing webhook adapter to receive a Crisp route and return safe JSON without invoking the agent or sending replies.

**Files:**
- Modify: `gateway/platforms/webhook.py`
- Test: existing webhook tests plus new tests as needed

**Design:** Add a route config option:

```yaml
kind: crisp_plugin
mode: observe_only
```

When `kind == "crisp_plugin"`, `_handle_webhook` should:

1. read raw body;
2. validate route secret using existing HMAC path or Crisp-specific verifier;
3. parse JSON;
4. normalize Crisp event;
5. derive `event_type` from normalized event;
6. idempotency by normalized `delivery_id`;
7. ignore self/unsupported events;
8. log safe metadata only;
9. return `{"status":"accepted"}` or `{"status":"ignored"}`;
10. never call the agent and never call `send()`.

**Step 1: Add failing unit/integration test**

Find the existing webhook adapter tests and add a test similar to existing POST tests, using an aiohttp test client if already used in the suite.

Acceptance assertions:

- `POST /webhooks/crisp-lk-canary` with valid payload returns HTTP 200.
- Response status is `accepted` for visitor message.
- Response status is `ignored` for operator/bot echo.
- Duplicate delivery returns `duplicate`.
- The adapter does not enqueue a `MessageEvent` for crisp observe_only mode.

**Step 2: Implement minimal branch**

In `gateway/platforms/webhook.py`, after payload parsing and before prompt rendering, branch on:

```python
if route_config.get("kind") == "crisp_plugin":
    return await self._handle_crisp_plugin_webhook(request, route_name, route_config, raw_body, payload)
```

Add helper method in the class:

```python
async def _handle_crisp_plugin_webhook(self, request, route_name, route_config, raw_body, payload):
    from gateway.integrations.crisp import normalize_crisp_plugin_event, should_ignore_crisp_event

    event = normalize_crisp_plugin_event(payload)
    delivery_id = request.headers.get("X-Crisp-Delivery") or event["delivery_id"]

    # Reuse/prune self._seen_deliveries with same TTL pattern as generic path.
    # If duplicate: return {"status":"duplicate", "delivery_id": delivery_id}.
    # If ignored: return {"status":"ignored", "reason":"self_or_unsupported"}.
    # Else: logger.info safe metadata and return {"status":"accepted", "delivery_id": delivery_id}.
```

Do not include `content` in logs.

**Step 3: Run targeted tests**

Run:

```bash
python -m pytest tests/gateway/test_crisp_plugin_integration.py tests/gateway/test_webhook_adapter.py -q
```

Expected: PASS.

---

## Task 6: Add sample safe config docs for local Canary 0/1

**Objective:** Document how to configure the route without real secrets.

**Files:**
- Create: `docs/plans/crisp-plugin-canary-config-example.md` or Brain-only doc if not touching repo docs

**Content:**

```yaml
platforms:
  webhook:
    enabled: true
    extra:
      host: "127.0.0.1"
      port: 8644
      routes:
        crisp-lk-canary:
          kind: crisp_plugin
          mode: observe_only
          events: ["message:send"]
          secret: "INSECURE_NO_AUTH" # local test only; never public
          deliver: "log"
```

For real canary, secret must come from Doppler as `CRISP_MARKETPLACE_SIGNING_SECRET` and not be written to config unless the deployment pattern securely injects it.

**Verification:** No real credentials in docs.

---

## Task 7: Add local curl test script or command block

**Objective:** Let us verify Canary 0 without Crisp Marketplace.

**Files:**
- Create: `scripts/test_crisp_plugin_webhook_local.py` if scripts are acceptable, or document a command block only.

**Command-only safe version:**

```bash
curl -sS -X POST http://127.0.0.1:8644/webhooks/crisp-lk-canary \
  -H 'Content-Type: application/json' \
  --data-binary @tests/fixtures/crisp/plugin_hook_message_send.json | python -m json.tool
```

Expected:

```json
{
  "status": "accepted",
  "delivery_id": "..."
}
```

Bot echo expected:

```bash
curl -sS -X POST http://127.0.0.1:8644/webhooks/crisp-lk-canary \
  -H 'Content-Type: application/json' \
  --data-binary @tests/fixtures/crisp/plugin_hook_bot_echo.json | python -m json.tool
```

Expected status: `ignored`.

---

## Task 8: Add receipt template for canary runs

**Objective:** Ensure every canary run creates a consistent Brain receipt without customer data.

**Files:**
- Create: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/crm/templates/crisp-plugin-canary-receipt-template.md`

**Content:**

```markdown
# Receipt — Crisp Plugin Canary — YYYY-MM-DD

## Scope

- Canary level: 0/1
- Mode: observe_only / internal_note_only
- Auto-reply enabled: false

## What was tested

- Fixture/live event type:
- Signature validation:
- Idempotency:
- Anti-loop:

## Result

- Accepted events:
- Ignored events:
- Duplicate events:
- Errors:

## Safety

- Customer-facing replies sent: none
- Secrets printed: none
- Docker/VPS/gateway production changes: none

## Evidence

- Test command:
- Test output summary:
- Commit/branch if applicable:
```

---

## Task 9: Run verification suite

**Objective:** Prove the slice works and did not break generic webhooks.

**Commands:**

```bash
cd /opt/data/hermes_bruno_ingest/hermes-agent-v0.13.0
python -m pytest tests/gateway/test_crisp_plugin_integration.py -q
python -m pytest tests/gateway/test_webhook_adapter.py tests/gateway/test_webhook_signature_rate_limit.py -q
```

If the repo has a helper script and it is fast enough:

```bash
scripts/run_tests.sh tests/gateway/test_crisp_plugin_integration.py tests/gateway/test_webhook_adapter.py tests/gateway/test_webhook_signature_rate_limit.py
```

Expected: all targeted tests pass.

---

## Task 10: Commit local code only after tests pass

**Objective:** Preserve a clean checkpoint before any deployment discussion.

**Commands:**

```bash
cd /opt/data/hermes_bruno_ingest/hermes-agent-v0.13.0
git status --short
git add gateway/integrations/crisp.py gateway/platforms/webhook.py tests/gateway/test_crisp_plugin_integration.py tests/fixtures/crisp/ docs/plans/crisp-plugin-canary-config-example.md
git commit -m "feat: add Crisp plugin webhook canary receiver"
```

Expected:

- Commit created locally.
- No production restart or deployment.

---

## Approval gates after this plan

### Gate A — Implementation approval

Lucas must approve before coding against the Hermes repo.

### Gate B — Runtime/gateway approval

Lucas must approve before restarting any gateway or changing runtime config.

### Gate C — Crisp Marketplace approval

Lucas must approve before configuring the real Crisp Marketplace Plugin Hook endpoint.

### Gate D — Customer-facing reply approval

Lucas must approve separately before enabling any customer-facing auto-reply.

---

## Definition of done for Canary 0/1 implementation

- Crisp fixtures exist and contain no customer data.
- Normalizer tests pass.
- Signature verifier tests pass.
- Webhook adapter can accept `kind: crisp_plugin` route in observe-only mode.
- Self/operator/bot messages are ignored.
- Duplicate events are deduped.
- No agent run or customer reply occurs in observe-only mode.
- Safe config example exists.
- Canary receipt template exists.
- Targeted pytest suite passes.
- Brain receipt records results and confirms no production mutation.
