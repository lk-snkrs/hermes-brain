# Cron Telegram Inline Buttons Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Enable the Mesa COO cron delivery to send Telegram inline buttons for decision messages (`Fazer`, `Não fazer`, `Agendar para depois`) without requiring the autonomous cron agent to call `clarify`.

**Architecture:** Add a small, explicit platform-action metadata channel for cron delivery. Cron output remains text by default; when a job opts in with structured button metadata, the scheduler passes that metadata to the live Telegram adapter. Telegram sends `reply_markup` using callback data under a new, non-clarify namespace. Callback handling converts the tap into a normal inbound user message/event so the next Hermes session can process the decision.

**Tech Stack:** Python, existing Hermes cron scheduler, gateway platform adapter, python-telegram-bot InlineKeyboardMarkup, pytest.

---

## Current code facts verified

- Telegram already supports inline keyboards for live `clarify` prompts in `gateway/platforms/telegram.py:2248-2297` via `send_clarify(...)`.
- Callback queries are already registered in `gateway/platforms/telegram.py:1293-1294`.
- Cron final delivery uses `_deliver_result(...)` in `cron/scheduler.py:489-650`.
- Live gateway delivery currently calls `runtime_adapter.send(chat_id, text_to_send, metadata=send_metadata)` at `cron/scheduler.py:596-598`.
- Standalone cron fallback uses `_send_to_platform(...)` in `tools/send_message_tool.py:518+`, and Telegram sends text through `_send_telegram(...)` at `tools/send_message_tool.py:757+`.
- Base adapter `send(...)` already accepts `metadata`, so no global interface break is needed.

---

## Non-goals / safety gates

- Do **not** restart the production gateway during implementation.
- Do **not** change Docker, compose, volumes, Traefik, or VPS networking.
- Do **not** require the cron agent to call `clarify`; cron jobs are autonomous and should not block waiting for user input.
- Do **not** make every cron response interactive. Opt-in only for decision jobs.
- Keep text fallback for non-Telegram platforms and standalone failures.

---

## Proposed metadata contract

Cron job prompt can emit a short structured footer or the job config can include metadata later. First implementation should avoid schema migration by parsing an explicit marker from cron content:

```text
<!-- HERMES_INLINE_BUTTONS:{"buttons":[{"label":"Fazer","value":"fazer"},{"label":"Não fazer","value":"nao_fazer"},{"label":"Agendar para depois","value":"agendar"}],"context":"mesa_coo:749ee30b51eb:2026-05-23:1"} -->
```

Scheduler strips the marker from visible content and passes:

```python
metadata={
    "thread_id": thread_id,
    "inline_buttons": {
        "buttons": [
            {"label": "Fazer", "value": "fazer"},
            {"label": "Não fazer", "value": "nao_fazer"},
            {"label": "Agendar para depois", "value": "agendar"},
        ],
        "context": "mesa_coo:749ee30b51eb:2026-05-23:1",
    },
}
```

Why marker-first: it avoids mutating cron job schema and preserves backwards compatibility. Later, move to first-class job config if needed.

---

## Task 1: Add marker parser tests

**Objective:** Parse and strip inline-button metadata safely from cron content.

**Files:**
- Modify: `cron/scheduler.py`
- Test: `tests/cron/test_scheduler_inline_buttons.py`

**Step 1: Write failing tests**

Create `tests/cron/test_scheduler_inline_buttons.py`:

```python
import json

from cron.scheduler import _extract_inline_buttons_marker


def test_extract_inline_buttons_marker_strips_visible_marker():
    content = 'Decisão 1/1\n<!-- HERMES_INLINE_BUTTONS:{"buttons":[{"label":"Fazer","value":"fazer"}],"context":"ctx"} -->\n'

    cleaned, payload = _extract_inline_buttons_marker(content)

    assert cleaned == "Decisão 1/1\n"
    assert payload == {"buttons": [{"label": "Fazer", "value": "fazer"}], "context": "ctx"}


def test_extract_inline_buttons_marker_ignores_invalid_json():
    content = "Oi\n<!-- HERMES_INLINE_BUTTONS:not-json -->"

    cleaned, payload = _extract_inline_buttons_marker(content)

    assert cleaned == content
    assert payload is None


def test_extract_inline_buttons_marker_requires_button_list():
    content = 'Oi\n<!-- HERMES_INLINE_BUTTONS:{"context":"ctx"} -->'

    cleaned, payload = _extract_inline_buttons_marker(content)

    assert cleaned == content
    assert payload is None
```

**Step 2: Run to verify failure**

Run:

```bash
cd /opt/hermes && python -m pytest tests/cron/test_scheduler_inline_buttons.py -q -o 'addopts='
```

Expected: FAIL because `_extract_inline_buttons_marker` does not exist.

**Step 3: Implement parser**

In `cron/scheduler.py`, add near delivery helpers:

