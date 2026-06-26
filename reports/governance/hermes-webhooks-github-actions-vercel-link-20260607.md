# Hermes Webhooks — Vercel/GitHub connection attempt and GitHub Actions deploy — 2026-06-07

## User ask

Lucas asked whether Hermes could connect the Vercel project to the GitHub repository.

Target repo:

```text
https://github.com/lucascimino/hermes-webhook.git
```

Target Vercel project:

```text
hermes-webhooks
```

## Native Vercel Git connection attempt

Checked current Vercel project metadata before the attempt:

- `link`: `null`
- `gitRepository`: `null`

Tried Vercel API patch shapes for `gitRepository`/`link` and Vercel CLI:

```text
npx vercel git connect https://github.com/lucascimino/hermes-webhook.git --scope lk-snkrs-projects
```

Result:

- Vercel CLI failed with repository-access/integration style error.
- Vercel project metadata remained:
  - `link`: `null`
  - `gitRepository`: `null`

Interpretation: native dashboard-style Git linking is blocked from this token/API path and likely needs a one-time GitHub/Vercel dashboard integration/login connection or repository installation permission.

## Implemented fallback

Configured GitHub Actions deployment from the canonical repo to the existing Vercel project.

Workflow added:

```text
.github/workflows/vercel-production.yml
```

Trigger:

- push to `main`
- manual `workflow_dispatch`

Secrets set in GitHub Actions without printing values:

- `VERCEL_TOKEN`
- `VERCEL_ORG_ID`
- `VERCEL_PROJECT_ID`

The workflow runs:

```text
vercel pull --environment=production
vercel build --prod
vercel deploy --prebuilt --prod --yes
```

## Verification

GitHub Actions run:

- workflow: `Deploy Vercel Production`
- status: `completed`
- conclusion: `success`
- run URL: `https://github.com/lucascimino/hermes-webhook/actions/runs/27095169243`

Vercel deployment after the GitHub Actions run:

- state: `READY`
- target: `production`
- source: `cli`
- `meta.githubCommitSha`: `1430176f62ded93ddf1e255f5160be9f14d08096`

Public health checks:

- `https://hermes-webhooks.lucascimino.com/health` → `200 OK`, `Server: Vercel`, `platform=webhook`
- `https://hermes-webhooks.vercel.app/health` → `200 OK`, `Server: Vercel`, `platform=webhook`

## Operational conclusion

Native Vercel dashboard Git link is still not active:

- `link`: `null`
- `gitRepository`: `null`

But GitHub-to-Vercel deployment is operational through GitHub Actions. Future pushes to `main` deploy production automatically through the workflow until/unless the one-time native Vercel GitHub integration is connected in the dashboard.

No secrets were printed or committed.
