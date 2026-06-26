# LK Supabase incident — targeted n8n pause receipt — 2026-06-01

Generated at: `2026-06-01T18:16:36.041936+00:00`

## Approved action

Lucas approved pausing only:

- `q8ZU4s8H50m7tFnP` — `LK - Envio de Email Novo Produto`

Lucas explicitly did **not** approve pausing:

- `VLOygUcX6xbQYQif` — `LK POS → WhatsApp Thank You`

## Execution

- Verified target workflow name before change.
- Deactivated target workflow through n8n API.
- Verified target post-state: `active=false`.
- Verified protected workflow post-state remained `active=true`.

## Safety

No secrets printed. No Supabase writes, restart, upgrade, DDL, cleanup, or POS workflow pause executed.

## Rollback

To rollback after Supabase stabilizes: reactivate workflow `q8ZU4s8H50m7tFnP` after confirming database health and retry behavior.
