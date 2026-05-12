# LK Klaviyo CRM Draft Readiness Watcher, 2026-05-11

Generated at: `2026-05-12T00:07:41.249010+00:00`

## Veredito

Status: `ready_for_lucas_review_no_send`

LK-AUTO-005 avançou para um watcher manual/read-only de readiness: ele valida IDs e estado do rascunho Klaviyo, mas não envia, não agenda, não cria campanha, não ativa flow e não expõe PII.

## Snapshot

- Checks: 10
- Fails: 0
- Warnings: 0
- Campaign status: `Draft`
- Campaign scheduled_at: `None`
- Campaign send_time: `None`
- Perfis aprovados enviados ao import original: 9
- Emails únicos no import original: 9
- Campaign sends: 0
- Campaign schedules: 0
- Customer contacts: 0
- Production writes: 0

## Objetos Klaviyo verificados por ID/nome

- list_name: `LK Phase 5 P1 Loja Física Recompra 2026-05-11`
- list_id: `U8YCCE`
- template_name: `LK Phase 5 P1 Curadoria Loja Física 2026-05-11`
- template_id: `XUSEtu`
- campaign_name: `LK Phase 5 P1 Curadoria Loja Física 2026-05-11, DRAFT`
- campaign_id: `01KRC1DPTY615GF5FNBPXMPKY6`
- campaign_message_id: `01KRC1DPVAMF0M9SRSR7RDQX1G`

## Checks

- OK: `list_get_readonly` — Klaviyo list can be read by ID.
- OK: `template_get_readonly` — Klaviyo template can be read by ID; warn only because the campaign can still exist without template linked via API.
- OK: `campaign_get_readonly` — Klaviyo campaign can be read by ID.
- OK: `campaign_is_draft` — Campaign must remain Draft.
- OK: `campaign_not_scheduled` — Campaign must not be scheduled.
- OK: `campaign_send_time_empty` — Campaign send_time must be empty.
- OK: `campaign_not_archived` — Campaign should not be archived if Lucas needs to inspect the draft.
- OK: `no_raw_pii_output` — Report uses only counts and Klaviyo object IDs; no customer emails/names are emitted.
- OK: `no_deep_link_guessed` — No Klaviyo UI deep link is generated; use verified IDs/names only.
- OK: `send_schedule_mutations_blocked` — Script only uses GET endpoints and does not call campaign send/schedule/update/create endpoints.

## Guardrails

- No campaign send executed.
- No campaign schedule executed.
- No campaign/list/template mutation executed by this watcher.
- No flow activation executed.
- No SMS/WhatsApp/customer contact executed.
- No raw PII emitted into Brain or Telegram.
- No unverified Klaviyo deep link generated.

## Próximo gate

Lucas can review verified IDs/names and decide adjust, pause, or explicitly approve a separate send packet. This watcher itself must not send.
