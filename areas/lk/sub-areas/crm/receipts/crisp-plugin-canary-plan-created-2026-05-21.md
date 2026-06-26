# Receipt — Plano Canary 0/1 Crisp Plugin Hermes — 2026-05-21

## Ação

Criado plano de implementação bite-sized para o Canary 0/1 do Crisp Marketplace Plugin → Hermes Brain, sem Hugo e sem resposta ao cliente.

## Arquivo criado

- `areas/lk/sub-areas/crm/plans/crisp-marketplace-plugin-canary-0-1-implementation-plan-2026-05-21.md`

## Base técnica revisada

- PRD: `areas/lk/sub-areas/crm/prds/crisp-marketplace-plugin-hermes-brain-prd-2026-05-21.md`
- Hermes webhook adapter existente: `/opt/data/hermes_bruno_ingest/hermes-agent-v0.13.0/gateway/platforms/webhook.py`
- Docs locais do webhook adapter: `/opt/data/hermes_bruno_ingest/hermes-agent-v0.13.0/website/docs/user-guide/messaging/webhooks.md`
- Referência durável: `/opt/data/skills/autonomous-ai-agents/hermes-agent/references/crisp-marketplace-plugin-hermes-brain.md`

## Escopo do plano

- Fixtures sintéticas Crisp.
- Normalizador de eventos Crisp.
- Verificação de assinatura HMAC isolada.
- Rota `kind: crisp_plugin` em modo `observe_only`.
- Idempotência e anti-loop.
- Config local segura.
- Template de receipt de canary.
- Testes direcionados.

## Guardrails mantidos

- Sem Hugo Workflow API/MCP.
- Sem auto-reply para cliente.
- Sem conexão real com Crisp Marketplace.
- Sem restart/alteração de Docker/VPS/gateway.
- Sem exposição de secrets.

## Verificação

- Plano escrito e verificado por busca de placeholders.
- Nenhuma alteração de runtime/prod executada.
