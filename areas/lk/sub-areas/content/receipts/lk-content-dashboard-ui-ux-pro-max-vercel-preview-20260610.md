# LK Content Dashboard — UI UX Pro Max Vercel preview receipt

Date: 2026-06-10
Status: Vercel preview deployed; autonomous readback protected
Values printed: false

## Scope approved

Lucas approved: "Pode subir a prova".

## Project

- Project: `/opt/data/projects/lk-content-dashboard`
- Deployment type: Vercel Preview
- Method: Doppler/Vercel token used in-process only; no token values printed or persisted.

## Preview

- Preview URL: https://lk-content-dashboard-ezi7ze5dr-lk-snkrs-projects.vercel.app
- Inspect URL: https://vercel.com/lk-snkrs-projects/lk-content-dashboard/4MtRaGzQcN4g91tKLi778wocD5Pd

## Build / deploy evidence

Raw Vercel log was read locally and showed:

- Vercel CLI: 54.11.1 locally, 54.10.2 during Vercel build
- Next.js: 16.2.9
- Build: compiled successfully
- TypeScript: finished successfully
- Static pages: 12/12 generated
- Build Completed in `/vercel/output` in 9s
- Deployment completed
- Ready in 23s

Routes generated:

- `/`
- `/_not-found`
- `/brand`
- `/calendario`
- `/campanhas`
- `/flows`
- `/guardrails`
- `/klaviyo`
- `/learnings`
- `/queue`
- `/receipts`

## Readback

- Public/autonomous fetch returned 401 due to Vercel Deployment Protection / Vercel Auth.
- Deploy script output: `READBACK=failed`, `http=failed;markers=missing`, preview URL present.
- Classified as preview protection/readback blocked, not build/deploy failure, because Vercel log shows deployment `Ready`.

## Local QA reference

- Local QA before deploy: `/opt/data/profiles/lk-content/cron/output/de82f76bd8d1/2026-06-10_11-51-15.md`
- Deploy cron output: `/opt/data/profiles/lk-content/cron/output/0fe6ee79b15b/2026-06-10_12-10-52.md`

## Visual approval

Visual approval remains pending Lucas review in the protected preview.
