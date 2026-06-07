# Audit — LKGOC Zero-Base / Superpowers / PRD Gate

Data UTC: 20260606T180716Z
Status: **FAIL_PROCESS_GAPS_FOUND / PRD_CREATED / REBUILD_NOT_STARTED**

## Pedido de Lucas

“Faça um audit e refaça do zero o LKGOC usando a skill Superpowers, faça um PRD e me faça perguntas; nunca pode acontecer esse monte de erro.”

## Interpretação operacional

Este trabalho é um **reset sistêmico do LKGOC**, não uma correção visual pontual da Puma.

Objetivo: criar uma base canônica que impeça novo ciclo de erros por:

- QA técnico substituindo QA visual;
- 204L tratado como inspiração em vez de contrato;
- falta de perguntas antes do build;
- falta de PRD antes da execução;
- falta de veto real da skill Superpowers/workers;
- aprovação indevida de coleção visualmente divergente.

## Artefatos auditados

- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/AGENTS.md
- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/playbooks/full-lkgoc-rebuild.md
- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/rules/REGRA-LKGOC-204L-GOLD-SOURCE-VISUAL-CONTRACT.md
- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/rules/REGRA-LKGOC-MIDIA-DEV-PRODUCTION-POLICY.md
- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/rules/REGRA-LKGOC-HERO-PESSOAS-E-GUIA-PADRAO-BLOQUEANTE.md
- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/rules/REGRA-LKGOC-CONTRACT-LOCK-ANTES-DE-WRITE.md
- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/templates/lkgoc-contract-lock-template.md
- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/skills/lk-superpowers-collection-optimizer/SKILL.md
- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/skills/lk-superpowers-collection-optimizer/checklists/qa-checklist.md

## Cobertura sistêmica detectada

```json
{
  "dev_unpublished_only": true,
  "production_blocked": true,
  "204l_gold_source": true,
  "side_by_side_required": true,
  "superpowers_skill": true,
  "worker_veto": true,
  "media_sources": true,
  "component_single": true,
  "no_new_layout": true,
  "prd_needed": false,
  "questions_gate": true
}
```

## Lacunas/risco atual

- Não existe PRD canônico obrigatório antes de rebuild LKGOC.

## Decisão do audit

- O LKGOC atual já tem correções importantes, mas ainda precisa de **PRD obrigatório + question gate + Superpowers veto mais explícito**.
- Nenhum novo rebuild de coleção deve começar antes de Lucas responder o briefing mínimo.
- Production/main permanece bloqueado.

## Próximo artefato criado neste pacote

- PRD canônico v2: `PRD-LKGOC-ZERO-BASE-SUPERPOWERS-V2.md`
- Perguntas obrigatórias: `QUESTIONS-FOR-LUCAS.md`
- Patch plan: `PATCH-PLAN.md`
