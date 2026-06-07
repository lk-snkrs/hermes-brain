# Hermes v0.16 Stage 1 — Candidate Runtime Validation

- Date: 2026-06-06T13:55:50+00:00
- Owner: default Hermes profile
- Request: Lucas approved Stage 1 with “Sim executar:..”
- Scope approved: prepare and validate a parallel/isolated Hermes v0.16 candidate runtime.
- Scope NOT approved: production swap, gateway restart, Docker/VPS/Traefik/API/dashboard changes, live config migration, `/opt/hermes` replacement.

## Verdict

Stage 1 candidate runtime is prepared and passes local validation after a candidate-local guardrail patch for cron inline buttons.

Recommendation: do not swap production yet. The official tag `v2026.6.5` / Hermes `v0.16.0` is usable as a candidate only with the local cron inline-button guardrail patch preserved or upstream-confirmed. Ask Lucas for a separate scoped approval before any live swap/restart.

## Runtime inventory

- Live Hermes CLI: `/opt/hermes/.venv/bin/hermes`
- Live runtime observed before Stage 1: Hermes Agent `v0.15.2 (2026.5.29.2)`
- Live config: `/opt/data/config.yaml`
- Target release: `NousResearch/hermes-agent` tag `v2026.6.5`
- Target commit: `d6b9cfa3e1f460f5729553ef42b174da28b765c7`
- Candidate root: `/opt/data/hermes-v016-candidate-20260606`
- Candidate source: `/opt/data/hermes-v016-candidate-20260606/src`
- Candidate venv: `/opt/data/hermes-v016-candidate-20260606/src/.venv`
- Candidate install: editable install with extras `[messaging,cron,cli,pty,mcp,web,voice,google]`

## Actions performed

1. Cloned official tag `v2026.6.5` into the isolated candidate directory.
2. Created an isolated venv under the candidate source tree.
3. Installed Hermes v0.16.0 candidate into that venv.
4. Ran version/config/import/compile checks with `HERMES_HOME` controlled.
5. Ran migration preview against a copied config under `/tmp/hermes-v016-migrate-preview-final`.
6. Compared critical guardrails, including cron delivery, Telegram reply markup, context compression, config validation, and fallback-related paths.
7. Detected that official v0.16 candidate lacked the local `HERMES_INLINE_BUTTONS` cron marker handling present in a prior local v0.15.1 path and important for clean Mesa COO Telegram decision cards.
8. Applied a candidate-local patch only, not production, to restore clean cron inline-button delivery semantics.
9. Re-ran selected smoke/unit tests after the patch.

## Candidate-local patch applied

Files modified in the candidate only:

- `/opt/data/hermes-v016-candidate-20260606/src/cron/scheduler.py`
- `/opt/data/hermes-v016-candidate-20260606/src/gateway/platforms/telegram.py`
- `/opt/data/hermes-v016-candidate-20260606/src/tools/send_message_tool.py`

Patch purpose:

- Strip trailing hidden `<!-- HERMES_INLINE_BUTTONS:{...} -->` markers before delivery.
- Convert marker payload into structured `inline_buttons` metadata.
- Pass metadata through runtime adapter and standalone send paths.
- Render Telegram native inline keyboard buttons with compact `cj:<context>:<value>` callback data.
- Keep user-facing Telegram output clean: no hidden marker text shown to Lucas.

Important: this patch is in the isolated candidate tree only. It did not alter `/opt/hermes`, live gateway code, Docker images, Traefik, or production services.

## Checks and evidence

### Candidate version

Command:

```bash
cd /opt/data/hermes-v016-candidate-20260606/src
HERMES_HOME=/opt/data env -u PYTHONPATH .venv/bin/hermes --version
```

Observed:

- `Hermes Agent v0.16.0 (2026.6.5)`
- Project: `/opt/data/hermes-v016-candidate-20260606/src`
- Python: `3.13.5`

Status: PASS

### Candidate config check

Command:

```bash
HERMES_HOME=/opt/data env -u PYTHONPATH .venv/bin/hermes config check
```

Observed:

- Config check exited 0.
- Config version shows `24 → 27 (update available)`.
- This indicates migration would be needed before live cutover, but Stage 1 did not migrate the live config.

Status: PASS with migration requirement noted

### Migration preview

Command summary:

```bash
rm -rf /tmp/hermes-v016-migrate-preview-final
mkdir -p /tmp/hermes-v016-migrate-preview-final
cp /opt/data/config.yaml /tmp/hermes-v016-migrate-preview-final/config.yaml
HERMES_HOME=/tmp/hermes-v016-migrate-preview-final .venv/bin/hermes config check
sha256sum /opt/data/config.yaml
sha256sum /tmp/hermes-v016-migrate-preview-final/config.yaml
```

Observed:

- `preview_config_check_exit_0`
- Live config SHA256: `1ffd8ffe2f597a64a584d21726152155cd1a74fdd7dd92955bc078d003fc2fba`
- Preview config SHA256: `1ffd8ffe2f597a64a584d21726152155cd1a74fdd7dd92955bc078d003fc2fba`

Status: PASS. The live config was not changed.

### Critical imports

Modules imported in candidate venv:

