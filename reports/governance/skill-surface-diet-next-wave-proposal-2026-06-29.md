# Skill Surface Diet — próxima onda proposta

Data: 2026-06-29T16:26:35Z

## Recomendação

Próxima rodada: fazer primeiro LK Ops + LK Growth em modo proposta/dry-run, depois aplicar com aprovação scoped; em paralelo curar heavy skills locais específicas sem deletar conteúdo.

## Por quê

São os dois profiles restantes com maior superfície e estão vivos em runtime; ambos sem platform_disabled.telegram e config antiga. Profiles menores têm ROI menor e maior chance de precisar regras específicas.

## Inventário resumido

| Profile | Prioridade | Config | Skills | Telegram disabled | Motivo |
|---|---|---:|---:|---:|---|
| `lk-ops` | P1 | 23 | 154 | 0 | alto volume, atendimento/operações LK e skill customer-chat pesada; perfil ainda v23 sem dieta |
| `lk-growth` | P1 | 24 | 148 | 0 | alto volume, Growth/SEO/GEO/CRO e skill lk-seo-weekly pesada; perfil ainda sem dieta |
| `lk-content` | P2 | 27 | 10 | 0 | baixo volume mas 1 skill Klaviyo muito pesada; candidato a curadoria local, não dieta ampla |
| `spiti-atendimento` | P2 | 23 | 8 | 0 | baixo volume; migrar config e talvez dieta mínima, mas menor ROI |
| `lk-finance` | P2 | 27 | 9 | 0 | baixo volume; migrar config depois, risco financeiro pede cautela |
| `lc-claude-cli` | P2 | 23 | 4 | 0 | baixo volume; auth/CLI profile, não priorizar dieta ampla |

## Maiores skills por profile

### `lk-ops`

- `pytorch-fsdp` — 160.170 bytes — `mlops/training/pytorch-fsdp/SKILL.md`
- `lk-operational-intelligence` — 101.980 bytes — `productivity/lk-operational-intelligence/SKILL.md`
- `bruno-openclaw-hermes-brain-adaptation` — 101.515 bytes — `productivity/bruno-openclaw-hermes-brain-adaptation/SKILL.md`
- `customer-chat-operations` — 93.626 bytes — `productivity/customer-chat-operations/SKILL.md`
- `hermes-agent` — 69.265 bytes — `autonomous-ai-agents/hermes-agent/SKILL.md`
- `mission-control-development` — 59.392 bytes — `software-development/mission-control-development/SKILL.md`
- `lk-shopify-readonly` — 50.295 bytes — `productivity/lk-shopify-readonly/SKILL.md`
- `lk-seo-weekly-improvement` — 46.372 bytes — `productivity/lk-seo-weekly-improvement/SKILL.md`

### `lk-growth`

- `pytorch-fsdp` — 160.170 bytes — `mlops/training/pytorch-fsdp/SKILL.md`
- `lk-operational-intelligence` — 101.044 bytes — `productivity/lk-operational-intelligence/SKILL.md`
- `lk-seo-weekly-improvement` — 98.865 bytes — `productivity/lk-seo-weekly-improvement/SKILL.md`
- `bruno-openclaw-hermes-brain-adaptation` — 88.938 bytes — `productivity/bruno-openclaw-hermes-brain-adaptation/SKILL.md`
- `hermes-agent` — 50.827 bytes — `autonomous-ai-agents/hermes-agent/SKILL.md`
- `lk-growth-operations` — 47.753 bytes — `productivity/lk-growth-operations/SKILL.md`
- `lk-collection-patterns` — 44.304 bytes — `productivity/lk-collection-patterns/SKILL.md`
- `lk-shopify-readonly` — 38.941 bytes — `productivity/lk-shopify-readonly/SKILL.md`

### `lk-content`