```python
_INLINE_BUTTONS_RE = re.compile(
    r"\n?<!--\s*HERMES_INLINE_BUTTONS:(?P<payload>\{.*?\})\s*-->\s*$",
    re.DOTALL,
)


def _extract_inline_buttons_marker(content: str) -> tuple[str, Optional[dict]]:
    match = _INLINE_BUTTONS_RE.search(content or "")
    if not match:
        return content, None
    try:
        payload = json.loads(match.group("payload"))
    except Exception:
        return content, None
    buttons = payload.get("buttons") if isinstance(payload, dict) else None
    if not isinstance(buttons, list) or not buttons:
        return content, None
    normalized = []
    for item in buttons[:5]:
        if not isinstance(item, dict):
            continue
        label = str(item.get("label", "")).strip()
        value = str(item.get("value", label)).strip()
        if label and value:
            normalized.append({"label": label[:60], "value": value[:48]})
    if not normalized:
        return content, None
    payload = {"buttons": normalized, "context": str(payload.get("context", ""))[:80]}
    return content[: match.start()] + content[match.end():], payload
```

Also add imports if missing:

```python
import json
import re
```

**Step 4: Run tests**

Expected: PASS.

---

## Task 2: Pass inline metadata through live cron delivery

**Objective:** When a cron output has button metadata, pass it to the live adapter metadata without disrupting thread delivery.

**Files:**
- Modify: `cron/scheduler.py:489-650`
- Test: `tests/cron/test_scheduler_inline_buttons.py`

**Step 1: Add failing test**

Use a fake adapter and monkeypatch target resolution/config enough to exercise `_deliver_result(...)` live adapter path.

```python
class FakeLoop:
    def is_running(self):
        return True

class FakeFuture:
    def __init__(self, result):
        self._result = result
    def result(self, timeout=None):
        return self._result

class FakeResult:
    success = True

class FakeAdapter:
    def __init__(self):
        self.calls = []
    async def send(self, chat_id, content, metadata=None):
        self.calls.append((chat_id, content, metadata))
        return FakeResult()


def test_deliver_result_passes_inline_buttons_to_live_adapter(monkeypatch):
    import cron.scheduler as sched
    from gateway.config import Platform

    adapter = FakeAdapter()
    job = {
        "id": "job1",
        "name": "Mesa COO",
        "deliver": "origin",
        "origin": {"platform": "telegram", "chat_id": "123", "thread_id": "7"},
    }
    content = 'Decisão\n<!-- HERMES_INLINE_BUTTONS:{"buttons":[{"label":"Fazer","value":"fazer"}],"context":"ctx"} -->'

    monkeypatch.setattr(sched, "_resolve_delivery_targets", lambda _job: [{"platform": "telegram", "chat_id": "123", "thread_id": "7"}])
    monkeypatch.setattr(sched, "load_gateway_config", lambda: object())
    monkeypatch.setattr(sched, "safe_schedule_threadsafe", lambda coro, loop: FakeFuture(FakeResult()))

    err = sched._deliver_result(job, content, adapters={Platform.TELEGRAM: adapter}, loop=FakeLoop())

    assert err is None
    assert adapter.calls
    chat_id, text, metadata = adapter.calls[0]
    assert "HERMES_INLINE_BUTTONS" not in text
    assert metadata["thread_id"] == "7"
    assert metadata["inline_buttons"]["buttons"][0]["label"] == "Fazer"
```

**Step 2: Implement**

In `_deliver_result(...)`, after wrapping but before media extraction:

```python
inline_buttons = None
clean_delivery_content, inline_buttons = _extract_inline_buttons_marker(delivery_content)
```

Then use `clean_delivery_content` for media extraction.

When building `send_metadata`:

```python
send_metadata = {}
if thread_id:
    send_metadata["thread_id"] = thread_id
if inline_buttons and platform_name == "telegram":
    send_metadata["inline_buttons"] = inline_buttons
send_metadata = send_metadata or None
```

**Step 3: Run targeted tests**

```bash
cd /opt/hermes && python -m pytest tests/cron/test_scheduler_inline_buttons.py tests/cron/test_jobs.py -q -o 'addopts='
```

Expected: PASS.

---

## Task 3: Render Telegram inline buttons from `metadata["inline_buttons"]`

**Objective:** Add Telegram adapter support for non-clarify inline buttons during normal sends.

**Files:**
- Modify: `gateway/platforms/telegram.py`
- Test: `tests/gateway/test_telegram_inline_buttons.py` or existing Telegram test module.

**Step 1: Add helper**

Near `send_clarify(...)`, add:

```python
def _inline_buttons_markup_from_metadata(self, metadata: Optional[Dict[str, Any]]):
    payload = (metadata or {}).get("inline_buttons")
    if not isinstance(payload, dict):
        return None
    rows = []
    context = str(payload.get("context", ""))[:80]
    for idx, button in enumerate(payload.get("buttons") or []):
        if not isinstance(button, dict):
            continue
        label = str(button.get("label", "")).strip()[:60]
        value = str(button.get("value", label)).strip()[:48]
        if not label or not value:
            continue
        callback_data = f"ib:{context}:{idx}:{value}"
        if len(callback_data.encode("utf-8")) > 64:
            callback_data = f"ib:{idx}:{value}"[:64]
        rows.append([InlineKeyboardButton(label, callback_data=callback_data)])
    if not rows:
        return None
    return InlineKeyboardMarkup(rows)
```