- `gateway.run`
- `gateway.platforms.telegram`
- `cron.scheduler`
- `cron.jobs`
- `agent.context_compressor`
- `agent.auxiliary_client`
- `gateway.platforms.api_server`
- `tools.registry`
- `tools.send_message_tool`

Observed: `critical_imports_ok 9`

Status: PASS

### Py compile

Files compiled:

- `cron/scheduler.py`
- `cron/jobs.py`
- `gateway/platforms/telegram.py`
- `tools/send_message_tool.py`
- `agent/context_compressor.py`
- `agent/auxiliary_client.py`
- `hermes_cli/config.py`

Observed: `py_compile_ok`

Status: PASS

### Inline button guardrail smoke

Validated behavior:

- input content with trailing `HERMES_INLINE_BUTTONS` marker is cleaned;
- cleaned content no longer contains `HERMES_INLINE_BUTTONS`;
- metadata is extracted;
- Telegram keyboard is generated;
- callback data is compact and compatible: `cj:mesa_coo:approve`, `cj:mesa_coo:defer`.

Observed: `inline_marker_clean_delivery_ok`

Status: PASS after candidate-local patch

### Selected pytest matrix

Command:

```bash
.venv/bin/python -m pytest -q -o addopts='' \
  tests/gateway/test_telegram_noise_filter.py \
  tests/gateway/test_telegram_send_path_health.py \
  tests/gateway/test_telegram_send_draft_format.py \
  tests/cron/test_scheduler.py \
  tests/cron/test_jobs.py \
  tests/cron/test_cron_no_agent.py \
  tests/cron/test_cron_context_from.py \
  tests/agent/test_context_compressor.py \
  tests/agent/test_context_compressor_summary_continuity.py \
  tests/hermes_cli/test_config_validation.py \
  tests/hermes_cli/test_config_env_expansion.py
```

Observed:

- `395 passed in 19.24s`

Status: PASS

## Guardrail comparison

### Mesa COO / Telegram actionable alerts

Status: PASS after candidate-local patch.

Evidence:

- hidden inline marker parser exists in candidate-local `cron/scheduler.py`;
- metadata is passed to runtime adapter and standalone send paths;
- Telegram adapter renders native inline keyboard with `reply_markup`;
- smoke test confirmed marker is stripped from user-facing text.

Risk if unpatched official tag is used directly:

- `HERMES_INLINE_BUTTONS` marker may leak into Telegram text or not produce native buttons.
- Mesa COO decision cards would be less clean/actionable for Lucas.

### Telegram noise filtering / delivery path

Status: PASS.

Evidence:

- `tests/gateway/test_telegram_noise_filter.py` passed.
- `tests/gateway/test_telegram_send_path_health.py` passed.
- `tests/gateway/test_telegram_send_draft_format.py` passed.

### Cron delivery / no-agent / context_from

Status: PASS.

Evidence:

- `tests/cron/test_scheduler.py` passed.
- `tests/cron/test_jobs.py` passed.
- `tests/cron/test_cron_no_agent.py` passed.
- `tests/cron/test_cron_context_from.py` passed.

### Context compression / summary continuity

Status: PASS.

Evidence:

- `tests/agent/test_context_compressor.py` passed.
- `tests/agent/test_context_compressor_summary_continuity.py` passed.

### Config validation/env expansion

Status: PASS with migration noted.

Evidence:

- `tests/hermes_cli/test_config_validation.py` passed.
- `tests/hermes_cli/test_config_env_expansion.py` passed.
- Candidate config check exited 0.
- Config version update available: `24 → 27`.

### Rollback

Status: PASS by design.

Evidence:

- Production runtime was not changed.
- `/opt/hermes` was not modified.
- Live config was not modified.
- Rollback remains the current live runtime: Hermes v0.15.2.

## Non-actions explicitly preserved

- No production swap.
- No gateway restart.
- No Docker build/pull/restart.
- No VPS/Traefik/API/dashboard change.
- No live config migration.
- No writes to `/opt/hermes`.
- No external production writes.

## Remaining risks before production cutover

1. The candidate tree is not a pristine official tag anymore; it contains a local guardrail patch. If the upgrade proceeds, decide whether to:
   - carry this patch into the production artifact, or
   - confirm an upstream equivalent fix before deploying vanilla v0.16.
2. Live Telegram round-trip with actual inline buttons was not executed; Stage 1 stayed local/read-only.
3. Config migration from version 24 to 27 was not applied live and must be handled in a scoped cutover plan with backup/rollback.
4. Full gateway restart behavior and connected platform initialization were not tested against production services.

## Recommended next step

Prepare Stage 2 approval packet for a controlled cutover, but do not execute it without Lucas’s explicit approval.

Minimum Stage 2 plan should include:

1. backup `/opt/data/config.yaml`, profile data, cron state, and relevant runtime metadata;
2. preserve or upstream-verify the inline-button guardrail patch;
3. stage production artifact without replacing live runtime until final checkpoint;
4. run config migration with backup and readback;
5. perform gateway restart in a maintenance window;
6. validate Telegram home channel, Mesa COO action buttons, API server, webhook, cron jobs, and profile watchdogs;
7. rollback immediately to `/opt/hermes` v0.15.2 if any critical guardrail fails.
