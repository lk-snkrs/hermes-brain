# Hermes Brain OS

**Nome curto:** Brain OS
**Subtítulo:** Canonical Project Intelligence Layer
**Status:** v1 publicado em hubs canônicos; maturidade/qualidade em evolução
**Atualizado em:** 2026-06-11T13:55:54.899501+00:00

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

## Estado pós-merge PR #144

- Os hubs canônicos das ondas Brain OS foram publicados em `main`.
- O scanner publicado possui `scanner_version=brain-os-v1`.
- O pacote mínimo de hub é validável por `manifest.json` + 6 arquivos documentais.
- O próximo foco não é criar hubs por volume, e sim maturidade: docs centrais, semântica de manifests e status executivo.

## Guardrail de execução

Brain OS v1 é local/documental:

- sem Docker/VPS/gateway/runtime;
- sem cron novo;
- sem writes em Shopify, Tiny, GMC, WhatsApp, Chatwoot, e-mail ou APIs externas;
- sem copiar secrets;
- sem apagar histórico;
- Git commit/push/PR apenas dentro de escopo documental aprovado.

## Arquivos deste projeto

- `PRD.md` — produto e critérios de sucesso.
- `CURRENT_STATE.md` — estado atual do Brain OS.
- `DECISIONS_AND_GUARDRAILS.md` — decisões de arquitetura e bloqueios.
- `PROJECT_HUB_STANDARD.md` — padrão obrigatório para hubs.
- `PROJECT_CANDIDATES.md` — ondas de consolidação.
- `ROLL_OUT_PLAN.md` — plano de rollout.
- `SCANNER_SPEC.md` — especificação do scanner local.
- `MANIFEST_STANDARD.md` — padrão de manifest.
- `MANIFEST_SEMANTICS.md` — diferença entre hub canônico, receipt, backup e artefato.
- `EXECUTIVE_STATUS.md` — superfície executiva de status Brain OS.
