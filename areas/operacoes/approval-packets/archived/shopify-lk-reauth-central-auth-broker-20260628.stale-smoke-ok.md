
> **Superseded status — 2026-06-28:** do not use this historical artifact as current Shopify auth truth. The Central Integration Auth Broker now forces central CLI `HOME=/opt/data/home` plus central XDG paths, and `hermes-cli-integrations smoke shopify_lk` uses `method=broker_shopify_store_execute`. Fresh control-plane and profile smoke returned `rc=0/status=ok` with `values_printed=false`. Reauth/OAuth is not currently pending unless a fresh broker smoke fails again after retry outside a reload window.

# Approval Packet — Shopify LK reauth via Hermes central integration auth broker — 2026-06-28

## Status

`waiting_control_plane_reauth`

## Context

Lucas corrigiu que o OAuth Shopify **não deve ser feito diretamente pelo agente/tarefa**. O fluxo correto é usar o **Hermes Central Integration Auth Broker** e a skill/procedimento de integração.

A tarefa operacional pendente é permitir read-only Shopify Admin GraphQL para `lk-sneakerss.myshopify.com`, para depois fazer readback de `webhookSubscriptions` ligado ao sync de estoque.

## Evidence gathered through broker

Commands executed through governed surfaces only:

```bash
/opt/data/home/.local/bin/hermes-cli-integrations smoke shopify_lk
/opt/data/home/.local/bin/hermes-cli-run --audit-json shopify store execute --store lk-sneakerss.myshopify.com --json --query '{ shop { name myshopifyDomain } }'
```

Observed sanitized result:

- `shopify_lk` smoke: `status=failed`, `method=shopify_store_execute`, `rc=1`, `values_printed=false`.
- read-only `store execute`: failed with `No stored app authentication found for lk-sneakerss.myshopify.com`.
- audit JSON: `integration=shopify`, `command_family=store execute`, `mode=read_only`, `exit_code=1`, `secret_values_printed=false`, `values_printed=false`.
- Broker policy tests passed: `python3 -m unittest /opt/data/scripts/tests/test_hermes_cli_run.py -v` → `5 tests OK`.

## Requested control-plane action

Reauthenticate `shopify_lk` **through the central integration auth broker / controlled operator procedure**, not from an arbitrary agent task.

Required store:

```text
lk-sneakerss.myshopify.com
```

Required read-only scopes for the pending audit/readback:

```text
read_products,read_orders,read_inventory,read_locations,read_webhooks
```

## Non-actions / guardrails

- Do not copy `.env`, `auth.json`, OAuth cache, token files, refresh tokens, app secrets, or credential files between profiles.
- Do not print OAuth URLs containing secrets, tokens, token previews, passwords, or cache contents.
- Do not use raw Shopify Admin HTTP as normal fallback.
- Do not run Shopify mutations.
- Do not write Tiny, Shopify, Supabase, Klaviyo, WhatsApp, Gmail, or external systems as part of reauth.

## Verification after reauth

After the broker/control-plane reauth is complete, verify with:

```bash
/opt/data/home/.local/bin/hermes-cli-integrations smoke shopify_lk
/opt/data/home/.local/bin/hermes-cli-run --audit-json shopify store execute --store lk-sneakerss.myshopify.com --json --query '{ shop { name myshopifyDomain } }'
```

Expected:

- smoke `shopify_lk`: `status=ok`;
- audit: `exit_code=0`, `mode=read_only`, `values_printed=false`.

## Follow-up readback task

Only after smoke is OK, run read-only webhook readback:

```graphql
{
  webhookSubscriptions(first: 50) {
    nodes {
      id
      topic
      endpoint { __typename }
    }
  }
}
```

Report only IDs/topics/endpoint type/status; no secrets.

## Rollback / mitigation

If reauth is wrong or over-scoped, remove/revoke the stored Shopify CLI auth through the controlled broker procedure and rerun `smoke shopify_lk` to confirm expected failure/absence.

## Owner / next action

Owner: Hermes central integration auth broker / control-plane operator.

Next action: perform governed Shopify LK reauth, then hand back to `lk-stock` for read-only `webhookSubscriptions` readback.

---

## Archived status — 2026-06-28

Archived as stale/no-action by Hermes default after live revalidation. `shopify_lk` smoke passes via the central broker from both default and LK Stock environments, and `hermes-cli-run --audit-json shopify store execute ...` returns `exit_code=0` / `status=ok` with `values_printed=false`. Do not treat this packet as an active approval need unless a fresh smoke fails again.

