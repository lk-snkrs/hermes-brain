# PRD — LKGOC DEV-first Agent Governance

Data UTC: 2026-06-03T15:16:11.720465+00:00
Owner: LK Growth / Collection Optimizer
Status: Implementado P0 local

## Problema

O agente LKGOC pode confundir tema com nome “dev” com ambiente seguro, enviar links antes de QA visual completo, ou tratar produção como patch independente. Isso quebra o fluxo desejado por Lucas: **publicar tudo no DEV, aprovar, depois fazer merge para Production**.

## Objetivo

Transformar DEV-first em regra hard do agente LK Otimização de Coleção / LKGOC:

- Nenhum write visual/theme LKGOC fora de tema `role: unpublished` sem exceção explícita.
- Nenhum link de aprovação sem QA visual e bloqueadores editoriais.
- Nenhuma produção por patch solto; apenas merge/promoção DEV → Production após approval.

## Requisitos funcionais

### RF1 — Theme role gate

Antes de qualquer write Shopify theme:

- chamar API de tema;
- registrar `theme_id`, `name`, `role`;
- abortar se `role: main` ou diferente de `unpublished`.

### RF2 — DEV preview obrigatório

Toda alteração LKGOC deve existir primeiro em DEV/unpublished, com link preview para Lucas.

### RF3 — QA bloqueante antes de link

O agente não pode enviar link de approval se detectar:

- `Liquid error`;
- placeholder editorial ou texto “pendente/substituir”;
- comentário técnico visível;
- FAQ/schema duplicado ou desatualizado;
- guia fora do padrão LKGOC;
- ausência de visual QA desktop/mobile;
- preview sem cookie/`preview_theme_id` validado.

### RF4 — Production como merge

Após aprovação explícita, production recebe o diff aprovado do DEV. Não fazer patch manual independente em production.

### RF5 — Exception handling

Hotfix direto em production só se Lucas disser explicitamente “hotfix direto em production” com escopo.

## Requisitos não funcionais

- Premium/minimalista em copy pública.
- Sem pronta entrega/encomenda/estoque como taxonomia pública.
- Receipts com rollback, before/after, sha/readback e QA.
- Telegram limpo: report executivo, sem logs técnicos excessivos.

## Critérios de aceite

- Canônico LKGOC contém gate DEV-first.
- Skill ativo `lk-superpowers-collection-optimizer` contém gate e checklist.
- SOUL do profile reforça `role: unpublished`.
- Auditoria registrada no Brain.
- Em nova execução LKGOC, agente deve declarar theme role antes de write e bloquear link se QA visual falhar.

## Implementação P0 concluída

- Canônico atualizado: `LKGOC-PADRAO-CANONICO.md`.
- Skill atualizada: `/opt/data/profiles/lk-collection-optimizer/skills/lk-superpowers-collection-optimizer/SKILL.md`.
- SOUL atualizado: `/opt/data/profiles/lk-collection-optimizer/SOUL.md`.
- Auditoria: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lkgoc-dev-first-governance-audit-20260603T151611Z.md`.
- Receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/governance/lkgoc-dev-first-governance-implementation-20260603T151611Z`.

## Próximos P1 recomendados

- Criar script `lkgoc_preflight_theme_gate.py` reutilizável para bloquear writes automaticamente.
- Criar checklist `LKGOC-PREVIEW-QA-CHECKLIST.md` com desktop/mobile + anti-placeholder.
- Adicionar teste local que falha se skill/canônico perderem termos: `role: unpublished`, `DEV → Production`, `placeholder`, `Liquid error`.
