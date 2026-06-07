# REGRA LKGOC — Pós-grid somente depois de todos os produtos

Registrado em: 20260606T205826Z

## Decisão Lucas
O pós-grid é **depois de todos os produtos da coleção**.

## Regra obrigatória
Nenhum guia, bloco editorial pós-grid, FAQ ou conteúdo LKGOC secundário pode ser inserido:
- antes do grid;
- dentro do grid;
- depois de apenas parte dos produtos;
- baseado em `ProductGridContainer` se isso não comprovar o fim dos produtos;
- baseado em estimativa visual de screenshot.

O bloco pós-grid só pode começar após o último card/produto renderizado da coleção.

## QA obrigatório
Antes de PASS:
1. contar/identificar o último produto/card renderizado;
2. verificar que o guia/bloco pós-grid aparece depois dele no DOM e no scroll;
3. screenshot deve mostrar a sequência produto-final → guia;
4. se não houver essa prova, status `FAIL_POS_GRID_NOT_AFTER_ALL_PRODUCTS`.

## Consequência
Qualquer implementação que coloque o guia antes do fim de todos os produtos é FAIL, mesmo que o DOM tenha `ProductGridContainer` antes.
