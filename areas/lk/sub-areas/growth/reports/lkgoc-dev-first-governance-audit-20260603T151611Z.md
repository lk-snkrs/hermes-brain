# Auditoria — Governança DEV-first LKGOC

Data UTC: 2026-06-03T15:16:11.720294+00:00

## Diagnóstico

Falha raiz confirmada: a regra “tudo deve ser publicado no tema DEV e depois mergeado para production” existia como documento operacional (`rules/shopify-theme-dev-to-production-promotion-rule-20260531.md`), mas não estava forte o suficiente no canônico LKGOC nem no skill ativo do agente `lk-superpowers-collection-optimizer`.

## Incidentes observados nesta sessão

- Um tema com nome de dev foi identificado depois como `role: main`; isso prova que nome do tema não é fonte de verdade.
- Link de preview foi enviado com QA técnico insuficiente para aprovação visual, deixando passar placeholder editorial e drift do guia.
- O fluxo correto deveria ter bloqueado entrega ao Lucas antes de visual QA desktop/mobile e checks anti-placeholder.

## Causa raiz

- Regra de promoção DEV → Production estava isolada, não como gate hard do LKGOC.
- QA anterior aceitava HTTP 200/sem Liquid error como suficiente, mas LKGOC exige visual QA e bloqueadores editoriais.
- Falta de checklist obrigatório antes de enviar link de approval.

## Correções implementadas agora

- `LKGOC-PADRAO-CANONICO.md`: adicionada seção `0.4 Gate DEV-first / merge para production`.
- `skills/lk-superpowers-collection-optimizer/SKILL.md`: adicionados gates de DEV real, bloqueio antes de link e fluxo mínimo com `role: unpublished`.
- `SOUL.md` do profile `lk-collection-optimizer`: reforçado guardrail de `role: unpublished` + DEV → QA → approval → merge production.

## Nova regra operacional

1. Verificar `theme_id`, `name`, `role` por API antes de write.
2. Se `role != unpublished`, abortar.
3. Aplicar no DEV/unpublished.
4. Rodar readback + storefront preview + QA desktop/mobile.
5. Bloquear link se houver placeholder, comentário técnico, Liquid error, drift de guia, FAQ/schema duplicado ou layout fora do padrão.
6. Enviar link DEV para Lucas.
7. Só após aprovação explícita: merge/promoção do diff aprovado do DEV para Production.
8. Production direto somente com autorização explícita de hotfix direto em production.

## Status

Implementado localmente no Brain e no profile ativo `lk-collection-optimizer`.

## Receipt

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/governance/lkgoc-dev-first-governance-implementation-20260603T151611Z`
