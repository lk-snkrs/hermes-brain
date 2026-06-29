# Honcho best-practice implementation — 2026-06-28

Generated at UTC: `2026-06-28T19:43:25.071037+00:00`

## Objective

Implement the best-practice gaps found in the Honcho documentation audit: isolate gateway Honcho sessions per profile/AI peer, fix Lucas identity mapping for multi-user/group safety, add quality watchdog coverage, and reactivate gateways with validation.

## Changes applied

1. Patched the Hermes Honcho client with `sessionAiPeerPrefix` support.
   - Gateway sessions now can resolve as `<aiPeer>-agent-main-telegram-...` instead of every profile sharing the same chat session.
   - Legacy behavior is preserved when the flag is false.
   - Honcho's 100-character session-id limit is still enforced after prefixing.
2. Added Honcho client regression tests.
   - Same gateway key differs for `lk-stock` vs `lk-growth` when `sessionAiPeerPrefix=true`.
   - AI peer prefix wins over user peer prefix.
3. Updated all active profile `honcho.json` files.
   - `sessionAiPeerPrefix=true`.
   - `pinUserPeer=false`.
   - `userPeerAliases` present for Lucas.
   - `runtimePeerPrefix` set for unknown/non-Lucas runtime users.
   - `lc-claude-cli` uses `sessionStrategy=per-repo`.
4. Copied patched client to the active runtime copies used by main/default and specialist gateways.
5. Added silent-OK Honcho quality watchdog and scheduled it hourly.
6. Added a durable skill reference and recopied `honcho-memory-operations` into profile-local skill folders.
7. Restarted/reloaded managed gateways and validated runtime.

## Verification

| Check | Result |
|---|---:|
| Honcho client tests | 85 passed |
| Python compile | OK |
| Profiles with best-practice config keys | 17/17 |
| Local Honcho skill recopied | 16/16 profiles |
| Strict live gateway roster | 13/13 |
| `hermes memory status` samples | Honcho available |
| Honcho API/deriver recent critical log scan | no hits in 10m window |
| Honcho quality watchdog | silent-OK |
| Cron | 41 active jobs |
| Broker smoke Shopify/Supabase/Google/Klaviyo | OK |
| Secrets printed | false |
| External writes | 0 |
| Docker/VPS/Traefik changes | 0 |

## Notes

- Main/default gateway restart reported the known PID-1 race, but health, cron and strict roster validated OK afterward.
- Existing old shared Honcho sessions may remain in history; the fix affects new session resolution going forward.
- `hermes honcho status` is not available in this installed CLI; `hermes memory status` is the stable runtime check.

## Backup / rollback handles

- Honcho source/test backup: `/opt/data/backups/honcho-best-practice-all-20260628T193119Z`.
- Honcho JSON backup: `/opt/data/backups/honcho-json-pre-best-practice-20260628T193119Z`.
- Active runtime client backup: `/opt/data/backups/honcho-client-active-copies-20260628T193516Z`.
- Profile-local skill backup: `/opt/data/backups/honcho-skill-recopy-best-practice-20260628T194256Z`.

## State classification

| State | Result |
|---|---:|
| configured | OK |
| active | OK |
| functioning | OK |
| protocol_aware | OK |
| useful | improved; continue observing via watchdog and real-agent behavior |
| best-practice optimized | materially improved; remaining work is historical memory hygiene/contamination cleanup |
