# Implementation Inventory — Mordomo OS × LC-WhatsApp Dashboard

Generated: 2026-06-06
Scope: read-only inventory for adapting the existing GitHub/Railway project into the Mordomo OS cockpit.

## 1. Repository / deployment identity

- GitHub repository: `lk-snkrs/LC-WhatsApp`
- Repository visibility: private
- Default branch: `claude/lc-whatsapp-agent`
- Local working copy: `/opt/data/projects/LC-WhatsApp`
- Package name: `lk-whatsapp-automation`
- App version: `2.0.0`
- Runtime: Node.js CommonJS, raw `http` server, no Express
- Railway project confirmed by API: `lc-whatsapp`
- Railway project id: `397ecb20-9e02-4125-91f6-b035bcd5bcad`
- Production health URL: `https://lc-whatsapp-prd.up.railway.app/health`
- Public health result at inventory time: `status=connected`, `version=2.0.0`, `memoryMB=125`
- Public stats result at inventory time: `totalContacts=389`, `totalMessages=1`, `dbEnabled=true`

## 2. Current codebase size

Excluding `.git`, `node_modules`, build/cache directories:

- Total files: 103
- `.js`: 78 files, 24,069 lines
- `.json`: 5 files, 4,451 lines
- `.md`: 5 files, 558 lines
- `.html`: 1 file, 1,212 lines
- `.sql`: 2 files, 192 lines

## 3. Integration gap

The dashboard currently treats Supabase as the application database. Mordomo OS treats local SQLite as canonical. First production-safe change should add a separate read-only adapter namespace, not replace Supabase globally:

- `GET /api/mordomo/health`
- `GET /api/mordomo/stats`
- `GET /api/mordomo/contacts`
- `GET /api/mordomo/followups?status=&risk=&limit=&offset=`
- `GET /api/mordomo/decision-packets`
- `GET /api/mordomo/sent-actions`
- `GET /api/mordomo/suppressions`

Canonical SQLite: `/opt/data/profiles/mordomo/state/zipper_canonical.sqlite`

Current table counts:

- `contact`: 123
- `artist_interest`: 36
- `lead_enquiry`: 126
- `followup`: 126
- `sent_action`: 150
- `decision_packet`: 18
- `suppression`: 10
- `meta`: 3

## 4. Baseline verification

Commands run locally after `npm ci`:

- `npm ci`: exit code 0; 363 packages installed; 7 vulnerabilities reported by npm audit (5 moderate, 2 high), no fix applied.
- `npm test`: exit code 1; 120 tests total, 106 pass, 14 fail. Failures all in `test/stockx.test.js`: expected exports missing from `src/services/stockx.js` (`extractSkuFromJsonLd`, `extractSkuFromNextData`, `findField`).
- `npm run lint`: exit code 1. Blocking error: `src/services/curadoriaAI.js:192:22` — `researchText` is not defined. Also 6 warnings.

## 5. Recommended safe implementation order

1. P1 baseline cleanup: fix StockX exports/tests and `curadoriaAI.js` undefined variable; re-run test/lint.
2. P2 read-only adapter: `src/services/mordomoStore.js`, `src/routes/mordomoApi.js`, env `MORDOMO_SQLITE_PATH`, endpoints `/api/mordomo/health` and `/api/mordomo/stats` first.
3. P3 cockpit UI panel: add Mordomo OS panel to `src/dashboard.js`, read-only only.
4. P4 dry-run action endpoint: policy evaluation and preview, no external send.
5. P5 live A1 follow-up only after green tests, dry-run validation, idempotency via `sent_action`, and explicit Lucas approval.

## 6. Guardrails before live send

- Allow only A1/pós-PDF lightweight follow-up.
- Block price, availability, reservation, payment, discount, logistics, measurements, complaints.
- Check `sent_action` before any runtime-send.
- Default live send disabled by env until approved.
- Every attempted action must produce an audit event.

Full inventory also saved at repo path:

`/opt/data/projects/LC-WhatsApp/docs/implementation-inventory.md`

## 7. Current implementation status

Local branch: `mordomo-os-readonly-adapter`.

Completed read-only backend:

- `src/services/mordomoStore.js` reads canonical SQLite via Python stdlib `sqlite3`/`execFileSync`, no new Node dependency.
- `src/routes/mordomoApi.js` exposes separate `/api/mordomo/*` namespace.
- `src/routes/api.js` dispatches Mordomo routes before existing dashboard routes.

Implemented endpoints:

- `GET /api/mordomo/health`
- `GET /api/mordomo/stats`
- `GET /api/mordomo/followups`
- `GET /api/mordomo/contacts`
- `GET /api/mordomo/decision-packets`
- `GET /api/mordomo/sent-actions`
- `GET /api/mordomo/suppressions`

Dashboard cockpit:

- Runtime file confirmed as `src/dashboard.js`; legacy `dashboard/index.html` was not used.
- Added `Mordomo OS` tab and read-only cockpit sections for follow-ups, contacts, decisions, sent actions, and suppressions.
- No write/send/approve/execute controls were added; only refresh/section switching.

Verification:

- `npm test`: exit code 0; 134 tests, 25 suites, 134 pass, 0 fail.
- `npm run lint`: exit code 0; 0 errors, 6 pre-existing warnings.
- Dashboard smoke: Mordomo tab/nav/loader present; no Mordomo write action controls.
- Real SQLite smoke: enabled/ok with counts contacts=123, followups=126, sentActions=150, decisionPackets=18, suppressions=10.

Still held intentionally:

- No deploy Railway.
- No GitHub push/PR.
- No external send.
- No live send or approval endpoint/UI.
