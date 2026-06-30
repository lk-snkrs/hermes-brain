# Skill Surface Diet — lk-stock apply dry-run

Data: 20260629T151923Z UTC  
Escopo aprovado: aplicar dieta de skills no profile `lk-stock`, com backup, patch local, restart somente do gateway `lk-stock`, readback e receipt.  
Não autorizado/tocado: Docker, VPS, Traefik, Main/default, crons, webhooks externos, Tiny/Shopify/Supabase writes, secrets.

## Princípio

LK Stock = estoque/pronta entrega/Stock OS/Tiny/Inventory Hub first; Growth, Trends, Shopify publishing and broad content stay as handoffs/lenses.

## Resultado proposto

| Métrica | Valor |
|---|---:|
| Skills ativas lidas | 226 |
| Habilitadas no Telegram | 51 |
| Desabilitadas no Telegram | 175 |
| Protegidas desabilitadas | 0 |

## Core protegido

- `lk-inventory-hub`
- `lk-operational-intelligence`
- `lk-shopify-readonly`
- `lk-stock`
- `multiempresa-routing-lucas`
- `superpowers`
- `verification-before-completion`

## Lentes críticas preservadas

- `brainstorming`
- `codebase-inspection`
- `customer-messaging-operations`
- `design-md`
- `dogfood`
- `doppler-github-pr-safe`
- `doppler-secrets-operations`
- `executing-plans`
- `fastmcp`
- `finishing-a-development-branch`
- `gateway-post-restart-validation`
- `github-auth`
- `github-pr-workflow`
- `google-workspace`
- `hermes-agent`
- `hermes-brain-governance`
- `hermes-central-integration-auth-broker`
- `himalaya`
- `honcho-memory-operations`
- `hostinger-vps-api-ssh-access`
- `impeccable`
- `last30days`
- `lk-shopify-product-upload`
- `lucas-chief-of-staff`
- `lucas-runtime-operations`
- `maps`
- `mcp-connections`
- `mcporter`
- `mesa`
- `native-mcp`
- `notion`
- `ocr-and-documents`
- `receiving-code-review`
- `requesting-code-review`
- `runtime-profile-map`
- `shopify`
- `spike`
- `supabase-security-operations`
- `systematic-debugging`
- `test-driven-development`
- `using-git-worktrees`
- `vercel-deployments`
- `webhook-subscriptions`
- `youtube-content`

## Exemplos fora do core desabilitados no Telegram

- `ads`
- `ads-amazon`
- `ads-apple`
- `ads-attribution`
- `ads-audit`
- `ads-budget`
- `ads-competitor`
- `ads-create`
- `ads-creative`
- `ads-dna`
- `ads-generate`
- `ads-google`
- `ads-landing`
- `ads-linkedin`
- `ads-math`
- `ads-meta`
- `ads-microsoft`
- `ads-photoshoot`
- `ads-plan`
- `ads-server-side-tracking`
- `ads-test`
- `ads-tiktok`
- `ads-youtube`
- `airtable`
- `apple-notes`
- `apple-reminders`
- `architecture-diagram`
- `arxiv`
- `ascii-art`
- `ascii-video`

## Backup

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/backups/skill-surface-diet-apply-20260629T151923Z`

## Guardrails

- Tiny/Shopify/Supabase writes remain blocked without scoped approval
- No cron/webhook/Docker/VPS/Traefik/Main changes
- No skill deletion; Telegram-only disable list
- Backup/readback/receipt required
