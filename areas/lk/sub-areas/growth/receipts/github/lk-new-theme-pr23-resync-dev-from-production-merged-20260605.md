# Receipt — PR #23 resync dev from production merged

Data: 2026-06-05

## Escopo aprovado

Lucas respondeu `Vamos seguir?` em resposta ao pacote do PR #23 de resync `production → dev`.

Interpretação operacional: seguir com o PR de resync já preparado, sem force-push e sem write Shopify.

## PR

- URL: https://github.com/lk-snkrs/lk-new-theme/pull/23
- Repo: `lk-snkrs/lk-new-theme`
- Base: `dev`
- Head original: `chore/resync-dev-from-production-20260605`

## O que aconteceu

1. Revalidação inicial detectou que `production` havia avançado novamente.
   - PR head anterior: `79c9b473bd44ac2b1e2ccbaa87b50cb1a0bda22f`
   - Production atual detectada: `6aada2bd5e1b590f437296b97bb05036784eaef8`
   - Resultado: não mergeado naquele momento porque o head do PR já não era igual à production atual.

2. Atualizei o PR branch sem force-push.
   - Commit normal criado/pushado: `41504adb257bcfa7a9bfc95ccb09b2b41d2513f9`
   - Resultado: PR branch voltou a ficar com árvore igual à `origin/production`.

3. GitHub ainda marcou o PR como `dirty` porque `dev` havia divergido como base de merge.
   - Apliquei um merge commit normal com estratégia `ours` para registrar a `origin/dev` atual como parent, preservando a árvore final de production.
   - Novo head do PR: `e3af5f68450371c24557892eb467e29838e86b5d`
   - Verificações:
     - `dev` virou ancestor do PR head: true
     - PR head continuou igual à production: true

4. Revalidação final antes do merge:
   - state: open
   - draft: true
   - mergeable: true
   - mergeable_state: clean
   - base: dev
   - head: chore/resync-dev-from-production-20260605
   - head SHA: `e3af5f68450371c24557892eb467e29838e86b5d`
   - production SHA: `6aada2bd5e1b590f437296b97bb05036784eaef8`
   - head equals production: true

5. Converti o PR de draft para ready-for-review e mergeei.
   - Merge SHA: `d9ca082a3f33fd0c7b9173d13302fee7fca318de`
   - GitHub message: `Pull Request successfully merged`
   - Branch remota deletada após merge: true

## Resultado final

- PR #23: merged/closed
- Branch `dev` atual: `d9ca082a3f33fd0c7b9173d13302fee7fca318de`
- Branch `production` comparada: `6aada2bd5e1b590f437296b97bb05036784eaef8`
- Validação pós-merge: `dev_equals_production = true`

## Não feito

- Nenhum Shopify theme upload.
- Nenhum write em Production Shopify.
- Nenhum produto/preço/estoque/feed/app alterado.
- Não houve force-push.

## Risco/caveat

O merge mudou a branch GitHub `dev` para baseline idêntico à `production`, como planejado. Isso remove experimentos/diffs que existiam somente na branch `dev`.

Isso ainda não garante que o tema Shopify DEV (`155065450718`) foi atualizado/deployado automaticamente. É necessário validar o tema DEV via Shopify Admin API ou executar deploy controlado se não houver automação.

## Próximo passo recomendado

1. Verificar se GitHub `dev` deployou para o tema Shopify DEV.
2. Comparar assets do tema Shopify DEV contra Production.
3. Só depois retomar correção/expansão da Curadoria LK PDP com baseline limpo.

## Rollback GitHub

Rollback do GitHub `dev` seria criar um novo PR revertendo o merge commit `d9ca082a3f33fd0c7b9173d13302fee7fca318de` ou restaurando a árvore anterior de `dev` (`43a62be4afa1ea34c934593b06641045187ab22a`) em uma branch revisada. Não executar rollback sem nova aprovação.
