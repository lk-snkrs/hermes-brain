# Honcho best-practice docs audit — 2026-06-28

Generated at UTC: `2026-06-28T19:15:48.528410+00:00`

## Question

Lucas asked whether Hermes is using Honcho in the best way according to current Honcho/Hermes documentation.

## Sources checked

- Hermes Agent docs: `Honcho Memory`.
- Hermes Agent docs: `Memory Providers` / Honcho provider reference.
- Honcho docs: `Hermes Agent + Honcho`.
- Honcho docs: `Architecture & Intuition`.
- Honcho docs: `Reasoning`.
- Honcho docs: `Design Patterns`.
- Honcho docs: `Get Context`.
- Hermes Honcho provider README/config reference.
- Live local evidence: `/opt/data*/honcho.json`, `hermes honcho status`, `hermes memory status`, Honcho container health/logs.

## Live configuration summary

- Workspace: `lucas-hermes` shared across profiles.
- User peer: `lucas` shared across profiles.
- AI peer: distinct per profile, e.g. `hermes-default`, `lk-stock`, `lk-growth`, `lk-shopify`.
- Recall mode: `hybrid`.
- Write frequency: `async`.
- Save messages: `true`.
- Context cadence: every turn (`contextCadence=1`).
- Dialectic cadence: every 2 turns (`dialecticCadence=2`).
- Dialectic depth: `2`.
- Base reasoning: `low`; heuristic cap resolves to default `high`.
- Context budget: `2000` tokens.
- Observation mode: `unified`, effective `user(me=True, others=False)` and `ai(me=False, others=True)`.
- User peer pinning: `pinUserPeer=true` in all sampled/all-profile config.
- Honcho containers: API, deriver, Redis, database up; API/database/Redis healthy.

## What matches best practice

1. **Shared workspace + stable user peer + separate AI peers** matches Honcho/Hermes multi-profile design: one Lucas memory with agent-specific AI identities.
2. **`hybrid` recall** matches Hermes recommendation for active use because it provides both automatic context and explicit tools.
3. **`async` writes** match the recommended live-gateway behavior.
4. **`contextCadence=1`, `contextTokens=2000`** are good defaults for continuity without huge prompt bloat.
5. **`dialecticDepth=2`, `dialecticCadence=2`, `base=low`** is a sensible controlled configuration: better than shallow storage, not an expensive max setting.
6. **`observationMode=unified`** is a deliberate anti-noise choice and aligns with Hermes docs as the single-observer/pool mode.
7. **Protocol-aware boot + local skill propagation** is now aligned with Lucas's expected operational use: agents are instructed to consult Honcho when history changes decisions.

## Main gaps / not “best possible” yet

### 1. Gateway session collision across many agents

Current installed Hermes Honcho client resolves `gateway_session_key` before applying `sessionPeerPrefix`. That means multiple specialist profiles talking to the same Telegram DM/chat can land in the same Honcho session such as `agent-main-telegram-dm-...` even though they have distinct `aiPeer` values.

Live evidence: Honcho API logs showed an `ObserverException`: cannot create a session with 11 observers; maximum allowed is 10 observers per session. This directly matches the documented/design issue that AI peers sharing a workspace and gateway chat can collide on one session.

Impact: this is likely the strongest reason agents appeared to stop using Honcho or got degraded context. It can produce session update failures and cross-agent context contamination.

Best-practice direction: isolate gateway Honcho sessions per AI peer/profile. The currently installed client does not do that for gateway keys. Fix requires Hermes provider patch or upgrade to a version with AI-peer/profile-aware gateway session naming.

### 2. `pinUserPeer=true` everywhere is only ideal for single-operator bots

Docs say `pinUserPeer=true` is best when the gateway is effectively “just me”. Some profiles have multiple allowed users or group-chat surfaces. In those cases, best practice is not to pin every runtime user to `lucas`; instead map Lucas runtime IDs to `lucas` via `userPeerAliases` and namespace unknown/other users with `runtimePeerPrefix`.

Impact: if non-Lucas humans talk to those bots, their messages can pollute Lucas's user peer.

Best-practice direction: classify profiles as single-Lucas vs multi-user/group. Keep `pinUserPeer=true` only for single-Lucas bots. For group/multi-user profiles, switch to aliases + prefix after a scoped migration plan.

### 3. Search relevance/noise is still weak

Current Honcho semantic search can return operational order/customer/webhook details when asking governance questions. The peer card is now curated, but raw search still shows contamination.

Impact: Honcho is functioning but not maximally useful; agents need guardrails to treat noisy context as noise and prefer Brain/source-of-truth for domain facts.

Best-practice direction: add a hygiene layer: ingestion filtering for operational payloads, cleanup candidates for sensitive order/customer facts, and evaluation metrics for relevance/contamination before increasing context budget or reasoning depth.

### 4. CLI/session strategy could be better per profile

For Telegram gateway, the gateway session key overrides `sessionStrategy`. For CLI/coding profiles, `per-session` fragments memory by invocation. Hermes docs often recommend `per-repo` for coder profiles and `per-directory` for general CLI work.

Impact: CLI-only or coding profiles may not accumulate project memory optimally.

Best-practice direction: set `lc-claude-cli`/coding-like profiles to `per-repo`; keep Telegram specialists governed by fixed gateway-session isolation once collision is fixed.

### 5. Standalone Honcho CLI is absent

`honcho` CLI is not installed/available as a direct command in this runtime, although Hermes commands and Honcho tools work. This is not blocking normal Hermes use, but it limits direct low-level inspection using `honcho peer inspect`, `honcho session context`, etc.

Best-practice direction: optional install/expose Honcho CLI read-only tooling, or rely on Hermes `honcho status` plus custom SDK probes.

## Verdict

Current setup is **good and operational**, but **not yet the best possible Honcho setup**.

Score by state:

| State | Result |
|---|---:|
| configured | OK |
| active | OK |
| functioning | mostly OK |
| protocol_aware | OK after repair |
| useful | partial / needs improvement |
| best-practice optimized | not yet |

The most important fix is **gateway session isolation per AI peer/profile**, because live logs show the 10-observer limit being hit. The second priority is **multi-user identity mapping** for group/shared bots. The third is **memory hygiene/search relevance**.

## Recommended next actions

1. Prepare a scoped approval packet to patch or upgrade Hermes Honcho gateway session resolution so each profile/AI peer gets its own gateway Honcho session.
2. Audit which Telegram profiles are single-Lucas vs group/multi-user; keep `pinUserPeer=true` only for single-Lucas and migrate multi-user profiles to `userPeerAliases` + `runtimePeerPrefix`.
3. Add Honcho quality watchdog metric: observer errors, dialectic/embedding errors, search contamination ratio, peer-card hygiene, and “agent used Honcho when history-dependent”.
4. Keep current depth/cadence/context budget unchanged until noise and session collision are fixed. Do not raise to `medium/high/max` yet.

## Safety

- Secrets printed: `false`.
- External writes: `0`.
- Docker/VPS/Traefik changes: `0`.
- This report is advisory; no runtime patch was applied.
