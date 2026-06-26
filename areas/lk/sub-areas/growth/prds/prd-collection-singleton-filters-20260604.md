# PRD — Ocultar filtros singleton em coleções LK

Data: 2026-06-04
Superfície: Shopify theme / collections
Asset candidato: `sections/lk-collection.liquid`

## Problema

Em coleções como `/collections/new-balance-9060`, o sidebar/sheet de filtros mostra grupos como `Marca` e `Categoria` mesmo quando existe apenas uma opção possível. Exemplo observado no live: `Categoria` com 1 opção e `Marca` com 1 opção.

Isso polui a navegação e cria falsa affordance: se só há uma marca/categoria, não há decisão real de filtro.

## Objetivo

Esconder automaticamente qualquer grupo de filtro de lista que tenha apenas 1 opção e não esteja ativo, em desktop e mobile.

## Escopo

Incluído:
- Coleções Shopify renderizadas por `sections/lk-collection.liquid`.
- Desktop sidebar `.coll-sidebar`.
- Mobile filter sheet `.coll-filter-sheet`.
- Todos os filtros do tipo `list` com `filter.values.size <= 1` e `filter.active_values.size == 0`.
- Preservar filtros ativos para permitir remoção/limpar.
- Ajustar links de valores ativos para `value.url_to_remove`; valores inativos continuam com `value.url_to_add`.

Não incluído:
- Alteração de produtos, metafields, taxonomy, cor nativa Shopify, preço, estoque, coleção, menu ou apps.
- Production deploy sem aprovação separada depois do preview Dev.
- Reescrever layout completo dos filtros.

## Regra funcional

Para cada `filter` em `collection.filters`:

- Se `filter.type != 'list'`: renderizar normalmente.
- Se `filter.type == 'list'` e `filter.values.size <= 1` e `filter.active_values.size == 0`: não renderizar o grupo.
- Se o filtro está ativo (`active_values.size > 0`): renderizar o grupo mesmo com uma opção, para o usuário conseguir remover/limpar.

## Critérios de aceite

1. Em `/collections/new-balance-9060`, `Marca` e `Categoria` não aparecem quando têm só 1 opção e não estão ativos.
2. Filtros com múltiplas opções, como tamanho/disponibilidade/cor quando aplicável, continuam aparecendo.
3. Se o usuário entra com um filtro singleton ativo via URL, o grupo não some; ele permanece visível e/ou removível.
4. Desktop e mobile seguem a mesma lógica.
5. Links de filtros ativos apontam para `url_to_remove`, evitando chip ativo que não desliga no segundo clique.
6. Sem Liquid syntax error.
7. Production permanece intacto até aprovação explícita.

## Risco

- Pode esconder filtros singleton úteis em alguns casos raros. Mitigação: a regra só esconde quando não está ativo; o clear global permanece.
- O asset `lk-collection.liquid` é grande e já tem warnings visuais preexistentes; não tratar warnings antigos como bloqueio do patch, mas registrar.
- Shopify Asset API pode bater limite de 256 KB se o asset crescer; o patch é pequeno e não adiciona volume relevante.

## Rollback

- Dev: re-upload do backup `dev_before.liquid` antes do teste.
- Production futuro: se aprovado depois, backup `production_before.liquid` antes do write e rollback por re-upload do asset anterior.

## Plano de verificação

- Static readback do asset Dev após upload.
- Checar presença da regra singleton global no readback.
- Checar ausência do escopo antigo `collection.handle == 'new-balance-204l'`.
- QA público/autenticado no Dev preview para `/collections/new-balance-9060`:
  - desktop: labels dos filtros;
  - mobile sheet: labels dos filtros;
  - URL com filtro ativo: grupo ativo removível.

## Status atual

PRD escrito e patch candidato preparado localmente. Aguardando aprovação de Lucas para upload apenas no tema Dev/unpublished. Production não deve ser tocado nesta etapa.
