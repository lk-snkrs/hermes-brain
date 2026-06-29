<!-- archived_reason: Lucas decided on 2026-06-28 not to use Linear; integration removed from central broker inventory/smoke. -->

# Approval Packet — Linear API key rotation for Hermes central auth broker — 2026-06-28

## Status

Archived/stale — no action. Lucas decided not to use Linear.

## Context

After central auth broker repair, all major CLI/MCP smokes passed except Linear.

## Evidence

- Doppler `lc-keys/prd` contains `LINEAR_API_KEY` by name.
- Runtime injection exists for `LINEAR_API_KEY`.
- Read-only Linear GraphQL viewer probe returns HTTP `401` with raw API-key header.
- Bearer header variant returns HTTP `400` and is not the correct Personal API Key format.
- No secret values/previews printed; `values_printed=false`.

## Interpretation

This is not a missing-secret or missing-runtime problem. It is an invalid/revoked/unauthorized Linear token problem.

## Requested action

Lucas should create a new Linear Personal API Key at:

https://linear.app/settings/account/security

Then paste it to Hermes only if he wants Hermes to store it in Doppler now, or store it directly in Doppler as `LINEAR_API_KEY` under `lc-keys/prd`.

## Approved safe update path if Lucas pastes the token

1. Do not echo, preview, or persist token in files/logs.
2. Update Doppler secret `LINEAR_API_KEY` in `lc-keys/prd` through the authorized Doppler helper/API.
3. Verify presence by secret name only.
4. Run read-only GraphQL viewer smoke.
5. Run `/opt/data/home/.local/bin/hermes-cli-integrations smoke linear`.
6. Update the central auth broker report/receipt with status only.

## Non-actions

- No Linear writes.
- No issue/comment/project/status mutation.
- No external business writes.
- No copying token to profile `.env` files.

## Rollback

If a pasted token is wrong, replace `LINEAR_API_KEY` again in Doppler with a valid Personal API Key. Do not restore any old token from chat/logs; old value was not printed or stored in Brain.
