# Receipt — Curadoria LK duplicate hotfix — 2026-06-02

## Veredito
Correção aplicada e validada. PDPs com grupos Curadoria LK sobrepostos agora renderizam apenas o primeiro bloco/correto.

## Escopo
- Asset alterado: `snippets/lk-variante-top30-visited.liquid`
- Production theme: `lk-new-theme/production` / role `main` / ID `155065417950`
- Dev theme: `lk-new-theme/dev` / role `unpublished` / ID `155065450718`

## Problema confirmado
Exemplo reportado por Lucas:
- URL: `https://lksneakers.com.br/products/tenis-new-balance-530-arid-stone-cinza`
- Antes: 2 blocos `Curadoria LK`
  - correto/cima: `top30-nb-530` com `Turtledove`, `White Indigo`, `Silver Cream`, `Silver White`, `Steel Grey`
  - duplicado/baixo: `top30-new-balance-530-regular`

Audit refinado encontrou duplicidades de classe em pares como NB 530, NB 9060, NB 204L, Mexico 66, Mexico 66 Sabot, SL72, Handball Spezial, Taekwondo Mei, Samba Jane, AJ1 Low e Alo.

## Correção aplicada
- Inserido guard para handles que já renderizam inline em `sections/lk-pdp.liquid`.
- Todos os blocos estáticos posteriores agora só renderizam se `lk_top30_rendered == false`.
- Resultado: preserva o primeiro bloco visível/de cima e impede o segundo bloco por baixo.

## Readback
- Production before SHA: `e6f3323a13c7`
- Production after SHA: `7320d9005f03`
- Production readback matches: `True`
- Dev before SHA: `e6f3323a13c7`
- Dev after SHA: `7320d9005f03`
- Dev readback matches: `True`
- Static blocks gated: `32`
- Legacy inline handles protected: `28`

## QA
- QA amostra inicial: 9 famílias, todas com 1 bloco, 5 itens e zero Liquid error.
- QA readback/gates:
  - gated_condition_count: `32`
  - legacy_guard_present: `True`
  - NB static gated: `True`
  - Samba static gated: `True`
  - Alo Airlift static gated: `True`
- QA amplo: 68 handles sobrepostos varridos; varredura rápida teve cache/429 parcial; retry lento dos 13 restantes passou em 13/13.
- NB 530 Arid Stone pós-fix: 1 bloco `top30-nb-530`, labels corretos preservados.

## GitHub
- Repo: `lk-snkrs/lk-new-theme`
- Branch: `production`
- Status: `Repo production already matches duplicate hotfix readback`
- Repo file SHA: `7320d9005f03`
- Target/readback SHA: `7320d9005f03`
- PR: `None`

## Rollback
Reverter `snippets/lk-variante-top30-visited.liquid` para o backup:
- Production backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/duplicate-audit-20260602T194656Z/fix-apply/production-before.liquid`
- Dev backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/duplicate-audit-20260602T194656Z/fix-apply/dev-before.liquid`

## Não alterado
Não foram alterados produtos, preços, estoque, checkout, apps, campanhas, GMC/feed, Klaviyo, Meta, Tiny ou menus.

## Artefatos
- Audit dir: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/duplicate-audit-20260602T194656Z`
- Apply dir: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/duplicate-audit-20260602T194656Z/fix-apply`
- Apply result: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/duplicate-audit-20260602T194656Z/fix-apply/fix-apply-result.json`
- Post-fix slow retry: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/duplicate-audit-20260602T194656Z/fix-apply/post-fix-slow-retry-failed-handles.json`
- GitHub sync result: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/duplicate-audit-20260602T194656Z/fix-apply/github-sync-hotfix-result.json`
