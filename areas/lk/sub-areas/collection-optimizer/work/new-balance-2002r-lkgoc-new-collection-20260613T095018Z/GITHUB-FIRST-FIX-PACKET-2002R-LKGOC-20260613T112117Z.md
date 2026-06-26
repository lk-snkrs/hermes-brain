# GitHub-first fix packet — New Balance 2002R LKGOC

Data UTC: 20260613T112117Z
Status: LOCAL BRANCH + COMMIT READY / NO SHOPIFY WRITE

## Context
Lucas reportou: layout público da 2002R está errado.
Nova regra ativa: nunca fazer write direto na Shopify Admin API.

## Branch local criada
Repo: `/opt/data/hermes_bruno_ingest/lk-new-theme`
Worktree: `/opt/data/worktrees/lk-new-theme-lkgoc-2002r-fix-20260613`
Branch: `lkgoc/new-balance-2002r-fix-20260613`
Base: `origin/dev`
Commit: `338f5a6 Fix LKGOC New Balance 2002R layout`

## Arquivos alterados
- `sections/lk-collection.liquid`
- `snippets/lk-goc-new-balance-2002r-hero-204l-clone.liquid`
- `snippets/lk-goc-new-balance-2002r-guide-panel.liquid`
- `templates/collection.new-balance-2002r.json`

## Correção LKGOC
- Remove dependência de render genérico `lk-goc-collection` para 2002R.
- Cria hero dedicado no padrão dos clones 204L já usados para NB530/NB9060.
- Mantém contrato visual 204L:
  - `lk-goc-coll-preview--204l`
  - `lk-204l-coll-preview`
  - collage/read-more/modal/spacing do golden.
- Adiciona classe própria:
  - `lk-goc-coll-preview--2002r`
- Cria guia dedicado pós-grid:
  - `lk-goc-new-balance-2002r-guide-panel`
  - `id="lk-guia-new-balance-2002r"`
- Cria template dedicado:
  - `collection.new-balance-2002r.json`

## Verificação local
- `git diff --cached --check`: passou antes do commit.
- Commit criado com sucesso.
- Checks locais confirmaram:
  - section renderiza hero dedicado: OK
  - section renderiza guide dedicado: OK
  - render genérico 2002R removido: OK
  - hero mantém aliases 204L: OK
  - hero tem classe 2002R: OK
  - guide tem ID 2002R: OK
  - template existe: OK

## Theme check
`shopify theme check --path .` foi executado e retornou falhas preexistentes do repo/tema, não específicas da alteração 2002R, incluindo `layout/theme.liquid` renderizando `lk-popup-ab` ausente e warnings antigos em backups/snippets. A validação específica foi feita por diff/checks locais.

## Próximo passo
Para continuar sem violar a regra:
1. Aprovar push da branch para GitHub e abertura de PR; ou
2. Revisar localmente o commit; ou
3. Pedir ajustes de copy/layout antes do push.

## Bloqueio
Nenhum novo write Shopify foi feito.
Deploy/merge para Shopify Production continua bloqueado até PR/QA/aprovação.