**Step 2: Wire into `TelegramAdapter.send(...)`**

Find the main text send path in `gateway/platforms/telegram.py` and add `reply_markup` when present:

```python
reply_markup = self._inline_buttons_markup_from_metadata(metadata)
...
if reply_markup is not None:
    kwargs["reply_markup"] = reply_markup
```

Important: only attach to the first/primary text message, not media-only sends or every chunk of a long split message.

**Step 3: Unit test**

Use a fake bot capturing `send_message` kwargs. Verify `reply_markup` is present when metadata includes inline buttons and absent otherwise.

**Step 4: Run tests**

```bash
cd /opt/hermes && python -m pytest tests/gateway -k 'telegram and inline' -q -o 'addopts='
```

Expected: PASS.

---

## Task 4: Handle non-clarify callback namespace

**Objective:** Convert `ib:` button taps into a normal gateway event/session message instead of being ignored.

**Files:**
- Modify: `gateway/platforms/telegram.py`
- Test: Telegram callback tests.

**Step 1: Inspect current callback handler**

Read `_handle_callback_query(...)`. It already handles `cl:<clarify_id>:<idx|other>` for clarify and likely model-picker callbacks.

**Step 2: Add branch for `ib:`**

Behavior:

- `await query.answer()` to stop Telegram spinner.
- Optionally edit message reply markup to remove buttons after tap.
- Emit an inbound message equivalent to:

```text
Botão selecionado: Fazer
Contexto: mesa_coo:749ee30b51eb:2026-05-23:1
Valor: fazer
```

For the Mesa COO skill, this is enough for the next Hermes session to interpret and proceed.

**Step 3: Add tests**

Verify:

- `ib:` callback calls the inbound message callback once.
- It does not touch `_clarify_state`.
- Unknown/malformed callback returns gracefully.

---

## Task 5: Standalone fallback support or graceful degradation

**Objective:** Decide whether standalone cron delivery should support inline buttons.

**Recommended first version:** graceful degradation only.

Reason: production cron delivery normally runs inside gateway with live adapters. The standalone path uses `tools/send_message_tool.py` and has no callback handling context beyond the bot token. Buttons sent standalone would render but could be unhandled if the gateway is down, so they may mislead Lucas.

Implementation:

- Live adapter path: send buttons.
- Standalone fallback: strip marker, send text only, and log a debug/warning if button metadata was present.

Test:

- `_deliver_result` with no live adapter does not leak marker into Telegram text.

---

## Task 6: Update Mesa COO cron prompt only after code tests pass

**Objective:** Add the marker footer to Mesa COO decision outputs.

**Files/Jobs:**
- Cron job: `749ee30b51eb`
- Skill: `mesa`

Prompt footer example:

```text
Ao emitir uma decisão que deve ter botões inline no Telegram, acrescente ao final exatamente uma linha HTML-comment marker:
<!-- HERMES_INLINE_BUTTONS:{"buttons":[{"label":"Fazer","value":"fazer"},{"label":"Não fazer","value":"nao_fazer"},{"label":"Agendar para depois","value":"agendar"}],"context":"mesa_coo:749ee30b51eb:${YYYY-MM-DD}:1"} -->
```

Verification:

- Trigger cron manually in a test profile or local mocked delivery first.
- Confirm marker is not visible to Lucas.
- Confirm buttons render.
- Confirm callback produces an inbound decision message.

---

## Task 7: Production deployment gate

**Objective:** Deploy safely only after Lucas approves.

Required before restart/deploy:

- Show diff.
- Show test results.
- Create rollback command/commit reference.
- Confirm no Docker/compose/network changes.
- Ask Lucas for explicit deploy/restart approval.

Verification after approved restart:

- Gateway logs show Telegram connected.
- Local API/webhook health remains OK if enabled.
- Send a manual Mesa test decision with buttons.
- Press each button once in a test message and verify no crash/no duplicate sessions.

---

## Risks

- Telegram `callback_data` max 64 bytes: keep context short or store context server-side later.
- Long cron messages may be chunked: attach buttons only to the first or final decision chunk, not every chunk.
- Cron wrap text (`Cronjob Response: ...`) can make buttons feel attached to the wrapper, not the decision. Consider disabling wrap for Mesa only later if needed.
- Callback tap is not the same as `clarify`; it creates a new inbound event and may start a new session. This is acceptable for Mesa if the context field is explicit.

---

## Acceptance criteria

- Mesa COO cron message renders Telegram inline buttons for a decision.
- The HTML marker is never visible in delivered text.
- Button tap is acknowledged and converted into a processable Hermes inbound message.
- Non-Telegram targets receive clean text fallback.
- No production restart/deploy occurs without explicit approval.