- `lk-content-klaviyo-campaign-operations` — 88.827 bytes — `operations/lk-content-klaviyo-campaign-operations/SKILL.md`
- `doppler-secrets-operations` — 19.228 bytes — `devops/doppler-secrets-operations/SKILL.md`
- `honcho-memory-operations` — 18.726 bytes — `autonomous-ai-agents/honcho-memory-operations/SKILL.md`
- `lk-content-dashboard-product-ui` — 18.179 bytes — `operations/lk-content-dashboard-product-ui/SKILL.md`
- `specialist-profile-activation` — 16.047 bytes — `devops/specialist-profile-activation/SKILL.md`
- `doppler-secrets-operations` — 14.114 bytes — `devops/doppler-secrets-operations.bak-sync-20260607T165901Z/SKILL.md`
- `lk-content-editorial-calendar` — 12.662 bytes — `operations/lk-content-editorial-calendar/SKILL.md`
- `ui-ux-pro-max` — 8.629 bytes — `design/ui-ux-pro-max/SKILL.md`

### `spiti-atendimento`

- `spiti-captacao-obras-intake` — 36.823 bytes — `productivity/spiti-captacao-obras-intake/SKILL.md`
- `spiti-chatwoot-intelligence` — 28.160 bytes — `productivity/spiti-chatwoot-intelligence/SKILL.md`
- `doppler-secrets-operations` — 18.887 bytes — `devops/doppler-secrets-operations/SKILL.md`
- `honcho-memory-operations` — 18.726 bytes — `autonomous-ai-agents/honcho-memory-operations/SKILL.md`
- `spiti-os-readonly-status` — 13.024 bytes — `productivity/spiti-os-readonly-status/SKILL.md`
- `hostinger-vps-api-ssh-access` — 9.663 bytes — `devops/hostinger-vps-api-ssh-access/SKILL.md`
- `hermes-central-integration-auth-broker` — 6.877 bytes — `devops/hermes-central-integration-auth-broker/SKILL.md`
- `verification-before-completion` — 4.334 bytes — `software-development/verification-before-completion/SKILL.md`

### `lk-finance`

- `lk-stock-ops-automation` — 23.701 bytes — `productivity/lk-stock-ops-automation/SKILL.md`
- `doppler-secrets-operations` — 20.612 bytes — `devops/doppler-secrets-operations/SKILL.md`
- `honcho-memory-operations` — 18.726 bytes — `autonomous-ai-agents/honcho-memory-operations/SKILL.md`
- `lk-finance` — 15.406 bytes — `productivity/lk-finance/SKILL.md`
- `lk-ops-whatsapp-automation` — 7.394 bytes — `productivity/lk-ops-whatsapp-automation/SKILL.md`
- `lk-ops-automation` — 6.895 bytes — `productivity/lk-ops-automation/SKILL.md`
- `hermes-central-integration-auth-broker` — 6.877 bytes — `devops/hermes-central-integration-auth-broker/SKILL.md`
- `lk-tiny` — 5.616 bytes — `productivity/lk-tiny/SKILL.md`

### `lc-claude-cli`

- `doppler-secrets-operations` — 18.887 bytes — `devops/doppler-secrets-operations/SKILL.md`
- `honcho-memory-operations` — 18.726 bytes — `autonomous-ai-agents/honcho-memory-operations/SKILL.md`
- `doppler-secrets-operations` — 14.114 bytes — `devops/doppler-secrets-operations.bak-sync-20260607T165901Z/SKILL.md`
- `hermes-central-integration-auth-broker` — 6.877 bytes — `devops/hermes-central-integration-auth-broker/SKILL.md`

## Design recomendado

1. **LK Ops**: core atendimento/operação/chat/WhatsApp/Klaviyo-safe + roteamento LK; tirar ML/creative/gaming/blog/SEO amplo da superfície Telegram.
2. **LK Growth**: core SEO/GEO/CRO/GSC/GA4/DataForSEO/Metricool/read-only Shopify; tirar ML/gaming/creative e operação que pertence a Stock/Shopify/Mordomo.
3. **Curadoria heavy local**: transformar skills profile-local enormes em gateways curtos com `references/full-skill-before-surface-diet-20260629.md`, preservando rollback semântico.
4. **Ativação**: se aprovado, backup → patch scoped → config migrate → restart só do profile → readback → QA → brain health → scan → receipt.

## Guardrails

- Sem Docker/VPS/Traefik/Main.
- Sem writes externos, Shopify/Tiny/Supabase/Klaviyo/WhatsApp/env/secrets.
- Sem deletar skills; usar `skills.platform_disabled.telegram`.
- Runtime só para `lk-ops`/`lk-growth` após aprovação explícita.
