# Hermes Brain OS

**Nome curto:** Brain OS
**Subtítulo:** Canonical Project Intelligence Layer
**Status:** v1 em implantação local/documental
**Criado em:** 2026-06-10

## Tese

O Brain do Hermes não deve ser apenas um arquivo gigante, nem um depósito de receipts. Ele deve operar como uma camada durável de inteligência por projeto: cada frente relevante tem estado atual, decisões, guardrails, histórico, próximos passos, índice de artefatos e manifest.

## Diferença entre Memory OS e Brain OS

- **Memory OS:** cuida de contexto, recall, hot/daily, higiene, auto-heal, continuidade e suficiência antes de responder.
- **Brain OS:** cuida da organização durável da inteligência: projetos canônicos, fontes da verdade, manifests, indexação, versionamento e separação entre histórico e estado atual.

## Regra central

Todo tema com múltiplos receipts, PRDs, reports, decisões, riscos externos ou handoffs recorrentes vira um **Projeto Brain OS** com pasta canônica.

## Arquitetura recomendada

Modelo híbrido:

1. O hub canônico fica dentro da **área dona** do projeto.
2. O Brain OS mantém um índice central e scanner para enxergar todos os hubs.
3. O histórico original permanece no lugar; hubs apontam para evidências, não apagam nem movem originais.

## Primeiro exemplo validado

`areas/lk/sub-areas/atendimento/projetos/chatwoot/`

Esse hub estabeleceu o padrão mínimo: README, estado atual, decisões/guardrails, índice de artefatos, timeline, próximos passos e manifest.

## Guardrail de execução

Brain OS v1 é local/documental:

- sem Docker/VPS/gateway/runtime;
- sem cron novo;
- sem writes em Shopify, Tiny, GMC, WhatsApp, Chatwoot, e-mail ou APIs externas;
- sem copiar secrets;
- sem apagar histórico;
- Git commit/push só com aprovação explícita.

## Arquivos deste projeto

- `PRD.md` — produto e critérios de sucesso.
- `CURRENT_STATE.md` — estado atual do Brain OS.
- `DECISIONS_AND_GUARDRAILS.md` — decisões de arquitetura e bloqueios.
- `PROJECT_HUB_STANDARD.md` — padrão obrigatório para hubs.
- `PROJECT_CANDIDATES.md` — ondas de consolidação.
- `ROLL_OUT_PLAN.md` — plano de rollout.
- `SCANNER_SPEC.md` — especificação do scanner local.
- `MANIFEST_STANDARD.md` — padrão de manifest.
