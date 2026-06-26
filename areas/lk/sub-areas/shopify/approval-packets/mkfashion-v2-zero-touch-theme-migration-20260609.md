# Approval packet — mKFashion Provador Virtual v2 zero-touch

Data: 2026-06-09
Perfil: LK Shopify
Worktree: `/opt/data/worktrees/lk-new-theme-mkfashion-v2-20260609`
Branch local: `fix/mkfashion-v2-zero-touch-20260609`
Base local: `origin/production` disponível localmente

## Escopo pedido

Migrar a integração mKFashion no tema Shopify LK para a nova versão zero-touch:

1. Remover integração antiga/manual.
2. Adicionar script novo global em `layout/theme.liquid` imediatamente antes de `</head>`.
3. Não usar condicional de template.
4. Não fazer commit/push sem revisão.
5. Não subir para Shopify sem aprovação explícita.

## Vestígios antigos encontrados antes da remoção

### Tema ativo/root

- `sections/lk-pdp.liquid`
  - Comentário `mKFashion Virtual Try-On (below ATC)`.
  - Render manual `{% render 'mkfashion-tryon', product: product %}`.

- `snippets/mkfashion-tryon.liquid`
  - Botão manual `Provador Virtual`.
  - Container/botão manual `mkfashion-container` / `mkfashion-btn`.
  - SDK antiga `https://unpkg.com/mkfashion-sdk/src/mkfashion.js`.
  - Chamadas antigas `mkfashion.isAvailable`, `mkfashion.addToCart`, `mkfashion.open`.
  - Lógica manual de `cart/add.js`.

### Observação de arquivos arquivados/réplica no repositório

Após a limpeza do tema ativo/root, ainda existem referências antigas em arquivos rastreados dentro de `projetos/lk-new-theme/...`, incluindo backups/dev-theme/réplica:

- `projetos/lk-new-theme/backups/v1.3/lk-pdp.liquid`
- `projetos/lk-new-theme/dev-theme/sections/lk-pdp.liquid`
- `projetos/lk-new-theme/dev-theme/snippets/mkfashion-tryon.liquid`
- `projetos/lk-new-theme/sections/lk-pdp.liquid`
- `projetos/lk-new-theme/snippets/mkfashion-tryon.liquid`

Esses arquivos não foram alterados nesta execução para evitar mexer em cópias/arquivos não pertencentes ao tema ativo/root sem decisão explícita.

## Alterações locais feitas

Status local:

- `M layout/theme.liquid`
- `M sections/lk-pdp.liquid`
- `D snippets/mkfashion-tryon.liquid`

Diff stat:

- `layout/theme.liquid`: 4 inserções
- `sections/lk-pdp.liquid`: 3 deleções
- `snippets/mkfashion-tryon.liquid`: 105 deleções
- Total: 3 arquivos, 4 inserções, 108 deleções

### Novo script inserido

Inserido em `layout/theme.liquid`, linhas 489–492, imediatamente antes de `</head>` linha 493:

```html
<script src="https://cdn.jsdelivr.net/npm/mk-sdk-git@latest/dist/mk-sdk.js"
        data-mk-project="698c806c1d3129430f15ddde"
        data-mk-product="mk-fashion"
        async></script>
</head>
```

### Integração antiga removida

Removido de `sections/lk-pdp.liquid`:

```liquid
{%- comment -%} mKFashion Virtual Try-On (below ATC) {%- endcomment -%}
{% render 'mkfashion-tryon', product: product %}
```

Removido arquivo inteiro:

```text
snippets/mkfashion-tryon.liquid
```

## Verificação executada

Comandos/checagens locais executados no worktree:

- `git diff --check`: sem saída/sem erro.
- Contagem do novo script no tema ativo: `1` ocorrência em `layout/theme.liquid`.
- Busca de resíduos antigos nos diretórios ativos `layout`, `sections`, `snippets`, `templates`, `assets`, `config`, `locales`: `0` ocorrências.
- Busca por referência ao snippet `mkfashion-tryon` nos diretórios ativos: nenhuma.
- Existência de `snippets/mkfashion-tryon.liquid`: `False`.
- Posicionamento:
  - script novo na linha 489.
  - `</head>` na linha 493.
  - bloco novo imediatamente antes de `</head>`.
- Nenhuma condicional de template detectada ao redor do script novo.

Resultado da verificação local focada:

```text
PASS active theme verification
```

## Limitação de verificação

`shopify theme check` foi tentado, mas não concluiu dentro do timeout mesmo em cópia temporária reduzida do tema. Portanto, a validação final disponível é estática/focada em diff, posicionamento, resíduos e `git diff --check`.

## O que NÃO aconteceu

- Não houve commit.
- Não houve push.
- Não houve upload para Shopify DEV.
- Não houve upload para Shopify Production.
- Não houve write externo.

## Risco

Baixo/médio:

- Baixo porque a integração antiga manual foi removida apenas dos pontos claramente mKFashion no tema ativo/root.
- Médio porque o novo script é global e carrega em todas as páginas, conforme exigido pela nova SDK zero-touch.

## Rollback local

Antes de commit/push/upload, rollback é simples:

```bash
git -C /opt/data/worktrees/lk-new-theme-mkfashion-v2-20260609 restore layout/theme.liquid sections/lk-pdp.liquid snippets/mkfashion-tryon.liquid
```

Ou remover a worktree/branch local se for descartar a migração.

## Próxima decisão

Lucas revisar o diff local. Se aprovado, próximo passo recomendado:

1. opcional: limpar também as cópias arquivadas/réplica em `projetos/lk-new-theme/...`, se elas fizerem parte do pacote/repo final esperado;
2. criar commit/PR ou preparar upload DEV/unpublished, conforme fluxo escolhido;
3. somente depois de aprovação explícita, fazer qualquer write em Shopify.
