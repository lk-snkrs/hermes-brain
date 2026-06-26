# LK Supabase CPU Incident — n8n Workflows Paused

Timestamp UTC: 2026-05-28T14:48:05Z

Scope approved by Lucas in Telegram: pause the listed n8n workflows during Supabase database CPU/availability incident for project `cnjimxglpktznenpbail`.

## Paused workflows

All target workflow names were verified before deactivation. All returned HTTP 200 from n8n `/deactivate` endpoint and read-back `active=false`.

- `JE0T1S8RLEYqduli` — `LKSA-194 Code DDL v2`
- `LgwNeYyiUqKH0IGA` — `LKSA-458/464 DDL tamanho_principal EXEC`
- `hmJ4gcFCXUAv2vO4` — `LKSA-264: tamanho_principal migration`
- `vl4C26cY13rFIbxE` — `LKSA-265 Fetch Test`
- `yhu6FIGBwoVt36PD` — `LKSA-333 Migration`
- `C4v2U9qbfhlVSPCF` — `LK - n8n Error Alert → Telegram + Supabase`

## Post-action health probe

After pausing, Supabase REST probes still returned HTTP 503 Service Unavailable:

- `lk_crm_event_log`: HTTP 503 in ~3975 ms
- `orders`: HTTP 503 in ~4755 ms

Interpretation: pausing removed possible n8n DDL/error-log pressure, but the database remained unavailable immediately afterward. Next likely remediation is Supabase database/project restart from dashboard, then SQL diagnostics after recovery.

## Rollback

Reactivate the same workflow IDs via n8n API only after Supabase stabilizes and after reviewing whether DDL/migration webhook workflows should remain permanently disabled.
