# Receipt — mKFashion v2 zero-touch PR merged into production

Data: 2026-06-09
Perfil: LK Shopify
Repo: `lk-snkrs/lk-new-theme`
PR: https://github.com/lk-snkrs/lk-new-theme/pull/44
Base: `production`

## Pedido

Lucas pediu: “Fazer merge para Production”.

## Segurança de escopo

Antes de promover, foi comparado `origin/dev` contra `origin/production`.

Resultado: um merge amplo `dev → production` levaria 38 arquivos e várias mudanças não relacionadas ao mKFashion/LK GOC/guia/curadoria/search.

Por segurança operacional, não foi feito merge amplo de todo `dev`.

Foi criada uma branch a partir de `origin/production` e aplicado somente o commit escopado da migração mKFashion já validada em `dev`:

- branch: `fix/mkfashion-v2-zero-touch-production-20260609`
- cherry-pick do commit dev: `5497125`
- commit resultante na branch production PR: `732381e`

## PR e merge

PR criado:

- PR #44 — `fix: promote mKFashion zero-touch SDK to production`
- URL: https://github.com/lk-snkrs/lk-new-theme/pull/44
- base: `production`

Mergeability:

- `mergeable=true`
- `mergeable_state=clean`

PR mergeado por squash merge.

Resultado remoto:

- PR #44: `closed`, `merged=true`
- merge commit em `origin/production`: `1924235 fix: promote mKFashion zero-touch SDK to production (#44)`
- branch remota temporária removida após merge

## Verificação Git pós-merge

Foi feito fetch de `origin/production` e verificação da árvore remota:

- `origin/production` aponta para `1924235`.
- Novo script zero-touch encontrado exatamente 1 vez em cada layout esperado:
  - `layout/theme.liquid`
  - `projetos/lk-new-theme/layout/theme.liquid`
  - `projetos/lk-new-theme/dev-theme/layout/theme.liquid`
- Resíduos antigos mKFashion/provador: `0`
- Referências a `mkfashion-tryon`: `[]`
- Arquivos `mkfashion-tryon.liquid`: `[]`

Resultado:

```text
PASS origin/production mkfashion verification
```

## Verificação Shopify/Admin readback

Read-only Shopify Admin no tema main:

- theme id: `155065417950`
- name: `lk-new-theme/production`
- role: `main`
- `layout/theme.liquid` no tema Production contém o novo script: count `1`
- referências antigas no asset Production:
  - `mkfashion-tryon`: false
  - `unpkg.com/mkfashion-sdk`: false
  - `Provador/provador`: false

## Verificação pública storefront

Amostras públicas cache-busted em 3 rounds:

- PDP `/products/new-balance-530-white-natural-indigo-1`: novo script presente (`count=1`) nos 3 rounds.
- Search `/search?q=530`: novo script presente (`count=1`) nos 3 rounds.
- Home `/`: novo script ausente (`count=0`) nos 3 rounds.
- Collection `/collections/sneakers`: novo script ausente (`count=0`) nos 3 rounds.

Sem resíduos antigos (`unpkg`, `mkfashion-tryon`) nas amostras públicas.

Classificação: Admin/API readback do tema Production está correto; storefront público ainda apresenta cache/rota/staleness parcial em Home/Collection. Não foi feito rollback porque a fonte do tema main está correta e PDP/Search já refletem a mudança.

## Estado local final

- Worktree: `/opt/data/worktrees/lk-new-theme-mkfashion-v2-20260609`
- Branch local atual: `production`
- `production` local sincronizado com `origin/production` em `1924235`
- Branch temporária local `fix/mkfashion-v2-zero-touch-production-20260609` deletada

## O que NÃO aconteceu

- Não houve write manual via Shopify Asset API.
- Não houve alteração de produtos, estoque, preços, checkout, apps ou campanhas.
- Não foram impressos tokens/segredos.

## Rollback

Rollback Git seguro:

1. Abrir PR revertendo o merge commit `1924235` em `production`; ou
2. Se for emergência, aplicar hotfix revertendo apenas:
   - remoção do script `mk-sdk-git` em `layout/theme.liquid`;
   - restauração do snippet antigo e render antigo somente se Lucas aprovar explicitamente.

Rollback Shopify direto só deve ser usado como hotfix emergencial com aprovação explícita separada, backup/readback/live QA.

## Próximo acompanhamento recomendado

Reexecutar QA público em alguns minutos para Home/Collection e confirmar propagação/cache. Se Home/Collection continuarem sem o script apesar do Admin readback correto, investigar se há cache/rota/template alternativo ou app/proxy interferindo nessas rotas.
