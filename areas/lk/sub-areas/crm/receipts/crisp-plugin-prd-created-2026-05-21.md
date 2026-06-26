# Receipt — PRD Crisp Marketplace Plugin Hermes Brain — 2026-05-21

## Ação

Criado PRD técnico v1 para implementar o grande cérebro de resposta do Crisp via **Crisp Marketplace Plugin + Hermes Brain**, sem Hugo no MVP.

## Arquivo criado

- `areas/lk/sub-areas/crm/prds/crisp-marketplace-plugin-hermes-brain-prd-2026-05-21.md`

## Decisões refletidas

- Plugin Crisp é a infraestrutura oficial.
- Hermes Brain é o núcleo de decisão/contexto/guardrails.
- Hugo Workflow API e Hugo MCP ficam fora do MVP.
- Resposta automática começa por modo canary/manual-first.
- A3/A4 escalam para Larissa/humano.
- Segredos permanecem no Doppler `lc-keys/prd` e não foram expostos.

## Verificação

- Arquivo lido após escrita.
- Busca por placeholders `TBD`, `TODO`, `???` sem pendências reais.
- Nenhuma alteração em Docker/VPS/gateway/Crisp runtime foi feita.

## Próximo passo

Após aprovação do PRD, criar plano de implementação bite-sized para Canary 0/1: fixtures, validação de assinatura, endpoint health/hooks, idempotência e modo sem resposta automática.
